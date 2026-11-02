from cad_model import *
from OCP.BRepAdaptor import BRepAdaptor_Surface
from scipy.optimize import minimize_scalar
from scipy.integrate import quad
from OCP.gp import gp_Pnt,gp_Vec
import numpy as np,json
sh,defs=load();d=json.load(open(R/'data/derived.json'));pts=d['models']['rev8']['corners'];out=[]
for i,pair in [(1,'CD'),(2,'GH')]:
 path=next(p for p in sh if p.endswith(f'/NAUO{i}/NAUO45'));f=BRepAdaptor_Surface(sh[path].Faces()[3].wrapped)
 def mid(v):return (np.array(xyz(f.Value(0,v)))+np.array(xyz(f.Value(.5,v))))/2
 def deriv(v):
  vs=[]
  for u in [0,.5]:
   p=gp_Pnt();du=gp_Vec();dv=gp_Vec();f.D1(u,v,p,du,dv);vs.append(np.array(xyz(dv)))
  return np.mean(vs,axis=0)
 def nearest(p):
  ans=minimize_scalar(lambda v:np.linalg.norm(mid(v)-p),bounds=(f.FirstVParameter(),f.LastVParameter()),method='bounded',options={'xatol':1e-14});return float(ans.x),float(ans.fun)
 ends=[nearest(np.array(pts[k])) for k in pair];vs=[p[0] for p in ends];length=abs(quad(lambda v:np.linalg.norm(deriv(v)),vs[0],vs[1],epsabs=1e-8,limit=100)[0]);bounds=sorted(vs)
 samples=[mid(v).tolist() for v in np.linspace(*vs,301)]
 mismatch=[];radial=[]
 for v in np.linspace(*bounds,100):
  c1=mid(v);c2=(np.array(xyz(f.Value(.25,v)))+np.array(xyz(f.Value(.75,v))))/2;mismatch.append(np.linalg.norm(c1-c2));radial.append(np.linalg.norm(np.array(xyz(f.Value(0,v)))-c1))
 row={'path':path,'face':4,'from_tag':pair[0],'to_tag':pair[1],'endpoint_projection_parameters':vs,'endpoint_residuals_mm':[p[1] for p in ends],'recovered_spine_length_mm':length,'basis':'Mean of opposed U=0,0.5 points on BSpline support surface; bounds are closest spine points to extracted straight-axis endpoints; not a healed exact hydraulic centerline','max_opposite_midpoint_disagreement_mm':max(mismatch),'max_profile_radius_error_mm':max(abs(x-16.7005) for x in radial),'polyline_xyz_mm':samples}
 if i==1:
  sen=next(s for s in d['sensors'] if s['sensor_id']=='STC-05');p=np.array([sen[f'CAD_{a}_mm'] for a in 'XYZ']);v,res=nearest(p);sl=abs(quad(lambda t:np.linalg.norm(deriv(t)),vs[0],v,epsabs=1e-8,limit=100)[0]);row.update(STC05_parameter=v,STC05_recovered_spine_xyz_mm=mid(v).tolist(),STC05_distance_from_projected_C_mm=sl,STC05_distance_to_projected_D_mm=length-sl,STC05_radial_distance_mm=res)
 out.append(row)
 print({k:v for k,v in row.items() if k!='polyline_xyz_mm'})
(R/'data/reconstructed_bends.json').write_text(json.dumps(out,indent=2))
