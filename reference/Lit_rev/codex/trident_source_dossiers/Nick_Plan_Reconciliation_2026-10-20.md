# Original Nick protocols: evidence reconciliation and proposed changes

20 October2026. The five supplied TeX originals were inspected as project documents **PF02–PF06**, corresponding to Phases0–4. They display Revision0.1/Draft. A requirement in a draft is not evidence that an instrument exists, a calibration passed, a test was approved or a run occurred. Originals remain unchanged; this document proposes reviewable scientific changes. No experimental data processing, test execution or protocol modification was performed.

Source locators below use original filenames, section/equation labels and line numbers in these exact supplied files; no compiled PDF pagination is invented. Hashes and identifiers are in project_protocol_registry.json. Original overall research priorities remain Markdown collé.md.

## What the originals already provide

| Phase / ID | Confirmed provisions | Where | Correction to earlier review |
|---|---|---|---|
| 0 / PF02 | Four penetrating fluid TCs, four Luna measurements, twelve under-insulation wall TCs; secondary duties, geometry/property/clock checks, environment/condensation and approved-channel matrix | Apparatus Tablechannels,lines246–263; Definitions,340–388; Procedure,399–480 | The earlier memo could not confirm these provisions. Retain them; do not request them as wholly new ideas. Their installed/as-built status remains to be verified. |
| 1 / PF03 | Full covariance propagation, TypeA/TypeB distinction, autocorrelation/block means, drift equivalence, class-specific acceptance, direct enthalpy-difference tests and model-independent diagnostics | TechnicalBasis,245–613; Procedure,618–730 | UQ/covariance is already central. Remaining work is mathematical qualification, resolvability and implementation evidence. |
| 2 / PF04 | Regional effective temperatures, positive C/nonnegative directed transfers, fixed sensor map, calibration/withheld warm/cold runs, model freezing, residual-duty checks and slow-mode uncertainty | Reduced-zone model,244–344; Method/Analysis,353–476 | Do not say the protocol lacks hidden-state caution, covariance or a holdout plan. Test its actual parameter scale and graph constraints. |
| 3 / PF05 | Two required low-duty heater-only/cooler-only states; blind comparison of frozen Phase2 model; reclassification and new independent validation after updates | §§2–3,244–372 | Both required runs are initially **validation**, not an existing calibration anchor. Earlier suggestion to use a P3 anchor is a scope change requiring explicit reallocation. |
| 4 / PF06 | Five unique states plus B-R repeat, separate target/constancy gates, signed exchanger-flow estimates, conditioning gates, covariance-aware consistency and frozen-model applicability check | Flowinference,258–334; Procedure,343–476 | These safeguards already exist. “Independent estimates” means separate balances, not independent statistical errors or a direct flowmeter. |

The drafts include provisional numbers: Phase1 at least6 h baseline plus a relevant environmental cycle; illustrative acceptance windows/classes; Phase2 roughly1 h conditioning and3 h relaxation with at least two warm and two cold runs; provisional±5/±10°C offsets; Phase4 enthalpy signal ratio5. **These are source-reported draft proposals, not recommendations or established safe/resolvable settings.** Measurement bandwidth, operating evidence, uncertainty goals and adviser approval still determine usable values.

## Ranked scientific issues and concrete changes

