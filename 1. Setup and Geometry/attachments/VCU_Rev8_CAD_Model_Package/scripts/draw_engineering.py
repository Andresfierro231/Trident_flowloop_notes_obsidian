"""Eight A3 vector sheets derived from the audited Rev8 STEP geometry."""
from pathlib import Path
import json,math,numpy as np
from decimal import Decimal, ROUND_HALF_UP
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT,TA_CENTER
R=Path(__file__).resolve().parents[1];D=json.load(open(R/'data/VCU_Rev8_Engineering_Data.json'));CAD=json.load(open(R/'raw/cad_projection.json'));MESH=json.load(open(R/'raw/rev8_mesh.json'))
OUT=R.parent/'output/pdf/VCU_Rev8_CAD_Engineering_Drawings.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
for n,f in [('Regular','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
W,H=1190.551,841.890
INK=HexColor('#172f42');MUTED=HexColor('#526575');LINE=HexColor('#b7c5ce');PALE=HexColor('#f0f4f6');BLUE=HexColor('#1679bd');GREEN=HexColor('#147844');WALL=HexColor('#343a40');RED=HexColor('#a64237');AMBER=HexColor('#8c5d1b')
C=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);C.setTitle('VCU Rev8 - CAD engineering drawings and sensor coordinates');C.setAuthor('CAD geometry extraction');C.setSubject('Eight A3 sheets. Dimensions from UTDTloopWithOpticsAndHXRev8(1).STEP, 26 September 2026.')
P={r['tag']:np.array(r['local_xyz_mm'][:2]) for r in D['corner_points']};SG={r['segment']:r for r in D['segments']};S={r['sensor_id']:r for r in D['sensors']};O=np.array(D['coordinate_frame']['origin_CAD_xyz_mm']);J=D['jacket'];AUX={r['component']:r for r in D['auxiliary_axes']}
def F(x,n=3):
 if x is None:return '-'
 val=Decimal(str(round(float(x),10))).quantize(Decimal(1).scaleb(-n),rounding=ROUND_HALF_UP)
 if val==0:val=abs(val)
 return f'{val:,.{n}f}'
def local(p):return ((np.array(p)-O)[[2,1,0]]*[-1,1,1])[:2]
def text(x,y,s,size=10,font='Regular',color=INK,align='left'):
 C.setFillColor(color);C.setFont(font,size);getattr(C,{'left':'drawString','right':'drawRightString','center':'drawCentredString'}[align])(x,y,str(s))
def line(x1,y1,x2,y2,color=LINE,width=.65,dash=None):
 C.setStrokeColor(color);C.setLineWidth(width);C.setDash(dash or []);C.line(x1,y1,x2,y2);C.setDash([])
def para(s,x,top,w,size=10,color=INK,leading=None):
 st=ParagraphStyle('body',fontName='Regular',fontSize=size,leading=leading or size*1.4,textColor=color,spaceAfter=0)
 p=Paragraph(s,st);_,h=p.wrap(w,1000);p.drawOn(C,x,top-h);return top-h

def heading(s,x,y,w=None):
 text(x,y,s,12,'Bold');
 if w:line(x,y-8,x+w,y-8,LINE,.6)

def note(s,x,top,w,size=9.2):return para(s,x,top,w,size,MUTED)
def box(x,y,w,h,fill=PALE,stroke=None):
 C.setFillColor(fill);C.setStrokeColor(stroke or fill);C.rect(x,y,w,h,fill=1,stroke=bool(stroke))
def table(headers,rows,x,top,widths,size=9.2,rowh=None):
 st=ParagraphStyle('cell',fontName='Regular',fontSize=size,leading=size*1.25,textColor=INK)
 hs=ParagraphStyle('head',fontName='Bold',fontSize=size,leading=size*1.25,textColor=white)
 data=[[Paragraph(str(v),hs) for v in headers]]+[[Paragraph(str(v),st) for v in r] for r in rows]
 t=Table(data,colWidths=widths,rowHeights=rowh,repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,PALE]),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,-1),(-1,-1),.5,LINE)]));w,h=t.wrap(1100,1000);t.drawOn(C,x,top-h);return top-h

def page(n,title,sub):
 C.setFillColor(white);C.rect(0,0,W,H,fill=1,stroke=0)
 text(32,H-34,'VCU / REV8',11,'Bold',BLUE);text(155,H-34,title,20,'Bold');text(32,H-57,sub,10,color=MUTED)
 line(32,H-70,W-32,H-70,INK,1)
 line(32,52,W-32,52,INK,.8)
 text(32,35,'SOURCE: UTDTloopWithOpticsAndHXRev8(1).STEP - CAD extraction',8.4)
 text(32,22,'Units: mm | Drawing issue: 2026-09-26 | Printed precision does not imply manufacturing tolerance',7.8,color=MUTED)
 text(W-32,35,f'VCU-R8-E01  /  SHEET {n} OF 8',9,'Bold',align='right');text(W-32,22,'A3 landscape | Use dimensions; do not scale the PDF',7.8,color=MUTED,align='right')
 C.bookmarkPage(f'sheet{n}');C.addOutlineEntry(f'{n}. {title}',f'sheet{n}')
