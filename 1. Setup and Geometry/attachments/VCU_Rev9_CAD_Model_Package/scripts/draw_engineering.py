"""Eight A3 vector sheets derived from the audited Rev9 STEP geometry."""
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
R=Path(__file__).resolve().parents[1];D=json.load(open(R/'data/VCU_Rev9_Engineering_Data.json'));CAD=json.load(open(R/'raw/cad_projection.json'))
OUT=R.parent/'output/pdf/VCU_Rev9_CAD_Engineering_Drawings.pdf';OUT.parent.mkdir(parents=True,exist_ok=True)
for n,f in [('Regular','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf'),('Mono','DejaVuSansMono.ttf')]:pdfmetrics.registerFont(TTFont(n,'/usr/share/fonts/truetype/dejavu/'+f))
W,H=1190.551,841.890
INK=HexColor('#172f42');MUTED=HexColor('#526575');LINE=HexColor('#b7c5ce');PALE=HexColor('#f0f4f6');BLUE=HexColor('#1679bd');GREEN=HexColor('#147844');WALL=HexColor('#343a40');RED=HexColor('#a64237');AMBER=HexColor('#8c5d1b')
C=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);C.setTitle('VCU Rev9 - CAD engineering drawings and sensor coordinates');C.setAuthor('CAD geometry extraction');C.setSubject('Eight A3 sheets. Dimensions from _STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step, 8 October 2026.')
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
 text(32,H-34,'VCU / REV9',11,'Bold',BLUE);text(155,H-34,title,20,'Bold');text(32,H-57,sub,10,color=MUTED)
 line(32,H-70,W-32,H-70,INK,1)
 line(32,52,W-32,52,INK,.8)
 text(32,35,'SOURCE: _STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step | CAD extraction',7.8)
 text(32,22,'Units: mm | Drawing issue: 2026-10-08 | Printed precision does not imply manufacturing tolerance',7.8,color=MUTED)
 text(W-32,35,f'VCU-R9-E01  /  SHEET {n} OF 8',9,'Bold',align='right');text(W-32,22,'A3 landscape | Use dimensions; do not scale the PDF',7.8,color=MUTED,align='right')
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
  jacket=any(path.endswith('/'+k) for k in ['NAUO56','NAUO57','NAUO58'])
  heater=path.rsplit('/',1)[-1] in ['NAUO25','NAUO26','NAUO27','NAUO28']
  C.setStrokeColor(BLUE if jacket else RED if heater else Color(.38,.43,.47) if light else WALL);C.setLineWidth(.65 if jacket else .55)
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

MAIN=['NAUO1/NAUO62','NAUO2/NAUO61'];HE=D['heater'];CL=HE['clamps'];ROOT='UTDTloopWithOpticsAndHXRev9_9_18_26/'
def sp(path):return path.removeprefix(ROOT)
def sl(name):return SG[name]['reference_length_mm']
# 1 - Overall front view and primary straight spans.
page(1,'General arrangement and pipe spans','Front orthographic projection from Rev9 CAD. Expansion tank at upper left. Traverse B-C-D-E-F-G-H-A-B clockwise.')
tr=view(170,273,72/25.4/14);centerlines(tr)
for k in P:
 dx,dy={'A':(-22,-8),'B':(-20,6),'C':(-21,-4),'D':(7,11),'E':(-7,13),'F':(10,-3),'G':(8,0),'H':(-18,-13)}[k];tag(k,P[k],tr,dx,dy)
for aa,bb,off,name in [('B','C',37,'upcomer'),('D','E',30,'cooler'),('F','G',-50,'downcomer'),('H','A',30,'heater')]:dimension(P[aa],P[bb],tr,off,aa+'-'+bb+'  '+F(sl(name))+('*' if name=='heater' else ''),9)
hdim(P['B'],P['G'],tr,166,'Vertical-axis separation  '+F(P['G'][0]-P['B'][0]),8.8)
text(230,456,'COOLING LEG',10,'Bold');text(236,254,'HEATING LEG',10,'Bold');text(82,422,'UPCOMER',9,'Bold',align='right');text(505,391,'DOWNCOMER',9,'Bold')
tt=tr(local(AUX['expansion_tank']['end_xyz_mm']));text(tt[0]+37,tt[1]-19,'Expansion tank',9.5);text(tt[0]+37,tt[1]-33,'OD 203.200 / L 311.150',8.7,color=MUTED)
text(227,586,'TLEP 469.900',8.7);text(444,92,'BREP 469.900',8.7)
for h in D['hoses']:
 a=tr(local(h['bend_join_xyz_mm']));tx=a[0]+(16 if h['id']=='HOSE-A' else 40);ty=a[1]-8;line(*a,tx,ty+2,LINE);text(tx+3,ty,h['id'],8,color=MUTED)
