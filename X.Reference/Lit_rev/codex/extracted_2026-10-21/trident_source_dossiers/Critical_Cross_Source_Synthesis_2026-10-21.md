> **S78 arrival update,21 October 2026:** the requested corrected13-page original is now scoped-read. Active acquisition request closed. See [S78 dossier](dossiers/S78_De_Tommasi_Passive_RC_2018.md), [Codex project questions](Codex_Project_Questions_for_Literature_Review.md) and [five next tasks](Five_Next_Tasks_and_Author_Inputs.md). Candidate recommendation remains provisional;S78 is a conditional linear conductive comparator,not a general sparse-observation loop solution.

# What the TRIDENT literature supports, and where a dissertation could contribute

**Critical synthesis, 21 October 2026.** Continues the v1.0 reviews, inspected dossiers and `Markdown collé.md`; it does not restart discovery. Source/claim IDs, H01–H04, M1/M2/M3, PF01 and the 62 original question IDs are retained. New CP01–CP04 are candidate work packages, not renamed hypotheses or established gaps. Findings are organized by scientific question and mechanism.

**Provisional recommendation:** develop CP01 and CP02 as a linked no-CFD research core, subject to a model-class/novelty gate. CP03 needs a named target circuit; CP04 needs qualified spatial evidence. No package is presently a demonstrated dissertation contribution. Applying the existing methods to a new loop, plotting a profile likelihood or adding wall states would not meet that bar.

Read this with the [methods review](Methods_and_Theory_Review_Working_Draft.md), [motivation review](Motivation_and_Contribution_Review_Working_Draft.md), [source index](Review_Source_Index.md), [claim ledger](Claim_to_Evidence.md) and [full original-question matrix](Question_to_Literature_Matrix.md). “PDF6/349” denotes PDF page 6, printed page 349. Dossier coverage controls what may be inferred from a cited source. No operating data, experiment, model code or new CFD was processed here.

## 1. What evidence is usable, and what must remain unresolved?

The carried corpus supports a critical first synthesis, not an exhaustive priority/novelty claim. Before this pass it contained 76 registered sources, 420 claims and 49 purpose-scoped dossier sources. Targeted web checks added S77, now read from an author-deposited typeset original, and S78, initially abstract-only and now scoped-read from the uploaded corrected original. Originals merely cited by inspected papers remain discovery leads.

| Evidence issue | Current status | Permitted use / blocked inference |
|---|---|---|
| S77 thermal-system identifiability | Complete nine-page published-format original retrieved; relevant equations and ambiguity figures checked; [dossier](dossiers/S77_Sanz_Bermejo_2023_Identifiability.md) | Strong novelty challenge to basic sensor/anchor and hidden-state arguments; no universal sensor rule or TRIDENT result |
| S78 passive RC identification | Corrected13-page published original now uploaded and scoped-read;new dossier and S78-C02–C09 | Strong prior for linear multiport response fitting;requires suitable ports/step-response information. Not a general nonlinear advective loop model or new method to assume |
| S71/S75/S76 manuscript versus final | Inspected identified manuscripts, final equivalence unverified | Cite exact manuscript locators; broad frameworks support synthesis; exact final implementation/wording remains conditional |
| S72 final and S72:THESIS1 | Final article inspected; earlier thesis asset remains distinctly identified | Do not combine differing versions into one set of equations or counts |
| Consequential equation conventions | Flags remain for S19/S29/S66/S72/S73/S74 and others in the implementation contract | Use qualitative mechanisms; resolve flags before literal solver reproduction. A printed ambiguity is not proof of a code defect |
| Official metrology and V&V | Selected S02/S31/S32 clauses inspected; S28 normative standard not completely acquired/read | Covariance/model-adequacy reasoning supported; no full-standard coverage or ASME conformance |
| Actual TRIDENT evidence | PF01 and proposed protocols supply context; operating data held; CFD, instrument calibration and completed holdouts not assumed | Feasibility conditional on metadata and permission; no validated physical parameter, local field or operational margin |
| Advanced reduction/error theory | Not every original for S03/S24/S25, passive realization or rigorous output bounds is cleared | Do not market conservation, stability, output bounds or nuisance-aware inference as intrinsically new |

These are different gaps: **formerly unavailable, now resolved** S78 original; **unread/partially extracted** advanced originals and metrology clauses; **unresolved version** manuscript/final comparisons; **missing project fact** decision tolerance and observation/energy contract; **unperformed research** new proofs or validation. No one category is evidence for another.

The new targeted search specifically tested the identifiability and passive-network novelty boundaries. It found S77 directly relevant enough to require extraction before recommendation. Other search leads—recent stability papers, network-identifiability theory and additional wall-inertia studies—were not silently added as read evidence. Exact queries, routes and outcomes are in `Synthesis_Search_and_Access_Log_2026-10-21.json`.

## 2. Which knowledge is established, limited, disputed or open?

The map below uses “established” for a result in its stated model or experiment, not a universal salt-loop law. Cross-source statements are analyst syntheses, recorded separately as SYN-C01–SYN-C10.

