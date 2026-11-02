"""Export component axes and explicit Rev9 branch-interface measurements."""
from pathlib import Path
import json,csv,numpy as np
R=Path(__file__).resolve().parents[1];file=R/'data/VCU_Rev9_Engineering_Data.json';D=json.load(open(file));raw=json.load(open(R/'raw/rev9.json'));N=np.linalg.norm;A=np.array
S={s['segment']:s for s in D['segments']};aux={a['component']:a for a in D['auxiliary_axes']};O=A(D['origin_CAD_xyz_mm']);src=D['source_file'];root=raw['records'][0]['path']+'/'
def local(p):return ((A(p)-O)[[2,1,0]]*[-1,1,1]).tolist()
def export(name,rows):
 keys=list(dict.fromkeys(k for r in rows for k in r))
 with (R/'data'/name).open('w',newline='') as f:w=csv.DictWriter(f,keys);w.writeheader();w.writerows(rows)
connections=[]
for name,leg in [('TLEP','cooler'),('BREP','heater')]:
 r=aux[name];pa,pb=map(A,[r['start_xyz_mm'],r['end_xyz_mm']]);u=(pb-pa)/N(pb-pa);s=S[leg];candidates=[]
 for g in s['axis_pieces']:
  a,b=map(A,[g['start_xyz_mm'],g['end_xyz_mm']]);v=(b-a)/N(b-a);t=np.linalg.lstsq(np.column_stack((v,-u)),pa-a,rcond=None)[0];q=a+t[0]*v;qb=pa+t[1]*u
  # Select the unique pipe-axis piece nearest the connection, preserving offsets.
  score=N(q-qb)+max(0,-t[0],t[0]-N(b-a));candidates.append((score,q,qb,t[1],g))
 _,q,qb,t,g=min(candidates,key=lambda z:z[0]);connections.append({'id':name+'-AXIS-CROSS','component':name,'main_segment':leg,'main_axis_point_xyz_mm':q.tolist(),'branch_axis_point_xyz_mm':qb.tolist(),'main_station_from_start_mm':float(np.dot(q-A(s['start_xyz_mm']),A(s['reference_direction']))),'branch_station_from_IN_mm':float(t),'axis_skew_mm':float(N(q-qb)),'main_source_face':g['source_face'],'branch_source_path':r['source_path'],'basis':'Closest points of extended cylindrical axes; not an ideal hydraulic tee or physical weld plane'})
D['branch_connections']=connections
D['tank_interface']={'TLEP_OUT_to_tank_IN_mm':float(N(A(aux['TLEP']['end_xyz_mm'])-aux['expansion_tank']['start_xyz_mm'])),'basis':'Distance between tube outer-axis endpoint and tank outer-axis endpoint; no automatic bore connectivity assertion'}
D['verification']=json.load(open(R/'raw/rev9_verification.json'))
# The cooler jacket is coaxial within extraction tolerance.
p=A(D['jacket']['shell_start_xyz_mm']);a=A(S['cooler']['start_xyz_mm']);v=A(S['cooler']['reference_direction']);D['jacket']['axis_offset_from_pipe_mm']=float(N(p-(a+np.dot(p-a,v)*v)))
# A deliberately explicit component-axis export: bends get their own geometry type.
axes=[]
def axis(id,typ,a,b,L,ro,ri,path,basis):
 delta=A(local(b))-local(a)
 axes.append({'id':id,'geometry_type':typ,**{f'start_CAD_{k}_mm':x for k,x in zip('XYZ',a)},**{f'end_CAD_{k}_mm':x for k,x in zip('XYZ',b)},**{f'd{k}_mm':x for k,x in zip('xyn',delta)},'length_mm':L,'outer_radius_mm':ro,'inner_radius_mm':ri,'source_path':path,'basis':basis,'source_file':src})
for s in D['segments']:
 if 'axis_pieces' in s:
  for i,p in enumerate(s['axis_pieces'],1):axis(s['segment']+'-piece-'+str(i),'straight cylinder',p['start_xyz_mm'],p['end_xyz_mm'],p['length_mm'],16.7005,None,p['source_face'],'Unique cylindrical span; heater pieces overlap and are offset')
 else:axis(s['segment'],'torus arc' if 'torus' in s else 'qualified spline',s['start_xyz_mm'],s['end_xyz_mm'],s['centerline_length_mm'],16.7005,None,'; '.join(s['cad_faces']),s['length_basis'])