text(388,75,'Drain valve',8.7);line(439,79,*tr(local(D['drain']['inlet_axis_end_xyz_mm'])),LINE)
x,y=tr(P['B']);line(x,y,x+37,y,INK,1);arrow([x+37,y],[-1,0],size=5);text(x+40,y-3,'+x',8.5);line(x,y,x,y+35,INK,1);arrow([x,y+35],[0,-1],size=5);text(x+4,y+38,'+y',8.5)
for name in ['upcomer','cooler','downcomer','heater']:
 a=P[SG[name]['from_tag']];b=P[SG[name]['to_tag']];m=tr(a+.48*(b-a));v=(b-a)/np.linalg.norm(b-a);line(*(m-v*10),*(m+v*10),MUTED,1);arrow(m+v*10,-v,MUTED,5)
heading('Straight axis-end spans',648,744,509)
y=table(['Leg / direction','Length','|dx|','|dy|'],[[name.title()+' '+SG[name]['from_tag']+'-'+SG[name]['to_tag'],F(sl(name))+('*' if name=='heater' else ''),F(abs(SG[name]['dx_mm'])),F(abs(SG[name]['dy_mm']))] for name in ['upcomer','cooler','downcomer','heater']],648,723,[193,110,103,103],9.2)
y=para('Inclined cylindrical axes: <b>10.800°</b> to horizontal.<br/>* H-A is a projected axial span. Heater pieces overlap by <b>7.202 mm</b> and their axes are offset <b>0.152 mm</b>; no healed continuous centerline is asserted.',648,y-14,509,9.7)
heading('Datum and coordinates',648,y-27,509)
y=para('<b>B = (0, 0, 0)</b> in the local drawing frame.<br/>CAD B = ('+point_text(O)+') mm.<br/><b>x = B<sub>Z</sub> - CAD Z</b>, rightward.<br/><b>y = CAD Y - B<sub>Y</sub></b>, upward.<br/><b>n = CAD X - B<sub>X</sub></b>, out of the view.',648,y-47,509,9.7)
heading('Color and geometry conventions',648,y-25,509)
y=para('Blue outlines: jacket shell and end plates only. Red outlines: four modeled heater clamps only. Main pipes and coolant hoses remain gray. Electrically active heater boundaries are not encoded. All visible outlines are projected CAD edges; centerlines and annotations are derived overlays.',648,y-45,509,9.4)
heading('Drawing set',648,y-27,509)
y=table(['Sheet','Contents'],[['2','Corner offsets, heights and virtual corner spans'],['3','Jacket length, pre/post lengths, radii and diameters'],['4','Heater clamps, exit-pipe interfaces and tank'],['5','Sensor locations with nearest-end labels'],['6','Sensor distances, contact ambiguity and sources'],['7','Ordered main-loop and sensor coordinates'],['8','Auxiliary coordinates, source evidence and Rev8 changes']],648,y-46,[50,459],8.7,rowh=[20]*8)
note('Main overview scale 1:14 at A3. Sensor hardware is represented by geometric reference markers on Sheet 5. Out-of-plane hoses and valve are projected; use 3D coordinates when modeling.',32,131,285,8.4)
finish()
# 2 - corner enlargements, dx/dy and exact vs reconstructed bends.
page(2,'Corners, vertical heights and length definitions','A-H are cylinder-axis endpoints. VLL/VUL/VUR/VLR are virtual intersections of extended straight axes, not physical corner points.')
for j,(title,aa,bb,path) in enumerate([('Lower left','A','B',MAIN[0]),('Upper left','C','D',MAIN[0]),('Upper right','E','F',MAIN[1]),('Lower right','G','H',MAIN[1])]):
 x=32+j*282;heading(title+' / '+aa+'-'+bb,x,744,257);mid=(P[aa]+P[bb])/2;sc=1.25
 tr=view(x+115-mid[0]*sc,625-mid[1]*sc,sc,paths=[path],clip=(x,541,257,173));tag(aa,P[aa],tr,-20,-12);tag(bb,P[bb],tr,8,7)
 s=next(s for s in D['segments'] if s['from_tag']==aa);hdim(P[aa],P[bb],tr,550,'|dx| '+F(abs(s['dx_mm'])),8);vdim(P[aa],P[bb],tr,x+237,'|dy| '+F(abs(s['dy_mm'])),8)
 text(x+3,522,'Endpoint chord '+F(s['chord_mm']),9)
 if s['centerline_length_mm']:
  text(x+3,505,'Arc '+F(s['centerline_length_mm'])+' / R '+F(s['bend_radius_mm'])+' / '+F(s['bend_angle_deg'],1)+'°',8.7)
  text(x+3,489,'Pipe envelope: inner R 40.4495 / outer R 73.8505',8,color=MUTED)
 else:
  text(x+3,505,'Recovered spine '+F(s['recovered_spine_length_mm'])+'*',8.7,color=AMBER)
  text(x+3,489,'Spline geometry; not an exact circular elbow',8,color=MUTED)