| Question / mechanism | Established and limited-domain evidence | Agreement, apparent disagreement or unresolved point | Consequence for TRIDENT |
|---|---|---|---|
| E01. What drives the response? Conservation, buoyancy and transport | Conjugate/source/loss loop models already exist: S50-C02 (§3/PDF3/515), S52-C02 (Eqs7–23/PDF5–7), S65-C02–C05 (§4/PDF8–10), S66-C01/C04 (PDF3–6/413–416) | Agreement that source/solid paths matter; no common universal importance ranking. Regime, boundary and output differ | Retain a conservative hierarchy; assess importance for a target, not by counting mechanisms. SYN-C01 |
| E02. Can a very small model capture circulation? | S59-C04/C05 gives a restricted asymptotic nonlinear Fourier subsystem and separate reconstruction (Thm3.6/PDF12–14/1083–1085); S18 adds conjugate Fourier dynamics under different coupling | Exact circulation reduction is not exact finite-time sensor/extrema reconstruction. These results are compatible, not contradictory | Specify which modes/physical states serve which output. “Reduced” alone is not novelty. SYN-C02 |
| E03. What can sparse temperature measurements identify? | S23 profiles nuisance-reoptimized parameters; S68-C05/C06 treats stable combinations and observation/structure; S70-C03/C05/C06 distinguishes aggregates from layer properties; S77-C02/C03 treats observation-dependent equivalence | Good observable predictions with ambiguous coefficients are compatible with structural identification under more informative measurements. Fixed model, known inputs and actual excitation differ | Derive the project's supported combinations/targets; do not equate a unique bounded fit with material identification. SYN-C03 |
| E04. Does network discovery recover physical structure? | S26 learns inclusion/coefficient uncertainty in a specified family (Eqs7–20/PDF3–6), with chain/recovery limitations (S26-C03/C05/C11); S78 now supplies a scoped original passive RC port-response comparator (Eqs15–22/PDF5–6) | S26's finite-data posterior/recovery and S77's ideal structural result answer different questions; no contradiction demonstrated | Structure learning needs meaningful physics, mixing checks and fair simple baselines. S78 now strengthens the passive-response prior;generalization to actual loop/observation structure still needs justification |
| E05. Can uncertainty reach an unobserved QoI? | S72-C02 restricts its observation-level discrepancy (§2.5/PDF7); S75-C01 embeds discrepancy in equations/observation/target maps (Eq8/PDF12) | Different discrepancy placements explain the different scopes. S75 is not refuted by S72's limitation | Propagation is possible under an informed backbone/closure; useful constraint and credibility are separate. SYN-C04 |
| E06. What should an experiment optimize? | S07 parameter information; S71-C01/C02 target information; S76-C01/C02 validation relevance; discrimination requires alternatives | These are distinct objectives. EIG, gradient alignment, physical similarity and predictive error are not equivalent scores | Choose the purpose first; use feasible design baselines and nuisance sensitivity. SYN-C05 |
| E07. Is a salt/surrogate loop representative of an MSR? | S56/S64 require fluid/solid/source/boundary similarity; S74 has simplified multigroup matching; S29 distinguishes candidate oil from achieved test range; S66-C07 gives conditional external/internal-source stability similarity | No direct disagreement: matched variables, actual cases, mission and outputs differ. Same-correlation Nu agreement is not independent heat-transfer validation | Name the circuit, source history and target; distinguish direct prediction, conditional transfer, analogy and incompatibility. SYN-C06 |
| E08. Does wall inertia always stabilize? | S66-C06 shows individual-property and combined-real-material effects can differ (§6.1/conclusion/PDF17/427); S57 separates friction transition and numerical effects | A universal stabilization claim is contradicted by these conditional results. We do not have common-case measurements establishing one universal direction | Test retained response/closure derivatives and numerical damping rather than assume more wall capacity is beneficial |
| E09. Does a close temperature fit establish local flow or extent? | S19/S29 use indirect/shared thermal information; S20-C06/C07 predicts recirculation numerically and leaves experimental assessment to future work | Sparse scalar agreement does not discriminate all spatial states. This is an evidence limit, not a finding that every numerical contour is wrong | H03 stays gated; no experimental extent or causal heat-transfer claim from fit alone. SYN-C07 |
| E10. Do uncertainty bands demonstrate predictive credibility? | S02/S31 propagate specified information; S73-C02/C06 uses local Gaussian/Hessian approximations; S75 distinguishes plausibility and target assessment | Conditional numerical/posterior precision and independent physical predictive coverage are different estimands | Separate numerical, observation, input, parameter, discrepancy and applicability uncertainty; state assessment independence. SYN-C08 |

### Compare like quantities before comparing conclusions

For each proposed agreement or contradiction, first match: control volume and coordinate; fluid/composition and temperature range; heating in fluid versus walls; cooler and ambient conditions; steady versus transient horizon; flow variable/averaging; observation mapping; calibration role; and uncertainty definition. An effective building capacity, wall material heat capacity and participating loop storage are not the same parameter. A pointwise GP interval, parameter SD, half a mesh spread and empirical case coverage are not the same uncertainty.

No pooled cross-paper percentage or combined accuracy estimate is justified here: geometries, source paths, observables, fitted quantities and assessment dependence do not match. The notable tensions are mainly overinterpretations—universal stabilization, physical parameter recovery, or blanket MSR representation—not controlled experimental contradictions. A true contradiction would require a common claim and overlapping assumptions with incompatible evidence, then investigation of uncertainty and independence.

## 3. Which MSR needs connect to decisions and assessable quantities?

