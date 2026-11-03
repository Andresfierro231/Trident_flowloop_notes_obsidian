"""Metadata-only discovery inventory: no source content reading, renames or symlink recursion."""
from pathlib import Path
import argparse,csv,os,collections,json
p=argparse.ArgumentParser(description=__doc__)
p.add_argument("--root",type=Path,default=Path.home()/"ObsidianVaults/MainVault/Box/books/research")
p.add_argument("--output",type=Path,default=Path(__file__).resolve().parents[1]/"01_sources/box_literature_inventory.csv")
a=p.parse_args();root=a.root.expanduser().resolve(strict=True);rows=[]
for here,dirs,files in os.walk(root,followlinks=False):
 dirs[:]=sorted(d for d in dirs if not (Path(here)/d).is_symlink() and not d.startswith("."))
 for name in sorted(files):
  f=Path(here)/name
  if name.startswith(".") or f.is_symlink():continue
  rel=f.relative_to(root)
  rows.append(dict(relative_path=str(rel),filename=name,extension=f.suffix.lower(),bytes=f.stat().st_size,vault_target="MainVault/Box/books/research/"+str(rel),reading_status="not_assessed_by_inventory"))
a.output.parent.mkdir(parents=True,exist_ok=True)
with a.output.open("w",newline="") as out:
 w=csv.DictWriter(out,fieldnames=["relative_path","filename","extension","bytes","vault_target","reading_status"],lineterminator="\n")
 w.writeheader();w.writerows(rows)
print(json.dumps({"files":len(rows),"extensions":dict(collections.Counter(r["extension"] for r in rows)),"source_bytes_read":False}))