heading('Signed changes in clockwise traversal order',32,468,710)
rows=[]
for s in D['segments']:
 ll=F(s['reference_length_mm'])+('†' if s['segment']=='heater' else '') if s['reference_length_mm'] is not None else F(s['recovered_spine_length_mm'])+'*'
 rows.append([s['from_tag']+'-'+s['to_tag'],s['segment'].replace('_',' ').title(),F(s['dx_mm']),F(s['dy_mm']),F(s['dn_mm'],6),ll])
y=table(['Ends','Segment','dx','dy','dn','Axial / arc length'],rows,32,447,[54,174,112,112,110,148],8.9,rowh=[24]+[23]*8)
note('* G-H: recovered support-spine length 98.266; endpoint residuals G 0.169 / H 0.146 mm. Its exact endpoint chord is 86.619 mm. † H-A: projected span; the two unique cylinders sum to 1,353.699 mm but overlap by 7.202 mm with 0.152 mm transverse offset. Neither qualified value is an exact continuous hydraulic length.',32,y-12,710,9)
heading('Corner heights relative to B',776,468,381)
rows=[[r['tag'],F(r['local_xyz_mm'][0]),F(r['local_xyz_mm'][1])] for r in D['corner_points']]
y2=table(['Point','x','Vertical height y'],rows,776,447,[55,156,170],9,rowh=[24]+[21]*8)
hs=[r['local_xyz_mm'][1] for r in D['corner_points']]
note('D is the highest listed axis endpoint: '+F(max(hs))+'. H is lowest: '+F(min(hs))+'. Endpoint height range: '+F(max(hs)-min(hs))+' mm. Actual curved apex/extents differ; this is not an evaluated buoyancy head.',776,y2-12,381,9)
heading('Virtual sharp-corner spans / axes extended to intersections',32,170,1125)
rows=[[s['leg'].title(),s['from']+' → '+s['to'],F(s['dx_mm']),F(s['dy_mm']),F(s['projected_axis_intersection_length_mm'])] for s in D['virtual_corner_spans']]
table(['Leg','Virtual endpoints','dx','dy','Intersection-to-intersection length'],rows,32,150,[167,237,174,174,373],8.5,rowh=[19]*5)
finish()
# 3 - cooler detail plus complete diameter chart.
page(3,'Cooler, cooling jacket and all tube diameters','D→E stationing. Complete jacket = shell + both end plates. Thermal effectiveness and active cooling length are not inferred from this envelope.')
x0,y0,k=84,646,.72;L=sl('cooler');js=J['pre_mm'];je=js+J['complete_mm'];tr=lambda p:np.array([x0+k*p[0],y0+k*p[1]])
box(x0+k*js,y0-J['shell_Ro_mm']*k,J['complete_mm']*k,2*J['shell_Ro_mm']*k,HexColor('#edf6fc'),BLUE)
box(x0+k*(js+6.35),y0-J['shell_Ri_mm']*k,J['shell_mm']*k,2*J['shell_Ri_mm']*k,white,BLUE)
box(x0,y0-16.7005*k,L*k,33.401*k,HexColor('#d8dde1'),WALL)
line(x0,y0,x0+L*k,y0,MUTED,.5,[4,2])
for port in D['ports']:
 pp=local(port['axis_end_xyz_mm'])-local(port['axis_start_xyz_mm']);vv=P['E']-P['D'];sgn=1 if np.dot(pp,np.array([-vv[1],vv[0]]))>0 else -1
 px=x0+k*port['station_from_D_mm'];line(px,y0+sgn*44.45*k,px,y0+sgn*92*k,WALL,5);text(px+7,y0+sgn*81*k+(-14 if sgn<0 else 0),port['id'],8.5)
