#!/usr/bin/env python3
"""Offline Trident skill catalog, budget checks and safe per-checkout discovery links."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys

PACK = Path(__file__).resolve().parents[1]
NOTES = PACK.parents[1]
# Character ceilings bound text growth; they do not measure billed model tokens.
MAX_DESCRIPTION = 160
MAX_DESCRIPTIONS = 1400
MAX_SKILL = 2600
MAX_CATALOG = 3200


def entries(pack=PACK):
    result = []
    for path in sorted(pack.glob('*/SKILL.md')):
        raw = path.read_text(encoding='utf-8')
        if not raw.startswith('---\n') or '\n---\n' not in raw[4:]:
            raise ValueError(f'{path}: missing YAML frontmatter')
        front, body = raw[4:].split('\n---\n', 1)
        fields = dict(line.split(': ', 1) for line in front.splitlines() if ': ' in line)
        name = fields.get('name', '')
        description = fields.get('description', '')
        # Keep catalog parsing dependency-free. New descriptions use one quoted line.
        try:
            description = json.loads(description)
        except (ValueError, TypeError) as error:
            raise ValueError(f'{path}: description must be one JSON-quoted YAML string') from error
        if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64 or name != path.parent.name:
            raise ValueError(f'{path}: name must match the hyphenated folder name')
        if not isinstance(description, str) or not description.strip() or '\n' in description:
            raise ValueError(f'{path}: invalid description')
        if len(description) > MAX_DESCRIPTION or len(raw) > MAX_SKILL:
            raise ValueError(f'{path}: description/body budget exceeded')
        if not body.strip() or '[TODO' in raw:
            raise ValueError(f'{path}: empty or unfinished skill')
        for target in re.findall(r'\]\(([^)]+)\)', body):
            if '://' not in target and not target.startswith('#'):
                destination = target.split('#', 1)[0]
                if destination and not (path.parent / destination).exists():
                    raise ValueError(f'{path}: broken reference {target}')
        result.append({'name': name, 'description': description,
                       'path': '.agents/skills/' + name + '/SKILL.md',
                       'characters': len(raw)})
    if not result or len({item['name'] for item in result}) != len(result):
        raise ValueError('Skill pack must contain unique, nonempty entries')
    if sum(len(item['description']) for item in result) > MAX_DESCRIPTIONS:
        raise ValueError('Combined description budget exceeded; narrow the catalog before expanding')
    return result


def render(items):
    header = '''---
title: Trident on-demand skills
status: maintained
owner: notes skill pack
updated: 2026-11-04
tags: [project/trident, doc/index, domain/agent_coordination]
---

# Skill catalog

Use native skill names/descriptions first. This is the fallback index when they
are unavailable. At task start or a scope change, select only the relevant skill;
routine work can need none. Read its `SKILL.md`, not the whole pack. Load another
only for a distinct required subtask. Existing owner instructions and user scope apply.

| Skill | When useful |
|---|---|
'''
    rows = '\n'.join(f"| [{item['name']}]({item['path']}) | {item['description']} |" for item in items)
    return header + rows + '''

Optional offline lookup: `python3 .agents/skills/_support/catalog.py list --match equation`.
[Maintenance, setup and source provenance](.agents/skills/_support/README.md)
are needed only when adding/updating skills or setting up another checkout.
'''


def validate(pack=PACK, catalog=None):
    items = entries(pack)
    expected = render(items)
    if len(expected) > MAX_CATALOG:
        raise ValueError('Catalog budget exceeded')
    if catalog is not None and catalog.read_text(encoding='utf-8') != expected:
        raise ValueError('Catalog differs from skills; run the explicit render command')
    sources = json.loads((pack / '_support/sources.json').read_text(encoding='utf-8'))
    if sources['pack_version'] != 1:
        raise ValueError('Unsupported source record version')
    for source in sources['sources']:
        if not re.fullmatch(r'[0-9a-f]{40}', source['revision']):
            raise ValueError('Upstream source revision is not pinned')
        for file in source['files']:
            if not re.fullmatch(r'[0-9a-f]{64}', file['sha256']):
                raise ValueError('Missing source hash')
        notice = source['upstream_license'].get('local_notice')
        if notice:
            notice_path = pack / '_support' / notice
            if not notice_path.is_file():
                raise ValueError('Missing attribution notice')
            if hashlib.sha256(notice_path.read_bytes()).hexdigest() != source['upstream_license']['sha256']:
                raise ValueError('Attribution notice differs from its pinned source')
    covered = set(sources['original_trident_skills'])
    for source in sources['sources']:
        covered.update(name for name in source['local_skills'] if name != 'all')
    if covered != {item['name'] for item in items}:
        raise ValueError('Every skill needs source attribution or original-Trident classification')
    if catalog is not None:
        for destination in re.findall(r'\]\(([^)]+)\)', expected):
            if '://' not in destination and not (catalog.parent/destination).exists():
                raise ValueError('Broken catalog link: ' + destination)
    discovery = '\n'.join(item['name'] + ' ' + item['description'] + ' ' + str(pack/item['name']/'SKILL.md') for item in items)
    return {'status': 'passed', 'skills': len(items),
            'description_characters': sum(len(item['description']) for item in items),
            'discovery_characters_including_paths': len(discovery),
            'discovery_tokens_rough_estimate': math.ceil(len(discovery)/4),
            'catalog_characters': len(expected),
            'largest_skill_characters': max(item['characters'] for item in items),
            'limits': 'Tokens use characters/4 only; actual tokenizer, host overhead and billing vary. No model calls or network.'}


def link_checkout(target, apply=False, pack=PACK, catalog=None):
    """Preflight every destination, then create relative links; never replace content."""
    target = target.expanduser().resolve()
    pack = pack.resolve()
    catalog = (catalog or pack.parents[1]/'SKILLS.md').resolve()
    if target in (Path('/'), Path.home().resolve()):
        raise ValueError('Use a project checkout, not the filesystem or user-home root')
    if not target.is_dir() or not ((target/'AGENTS.md').is_file() or (target/'.git').exists()):
        raise ValueError('Target must be an existing project with AGENTS.md or .git')
    if not pack.is_dir() or not catalog.is_file():
        raise ValueError('Canonical pack/catalog unavailable')
    # Do not inject a second copy below an existing discovery root in one Git repo.
    for ancestor in [target, *target.parents]:
        if ancestor != target and (ancestor/'.agents/skills').resolve() == pack:
            return {'status': 'inherited', 'target': str(target), 'discovery_root': str(ancestor)}
        if (ancestor/'.git').exists():
            break
    planned = []
    for source, destination in [(pack, target/'.agents/skills'), (catalog, target/'SKILLS.md')]:
        if destination == source:
            continue
        if os.path.lexists(destination):
            if destination.is_symlink() and destination.resolve() == source:
                continue
            raise ValueError(f'Refusing to replace existing path: {destination}')
        planned.append((source, destination))
    if apply:
        made = []
        try:
            for source, destination in planned:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.symlink_to(os.path.relpath(source, destination.parent))
                made.append(destination)
        except OSError:
            # Remove only links created by this invocation; never existing user content.
            for destination in reversed(made):
                destination.unlink()
            raise
    return {'status': 'linked' if apply and planned else 'unchanged' if not planned else 'dry_run',
            'target': str(target), 'links': [str(destination) for _, destination in planned]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='command', required=True)
    listing = commands.add_parser('list', help='Metadata only; no skill bodies in output')
    listing.add_argument('--match', default='', help='Literal name/description substring, not semantic classification')
    commands.add_parser('check', help='Offline structure, provenance, links and text budgets')
    commands.add_parser('render', help='Explicitly regenerate notes SKILLS.md')
    linking = commands.add_parser('link', help='Plan project-local aliases; requires --apply to write')
    linking.add_argument('--target', required=True, type=Path)
    linking.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    try:
        if args.command == 'list':
            match = args.match.casefold()
            items = entries()
            print(json.dumps([dict(name=x['name'], when=x['description'], path=x['path']) for x in items
                              if match in (x['name']+' '+x['description']).casefold()], indent=2))
        elif args.command == 'render':
            items = entries()
            rendered = render(items)
            if len(rendered) > MAX_CATALOG:
                raise ValueError('Catalog budget exceeded')
            (NOTES/'SKILLS.md').write_text(rendered, encoding='utf-8')
            print(json.dumps({'status':'rendered', 'skills':len(items)}))
        elif args.command == 'check':
            print(json.dumps(validate(catalog=NOTES/'SKILLS.md')))
        else:
            validate(catalog=NOTES/'SKILLS.md')
            print(json.dumps(link_checkout(args.target, args.apply)))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'status':'error', 'reason':str(error)}), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
