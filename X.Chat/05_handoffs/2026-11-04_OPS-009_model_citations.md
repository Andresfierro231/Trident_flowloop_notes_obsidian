---
title: Model overview and property-specific citations
status: review
owner: agent-root-model-citations-20261104 / TACC
updated: 2026-11-04
tags: [project/trident, doc/handoff]
---

# OPS-009

- User requested appendix citations from the notes and a model-faithful, brief
  replacement for the generic energy balance. Received bases: notes01cdee5,
  proposal8fa1ee8; independent pulls were current and clean before editing.
- Proposal correction was pushed at `04c4a24` after a fresh pull, with a clean
  worktree. This records publication, not another agent's receipt.
- Proposal Equation1 now shows the actual fluid/pipe/insulation steady residuals
  for the explicit-insulation/pipe-cooler form; signed upwind enthalpy and the
  nested temperature-dependent flow residual follow. The implemented wall-shell
  transient model is separated from the steady core. No model/source parameters changed.
- Exact local sources: canonical M1/M2/M3 notes and network implementations;
  read-only 1D write-up edition4dda733, governing/numerical/transient appendices.
  Source hashes and scope are pinned in proposal MODEL_PROPERTY_CITATIONS.json.
- The [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/MATERIAL_CITATION_GUIDE.md|material citation guide]] maps exact primary matches, note alternatives, product-only data and configuration-only candidates. Original notes/coefficients remain unchanged.
- Verified primary support: IAEA Eq6.27 matches steel conductivity; MOOSE matches
  the note's alternative rho/cp (not v3); Morgan's blanket sheet supplies product
  tables, not proof of the legacy polynomial fit. NRC retrieval returned403;
  McMaster links remain note product pointers rather than inspected fit sources.
- Per-material citations are generated from the proposal source record. Existing
  coefficients/ranges/provenance are unchanged. Original bibliography keys remain;
  Markdown numbers now match the 28-entry compiled citation order.
- Checks: 72 off-solution states / 1,080 node comparisons match actual assembly
  within 9.1e-13W, including signed/zero flow, axial toggles, nonlinear properties,
  unequal cells and pipe cooling. The 125 existing property comparisons pass.
- Final proposal build:19pages; pdfTeX1.40.24 / TeX Live2022, latexmk4.77;
  no LaTeX warnings/undefined references or overfull boxes. Output is
  `build/OPS-009_2026-11-04/main.pdf`. No image/PDF-page/CAD viewing.
- Exact task evidence: HPC initiative `runs/2026-11-04_OPS-009_model_citations/`.
  Actual resulting Git commits/clean state are recorded by publication receipts.
  Both owners must be pulled independently by the next agent; a push does not
  establish Mac receipt or answer pending scientific-result requests.