for a,b,off,label in [(0,js,89,'Pre '+F(js)),(js,je,89,'Complete jacket '+F(J['complete_mm'])),(je,L,89,'Post '+F(J['post_mm'])),(0,L,-88,'D-E '+F(L)),(js+6.35,je-6.35,-55,'Shell only '+F(J['shell_mm']))]:dimension([a,0],[b,0],tr,off,label,9)
tag('D',[0,0],tr,-18,-3);tag('E',[L,0],tr,8,-3)
text(32,535,'Straightened section schematic. Gray pipe envelope has no modeled bore. End plates: 6.350 thick each. Jacket annulus radial gap: 22.2631; concentric unobstructed hydraulic diameter: 44.5262.',8.35,color=MUTED)
heading('Analytical cylinder radii and diameters',32,510,1125)
rows=[[r['item'],F(r['outer_radius_mm'],4),F(r['inner_radius_mm'],4),F(r['outer_diameter_mm'],4),F(r['inner_diameter_mm'],4),r['source_path']+' / '+r['faces']] for r in D['diameters']]
y=table(['Component','Outer radius','Inner radius','OD','ID / hole','CAD instance / face evidence'],rows,32,489,[223,103,103,103,103,490],8.1,rowh=[23]+[18.3]*len(rows))
note('“–” means not encoded. End-plate ID is a clearance hole. Port OD is the cylindrical land, excluding thread detail. Local sensor-spool bores differ and do not establish the main-loop bore. All analytical cylindrical faces, including fittings, are in the CSV package.',32,y-9,1125,8.6)
heading('Jacket end planes and coolant-port crossings',32,169,1125)
rows=[['J-IN / complete jacket inlet plane',point_text(J['outer_start_xyz_mm']),F(js)],['J-OUT / complete jacket outlet plane',point_text(J['outer_end_xyz_mm']),F(je)]]
for p in D['ports']:rows.append([p['id']+' axis crossing of main pipe axis',point_text(p['axis_crossing_on_cooler_xyz_mm']),F(p['station_from_D_mm'])])
table(['Feature','CAD X, Y, Z at axis','Station from D'],rows,32,151,[360,532,233],8.4,rowh=[17]*5)
text(32,58,'Port-axis spacing 914.400. Port A is 57.150 from J-IN; Port B is 58.738 from J-OUT. Both port bore axes are 50.800 long. Out-of-plane port inclination is retained in the coordinate files.',8,color=MUTED)
finish()
# 4 - heater clamp locations and branch interfaces.
page(4,'Heater hardware, exit pipes and tank','Heater clamps are located directly from their CAD bore axes. Mechanical spans are distinct from the unknown energized length.')
x0,y0,k=87,670,.72;L=sl('heater');tr=lambda p:np.array([x0+k*p[0],y0+k*p[1]])
line(x0,y0,x0+L*k,y0,WALL,7);line(x0,y0,x0+L*k,y0,MUTED,.5,[4,2]);tag('H',[0,0],tr,-18,-3);tag('A',[L,0],tr,8,-3)
for c in CL:
 x=x0+k*c['station_start_from_H_mm'];box(x,y0-17,c['axial_width_mm']*k,34,HexColor('#fae9e6'),RED);text(x+k*c['axial_width_mm']/2,y0-35,c['id'],9,'Bold',RED,'center')