| Rank | Existing coverage | Proposed change / exact missing item | QoI and assessment consequence | Acceptance question |
|---|---|---|---|---|
| P0-1 | PF04 fixes inventories “where practical,” otherwise fits C/G and then freezes before blind PF05 | Make an **energy-scale declaration**: which C/inventory/source scale is independently fixed; which are uncertain; which combinations are fitted. If no adequate anchor exists, choose an explicitly identified P3 calibration case and add/retain genuinely independent steady validation. | Absolute loss corrections and physical capacities cannot be justified solely by passive temperature relaxation. No automatic extra run if existing inventory evidence suffices. | Which independent datum breaks the scale symmetry, with what participation/property uncertainty? |
| P0-2 | PF04 zonebalance/conductancematrix require whole-loop cancellation and stability | Add per-region balance/uniform-equilibrium and temperature-reference-invariance checks to the directed graph; use a reciprocal network or a physically mass-balanced transport network where justified. | A globally conserving matrix can still generate nonphysical internal exchange at uniform temperature. Affects fitted regional losses and slow modes. | Does every candidate satisfy both conservation and uniform equilibrium before fitting? |
| P0-3 | PF04 describes mixed-tank/two-fill initialization, then specifies continuous recirculation | Resolve the **actual preparation protocol** and ownership of tank/transfer steps; revise the analysis qualification accordingly. | Hidden solid/fluid initial-state uncertainty and repeatability depend on preparation; cannot claim two-fill evidence for a different procedure. | Which protocol is intended and feasible? Are both being compared as separately labeled designs? |
| P0-4 | PF04 withheld warm/cold runs select complexity | Call them **selection/validation runs**, reserve PF05 as blind assessment of the selected frozen model, and document any additional tuning reuse. | No need to pretend every holdout is a final test; prevents optimistic predictive claims. | Were any run outcomes used to choose model, weights, fitting interval or priors before assessment? |
| P0-5 | PF03 uses Tdiag/wall spread/fluid–wall offset to screen storage; PF05 calls this conservative/model-independent | Qualify as an observable storage screen. Where quantitative duty accuracy requires it, bound residual storage with inventory/temperature-rate assumptions and explicit unobserved-solid remainder. | Flat measured traces do not prove negligible total storage in unobserved insulation/tank/supports. | Is the possible residual-storage term small against the declared duty uncertainty/decision tolerance? |
| P0-6 | PF06 validates integral model before inferring local exchanger losses | Require a separate **regional-allocation/observation applicability check** for heater/cooler corrections and bulk enthalpy. Propagate uncertainty when mapping under-insulation wall and point/fiber signals to effective/bulk states. | Integral loss validation cannot uniquely validate Q_a,H and Q_a,C. Flow is model-dependent; may remain unreportable even with a good total balance. | Do independently supported local corrections and bulk-temperature definitions exist at operating gradients? |
| P1-1 | PF03 covariance/HAC method and baseline-frozen settings; later-state checking already required | Specify finite-sample/lag conventions, one coherent positive-semidefinite joint covariance estimate, and predeclared operating-regime checks. Do not treat a short-record bootstrap as extra independent evidence. | Protect duty/flow intervals without weakening the existing reporting-target logic. | Are sampling clocks, block lengths and effective independent cases adequate for the inference? |
| P1-2 | PF06 varies duty at fixed mean-temperature target and temperature at fixed duty | Preserve actual cooler/secondary control histories; distinguish a controlled-condition response surface from an autonomous forward test. Add a fixed-external-boundary prediction test only if required by the selected thesis claim. | Mean T is a controlled target/response, not an independent thermal BC for validation of that same T. | Which outputs were genuinely forecast versus used to establish the operating condition? |
| P1-3 | PF06 B/B-R tests path dependence; unique withheld applicability state designated | Freeze the applicability-case selection/analysis rule before examining its outcome; report dependence across the sequential campaign and adaptive A/C→Q_M choice. | Six accepted states are not six independent thermal histories or six independent uncertainty-calibration trials. | What level of interpolation, path-repeatability or regime-out generalization can this design assess? |

All proposed changes retain the draft's clock/record/uncertainty discipline. No numerical setpoint, repeat count or new instrument is imposed by this review. Physical changes require the facility's normal approvals, not a literature-derived guess.

## 1. Energy scale: the existing sequence needs an explicit choice

PF04 Eqzonebalance has unknown participating C and G. With no active input, scaling all these coefficients by a common positive a leaves the temperature trajectories unchanged. Effective initial temperature mappings do not remove that symmetry. Known fixed capacities/inventories can anchor it, but “nominal where practical” does not show which combination is known or how effective participation differs from total mass.

Two feasible branches:

