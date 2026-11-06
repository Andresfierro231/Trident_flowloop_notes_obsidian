# Shared review audit, candidate aims and question coverage

21 October 2026. Canonical companion to both v1.0 first drafts.

## Skeptical claim audit

| Claim under consideration | Audit decision | Strongest evidence and remaining condition |
|---|---|---|
| A physically explicit reduced loop model is inherently novel | Remove | Conjugate/nonuniform-area/source/wall reduction already appears in S50/S52/S59/S65/S66. Define an additional model-class or predictive result. |
| Learning thermal-network structure with uncertainty is new | Remove | S26 already does this within a specified family, with mode/recovery limitations (Eqs7–20/PDF3–6; Table 4/PDF10). A transport/conservation/evidence increment must be specific. |
| Prediction-oriented calibration/design has not been developed | Remove | S71/S72/S76 explicitly establish different forms (S71 Eqs10–14/PDF5; S72 Algorithm1/PDF13; S76 Eq14–17/PDF13–15). |
| Discrepancy cannot be propagated to an unobserved QoI | Replace with a narrower claim | Output-only corrections do not supply that mapping automatically; embedded discrepancy is established by S75 Eq8a–c/PDF12. Whether the available evidence constrains it is the project question. |
| Good temperatures or narrow posterior bands validate flow/extrema | Unsupported | S19/S29 use indirect/shared thermal ingredients; S72/S75 distinguish observation agreement from target adequacy. Independent target-relevant evidence or a justified bound is required. |
| Similar Pr or matched Nu makes a loop quantitatively representative of an MSR | Unsupported | S56/S64 require more similarity; S74 uses same-correlation consistency; S29 does not establish salt-matched tested Pr (Table 4.10/PDF17; Fig22/PDF30). |
| CFD contours establish recirculation extent and its causal thermal effect | Unsupported | S20/S19/S29 provide numerical structures, not direct extent/causal validation. Descriptor convergence, controlled comparison and independent support are separate requirements. |
| Uncertainty propagation demonstrates calibrated prediction intervals | Unsupported | S02/S31 propagate the specified model/input information; S73 local curvature and S72 pointwise GP bands do not prove physical coverage. |
| A rigorous no-CFD dissertation core is possible | Feasible conditional proposal | Restrict targets to assessable thermal/duty/response quantities and a nontrivial identification/adequacy result; require energy/observation support and independent assessment. No completed result asserted. |

Source ambiguities are retained in dossiers rather than silently repaired. They are not proof that the authors' executed solvers are wrong. Unknown future facility facts, an author's future-work statement or a limited search do not establish a vacant research niche.

## Three provisional aims, with a two-aim no-CFD core

The names and identities of H01–H04 remain unchanged. The following three **candidate aims** group those hypotheses into reviewable work packages; they are not selected, approved or established novel contributions.

**Aim 1 — Determine supported predictions and parameter combinations under sparse thermal observation (H01).** Define a manageable class of conservative regional/segmented thermal models, explicit observation maps and uncertain boundary/initial quantities. Seek a nontrivial identifiability/invariance or information-limit result, then determine its consequences for a declared thermal/duty/response prediction. Begin with a tractable constant-property/passive or locally specified class; broader nonlinear transport is an extension, not a promised universal theorem.

- **Required evidence:** actual geometry/fluid/observation contract; an independently supported net-energy or inventory anchor where absolute parameters are claimed; justified nuisance uncertainty; approved independent assessment cases when empirical predictive benefit is claimed.
- **Strongest challenges/baselines:** S23/S26/S67–S70/S73; simple grouped balance versus overparameterized physical fit under the same information budget.
- **Failure condition:** the result repeats known scale/grouping arguments, depends chiefly on arbitrary bounds/priors, or changes no independently assessed QoI. **Fallback:** a precise non-identifiability/unsupported-quantity result with an engineering consequence; do not rename an effective coefficient a material property.

**Aim 2 — Establish when retained storage and transport physics earn their complexity (H02, with design supporting H01).** Develop and test a QoI-specific adequacy criterion across a small physical hierarchy. It should predict when omitting wall/insulation participation, advection, source placement or another declared mechanism changes the target beyond a decision-linked tolerance—not merely show a better fit after adding states. Compare feasible evidence choices as a means to challenge that criterion.

- **Required evidence:** declared target/horizon/tolerance; controlled model alternatives; qualified input/observation uncertainty; numerical refinement for the target; selection separated from withheld assessment.
- **Strongest challenges/baselines:** S18/S48/S52/S59/S65/S66, thermal model-selection studies and S71/S72/S75/S76. Compare simple models, ordinary covariance-aware fits and simple feasible designs before expensive methods.
- **Failure condition:** the criterion is only a retrospective sensitivity ranking, has no transfer to new conditions, or its benefit is indistinguishable from nuisance uncertainty/extra calibration. **Fallback:** retain the simpler model over a supported scope and identify a defensible boundary or unresolved ambiguity.