dimension([0,0],[L,0],tr,64,'H-A projected axial span '+F(L),9.5)
for a,b in zip(CL,CL[1:]):dimension([a['station_from_H_mm'],0],[b['station_from_H_mm'],0],tr,35,F(b['station_from_H_mm']-a['station_from_H_mm']),8.5,RED)
dimension([CL[0]['station_start_from_H_mm'],0],[CL[-1]['station_end_from_H_mm'],0],tr,-58,'Outer clamp-edge span '+F(HE['outer_clamp_outer_edge_span_mm'])+' / mechanical only',9,RED)
text(32,590,'Each clamp: axial width 50.800; bore radius 16.7000; curved outer radius 21.9075 (the overall block is not a cylinder). Red denotes clamp hardware only.',8.6,color=MUTED)
rows=[[c['id'],sp(c['path']),F(c['station_from_H_mm']),F(c['station_start_from_H_mm'])+' / '+F(c['station_end_from_H_mm']),point_text(c['axis_center_xyz_mm'])] for c in CL]
y=table(['Clamp','CAD instance','Center s from H','Start / end s from H','CAD X, Y, Z of bore-axis center'],rows,32,571,[82,127,154,244,518],8.7,rowh=[22]+[20]*4)
note('Outermost clamp-center span: 1,104.900 mm. CAD does not identify wiring, clamp electrical roles or active heat-flux boundaries. Clamp endpoint coordinates are also supplied in CSV. Sensor stations along H-A are on Sheets 5-7.',32,y-9,1125,9)
for idx,name in enumerate(['TLEP','BREP']):
 x=32+idx*298;ref='D' if name=='TLEP' else 'H';center=local(AUX[name]['start_xyz_mm']);sc=1.35;heading(name+' connection',x,413,270)
 tr=view(x+105-center[0]*sc,323-center[1]*sc,sc,paths=[MAIN[0] if name=='TLEP' else MAIN[1],'/NAUO3' if name=='TLEP' else '/NAUO5'],clip=(x,249,270,140));tag(ref,P[ref],tr,-24,-18);tag('IN',center,tr,11,9)
 delta=AUX[name]['start_delta_from_corner_local_mm'];text(x,233,'IN from '+ref+': dx '+F(delta[0])+' / dy '+F(delta[1]),8.5)
 c=next(v for v in D['branch_connections'] if v['component']==name);text(x,218,'Extended-axis crossing: '+ref+' + '+F(c['main_station_from_start_mm']),8.5,color=MUTED)
heading('Exit and tank cylinders',650,413,507)
y=table(['Component','Length','OD','ID'],[[name.replace('_',' ').title(),F(AUX[name]['length_mm']),F(2*AUX[name]['outer_radius_mm']),F(2*AUX[name]['inner_radius_mm'])] for name in ['TLEP','BREP','expansion_tank']],650,394,[205,108,95,99],8.8,rowh=[23]*4)
y=para('Exit and tank axes are tilted <b>10.800° from vertical</b>. Both exit IN planes are 4.0005 mm outward from the extended main-axis crossing. Crossings are geometric constructions; they do not assert ideal hydraulic tees.',650,y-12,507,9.2)
para('TLEP-OUT and tank-IN coincide within extraction tolerance. Tube and tank axes retain their tiny CAD out-of-plane components. IN/OUT order means near/far from the loop, not a prescribed branch flow.',650,y-13,507,9.1)
heading('CAD-coordinate exit and tank endpoint schedule',32,194,1125)
rows=[]
for name in ['TLEP','BREP','expansion_tank']:
 for end in ['start','end']:
  r=AUX[name];label=name.replace('expansion_tank','TANK')+('-IN' if end=='start' else '-OUT');rows.append([label,*[F(v) for v in r[end+'_xyz_mm']],sp(r['source_path'])+' / F'+str(r['source_outer_face'])])
table(['Endpoint','CAD X','CAD Y','CAD Z','CAD source'],rows,32,177,[221,191,191,191,331],8.6,rowh=[17]*7)
finish()
# 5 - Sensor reference map.
page(5,'Sensor locations and nearest-corner distances','Colored symbols mark sensor types. Main-loop stations are projected to the pipe axis; callouts give along-axis distance to the nearest leg endpoint.')
tr=view(202,250,.29,paths=MAIN+['/NAUO18/']);centerlines(tr)
for t in P:
 dx,dy=(-20,-18) if t=='A' else (7,8);tag(t,P[t],tr,dx,dy)
