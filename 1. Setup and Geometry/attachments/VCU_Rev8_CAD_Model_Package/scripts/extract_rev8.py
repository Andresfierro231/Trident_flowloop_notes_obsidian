"""Recursive, world-coordinate CAD audit; no edits to source assemblies."""
import sys,json,hashlib
from pathlib import Path
import cadquery as cq
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDF import TDF_Label,TDF_LabelSequence
from OCP.BRepAdaptor import BRepAdaptor_Surface
from OCP.GeomAbs import GeomAbs_Cylinder,GeomAbs_Torus,GeomAbs_Plane,GeomAbs_Circle
from OCP.BRepAdaptor import BRepAdaptor_Curve
from OCP.BRepExtrema import BRepExtrema_DistShapeShape
from inspect_step import label_name,transform_shape
f=Path(sys.argv[1]);dest=Path(sys.argv[2]);dest.parent.mkdir(parents=True,exist_ok=True)
doc=TDocStd_Document(TCollection_ExtendedString('XmlXCAF'));rd=STEPCAFControl_Reader();rd.SetNameMode(True)
assert 'RetDone' in str(rd.ReadFile(str(f)));assert rd.Transfer(doc)
tool=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main());roots=TDF_LabelSequence();tool.GetFreeShapes(roots)
rows=[];shapes={}
def walk(lab,tr,path,parent='',depth=0):
 n=label_name(lab);isasm=tool.IsAssembly_s(lab)
 shape=transform_shape(tool.GetShape_s(lab),tr)
 wrapped=cq.Shape(shape);bb=wrapped.BoundingBox()
 center=wrapped.Center() if n in ['Part3','30TC Main Pipe_4837N25','4837N25_Standard-Wall Unthreaded Stainless Steel Pipe_4837N25'] else cq.Vector((bb.xmin+bb.xmax)/2,(bb.ymin+bb.ymax)/2,(bb.zmin+bb.zmax)/2)
 row={'path':path,'definition':n,'parent':parent,'depth':depth,'assembly':isasm,'xmin':bb.xmin,'xmax':bb.xmax,'ymin':bb.ymin,'ymax':bb.ymax,'zmin':bb.zmin,'zmax':bb.zmax,'cx':center.x,'cy':center.y,'cz':center.z,'center_basis':'solid centroid for sensor mount bodies; bounding-box center for other inventory items'}
 print('component',path,n,flush=True)
 rows.append(row);shapes[path]=shape
 if isasm:
  ch=TDF_LabelSequence();tool.GetComponents_s(lab,ch,False)
  for i in range(1,ch.Length()+1):
   c=ch.Value(i);ref=TDF_Label();assert tool.GetReferredShape_s(c,ref)
   walk(ref,tr.Multiplied(tool.GetLocation_s(c).Transformation()),path+'/'+label_name(c),path,depth+1)
 else:
  cs=[];ts=[];planes=[];surfaces=[];edges=[]
  for i,face in enumerate(cq.Shape(shape).Faces(),1):
   a=BRepAdaptor_Surface(face.wrapped)
   surfaces.append({'face':i,'type':str(a.GetType()),'area_mm2':face.Area()})
   if a.GetType()==GeomAbs_Plane:
    pl=a.Plane();p=pl.Location();v=pl.Axis().Direction();planes.append({'face':i,'point':[p.X(),p.Y(),p.Z()],'normal':[v.X(),v.Y(),v.Z()]})
   if a.GetType()==GeomAbs_Torus:
    t=a.Torus();p=t.Location();v=t.Axis().Direction()
    ts.append({'face':i,'major_radius_mm':t.MajorRadius(),'minor_radius_mm':t.MinorRadius(),'center_xyz_mm':[p.X(),p.Y(),p.Z()],'axis_dir':[v.X(),v.Y(),v.Z()],'umin':a.FirstUParameter(),'umax':a.LastUParameter()})
   if a.GetType()!=GeomAbs_Cylinder:continue
   c=a.Cylinder();p=c.Location();v=c.Axis().Direction();p=[p.X(),p.Y(),p.Z()];v=[v.X(),v.Y(),v.Z()]
   cs.append({'face':i,'radius_mm':c.Radius(),'axis_point':p,'axis_dir':v,'vmin':a.FirstVParameter(),'vmax':a.LastVParameter(),
    'start_xyz_mm':[p[j]+v[j]*a.FirstVParameter() for j in range(3)],'end_xyz_mm':[p[j]+v[j]*a.LastVParameter() for j in range(3)]})
  row['cylinders']=cs
  row['tori']=ts
  row['planes']=planes;row['surfaces']=surfaces
  if n.startswith('MSRloop') or n in ['Pipe8in','3in3ftCutSS_44635K443'] or '8983K211' in n:
   for j,e in enumerate(cq.Shape(shape).Edges(),1):
    ac=BRepAdaptor_Curve(e.wrapped);entry={'edge':j,'type':str(ac.GetType()),'length_mm':e.Length()}
    if ac.GetType()==GeomAbs_Circle:
     cc=ac.Circle();p=cc.Location();v=cc.Axis().Direction();entry.update(radius_mm=cc.Radius(),center_xyz_mm=[p.X(),p.Y(),p.Z()],axis_dir=[v.X(),v.Y(),v.Z()])
    edges.append(entry)
   row['edges']=edges
  row['vertices_xyz_mm']=[list(p.toTuple()) for p in cq.Shape(shape).Vertices()]
