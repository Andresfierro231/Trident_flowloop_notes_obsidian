---
title: Flowing versus conductive energy-balance audit
status: review
owner: agent-root-energy-audit-20261104 / TACC
updated: 2026-11-04
tags: [project/trident, doc/handoff, domain/thermal_network]
---

# OPS-011 — axial conduction versus enthalpy transport

November4,2026; owner agent-root-energy-audit-20261104 / TACC,
c318-009.ls6.tacc.utexas.edu, Linux. Scope: manuscript review and bounded
algebra verification; source code/configurations read only.

The author's intended flowing baseline neglects axial fluid conduction, as
explicitly stated in the master's chapter4. Previous proposal Equation1 instead
represented the conduction-enabled M2 diagnostic without explaining that choice.
Both molecular conduction and advective enthalpy may physically coexist; this
was an unqualified model-selection description, not algebraic double counting.
The corrected flowing fluid row is `0=H_(i-1)-H_i+g_i(P_i-F_i)`.
Radial fluid-wall heat exchange remains. Pipe axial conduction is separately
selectable. A no-flow conductive fluid equation is now shown separately.

High Peclet number, not merely nonzero flow, supports neglecting axial fluid
conduction. The length scale is the relevant axial temperature-variation scale.
Near stagnation/reversal, reassess the approximation; do not impose an unexplained
binary switch at exactly zero. M2/M3 diagnostics still retain default-on fluid
conduction through M1 unless `axial_fluid_conduction: false` is selected. No
runtime/default change, physical-case admission or rerun is claimed.

Independent residual checks:96synthetic states/1,440node comparisons, maximum
absolute difference below3e-14W; both flow signs and zero, constant/variable cp,
fluid/pipe conduction toggles, pairwise cancellation, global external budget,
zero-flow M1 equivalence and constant-cp enthalpy-reference invariance. Cooler
removal sign checked from source only; bounded numerical checks use the no-cooler
fixed-conductance five-cell diagnostic. No nonlinear solves or facility Pe study.
Sources/hashes, equation-by-equation findings and evidence limits:
`doc_support/committee/ENERGY_BALANCE_AUDIT.json`. Reproduce with
`python3.11 -B scripts/check_energy_balances.py --model-root <initiative>`.

Build: `bash scripts/build_proposal.sh build/OPS-011_2026-11-04`;
18pages/23references, unchanged reference order, no undefined references/citations
or overfull boxes. Actual pdfTeX1.40.24/TeXLive2022, latexmk4.77 via texlive/2023.
No images or PDF pages viewed. Original material coefficients/citations unchanged.
Both repositories pulled before edits; scoped commits receive a fresh clean pull
and push independently at closeout. Git history records publication, not another
agent's scientific acknowledgment.
