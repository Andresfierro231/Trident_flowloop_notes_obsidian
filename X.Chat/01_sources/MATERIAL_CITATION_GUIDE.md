---
title: Material equation citations and source support
status: maintained
owner: agent-root-original-material-sources-20261104 / TACC
updated: 2026-11-04
tags: [project/trident, doc/index, domain/materials]
---

# Material equation citations and source support

The author's November4 correction supersedes OPS-009: **do not cite Trident
notes, personal material notes or internal candidate-library manifests in the
proposal bibliography.** Use verified originals or the master's/Rozak material
definitions only for equations actually supported there. Internal notes retain
discovery/provenance value. A shared material name is not proof of a shared fit.

| Adopted input | Verified citation support | Limit |
|---|---|---|
| HITEC working rho/cp/k/mu | `fierroMasters2026`, chapter4, Fixed fluid and solid properties | Exact implemented equations; original Jin paper coefficients not independently recovered. |
| HITEC rho/k | `rozak2026cfdNaturalCirculation`, AppendixB.1, printedp111 | Same rho/k; his polynomial cp and viscosity differ. |
| Legacy steel rho/cp/k/emissivity | Master's thesis, chapter4 | Full set present. |
| Both steel conductivity laws | [IAEA handbook](https://www-pub.iaea.org/MTCD/Publications/PDF/IAEA-THPH_web.pdf), Sec6.3.2.2 Eq6.27 | Exact k=9.248+0.01571T. IAEA rho/cp differ. |
| Legacy ceramic conductivity/emissivity | Master's thesis, chapter4 | Polynomial matches to displayed rounding; full precision preserved from implementation. Density128/cp1000 are prescribed inputs. |
| Rozak ceramic fit | AppendixB.4, printedpp113–114 | Different Cerablanket64 fit; do not attribute the legacy polynomial to this appendix. |
| Kirst alternative | Original exact coefficient source unresolved | Branch name is insufficient attribution. |
| VCU rho/cp, fiberglass/heater strip fits | Supplied working approximations; original fit source unresolved | Internal intake records user-forwarded ChatGPT surrogate inputs. Do not assign them to either thesis. Steel k has the exact IAEA source above. |

The [Superwool Plus manufacturer table](https://www.lynnmfg.com/wp-content/uploads/data/DATA-TC-1114-105.pdf)
is product context, not proof of the legacy polynomial's derivation. MOOSE's
alternative steel laws differ from selected VCU candidates. Exact-number web
searches did not identify the VCU fits; this does not prove they were invented.
No source images or PDF pages were visually inspected.

## Exact source routes

- TACC master source, separate external owner: `Papers/UTexas_Research/Master_support/csem-Masters_thesis/`; `AGENTS.md`, `README.md`, `chapters/04_reduced_model_methodology.tex`. Reference reading does not activate its manuscript workflow.
- TACC Rozak source: initiative `reference/Lit_rev/Ethan_Thesis_Integration_Package/pages/pdf_page_125.txt`, `pdf_page_127.txt`, `pdf_page_128.txt`; title page `pdf_page_001.txt` identifies May2026.
- Proposal owner: `main.bib`, `doc_support/committee/ORIGINAL_MATERIAL_SOURCES.json` (exact sources/hashes/support limits), `MATERIAL_SOURCE_RECORD.json` (unchanged numerical data), renderer and generated appendix. Align the Markdown companion after Biber.
- HPC verification: `runs/2026-11-04_OPS-010_original_material_sources/`.
- Original notes/attachments remain intact; internal audit records retain prior history, not current citation permission.

The model overview/equation checks remain OPS-009 work. No material selection,
research direction, processing hold or scientific execution changes here.
