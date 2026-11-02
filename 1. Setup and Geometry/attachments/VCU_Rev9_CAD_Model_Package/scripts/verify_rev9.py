"""Cross-check analytical V bounds against independently projected CAD vertices."""
from pathlib import Path
import json,sys,hashlib
import numpy as np
import cadquery as cq
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.TDF import TDF_Label,TDF_LabelSequence
from inspect_step import label_name,transform_shape
R=Path(__file__).resolve().parents[1];O=R;rev=sys.argv[1]
d=json.loads((O/'raw'/f'{rev}.json').read_text());f=__import__('cad_model').SOURCE;by={r['path']:r for r in d['records']}
doc=TDocStd_Document(TCollection_ExtendedString('XmlXCAF'));reader=STEPCAFControl_Reader();assert 'RetDone' in str(reader.ReadFile(str(f)));assert reader.Transfer(doc)
tool=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main());roots=TDF_LabelSequence();tool.GetFreeShapes(roots);results=[]
def walk(lab,tr,path):
 if tool.IsAssembly_s(lab):
  seq=TDF_LabelSequence();tool.GetComponents_s(lab,seq,False)
  for i in range(1,seq.Length()+1):
   comp=seq.Value(i);ref=TDF_Label();assert tool.GetReferredShape_s(comp,ref)
   walk(ref,tr.Multiplied(tool.GetLocation_s(comp).Transformation()),path+'/'+label_name(comp))
 elif label_name(lab).startswith('MSRloop'):
  shape=cq.Shape(transform_shape(tool.GetShape_s(lab),tr));faces=shape.Faces()
  for c in by[path]['cylinders']:
   if abs(c['radius_mm']-16.7005)>.01 or c['vmax']-c['vmin']<20:continue
   pts=np.array([v.toTuple() for v in faces[c['face']-1].Vertices()]);a=np.array(c['axis_point']);v=np.array(c['axis_dir']);u=(pts-a)@v
   ends=[a+min(u)*v,a+max(u)*v];error=max(np.linalg.norm(ends[0]-c['start_xyz_mm']),np.linalg.norm(ends[1]-c['end_xyz_mm']))
   results.append({'path':path,'face':c['face'],'vertex_projection_endpoint_error_mm':float(error)})
for i in range(1,roots.Length()+1):
 lab=roots.Value(i);walk(lab,cq.Matrix().wrapped.Trsf(),label_name(lab))
assert len(results)==12
assert max(r['vertex_projection_endpoint_error_mm'] for r in results)<1e-6
out={'source_file':f.name,'sha256_matches':hashlib.sha256(f.read_bytes()).hexdigest()==d['sha256'],'method':'Independent STEP reload; project boundary vertices onto each long main-pipe cylinder axis, compare with analytical V bounds','checks':results,'max_endpoint_error_mm':max(r['vertex_projection_endpoint_error_mm'] for r in results)}
assert out['sha256_matches'];(O/'raw'/f'{rev}_verification.json').write_text(json.dumps(out,indent=2));print(rev,'verified',len(results),'faces; max error mm:',out['max_endpoint_error_mm'])
