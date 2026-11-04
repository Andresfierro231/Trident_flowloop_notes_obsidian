---
name: trident-equation-audit
description: "Check model equations against implementation, units, signs and conservation when reviewing or changing mathematical balances."
---

# Equation audit

Resolve the model owner from the active project map. Read the relevant row of
its `reports/IMPORTANT_REPORTS.md`, then only the named theory and implementation.

- Identify the selected model, states, units, signs, boundaries and configuration
  switches. Separate the implemented equation from a proposed approximation.
- Check each transfer enters connected cells with opposite signs. Sum the
  balances: internal transfers cancel; external power and storage remain.
- Distinguish axial fluid conduction, advected enthalpy and radial heat exchange.
  They can coexist. Zero bulk flow removes advection; it does not remove conduction.
  Explain a dimensionless comparison when useful without imposing a new cutoff.
- Check limiting cases, flow reversal, enthalpy reference and temperature-dependent
  properties where relevant. Prefer a bounded independent residual calculation
  over a new campaign. Reuse the owning verification script if it answers the question.
- Report source path/revision, actual checks and evidence limits. A manuscript
  correction does not change code or validate a physical operating point.

Preserve the author's selected assumptions. Record consequential changes in the
owner's existing theory/decision/index workflow; do not create another task system.
