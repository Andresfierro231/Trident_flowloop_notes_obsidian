#!/usr/bin/env python3
"""Read-only integration check of actual reference routes and current local links."""
from pathlib import Path
import importlib.util,json,re,time
D=Path(__file__).resolve().parent
N=next(p for p in D.parents if (p/'tools/resolve_reference_path.py').is_file())
spec=importlib.util.spec_from_file_location('reference_routes',N/'tools/resolve_reference_path.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
x=json.loads((D.parent/'MOVE_MANIFEST.json').read_text());X=N/'X.Reference';start=time.monotonic();checked=0
# Each original filename is exercised through both recorded roots and the current root.
old_m=Path(x['source']);old_n=old_m.parent/x['compatibility_target']
for row in x['files']:
 rel=row['relative_path'];target=(X/rel).resolve()
 for path in [X/rel,old_m/rel,old_n/rel]:
  assert Path(mod.resolve_reference_path(str(path))['resolved'])==target,(rel,path);checked+=1
routes=json.loads((X/'manifest_routes.json').read_text())['routes']
for old,rel in routes.items():
 assert Path(mod.resolve_reference_path('reference/'+old)['resolved'])==(X/rel).resolve()
for bad in ['reference/../../AGENTS.md','reference/__missing_reference__']:
 try:mod.resolve_reference_path(bad)
 except (ValueError,OSError):pass
 else:raise AssertionError('Invalid source path accepted: '+bad)
prefix='MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/'
external_aliases=0
files=[N/p for p in ['README.md','AGENTS.md','PROJECT_MAP.md','STATUS.md','tools/README.md','X.Reference/INDEX.md','X.Chat/01_sources/REFERENCE_INPUTS.md','X.Chat/02_synthesis/MOSER_PROPOSAL_THROUGHLINE.md','X.Chat/00_navigation/LOCATIONS.md','X.Chat/01_sources/reference_migration/README.md']]+[D/'README.md'];links=0
for f in files:
 s=re.sub(r'```.*?```','',f.read_text(),flags=re.S);s=re.sub(r'`[^`\n]+`','',s)
 for raw in re.findall(r'\[\[([^\]\n]+)\]\]',s):
  target=raw.replace('\\|','|').split('|')[0].split('#')[0]
  if target.startswith(prefix):
   relative=target[len(prefix):]
   if relative.startswith(('X.Chat/80_repository_links/','X.Chat/03_proposal/current/')):
    external_aliases+=1;continue
   assert (N/relative).exists(),(f,target);links+=1
 for angle,normal in re.findall(r'(?<!!)\[[^\]\n]+\]\((?:<([^>]+)>|([^\s)]+))\)',s):
  target=angle or normal
  if target.startswith(('http:','https:','#')):continue
  target=target.split('#')[0]
  if target:assert (f.parent/target).exists(),(f,target);links+=1
print(json.dumps({'status':'passed','original_source_paths':checked,'bootstrap_filename_routes':len(routes),'invalid_paths_rejected':2,'current_links_checked':links,'external_machine_aliases_classified':external_aliases,'elapsed_s':round(time.monotonic()-start,3),'visual_inspection':False}))
