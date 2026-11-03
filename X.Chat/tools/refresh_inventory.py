"""Read-only source scan; write only the generated X.Chat source inventories."""
from pathlib import Path
from collections import defaultdict, Counter
from urllib.parse import unquote
import csv, json, re, hashlib

HUB = Path(__file__).resolve().parents[1]
VAULT = HUB.parent
PAPERS = Path('/Users/andres/projects/research/Paper_and_Presentations')
PROPOSAL = PAPERS / 'Andres_Fierro_Dissertation_Proposal'
MASTER = PAPERS / 'Tamu_masters_papers_and_docs/CSEM-Master-s-Dissertation-Template'
MAINVAULT = Path('/Users/andres/ObsidianVaults/MainVault')
OUT = HUB / '01_sources'
FILES = sorted(p for p in VAULT.rglob('*') if p.is_file() and HUB not in p.parents and not any(x.startswith('.') for x in p.relative_to(VAULT).parts))
BYNAME = defaultdict(list)
SHARED = Path('/Users/andres/Library/CloudStorage/Box-Box/VCU ACU Shared Research')
EXTERNAL_ROOTS = [SHARED / 'Design_Documentation', SHARED / 'Images from VCU for ANS']
EXTERNAL_BYNAME = defaultdict(list)
for root in EXTERNAL_ROOTS:
    if root.exists():
        for p in root.rglob('*'):
            if p.is_file() and not any(x.startswith('.') for x in p.relative_to(root).parts):
                EXTERNAL_BYNAME[p.name.casefold()].append(p)
for p in FILES:
    BYNAME[p.name.casefold()].append(p)
    if p.suffix == '.md':
        BYNAME[p.stem.casefold()].append(p)


def resolve(target, note):
    target = unquote(target)
    if not target:
        return 'same_note', [str(note)]
    candidates = [note.parent / target, VAULT / target]
    if target.startswith('MainVault/'):
        candidates.insert(0, MAINVAULT / target[len('MainVault/'):])
    if target.startswith('/'):
        candidates.insert(0, Path(target))
    for path in candidates:
        if path.is_file():
            return 'resolved', [str(path.resolve())]
        if not path.suffix and path.with_suffix('.md').is_file():
            return 'resolved', [str(path.with_suffix('.md').resolve())]
    matches = sorted(set(BYNAME[Path(target).name.casefold()]))
    if len(matches) == 1:
        return 'resolved_by_name', [str(matches[0])]
    if len(matches) > 1:
        return 'ambiguous', [str(p) for p in matches]
    external = sorted(set(EXTERNAL_BYNAME[Path(target).name.casefold()]))
    if len(external) == 1:
        return 'resolved_shared_by_name', [str(external[0])]
    if len(external) > 1:
        return 'ambiguous_shared', [str(p) for p in external]
    return 'unresolved_in_scanned_roots', []


def csvwrite(path, rows, fields):
    with path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


inventory = []
links = []
for p in FILES:
    inventory.append({'path': str(p.relative_to(VAULT)), 'extension': p.suffix.lower(), 'size_bytes': p.stat().st_size, 'role': 'source_note' if p.suffix == '.md' else 'attachment_or_source_asset', 'content_review': 'inventory_only_not_proof_of_reading'})
    if p.suffix != '.md':
        continue
    for number, line in enumerate(p.read_text().splitlines(), 1):
        for match in re.finditer(r'(!?)\[\[([^\]]+)\]\]', line):
            raw = match.group(0)
            target = match.group(2).split('|', 1)[0].split('#', 1)[0]
            status, paths = resolve(target, p)
            links.append({'source_note': str(p.relative_to(VAULT)), 'source_line': number, 'kind': 'embed' if match.group(1) else 'wikilink', 'original_link': raw, 'target': target, 'status': status, 'resolved_paths': json.dumps(paths, ensure_ascii=False), 'content_inspected': 'no'})
        for match in re.finditer(r'!\[[^\]]*\]\(([^)]+)\)', line):
            target = match.group(1)
            if target.startswith('data:image/'):
                links.append({'source_note': str(p.relative_to(VAULT)), 'source_line': number, 'kind': 'embedded_image', 'original_link': '[inline data image retained in original note]', 'target': '[inline data image]', 'status': 'inline_in_source', 'resolved_paths': '[]', 'content_inspected': 'no'})
            elif not target.startswith(('http:', 'https:')):
                status, paths = resolve(target.split('#', 1)[0], p)
                links.append({'source_note': str(p.relative_to(VAULT)), 'source_line': number, 'kind': 'markdown_image', 'original_link': match.group(0), 'target': target, 'status': status, 'resolved_paths': json.dumps(paths, ensure_ascii=False), 'content_inspected': 'no'})

