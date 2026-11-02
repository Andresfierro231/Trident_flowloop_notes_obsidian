"""Derive drawing and model-input tables from the current fresh Rev8 extraction."""
from pathlib import Path
import json,csv,math,hashlib
import numpy as np
R=Path(__file__).resolve().parents[1];raw=json.load(open(R/'raw/rev8.json'));old=json.load(open(R/'data/derived.json'));m=old['models']['rev8'];rr=raw['records'];by={r['path']:r for r in rr};O=np.array(m['origin_CAD_XYZ_mm']);P={k:np.array(v) for k,v in m['corners'].items()};root='UTDTloopWithOpticsAndHXRev8/'
a=np.array;norm=np.linalg.norm
def loc(p):return ((a(p)-O)[[2,1,0]]*[-1,1,1]).tolist()
def short(p):return p.removeprefix(root)
def cylinder(r,face):return next(c for c in r['cylinders'] if c['face']==face)
def axis(c):return a(c['start_xyz_mm']),a(c['end_xyz_mm'])
def ends(c):return sorted(axis(c),key=lambda p:-p[1])
def flatten(prefix,v):return {prefix+'_'+k+'_mm':float(x) for k,x in zip('XYZ',v)}
segments=m['segments'];segby={s['segment']:s for s in segments}
legs={}
for name in ['upcomer','cooler','downcomer','heater']:
 s=segby[name];pa,pb=P[s['from_tag']],P[s['to_tag']];v=(pb-pa)/norm(pb-pa);pieces=[]
 for path in s['cad_faces'].split('; '):
  pp,ff=path.rsplit('/Face',1);cc=cylinder(by[pp],int(ff));aa,bb=axis(cc)
  if np.dot(bb-aa,v)<0:aa,bb=bb,aa
  if any(norm(aa-g['a'])<1e-5 and norm(bb-g['b'])<1e-5 for g in pieces):continue
  pieces.append({'a':aa,'b':bb,'length':float(norm(bb-aa)),'path':path})
 pieces.sort(key=lambda g:np.dot(g['a']-pa,v));off=0
 for g in pieces:g['offset']=off;off+=g['length']
 legs[name]={'s':s,'pieces':pieces}
def project(p,name):
 choices=[]
 for g in legs[name]['pieces']:
  v=(g['b']-g['a'])/g['length'];st=float(np.dot(a(p)-g['a'],v));q=g['a']+st*v;clamped=g['a']+np.clip(st,0,g['length'])*v
  choices.append((norm(a(p)-clamped),st+g['offset'],q,float(norm(a(p)-q)),g['path']))
 _,st,q,rho,path=min(choices,key=lambda v:v[0]);return st,q,rho,path
bends=json.load(open(R/'data/reconstructed_bends.json'))
for b in bends:
 sg=next(s for s in segments if s['from_tag']==b['from_tag']);sg['recovered_spine_length_mm']=b['recovered_spine_length_mm'];sg['spine_endpoint_residuals_mm']=b['endpoint_residuals_mm'];sg['recovered_length_is_exact_hydraulic_length']=False
# Virtual sharp corners: intersections of projected straight axes, explicitly derived in 2D.
virtual={}
for tag,n1,n2 in [('VLL','heater','upcomer'),('VUL','upcomer','cooler'),('VUR','cooler','downcomer'),('VLR','downcomer','heater')]:
 s,t=segby[n1],segby[n2];p=np.array(loc(P[s['from_tag']])[:2]);q=np.array(loc(P[t['from_tag']])[:2]);v=np.array(loc(P[s['to_tag']])[:2])-p;w=np.array(loc(P[t['to_tag']])[:2])-q
 u=np.linalg.solve(np.column_stack((v,-w)),q-p);virtual[tag]=(p+u[0]*v).tolist()
virtuallegs=[]
for name,st,en in [('upcomer','VLL','VUL'),('cooler','VUL','VUR'),('downcomer','VUR','VLR'),('heater','VLR','VLL')]:
 dv=a(virtual[en])-a(virtual[st]);virtuallegs.append({'leg':name,'from':st,'to':en,'dx_mm':float(dv[0]),'dy_mm':float(dv[1]),'projected_axis_intersection_length_mm':float(norm(dv)),'basis':'Virtual sharp-corner intersections in drawing plane; not developed physical pipe length'})
