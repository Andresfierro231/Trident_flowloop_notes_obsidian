from cad_model import *
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
import json
sh,defs=load();rows=[]
for path in sh:
 if 'Surface_Thermoc' not in defs[path]:continue
 results=[]
 for mp in sh:
  if not defs[mp].startswith('MSRloop'):continue
  dis=BRepExtrema_DistShapeShape(sh[path].wrapped,sh[mp].wrapped);dis.Perform();assert dis.IsDone()
  results.append({'path':path,'pipe_path':mp,'gap_mm':dis.Value(),'solutions':[{'sensor_xyz_mm':xyz(dis.PointOnShape1(i)),'pipe_xyz_mm':xyz(dis.PointOnShape2(i))} for i in range(1,dis.NbSolution()+1)]})
 best=min(results,key=lambda r:r['gap_mm']);rows.append(best);print(path,best['gap_mm'],best['solutions'],flush=True)
(R/'data/surface_contact_solutions.json').write_text(json.dumps(rows,indent=2))
