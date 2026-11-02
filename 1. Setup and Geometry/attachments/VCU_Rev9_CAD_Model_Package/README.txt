VCU REV9 — CAD ENGINEERING DRAWINGS AND COMPUTATIONAL-GEOMETRY DATA
Issue 2026-10-08 | Eight A3 vector PDF sheets | Length units: mm

PRIMARY SOURCE
_STEPFILE_UTDTloopWithOpticsAndHXRev9_9_18_26.step
SHA-256: 78c6ae52bf39084fbd9b1306d28dcbe2c1c4d5fccd334b0e68c861022a1bfbcf
STEP internal name: UTDTloopWithOpticsAndHXRev9_9_18_26.STEP
Export: 2026-10-06T16:40:01, SolidWorks 2026, AP214, native millimetres.
The exact uploaded bytes are preserved under source/. Every Rev9 dimension
comes from this CAD, not from an earlier PDF. Face numbers are the imported
OCCT enumeration for this source and the recorded extraction environment.
The reference/Rev8 JSON is the earlier CAD extraction and is used solely for
explicit comparison tables. Rev9 geometry does not inherit Rev8 dimensions.

START HERE
- VCU_Rev9_CAD_Engineering_Drawings.pdf: 8 printable A3 landscape sheets.
- data/VCU_Rev9_Engineering_Data.json: combined model, geometry and evidence.
- data/VCU_Rev9_Dimensions.csv: 199 long-format quantities; explicit units,
  status, basis and source fields. Safe first table for automatic ingestion.
- data/VCU_Rev9_Data_Dictionary.json: table meanings and column names/types.
- scripts/load_vcu_rev9.py: runnable pandas/JSON reading example.

CSV TABLES (13)
VCU_Rev9_Coordinates.csv — 57 ordered geometric reference points: 8 main-loop
  axis/corner limits, 23 sensor refs, 2 jacket planes, 6 exit/tank ends,
  4 clamp centers, 4 port ends, 6 hose ends/joins and 4 valve-axis ends.
VCU_Rev9_Sensor_Stations.csv — 23 sensor refs, 21 on the main loop and 2 on
  jacket ports; actual reference and projected-axis XYZ; distance to both
  leg ends, closest end, source and any contact gap/range. LF/PTC pairs can
  share a mounting body and coordinates; these are logical sensor references.
VCU_Rev9_Segments.csv — 8 segments in clockwise order with beginning/end XYZ,
  signed dx/dy/dn, chords, supported lengths, sources and qualification.
VCU_Rev9_Pipe_Axes.csv — 22 component straight or curved axes, including
  unique main-leg pieces, torus/spline corners, exits, tank, shell, nipples,
  hoses and drain. Individual heater pieces overlap: do not sum them blindly.
VCU_Rev9_Diameters.csv — 14 representative pipe/tube families: radii, OD/ID,
  wall thickness where meaningful, end-plate axial thickness and face evidence.
VCU_Rev9_Heater_Clamps.csv — 4 clamp centers/ends, stations from H, widths,
  bore radii and curved outer radii. These are mechanical heater-clamp limits.
VCU_Rev9_Branch_Connections.csv — TLEP and BREP extended-axis intersections,
  station from D/H, branch station from IN, axis residuals and source faces.
VCU_Rev9_Contact_Solutions.csv — all 21 returned minimum-distance solutions
  across the 12 STC bodies; both pipe-side and STC-body-side XYZ are preserved.
VCU_Rev9_Probe_Shafts.csv — 7 external sheath axis endpoints, lengths and OD.
VCU_Rev9_All_Cylindrical_Faces.csv — 1,226 leaf-instance cylindrical faces.
  This includes fittings, split faces and repeated instances. A radius is
  not automatically a bore, and an axial surface bound is not automatically
  a pipe segment length. Do not sum this inventory to get loop length.
VCU_Rev8_to_Rev9_Dimension_Changes.csv — 7 primary span/jacket comparisons.
VCU_Rev8_to_Rev9_Sensor_Changes.csv — 23 label-based comparisons, including
  the new PTC-X. Each revision uses its own B origin; global assembly
  translations are not interpreted as physical changes. STC selected points
  may vary within a non-unique geometric closest-point set.
