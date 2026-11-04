---
title: Original material-source citation correction
status: review
owner: agent-root-original-material-sources-20261104 / TACC
updated: 2026-11-04
tags: [project/trident, doc/handoff, domain/materials]
---

# OPS-010 original material-source correction — 2026-11-04

Owner: agent-root-original-material-sources-20261104 / TACC,
c318-009.ls6.tacc.utexas.edu, Linux. Scoped manuscript/source documentation.

Removed the three author-rejected internal notes/library entries from main.bib
and all active appendix/Markdown citations. The master thesis chapter4 supplies
the working HITEC, legacy steel and rounded ceramic equations. IAEA Eq6.27
supports the exact steel conductivity. Rozak AppendixB supplies a distinct CFD
property set; cp/mu/ceramic differences are explicit. Title-page text corrects
Rozak's title and date to May2026 and removes the stale Forthcoming note.

VCU density/cp and fiberglass/heater fits, plus the Kirst alternative, have no
verified original exact-fit source. Supplied approximations remain identified
honestly; neither thesis is used as a false citation for these different laws.
Internal source paths, hashes, coefficient provenance and search limits are in
`doc_support/committee/ORIGINAL_MATERIAL_SOURCES.json`. The prior OPS-009 audit
is marked superseded for property citation policy. No numerical selection or
model equation changed.

Validation: source-record properties identical before/after;125numeric
comparisons across7materials; renderer exact match;18-page PDF with23 aligned
references, no undefined citations/references or overfull boxes. Compiler:
pdfTeX1.40.24 / TeXLive2022 via texlive/2023; latexmk4.77. No visual inspection.
Build: `bash scripts/build_proposal.sh build/OPS-010_2026-11-04`.
HPC check bundle: initiative `runs/2026-11-04_OPS-010_original_material_sources/`.
Notes navigation checker:17documents/72resolved links,0errors.

Both repositories were pulled independently before edits. Task-scoped commits
are pulled again and pushed independently at closeout; actual publication IDs
are in Git history. A push establishes transport, not another agent's receipt.
No external source repository edits or scientific execution occurred.