def finish():C.showPage()

def view(ox,oy,scale,paths=None,clip=None,light=False):
 # Orthographic CAD hidden-line result. Geometry is vector; no image tracing.
 def tr(p):return np.array([ox+scale*p[0],oy+scale*p[1]])
 C.saveState()
 if clip:
  cp=C.beginPath();cp.rect(*clip);C.clipPath(cp,stroke=0)
 for item in CAD:
  path=item['path'];
  if paths and not any(k in path for k in paths):continue
  jacket=any(path.endswith('/'+k) for k in ['NAUO40','NAUO41','NAUO42'])
  C.setStrokeColor(BLUE if jacket else Color(.38,.43,.47) if light else WALL);C.setLineWidth(.65 if jacket else .55)
  for points in item['polylines']:
   if len(points)<2:continue
   p=C.beginPath();p.moveTo(*tr(points[0]));
   for v in points[1:]:p.lineTo(*tr(v))
   C.drawPath(p,stroke=1,fill=0)
 C.restoreState();return tr

def pathline(points,tr,color=INK,width=.7,dash=None):
 C.setStrokeColor(color);C.setLineWidth(width);C.setDash(dash or []);p=C.beginPath();p.moveTo(*tr(points[0]));
 for q in points[1:]:p.lineTo(*tr(q))
 C.drawPath(p);C.setDash([])
def centerlines(tr):
 for name in ['upcomer','cooler','downcomer','heater']:
  s=SG[name];pathline([P[s['from_tag']],P[s['to_tag']]],tr,MUTED,.6,[5,2,1,2])

def arrow(pt,vec,color=INK,size=5):
 pt=np.array(pt);v=np.array(vec)/np.linalg.norm(vec);nv=np.array([-v[1],v[0]]);p=C.beginPath();p.moveTo(*pt);p.lineTo(*(pt+v*size+nv*size*.36));p.lineTo(*(pt+v*size-nv*size*.36));p.close();C.setFillColor(color);C.drawPath(p,stroke=0,fill=1)

def dimension(p,q,tr,offset,label,size=9,color=INK):
 a,b=tr(p),tr(q);v=(b-a)/np.linalg.norm(b-a);n=np.array([-v[1],v[0]]);aa=a+n*offset;bb=b+n*offset
 for u,z in [(a,aa),(b,bb)]:line(*(u+n*np.sign(offset)*3),*(z+n*np.sign(offset)*4),color,.5)
 line(*aa,*bb,color,.65);arrow(aa,v,color,4);arrow(bb,-v,color,4)
 angle=math.degrees(math.atan2(v[1],v[0]));
 if angle>90 or angle<-90:angle+=180
 mid=(aa+bb)/2;C.saveState();C.translate(*mid);C.rotate(angle);w=pdfmetrics.stringWidth(label,'Regular',size);box(-w/2-4,-3,w+8,size+5,white);text(0,0,label,size,color=color,align='center');C.restoreState()

def hdim(p,q,tr,y,label,size=9):
 a,b=tr(p),tr(q);a0=np.array([a[0],y]);b0=np.array([b[0],y]);line(*a,*a0,LINE,.6);line(*b,*b0,LINE,.6);line(*a0,*b0,INK,.6);arrow(a0,[1 if b[0]>a[0] else -1,0],size=4);arrow(b0,[-1 if b[0]>a[0] else 1,0],size=4);text((a[0]+b[0])/2,y+5,label,size,align='center')
def vdim(p,q,tr,x,label,size=9):
 a,b=tr(p),tr(q);line(*a,x,a[1],LINE,.6);line(*b,x,b[1],LINE,.6);line(x,a[1],x,b[1],INK,.6);arrow([x,a[1]],[0,1 if b[1]>a[1] else -1],size=4);arrow([x,b[1]],[0,-1 if b[1]>a[1] else 1],size=4)
 C.saveState();C.translate(x-5,(a[1]+b[1])/2);C.rotate(90);text(0,0,label,size,align='center');C.restoreState()

def tag(label,p,tr,dx=8,dy=8):
 x,y=tr(p);C.setFillColor(white);C.setStrokeColor(INK);C.setLineWidth(.7);C.circle(x,y,2.7,fill=1,stroke=1);text(x+dx,y+dy,label,10,'Bold')
def sensor_symbol(x,y,typ,size=6):
 if typ=='LF':
  C.saveState();C.setFillColor(BLUE);C.circle(x,y,size,fill=1,stroke=0);C.setFillColor(white);C.circle(x+size*.47,y+size*.28,size*.84,fill=1,stroke=0);C.restoreState()
 elif typ=='PTC':
  C.setFillColor(GREEN);p=C.beginPath();p.moveTo(x,y+size);p.lineTo(x+size*.72,y);p.lineTo(x,y-size);p.lineTo(x-size*.72,y);p.close();C.drawPath(p,fill=1,stroke=0)
 else:C.setFillColor(WALL);C.circle(x,y,size*.55,fill=1,stroke=0)