VCU_Rev9_Dimensions.csv — long-format numeric index described above.

COORDINATE FRAME AND TOPOLOGY
Global CAD X/Y/Z retain the imported assembly transforms in millimetres.
Local origin B = [580.490685642161, -2830.921838891466, 1990.8865097103596].
x = B_CAD_Z - CAD_Z (right in the drawing)
y = CAD_Y - B_CAD_Y (up in the drawing)
n = CAD_X - B_CAD_X (normal to the main-loop drawing)
This is a right-handed frame. The main loop is planar to extraction precision;
hoses, coolant ports, sensors and valve have real out-of-plane offsets.
Clockwise order: B-C upcomer; C-D upper-left bend; D-E cooling leg;
E-F upper-right bend; F-G downcomer; G-H lower-right bend;
H-A heating leg; A-B lower-left bend; return to B.
A-H use straight-cylinder axis bounds, not virtual sharp corners. The three
analytical torus transitions have tangent endpoints. G/H are cylinder-axis
limits beside a spline transition. The separate virtual_corners_local_xy_mm
and virtual_corner_spans JSON fields extend axes to ideal sharp intersections.

REFERENCE AND LENGTH DEFINITIONS
- Main-loop station s is measured from the first endpoint of its straight leg.
  The nearest-end distance uses the axis coordinate, not horizontal distance.
- STC reference: one returned closest point on the main pipe to the STC solid.
  It is not necessarily the TC junction, or even a point on the STC body.
  The selected sensor-body point and every returned solution are also retained.
  Intersecting solids may return coincident points slightly inside the pipe
  envelope; they must not be interpreted as certified wall-contact junctions.
- LF/PTC/JTC reference: solid centroid of the local mounting-pipe body.
  This locates hardware, not optical active length or a thermocouple junction.
- Drawing symbols: STC gray dots, LF blue crescents, PTC/JTC green diamonds.
  Main-loop diamonds are on projected pipe axes; LF moons may be offset for
  readability. Numbers in the data are never offset to match the symbols.
- STC-01..12 and LF-01..04/PTC-01..04 preserve the prior collaborator convention
  by region and order. These names are not encoded DAQ labels in the STEP.
  PTC-X is the supplemental Rev9 probe sharing the LF-04 mounting body; its
  acquisition-channel identity is unassigned. JTC-A/B are coolant-port TCs.
- J-IN/J-OUT include both jacket end plates. Shell-only length is separate.
  TLEP/BREP IN is the tube end nearest the loop; OUT is the remote end.
  TANK IN/OUT are outer-cylinder axis ends. Port IN/OUT runs outward from the
  jacket. Hose IN/BEND/OUT labels are geometric order, not verified flow order.
- Branch crossings are closest points of extended cylinder axes, not a
  claimed tee or weld-plane location. TLEP crosses D+50.800 mm; BREP crosses
  H+19.769579 mm. Both tube IN planes are 4.0005 mm outward from the crossing.

KEY RESULTS AND UNRESOLVED CAD FEATURES
- Upcomer B-C: 1219.200 mm; cooling leg D-E: 1352.550 mm;
  downcomer F-G: 1228.668560 mm; inclined axes: 10.800 degrees.
- Heating leg H-A projected span: 1346.496215 mm. Its two unique cylindrical
  pieces sum to 1353.698560 mm, with 7.202345 mm projected overlap and
  0.151551 mm transverse offset. centerline_length_mm is null. The projected
  span supports stationing but is not asserted as an exact joined flow path.
- Three exact torus centerlines: R57.15 mm; A-B and E-F 79.2 degrees /
  78.998489 mm arc; C-D 100.8 degrees / 100.543531 mm arc.
- G-H exact endpoint chord: 86.619443 mm. Reconstructed supporting-surface
  spine: 98.265651 mm; G/H endpoint residuals 0.168531/0.145883 mm.
  Its exact continuous hydraulic centerline length remains unresolved.
- Jacket shell: 1017.5875 mm; complete with end plates: 1030.2875 mm.
  Pre-jacket from D: 127.561809 mm; post-jacket to E: 194.700691 mm.
  Shell OD/ID: 88.9 / 77.9272 mm. Each end plate is 6.35 mm thick with
  33.655 mm clearance hole. Main pipe OD: 33.401 mm; its bore is absent.
  The annulus hydraulic diameter 44.5262 assumes a concentric unobstructed
  jacket annulus; it does not establish the main-pipe hydraulic diameter.
