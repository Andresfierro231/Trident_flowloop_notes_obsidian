from cad_model import *
from OCP.HLRBRep import HLRBRep_Algo,HLRBRep_HLRToShape
from OCP.HLRAlgo import HLRAlgo_Projector
from OCP.gp import gp_Ax2,gp_Pnt,gp_Dir
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.GeomAbs import GeomAbs_Line
import json,numpy as np
sh,defs=load();d=json.load(open(R/'data/geometry.json'));o=d['origin_CAD_xyz_mm'];out=[]
for path,s in sh.items():
 if not (defs[path].startswith('MSRloop') or '/NAUO18/' in path or defs[path] in ['Pipe8in','expansiontank','HX_Hose','DrainValve','DrainValve_Handle','MSETF_STNCL_HeaterClamp']):continue
 a=HLRBRep_Algo();a.Add(s.wrapped);a.Projector(HLRAlgo_Projector(gp_Ax2(gp_Pnt(*o),gp_Dir(1,0,0),gp_Dir(0,0,-1))));a.Update();a.Hide();res=HLRBRep_HLRToShape(a);lines=[]
 for comp in [res.VCompound(),res.OutLineVCompound()]:
  if comp.IsNull():continue
  for e in cq.Shape(comp).Edges():
   ac=BRepAdaptor_Curve(e.wrapped);n=2 if ac.GetType()==GeomAbs_Line else min(1000,max(12,int(e.Length()/1.5)))
   lines.append([xyz(ac.Value(float(t)))[:2] for t in np.linspace(ac.FirstParameter(),ac.LastParameter(),n)])
 out.append({'path':path,'definition':defs[path],'polylines':lines});print(path,len(lines),flush=True)
(R/'raw/cad_projection.json').write_text(json.dumps(out))