def sensor_type(s):return 'LF' if s['sensor_id'].startswith('LF') else 'STC' if s['sensor_id'].startswith('STC') else 'PTC'
def point_text(p):return ', '.join(F(x) for x in p)

# 1 - general arrangement
page(1,'General arrangement and pipe spans','Front orthographic CAD projection. Tank at upper left. Clockwise traversal starts at B, the upcomer inlet.')
tr=view(195,255,72/25.4/14);centerlines(tr)
for k in P:
 dx,dy={'A':(-22,-5),'B':(-19,6),'C':(-21,-5),'D':(6,14),'E':(-7,12),'F':(10,-2),'G':(8,0),'H':(-18,-13)}[k];tag(k,P[k],tr,dx,dy)
dimension(P['B'],P['C'],tr,37,'B-C  1,435.376')
dimension(P['F'],P['G'],tr,35,'F-G  1,435.376')
dimension(P['D'],P['E'],tr,34,'D-E  1,532.700')
dimension(P['H'],P['A'],tr,33,'H-A  1,532.700')
hdim(P['B'],P['G'],tr,147,'Vertical-axis horizontal separation  1,626.204')
text(302,474,'COOLING LEG',10,'Bold');text(304,266,'HEATING LEG',10,'Bold');text(133,444,'UPCOMER',9,'Bold',align='right');text(574,394,'DOWNCOMER',9,'Bold')
tank=AUX['expansion_tank'];tt=tr(local(tank['end_xyz_mm']));text(tt[0]+36,tt[1]-24,'Expansion tank',10);text(tt[0]+36,tt[1]-39,'OD 203.200 / L 311.150',9,color=MUTED)
text(231,622,'TLEP 469.900',9);text(417,83,'BREP 469.900',9)
# datum and directional arrows
x,y=tr(P['B']);line(x,y,x+40,y,INK,1);arrow([x+40,y],[-1,0],size=5);text(x+43,y-3,'+x',9);line(x,y,x,y+39,INK,1);arrow([x,y+39],[0,-1],size=5);text(x+4,y+42,'+y',9)
for pt,vec in [([0,700],[0,1]),([790,1380],[1,-.1763]),([1626,600],[0,-1]),([800,-206],[-1,.1763])]:
 zz=tr(pt);vv=np.array(vec);line(*(zz-vv*11),*(zz+vv*11),MUTED,1);arrow(zz+vv*11,-vv,MUTED,6)
heading('Measured straight spans',665,744,492)
top=table(['Leg / direction','Axis-end length','|dx|','|dy|'],[[name.title()+' '+SG[name]['from_tag']+'-'+SG[name]['to_tag'],F(SG[name]['centerline_length_mm']),F(abs(SG[name]['dx_mm'])),F(abs(SG[name]['dy_mm']))] for name in ['upcomer','cooler','downcomer','heater']],665,723,[190,105,99,98],9.4)
top=para('Lengths above are between the extracted ends of the straight cylindrical axes. Curved corner lengths are listed separately on Sheet 2. Cooling and heating legs are inclined approximately 10 degrees to horizontal.',665,top-17,492,10)
heading('Datum and coordinate convention',665,top-29,492)
top=para('<b>B = (0, 0, 0)</b> in the local drawing frame.<br/>CAD B = ('+point_text(O)+') mm.<br/><b>x = B<sub>Z</sub> - CAD Z</b>, rightward.<br/><b>y = CAD Y - B<sub>Y</sub></b>, upward.<br/><b>n = CAD X - B<sub>X</sub></b>, out of this drawing.',665,top-49,492,10.4)
heading('What is physically modeled',665,top-28,492)
top=para('Blue outlines identify only the jacket shell and its two end plates. The bare cooling-leg pipe remains gray. The CAD does not separately define the active heater boundaries, so the heating-leg dimension is not a heated-length measurement.',665,top-48,492,10)
heading('Drawing set',665,top-29,492)
top=table(['Sheet','Contents'],[['2','Corner offsets, heights, virtual corner-to-corner spans'],['3','Cooler, jacket, ports, radii and diameters'],['4','Heating leg, exit tubes and tank interfaces'],['5','Sensor locations with nearest-end callouts'],['6','Sensor stations, distance tables and contact ambiguity'],['7','Ordered CAD and local coordinate schedule'],['8','CAD references, probe geometry and model-input checks']],665,top-47,[49,443],9)
note('View scale 1:14 at A3. Dimensions are CAD-derived; no PDF dimensions were used. Instrument hardware is omitted from this overview and represented by reference symbols on Sheet 5.',32,101,356,8.7)
finish()