**Aim 3 — Quantify the limits of a specified surrogate-to-salt prediction (H04; H03 only as a gated local extension).** For a named circuit and QoI, study how source, loss, solid/property and observation distortions affect interpretation of surrogate evidence. Seek an additional uncertainty/adequacy result beyond repeating known similarity calculations. A local descriptor/thermal-effect study is optional and requires its own qualified spatial evidence.

- **Required evidence:** selected target architecture/fluid/envelope and source history; property uncertainty; relevant transfer comparator or independently justified bound; qualified fields/local observations for spatial claims.
- **Strongest challenges/baselines:** S15/S36/S56/S64/S65/S74, and S20/S29 for contemporary limitations. Compare established scaling/distortion methods, not only our favored model.
- **Failure condition:** the target remains undefined, existing methods already answer the question, or distortion/reference uncertainty prevents a useful inference. **Fallback:** complete Aims 1–2 as the no-CFD core, retain mechanism analogy and facility prediction, and omit quantitative reactor/local-flow claims.

A valuable negative result needs a precise model class, ambiguity or validity boundary and a consequential prediction. A failed fit or unavailable CFD alone does not meet that standard. A facility demonstration, an integration workflow, new physical evidence and a methodological/theoretical result should be reported as distinct contributions.

## Original-question coverage matrix

All 62 original IDs and full question texts are preserved in `question_to_literature_matrix.json` and `Question_to_Literature_Matrix.md`. The focus phrases below are abbreviations, not replacements. “Basis” means inspected literature supports the discussion; it does not mean project facts or new scientific results are established. ReviewA and review B refer to the two linked drafts.

