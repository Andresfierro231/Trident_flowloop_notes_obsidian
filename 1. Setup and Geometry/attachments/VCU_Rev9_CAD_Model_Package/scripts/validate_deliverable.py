"""Numerical integrity and source-evidence checks; no geometry is healed."""
from pathlib import Path
import json,hashlib,csv,collections
import numpy as np
from pypdf import PdfReader
from cad_model import SOURCE
R=Path(__file__).resolve().parents[1];D=json.load(open(R/'data/VCU_Rev9_Engineering_Data.json'));raw=json.load(open(R/'raw/rev9.json'));by={r['path']:r for r in raw['records']};A=np.array;N=np.linalg.norm;O=A(D['origin_CAD_xyz_mm']);S={s['segment']:s for s in D['segments']}
def close(a,b,tol=1e-8):assert N(A(a)-A(b))<tol,(a,b)
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==D['source_sha256']==raw['sha256']
assert len(raw['records'])==99
assert len(D['sensors'])==23 and len({s['sensor_id'] for s in D['sensors']})==23
assert {s['sensor_id'] for s in D['sensors']}=={f'STC-{i:02d}' for i in range(1,13)}|{f'LF-{i:02d}' for i in range(1,5)}|{f'PTC-{i:02d}' for i in range(1,5)}|{'PTC-X','JTC-A','JTC-B'}
assert len(D['probe_shafts'])==7 and len(D['heater']['clamps'])==4
for s in D['sensors']:
 L=S[s['segment']]['reference_length_mm'] if s['domain']=='main_loop' else next(p['bore_axis_length_mm'] for p in D['ports'] if p['id']==s['segment'])
 if s['domain']=='main_loop':assert 0<=s['station_from_start_mm']<=L and not s['projection_outside_segment']
 close(s['station_from_start_mm']+s['distance_to_end_mm'],L)
 close(s['nearest_distance_mm'],min(abs(s['station_from_start_mm']),abs(s['distance_to_end_mm'])))
 close(s['axis_radial_offset_mm'],N(A(s['actual_reference_xyz_mm'])-s['projected_axis_xyz_mm']))
 close(s['local_reference_xyz_mm'],(A(s['actual_reference_xyz_mm'])-O)[[2,1,0]]*[-1,1,1])
 assert s['reference_path'] in by and s['assembly_path'] in by
 if s['sensor_type']=='STC':
  vals=[p['station_from_segment_start_mm'] for p in s['contact_solutions']];close(s['minimum_distance_solution_station_range_mm'],[min(vals),max(vals)])
  for p in s['contact_solutions']:close(N(A(p['pipe_xyz_mm'])-p['sensor_xyz_mm']),s['surface_gap_mm'],1e-6)
 assert s['physical_junction_is_defined'] is False and s['channel_label_in_CAD'] is None
j=D['jacket'];close(j['pre_mm']+j['complete_mm']+j['post_mm'],S['cooler']['reference_length_mm']);close(j['complete_mm'],j['shell_mm']+sum(p['thickness_mm'] for p in j['end_plates']));assert j['axis_offset_from_pipe_mm']<1e-6
close([sum(s[k] for s in D['segments']) for k in ['dx_mm','dy_mm','dn_mm']],[0,0,0])
for i,s in enumerate(D['segments']):
 close(s['end_xyz_mm'],D['segments'][(i+1)%8]['start_xyz_mm']);close(s['chord_mm'],N(A(s['start_xyz_mm'])-s['end_xyz_mm']))
 if 'torus' in s:
  close(s['centerline_length_mm'],np.radians(s['bend_angle_deg'])*s['bend_radius_mm']);assert s['torus_endpoint_residual_mm']<1e-6
  close(s['polyline_xyz_mm'][0],s['start_xyz_mm'],1e-6);close(s['polyline_xyz_mm'][-1],s['end_xyz_mm'],1e-6)
 if 'axis_pieces' in s:
  close(s['unique_face_axis_length_sum_mm']-s['projected_overlap_mm'],s['projected_union_length_mm']);close(s['projected_union_length_mm'],s['reference_length_mm'])
