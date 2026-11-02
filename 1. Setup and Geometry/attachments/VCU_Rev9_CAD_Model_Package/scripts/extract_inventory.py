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
    ts.append({'face':i,'major_radius_mm':t.MajorRadius(),'minor_radius_mm':t.MinorRadius(),'center_xyz_mm':[p.X(),p.Y(),p.Z()],'x_direction':[t.XAxis().Direction().X(),t.XAxis().Direction().Y(),t.XAxis().Direction().Z()],'y_direction':[t.YAxis().Direction().X(),t.YAxis().Direction().Y(),t.YAxis().Direction().Z()],'axis_dir':[v.X(),v.Y(),v.Z()],'umin':a.FirstUParameter(),'umax':a.LastUParameter()})
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

out={"source_file":f.name,"sha256":hashlib.sha256(f.read_bytes()).hexdigest(),"units":"mm","method":"Fresh recursive XCAF import; analytical surface extraction without healing","records":rows}
dest.write_text(json.dumps(out,indent=2));print("COMPLETE",len(rows),flush=True)