for r in D['auxiliary_axes']:axis(r['component'],'straight cylinder',r['start_xyz_mm'],r['end_xyz_mm'],r['length_mm'],r['outer_radius_mm'],r['inner_radius_mm'],r['source_path'], 'Outer cylindrical axis between end planes')
j=D['jacket'];axis('jacket-shell','straight cylinder',j['shell_start_xyz_mm'],j['shell_end_xyz_mm'],j['shell_mm'],j['shell_Ro_mm'],j['shell_Ri_mm'],j['source_path'],'Shell only, excludes end plates')
for p in D['ports']:axis(p['id'],'straight bore axis',p['axis_start_xyz_mm'],p['axis_end_xyz_mm'],p['bore_axis_length_mm'],p['outer_land_radius_mm'],p['inner_radius_mm'],p['path'],'Port axis ordered outward from jacket')
for h in D['hoses']:
 axis(h['id']+'-STRAIGHT','straight cylinder',h['connected_end_xyz_mm'],h['bend_join_xyz_mm'],h['straight_mm'],h['outer_radius_mm'],None,h['path'],'Modeled hose outer envelope; bore absent')
 axis(h['id']+'-BEND','torus arc',h['bend_join_xyz_mm'],h['free_end_xyz_mm'],h['arc_mm'],h['outer_radius_mm'],None,h['path'],'180-degree arc; centerline radius '+str(h['bend_radius_mm'])+' mm')
r=D['drain']
for nm,aa,bb,ll in [('INLET','inlet_axis_start_xyz_mm','inlet_axis_end_xyz_mm','inlet_outer_axis_length_mm'),('CROSS','cross_axis_start_xyz_mm','cross_axis_end_xyz_mm','cross_axis_length_mm')]:axis('DRAIN-'+nm,'straight cylinder',r[aa],r[bb],r[ll],r['outer_radius_mm'],r['inner_radius_mm'],r['path'],r['note'])
D['component_axes']=axes;export('VCU_Rev9_Pipe_Axes.csv',axes)
export('VCU_Rev9_Branch_Connections.csv',[{**{k:v for k,v in r.items() if not isinstance(v,list)},**{f'main_CAD_{k}_mm':x for k,x in zip('XYZ',r['main_axis_point_xyz_mm'])},**{f'branch_CAD_{k}_mm':x for k,x in zip('XYZ',r['branch_axis_point_xyz_mm'])},'source_file':src} for r in connections])
# Extend the numeric index with component lengths and branch positions.
metrics=list(csv.DictReader((R/'data/VCU_Rev9_Dimensions.csv').open()))
def metric(part,feature,val,basis,path='',unit='mm',status=None):metrics.append({'revision':'Rev9','component':part,'feature':feature,'value':val,'unit':unit,'status':status or ('not_encoded' if val is None else 'CAD_derived'),'basis':basis,'source_file':src,'source_path':path})
for r in D['auxiliary_axes']:
 for k in ['length_mm','dx_mm','dy_mm','dn_mm']:metric(r['component'],k.removesuffix('_mm'),r[k],'Outer-cylinder axis endpoints',r['source_path'])
for r in D['ports']:
 for k in ['bore_axis_length_mm','station_from_D_mm','station_from_jacket_in_mm','axis_skew_mm']:metric(r['id'],k.removesuffix('_mm'),r[k],'Port bore-axis extraction',r['path'])
for r in connections:
 for k in ['main_station_from_start_mm','branch_station_from_IN_mm','axis_skew_mm']:metric(r['component'],k.removesuffix('_mm'),r[k],r['basis'],r['main_source_face'])
for r in D['hoses']:
 for k in ['bend_radius_mm','bend_angle_deg']:metric(r['id'],k.rsplit('_',1)[0],r[k],'Analytical torus face',r['path'], 'deg' if k.endswith('_deg') else 'mm')
for k in ['inlet_outer_axis_length_mm','cross_axis_length_mm']:metric('drain_valve',k.removesuffix('_mm'),D['drain'][k],D['drain']['note'],D['drain']['path'])
metric('heater','outer_clamp_edge_span',D['heater']['outer_clamp_outer_edge_span_mm'],'Mechanical extent only; energized span unknown')
for i,v in enumerate(D['heater']['adjacent_center_spacings_mm'],1):metric('heater',f'HC{i}_to_HC{i+1}_centers',v,'Mechanical clamp center spacing')
for s in D['segments']:
 if 'inclination_from_horizontal_deg' in s:metric(s['segment'],'inclination_from_horizontal',s['inclination_from_horizontal_deg'],'CAD cylinder axis', '; '.join(s['cad_faces']),'deg')
for r in metrics:
 if r['feature'] in ['recovered_spine_length']:r['status']='qualified_reconstruction'
 if r['component']=='heater' and r['feature']=='reference_length':r['status']='projected_span_with_overlap'
 if r['feature']=='centerline_length' and r['component'] in ['heater','lower_right_bend']:r['status']='unresolved_geometry'
export('VCU_Rev9_Dimensions.csv',metrics)
D['numeric_dimension_count']=len(metrics);D['component_axis_count']=len(axes)
file.write_text(json.dumps(D,indent=2))
print('Axes',len(axes),'metrics',len(metrics),'branch stations',[(r['component'],r['main_station_from_start_mm'],r['branch_station_from_IN_mm'],r['axis_skew_mm']) for r in connections]);print('tank endpoint coincidence',D['tank_interface']);print('jacket offset',j['axis_offset_from_pipe_mm'])