# 2 - corner geometry, virtual dimensions
page(2,'Corners, heights and end-to-end definitions','A-H identify two axial endpoints per physical corner. Virtual sharp intersections VLL/VUL/VUR/VLR are a separate modeling construction.')
# four inset corner views, actual CAD projected
for j,(title,aa,bb,path) in enumerate([('Lower left','A','B','NAUO1/NAUO45'),('Upper left','C','D','NAUO1/NAUO45'),('Upper right','E','F','NAUO2/NAUO45'),('Lower right','G','H','NAUO2/NAUO45')]):
 x=32+j*282;heading(title+'  '+aa+'-'+bb,x,743,257);mid=(P[aa]+P[bb])/2;sc=1.1;ox=x+128-mid[0]*sc;oy=621-mid[1]*sc
 tr=view(ox,oy,sc,paths=[path],clip=(x,536,257,173));tag(aa,P[aa],tr,-20,-13);tag(bb,P[bb],tr,8,5)
 s=next(s for s in D['segments'] if s['from_tag']==aa);hdim(P[aa],P[bb],tr,548,'|dx| '+F(abs(s['dx_mm'])),8);vdim(P[aa],P[bb],tr,x+231,'|dy| '+F(abs(s['dy_mm'])),8)
 text(x+4,519,'Chord '+F(s['chord_mm']),9)
 if s['centerline_length_mm']:
  text(x+4,503,'Arc '+F(s['centerline_length_mm'])+' / R 76.200 / 80.000 deg',8.7)
  text(x+4,487,'Envelope: inside R 59.4995 / outside R 92.9005',8.0,color=MUTED)
 else:text(x+4,503,'Recovered spine '+F(s['recovered_spine_length_mm'])+' (qualified below)',8.7,color=AMBER)
heading('Signed segment changes in traversal order',32,469,712)
rows=[]
for name in ['upcomer','upper_left_bend','cooler','upper_right_bend','downcomer','lower_right_bend','heater','lower_left_bend']:
 s=SG[name];ll=F(s['centerline_length_mm']) if s['centerline_length_mm'] is not None else F(s['recovered_spine_length_mm'])+'*'
 rows.append([s['from_tag']+'-'+s['to_tag'],name.replace('_',' ').title(),F(s['dx_mm']),F(s['dy_mm']),F(s['dz_normal_mm'],6),ll])
y=table(['Ends','Segment','dx','dy','dn','Length'],rows,32,448,[55,191,119,119,115,113],9.2)
note('* C-D and G-H: 99.578 is a reconstructed spline-support spine, not an established exact joined hydraulic length. Its projected endpoints miss the cylinder limits by 0.009 and 1.031 mm. The exact endpoint chord is 93.268 mm. Do not silently substitute a circular elbow.',32,y-12,712,9)
heading('Endpoint heights relative to B',775,469,382)
rows=[[r['tag'],F(r['local_xyz_mm'][0]),F(r['local_xyz_mm'][1])] for r in D['corner_points']]
y2=table(['Point','x','Height y'],rows,775,448,[66,158,158],9.2)
note('Highest listed tangent/axis limit: D +1,511.549.<br/>Lowest: H -341.193.<br/>Vertical range: 1,852.741 mm. This is a geometric height range, not an evaluated buoyancy head.',775,y2-12,382,9)
heading('Virtual sharp-corner spans (projected axes extended to intersections)',32,166,1125)
rows=[[s['leg'].title(),s['from']+' to '+s['to'],F(s['dx_mm']),F(s['dy_mm']),F(s['projected_axis_intersection_length_mm'])] for s in D['virtual_corner_spans']]
table(['Leg','Virtual endpoints','dx','dy','Intersection-to-intersection length'],rows,32,146,[167,237,174,174,373],8.4,rowh=[18]*5)
finish()

# 3 - jacket and diameter chart
page(3,'Cooling leg, jacket and section dimensions','All axial dimensions run from D toward E. Complete jacket includes the two modeled end plates; effective thermal length is not specified.')
# straightened local-axis detail, geometric scales except port fittings simplified
x0,y0,k=66,637,.68;L=SG['cooler']['centerline_length_mm'];js=J['pre_mm'];je=js+J['complete_mm']
line(x0,y0,x0+k*L,y0,WALL,4);line(x0,y0,x0+k*L,y0,MUTED,.5,[4,2])
# Draw actual shell section using measured lengths/radii, medium simplified
box(x0+k*js,y0-44.45*k,J['complete_mm']*k,88.9*k,HexColor('#edf6fc'),BLUE)
box(x0+k*(js+6.35),y0-38.9636*k,J['shell_mm']*k,77.9272*k,white,BLUE)
# central pipe envelope, deliberately uncut interior because main bore absent
box(x0,y0-16.7005*k,L*k,33.401*k,HexColor('#d8dde1'),WALL)
for st in [js,je]:line(x0+k*st,y0-44.45*k,x0+k*st,y0+44.45*k,BLUE,1)
for port in D['ports']:
 st=port['station_from_D_mm'];sgn=1 if port['id']=='PORT-A' else -1;px=x0+k*st;line(px,y0+sgn*44.45*k,px,y0+sgn*89*k,WALL,5);text(px+8,y0+sgn*84*k,port['id']+' / '+('JTC-A' if sgn==1 else 'JTC-B'),9,color=GREEN)