for i in range(1,roots.Length()+1):
 lab=roots.Value(i);walk(lab,cq.Matrix().wrapped.Trsf(),label_name(lab))
main=[r for r in rows if r['definition'].startswith('MSRloop')]
print('Walking complete',len(rows),flush=True)
jacket=[r for r in rows if r['definition']=='3in3ftCutSS_44635K443']
for r in rows:
 if 'Surface_Thermoc' not in r['definition']:continue
 print('surface contact',r['path'],flush=True)
 best=None
 for q in main:
  d=BRepExtrema_DistShapeShape(shapes[r['path']],shapes[q['path']]);d.Perform();assert d.IsDone()
  if best is None or d.Value()<best['gap_mm']:
   p=d.PointOnShape1(1);v=d.PointOnShape2(1)
   best={'pipe_path':q['path'],'gap_mm':d.Value(),'sensor_xyz_mm':[p.X(),p.Y(),p.Z()],'pipe_xyz_mm':[v.X(),v.Y(),v.Z()],'number_of_solutions':d.NbSolution()}
 r['surface_contact']=best
for r in rows:
 if r['definition'] not in ['Fiber_Holder','Fiber_Holder_30deg','TC_No_Fiber_Holder']:continue
 print('mount',r['path'],flush=True)
 children=[q for q in rows if q['parent']==r['path']]
 mounts=[q for q in children if q['definition'] in ['Part3','30TC Main Pipe_4837N25','4837N25_Standard-Wall Unthreaded Stainless Steel Pipe_4837N25']]
 assert len(mounts)==1,(r['path'],mounts)
 m=mounts[0];p=cq.Vertex.makeVertex(m['cx'],m['cy'],m['cz']).wrapped
 r['mount_reference']={'path':m['path'],'definition':m['definition'],'xyz_mm':[m['cx'],m['cy'],m['cz']]}
 for label,items in [('main_pipe',main),('jacket',jacket)]:
  best=None
  for q in items:
   d=BRepExtrema_DistShapeShape(p,shapes[q['path']]);d.Perform();assert d.IsDone()
   if best is None or d.Value()<best['distance_to_solid_mm']:
    v=d.PointOnShape2(1);best={'path':q['path'],'distance_to_solid_mm':d.Value(),'nearest_xyz_mm':[v.X(),v.Y(),v.Z()]}
  r['mount_to_'+label]=best
out={'source_file':f.name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'units':'mm','method':'Recursive assembly transforms via XCAF; exact cylindrical face axes; no geometry healing','records':rows}
dest.write_text(json.dumps(out,indent=2))
# Save world-coordinate tessellation of pipe/jacket/tank only for an independent visual check.
mesh=[]
for r in rows:
 if r['assembly']:continue
 if not (r in main or '/NAUO6/' in r['path'] or r['definition'] in ['Pipe8in','expansiontank']):continue
 verts,tri=cq.Shape(shapes[r['path']]).tessellate(.7,.15)
 mesh.append({'path':r['path'],'definition':r['definition'],'vertices_xyz_mm':[[v.x,v.y,v.z] for v in verts],'triangles':tri})
dest.with_name(dest.stem+'_mesh.json').write_text(json.dumps(mesh))
dest.write_text(json.dumps(out,indent=2));print(f.name,len(rows),'records')