# Leaders are placed for this Rev9 geometry; main PTC diamonds stay exactly on axis.
pos={'STC-02':(43,294),'STC-03':(43,383),'STC-04':(43,465),'STC-05':(43,533),'LF-01':(50,594),'STC-06':(261,697),'PTC-01':(390,726),'STC-07':(548,657),'LF-03':(611,613),'PTC-03':(675,579),'STC-08':(663,497),'STC-09':(663,433),'STC-10':(663,353),'STC-11':(663,277),'LF-04':(688,209),'PTC-X':(671,171),'STC-12':(578,125),'PTC-04':(536,91),'LF-02':(309,149),'PTC-02':(256,115),'STC-01':(62,198),'JTC-A':(328,545),'JTC-B':(447,586)}
for sid,s in S.items():
 pp=local(s['actual_reference_xyz_mm']) if sid.startswith('JTC') else local(s['projected_axis_xyz_mm']);x,y=tr(pp)
 if sid in ['LF-02','LF-03','LF-04']:y+=10
 typ=sensor_type(s);sensor_symbol(x,y,typ,8.5 if typ=='LF' else 7.3);tx,ty=pos[sid];co=BLUE if typ=='LF' else GREEN if typ=='PTC' else WALL
 line(x,y,tx+14,ty+4,LINE,.6)
 star='*' if s.get('number_contact_solutions',1)>1 else ''
 label=sid+star+(' / port' if sid.startswith('JTC') else '  '+s['nearest_endpoint']+' '+F(s['nearest_distance_mm']))
 text(tx,ty,label,8.6,'Bold',co)
heading('Symbols and coordinate meaning',832,744,325)
for yy,typ,label in [(713,'LF','LF / Luna fiber mount'),(681,'PTC','PTC / penetrating TC mount'),(649,'STC','STC / pipe reference point')]:sensor_symbol(846,yy+3,typ,8);text(864,yy,label,9.6)
y=para('JTC-A/B are additional coolant-port thermocouples. Their markers locate mounting references near the two jacket nipples, rather than the main loop.',832,624,325,9.8)
y=para('Green main-loop diamonds remain on the extracted pipe axes. Larger blue moons are offset slightly at shared mounts. Full 3D reference coordinates, including out-of-plane offsets, are preserved in the data.',832,y-15,325,9.8)
heading('Rev9 sensor inventory',832,y-28,325)
y=para('<b>12 STC + 4 LF + 5 loop PTC + 2 JTC</b><br/>LF-02/PTC-02, LF-03/PTC-03 and LF-04/PTC-X share mounting bodies. <b>PTC-X is new</b> relative to the Rev8 map; its acquisition-channel number is unknown.',832,y-48,325,9.8)
heading('Reference qualifications',832,y-28,325)
y=para('STC coordinates use one returned closest point on the pipe solid. An asterisk flags multiple equally close solutions. <b>STC-01 has a 1.0455 mm body-to-pipe gap</b>; its pipe reference is not a point of physical contact.',832,y-48,325,9.6)
y=para('LF/PTC/JTC references use local mounting-body centroids. Neither actual TC junctions nor optical sensing extents are defined. IDs follow the prior collaborator convention by region/order; STEP does not encode channel names.',832,y-14,325,9.6)
note('Clockwise order: B-C-D-E-F-G-H-A-B. Distances are from selected geometric references to axial corner endpoints, not from sensor tips. Only the jacket shell/end plates are blue CAD outlines; blue moons indicate LF sensors.',32,75,757,8.7)
finish()
# 6 - Unrolled distance schedules and per-sensor source IDs.
page(6,'Sensor stations, distance ranges and CAD references','s = distance from the first endpoint of the named leg. To end = remaining axial coordinate. Main-loop stationing never adds a corner arc.')
plotx,plotw,ploty=139,954,716
for i,name in enumerate(['upcomer','cooler','downcomer','heater']):
 y=ploty-i*36;sg=SG[name];L=sl(name);text(32,y-3,name.title(),9,'Bold');line(plotx,y,plotx+plotw,y,LINE,1);text(plotx-7,y-3,sg['from_tag'],8,'Bold',align='right');text(plotx+plotw+7,y-3,sg['to_tag'],8,'Bold')
 for s in D['sensors']:
  if s['segment']!=name:continue
  typ=sensor_type(s);xx=plotx+plotw*s['station_from_start_mm']/L;yy=y+{'STC':0,'LF':8,'PTC':-8}[typ];sensor_symbol(xx,yy,typ,5.5)
  rg=s.get('minimum_distance_solution_station_range_mm')
  if rg and rg[1]-rg[0]>.01:line(plotx+plotw*rg[0]/L,y,plotx+plotw*rg[1]/L,y,WALL,2.5)