# Jacket envelope, fresh analytical cylinder axes and projected CAD vertices.
shell=next(r for r in rr if r['definition']=='3in3ftCutSS_44635K443');outer=cylinder(shell,4);inner=cylinder(shell,3);ss,se=ends(outer);v=(se-ss)/norm(se-ss)
caps=[r for r in rr if '8983K211' in r['definition']];ext=[]
for r in caps:
 pr=(a(r['vertices_xyz_mm'])-ss)@v;ext.append({'path':r['path'],'min':float(min(pr)),'max':float(max(pr)),'thickness':float(max(pr)-min(pr))})
js=min(x['min'] for x in ext);je=max(x['max'] for x in ext);pipe_s=float(np.dot(P['D']-ss,v));pipe_e=float(np.dot(P['E']-ss,v))
jacket={'shell_start_xyz_mm':ss.tolist(),'shell_end_xyz_mm':se.tolist(),'outer_start_xyz_mm':(ss+js*v).tolist(),'outer_end_xyz_mm':(ss+je*v).tolist(),'flow_direction':v.tolist(),'pre_mm':js-pipe_s,'shell_mm':float(norm(se-ss)),'complete_mm':je-js,'post_mm':pipe_e-je,'shell_Ro_mm':outer['radius_mm'],'shell_Ri_mm':inner['radius_mm'],'end_plates':ext,'source_path':shell['path'],'endplate_hole_radius_mm':cylinder(caps[0],1)['radius_mm']}
assert abs(jacket['pre_mm']+jacket['complete_mm']+jacket['post_mm']-segby['cooler']['centerline_length_mm'])<1e-6
ports=[]
for r in rr:
 if not r['definition'].startswith('9157K35'):continue
 c=cylinder(r,27);pa,pb=axis(c);pv=(pb-pa)/norm(pb-pa)
 # Closest approach of infinite port-bore axis and cooler shell axis.
 ts=np.linalg.lstsq(np.column_stack((v,-pv)),pa-ss,rcond=None)[0];on_j=ss+ts[0]*v;on_p=pa+ts[1]*pv
 pe=sorted([pa,pb],key=lambda p:norm(p-on_j));ports.append({'id':'PORT-A' if r['path'].endswith('NAUO43') else 'PORT-B','path':r['path'],'inner_radius_mm':c['radius_mm'],'outer_land_radius_mm':cylinder(r,1)['radius_mm'],'axis_start_xyz_mm':pe[0].tolist(),'axis_end_xyz_mm':pe[1].tolist(),'bore_axis_length_mm':float(norm(pb-pa)),'axis_crossing_on_cooler_xyz_mm':on_j.tolist(),'axis_skew_mm':float(norm(on_j-on_p)),'station_from_D_mm':float(ts[0]-pipe_s),'station_from_complete_jacket_start_mm':float(ts[0]-js)})
