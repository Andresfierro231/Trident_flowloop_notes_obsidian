from pathlib import Path
import os
import cadquery as cq
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TDocStd import TDocStd_Document
from OCP.TCollection import TCollection_ExtendedString
from OCP.TDataStd import TDataStd_Name
from OCP.TDF import TDF_Label,TDF_LabelSequence
from OCP.XCAFDoc import XCAFDoc_DocumentTool
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
R=Path(__file__).resolve().parents[1]
SOURCE=Path(os.environ.get('VCU_REV9_STEP',R/'source/_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step'))
if not SOURCE.exists():SOURCE=R.parent/'upload/_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step'
def name(l):
 a=TDataStd_Name();return a.Get().ToExtString() if l.FindAttribute(TDataStd_Name.GetID_s(),a) else 'unnamed'
def xyz(p):return [p.X(),p.Y(),p.Z()]
def load():
 doc=TDocStd_Document(TCollection_ExtendedString('XmlXCAF'));rd=STEPCAFControl_Reader();rd.SetNameMode(True);assert 'RetDone' in str(rd.ReadFile(str(SOURCE)));assert rd.Transfer(doc)
 tool=XCAFDoc_DocumentTool.ShapeTool_s(doc.Main());roots=TDF_LabelSequence();tool.GetFreeShapes(roots);shapes={};defs={}
 def walk(l,tr,path):
  if tool.IsAssembly_s(l):
   seq=TDF_LabelSequence();tool.GetComponents_s(l,seq,False)
   for i in range(1,seq.Length()+1):
    c=seq.Value(i);ref=TDF_Label();assert tool.GetReferredShape_s(c,ref);walk(ref,tr.Multiplied(tool.GetLocation_s(c).Transformation()),path+'/'+name(c))
  else:
   shapes[path]=cq.Shape(BRepBuilderAPI_Transform(tool.GetShape_s(l),tr,True).Shape());defs[path]=name(l)
 for i in range(1,roots.Length()+1):
  root=roots.Value(i);walk(root,cq.Matrix().wrapped.Trsf(),name(root))
 return shapes,defs