csvwrite(OUT / 'resource_inventory.csv', inventory, ['path', 'extension', 'size_bytes', 'role', 'content_review'])
csvwrite(OUT / 'obsidian_links.csv', links, ['source_note', 'source_line', 'kind', 'original_link', 'target', 'status', 'resolved_paths', 'content_inspected'])
summary = {'date': '2026-11-02', 'source_files': len(FILES), 'source_markdown_notes': sum(p.suffix == '.md' for p in FILES), 'link_occurrences': len(links), 'link_statuses': dict(Counter(x['status'] for x in links)), 'scan_scope': 'Original Trident_FlowLoop_Notes files excluding X.Chat and hidden directories; explicit MainVault-prefixed targets checked directly. Unresolved basenames checked in shared Design_Documentation and Images from VCU for ANS. No global vault/Box filename search.', 'external_lookup_roots': [str(p) for p in EXTERNAL_ROOTS], 'warning': 'Unresolved means not found by this scoped resolver, not proof of a broken link, missing source or inaccessible remote file. Image contents and PDF page fragments were not validated.'}
(OUT / 'inventory_summary.json').write_text(json.dumps(summary, indent=2) + '\n')

text = '''# Photo and drawing routes

- Original embeds and page/rectangle fragments remain in their source notes; no images were moved or edited.
- The link audit records availability, not scientific geometry authority or figure quality. Image/PDF contents were not inspected.
- `unresolved_in_scanned_roots` means a target was not located in the scan; external vault/Box targets may still exist. Resolve before selecting a figure.
- A Rev9 subsection in the sensor note embeds a Rev8 drawing; preserve the revision label and select the appropriate asset explicitly.
- For each final figure record facility, configuration/revision, capture/run date, original link, intended caption, claim supported and author selection.

## Recommended source routes

'''
for rel, purpose in [('1. Setup and Geometry/1.1.1 Geometry pics.md', 'Facility geometry and revision candidates'), ('1. Setup and Geometry/1.1.0 Geometry notes.md', 'Assembly, tanks and revision-qualified drawings'), ('1. Setup and Geometry/1.1.2 Sensors.md', 'Channel positions and ACU/VCU schematics'), ('1. Setup and Geometry/1.1.0 Heaters and coolers.md', 'Heater placement and exchanger photos'), ('1. Setup and Geometry/1.2 Main Material Props.md', 'Insulation/product evidence'), ('A. Appendix/A.1 Interesting Pictures and drawing.md', 'Additional photograph/drawing candidates')]:
    text += f'- [{purpose}](<../../{rel}>).\n'
text += '\n## Master’s result figures for the early feasibility section\n\n'
with (MASTER / 'evidence/FIGURE_SOURCE_MANIFEST.csv').open() as f:
    for row in csv.DictReader(f):
        if row['figure_id'] in ['F09', 'F10', 'F11']:
            asset = MASTER / row['manuscript_output']
            text += f"- {row['figure_id']}: [{asset.name}](<{asset}>) — use the [figure manifest](<{MASTER / 'evidence/FIGURE_SOURCE_MANIFEST.csv'}>) for input rows/hashes; retrospective master’s evidence, not ACU/VCU validation.\n"
text += '\n## Availability summary\n\n'
for key, count in summary['link_statuses'].items():
    text += f'- `{key}`: {count} link occurrences.\n'
text += '\n- Complete original link text, parent note and line locator: [link audit](obsidian_links.csv).\n- File metadata: [resource inventory](resource_inventory.csv); [scan scope](inventory_summary.json).\n'
(OUT / 'FIGURE_ROUTES.md').write_text(text)
from obsidian_links import normalize
normalize()  # Generated notes must use the vault's internal aliases, never OS paths.
print(json.dumps(summary, indent=2))