# All minimum-distance solver solutions retained. First reference matches earlier CAD audit.
contacts={r['path']:r for r in json.load(open(R/'data/surface_contact_solutions.json'))};sensors=[]
for s in m['sensors']:
 s=dict(s);p=a([s[f'CAD_{k}_mm'] for k in 'XYZ']);sid=s['sensor_id'];s['actual_reference_xyz_mm']=p.tolist();s['local_reference_xyz_mm']=loc(p)
 if sid.startswith('JTC'):
  port=next(t for t in ports if t['id']=='PORT-'+sid[-1]);pa,pb=a(port['axis_start_xyz_mm']),a(port['axis_end_xyz_mm']);vv=(pb-pa)/norm(pb-pa);st=float(np.dot(p-pa,vv));q=pa+st*vv;L=port['bore_axis_length_mm'];name=port['id'];start=name+'-IN';end=name+'-OUT';rho=float(norm(p-q));s['domain']='jacket_port';s['port_path']=port['path'];s['main_leg_distance_is_applicable']=False
 elif sid=='STC-05':
  b=bends[0];st=b['STC05_distance_from_projected_C_mm'];q=a(b['STC05_recovered_spine_xyz_mm']);L=b['recovered_spine_length_mm'];name='upper_left_bend';start='C*';end='D*';rho=b['STC05_radial_distance_mm'];s['station_basis']='Recovered spline spine; C* and D* are projections of C and D, not exact joined tangent nodes';s['main_leg_distance_is_applicable']=True
 else:
  choices=[(norm(p-q),name,st,q,rho,ev) for name in legs for st,q,rho,ev in [project(p,name)]];_,name,st,q,rho,ev=min(choices,key=lambda q:q[0]);sg=segby[name];L=sg['centerline_length_mm'];start=sg['from_tag'];end=sg['to_tag'];s['station_source_faces']=ev;s['main_leg_distance_is_applicable']=True
 s.update(segment=name,segment_start=start,segment_end=end,station_from_start_mm=st,distance_to_end_mm=L-st,nearest_endpoint=start if abs(st)<=abs(L-st) else end,nearest_distance_mm=min(abs(st),abs(L-st)),projection_outside_segment=bool(st<0 or st>L),projected_axis_xyz_mm=q.tolist(),axis_radial_offset_mm=rho)
 s.setdefault('station_basis','Orthogonal projection of selected CAD reference onto the relevant cylindrical axis; sum unique axial spans if split')
 s['source_cad_path']=short(s['assembly_path']);s['source_reference_path']=short(s['reference_path'])
 if sid.startswith('STC'):
  sols=contacts[s['assembly_path']]['solutions'];values=[]
  for sol in sols:
   if name in legs:sol['station_from_segment_start_mm']=project(sol['pipe_xyz_mm'],name)[0];values.append(sol['station_from_segment_start_mm'])
  s['contact_solutions']=sols;s['number_contact_solutions']=len(sols);s['minimum_distance_solution_station_range_mm']=[min(values),max(values)] if values else [st,st]
  s['physical_junction_is_defined']=False
 else:s['physical_junction_is_defined']=False
 sensors.append(s)
order={'upcomer':0,'upper_left_bend':1,'cooler':2,'downcomer':3,'heater':4,'PORT-A':5,'PORT-B':6}
sensors.sort(key=lambda s:(order[s['segment']],s['station_from_start_mm'],s['sensor_id']))
# Exact auxiliary tube and tank cylinder endpoints, oriented flow/connection-first.
aux=[]
for r in old['auxiliary_axes']:
 if r['component']=='cooling_jacket':continue
 st=a([r[f'start_CAD_{k}_mm'] for k in 'XYZ']);en=a([r[f'end_CAD_{k}_mm'] for k in 'XYZ']);ref='D' if r['component']=='TLEP' else 'H' if r['component']=='BREP' else None
 if r['component']=='BREP':st,en=en,st
 rec={'component':r['component'],'start_xyz_mm':st.tolist(),'end_xyz_mm':en.tolist(),'length_mm':r['length_mm'],'source_path':r['cad_path'],'outer_radius_mm':r['OD_mm']/2,'inner_radius_mm':cylinder(by[r['cad_path']],1)['radius_mm'],'reference_corner':ref,'start_delta_from_corner_local_mm':(a(loc(st))-a(loc(P[ref]))).tolist() if ref else None};aux.append(rec)