tr=lambda p:np.array([x0+k*p[0],y0+k*p[1]])
for aa,bb,off,label in [(0,js,79,'Pre '+F(js)),(js,je,79,'Complete jacket '+F(J['complete_mm'])),(je,L,79,'Post '+F(J['post_mm'])),(0,L,-85,'D-E straight axial span '+F(L)),(js+6.35,je-6.35,-54,'Shell only '+F(J['shell_mm']))]:dimension([aa,0],[bb,0],tr,off,label,9.3)
tag('D',[0,0],tr,-20,-3);tag('E',[L,0],tr,8,-3)
text(66,523,'Section diagram straightened to the cooling-leg axis. Gray core denotes modeled pipe envelope; its bore is absent from the source.',8.8,color=MUTED)
heading('Radii and diameters from analytical CAD cylinders',32,493,1125)
rows=[]
for r in D['diameters']:
 rows.append([r['item'],F(r['outer_radius_mm'],4),F(r['inner_radius_mm'],4),F(r['outer_diameter_mm'],4),F(r['inner_diameter_mm'],4),r['source_path']+' / F'+r['faces']])
y=table(['Component','Outer radius','Inner radius','OD','ID / hole','CAD instance / face evidence'],rows,32,471,[234,107,107,105,105,467],8.5)
note('Missing radius/ID = not encoded, not zero. End-plate inner radius is the clearance-hole radius. Nipple outer radius refers to the cylindrical land. Local LF and PTC spool bores differ, so none is promoted to a loop-wide hydraulic diameter.',32,y-10,1125,8.7)
heading('Jacket ends and coolant ports',32,188,1125)
rows=[['Complete jacket upstream plane',point_text(J['outer_start_xyz_mm']),F(js)],['Complete jacket downstream plane',point_text(J['outer_end_xyz_mm']),F(je)]]
for p in D['ports']:rows.append([p['id']+' axis crossing of jacket axis',point_text(p['axis_crossing_on_cooler_xyz_mm']),F(p['station_from_D_mm'])])
y=table(['Feature','CAD X, Y, Z at axis','Station from D'],rows,32,168,[320,582,223],8.7,rowh=[18]*5)
text(32,67,'Each end plate: 6.350 thick. Port-axis spacing: 914.400. Port A: 57.150 from jacket inlet plane. Port B: 58.738 from jacket outlet plane. Each port bore axis: 50.800 long.',8.5,color=MUTED)
finish()

# 4 - heater and branches
page(4,'Heating leg, exit tubes and tank interfaces','Exact endpoints refer to cylinder axes at the tube end planes. Branch connection points are not assumed to be ideal hydraulic tees.')
heading('Heating leg H to A',32,744,1125)
# straight axis heater details
x0=90;y0=650;k=.65;L=SG['heater']['centerline_length_mm'];tr=lambda p:np.array([x0+k*p[0],y0+k*p[1]])
line(x0,y0,x0+k*L,y0,WALL,7);line(x0,y0,x0+k*L,y0,white,1)
tag('H',[0,0],tr,-19,-3);tag('A',[L,0],tr,8,-3);dimension([0,0],[L,0],tr,55,'Heating-leg straight axis  '+F(L),10)
for i,sid in enumerate(['STC-12','PTC-04','LF-02','PTC-02','STC-01']):
 s=S[sid];x=x0+k*s['station_from_start_mm'];sy=y0;dx=0
 if sid=='LF-02':sy+=8
 sensor_symbol(x,sy,sensor_type(s),6.2);ly=y0-(36 if sid in ['STC-12','LF-02'] else 63 if sid in ['PTC-04','PTC-02'] else 90);tx=x+(-10 if sid in ['STC-12','LF-02'] else 10);line(x,sy,tx,ly+12,LINE,.7);text(tx,ly,sid+' / '+s['nearest_endpoint']+' '+F(s['nearest_distance_mm']),8.5,align='center')
note('Straightened station diagram. Active heater start/end boundaries are not encoded in Rev8. This CAD extraction therefore does not assign a heater thermal length or color the whole heating leg as active heater.',32,532,1125,9.2)
# branch enlargements fitleft
for idx,(name,ref,center) in enumerate([('TLEP','D',local(AUX['TLEP']['start_xyz_mm'])),('BREP','H',local(AUX['BREP']['start_xyz_mm']))]):
 x=32+idx*292;heading(name+' connection',x,488,261);sc=1.3;ox=x+112-center[0]*sc;oy=390-center[1]*sc
 tr=view(ox,oy,sc,paths=['NAUO1/NAUO45' if name=='TLEP' else 'NAUO2/NAUO45','/NAUO3' if name=='TLEP' else '/NAUO5'],clip=(x,301,260,164));tag(ref,P[ref],tr,-24,-17);tag(name+'-IN',center,tr,10,8)
 delta=AUX[name]['start_delta_from_corner_local_mm'];text(x,283,'IN relative to '+ref+': dx '+F(delta[0])+', dy '+F(delta[1]),8.8);text(x,267,'Out-of-plane dn '+F(delta[2],6),8.4,color=MUTED)
