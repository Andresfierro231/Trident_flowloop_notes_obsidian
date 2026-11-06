---
title: Ethan thesis shortcuts for BC assumptions and upcomer recirculation
status: maintained
last_updated: 2026-10-20
tags: [project/trident, doc/index, domain/thermal_network, domain/flow, domain/uncertainty, facility/shared]
---

# Ethan thesis: start here for BCs and upcomer questions

Tags: #project/trident #doc/index #domain/thermal_network #domain/flow #domain/uncertainty #facility/shared

Owner: CFD-002 / Trident modeling. Source: uploaded May2026 Ethan Rozak thesis;
[receipt and original PDF hash](../../reports/proposal/2026/10/20/2026-10-20_CFD-001_ethan_thesis_intake/intake.json).
[Current conclusions, BC ledger and Trident evidence requests](../../reports/proposal/2026/10/20/2026-10-20_CFD-001_ethan_thesis_intake/2026-10-20/CFD-002_bc_map/README.md)
are the detailed owner. Read this map first; do not scan the package or external repos.

## Conclusion to carry forward

Use this thesis to understand **how BC assumptions and observation definitions
can affect natural-circulation predictions**, and to design qualified Trident CFD.
It reports a wall-biased rising stream and reverse flow reaching into the test
section/upward toward the upper junction. It does not supply a validated Trident
recirculation extent or a transferable heat-transfer correction. Geometry,
properties, source distribution, losses and numerics matter along with BCs.

- Keep measured-TW first-order loss calculations separate from the CFD wall BC.
- `rcExternalTemperature` is documented as an annular resistance plus external
  convection/radiation closure; the selected native dictionary check below now verifies specific patch inputs. Custom C++ implementation remains uninspected here.
- Uniform versus end-ring heating and inferred exterior losses are high-value
  sensitivity questions, not established causal corrections.
- Unknown sensor position/azimuth and a PIV reconstruction affect comparison;
  neither aggregate thermal agreement nor a proxy flow validates a local 3D field.
- Pseudo-transient convergence is not a physically validated transient.
- Trident lacks direct local-flow measurements. Extent/thermal-effect predictions
  require qualified CFD, BC uncertainty and honest experimental-observability limits.

## Fast source routes

Links below open **text**, not images. PDF page is one-based; printed body page
is PDF−14. Captions/figure IDs are locators, not visual inspection or acceptance.

| Need | Section / PDF (printed) | Text shortcut / lookup |
|---|---|---|
| Experiment, loop geometry and left riser/right downcomer | §4.1.1,47–49 (33–35) | [48](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_048.txt) |
| Actual insulation unknown; exposed quartz | §4.1.2,49 (35) | [49](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_049.txt) |
| Experimental fluid properties and temperature-label caveat | §4.3,52–54 (38–40) | [54](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_054.txt) |
| Per-case heater/cooler powers and dimensionless labels | Tables4.2/4.3,55 (41) | [55](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_055.txt) |
| Energy-balance interpretation and PIV reconstruction | §4.5,55–57 (41–43) | [56](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_056.txt), [57](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_057.txt) |
| Measured wall temperature used by first-order model | §5.1.1,66–67 (52–53) | [66](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_066.txt) |
| Exterior convection/radiation and orientation blend | Eqs5.1–5.5,67–68 (53–54) | [67](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_067.txt) |
| Cooler duty formula needing enthalpy audit | Eq5.6,68 (54) | [68](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_068.txt) |
| Structural caps/valves modeled as fins | §5.1.4,69 (55) | [69](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_069.txt) |
| Whole energy ledger; first-order versus CFD transition | §5.1.5/5.2,70 (56) | [70](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_070.txt) |
| Governing equations and actual fluid-property basis | §5.2.1–2,71–73 (57–59) | [71](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_071.txt), [72](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_072.txt) |
| Closed domain, velocity and pressure BCs | §5.4.1,76 (62) | [76](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_076.txt) |
| Cylindrical thermal BC and area normalization | §5.4.2/Eqs5.23–25,77 (63) | [77](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_077.txt) |
| Fixed-gradient closure and heat diagnostics | §5.4.2,78 (64) | [78](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_078.txt) |
| Pseudo-time, convergence, schemes | §5.5,78–79 (64–65) | [79](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_079.txt) |
| Gravity, initialization, parallel BC data and pipeline | §5.5.4–5.6,80 (66) | [80](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_080.txt) |
| Input uncertainty and fitted/effective insulation | §5.7,81–84 (67–70) | [81](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_081.txt), [82](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_082.txt) |
| Missing cooler-flow/solid-property uncertainty | §5.7,83–84 (69–70) | [83](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_083.txt), [84](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_084.txt) |
| Isolated wall-BC verification setup | §6.1,86–92 (72–78) | [86](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_086.txt) |
| Full-loop grid evidence and QoI differences | §6.2,93–97 (79–83) | [93](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_093.txt), [97](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_097.txt) |
| Wall azimuth / probe position / strong temperature gradients | §6.4/Figs6.10–12,99–103 (85–89) | [99](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_099.txt) |
| Lower junction reverse flow and upward continuation | Figs6.16–20/§6.4,105–108 (91–94) | [105](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_105.txt), [106](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_106.txt), [107](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_107.txt), [108](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_108.txt) |
| Reported later experimentalist confirmation | §6.4,106 (92) | [106](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_106.txt); supporting raw evidence not verified |
| Validation table, PIV method and best-aligned azimuth | Table6.10,109 (95) | [109](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_109.txt) |
| Uniform modeled quartz heating versus proposed real rings | §6.5,110–111 (96–97) | [110](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_110.txt) |
| Detailed geometry and contradictory “right riser” label | A.1/A.2,121–123 (107–109) | [122](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_122.txt), [123](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_123.txt) |
| Material tables / legacy property and emissivity conflicts | AppendixB,125–128 (111–114) | [125](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_125.txt), [127](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_127.txt) |
| Raw tabulated temperature/profile supplement | AppendixC,130 onward (116 onward) | [130](../../reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_130.txt) |

