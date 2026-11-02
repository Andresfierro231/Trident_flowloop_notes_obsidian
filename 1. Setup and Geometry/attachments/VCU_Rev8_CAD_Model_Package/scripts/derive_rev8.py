"""Derive comparisons solely from freshly extracted per-revision CAD records."""
from pathlib import Path
import json,csv,math
import numpy as np
R=Path(__file__).resolve().parents[1];O=R
norm=np.linalg.norm
def arr(v):return np.array(v,dtype=float)
def csvout(name,rows):
 if not rows:return
 keys=list(dict.fromkeys(k for r in rows for k in r))
 with (O/'data'/(name+'.csv')).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
def cols(prefix,v):return {f'{prefix}_{a}_mm':float(x) for a,x in zip('XYZ',v)}
def local(p,origin):return ((arr(p)-origin)[[2,1,0]]*[-1,1,1]).tolist()
models={};cornerrows=[];segmentrows=[];sensorrows=[];shaftrows=[];componentrows=[];features=[];axisrows=[];auxrows=[]
for rev in ['rev8']:
 d=json.loads((O/'raw'/f'{rev}.json').read_text());rr=d['records'];main=[r for r in rr if r['definition'].startswith('MSRloop')]
 # Merge only contiguous, collinear cylindrical outer faces on each main-pipe axis.
 groups=[]
 for r in main:
  for c in r['cylinders']:
   if abs(c['radius_mm']-16.7005)>.01:continue
   axisrows.append({'revision':rev,'part_path':r['path'],'face':c['face'],'radius_mm':c['radius_mm'],**cols('start_CAD',c['start_xyz_mm']),**cols('end_CAD',c['end_xyz_mm']),'length_mm':c['vmax']-c['vmin'],'source_file':d['source_file']})
   if c['vmax']-c['vmin']<20:continue # short connection stubs, retained in raw axis table
   a,b=arr(c['start_xyz_mm']),arr(c['end_xyz_mm']);v=(b-a)/norm(b-a)
   found=None
   for g in groups:
    if norm(np.cross(v,g['v']))<1e-6 and norm(np.cross(a-g['a'],g['v']))<.5:
     found=g;break
   if found is None:
    found={'a':a,'v':v,'points':[],'evidence':[],'spans':[]};groups.append(found)
   found['points'] += [a,b];found['evidence'].append(r['path']+f"/Face{c['face']}")
   if not any(norm(a-p)<.001 and norm(b-q)<.001 for p,q in found['spans']):found['spans'].append((a,b))
 assert len(groups)==4,[(g['a'].tolist(),g['v'].tolist()) for g in groups]
 for g in groups:
  pr=sorted(g['points'],key=lambda p:np.dot(p-g['a'],g['v']));g['ends']=[pr[0],pr[-1]]
 vert=[g for g in groups if abs(g['v'][1])>.99];incl=[g for g in groups if abs(g['v'][2])>.9]
 assert len(vert)==len(incl)==2
 up,down=sorted(vert,key=lambda g:-np.mean(g['ends'],axis=0)[2])
 heater,cooler=sorted(incl,key=lambda g:np.mean(g['ends'],axis=0)[1])
 def byY(g):return sorted(g['ends'],key=lambda p:p[1])
 hp=byY(heater);cp=byY(cooler);upoints=byY(up);dp=byY(down)
 points={'A':hp[1],'B':upoints[0],'C':upoints[1],'D':cp[1],'E':cp[0],'F':dp[1],'G':dp[0],'H':hp[0]}
 origin=points['B'].copy() # Corresponding geometric datum, no best-fit registration.
 naming={'A':('lower_left','heater_outlet',heater),'B':('lower_left','upcomer_inlet',up),'C':('upper_left','upcomer_outlet',up),'D':('upper_left','cooler_inlet',cooler),'E':('upper_right','cooler_outlet',cooler),'F':('upper_right','downcomer_inlet',down),'G':('lower_right','downcomer_outlet',down),'H':('lower_right','heater_inlet',heater)}
 for tag,p in points.items():
  corner,name,g=naming[tag];q=local(p,origin)
  cornerrows.append({'revision':rev,'tag':tag,'corner':corner,'tangent':name,**cols('CAD',p),'x_mm':q[0],'height_y_mm':q[1],'normal_z_mm':q[2],'source_file':d['source_file'],'reference_basis':'Outer-cylinder axis endpoint at straight/bend tangent','cad_faces':'; '.join(g['evidence'])})
 specs=[('heater','H','A',heater),('lower_left_bend','A','B',None),('upcomer','B','C',up),('upper_left_bend','C','D',None),('cooler','D','E',cooler),('upper_right_bend','E','F',None),('downcomer','F','G',down),('lower_right_bend','G','H',None)]
 segs=[]
 for name,a,b,g in specs:
  p,q=points[a],points[b];dv=q-p;lv=arr(local(q,p));chord=float(norm(dv));length=sum(float(norm(y-x)) for x,y in g['spans']) if g else chord;basis='sum of unique cylindrical-axis lengths' if g and len(g['spans'])>1 else 'straight centerline';radius=None;angle=None;ev='; '.join(g['evidence']) if g else ''
  join_gap=0.
  if g and len(g['spans'])>1:
   join_gap=min(float(norm(x-y)) for x in g['spans'][0] for y in g['spans'][1])
   if join_gap>.001:basis+='; offset joint retained, no healing'
  if g is None:
   basis='endpoint chord only; exact centerline arc not established';length=None
   candidates=[]
   for r in main:
    for t in r.get('tori',[]):
     c=arr(t['center_xyz_mm']);rad=t['major_radius_mm']
     if abs(norm(p-c)-rad)<.01 and abs(norm(q-c)-rad)<.01:
      candidates.append((r,t))
   if candidates:
    r,t=candidates[0];radius=t['major_radius_mm'];angle=abs(t['umax']-t['umin']);length=radius*angle;basis='exact torus centerline arc';ev=r['path']+f"/Face{t['face']}"
  row={'revision':rev,'segment':name,'from_tag':a,'to_tag':b,**cols('start_CAD',p),**cols('end_CAD',q),**cols('delta_CAD',dv),'dx_mm':lv[0],'dy_mm':lv[1],'dz_normal_mm':lv[2],'vertical_span_mm':abs(lv[1]),'horizontal_span_mm':abs(lv[0]),'chord_mm':chord,'centerline_length_mm':length,'axis_joint_gap_mm':join_gap,'bend_radius_mm':radius,'bend_angle_deg':None if angle is None else math.degrees(angle),'length_basis':basis,'source_file':d['source_file'],'cad_faces':ev};segmentrows.append(row);segs.append(row)
 # Every mount and every surface sensor is visited, including nested holders.
 sensors=[]
 for r in rr:
  entries=[]
  if 'surface_contact' in r:
   p=r['surface_contact']['pipe_xyz_mm'];entries=[('STC',p,'Nearest point on main-pipe solid to modeled surface thermocouple')]
  elif 'mount_reference' in r:
   p=r['mount_reference']['xyz_mm'];typ=r['definition']
   entries=([('LF',p,'Fiber-holder mount-body centroid; not optical sensing range')]+([('PTC',p,'Combined LF/PTC mount-body centroid; not sensing junction')] if typ=='Fiber_Holder_30deg' else [])) if typ.startswith('Fiber_Holder') else [('PTC',p,'TC mount-body centroid; not sensing junction')]
  for typ,p,basis in entries:
   q=local(p,origin)
   md=r.get('mount_to_main_pipe');jd=r.get('mount_to_jacket')
   domain='main_loop'
   if typ=='PTC' and md and md['distance_to_solid_mm']>20:domain='off_loop_candidate'
   row={'revision':rev,'sensor_type':typ,'domain':domain,**cols('CAD',p),'x_mm':q[0],'height_y_mm':q[1],'normal_z_mm':q[2],'reference_basis':basis,'assembly_definition':r['definition'],'assembly_path':r['path'],'reference_path':r.get('mount_reference',{}).get('path',r['path']),'surface_gap_mm':r.get('surface_contact',{}).get('gap_mm'),'distance_to_main_solid_mm':md['distance_to_solid_mm'] if md else r.get('surface_contact',{}).get('gap_mm'),'distance_to_jacket_solid_mm':jd['distance_to_solid_mm'] if jd else None,'source_file':d['source_file']}
   sensors.append(row)
 # Long small-radius TC cylinders: include mounted and any standalone modeled probes.
 shafts=[]
 for r in rr:
  if r['assembly'] or r['definition'] not in ['30TC TC','Temp_TC','Part1']:continue
  cc=[c for c in r.get('cylinders',[]) if abs(c['radius_mm']-1.5875)<.01 and c['vmax']-c['vmin']>40]
  if not cc:continue
  c=max(cc,key=lambda c:c['vmax']-c['vmin']);p,q=arr(c['start_xyz_mm']),arr(c['end_xyz_mm'])
  parents=[s for s in sensors if s['sensor_type']=='PTC' and r['path'].startswith(s['assembly_path']+'/')]
  row={'revision':rev,'part_path':r['path'],'part_definition':r['definition'],'parent_sensor_path':parents[0]['assembly_path'] if parents else None,**cols('shaft_start_CAD',p),**cols('shaft_end_CAD',q),'length_mm':float(norm(q-p)),'radius_mm':c['radius_mm'],'face':c['face'],'source_file':d['source_file'],'basis':'Geometric shaft endpoints; sensing junction not encoded'};shaftrows.append(row);shafts.append(row)
  if not parents:
   mid=(p+q)/2;v=local(mid,origin);sensors.append({'revision':rev,'sensor_type':'unassigned_TC','domain':'unassigned','CAD_X_mm':mid[0],'CAD_Y_mm':mid[1],'CAD_Z_mm':mid[2],'x_mm':v[0],'height_y_mm':v[1],'normal_z_mm':v[2],'reference_basis':'Unassigned modeled shaft midpoint; see shaft endpoint table','assembly_definition':r['definition'],'assembly_path':r['path'],'reference_path':r['path'],'source_file':d['source_file']})
 # Temporary neutral IDs follow flow around the loop. They are not DAQ channels.
 def station(s):
  p=arr([s[f'CAD_{a}_mm'] for a in 'XYZ']);best=(1e99,0);offset=0.
  for seg in segs:
   a=points[seg['from_tag']];b=points[seg['to_tag']];v=b-a;t=np.clip(np.dot(p-a,v)/np.dot(v,v),0,1);dist=norm(p-(a+t*v))
   if dist<best[0]:best=(dist,offset+t*norm(v))
   offset+=norm(v)
  return best[1]
 for typ in ['STC','LF','PTC','unassigned_TC']:
  subset=sorted([s for s in sensors if s['sensor_type']==typ],key=station)
  for i,s in enumerate(subset,1):s['sensor_id']=f'{typ}-{i:02d}';s['label_basis']='Drawing-local type/order ID; no experimental channel mapping asserted'
 for s in sensors:
  if s['sensor_type']=='STC':
   n=int(s['sensor_id'].split('-')[1]);s['sensor_id']=f'STC-{12 if n==1 else n-1:02d}'
  elif s['sensor_type']=='LF':s['sensor_id']={'LF-01':'LF-02','LF-02':'LF-01','LF-03':'LF-03','LF-04':'LF-04'}[s['sensor_id']]
  elif s['sensor_type']=='PTC':
   maps={'rev8':{'PTC-01':'PTC-04','PTC-02':'PTC-02','PTC-03':'PTC-01','PTC-04':'JTC-A','PTC-05':'JTC-B','PTC-06':'PTC-03'},'rev7':{'PTC-01':'PTC-02','PTC-02':'R7-TC-A','PTC-03':'JTC-A','PTC-04':'JTC-B','PTC-05':'PTC-03','PTC-06':'R7-TC-B'}}
   s['sensor_id']=maps[rev][s['sensor_id']]
  else:s['sensor_id']='R7-TC-extra'
  s['label_basis']='Comparison labels; STC/LF/PTC ordering follows collaborator schema by loop region, not verified DAQ channels; JTC/R7 labels supplemental'
 sensorrows+=sensors
 for r in rr:
  if r['definition'] not in ['Pipe8in','3in3ftCutSS_44635K443','expansiontank']:continue
  c=max(r['cylinders'],key=lambda c:c['radius_mm']);p=arr(c['start_xyz_mm']);q=arr(c['end_xyz_mm'])
  if p[1]>q[1]:p,q=q,p
  name={'Pipe8in':'TLEP' if (p[1]+q[1])/2>origin[1] else 'BREP','3in3ftCutSS_44635K443':'cooling_jacket','expansiontank':'expansion_tank'}[r['definition']]
  dv=q-p;v=local(q,p)
  auxrows.append({'revision':rev,'component':name,**cols('start_CAD',p),**cols('end_CAD',q),'dx_mm':v[0],'dy_mm':v[1],'dz_normal_mm':v[2],'length_mm':float(norm(dv)),'OD_mm':2*c['radius_mm'],'cad_path':r['path'],'face':c['face'],'basis':'Outer cylinder axis; endpoints ordered lower to higher CAD Y','source_file':d['source_file']})
 for r in rr:
  componentrows.append({'revision':rev,'path':r['path'],'definition':r['definition'],'is_assembly':r['assembly'],'depth':r['depth'],**{k:r[k] for k in ['cx','cy','cz','xmin','xmax','ymin','ymax','zmin','zmax']},'center_basis':r['center_basis'],'source_file':d['source_file']})
 models[rev]={'source_file':d['source_file'],'sha256':d['sha256'],'origin_CAD_XYZ_mm':origin.tolist(),'corners':{k:v.tolist() for k,v in points.items()},'sensors':sensors,'segments':segs,'shafts':shafts}
 for label,val in [('upcomer_straight_mm',next(s['centerline_length_mm'] for s in segs if s['segment']=='upcomer')),('downcomer_straight_mm',next(s['centerline_length_mm'] for s in segs if s['segment']=='downcomer')),('heater_straight_mm',next(s['centerline_length_mm'] for s in segs if s['segment']=='heater')),('cooler_straight_mm',next(s['centerline_length_mm'] for s in segs if s['segment']=='cooler')),('vertical_leg_horizontal_spacing_mm',abs(points['B'][2]-points['G'][2])),('listed_tangent_height_range_mm',max(p[1] for p in points.values())-min(p[1] for p in points.values()))]:
  features.append({'revision':rev,'feature':label,'value_mm':float(val),'source_file':d['source_file']})
csvout('corners',cornerrows);csvout('segments',segmentrows);csvout('sensors',sensorrows);csvout('probe_shafts',shaftrows);csvout('components',componentrows);csvout('features',features);csvout('main_cylinder_axes',axisrows);csvout('auxiliary_axes',auxrows)

(O/'data/derived.json').write_text(json.dumps({'models':models,'corners':cornerrows,'segments':segmentrows,'sensors':sensorrows,'probe_shafts':shaftrows,'features':features,'auxiliary_axes':auxrows},indent=2))
