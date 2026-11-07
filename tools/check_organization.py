#!/usr/bin/env python3
"""Read-only notes navigation checks; never follow repository aliases or archives."""
import argparse
from collections import Counter
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/'
LAYERS = ('00_navigation', '01_sources', '02_synthesis', '03_proposal',
          '04_decisions', '05_handoffs', '06_hpc_exchange', '80_repository_links', '90_templates', 'tools')
MANAGED = ['PROJECT_MAP.md', 'STATUS.md', 'tools/README.md'] + [f'X.Chat/{x}/README.md' for x in
          ('00_navigation', '01_sources', '02_synthesis', '04_decisions', '05_handoffs', '90_templates', 'tools')]
MANAGED += ['X.Chat/00_navigation/ORGANIZATION.md', 'X.Chat/02_synthesis/studies/README.md']
MANAGED += [f'X.Chat/00_navigation/agents/{name}.md' for name in ('README', 'SHARED', 'MAC', 'TACC')]
WIKI = re.compile(r'\[\[([^\]\n]+)\]\]')
MARKDOWN = re.compile(r'(?<!!)\[[^\]\n]+\]\((?:<([^>]+)>|([^\s)]+))\)')


def active_markdown():
    for top in (ROOT, ROOT / 'X.Chat'):
        if top == ROOT:
            yield from (p for p in top.glob('*.md') if not p.is_symlink())
            continue
        for directory, dirs, files in os.walk(top, followlinks=False):
            base = Path(directory)
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('archive', 'build', 'past')
                       and not (base / d).is_symlink()
                       and not (base == ROOT / 'X.Chat/03_proposal' and re.fullmatch(r'\d{4}-\d{2}-\d{2}', d))]
            for name in files:
                p = base / name
                if p.suffix == '.md' and not p.is_symlink():
                    yield p


def target_state(note, raw, wiki):
    raw = unquote(raw.replace('\\|', '|').split('|')[0]).strip()
    target = raw.split('#')[0]
    if not target or re.match(r'^(https?|mailto|obsidian|app|plugin):', target):
        return 'external_url_or_anchor'
    if target.startswith(PREFIX):
        path = ROOT / target[len(PREFIX):]
    elif target.startswith(('MainVault/', '/')):
        return 'external_machine_pointer'
    else:
        path = note.parent / target
    path = Path(os.path.normpath(path))
    try:
        relative = path.absolute().relative_to(ROOT)
    except ValueError:
        return 'external_owner_pointer'
    parts = relative.parts
    if parts[:2] == ('X.Chat', '80_repository_links') and len(parts) > 2:
        return 'external_alias_pointer'
    if parts[:3] == ('X.Chat', '03_proposal', 'current'):
        return 'external_alias_pointer'
    if any((ROOT.joinpath(*parts[:i])).is_symlink() for i in range(1, len(parts) + 1)):
        return 'preserved_symlink_pointer'
    if path.is_file():
        return 'resolved_local'
    if wiki and not path.suffix and path.with_suffix('.md').is_file():
        return 'resolved_local'
    if path.is_dir():
        return 'folder_target_use_readme'
    return 'missing_local'


def check(all_active=False):
    errors = []
    for name in LAYERS:
        p = ROOT / 'X.Chat' / name
        if not p.is_dir() or p.is_symlink() or not (p / 'README.md').is_file():
            errors.append({'path': str(p.relative_to(ROOT)), 'problem': 'missing owned folder/index'})
    root_files = {p.name for p in (ROOT / 'X.Chat').iterdir()
                  if p.is_file() and not p.is_symlink() and p.name != '.DS_Store'}
    for name in sorted(root_files - {'README.md', 'AGENTS.md'}):
        errors.append({'path': 'X.Chat/' + name, 'problem': 'loose file needs an owning layer or documented exception'})
    for rel in MANAGED:
        path = ROOT / rel
        if not path.is_file():
            errors.append({'path': rel, 'problem': 'missing maintained route'})
            continue
        text = path.read_text()
        header = text.split('---', 2)[1] if text.startswith('---\n') and text.count('---') >= 2 else ''
        for key in ('title', 'status', 'owner', 'updated', 'tags'):
            if not re.search(r'^' + key + r':\s*\S', header, re.M):
                errors.append({'path': rel, 'problem': 'missing metadata: ' + key})
    states = Counter()
    local_issues = []
    files = list(active_markdown()) if all_active else [ROOT / p for p in MANAGED] + [ROOT / 'X.Chat/README.md']
    for path in sorted(set(files)):
        if not path.is_file():
            continue
        fenced = False
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if re.match(r'^\s*(```|~~~)', line):
                fenced = not fenced
                continue
            if fenced:
                continue
            targets = [(m[1], True) for m in WIKI.finditer(line)]
            targets += [(m[1] or m[2], False) for m in MARKDOWN.finditer(line)]
            for raw, wiki in targets:
                state = target_state(path, raw, wiki)
                states[state] += 1
                if state in ('missing_local', 'folder_target_use_readme'):
                    issue = {'path': str(path.relative_to(ROOT)), 'line': number, 'target': raw, 'problem': state}
                    local_issues.append(issue)
                    if not all_active or str(path.relative_to(ROOT)) in MANAGED:
                        errors.append(issue)
    return {'status': 'passed' if not errors else 'failed', 'scope': 'all-active report' if all_active else 'maintained navigation',
            'documents_checked': len(set(files)), 'link_states': dict(states), 'errors': errors,
            'broader_local_link_debt': local_issues if all_active else [],
            'limits': 'External machine/library pointers are classified, not verified; aliases/archives are not traversed. No image/CAD content inspected.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--all-active', action='store_true')
    parser.add_argument('--json-out', type=Path)
    args = parser.parse_args()
    result = check(args.all_active)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(result, indent=2) + '\n')
    concise = {k: v for k, v in result.items() if k not in ('errors', 'broader_local_link_debt')}
    concise.update(error_count=len(result['errors']), broader_local_link_debt_count=len(result['broader_local_link_debt']))
    print(json.dumps(concise))
    for error in result['errors'][:8]:
        print(json.dumps(error))
    if result['errors']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