assert S['heater']['centerline_length_mm'] is None and S['lower_right_bend']['centerline_length_mm'] is None
assert S['heater']['projected_overlap_mm']>7 and S['heater']['axis_offset_mm']>.15
assert D['heater']['active_length_mm'] is None
for s in D['probe_shafts']:close(N(A(s['start_xyz_mm'])-s['end_xyz_mm']),s['length_mm'])
for c in D['heater']['clamps']:
 close(c['station_end_from_H_mm']-c['station_start_from_H_mm'],c['axial_width_mm']);close(c['axis_center_xyz_mm'],(A(c['axis_start_xyz_mm'])+c['axis_end_xyz_mm'])/2);assert c['axis_offset_from_pipe_mm']<1e-6
for row in D['diameters']:
 r=by[raw['records'][0]['path']+'/'+row['source_path']]
 for role in ['inner','outer']:
  v=row[role+'_radius_mm'];dia=row[role+'_diameter_mm']
  if v is None:assert dia is None
  else:
   close(dia,2*v);assert any(abs(c['radius_mm']-v)<1e-6 for c in r['cylinders'])
assert next(x for x in D['diameters'] if x['item']=='Main swept loop')['inner_diameter_mm'] is None
for s in D['hoses']:
 close(s['arc_mm'],s['bend_radius_mm']*np.radians(s['bend_angle_deg']));close(s['modeled_centerline_length_mm'],s['straight_mm']+s['arc_mm']);assert s['join_residual_mm']<1e-6
for c in D['sequential_coordinates']:close(c['local_xyz_mm'],(A(c['CAD_xyz_mm'])-O)[[2,1,0]]*[-1,1,1])
counts={}
for f in (R/'data').glob('*.csv'):
 rows=list(csv.DictReader(f.open()));counts[f.name]=len(rows)
 for row in rows:
  for v in row.values():assert v not in ['nan','NaN','inf','-inf','None']
coords=list(csv.DictReader((R/'data/VCU_Rev9_Coordinates.csv').open()));assert len(coords)==57
for c,r in zip(coords,D['sequential_coordinates']):
 close([float(c['CAD_'+k+'_mm']) for k in 'XYZ'],r['CAD_xyz_mm']);assert c['id']==r['tag']
assert counts['VCU_Rev9_Sensor_Stations.csv']==23 and counts['VCU_Rev9_Pipe_Axes.csv']==22
metrics=list(csv.DictReader((R/'data/VCU_Rev9_Dimensions.csv').open()));assert len(metrics)==D['numeric_dimension_count']==199
assert len({(r['component'],r['feature']) for r in metrics})==len(metrics)
assert all(r['value']=='' for r in metrics if r['status'] in ['not_encoded','unresolved_geometry'])
pdf=PdfReader(R.parent/'output/pdf/VCU_Rev9_CAD_Engineering_Drawings.pdf');assert len(pdf.pages)==8
texts='\n'.join(p.extract_text() for p in pdf.pages)
for p in pdf.pages:assert abs(float(p.mediabox.width)-1190.551)<.01 and D['source_file'] in p.extract_text()
for sid in {s['sensor_id'] for s in D['sensors']}:assert sid in texts
out={'source_sha256_matches':True,'pages':8,'CAD_assembly_records':99,'corners':8,'sensor_references':23,'coordinate_rows':57,'pipe_axis_records':22,'numeric_dimension_rows':199,'CSV_row_counts':counts,'station_sums_and_nearest_ends_pass':True,'jacket_chain_pass':True,'coordinate_loop_closure_pass':True,'diameter_source_evidence_pass':True,'null_unknowns_preserved':True,'independent_face_bound_error_mm':D['verification']['max_endpoint_error_mm'],'qualifications_not_healed':['heater overlap/offset','lower-right spline residuals','STC-01 gap','unknown bores and energized length','unassigned PTC-X channel'],'PDF_sensor_ids_and_source_names_present':True}
(R/'data/deliverable_validation.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