text(32,570,'Type lanes separate overlapping stations. Dark bars show the returned STC closest-point station range; they do not establish a sensing footprint.',8.7,color=MUTED)
rows=[]
for s in D['sensors']:
 if s['domain']!='main_loop':continue
 rg=s.get('minimum_distance_solution_station_range_mm');multiple=s.get('number_contact_solutions',1)>1
 alt=(F(rg[0])+'–'+F(rg[1])) if multiple else 'One returned point' if s['sensor_type']=='STC' else 'Mount centroid'
 rows.append([s['sensor_id']+('*' if multiple else ''),s['segment_start']+'-'+s['segment_end'],F(s['station_from_start_mm']),F(s['distance_to_end_mm']),s['nearest_endpoint']+' / '+F(s['nearest_distance_mm']),alt,s['source_cad_path']])
y=table(['Sensor','Leg','s from start','To end','Nearest end / distance','STC range / other basis','CAD assembly'],rows,32,551,[86,58,125,120,168,301,267],8.5,rowh=[23]+[17.6]*len(rows))
note('STC-01*: 1.0455 mm separation from pipe; the table uses its closest pipe point. STC-06/07/12* have multiple returned points. H-A values use the projected axial coordinate despite overlapping offset pieces. Every returned solution and both body/pipe points are in Contact_Solutions.csv.',32,y-10,1125,8.7)
rows=[]
for sid in ['JTC-A','JTC-B']:
 s=S[sid];rows.append([sid,s['segment'],F(s['station_from_start_mm']),F(-s['distance_to_end_mm']),F(s['axis_radial_offset_mm']),s['source_cad_path']])
table(['Jacket TC','Port axis','From inner bore end','Beyond outer bore end','Radial axis offset','CAD assembly'],rows,32,112,[115,158,223,241,181,207],8.2,rowh=[18]*3)
finish()
# 7 - Main sequence with actual reference coordinates.
page(7,'Ordered main-loop and sensor coordinates','Traverse B→C→D→E→F→G→H→A→B. Sensor coordinates are selected pipe or mounting references; the projected axis coordinates are separate CSV columns.')
rows=[]
for r in D['sequential_coordinates'][:39]:
 label=r['tag'].replace('expansion_tank','TANK');rows.append([label,r['kind'],*[F(v) for v in r['CAD_xyz_mm']],*[F(v) for v in r['local_xyz_mm']],r['reference'].replace('_',' ')])