heading('Exit tube and tank axis lengths',650,488,507)
y=table(['Component','Axial length','OD','ID'],[[name,F(AUX[name]['length_mm']),F(2*AUX[name]['outer_radius_mm']),F(2*AUX[name]['inner_radius_mm'])] for name in ['TLEP','BREP','expansion_tank']],650,467,[221,109,88,89],9)
y=para('TLEP-IN is the lower end nearest the loop; TLEP-OUT is nearest the tank. BREP-IN is the upper end nearest the loop; BREP-OUT is its lower end. These names describe the coordinate ordering, not an asserted branch flow direction.',650,y-15,507,9.5)
y=para('TLEP-OUT lies 0.254 mm above the tank outer-cylinder lower end, a modeled axial overlap. BREP has 0.080572 mm change in CAD X along its 469.900 mm axis. The assembly has not been flattened or healed.',650,y-13,507,9.5)
heading('World-coordinate endpoint schedule',32,237,1125)
rows=[]
for nm in ['TLEP','BREP','expansion_tank']:
 r=AUX[nm]
 for e in ['start','end']:rows.append([nm+(' / IN' if e=='start' else ' / OUT'),*map(lambda v:F(v),r[e+'_xyz_mm']),r['source_path'].split('Rev8/')[1]+' / F2'])
y=table(['Axis endpoint','CAD X','CAD Y','CAD Z','CAD source'],rows,32,217,[289,166,166,166,338],8.9,rowh=[19]*7)
note('For the tank, IN/OUT denote lower/upper shell-axis ends only. Its outside axial envelope is 311.150 mm. Source identity and face numbering are defined on Sheet 8.',32,y-9,1125,8.6)
finish()

# 5 - sensor map
page(5,'Sensor locations and nearest-end distances','Symbols mark projected main-loop stations. Callouts give selected-reference distances along the leg; * identifies a non-unique or reconstructed reference.')
tr=view(170,245,.26,paths=['NAUO1/NAUO45','NAUO2/NAUO45','NAUO6/']);centerlines(tr)
for tagname in P:tag(tagname,P[tagname],tr,7,8)
# fixed callout positions avoid overlaps, all units mm
pos={'STC-02':(57,322),'STC-03':(55,429),'STC-04':(55,532),'LF-01':(63,597),'STC-05':(113,696),'STC-06':(244,710),'PTC-01':(389,735),'LF-03':(493,672),'PTC-03':(580,640),'STC-07':(631,603),'STC-08':(634,532),'STC-09':(634,425),'STC-10':(634,325),'LF-04':(634,233),'STC-11':(633,197),'STC-12':(521,111),'PTC-04':(519,80),'LF-02':(319,171),'PTC-02':(255,139),'STC-01':(92,182),'JTC-A':(331,666),'JTC-B':(442,517)}
for sid,s in S.items():
 pp=local(s['actual_reference_xyz_mm']) if sid.startswith('JTC') else local(s['projected_axis_xyz_mm']);x,y=tr(pp)
 # LF moon shifted only at combined mount pairs; green diamond stays on axis.
 if sid in ['LF-02','LF-03']:y+=9
 typ=sensor_type(s);sensor_symbol(x,y,typ,7.2 if typ=='LF' else 6.4)
 tx,ty=pos[sid];color=BLUE if typ=='LF' else GREEN if typ=='PTC' else WALL;line(x,y,tx+10,ty+5,LINE,.6)
 star='*' if sid=='STC-05' or s.get('number_contact_solutions',1)>1 else ''
 label=sid+star
 if not sid.startswith('JTC'):label+='  '+s['nearest_endpoint']+' '+F(s['nearest_distance_mm'])
 else:label+='  jacket port'
 text(tx,ty,label,8.7,'Bold',color)
# right information panel
heading('Symbol and reference definitions',824,743,333)
for yy,typ,label in [(712,'LF','LF - Luna fiber mount'),(682,'PTC','PTC - penetrating TC mount'),(652,'STC','STC - surface contact reference')]:sensor_symbol(838,yy+3,typ,7);text(855,yy,label,10)
y=para('JTC-A/B use green diamonds and belong to the coolant ports. They are additional thermocouples, not missing main-loop PTC locations.',824,628,333,10)
y=para('Main-loop dots and diamonds are placed on their projected pipe axes for clear station reading. The actual 3D mounting/contact coordinates are retained on Sheet 7. LF moons are slightly offset at shared LF/PTC mounts.',824,y-16,333,10)
heading('Reference integrity',824,y-29,333)
y=para('STC markers use one closest point between the modeled thermocouple and pipe solid. Several bodies have multiple equally close points. Sheet 6 lists their station ranges; the CAD does not label a sensing junction.',824,y-49,333,10)
y=para('LF and PTC coordinates use the centroid of the local mounting-pipe body. These locate hardware, not the optical active length or TC junction.',824,y-15,333,10)
heading('Numbering and counts',824,y-28,333)
y=para('12 STC + 4 LF + 4 loop PTC + 2 JTC.<br/>LF-02/PTC-02 and LF-03/PTC-03 share mounting bodies. Labels follow the collaborator schema by region/order; STEP carries component instances, not verified acquisition-channel names.',824,y-49,333,10)
note('Clockwise loop order: B-C-D-E-F-G-H-A-B. Nearest-end labels are along-axis distances, not horizontal or vertical separations. The jacket-only symbols use port references on Sheet 6.',32,78,727,8.6)
finish()

