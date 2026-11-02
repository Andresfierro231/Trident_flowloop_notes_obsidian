"""Rev9 geometry from the fresh world-coordinate CAD inventory; no Rev8 dimensions."""
from pathlib import Path
import json,math,numpy as np
R=Path(__file__).resolve().parents[1];d=json.load(open(R/'raw/rev9_inventory.json'));rr=d['records'];main=[r for r in rr if r['definition'].startswith('MSRloop')];N=np.linalg.norm;A=np.array
G=[]
for r in main:
 for c in r['cylinders']:
  if abs(c['radius_mm']-16.7005)>1e-4 or c['vmax']-c['vmin']<20:continue
  a,b=map(A,[c['start_xyz_mm'],c['end_xyz_mm']]);v=(b-a)/N(b-a);found=None
  for g in G:
   if N(np.cross(v,g['v']))<1e-7 and N(np.cross(a-g['a'],g['v']))<.5:found=g;break
  if found is None:found={'a':a,'v':v,'pieces':[],'faces':[]};G.append(found)
  found['faces'].append(r['path']+f"/Face{c['face']}")
  if not any(min(N(a-p['a'])+N(b-p['b']),N(a-p['b'])+N(b-p['a']))<1e-5 for p in found['pieces']):found['pieces'].append({'a':a,'b':b,'length':float(N(b-a)),'evidence':r['path']+f"/Face{c['face']}"})
assert len(G)==4
for g in G:
 pts=[p[k] for p in g['pieces'] for k in ['a','b']];pts.sort(key=lambda p:float(p@g['v']));g['ends']=[pts[0],pts[-1]]
vertical=sorted([g for g in G if abs(g['v'][1])>.99],key=lambda g:-np.mean(g['ends'],axis=0)[2]);inclined=sorted([g for g in G if abs(g['v'][2])>.9],key=lambda g:np.mean(g['ends'],axis=0)[1]);up,down=vertical;heater,cooler=inclined
byY=lambda g:sorted(g['ends'],key=lambda p:p[1])
P={'A':byY(heater)[1],'B':byY(up)[0],'C':byY(up)[1],'D':byY(cooler)[1],'E':byY(cooler)[0],'F':byY(down)[1],'G':byY(down)[0],'H':byY(heater)[0]};O=P['B']
def loc(p):return ((A(p)-O)[[2,1,0]]*[-1,1,1]).tolist()
def delta(p,q):return ((A(q)-p)[[2,1,0]]*[-1,1,1]).tolist()
segments=[]
for name,st,en,g in [('upcomer','B','C',up),('upper_left_bend','C','D',None),('cooler','D','E',cooler),('upper_right_bend','E','F',None),('downcomer','F','G',down),('lower_right_bend','G','H',None),('heater','H','A',heater),('lower_left_bend','A','B',None)]:
 pa,pb=P[st],P[en];dv=delta(pa,pb);row={'segment':name,'from_tag':st,'to_tag':en,'start_xyz_mm':pa.tolist(),'end_xyz_mm':pb.tolist(),'dx_mm':dv[0],'dy_mm':dv[1],'dn_mm':dv[2],'chord_mm':float(N(pb-pa)),'centerline_length_mm':None,'reference_length_mm':None,'source_file':d['source_file']}
 if g:
  dominant=max(g['pieces'],key=lambda p:p['length']);v=(dominant['b']-dominant['a'])/dominant['length'];v*=1 if np.dot(v,pb-pa)>0 else -1
  L=float(np.dot(pb-pa,v));intervals=[];pieces=[]
  for p in g['pieces']:
   a,b=p['a'],p['b']
   if np.dot(b-a,v)<0:a,b=b,a
   ss,ee=float(np.dot(a-pa,v)),float(np.dot(b-pa,v));intervals.append([ss,ee]);pieces.append({'start_xyz_mm':a.tolist(),'end_xyz_mm':b.tolist(),'start_station_mm':ss,'end_station_mm':ee,'length_mm':p['length'],'source_face':p['evidence'],'perpendicular_offset_from_reference_mm':float(N(np.cross(a-pa,v)))})
  intervals.sort();union=0;start,end=intervals[0]
  for aa,bb in intervals[1:]:
   if aa>end:union+=end-start;start,end=aa,bb
   else:end=max(end,bb)
  union+=end-start;sm=sum(p['length'] for p in g['pieces']);overlap=sm-union;offset=max(p['perpendicular_offset_from_reference_mm'] for p in pieces)
  row.update(reference_direction=v.tolist(),reference_length_mm=L,centerline_length_mm=L if overlap<1e-6 and offset<1e-6 else None,unique_face_axis_length_sum_mm=sm,projected_union_length_mm=union,projected_overlap_mm=overlap,axis_offset_mm=offset,axis_pieces=pieces,cad_faces=g['faces'],length_basis='Continuous straight axis' if overlap<1e-6 and offset<1e-6 else 'Projected endpoint-to-endpoint axial span; overlapping offset pieces retained, no healed centerline',inclination_from_horizontal_deg=float(np.degrees(np.arctan2(abs(v[1]),abs(v[2])))))
 else:
  matches=[]
  for r in main:
   for t in r['tori']:
    center=A(t['center_xyz_mm']);xd=A(t['x_direction']);yd=A(t['y_direction']);rad=t['major_radius_mm'];ends=[center+rad*(math.cos(u)*xd+math.sin(u)*yd) for u in [t['umin'],t['umax']]]
    err=min(N(ends[0]-pa)+N(ends[1]-pb),N(ends[0]-pb)+N(ends[1]-pa))
    if err<1e-5:matches.append((r,t,err,ends))
  if matches:
   r,t,err,te=matches[0];rad=t['major_radius_mm'];angle=t['umax']-t['umin'];start_u=t['umin'] if N(te[0]-pa)<N(te[1]-pa) else t['umax'];end_u=t['umax'] if start_u==t['umin'] else t['umin'];poly=[(A(t['center_xyz_mm'])+rad*(math.cos(u)*A(t['x_direction'])+math.sin(u)*A(t['y_direction']))).tolist() for u in np.linspace(start_u,end_u,151)]
   row.update(centerline_length_mm=rad*abs(angle),reference_length_mm=rad*abs(angle),bend_radius_mm=rad,bend_angle_deg=math.degrees(abs(angle)),length_basis='Exact analytical torus centerline arc',cad_faces=[r['path']+f"/Face{t['face']}"],polyline_xyz_mm=poly,torus=t,torus_endpoint_residual_mm=float(err))
  else:row.update(length_basis='Endpoint chord; exact joined centerline not established',cad_faces=[])
 segments.append(row)
