#!/usr/bin/env python3
"""Resolve current or recorded historical reference paths without changing sources.
Usage: python3 tools/resolve_reference_path.py reference/MANIFEST.sha256 --json
"""
from pathlib import Path
from urllib.parse import unquote
import argparse,hashlib,json,os
ROOT=Path(__file__).resolve().parents[1]
CANONICAL=ROOT/'X.Reference'
RECORD=ROOT/'X.Chat/01_sources/reference_migration/2026-11-06'

def resolve_reference_path(value,base=None):
 pin=json.loads((RECORD/'MOVE_MANIFEST.json').read_text())
 original=Path(pin['source']);old_notes=original.parent/pin['compatibility_target']
 prefixes=[str(CANONICAL),str(ROOT/'reference'),str(original),str(old_notes),'MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Reference','MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/reference','X.Reference','reference']
 raw=unquote(str(value)).strip();candidate=raw
 if base is not None and not Path(raw).is_absolute():candidate=os.path.abspath(Path(base)/raw)
 rel=None
 for prefix in sorted(set(prefixes),key=len,reverse=True):
  if candidate==prefix or candidate.startswith(prefix+'/'):
   rel=candidate[len(prefix):].lstrip('/');break
 if rel is None:
  if Path(candidate).is_absolute():raise ValueError('Path does not belong to a recorded reference root')
  rel=candidate
 target=CANONICAL/rel;kind='canonical_or_prefix_relocation'
 if not target.exists():
  routes=json.loads((CANONICAL/'manifest_routes.json').read_text())['routes']
  if rel in routes:target=CANONICAL/routes[rel];kind='issued_bootstrap_name_relocation'
 if not target.resolve().is_relative_to(CANONICAL.resolve()):raise ValueError('Reference target escapes the source collection')
 if not target.exists():raise FileNotFoundError(str(target))
 return {'requested':str(value),'resolved':str(target.resolve()),'route':kind,'is_file':target.is_file()}

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('path');p.add_argument('--from-dir',type=Path);p.add_argument('--json',action='store_true');p.add_argument('--sha256');a=p.parse_args()
 try:
  row=resolve_reference_path(a.path,a.from_dir)
  if a.sha256:
   h=hashlib.sha256()
   with Path(row['resolved']).open('rb') as f:
    for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
   row['sha256']=h.hexdigest()
   if row['sha256']!=a.sha256:raise ValueError('Resolved source does not match the requested digest')
  print(json.dumps(row) if a.json else row['resolved'])
 except (ValueError,OSError,KeyError) as e:p.exit(1,str(e)+'\n')
if __name__=='__main__':main()