# 6 - full sensor station schedule + unrolled diagram
page(6,'Sensor stations and reference ambiguity','Distances use actual CAD references projected to the relevant leg. s is measured from the first endpoint in the leg name. No rounded-corner length is added.')
# compact station plots with per-type lanes
plotx=139;plotw=954;ploty=713
for i,name in enumerate(['upcomer','cooler','downcomer','heater']):
 y=ploty-i*38;sg=SG[name];L=sg['centerline_length_mm'];text(32,y-3,name.title(),9,'Bold');line(plotx,y,plotx+plotw,y,LINE,1);text(plotx-7,y-3,sg['from_tag'],8,'Bold',align='right');text(plotx+plotw+7,y-3,sg['to_tag'],8,'Bold')
 for s in D['sensors']:
  if s['segment']!=name:continue
  typ=sensor_type(s);xx=plotx+plotw*s['station_from_start_mm']/L;yy=y+({'STC':0,'LF':8,'PTC':-8}[typ]);sensor_symbol(xx,yy,typ,5)
  rg=s.get('minimum_distance_solution_station_range_mm')
  if rg and rg[1]-rg[0]>.01:line(plotx+plotw*rg[0]/L,y,plotx+plotw*rg[1]/L,y,WALL,2.5)
text(32,553,'Lane offsets separate sensor types in this unrolled view. Dark short bars span returned STC minimum-distance solutions; they are not certified sensing footprints.',8.6,color=MUTED)
rows=[]
for s in D['sensors']:
 if s['sensor_id'].startswith('JTC'):continue
 rg=s.get('minimum_distance_solution_station_range_mm');mult=s.get('number_contact_solutions',1)>1
 alt=(F(rg[0])+' to '+F(rg[1])) if mult else 'Single returned point' if s['sensor_id'].startswith('STC') else 'Mount centroid'
 if s['sensor_id']=='STC-05':alt='Recovered spline spine*'
 rows.append([s['sensor_id'],s['segment_start']+'-'+s['segment_end'],F(s['station_from_start_mm']),F(s['distance_to_end_mm']),s['nearest_endpoint']+' / '+F(s['nearest_distance_mm']),alt])
y=table(['Sensor','Leg ends','s from start','To end','Nearest end / distance','Other returned contact stations, measured from start'],rows,32,536,[96,92,122,122,167,526],8.9,rowh=[21]+[18]*20)
note('* STC-05 is on the upper-left spline corner: recovered station 17.550 from C*, 82.029 to D*. Direct coordinate difference from C is dx +1.632 and dy +17.418 mm. C*/D* are projected spine endpoints with the residuals documented on Sheet 2.',32,y-9,1125,8.7)
rows=[]
for sid in ['JTC-A','JTC-B']:
 s=S[sid];rows.append([sid,s['segment'],F(s['station_from_start_mm']),F(-s['distance_to_end_mm']),F(s['axis_radial_offset_mm']),s['source_cad_path']])
y=table(['Jacket TC','Port bore axis','From inner bore end','Beyond outer bore end','Off port axis','CAD assembly'],rows,32,111,[111,183,213,236,181,201],8.1,rowh=[17,17,17])
finish()

# 7 - ordered coordinates
page(7,'Ordered coordinates for model construction','Traverse B to C to D to E to F to G to H to A, then return to B. Sensor rows contain actual CAD reference points, not their projected axis stations.')
rows=[]
for r in D['sequential_coordinates']:
 rows.append([r['tag'],r['kind'],*map(lambda v:F(v),r['CAD_xyz_mm']),*map(lambda v:F(v),r['local_xyz_mm']),r['reference'].replace('_',' ')])
y=table(['ID','Point basis','CAD X','CAD Y','CAD Z','Local x','Height y','Normal n','Segment / reference'],rows,32,748,[81,88,112,118,118,114,111,92,291],8.35,rowh=[24]+[16.6]*len(rows))
note('Local x = 3306.139984198 - CAD Z; y = CAD Y - 852.124195141; n = CAD X - 629.806632391. Full-precision XYZ, projected sensor stations, additional contact solutions, probe-shaft endpoints and port-axis endpoints are included in the companion JSON/CSV package.',32,y-12,1125,9)
note('J-IN / J-OUT = complete jacket outer end planes at the axis. TLEP/BREP IN = tube end nearest the loop; OUT = remote end. Sensor coordinates represent geometric references as defined on Sheets 5-6, not verified sensing junctions.',32,y-47,1125,8.7)
finish()

