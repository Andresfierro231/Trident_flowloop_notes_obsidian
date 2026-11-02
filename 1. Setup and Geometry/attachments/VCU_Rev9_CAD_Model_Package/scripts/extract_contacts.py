from cad_model import *
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
import json, numpy as np
sh,defs=load();d=json.load(open(R/'raw/rev9_inventory.json'));rows=d['records'];main=[r for r in rows if r['definition'].startswith('MSRloop')];shell=next(r for r in rows if r['definition']=='3in3ftCutSS_44635K443')
for r in rows:
 if 'Surface_Thermoc' not in r['definition']:continue
 print('contact',r['path'],flush=True);choices=[]
 for q in main:
  dis=BRepExtrema_DistShapeShape(sh[r['path']].wrapped,sh[q['path']].wrapped);dis.Perform();assert dis.IsDone()
  sols=[{'sensor_xyz_mm':xyz(dis.PointOnShape1(i)),'pipe_xyz_mm':xyz(dis.PointOnShape2(i))} for i in range(1,dis.NbSolution()+1)]
  choices.append({'pipe_path':q['path'],'gap_mm':dis.Value(),'solutions':sols,'number_of_solutions':len(sols),**sols[0]})
 r['surface_contact']=min(choices,key=lambda q:q['gap_mm'])
for r in rows:
 if r['definition'] not in ['Fiber_Holder','Fiber_Holder_30deg','TC_No_Fiber_Holder']:continue
 children=[q for q in rows if q['parent']==r['path']];mounts=[q for q in children if q['definition'] in ['Part3','30TC Main Pipe_4837N25','4837N25_Standard-Wall Unthreaded Stainless Steel Pipe_4837N25']];assert len(mounts)==1
 m=mounts[0];p=[m[k] for k in ['cx','cy','cz']];r['mount_reference']={'path':m['path'],'definition':m['definition'],'xyz_mm':p};vertex=cq.Vertex.makeVertex(*p).wrapped
 for label,items in [('main_pipe',main),('jacket',[shell])]:
  choices=[]
  for q in items:
   dis=BRepExtrema_DistShapeShape(vertex,sh[q['path']].wrapped);dis.Perform();assert dis.IsDone();choices.append({'path':q['path'],'distance_to_solid_mm':dis.Value(),'nearest_xyz_mm':xyz(dis.PointOnShape2(1))})
  r['mount_to_'+label]=min(choices,key=lambda t:t['distance_to_solid_mm'])
 print('mount',r['path'],p,flush=True)
(R/'raw/rev9.json').write_text(json.dumps(d,indent=2));print('COMPLETE',len(rows),flush=True)