| Original ID | Scientific question (abbreviated) | Review location | Evidence status / unresolved condition | Main sources |
|---|---|---|---|---|
| A1 | MSR decisions and QoIs | A§1; B§4 | Basis; decision tolerances open | S13/S50–S52 |
| A2 | Distinct reactor and circuit needs | B§3–5 | Basis; target circuit unselected | S13/S42/S51/S74 |
| A3 | Similarity and unavoidable distortion | B§6; A§4 | Basis; no actual TRIDENT scaling demonstrated | S56/S64/S74/S76 |
| A4 | Volumetric versus external source/loss | A§2/4; B§5–6 | Basis; conditional transfer | S20/S65/S66/S29 |
| A5 | MSRE discrepancy claim and CHF scope | B§2.5/4 | Original claim corrected; CHF not default scope | S47; PF01 |
| B1 | Minimum input/state/output contract | A§1/11 | Specified proposal; actual inputs need support | S71/S72/S75; PF01 |
| B2 | Bulk, point, wall and field outputs | A§5 | Definitions/basis; field support conditional | S19/S29/S32 |
| B3 | Unobserved extrema and honest uncertainty | A§5/7; B§8 | Partial; embedded route exists, evidence gate remains | S72/S75/S76 |
| B4 | Observation/sensor/placement effects | A§5–6 | Basis; facility mapping/response unresolved | S32/S68–S70 |
| B5 | Decision versus statistical tolerances | A§1/8; B§4 | Literature distinction; numeric values open | S32/S75 |
| C1 | Competing physical model forms | A§2–3 | Minimal hierarchy proposed | S50/S52/S66/S73 |
| C2 | Storage, losses, source and transport | A§2/4 | Basis; retention depends on target | S52/S65/S66 |
| C3 | Steady closure, inertia, advection/reversal | A§2.2/10 | Basis; equation assumptions explicit | S54/S55/S57/S59 |
| C4 | Convection/development/curvature closures | A§4 | Partial; all original correlation limits not audited | S19/S20/S60/S74 |
| C5 | Physical, learned and simple baselines | A§3/11 | Proposed comparison; advanced branches conditional | S04/S26/S67/S73 |
| C6 | Data, cost, constraints and failure modes | A§3/11 | Compared; resource-specific choices remain | S18/S26/S71/S72 |
| D1 | What reduction actually removes/learns | A§3 | Basis; operations distinguished | S18/S26/S59 |
| D2 | CFD-supported observation/closure maps | A§5/11; B§8 | Conditional; no qualified TRIDENT CFD | S19/S20/S29 |
| D3 | Goal, balanced, POD, nonlinear reduction | A§3 | Partial; not all families technically cleared | S04/S18/S25/S59 |
| D4 | Closure correction versus state enrichment | A§4/7/11 | Basis/proposed discrimination; causality not established | S29/S65/S66/S75 |
| D5 | Conservation, positivity, passivity frameworks | A§2/12 | Conservative formulation; port-Hamiltonian branch incomplete | S26/S52; our equations |
| D6 | Leakage-free case/regime assessment | A§10–11 | Assessment contract proposed | S18/S29/S71/S75 |
| E1 | Recirculation extent descriptors | A§5; B§8 | Definitions proposed; no validated descriptor selected | S20/S60; H03 |
| E2 | Thermal effect and ill-conditioned HTC | A§4–5; B§8 | Proposed quantities; causal/reference evidence missing | S19/S20/S29 |
| E3 | Controlled recirculation counterfactual | B§8; A§4/10 | Unresolved causal evidence; conditions stated | S20/S29; H03 |
| E4 | Minimum local correction/representation | B§8; A§3/11 | Conditional hierarchy; not selected | S19/S20/S75 |
| E5 | What sparse thermal data cannot identify | A§5–7 | Basis; particular TRIDENT ambiguity not proved | S19/S29/S75 |
| E6 | Future CFD evidence/data contract | A§10–11; B§8 | Proposed; no campaign assumed | S20/S29; H03 |
| E7 | External thesis and feasibility ladder | B§8 | Ladder preserved; Ethan reconciliation excluded | ExistingS35/S39 dossiers; PF01 |
| F1 | Identifiable combinations and diagnostics | A§6 | Basis; model-class result remains research | S23/S67–S70 |
| F2 | Scale ambiguity and energy anchors | A§6/EQ-05 | Elementary derivation; network uniqueness not guaranteed | Our derivation; PF01 |
| F3 | Hidden initial storage/input confounding | A§1/6/8 | Nuisance requirements; actual values open | S69/S70/S73 |
| F4 | Constrained, Bayesian/discrepancy fits | A§6–8 | Basis; fair comparison proposed | S23/S72/S73/S75 |
| F5 | Separate error sources or report confounding | A§7–8 | Conditional; independent information needed | S06/S69/S72/S75 |
| F6 | Experiment–CFD fusion without double count | A§7/10 | Partial; formal multifidelity/cut methods incomplete | S18/S19/S29/S75 |
| G1 | Uncertainty source/dependence taxonomy | A§8 | Specified; no numerical facility budget invented | S02/S31/S32/S73 |
| G2 | Propagation alternatives and limits | A§8/12 | Linear/MCbasis; other accelerators conditional | S02/S31/S04 |
| G3 | Shared instruments and derived quantities | A§5/8/EQ-06 | Basis; actual covariance needs evidence | S29/S31/S32 |
| G4 | Uncertain constrained closures/operators | A§3/7–8 | Partial; family-specific stability not guaranteed | S04/S26/S75 |
| G5 | Coverage, sharpness and proper assessment | A§8/10 | Distinctions grounded; empirical coverage absent | S31/S72/S73/S75 |
| G6 | Extrema/event/location uncertainty | A§5/8; B§8 | Partial; nonregular/spatial targets gated | S72/S75/S76 |
| G7 | Numerical error versus discrepancy | A§10 | Basis; target-specific verification required | S19/S20/S29/S75 |
| G8 | NEMO inverse structure and applicability | A§3 | Selected-methods evidence; conditional comparator | M-S05-01/02 |
| H1 | Smallest informative feasible design | A§9 | Proposed alternatives; minimum not established | S07/S71/S76 |
| H2 | Absolute energy-scale evidence | A§6/8–9; B§2.5 | Basis; installed evidence open | S47/S29/S32 |
| H3 | Excitation, duration, repeats, sensors | A§9 | Requests only; no universal setpoints/rates | S07/S71/S73 |
| H4 | Parameter, QoI, discrimination, validation design | A§9 | Established distinctions and challenger methods | S07/S71/S72/S76 |
| H5 | Extra evidence versus dropped claims | A§9/11; B§8 | Feasibility/fallback; no new instrument assumed | S19/S29/S75; PF01 |
| H6 | NickP0–P4 change requests | A§9 | Proposed matrix; exact approval/instrument/timing open | PF01/originalprotocols |
| I1 | Experiment/CFD input–output evidence | A§1/10–11 | Contract proposed; fields unavailable | S19/S20/S29 |
| I2 | Local QoI verification and validation | A§10; B§8 | Basis; no qualified TRIDENTreference | S19/S20/S29 |
| I3 | Regime, buoyancy, development, conjugate limits | A§2/4; B§6 | Basis; actual envelope/closure qualification open | S20/S57/S60/S74 |
| I4 | Efficient limited CFD discrimination | A§11; B§8 | Conditional design; no-CFD fallback retained | S48/S71/S76 |
| J1 | State estimate versus actionable forecast | A§1/8/11; B§9 | Contract distinction; actual decision owner needed | S73/S75; PF01 |
| J2 | Uncertainty/validity communication | B§9; A§11 | Proposed requirements; human-interface literature incomplete | S75; PF01 |
| J3 | BenBooth/NeutronOS result contract | B§9; A§11 | Collaboration boundary; architecture not assumed | PF01/originalbrief |
| J4 | Startup, freezing, pressure/level extensions | B§4/9 | Future physics/data explicitly outside core | S38/S51; PF01 |
| K1 | Closest prior methods and results | A§3–10; B§7 | Strong challengers incorporated; not exhaustive | S23/S26/S59/S67–S76 |
| K2 | Candidate contribution packages | Concluding aims | Three provisional aims; two-aim core | H01–H04 retained |
| K3 | Possible reduction, UQ, local/transfer increments | Aims/audit; B§7–8 | Hypotheses; no vacancy certified | S20/S74/S75/S76 |
| K4 | Method, theory, physics versus demonstration | Aims/audit; B§9 | Distinct contribution types; results not yet obtained | Strong-prior-method synthesis |
| K5 | Valuable negative result and evidence | Concluding aims | Precise limit plus engineering consequence required | S23/S70/S75; H01–H04 |