# 8 - evidence and validation
page(8,'CAD traceability and modeling qualifications','Source priority: Rev8 STEP geometry only. Earlier PDFs and Rev7 dimensions were not used to populate this drawing set.')
heading('Source identity and extraction',32,744,552)
y=para('<b>UTDTloopWithOpticsAndHXRev8(1).STEP</b><br/>Assembly root: UTDTloopWithOpticsAndHXRev8<br/>Source SHA-256:',32,724,552,9.8)
text(32,y-16,D['source_sha256'][:32],8.7,'Mono');text(32,y-29,D['source_sha256'][32:],8.7,'Mono')
y=para('Recursive XCAF placements were composed for all 88 assembly records. OCCT imported STEP inch units to millimetres. Native cylindrical/torus faces supplied axes, radii and bounds. CAD hidden-line projection supplied the drawing outlines.',32,y-43,552,9.5)
y=para('An independent STEP reload checked 12 long main-pipe face bounds against projected boundary vertices: maximum endpoint discrepancy &lt; 0.000001 mm. This checks extraction consistency, not manufacturing accuracy.',32,y-13,552,9.5)
heading('CAD instance references',620,744,537)
rows=[['Upcomer / cooler / lower-left corner','NAUO1/NAUO45'],['Downcomer / heater / upper-right corner','NAUO2/NAUO45'],['TLEP / tank / BREP','NAUO3 / NAUO4 / NAUO5'],['Jacket shell / end plates','NAUO6/NAUO40 / NAUO41 / NAUO42'],['Jacket coolant ports','NAUO6/NAUO43 / NAUO44']]
y2=table(['Feature','Path below root'],rows,620,724,[302,235],8.8)
note('Within each main-loop part: F3/F9 long inclined face; F5/F11 vertical face; F6/F12 short inclined continuation; F1/F13 exact torus; F4/F10 spline corner. Repeated faces are opposite halves, not extra pipe lengths.',620,y2-11,537,8.8)
heading('Sensor identity to CAD assembly',32,488,552)
rows=[]
for row in [('STC-01 / 02 / 03 / 04','NAUO10 / 13 / 12 / 11'),('STC-05 / 06 / 07 / 08','NAUO14 / 15 / 16 / 17'),('STC-09 / 10 / 11 / 12','NAUO18 / 19 / 20 / 21'),('LF-01 / LF-04','NAUO1/NAUO46 / NAUO2/NAUO46'),('LF-02 + PTC-02 / LF-03 + PTC-03','NAUO8 / NAUO7'),('PTC-01 / PTC-04','NAUO24 / NAUO23'),('JTC-A / JTC-B','NAUO9 / NAUO22')]:rows.append(row)
y=table(['Drawing IDs','Path below root'],rows,32,469,[303,249],8.8)
note('Mount-reference child: LF-01/04 -> NAUO47; combined LF/PTC -> NAUO31; PTC-only and JTC -> NAUO28. Surface references come from the whole STC part to the closest main-pipe solid. Source names and full paths are retained in JSON.',32,y-11,552,8.8)
heading('Model-input qualifications',620,488,537)
items=[('Main bore / active heater','The solid main-loop envelope supplies OD 33.401 but no bore. Neither heater active length nor heat-flux boundaries are separately defined.'),('Spline corner closure','Recovered C-D and G-H spines are 99.578 long with 0.009 / 1.031 endpoint residuals. Exact hydraulic corner lengths remain unresolved.'),('Cooler assembly alignment','Two straight-axis pieces meet with a 0.271771 mm offset. The 1532.700 span sums their unique lengths; the offset is not added as pipe.'),('Sensor contact / junction','STC-08 and STC-11 minimum gaps are 0.005634 and 0.092102 mm. Multiple contact solutions are reported on Sheet 6. TC junctions and LF sensing extents are not identified.')]
y=468
for title,body in items:
 text(620,y,title,9.4,'Bold');y=para(body,620,y-9,537,9.1)-17
heading('Modeled thermocouple sheaths',32,193,552)
rows=[['PTC-01 / PTC-04','158.750','3.175'],['PTC-02 / PTC-03','152.400','3.175'],['JTC-A / JTC-B','158.750','3.175']]
y=table(['Probe grouping','Longest shaft length','Shaft OD'],rows,32,173,[271,174,107],8.7,rowh=[20]*4)
note('These are geometric cylindrical-shaft spans. Both 3D shaft endpoints are supplied in JSON; neither endpoint is asserted to be the sensing junction.',32,y-8,552,8.7)
heading('Using the companion data',620,191,537)
para('The JSON preserves full floating-point coordinates, evidence paths and qualified values. CSV tables provide ordered points, sensor stations, pipe segments and radii/diameters. Null/blank means unavailable. Retain the normal coordinate n for 3D modeling. Choose and document any bore, heater extent, sensor-junction or geometry-healing assumption before constructing the computational model.',620,171,537,9.5)
finish()
C.save();print(OUT)