y=table(['ID','Point basis','CAD X','CAD Y','CAD Z','Local x','Height y','Normal n','Leg / reference'],rows,32,748,[95,84,117,118,118,115,113,100,265],8.15,rowh=[24]+[15.35]*len(rows))
note('Exact frame: x = '+F(O[2],9)+' - CAD Z; y = CAD Y - ('+F(O[1],9)+'); n = CAD X - '+F(O[0],9)+'. Coordinates are rounded only for printing. Full floating-point values, 57 point records, probe endpoints, all component axes and evidence paths are supplied in JSON/CSV.',32,y-12,1125,8.9)
note('STC = selected nearest pipe-surface point, not necessarily the sensing junction or a point on the STC body. J-IN/J-OUT = complete jacket outer planes at its axis. TANK-IN/TANK-OUT = lower/upper outer-cylinder axial planes. Auxiliary endpoints continue on Sheet 8; heater clamp centers are on Sheet 4.',32,y-49,1125,8.7)
finish()
# 8 - Source, changes, qualifications and auxiliary coordinate schedule.
page(8,'Source evidence, auxiliary coordinates and Rev9 changes','Rev9 values come from the attached STEP only. Rev8 values below are an explicitly separate comparison with the earlier CAD extraction.')
heading('Source identity and extraction checks',32,744,556)
y=para('<b>'+D['source_file']+'</b><br/>STEP internal file: UTDTloopWithOpticsAndHXRev9_9_18_26.STEP<br/>Export timestamp: 2026-10-06T16:40:01 / SolidWorks 2026 / AP214<br/>Native length unit: millimetres. Source SHA-256:',32,724,556,8.8)
text(32,y-14,D['source_sha256'][:32],8.5,'Mono');text(32,y-27,D['source_sha256'][32:],8.5,'Mono')
y=para('99 assembly records were traversed with recursive placement transforms. An independent STEP reload checked 12 long main-pipe face bounds against boundary-vertex projections: maximum discrepancy below 0.000001 mm. Three analytical torus centerlines join their axis endpoints to the same tolerance. These are extraction checks, not manufacturing tolerances.',32,y-39,556,9)
rows=[['Main upcomer / cooling leg','NAUO1/NAUO62'],['Main downcomer / heating leg','NAUO2/NAUO61'],['Shell / end plates / ports','NAUO18: NAUO56 / 57,58 / 59,60'],['Clamps / hoses / drain body','NAUO25–28 / 30,31 / 32']]
y=table(['Component family','Path below assembly root'],rows,32,y-13,[260,296],8.2,rowh=[20]*5)
note('Face numbers refer to the imported OCCT face sequence for this hashed file. Full assembly paths and face radii/bounds are retained in the package. PDF dimensions never override Rev9 CAD.',32,y-9,556,8.6)
heading('Auxiliary 3D axis endpoint coordinates',32,373,556)
rows=[]
for r in D['sequential_coordinates'][43:]:rows.append([r['tag'],*[F(v) for v in r['CAD_xyz_mm']]])
y=table(['Endpoint / bend join','CAD X','CAD Y','CAD Z'],rows,32,353,[160,131,133,132],8.1,rowh=[21]+[16]*len(rows))
note('Hose labels IN/BEND/OUT identify modeled axis endpoints, not verified fluid-network connectivity. DRAIN-J is the inlet-cylinder end; DRAIN-C1/C2 bound the crossbody cylinder. Nonzero normal offsets are preserved.',32,y-9,556,8.3)
heading('Changes relative to Rev8',621,744,536)
rows=[]
for c in D['rev8_dimension_comparison']:
 nm=c['quantity'].replace('_straight_reference_length',' span').replace('jacket_','Jacket ').replace('_mm','').replace('complete','complete').replace('_',' ')
 rows.append([nm.title(),F(c['rev8_mm']),F(c['rev9_mm']),F(c['delta_mm'])])
y=table(['Dimension','Rev8','Rev9','Change'],rows,621,724,[197,113,113,113],8.2,rowh=[22]+[19]*len(rows))
y=para('Rev9 inclination is 10.800° (Rev8: 10.000°). STC-05 is now on the upcomer. Rev9 adds four heater clamps, two hose bodies, drain-valve hardware and PTC-X at LF-04. Comparison CSVs use each revision’s own B datum; raw assembly translations are not treated as physical movement.',621,y-12,536,9)
heading('Computational-model qualifications',621,y-26,536)
y-=46
for title,body in [('Bores and heated boundaries','Main swept-pipe and hose bores are absent. Local fitting/spool IDs are not a loop-wide ID. Clamp geometry locates hardware but not energized boundaries.'),('Unhealed joins and sensor references','H-A pieces overlap 7.202 mm with 0.152 mm axis offset. G-H recovered spine has 0.169/0.146 mm endpoint residuals. STC-01 has a 1.0455 mm gap; physical sensing junctions and PTC-X channel ID remain unknown.')]:
 text(621,y,title,9.2,'Bold');y=para(body,621,y-10,536,8.8)-17
heading('Auxiliary lengths and probe geometry',621,y-4,536)
rows=[['Each HX hose','304.800 straight + R76.200 × 180° arc = 544.189'],['Drain body axes','Inlet 25.400 / crossbody 292.100'],['PTC-01 / PTC-04 / JTC-A,B','Sheath length 158.750 / OD 3.175'],['PTC-02 / PTC-03 / PTC-X','Sheath length 152.400 / OD 3.175']]
y=table(['Part / group','CAD dimension (mm unless marked)'],rows,621,y-24,[221,315],8.2,rowh=[21]*5)
note('Sheath endpoints are geometric shaft ends, not verified TC junctions. Drain geometry is simplified; passage connectivity and valve loss coefficient are not established.',621,y-9,536,8.6)
note('Companion data: explicit units, coordinate frame, source filenames/paths, nulls for unknowns, segment/diameter/station tables and extraction scripts. The source STEP and hash are included for reproducibility.',621,90,536,8.6)
finish()
C.save();print(OUT)
