#!/usr/bin/env python3
"""Verify X.Reference or move an explicitly supplied reference tree into it.
Dry run: python3 tools/relocate_reference_inputs.py --source /verified/initiative/reference
Apply: same command with --apply. Verify later: --check (works after local Git pull).
No image/CAD/archive interpretation, network transfer or scientific processing.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,os,time
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'X.Reference'
RECORD=ROOT/'X.Chat/01_sources/reference_migration/2026-11-06'
MANIFEST=RECORD/'MOVE_MANIFEST.json'
def digest(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def inventory(root,workers):
 files=[]
 for base,dirs,names in os.walk(root,followlinks=False):
  for d in dirs:
   if (Path(base)/d).is_symlink() or d=='.git':raise ValueError('Nested repository or directory symlink requires explicit reconciliation')
  for name in names:
   p=Path(base)/name
   if p.is_symlink():raise ValueError('Source symlink requires explicit reconciliation: '+str(p))
   files.append(p)
 def row(p):return {'relative_path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':digest(p)}
 with ThreadPoolExecutor(max_workers=workers) as pool:rows=list(pool.map(row,sorted(files)))
 return rows

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--source',type=Path);ap.add_argument('--apply',action='store_true');ap.add_argument('--check',action='store_true');ap.add_argument('--workers',type=int,default=4);args=ap.parse_args();start=time.monotonic()
 affinity=len(os.sched_getaffinity(0)) if hasattr(os,'sched_getaffinity') else (os.cpu_count() or 1)
 workers=max(1,min(args.workers,affinity))
 if args.check:
  pin=json.loads(MANIFEST.read_text());actual=inventory(DEST,workers)
  expected={x['relative_path']:x for x in pin['files']}; received={x['relative_path']:x for x in actual}
  assert all(received.get(k)==v for k,v in expected.items()),'An original reference is missing or changed'
  added=sorted(set(received)-set(expected))
  result={'status':'passed','files':len(expected),'additional_files':len(added),'bytes':sum(x['bytes'] for x in pin['files']),'workers':workers,'elapsed_s':round(time.monotonic()-start,3),'content':'all original bytes preserved','visual_or_scientific_inspection':False}
  print(json.dumps(result));return
 if args.source is None:ap.error('--source is required for a dry run or move')
 source=args.source.absolute()
 if not source.is_dir() or source.is_symlink():ap.error('Source must be an existing real directory, not an alias')
 if DEST.exists() or DEST.is_symlink():ap.error('Destination already exists; no merge or overwrite is permitted')
 if source==ROOT or source.is_relative_to(ROOT) or ROOT.is_relative_to(source):ap.error('Source/destination roots must be disjoint')
 rows=inventory(source,workers)
 if any(x['bytes']>=100*1024*1024 for x in rows):ap.error('A file exceeds the regular Git blob limit; reconcile before moving')
 plan={'schema':1,'date':'2026-11-06','source':str(source),'destination_relative_to_notes':'X.Reference','compatibility_target':os.path.relpath(DEST,source.parent),'files':rows,'workers':workers,'total_bytes':sum(x['bytes'] for x in rows),'reading_depth':'filenames/bytes/SHA256 only; no image, native CAD, archive contents or source-paper interpretation'}
 RECORD.mkdir(parents=True,exist_ok=True)
 if not args.apply:
  (RECORD/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n');print(json.dumps({'mode':'dry-run','files':len(rows),'bytes':plan['total_bytes'],'destination':str(DEST),'workers':workers}));return
 # Atomic same-filesystem rename; fail rather than introduce a partial cross-device copy.
 os.rename(source,DEST)
 source.symlink_to(plan['compatibility_target'],target_is_directory=True)
 actual=inventory(DEST,workers)
 assert rows==actual,'Post-move content differs; preserve all files and investigate before publishing'
 assert source.resolve()==DEST.resolve()
 plan['status']='moved_and_verified';plan['elapsed_s']=round(time.monotonic()-start,3)
 MANIFEST.write_text(json.dumps(plan,indent=2)+'\n')
 print(json.dumps({'status':plan['status'],'files':len(rows),'bytes':plan['total_bytes'],'old_path_is_compatibility_symlink':True,'elapsed_s':plan['elapsed_s']}))
if __name__=='__main__':main()