Historical context matters through **purpose**, not a claim of direct reactor ancestry. S40's 1958 natural-convection reactor design trades pumps/maintenance against salt inventory (Introduction/PDF4/1; S40-C01/C02). S42 describes pumped normal MSRE operation (§2.4/PDF41/9 and §2.4.2/PDF44/12). S41's irradiated convection loop has a materials/fuel-exposure mission (PDF9/1; S41-C01). Those distinct roles already show why “a natural-circulation loop represents an MSR” is too imprecise. S47's separated exchanger/metrology issues motivate careful accounting, not a generic 25% discrepancy (conclusions/PDF31–32/27–28; S47-C01–C04).

| MSR need / circuit | Engineering decision | QoI | Governing mechanism | Inspected loop or original engineering evidence | Transfer limit and first defensible TRIDENT claim |
|---|---|---|---|---|---|
| Required heat transport, specified primary/secondary path | Can this configured path remove the assigned load? | Deposited heat, exchanger duty, ambient loss, storage; circulation if supported | Source–sink balance, buoyancy, friction, exchange | S13-C06/C07, §V.B–D/PDF20–25; S50/S52 conjugate/loss models | Circuit/topology and duty history must match. Facility duty/temperature prediction first; not reactor safety certification |
| Liquid-fuel primary temperature management | Which structures or fuel regions approach an assigned limit? | Defined wall/fluid temperature and a supported margin | Distributed salt/solid heating, advection, local heat exchange | S13 TableII/PDF17–19; S65/S66 source studies; S20 internal-generation concept | External heater is not nuclear generation; no neutronic/chemical coupling or unobserved global extreme validated |
| Passive residual-removal path, e.g. specified FHR/DRACS branch | Does heat removal persist without overcooling or overheating? | Duty/history, signed flow, temperature limits, time to limit | Coupled-loop buoyancy, exchanger resistance and property/closure choice | S51-C01–C03/C06, §§1–2/PDF1–2 and §4.8/Fig11/PDF8–9 | Salt/topology-specific thresholds and reliability probabilities cannot be borrowed; no assumed independent TRIDENT flow channel |
| Startup, source or sink change | Is the overshoot/settling compatible with a stated operating requirement? | Observed thermal response, overshoot, settling, supported flow transient | Fluid/wall/insulation storage, source partition, transport phase | S50/S52; S55/S57; S66 Eqs41/46/PDF6/416 | Heater-off is not nuclear shutdown; steady agreement does not establish transient adequacy |
| Freeze avoidance in a specified salt circuit | When is a qualified sensible-temperature margin lost? | Minimum supported temperature, cooldown rate, time above liquidus | Heat rejection/loss, inventory/storage, property dependence | S51 threshold scope; S38 separate solidification study | Crossing a threshold is not simulation of freezing/blockage; minimum anywhere requires spatial support |
| Source placement, insulation or local resistance selection | Which change materially alters heat delivery or temperature? | Regional loss/duty, response, defined temperature or flow | Competing pathways, solid storage and hydraulic feedback | S52/S65/S66; S64 distortion guidance | Changes in power and circulation confound attribution; prioritize observation-supported differences |
| Reliable inference and model use | What can be inferred now, and what additional evidence is valuable? | Estimable combinations, target ambiguity, uncertainty usefulness, held-out error | Observation/energy dependency and parameter equivalence | S23/S26/S67–S77; S02/S31/S32 | A new application is not new identification theory. Independent energy anchors and case roles must be explicit |
| Local mixing/recirculation where thermally consequential | Does a defined local structure change a decision-relevant thermal quantity? | Declared reverse-flow/exchange descriptor and controlled thermal consequence | Buoyancy/shear/development, counterflow, wall exchange | S20 PDF6–8; S19/S29; S37/S46/S60 diagnostics | No direct TRIDENT local-flow observations. Qualified spatial reference, descriptor convergence and causal comparison required |

S13 principally motivates liquid-fuel primary modeling, not every auxiliary subsystem (S13-C05). A single framework can be relevant across circuits, but transfer is a claim to demonstrate for a named output. No current reactor architecture or numerical tolerance is selected by this synthesis.

## 4. What do the closest existing methods already accomplish?

