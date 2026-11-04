---
title: Material equation citations and source support
status: maintained
owner: agent-root-model-citations-20261104 / TACC
updated: 2026-11-04
tags: [project/trident, doc/index, domain/materials]
---

# Material equation citations and source support

The proposal appendix now puts citations beside each material block. Cite the
source that actually supports the displayed law; keep source coefficients,
configured candidates and product references distinct. Original notes stay intact.

| Notes/model route | Citation key / verified source | Exact support and limit |
|---|---|---|
| Steel conductivity in both candidate libraries | `iaea2008Thermophysical`: [IAEA handbook](https://www-pub.iaea.org/MTCD/Publications/PDF/IAEA-THPH_web.pdf), Sec.6.3.2.2, Eq.6.27 | Exact match for `k=9.248+0.01571*T` with Kelvin input, for solid type316. Does not establish the different candidate rho/cp laws or installed316L identity. |
| Steel note's suggested rho/cp alternative | `mooseSS316Properties`: [MOOSE description](https://mooseframework.inl.gov/source/solidproperties/ThermalSS316Properties.html), [implementation](https://mooseframework.inl.gov/docs/doxygen/modules/ThermalSS316Properties_8C_source.html) | Exact match to the note's `cp=428.46+0.1816*T` and `rho=8089.4-0.4297*T-4.454e-5*T^2`. MOOSE's conductivity differs; its stated25–1300C range belongs to that alternative, not the configured v3 candidate. |
| ACU material-note blanket reference | `morganSuperwool2022`: [Superwool Plus data sheet](https://www.lynnmfg.com/wp-content/uploads/data/DATA-TC-1114-105.pdf), BU.05, April26,2022, p.2 | Density-dependent conductivity tables/product reference. It does not establish the legacy polynomial's fit history or actual installed product. |
| Fiberglass conductivity and nominal VCU geometry/product identities | `tridentMaterialNotes2026`: original main material note; stable Git permalink in proposal bibliography | Supports what the author's notes record. Fiberglass polynomial/range is in note text; product links alone do not derive all constants or fits. |
| Selected HITEC branches, legacy solids, VCU v3 rho/cp and heater-strip law | `tridentMaterialCandidates2026`: exact current HPC configuration snapshot | Exact coefficient/revision/range source. Primary fit publication remains unresolved for these specific candidate values; Jin/Kirst branch names alone are not sufficient attribution. |
| Steel-note history and alternatives | `tridentSteelNotes2026`: original steel note, pinned notes commit01cdee5 | Preserves crossed-out/selected suggestions and their original references. Does not change the HPC material selection. |

The NRC PDF linked by the steel note returned403 during text retrieval on
November4; it was not used as inspected equation evidence. McMaster links remain
the note's product pointers; their page content and fit derivations were not
certified. No source images or PDF pages were visually inspected.

## Original note routes

- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2 Main Material Props.md|Main material/product notes]].
- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2.2 Steel Pipe Properties.md|Steel note and alternatives]].
- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2.1 Prop 30 ThermoPhys Props.md|Prop-30 original table routes]]. No numerical fluid law was inferred from its images.

## Proposal and model routes

- The separate proposal owns `main.bib`, its generated technical appendix,
  `doc_support/committee/MATERIAL_SOURCE_RECORD.json` and
  `MODEL_PROPERTY_CITATIONS.json`. The former pins coefficients; the latter
  records exact/alternative/product-only/unavailable source support.
- `scripts/render_technical_reference.py` renders per-material citations from
  that metadata. Bibliography numbers follow first appearance automatically;
  align Markdown numbers only after a clean Biber build.
- The short model overview now follows the actual M1/M2 layer balances and
  signed upwind transport; `trident1DSolverWriteup2026` cites the versioned
  governing/numerical/wall-response appendices of the 1D write-up (4dda733).
- Exact sources and algebra checks: HPC initiative
  `runs/2026-11-04_OPS-009_model_citations/`. No model or coefficient selection
  changed, and these documentation checks do not answer pending scientific requests.
