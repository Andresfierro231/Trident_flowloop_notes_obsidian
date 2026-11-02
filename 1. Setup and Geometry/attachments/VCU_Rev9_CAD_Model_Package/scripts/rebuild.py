"""Rebuild this Rev9 CAD extraction package from its preserved source.
Dependencies are listed in environment_versions.json. Output PDF is written to
../output/pdf relative to the package root, as printed by draw_engineering.py.
"""
from pathlib import Path
import subprocess,sys,os
R=Path(__file__).resolve().parents[1];PY=sys.executable
for d in ['raw','data','render']:(R/d).mkdir(exist_ok=True)
src=Path(os.environ.get('VCU_REV9_STEP',R/'source/_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step'))
commands=[['extract_inventory.py',str(src),str(R/'raw/rev9_inventory.json')],['extract_contacts.py'],['derive_geometry.py'],['reconstruct_bends.py'],['project_cad.py'],['verify_rev9.py','rev9'],['build_model_data.py'],['enrich_data.py'],['draw_engineering.py'],['validate_deliverable.py']]
for script,*args in commands:
 print('Running',script,flush=True)
 subprocess.run([PY,str(R/'scripts'/script),*args],check=True)