# Diameter/radius schedule only asserts bores where a modeled cylinder exists.
diameters=[]
def dim(item,ro,ri,path,faces,note):diameters.append({'item':item,'outer_radius_mm':ro,'inner_radius_mm':ri,'outer_diameter_mm':None if ro is None else 2*ro,'inner_diameter_mm':None if ri is None else 2*ri,'wall_thickness_mm':None if ri is None or ro is None else ro-ri,'source_path':path,'faces':faces,'note':note,'source_file':raw['source_file']})
dim('Main swept loop',16.7005,None,'NAUO1/NAUO45; NAUO2/NAUO45','3,5,6,9,11,12','Export models solid pipe envelope. Main bore is not encoded; do not infer it from exit tubes or sensor spools.')
dim('TLEP / BREP',aux[0]['outer_radius_mm'],aux[0]['inner_radius_mm'],'NAUO3; NAUO5','2 outer; 1 inner','Annular exit tube cylinders')
dim('Cooling jacket shell',outer['radius_mm'],inner['radius_mm'],'NAUO6/NAUO40','4 outer; 3 inner','Full cylindrical shell span')
dim('Jacket end plates',44.45,jacket['endplate_hole_radius_mm'],'NAUO6/NAUO41; NAUO42','2 outer; 1 hole','Each plate 6.350 mm axial thickness; Ri is through-hole radius')
dim('Jacket port nipples',ports[0]['outer_land_radius_mm'],ports[0]['inner_radius_mm'],'NAUO6/NAUO43; NAUO44','1 outer land; 27 bore','Outer value is cylindrical land; thread geometry is not summarized by this diameter')
dim('LF / combined LF-PTC spools',16.7005,13.3223,'NAUO1/NAUO46/NAUO47; NAUO7/NAUO31','2/1; 5/4','Local instrument spools only; 101.600 mm length')
dim('PTC / JTC mounting spools',16.764,12.7,'NAUO9,22,23,24/NAUO28','3 outer; 2 bore','Part3 mount; 76.200 mm length')
dim('TC sheath',1.5875,None,'NAUO7,8,9,22,23,24','See shaft table / JSON','External modeled shaft only; sensing junction is not identified')
tank=next(t for t in aux if t['component']=='expansion_tank');dim('Expansion tank shell',tank['outer_radius_mm'],tank['inner_radius_mm'],'NAUO4','2 outer; 1 inner','Outer axial span 311.150 mm; inner cylinder 310.896 mm')
# Corner-coordinate source table.
corners=[]
for tag in 'BCDEFGHA':
 p=P[tag];row={'tag':tag,'CAD_xyz_mm':p.tolist(),'local_xyz_mm':loc(p),'definition':'Straight-cylinder axial limit at spline transition' if tag in 'CDGH' else 'Straight-cylinder endpoint coincident with exact torus centerline tangent'};corners.append(row)
# Sequential reference coordinate schedule, starting at B and returning to B.
coords=[]
def coord(tag,kind,p,reference):coords.append({'tag':tag,'kind':kind,'CAD_xyz_mm':list(map(float,p)),'local_xyz_mm':loc(p),'reference':reference})
for seg,start,end in [('upcomer','B','C'),('upper_left_bend','C','D'),('cooler','D','E'),('upper_right_bend','E','F'),('downcomer','F','G'),('lower_right_bend','G','H'),('heater','H','A'),('lower_left_bend','A','B')]:
 coord(start,'Axis endpoint',P[start],seg)
 for s in sensors:
  if s['segment']==seg:coord(s['sensor_id'],'Contact' if s['sensor_id'].startswith('STC') else 'Mount',s['actual_reference_xyz_mm'],seg)
for s in sensors:
 if s['sensor_id'].startswith('JTC'):coord(s['sensor_id'],'Mount',s['actual_reference_xyz_mm'],s['segment'])
for tag,key in [('J-IN','outer_start_xyz_mm'),('J-OUT','outer_end_xyz_mm')]:coord(tag,'Jacket axis',jacket[key],'Complete jacket outer end plane')
for ex in aux:
 if ex['component']=='expansion_tank':continue
 for end in ['start','end']:coord(ex['component']+('-IN' if end=='start' else '-OUT'),'Tube axis',ex[end+'_xyz_mm'],ex['component'])
