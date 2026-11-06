# S77 — Structural identifiability of a heat-transfer system

F. J. Sanz Bermejo, É. Ramírez Laboreo, C. Sagüés (2023), *Revista Iberoamericana de Automática e Informática Industrial* 20(4), 412–420. DOI: [10.4995/riai.2023.19170](https://doi.org/10.4995/riai.2023.19170). Retrieved 21 October 2026 from the authors' [Zenodo record](https://zenodo.org/records/10722907), file `412-420-19170-ED.pdf`.

**Identity/completeness.** Typeset nine-page article; PDF page n = printed n+411. Title/authors/DOI/pagination agree with the journal and repository records. All §§1–5, Figure 1–7, Tables 1–2 and references are present. Main text read; equations/figures on PDF3,6,7,9 visually inspected. References inspected as leads, not read originals. No separate supplement identified or acquired; no code/data, proof reproduction or numerical rerun. Ready for scoped structural-identifiability/novelty synthesis, not a certified symbolic solver or experimental-validation claim.

## Extracted primary evidence

| Stable claim | Finding | Original locator | Governing qualification |
|---|---|---|---|
| S77-C01 | Three temperatures, four resistances and three capacities form a conductive RC model driven by power at node 1. | §2, Eqs1–10, PDF3–4/414–415 | Known power/ambient; no advection or buoyancy. R in K/W and C in J/K follow dimensionally from the balances. |
| S77-C02 | Full observation is identifiable; single T1 is not; T1 plus either other temperature supplies a minimum identifiable configuration in this model. | §§3.2–3.4, Eqs20–65, Table1, PDF5–7/416–418 | Minimal-realization/isomorphism assumptions; constant ambient in partial-observation analysis. Not a universal two-sensor rule. |
| S77-C03 | Different parameter sets produce the same observed T1 and different unobserved temperatures. | §4.2, Figures5–7, PDF8–9/419–420 | Constructed model example, not a measured flow field. |
| S77-C04 | Fitting uses moving-average-filtered experimental traces and constrained optimization. | §4.1, Eqs66–69, Table2, PDF7–8/418–419 | No separate untouched physical test or complete covariance budget is demonstrated in this article. |
| S77-C05 | State-isomorphism analysis addresses structural input–output equivalence under a specified model. | §3.1, Eqs11–19, PDF4–5/415–416 | The theorem's cited original is not thereby read; structural uniqueness does not establish practical precision or physical-model truth. |

The reported balances exchange the same heat rate with opposite signs. Unknown parameters enter reciprocally, although the state dynamics are linear. Initial-state and admissible-input assumptions belong to the input–output map. Equation transcription is unnecessary for the present novelty decision; see the source before implementation.

## Critical appraisal and transfer

**Our appraisal:** the conclusions' physical-parameter interpretation is stronger than structural identifiability alone warrants. A unique parameterization within a selected model, under ideal inputs/outputs, does not prove that fitted finite/noisy observations recover true material values. Model inadequacy, filtered errors and optimizer convergence remain separate questions. This appraisal follows the distinction between structural and practical inference, not a claim that the authors' calculation is wrong.

**Conditional transfer:** the paper is close prior work for H01's observation/anchor reasoning. It rules out novelty based merely on finding minimum thermal sensors, showing ambiguous RC coefficients or warning about unobserved states. A circulating-fluid model with uncertain calorimetry, shared biases and specific target estimands would require a new derivation, not an unexamined transplantation. There is no TRIDENT experiment, CFD or salt-property validation here.

## Coverage

| Material | Status / relevance | Not completed |
|---|---|---|
| §1 PDF1–3/412–414 | Read for scope and earlier methods | Cited originals not independently read |
| §2 PDF3–4/414–415 | Read/extracted; balance and topology visually checked | No code transcription |
| §3 PDF4–7/415–418 | Read/extracted; observation cases visually checked | No independent proof of every inverse/isomorphism |
| §4 PDF7–8/418–419; figures PDF9/420 | Read/extracted; ambiguity figures visually checked | No raw data, rerun or independent assessment |
| §5 PDF8–9/419–420 | Read with physical-interpretation qualification | No generalization beyond stated model proved here |
| References PDF9/420 | Discovery-inspected | Vajda–Rabitz1989 and earlier thermal-identification originals remain leads |

Further acquisition is conditional on selecting an exact theorem/proof route. No upload is required for this source.