virtual={};sb={s['segment']:s for s in segments}
for tag,n1,n2 in [('VLL','heater','upcomer'),('VUL','upcomer','cooler'),('VUR','cooler','downcomer'),('VLR','downcomer','heater')]:
 s,t=sb[n1],sb[n2];p=A(loc(P[s['from_tag']])[:2]);q=A(loc(P[t['from_tag']])[:2]);v=A(s['reference_direction'])[[2,1]]*[-1,1];w=A(t['reference_direction'])[[2,1]]*[-1,1];u=np.linalg.solve(np.column_stack((v,-w)),q-p);virtual[tag]=(p+u[0]*v).tolist()
vl=[]
for n,st,en in [('upcomer','VLL','VUL'),('cooler','VUL','VUR'),('downcomer','VUR','VLR'),('heater','VLR','VLL')]:
 dv=A(virtual[en])-virtual[st];vl.append({'leg':n,'from':st,'to':en,'dx_mm':float(dv[0]),'dy_mm':float(dv[1]),'projected_axis_intersection_length_mm':float(N(dv))})
out={'source_file':d['source_file'],'source_sha256':d['sha256'],'units':'mm','origin_CAD_xyz_mm':O.tolist(),'corners':{k:v.tolist() for k,v in P.items()},'segments':segments,'virtual_corners_local_xy_mm':virtual,'virtual_corner_spans':vl}
(R/'data/geometry.json').write_text(json.dumps(out,indent=2))
for s in segments:print(s['segment'],'ref',s['reference_length_mm'],'exact CL',s['centerline_length_mm'],'dxdy',s['dx_mm'],s['dy_mm'],'overlap',s.get('projected_overlap_mm'),'offset',s.get('axis_offset_mm'))
print('ORIGIN',O)
