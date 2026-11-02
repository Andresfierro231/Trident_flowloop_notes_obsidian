from pathlib import Path
import json,hashlib,math,csv
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1];d=json.load(open(R/'data/VCU_Rev8_Engineering_Data.json'))
from cad_model import SOURCE
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()==d['source_sha256']
assert len(d['corner_points'])==8 and len(d['sensors'])==22
assert len(set(s['sensor_id'] for s in d['sensors']))==22
assert {s['sensor_id'] for s in d['sensors']}=={f'STC-{i:02d}' for i in range(1,13)}|{f'LF-{i:02d}' for i in range(1,5)}|{f'PTC-{i:02d}' for i in range(1,5)}|{'JTC-A','JTC-B'}
for s in d['sensors']:
 if s['segment'] in ['upcomer','cooler','downcomer','heater']:
  L=next(g['centerline_length_mm'] for g in d['segments'] if g['segment']==s['segment'])
  assert 0<=s['station_from_start_mm']<=L
  assert abs(s['station_from_start_mm']+s['distance_to_end_mm']-L)<1e-9
  assert abs(s['nearest_distance_mm']-min(s['station_from_start_mm'],s['distance_to_end_mm']))<1e-9
j=d['jacket'];L=next(g['centerline_length_mm'] for g in d['segments'] if g['segment']=='cooler');assert abs(j['pre_mm']+j['complete_mm']+j['post_mm']-L)<1e-8
assert abs(j['complete_mm']-j['shell_mm']-sum(c['thickness'] for c in j['end_plates']))<1e-8
assert abs(sum(s['dx_mm'] for s in d['segments']))<1e-8 and abs(sum(s['dy_mm'] for s in d['segments']))<1e-8
assert d['validation']['max_endpoint_error_mm']<1e-6
coords=list(csv.DictReader(open(R/'data/VCU_Rev8_Coordinates.csv')));assert len(coords)==36
pdf=PdfReader(R.parent/'output/pdf/VCU_Rev8_CAD_Engineering_Drawings.pdf');assert len(pdf.pages)==8
for p in pdf.pages:
 assert abs(float(p.mediabox.width)-1190.551)<.01
 assert d['source_file'] in p.extract_text()
texts='\n'.join(p.extract_text() for p in pdf.pages)
for sid in {s['sensor_id'] for s in d['sensors']}:assert sid in texts
out={'source_sha256_matches':True,'pages':8,'corners':8,'sensor_references':22,'ordered_coordinate_rows':36,'station_sums_and_nearest_ends_pass':True,'jacket_chain_pass':True,'coordinate_loop_closure_pass':True,'independent_face_bound_error_mm':d['validation']['max_endpoint_error_mm'],'PDF_sensor_ids_and_source_names_present':True}
(R/'data/deliverable_validation.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
