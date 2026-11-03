"""Normalize authored X.Chat links for Obsidian and validate existing targets.

Never follow repository symlinks while scanning or modifying notes.
"""
from pathlib import Path
from urllib.parse import unquote, urlparse
import argparse, os, re, json

HUB = Path(__file__).resolve().parents[1]
NOTES = HUB.parent
BOX = Path.home() / 'ObsidianVaults/MainVault/Box'
PAPERS_ALIAS = HUB / '80_repository_links/Papers'
NOTES_VAULT = 'MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes'
STAGED = HUB / '03_proposal/2026-11-02/archive/staged'
PROPOSAL = PAPERS_ALIAS / 'Andres_Fierro_Dissertation_Proposal'
LINK = re.compile(r'(?<!!)\[([^\]\n]+)\]\((?:<([^>]+)>|([^\s)]+))\)')


def notes(include_archives=True):
    for root, dirs, files in os.walk(HUB, followlinks=False):
        dirs[:] = [d for d in dirs if not (Path(root) / d).is_symlink() and (include_archives or d != 'archive')]
        for name in files:
            p = Path(root) / name
            if p.suffix == '.md' and not p.is_symlink():
                yield p


def vault_name(path):
    resolved = path.resolve()
    try:
        return NOTES_VAULT + '/' + str(resolved.relative_to(NOTES.resolve()))
    except ValueError:
        pass
    try:
        return 'MainVault/Box/' + str(resolved.relative_to(BOX.resolve()))
    except ValueError:
        pass
    if PAPERS_ALIAS.is_symlink():
        try:
            rel = resolved.relative_to(PAPERS_ALIAS.resolve())
            return NOTES_VAULT + '/X.Chat/80_repository_links/Papers/' + str(rel)
        except ValueError:
            pass
    return None


def resolve(note, raw):
    if raw.startswith('file:'):
        target = unquote(urlparse(raw).path)
        fragment = ''
    else:
        path, sep, fragment = raw.partition('#')
        target = unquote(path)
        fragment = ('#' + unquote(fragment)) if sep else ''
    p = Path(target)
    if not p.is_absolute():
        candidates = [note.parent / p]
        if STAGED in note.parents:
            candidates.append(PROPOSAL / note.parent.relative_to(STAGED) / p)
        p = next((x for x in candidates if x.exists()), candidates[0])
    return p, fragment


def normalize():
    changes = []
    unresolved = []
    for note in notes(include_archives=False):
        original = note.read_text()
        out = []
        fenced = False
        count = 0
        for line in original.splitlines(keepends=True):
            if re.match(r'^\s*(```|~~~)', line):
                fenced = not fenced
            if fenced:
                out.append(line)
                continue
            table = line.lstrip().startswith('|')
            def replace(m):
                nonlocal count
                label, raw = m[1], m[2] or m[3]
                if re.match(r'^(https?|obsidian|app|plugin|mailto):', raw):
                    return m[0]
                if raw.startswith('#'):
                    return m[0]
                p, fragment = resolve(note, raw)
                alias = vault_name(p)
                if p.is_dir():
                    # Folder wikilinks can create unwanted notes; only link real files.
                    if (p / 'README.md').is_file():
                        p = p / 'README.md'
                        alias = vault_name(p)
                    else:
                        count += 1
                        return label + ' — `' + (alias or str(p)) + '/` (folder)'
                if not p.is_file() or alias is None:
                    unresolved.append({'note': str(note.relative_to(HUB)), 'target': raw})
                    count += 1
                    return label + ' — `' + raw + '` (unresolved source pointer)'
                count += 1
                # Escape alias separators in Markdown tables.
                separator = r'\|' if table else '|'
                return '[[' + alias + fragment + separator + label + ']]'
            out.append(LINK.sub(replace, line))
        new = ''.join(out)
        if new != original:
            note.write_text(new)
            changes.append({'note': str(note.relative_to(HUB)), 'converted': count})
    return {'changed_notes': changes, 'unresolved_links_made_nonclickable': unresolved}


def validate(vault_root):
    missing = []
    absolute = []
    count = 0
    for note in notes():
        fenced = False
        for lineno, line in enumerate(note.read_text().splitlines(), 1):
            if re.match(r'^\s*(```|~~~)', line):
                fenced = not fenced
            if fenced:
                continue
            for m in LINK.finditer(line):
                raw = m[2] or m[3]
                if raw.startswith(('/Users/', 'file:')):
                    absolute.append({'note': str(note.relative_to(HUB)), 'line': lineno, 'target': raw})
            for m in re.finditer(r'(?<!!)\[\[([^\]]+)\]\]', line):
                target = m[1].replace(r'\|', '|').split('|', 1)[0].split('#', 1)[0]
                p = vault_root / target
                if not p.is_file():
                    missing.append({'note': str(note.relative_to(HUB)), 'line': lineno, 'target': target})
                count += 1
    return {'vault_root_checked': str(vault_root), 'wikilinks_checked': count, 'missing_or_folder_targets': missing, 'unsafe_os_path_markdown_links': absolute, 'scan_follows_symlinks': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--normalize', action='store_true')
    parser.add_argument('--vault-root', type=Path, default=Path.home() / 'ObsidianVaults')
    args = parser.parse_args()
    result = normalize() if args.normalize else {}
    result['validation'] = validate(args.vault_root)
    print(json.dumps(result, indent=2))
    raise SystemExit(bool(result['validation']['missing_or_folder_targets'] or result['validation']['unsafe_os_path_markdown_links']))