summary={'source_file':raw['source_file'],'source_sha256':raw['sha256'],'extraction_date':'2026-09-26','units':'mm','CAD_unit_conversion':'STEP declares INCH; OCCT system length unit is millimetres','coordinate_frame':{'origin_CAD_xyz_mm':O.tolist(),'origin_tag':'B','x':'origin_CAD_Z - CAD_Z','y':'CAD_Y - origin_CAD_Y','n':'CAD_X - origin_CAD_X','n_note':'n is out of plane and must be retained for 3D models'},'corner_definition':'Two straight-axis endpoints per rounded corner, not a single sharp vertex. C,D,G,H are axial limits of trimmed cylinder faces.','corner_points':corners,'segments':segments,'virtual_corners_local_xy_mm':virtual,'virtual_corner_spans':virtuallegs,'jacket':jacket,'ports':ports,'auxiliary_axes':aux,'diameters':diameters,'exact_torus_bend_radii_mm':{'centerline':76.2,'outer_tube_intrados':76.2-16.7005,'outer_tube_extrados':76.2+16.7005,'note':'Envelope radii, not pipe bore radii; applies to A-B and E-F'},'sensors':sensors,'sequential_coordinates':coords,'probe_shafts':old['probe_shafts'],'reconstructed_bends':bends,'validation':json.load(open(R/'raw/rev8_verification.json')),'sensor_label_basis':'Region/order aligned with the collaborator schema; STEP itself has no channel IDs. LF/PTC-02 and LF/PTC-03 share mounting bodies. JTC-A/B label two additional jacket-port assemblies.','limitations':['Active heater length and boundaries are not separately modeled. Heating-leg length is not an active heater length.','Main swept loop fluid bore is not encoded. Local instrument spool bores differ from exit tube bores.','Surface contact references can be non-unique. All minimum-distance solver solutions are retained; a physical sensing junction is not identified.','LF coordinates locate modeled mounts, not distributed optical sensing extents.','Spline bend reconstructions have endpoint residuals; exact joined hydraulic centerline lengths are not established.','Cooler straight axes have a 0.271771 mm assembly offset. No source geometry has been healed.']}
(R/'data/VCU_Rev8_Engineering_Data.json').write_text(json.dumps(summary,indent=2))
# Flat CSVs are data exports, all values numeric where known; empty cells mean unavailable.
def csvwrite(name,rows):
 keys=list(dict.fromkeys(k for r in rows for k in r))
 with (R/'data'/name).open('w',newline='') as f:
  w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
csvwrite('VCU_Rev8_Coordinates.csv',[{'id':r['tag'],'kind':r['kind'],'reference':r['reference'],**flatten('CAD',r['CAD_xyz_mm']),'x_mm':r['local_xyz_mm'][0],'y_mm':r['local_xyz_mm'][1],'n_mm':r['local_xyz_mm'][2],'source_file':raw['source_file']} for r in coords])
csvwrite('VCU_Rev8_Sensor_Stations.csv',[{**{k:v for k,v in s.items() if isinstance(v,(str,float,int,bool)) or v is None},**flatten('projected_CAD',s['projected_axis_xyz_mm']),'contact_solution_s_min_mm':s.get('minimum_distance_solution_station_range_mm',[None,None])[0],'contact_solution_s_max_mm':s.get('minimum_distance_solution_station_range_mm',[None,None])[1]} for s in sensors])
csvwrite('VCU_Rev8_Contact_Solutions.csv',[{'sensor_id':s['sensor_id'],'solution_index':i,'segment':s['segment'],'station_from_start_mm':q.get('station_from_segment_start_mm'),'minimum_gap_mm':s['surface_gap_mm'],**flatten('pipe_CAD',q['pipe_xyz_mm']),**flatten('sensor_CAD',q['sensor_xyz_mm']),'source_file':raw['source_file'],'source_path':s['assembly_path']} for s in sensors for i,q in enumerate(s.get('contact_solutions',[]),1)])
csvwrite('VCU_Rev8_Probe_Shafts.csv',old['probe_shafts'])
csvwrite('VCU_Rev8_Diameters.csv',diameters)
csvwrite('VCU_Rev8_Segments.csv',[{k:v for k,v in s.items() if not isinstance(v,list)} for s in segments])
print('DATA',len(corners),'corners;',len(sensors),'sensors;',len(coords),'coordinate rows')
print('JACKET', {k:v for k,v in jacket.items() if isinstance(v,float)})
for s in sensors:print(s['sensor_id'],s['segment'],round(s['station_from_start_mm'],3),s['nearest_endpoint'],round(s['nearest_distance_mm'],3),s.get('minimum_distance_solution_station_range_mm'))
print('VIRTUAL',virtuallegs)
