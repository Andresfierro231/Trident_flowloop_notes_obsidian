# VCU Rev8 engineering drawing and model-input package

Authoritative source: **UTDTloopWithOpticsAndHXRev8(1).STEP**. Its internal STEP header names UTDTloopWithOpticsAndHXRev8.STEP.
SHA-256: `c40a7e6ce597a35cdaa9d7358835b242df408750b021385c1653d02a0871bf1e`.
Extraction/drawing issue: 2026-09-26. No PDF or Rev7 dimensional inputs were used.

## Contents

- `drawings/VCU_Rev8_CAD_Engineering_Drawings.pdf`: eight A3 landscape sheets with vector CAD outlines, dimensions, sensor stations, sequential coordinates and qualifications.
- `data/VCU_Rev8_Engineering_Data.json`: comprehensive full-precision structured output and evidence references.
- `data/VCU_Rev8_Coordinates.csv`: ordered actual reference points, with world XYZ and local x/y/n.
- `data/VCU_Rev8_Sensor_Stations.csv`: all 22 sensor references and axial stations. Includes projected world coordinates and alternative contact station ranges.
- `data/VCU_Rev8_Contact_Solutions.csv`: every minimum-distance solution returned for the surface sensors.
- `data/VCU_Rev8_Segments.csv`: straight and curved segments, endpoint coordinates and signed changes.
- `data/VCU_Rev8_Diameters.csv`: radii, diameters, wall thickness where defined, and CAD source paths.
- `data/VCU_Rev8_Probe_Shafts.csv`: six external geometric probe-shaft endpoint pairs; these are not claimed sensing junctions.
- `raw/`: fresh STEP extraction, CAD projection, independent face-bound verification and logs.
- `scripts/`: extraction, derivation, independent checks and drawing generation.
- `source/`: the exact source STEP file, unchanged.

## Coordinate and length conventions

All numbers are in **millimetres**. OCCT converts the STEP's INCH length unit to mm.
The local right-handed frame is:

```
B_world = [629.8066323905703, 852.1241951408306, 3306.139984197984]
x = B_world[2] - CAD_Z
y = CAD_Y - B_world[1]
n = CAD_X - B_world[0]
```

`n` is normal to the drawing plane. Retain it for 3D work.
Loop traversal: B-C-D-E-F-G-H-A-B. B-C is the upcomer, D-E cooling leg, F-G downcomer, H-A heating leg.
A rounded corner has two axis endpoints, not one vertex. A/B/E/F coincide with exact torus tangents. C/D/G/H are straight-cylinder axial limits at trimmed spline transitions.
Virtual sharp intersections are separately identified and are not physical developed pipe lengths.
The cooling-leg straight span sums unique collinear/near-collinear cylindrical spans; it does not insert extra length for the modeled 0.271771 mm joint offset.

## Measurements and unresolved inputs

Complete cooling-jacket axial envelope: 1030.2875 mm, including two 6.35 mm end plates.
Shell alone: 1017.5875 mm. Pre-jacket: 271.5758378224 mm. Post-jacket: 230.8364212312 mm.
Shell Ro/Ri: 44.45/38.9636 mm.

The main swept loop has OD 33.401 mm but **no modeled bore**. Local instrument spool bores and exit bores differ and do not establish the entire main-loop ID.
The active heater boundaries are not separately modeled.
Two corners have exact R76.2 mm, 80-degree torus centerlines. For the two spline corners the package gives chords and a qualified recovered support-spine construction with endpoint residuals. No healed hydraulic centerline is asserted.

Surface sensor coordinates use the **first minimum-distance pipe point** reported in the extraction, preserving the selected reference used in the comparison work. Some sensor bodies have multiple equally close points (up to about 25.4 mm axial separation). All returned solutions are provided. Their range is not a certified full contact footprint, and no point is claimed to be the physical sensing junction.
STC-05 is on the spline corner and uses a recovered-spine station with explicit qualification.
LF/PTC coordinates are mounting-body centroids. LF-02/PTC-02 and LF-03/PTC-03 share mounting bodies. LF sensing extents and TC junctions are not identified in the model.
JTC-A/B are on coolant-port hardware. Their projections lie 0.040 and 10.942 mm beyond the respective outer bore-axis endpoints. Negative `distance_to_end_mm` records that signed extension; `nearest_distance_mm` is its nonnegative magnitude. They are not main-loop PTCs.
Drawing IDs are aligned to the collaborator schema by type and region/order. The STEP has no verified acquisition channel labels.

JSON null / empty CSV cells mean unknown or inapplicable, never zero. Display rounding in the PDF is not a tolerance.

## Read with Python

```python
import json
from pathlib import Path
import pandas as pd

root = Path('VCU_Rev8_CAD_Model_Package')
model = json.loads((root/'data/VCU_Rev8_Engineering_Data.json').read_text())
points = pd.read_csv(root/'data/VCU_Rev8_Coordinates.csv')
sensors = pd.read_csv(root/'data/VCU_Rev8_Sensor_Stations.csv')
segments = pd.read_csv(root/'data/VCU_Rev8_Segments.csv')
```

## Reproduce

Tested with Python 3.12, CadQuery 2.7.0 / OCP, NumPy, SciPy and ReportLab. Drawing fonts: DejaVu Sans. Poppler renders the finished PDF for visual review.
Run from the extracted package root. `VCU_REV8_STEP` can override the default `source/` path.

```sh
python3 scripts/extract_rev8.py 'source/UTDTloopWithOpticsAndHXRev8(1).STEP' raw/rev8.json
python3 scripts/derive_rev8.py
python3 scripts/verify_rev8.py rev8
python3 scripts/reconstruct_bends.py
python3 scripts/audit_surface_contacts.py
python3 scripts/project_cad.py
python3 scripts/build_model_data.py
python3 scripts/draw_engineering.py
```

The drawing script writes `../output/pdf/VCU_Rev8_CAD_Engineering_Drawings.pdf` relative to the package root. The included PDF is in `drawings/`.
Face numbers refer to OCCT/CadQuery traversal of this import; use the unchanged source, hash and full instance paths. They are not permanent native SolidWorks feature IDs.