## Ranked remaining gaps and consequences

| Rank | Remaining gap | Why consequential / next action | Consequence if unresolved |
|---|---|---|---|
| 1 — P0 | Decision, QoI, horizon and tolerance for a specific facility/circuit | Choose what the model must support before optimizing accuracy or claiming transfer. Numerical thresholds require project/adviser ownership. | Retain a methodological study and relative comparisons; do not claim operational/safety adequacy. |
| 2 — P0 | Absolute energy and observation contract | Confirm actual deposited power/secondary duty, fluid/property identity, sensor map/calibration/clock/shared bias and initial solid states. Metadata/protocol descriptions suffice for planning; bulk data processing is not requested. | Restrict absolute parameter/flow claims; retain supported ratios and conditional thermal predictions. |
| 3 — P0 | Truly independent assessment cases and permissible development use | Distinguish proposed, approved and executed Nick-plan cases; reallocate any test used as an anchor or model-selection case. | Report verification/calibration or synthetic demonstrations, not independent facility validation. |
| 4 — P0/P1 | A precise additional theory/method result beyond the strongest priors | Formulate the model class and target; challenge it against S23/S26/S59/S67–S76. Embedded discrepancy and validation design are already prior art. | Do not make novelty claims; revise aims before committing a dissertation-scale implementation. |
| 5 — P1 | Source/implementation conventions and limited exact-version checks | Resolve consequential catalogue flags; read S23's algorithm supplement if reproducing it; compare final S71/S75/S76/S18 where wording/equations matter. | Use explicitly identified manuscripts and independently derived verified equations; avoid faithful-reproduction/compliance claims. |
| 6 — P1, conditional | Data and theory for advanced reduction/fusion | S03/S24/S25 and advanced balanced/manifold/port-Hamiltonian/multifidelity branches are not all technically cleared. Read only branches justified by the minimal comparison. | Preserve conservative simple/richer physical models; no requirement to implement every modern family. |
| 7 — P1/P2, conditional | Qualified spatial/causal evidence for local extent or extrema | S20 is now received/read; the gap is suitable reference/observation/descriptor evidence, not another copy of S20. | H03 stays conditional; do not claim experimentally validated local extent or heat-transfer causality. |
| 8 — P2 | Complete historical chronology and later operational/digital-twin scope | Original1969MSREtest record and later metrology follow-up remain unverified; S11 terminology and interface/human-use literature need targeted reading if those claims become central. | Keep the scoped history and collaborative advisory prototype; exclude exact unverified test stories, control and freeze/phase-change promises. |

**No essential new upload blocks these first drafts.** S20, S19, S72 final and S74 requests are resolved. Optional exact-version or supplement requests remain in `Upload_Requests_Current.md`; none justifies restarting broad discovery. ASME V&V 20 has not been fully acquired/read and no normative conformance is claimed. Selected official metrology clauses are now incorporated; unread portions are listed in their dossiers.

Operating data, FlowTests5/6, experimental execution, new instruments, assumed TRIDENT CFD, external contact and Ethan discrepancy reconciliation remain outside this pass. The no-CFD core proceeds through explicit contracts, conservative model comparisons, identification/adequacy analysis and honest assessment limits.