| Prior result / original locator | Already accomplished | Conditions and evidence limit | Precise additional result needed from us |
|---|---|---|---|
| S77 §§3.2–3.4/PDF5–7/416–418; S23 Eq10/PDF4/1926 | Observation-dependent structural identifiability; minimum configurations in a thermal example; nuisance-reoptimized practical profiles | Specified RC topology, ideal structural inputs/outputs; profiles depend on noise, bounds and optimization | A nontrivial result for a declared conservative transport/observation class and target, beyond repeating minimum sensors or an elementary scale ambiguity |
| S68 §§4.3–4.5/PDF6–7; S70 Figures5–7/PDF13–17/456–460 | Joint observation/structure/identifiability assessment; useful aggregate resistance despite internal ambiguity; free-run versus filtered-fit distinction | Building conduction, conditional data and effective parameter meanings | Explain which loop predictions survive ambiguity under actual uncertain energy/observation conditions, with independently assessed consequences |
| S26 Eqs7–20/PDF3–6; Table4/PDF10 and SUP1 diagnostics | Bayesian network inclusion and coefficient learning | Fixed prior family; recovery/mixing qualifications; building/synthetic cases | Additional physical/information-limit result; a new loop application or sparsity algorithm alone is insufficient |
| S73 Eqs1–2/PDF2/226 and §§2–4; S67 Eqs7–14/PDF3–4 | Stochastic physical fitting, partial discrete measurements, innovation likelihood and parameter profiles | Gaussian/local approximations; input error/shared biases not automatically identified; uncertainty local | A justified estimand/model-error/measurement contract and demonstrated benefit versus ordinary constrained fits |
| S59 Thm3.6/PDF12–13/1083–1084; S18 Eqs24–36/PDF6–7 | Rigorous restricted asymptotic circulation reduction; conjugate Fourier loop models | Different forcing/coupling; slave-mode reconstruction and finite-time observations matter | A valid finite-time/output or retained-physics result for an expanded but tractable model class |
| S65 §4/PDF8–10; S66 Eqs41/46/PDF6/416, §6.2/PDF12–14 | Source partition, wall time scales, heat-transfer derivative and stability; conditional source equivalence | Linearization/regimes and particular geometry/boundaries; code comparisons, not universal measured truth | A target-specific adequacy/domain criterion robust to observation/input ambiguity, not “wall effects exist” |
| S71 Eqs10–14/PDF5; S72 Algorithm1/PDF13 | Nonlinear prediction-information design and goal-oriented calibration | Assumed prior/likelihood/target; cost/bias and observed-target restrictions; no guaranteed superiority | A testable new physical or information-limit result; target-weighting or EIG use alone is established |
| S75 Eq8/PDF12, §3.3/PDF19–23; S76 Eqs14–17/PDF13–15 | Embedded discrepancy propagating to unobserved targets; prediction-specific validation-design relevance | Credible backbone/observation maps; certainty/coordinate and error-propagation restrictions | Show why a proposed extension is additional to these frameworks and informative under available evidence |
| S56/S64; S74 §4.1/PDF8 and Table4.10/PDF17 | Fluid/solid scaling, distortion analysis and modern multigroup surrogate comparisons | Definitions, wall/source/loss omissions and chosen regimes; same-correlation checks not independent validation | A new target-specific distortion/uncertainty or applicability result beyond calculating familiar groups |
| S19/S29/S20 dossiers | Modern thermal/CFD comparisons, indirect circulation and numerical local structures | Shared thermal ingredients; calibration/numerical selection; limited independent local evidence | A qualified discriminating/causal result, not another contour or measured-temperature match |
| S78 Eqs15–22/PDF5–6;§4/PDF7–8;Table1/PDF10 | Passive real-pole multiport step-response fitting and Foster realization,with shared time constants | Linear diffusion/computed full-response cases;outer fit nonlinear;equivalent elements not physical layers;entrywise superiority not established | New passive fitting alone is established;check actual actuators,ports and observation support before adopting as a baseline |

The strongest novelty counterargument is often that an existing framework already permits the proposed analysis, even if the exact facility has not been studied. A dissertation can still contribute physical understanding, a useful theorem or a new qualified dataset, but must specify what was not already implied and demonstrate its consequence. Absence of a paper about ACU/VCU is not that specification. SYN-C09.

## 5. How should the model hierarchy be connected to evidence and QoIs?

Complexity has several axes: spatial resolution, thermal storage, hydraulic dynamics, closure flexibility and learned parameters. The rows below are comparison roles, not a claim that one universal scalar order ranks all models. Existing M1/M2/M3 retain their project meanings.

| Model / retained physics | Supported candidate QoIs | Information and computation required | Principal uncertainty / failure test |
|---|---|---|---|
| Global steady balance; current M1 no-flow energy | Net duty/loss consistency, a grouped thermal level | Qualified power, cooler/ambient accounting; negligible storage | Net-energy scale and point/bulk meaning; cannot recover spatial allocation/flow uniquely |
| Current M2 prescribed-flow energy | Conditional temperatures/duty at supplied flow | Flow input with provenance, source/sink and properties | Input-flow uncertainty; cannot assess autonomous circulation as an output |
| Current M3 scalar steady buoyancy–resistance | Steady circulation branch and coupled thermal predictions | Geometry, resistance/property/closure support; solve periodic energy and pressure balance | Branch/sign, low-flow laws, energy/flow dependence; not reversal/transient dynamics |
| Small transient regional thermal network | Measured regional response and grouped time constants | Initial states, input histories and observation map; few states | Capacity/conductance scale and hidden storage; model parameters may remain effective |
| Conservative segmented fluid–wall model | Thermal transport delay, regional loss/storage, measured wall/fluid response | More geometry/source detail and identifiable combinations; mesh/time verification | Closure/observation ambiguity, numerical diffusion; complexity must earn held-out target benefit |
| Add justified insulation/axial transport or transient momentum | Additional response scales, source paths, qualified circulation transients | Evidence that omitted dynamics affect target; constitutive derivatives and signed conventions | Separating slow storage from loss/input drift; stability and low-flow numerical error |
| Fourier/projection or hybrid learned model | Particular spatial modes or rapid input-to-target map | Basis/training/reconstruction evidence; physical constraints and regime coverage | Missing fields, retained-mode target error, instability, extrapolation; advanced originals conditional |
| Qualified spatial CFD/reference plus local enrichment | Defined local transport/extent or supported extrema | Field/reference availability, mesh/time/model/input uncertainty and compatible observations | CFD is conditional evidence; contours require descriptor-specific convergence and physical assessment |

Use the same available input, calibration and assessment budgets where the prediction contracts match. Compare a model-only output and a discrepancy-corrected output separately. For sparse thermal observations, a simple covariance-aware fit is a serious baseline; adding filtering, posterior parameters or a neural closure does not establish better autonomous predictions.

### Two analytical checks that clarify a contribution without claiming new theory