- **Inventory-anchored branch:** document independent material/fluid masses, cp laws, effective participation assumptions and covariance; fit identifiable ratios/multipliers while propagating anchor uncertainty. Retain both PF05 runs as blind assessments. Test sensitivity to uncertain participation.
- **Duty-anchored branch:** predesignate a known-duty steady condition as calibration. If it is one of the originally blind PF05 cases, record its changed role and obtain independent validation in the affected warm/cold/condensation regime, consistent with PF05's existing revision rule. A global duty anchor alone does not identify every internal coefficient.

Without either branch, report temperature rates/identifiable combinations and honest loss scenarios; do not claim physical C or qualified absolute exchanger-loss corrections.

## 2. Directed-model mathematical audit

PF04 lines275–305 specify
\[
C_i\dot\Theta_i=\sum_j(G_{j\to i}\Theta_j-G_{i\to j}\Theta_i)
-G_{i,a}(\Theta_i-T_{a,i})+Q_i.
\]

**Analyst derivation, not a new literature theorem:** paired transfers cancel in the whole-loop sum. But at an entirely uniform state \(\Theta_i=T_{a,i}=T_0\), no active sources, the regional residual is
\[
T_0\left(\sum_jG_{j\to i}-\sum_jG_{i\to j}\right).
\]

Thus cancellation of the total alone does not preserve uniform equilibrium. Shifting every temperature and ambient value by a constant adds the same imbalance term. With the declared temperature mapping, require incoming=outgoing at every node for this direct coefficient form, or derive an appropriate physically consistent alternative. Conduction is reciprocal; closed-loop advective thermal transport needs continuity/enthalpy conventions. An empirical directed matrix requires more than nonnegative entries and stable eigenvalues.

For the closed transfer matrix L, conservation is \(1^\mathsf T L=0\), while common-temperature invariance is \(L1=0\). Those are different conditions. With diagonal positive C, the corresponding state-matrix conditions are capacity-weighted conservation and uniform equilibrium. If effective states instead use another coordinate/energy basis, explicitly derive the transformation and observation map rather than calling them temperatures with the current coefficients.

A minimal synthetic audit should test internal power cancellation, uniform equilibrium, Celsius/Kelvin shift equivalence, response to a known constant input, signed transport and stability with declared ambient connections. These checks are **proposed**, not experiments performed here.

## 3. Initialization and evidence-role corrections

PF04 lines237,249 reference a mixing tank/two-fill arrangement; Methodlines355–394 explicitly replace batch conditioning with continuous drain/refill recirculation. Analysisline448 again asks for tank uniformity before each fill and post-fill qualification. Either physical preparation can be documented and evaluated, but the current text mixes their assumptions. This is a concrete document consistency issue, not a reason to delay the literature work.

Warm/cold “withheld validation” is used to **select** candidate partitions (PF04 lines313–314,458,462). It therefore informs the chosen model. PF05's blind states are the next distinct predictive check if kept untouched. PF05 explicitly prohibits validating a revised model on the same data used for revision; retain that rule.

## 4. What the flow estimate can and cannot validate

PF06 correctly uses enthalpy integrals and consistent signs:
\[
\dot m_H=\frac{Q_{H,s}-Q_{a,H}}{\Delta h_H},\qquad
\dot m_C=\frac{Q_{C,s}+Q_{a,C}}{\Delta h_C}.
\]

Their statistical errors are correlated through properties, shared calibrations, the loss model and common thermal history. The existing covariance-aware compatibility/GLS step is appropriate in principle; it cannot establish accuracy against an independent flow truth. In particular, regional loss allocations can change these ratios while leaving the measured total loss unchanged.

Point or fiber-path temperatures must be shown to represent the relevant bulk enthalpy. PF04 explicitly calls its states **effective**, not separately predicted fluid/wall temperatures. Agreement of those states with a weighted observation is not independent validation of mixing-cup enthalpy at the exchanger plane. Phase4 model-loss uncertainty must include the allocation/observation discrepancy, or the output must remain conditional/unavailable.