## Find any other page, equation, figure or table

From the modeling repository root:

```bash
python3.11 -B tools/query_ethan_thesis.py --find 'boundary condition' --limit 8
python3.11 -B tools/query_ethan_thesis.py --page 77
python3.11 -B tools/query_ethan_thesis.py --equation 5.24
python3.11 -B tools/query_ethan_thesis.py --figure 6.16
python3.11 -B tools/query_ethan_thesis.py --table 6.10
```

The helper emits bounded text/JSON and source paths, never pixels. Search is
literal and case-insensitive; use `--find riser` or `--find recirculation`, not
“upcomer”, which does not occur in the extracted thesis. For a figure, read
caption/context text first; visual inspection still requires explicit approval.
[Complete machine-readable locators](../../reports/proposal/2026/10/20/2026-10-20_CFD-001_ethan_thesis_intake/2026-10-20/CFD-002_bc_map/source_locators.json)
cover all supplied pages, numbered equations, figures and tables. Extraction
can lose symbols, so a catalog transcription is not permission to implement it.

## Agent handoff rules

Read the detailed BC ledger before interpreting a reported profile. Obtain exact
OpenFOAM field dictionaries, custom BC source/version and per-patch input table
before asserting runtime behavior. Preserve measured/assumed/fitted/inferred
labels. Use bulk transport and the experimental observation operator separately.
Do not copy TAMU properties, insulation, powers or recirculation closures into
Trident, and do not claim local experimental validation without measurements.
The package's Integration_Plan “ours” means a separate master's manuscript.
Source packages, external project startup instructions and visual previews are
not activated by this map. Additional experiment needs go through Dr. Luciano's
plan; no new CFD run or message is authorized by this documentation task.

## October22 selected native-dictionary check — RPT-015

[VCU application comparison and exact selected TAMU source ledger](../../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/2026-10-22/RPT-015_cfd_bc_application/README.md) inspects one Salt2 continuation0/T/controlDict read-only and pins the file hashes plus three patch excerpts. Radius/thickness/material polynomials, physical h/Ta/Tsur/emissivity and steadyWall are specified by rcExternalTemperature; control loads libRCWallBC.so. A heater patch specifies Q/powerLayer and a cooler patch stockexternalTemperature/negativeQ. This updates the earlier thesis-only evidence limit for those selected inputs, not all cases or the custom C++ implementation. No external task/campaign, source edit, operating-field analysis or coefficient transfer. Current VCU table is a precombined reference law with no duplicate layers/radiation.