- Main swept bodies and HX hose bodies do not contain a modeled bore.
  Exit tubes have ID26.924; LF/combined spools ID26.6446; PTC/JTC mounting
  spools ID25.4. These local IDs are deliberately not generalized to the loop.
- Heater clamps HC-01..04 are ordered H→A; centers at 109.941860, 478.241860,
  859.241860, 1214.841860 mm from H; each is 50.8 mm wide. Center spacings
  368.3 / 381.0 / 355.6 mm; outermost center span 1104.9 mm and mechanical
  outer-edge span 1155.7 mm. No wiring or energized boundaries are defined;
  active heater coordinates and length remain null.
- STC-01 is 1.0455 mm away from the pipe. STC-01/06/07/12 return multiple
  closest points. Returned ranges are algorithmic solutions, not a proven
  sensing footprint. No physical junction is labeled in the CAD.
- Each exit tube is 469.9 mm; tank outer-axis length 311.15 mm. These axes
  are inclined 10.8 degrees from vertical. TLEP-OUT and TANK-IN coincide.
- Each modeled hose has 304.8 mm straight + R76.2 mm, 180-degree turn;
  total modeled centerline 544.189360 mm. Hose bore is unknown.
- Drain body is simplified: OD42.545 / ID34.671; inlet outer-axis span25.4,
  crossbody span292.1 mm. No valve loss coefficient or verified passage
  connectivity is asserted.

MACHINE-READING RULES
CSV is UTF-8, comma-separated, with one header row, period decimal separator
and no thousands separators in numeric values. Blank numeric fields mean
unknown/not applicable; JSON represents those fields with null. Zero is a
measured/derived zero. _mm means millimetres; _deg and unit=deg mean degrees.
Keep the status and basis columns with every model input. Qualified spline
lengths and the projected heater span have explicit status values. CSV Booleans
use True/False; JSON uses true/false. No physical dimensions are repaired or
filled with nominal assumptions. Arrays/nested evidence are preserved in JSON.

QUICK PYTHON / PANDAS
    from pathlib import Path
    import pandas as pd, json
    root = Path('VCU_Rev9_CAD_Model_Package')
    dims = pd.read_csv(root/'data/VCU_Rev9_Dimensions.csv')
    sensors = pd.read_csv(root/'data/VCU_Rev9_Sensor_Stations.csv')
    points = pd.read_csv(root/'data/VCU_Rev9_Coordinates.csv')
    model = json.loads((root/'data/VCU_Rev9_Engineering_Data.json').read_text())
    jacket = dims[dims.component.eq('cooling_jacket')]
See scripts/load_vcu_rev9.py for projected sensor positions and corner ordering.

REPRODUCTION AND VALIDATION
The source STEP, raw inventory and contacts, HLR vector projection, spline
reconstruction, derived data and Python scripts are included. Environment
versions are recorded in scripts/environment_versions.json. CadQuery/OCP,
NumPy/SciPy and ReportLab handle extraction/geometry/vector PDF creation.
    python scripts/rebuild.py
runs the ordered source-to-report pipeline. The extraction scripts are specific
to this hashed revision: they intentionally use inspected part definitions,
face evidence and sensor mapping, rather than silently generalizing to new CAD.
Report generation also requires DejaVu fonts at the paths in draw_engineering.py.
The PDF output path is ../output/pdf/VCU_Rev9_CAD_Engineering_Drawings.pdf
relative to the package root. The supplied PDF is already built and inspected.

raw/rev9_verification.json: independent STEP reload verifies 12 long main-pipe
face bounds against projected boundary vertices (max 2.274e-13 mm discrepancy).
data/deliverable_validation.json: station sums, jacket dimension chain, closed
coordinate traversal, source diameter evidence, coordinate/CSV agreement,
null preservation and eight-page/source/sensor-ID checks. All eight sheets were
rendered and visually inspected. Numerical precision is extraction consistency,
not fabrication tolerance or confirmation of as-built hardware.