**SYN-D01: exact and practical target support.** Let a declared model/observation contract produce observations F(θ,η;d), with physical parameters θ, nuisance quantities η and design d. Let E be a set of admissible parameter/nuisance choices indistinguishable under that contract. In an ideal structural analysis, indistinguishable means the same input–output map under the stated admissible inputs. In a finite experiment it instead means an explicitly justified discrepancy/confidence set; these sets must not be conflated.

For a scalar target q define its spread over E as

\[
D_q(E)=\sup_{a,b\in E}|q(a)-q(b)|.
\]

If Dq exceeds twice a chosen absolute tolerance ε, no single point prediction can be within ε of every member of E, by the triangle inequality. If its bounded scalar range is known, its midrange has maximum error Dq/2 **within this assumed set**. Units are those of q. At a regular point, a necessary condition for a differentiable target to be a differentiable function of the observation map is ker(JF) ⊆ ker(Jq), with nuisance columns included. This follows by the chain rule and is a first-order diagnostic. At singular points, zero observation derivative need not mean exact indistinguishability: y=θ³ and q=θ at θ=0 is a simple counterexample to that interpretation. The condition is not a global, singular-point or finite-noise certificate.

These are our elementary deductions and problem definitions, not novel theorems or computed TRIDENT bounds. S23/S70/S75/S77 already motivate target-versus-parameter distinctions. The hard research would be characterizing an appropriate equivalence/uncertainty set, supported combinations and a useful bound for a specified nontrivial physical class. A narrow prior or omitted discrepancy can make Dq falsely small. Practical confidence requires both a credible set and a correct-enough model, not just optimizing its diameter.

**SYN-D02: a wall-state elimination test.** In our restricted constant-coefficient two-path example,

\[
C_w\dot T_w=G_{fw}(T_f-T_w)-G_{wa}(T_w-T_a).
\]

For zero initial perturbations, fixed ambient and fluid-temperature perturbation input, eliminating the wall in the Laplace domain gives heat-flow admittance

\[
Y_w(s)=G_{fw}\frac{C_ws+G_{wa}}{C_ws+G_{fw}+G_{wa}},\qquad
\tau_w=\frac{C_w}{G_{fw}+G_{wa}}.
\]

Cw is J/K, G values W/K, s has units 1/s and Yw W/K. At s=0 this is the series conductance; at high frequency it approaches Gfw. Nonzero initial wall storage adds a forcing term. The exact difference from its zero-storage value is

\[
Y_w(s)-Y_w(0)=\frac{G_{fw}^2C_ws}{(G_{fw}+G_{wa})(C_ws+G_{fw}+G_{wa})}.
\]

This verifies the steady and zero-capacity limits and shows why a steady-fit coefficient need not capture transient exchange. It is conventional linear elimination, not an additional result beyond wall-aware prior art. Small ωτw alone is not a complete target-error criterion: amplitude, downstream dynamics, initial conditions and hydraulic feedback can magnify or mask the difference. S66 already treats the flow derivative of heat exchange. CP02 must go beyond this example to a justified output/applicability result and test it independently.

## 6. Which candidate contributions could teach something new?

### CP01 — Supported predictions under physical-parameter and measurement ambiguity

**Links:** H01; original questions B, F, G, H and relevant C/D. **Gap type:** identifiability/theory, with validation implications. This is a candidate precise problem, not an established vacant field.

**Narrow question and falsifiable hypothesis.** For a defined conservative regional/segmented thermal class with a specified source and centerline/wall observation contract, which parameter/nuisance equivalence classes remain, and which duty or thermal-response predictions are invariant or bounded usefully over them? Hypothesis: an explicitly derived combination/anchor characterization can distinguish supported from unsupported targets and improve robustness over interpreting every fitted coefficient as physical. Absolute energy scale, shared calorimetry and observation bias must be part of that statement, not post-fit caveats.

**Strongest existing result and proposed advance.** S77 already demonstrates ideal observation-dependent equivalence; S68/S70 already identify stable aggregate quantities and effective-parameter limits; S23 supplies profile tools; S73 supplies stochastic fitting. The proposed advance must characterize a **specific additional conservative transport/measurement class**, including a nontrivial target-support or anchor result. Deriving only G/C from passive cooldown, showing correlated parameters or finding two sensors does not qualify.

**Understanding and domain.** A successful result explains why some outputs remain inferable while others do not, what physical/measurement assumptions create that boundary, and what attainable independent evidence changes it. Start with fixed topology, positive constant properties and a declared flow/source approximation; extend nonlinear buoyancy, temperature dependence or uncertain sensor response only after the tractable class is resolved. No global claim for arbitrary networks or regimes.

**Strongest novelty counterargument.** This could be ordinary structural identifiability, reparameterization and profile-based prediction uncertainty packaged for a new loop. The same effect may follow immediately from S77's tools or the cited general theory. Reject the novelty claim unless the extra class/result and practical consequence withstand that comparison; acquire the relevant foundational original before claiming a theorem extends it. S78 additionally rules out passive response fitting alone as a methodological advance;its equivalent realization does not identify material layers.

**Required work and assessment.** Derive symmetries/identifiable combinations including admissible initial states and nuisance inputs; check generic and singular regimes; distinguish state observability from parameter identifiability. Verify algebra against counterexamples and synthetic recovery using independent numerical formulations. Compare grouped balance, ordinary constrained covariance-aware fit, nuisance-reoptimized profiles and an S73-style fit where justified. Use identical information and bounds; assess autonomous, held-out target predictions and ambiguity robustness. An energy-derived flow cannot be treated as independent evidence of its own ingredients.