For the stated mass-flow Reynolds formula, density cancels algebraically:
\[
Re=|\dot m|D_h/(A\mu).
\]
Density uncertainty remains relevant to volumetric flow and any upstream inference dependence, but should not be independently added a second time merely by also using \(Re=\rho uD/\mu\).

## 5. Storage and statistical qualifications

PF03 deliberately labels its sixteen-channel Tdiag as unweighted and not energy-weighted. This is useful for detecting some hidden redistribution. It does not make that average a rigorous storage bound. Under declared lump/representativeness assumptions, a possible conservative form is
\[
|\dot U|\leq\sum_i C_{i,\max}|\dot T_i|+\epsilon_{\rm unobserved}.
\]
The unresolved term and participating-capacity bounds must be justified; otherwise report an observable screening criterion rather than proof of zero storage.

PF03 Eqneweywest is a heteroskedasticity/autocorrelation robust sandwich expression. At lagzero it gives the uncorrected heteroskedasticity-robust estimate; it is **not exactly** the familiar finite-sample homoskedastic OLS variance for every white-noise realization, contrary to lines450–451's wording. Use the declared small-sample convention and assess performance with the actual correlation/sample size. The provisional two-standard-error and repeated-window rules are project allocations, not a demonstrated global false-acceptance probability.

## Coverage and stable claims

| Project source | Inspected scope | Skipped/unverified |
|---|---|---|
| PF02 Phase0 | Apparatus table, definitions and substantive procedure,lines230–263,340–480 | Shared formatting, nomenclature; schematic not checked against CAD/installed loop |
| PF03 Phase1 | TechnicalBasis/acceptance/UQ and procedure,lines245–730 | WorkedExamples731–1038 not fully evaluated; formatting/nomenclature; no statistical implementation test |
| PF04 Phase2 | Substantive introduction/model/procedure/outputs,lines229–476 | Formatting/nomenclature; no actual qualification data |
| PF05 Phase3 | Substantive body,lines229–372 | Formatting/nomenclature; no performed runs |
| PF06 Phase4 | Substantive body/flow equations/matrix/analysis,lines229–476 | Formatting/nomenclature; no accepted operating evidence |

| Claim ID | Finding | Exact source locator | Status |
|---|---|---|---|
| PF03-C01 | Covariance and autocorrelation-aware mean/drift methods already exist in plan | Phase1 §§TechnicalBasis/Uncertainty,245–603 | Project-text evidence, not executed validation |
| PF04-C01 | Directed coefficients need node balance/common-temperature invariance in addition to total cancellation | Phase2 Eqzonebalance/conductancematrix,275–305 | Analyst derivation from reported model |
| PF04-C02 | Passive fitting needs an explicit independently anchored scale | Phase2 model/fit sequence,273,309–317,456 | Analyst identification consequence |
| PF04-C03 | Two-fill and continuous-recirculation preparation descriptions conflict | Phase2 lines237,249,355–394,448 | Project-text consistency finding |
| PF04-C04 | Withheld Phase2 runs participate in model selection | Phase2 lines313–314,458,462 | They are selection evidence, not final untouched assessment |
| PF05-C01 | Both required Phase3 cases are blind and cannot validate a revised fit to themselves | Phase3 lines257–267,358–372 | Existing safeguard; preserve/reallocate explicitly |
| PF06-C01 | Primary-flow estimates are separate balances with common model/metrology dependencies | Phase4 lines261–334 | Not independent flowmeter truth |
| PF06-C02 | Mean-temperature matrix coordinate is achieved by cooler adjustment | Phase4 lines246–254 | Conditional/controlled response, not independent autonomous validation |
| PF03-C02 | Unweighted storage diagnostics do not by themselves bound total stored-energy rate | Phase1 lines506–548 | Analyst scope qualification |
| PF03-C03 | The printed Newey–West white-noise equality needs a finite-sample qualification | Phase1 lines424–451 | Analyst statistical audit; implementation not tested |

The next substantive methods reading can proceed with S18/S23 and S07. No remaining project-document request should ask for these five protocols again.