**Feasibility:** without CFD, substantial theory/synthetic work and assessable thermal/duty tests are possible if metadata/anchors and later approved cases exist. Limited CFD may test observation-map discrepancy, not eliminate structural ambiguity. Adequate CFD adds conditional field targets but still requires reference uncertainty and cannot supply independent material truth by decree. No new instrument is assumed; analyze existing feasible evidence first.

**Fallback versus dissertation threshold.** Useful fallback: a transparent parameter/target-support audit and trustworthy effective model for the facility. Sufficient research would require an additional nontrivial model-class/information-limit result with demonstrated generality or consequential independent predictive assessment; the audit alone is implementation practice. **Rejection:** ambiguities disappear under a known standard result, the proposed grouping is unstable to admissible nuisance uncertainty, or it changes no assessable prediction. A negative result is generalizable only if it establishes a precise impossibility/validity boundary for a class and identifies its engineering consequence.

### CP02 — When do wall storage, source pathways or transport earn their complexity?

**Links:** H02 and H01. **Gap type:** physical understanding and applicability/theory, with computational assessment.

**Narrow question and falsifiable hypothesis.** Within a restricted single-phase class and operating domain, can a criterion predict when omitting a selected wall/insulation storage or transport mechanism changes a declared finite-time thermal/duty QoI beyond tolerance, after allowed parameter and nuisance re-fitting? Hypothesis: an output-weighted retention criterion using mechanism time scales, source paths and observation support transfers to withheld conditions better than a nominal time-scale rule, sensitivity ranking or adding states indiscriminately.

**Strongest existing result and proposed advance.** S59 already gives a restricted rigorous reduction; S18 conjugate Fourier reduction; S65/S66 source and wall stability; S68/S69 model-order assessment; S75/S76 target-aware assessment. The candidate advance is a **qualified finite-time adequacy boundary** for a declared class/output, not discovering that wall inertia or advection matters. A generic linear transfer-function bound may already cover the intended case and must be checked before a new theorem is claimed.

**Understanding and domain.** Explain the physical distinction between a hidden state that changes an observed trajectory, one whose effect calibration absorbs, and one that leaves calibration nearly unchanged yet changes the intended prediction. Connect that distinction to source location, initial storage and buoyancy/closure feedback. Begin with constant-property, single-phase, non-reversing cases and clear measured targets. A stability boundary, reversal or local maximum is a separate harder target, not a promised extension.

**Strongest novelty counterargument.** A posteriori error estimation, singular perturbation, transfer-function reduction and sensitivity-informed model selection already address model adequacy. Merely defining a dimensionless wall time, showing a richer model fits better or creating a retrospective regime plot is insufficient. S66 and S59 are particularly strong challenges; their technical appendices/proofs need deeper extraction if the claim rests on extending them.

**Required work and assessment.** Derive a restricted mechanism elimination/error expression with stated norms, horizon, initial conditions, input amplitudes and stability assumptions; test its breakdown. Analyze output sensitivity and uncertainty margins, including closure derivatives when flow couples back. Compare global/regional, steady-closure and dynamic-wall/segmented alternatives; use matched calibration budgets. Test criterion predictions on new conditions, not just conditions used to construct it. Numerical mesh/time/modal effects must be smaller than the claimed mechanism effect or explicitly retained.

**Feasibility:** no CFD is needed for a tractable derivation, conservative 1D/synthetic counterexamples or measured thermal-response assessment. Limited qualified CFD can test selected observation/source distortions; it cannot validate a universal boundary. Adequate CFD can broaden regime/geometry testing with solution/input/model uncertainty, still distinct from experimental validation. Required experiments are proposed independently varied source/sink/initial-state cases only if Nick/facility approve and can supply them; no execution presumed.

**Fallback versus dissertation threshold.** Useful fallback: justified retention of the simpler model over a supported envelope and a reproducible fair-comparison specification. A scientifically sufficient contribution needs a transferable physical/applicability result or bound, with evidence distinguishing it from ordinary refit/sensitivity effects. **Rejection:** classification fails under permissible nuisance changes, is only retrospective, or does not outperform existing simple criteria on independent cases. A negative result is useful research if it proves that a common criterion is insufficient under defined physical conditions and provides a general counterexample/boundary, not merely one bad fit.

### CP03 — When does surrogate-loop evidence discriminate a specified salt-circuit prediction?

**Links:** H04. **Gap type:** physical knowledge/scaling/applicability, with uncertainty.

**Narrow question and falsifiable hypothesis.** For one named target circuit and QoI, do unavoidable fluid/solid/source/loss distortions change the prediction enough to alter what can be learned from the surrogate? Hypothesis: an explicitly derived, uncertainty-aware distortion assessment identifies domains where one dominant distortion changes model discrimination or target inference despite otherwise matched familiar groups. The direction or dominant distortion is not assumed in advance.

**Strongest existing result and proposed advance.** S56/S64 already analyze fluid/solid similarity and distortion; S65/S66 compare sources and stability; S74 supplies a modern high-Pr multigroup study. The advance must connect a specific unavoidable distortion to a nontrivial target error/applicability or learning limit, beyond recalculating Re/Pr, wall ratios or matching Nu from one shared correlation.

**Understanding and domain.** Determine when a seemingly secondary source path, wall time or heat loss changes the selected inference, and why its importance differs between steady duty, transition response and stability. Domain must name target architecture, fluid/property range, gravity/topology, source/sink and horizon. A liquid-fuel primary with distributed generation, a solid-fuel salt-cooled heat path and a secondary transport loop cannot be combined into one universal representation claim.

**Strongest novelty counterargument.** Existing hierarchical scaling/distortion methods and target-sensitive validation may already provide this assessment. A new fluid selection or facility table is usually implementation. No gap is established until the target and the relevant prior applicability analyses are specified.

**Required work and assessment.** Derive matched and deliberately distorted cases with consistent nondimensional definitions, property uncertainty and source/solid accounting. Keep nuisance/source changes controlled; compare existing scaling rules, a simple prediction model and a richer reference under the same target. Use an independent target-relevant comparator or a separately justified bound; a matched correlation is not such a comparator. Distinguish transfer uncertainty from uncertainty internal to the surrogate model.

**Feasibility:** without CFD, nondimensional/uncertainty analysis and selected conservative 1D comparisons can proceed after target selection; quantitative reactor accuracy cannot be asserted without reference support. Limited CFD helps isolate one distortion with conditional comparisons. Adequate CFD or qualified matched experimental evidence can test broader behavior, subject to model/input uncertainty and scope. No target or resources are assumed present.

**Fallback versus dissertation threshold.** Useful fallback: a defensible mechanism analogy and applicability ledger, preserving the value of facility prediction. Sufficient contribution: an additional scaling relationship, target-specific bound or validated applicability limit that changes a consequential interpretation beyond existing methods. **Rejection:** the target stays undefined, previous scaling already resolves it, or reference/property uncertainty overwhelms discrimination. A negative result is generalizable if it identifies a defensible nontransfer region or irreducible distortion for a class; “our loop is not identical to a reactor” is not enough.

### CP04 — Local transport descriptors and their thermal consequence

**Links:** H03, optional extension of H02/H04. **Gap type:** physical knowledge and validation/data; method development only if separately justified.

**Narrow question and falsifiable hypothesis.** In a specified geometry/regime, does a well-defined counterflow/exchange descriptor explain a controlled regional thermal consequence beyond what bulk circulation and source/sink conditions explain? Hypothesis: a reproducible local descriptor improves out-of-case explanation/prediction of a declared heat-rate or temperature asymmetry after confounders and reference uncertainty are retained. It is not assumed that recirculation always enhances heat transfer.

**Strongest existing result and proposed advance.** S20 already predicts recirculation in a conceptual internally heated loop; S19/S29 provide local numerical structures and thermal comparisons; S37/S46/S60 contribute experimental diagnostic precedents. The proposed advance would be a qualified descriptor–thermal-effect relationship, applicability limit or discriminating evidence, not the existence of a reverse-flow contour or a new reconstruction network.

**Understanding and domain.** Separate net circulation from persistent reverse-flow extent, intermittency and local exchange. Establish which descriptor has a physical relation to a chosen thermal consequence, under which source/geometry/flow conditions. Define coordinate/frame, threshold, averaging and wall/enthalpy references before comparing cases.

**Strongest novelty counterargument.** The apparent descriptor relation may be known mixed-convection/development physics or a proxy for power/throughflow. The sparse measurements may not identify it at all. Thermal agreement can be achieved by incompatible local structures; interpreting inferred extent as measured would invalidate the claim.

**Required work and assessment.** Obtain qualified fields or direct appropriate measurements; check descriptor-specific mesh/time/model and observation uncertainty. Design controlled source/sink/flow or geometry comparisons where feasible, retaining energy conservation and competing mechanisms. Compare bulk-only, conventional local heat-transfer/transport measures and simple descriptor alternatives before learned reconstruction. Hold out whole cases/regimes, not shuffled field points. A CFD ablation establishes a conditional model effect; physical causality needs independent discriminating evidence and an experimental argument.

**Feasibility:** without qualified CFD/local observations, quantitative local extent cannot be validated; only thermal predictions or carefully proved bounds remain. Limited CFD supports a case-specific hypothesis and descriptor tests, not broad physical validation. Adequate qualified CFD plus independent target-relevant measurements could support a spatial study, but direct extent validation still requires adequate local evidence. No future field campaign is assumed.

**Fallback versus dissertation threshold.** Useful fallback: document the inference limit and exclude unsupported field claims while finishing CP01/CP02. Sufficient research: a generalizable, qualified physical descriptor/consequence or impossibility result beyond known scalar nonuniqueness, with relevant independent evidence. **Rejection:** descriptors fail convergence, lose explanatory value after confounder control, or do not generalize across declared cases. A negative result is valuable if it identifies the missing information or invalid descriptor class quantitatively; an unavailable CFD file alone is not a scientific result.

## 7. What should be recommended now, and what could change it?

| Package | Present evidence strength | Principal missing condition | Provisional role |
|---|---|---|---|
| CP01 / H01 | Strong prior methods and clear physical/evidence problem; additional theorem/result not established | Exact model class, actual input/observation anchors and advance beyond S23/S68/S70/S77 | First feasibility/theory gate; avoid generic identifiability claim |
| CP02 / H02 | Strong physical mechanism precedents; useful candidate consequence tied to project goals | Nontrivial adequacy criterion, target/tolerance, independent assessment opportunity and relevant error-theory check | Partner to CP01; preferred physical-understanding component if gate passes |
| CP03 / H04 | Strong similarity priors; motivation is conditional | Selected reactor circuit/QoI and target-relevant reference/bound | Optional third aim after target choice, not present quantitative transfer promise |
| CP04 / H03 | Local phenomena exist; present inference/validation support inadequate | Qualified spatial/reference and discriminating causal evidence | Resource-gated extension; not a core dependency |

**Reasoned recommendation, not forced confidence.** CP01 supplies an honest information contract; CP02 asks a physical-understanding question whose answer matters to model choice. Together they fit the supplied goals, permit progress without CFD and have clear failure conditions. That makes them a better initial commitment of analysis than a full local-flow reconstruction or an unspecified “MSR digital twin.” It does **not** prove novelty or that Aims 1–2 already constitute a dissertation.

The combined research question could be: **For a stated conservative thermal/transport class, when can sparse, uncertain observations distinguish omitted storage/transport physics strongly enough to support a specified prediction—and when are models observationally similar but predictively different?** This connects physical mechanism, identifiability and assessment. It is still a question to refine against prior theory, not an announced field gap. SYN-C10.

### Three gates before committing a direction

1. **Prediction and information contract.** Choose an assessable thermal/duty/response target, horizon and tolerance; record actual net-energy support, fluid identity, sensor semantics/dependence and admissible case roles. A temperature margin cannot be called operationally adequate before its limit and evidence are defined.
2. **Additional-result gate.** Attempt a tightly scoped model-class derivation/counterexample for CP01 and an omitted-physics relation for CP02. Compare directly with S77/S70/S59/S66 and the relevant general originals. If the result is an immediate specialization or only a workflow, narrow/change the aim before a large implementation. S78 is now acquired/read;its baseline should be used only if the declared linear port/input-response contract is supportable.
3. **Independent-consequence gate.** Establish which conditions could test the result without being reused for calibration/selection. Until approved evidence exists, label synthetic verification and conditional reference tests accurately. If independent physical assessment is unavailable, a sufficiently nontrivial theorem/general counterexample could remain scientific research; a collection of unvalidated fits cannot substitute for it.

No-CFD does not mean no evidence or no physics. It changes which quantities are assessable and places more weight on tractable theory, observation-supported targets, conservation and honest limits. Conversely, adding CFD does not resolve an undefined target, unknown input scale or dependent validation channel.

## 8. What acquisition/extraction should happen next?

| Rank / gap | Exact next item or action | Why decisive | Fallback / status |
|---|---|---|---|
| P0 project | Selected decision/QoI/horizon/tolerance and small configuration/measurement metadata | Defines domain, estimand and whether a proposed result has consequence | Not a request for bulk operating data; missing metadata narrows claims |
| P0 theory/extraction | Select the exact conservative model class; deepen relevant S59/S66 proof/appendix and the structural/realization original cited by S77 if extending it | Current scoped extraction does not certify a new general theorem or dispersion solver | No upload requested before identifying the decisive original and checking access |
| Resolved S78 | Corrected published original now uploaded/read; DOI **10.1002/jnm.2296** | Passive identification is strong prior;its linear/multiport assumptions and equivalent-state meaning are now inspected | Do not request again. Further proofs/code would be needed only for an exact generalization or reproduction |
| P1 conditional extraction, S23 | Algorithm supplement if reproducing the profile implementation; main DOI 10.1093/bioinformatics/btp358 | Optimizer/algorithm details cannot be reconstructed from general description | Ordinary declared optimization/profile baseline can proceed without faithful-reproduction claim |
| P1 optional version checks | Final S71 10.1137/24M1649344; S75 10.1016/j.cma.2014.08.023; S76 10.1016/j.cma.2023.116182 | Resolve exact manuscript/final equation or wording differences when implementation depends on them | Inspected manuscript framework sufficient for provisional synthesis; equivalence unverified |
| P1/P2 conditional branch | Qualified local fields/reference metadata or a named target circuit | Required for CP04 extent/causal claim or CP03 quantitative transfer | No new instruments/CFD assumed; keep CP01/CP02 core |

No S20/S19/S72/S74 re-upload is needed. S77 is now acquired and read. No unavailable paper is used to certify a methodological gap. The remaining optional acquisitions do not stop present literature synthesis; they stop specific stronger implementation or novelty claims.

## 9. Claim audit and handoff

Retain as supported: physical source/solid pathways can matter within specified regimes; reduced circulation and observed/local-temperature information can differ; observability and physical-parameter recovery depend on a declared contract; target-oriented calibration/design and embedded discrepancy already exist; similarity and uncertainty must be QoI/circuit-specific.

Reject or narrow: “RC/network learning is new,” “wall inertia always stabilizes,” “this high-Pr loop represents MSRs,” “a narrow posterior proves physical parameters,” “thermal agreement validates recirculation,” and “a newer model form must be better.” No strongest-prior comparison here establishes novelty by omission.

The ledger adds S77 primary-source claims, the historical abstract-only S78-C01 plus new original-source S78-C02–C09, SYN-C01–SYN-C10 cross-source interpretations and SYN-D01/SYN-D02 elementary analytical checks. They are tagged by evidence type and preserve older claims unchanged. `Contribution_Packages_2026-10-21.json` records hypotheses, rejection conditions and resource gates. The research state and current checkpoint point here; v1.0 reviews remain the comprehensive bases with a dated synthesis addendum. All 62 original questions persist, with package links added rather than renumbered or declared scientifically closed.

**Unresolved conclusion:** there is a credible and feasible research problem at the intersection of supported predictions and retained physics. There is not yet enough evidence to certify its precise novelty, choose the final model class or guarantee a dissertation result. The next advance comes from narrowing and testing that statement, not expanding an undirected reading list.
