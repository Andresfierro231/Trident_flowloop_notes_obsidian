# B. Why study natural-circulation loops, and what can TRIDENT contribute?

> **Critical-synthesis addendum, 21 October 2026:** see [cross-source synthesis](Critical_Cross_Source_Synthesis_2026-10-21.md). Newly inspected S77 strengthens the prior-work challenge to basic thermal identifiability/minimum-sensor claims. CP01/CP02 are the provisional no-CFD core; no precise novelty is certified. S78 corrected original is now scoped-read;the earlier conditional request is closed. Its linear multiport response assumptions limit transfer to the loop. The v1.0 comprehensive body below is retained with its original IDs.

**Comprehensive first review draft, v1.0 — 21 October 2026.** Proposal and dissertation motivation, linked to review A's methods, equations and comparison plan. This continues the original `Markdown collé.md` brief and its 62 questions. Stable source, claim and hypothesis IDs are preserved. The review distinguishes established evidence, conditional transfer and proposed research; it does not certify a vacant literature gap, select a final thesis direction or claim reactor-scale validation.

Primary-source locators accompany consequential claims. “PDF6/349” means PDF page 6/printed 349. Available manuscripts are identified as such; their pages are not journal pagination. Historical reports, modern studies and official measurement guidance have purpose-scoped reading limits in their dossiers. This is a comprehensive first synthesis of the acquired corpus, not an exhaustive history of thermosyphons or a systematic proof of novelty. The concluding audit, candidate aims, original-question matrix and ranked gaps state what remains unresolved.

Bibliographic identity, publication/version and reading depth: [source index](Review_Source_Index.md); exact claim records: [claim ledger](Claim_to_Evidence.md). These preserve the reading-depth distinctions needed to audit this synthesis.

## 1. What scientific and engineering problem makes these loops worth studying?

Natural circulation couples heat addition, density distribution, buoyant head, resistance and heat rejection without requiring the circulation to be prescribed by a pump. Thermal storage in fluid and structures, source location and heat losses add time scales and feedback. A test loop makes parts of that coupled problem accessible to controlled observation. Its scientific value does not depend on being a miniature replica of an entire reactor.

The engineering question is narrower than whether a simulation reproduces a temperature trace. Can a specified heat path remove a required load? Which wall/fluid temperatures approach a stated limit? How does a source or sink change affect the response? Is a simpler model adequate for that decision, and what uncertainty remains? Answers require both a credible physical model and evidence that actually tests the prediction of interest.

For liquid-fuel MSRs, the literature identifies temperature distribution and bulk/potentially local velocity as figures of merit linked to structures, transport and feedback. Brown et al.'s preliminary expert assessment makes those connections explicitly (S13, §V.A/Table II, PDF17–19; §V.B–D, PDF20–25; S13-C01–C03). That exercise does not formally rank all research priorities or quantify a universal uncertainty budget (S13-C04). A fundamental-safety-function PIRT also exists, but its liquid-fuel accident/spill scope cannot be adopted wholesale as a TRIDENT research-gap list (S12, Table1/PDF16/5; summary PDF65–67; M-S12-01).

TRIDENT can contribute by determining which economical physical descriptions and sparse observations support useful thermal predictions, when additional physics or evidence is necessary, and which quantities cannot be inferred reliably. That is a methodological and physical-understanding problem. Dashboard integration is a useful delivery route, but not by itself the scientific advance.

## 2. What does the history show about the purposes of natural-circulation loops?

### 2.1 A reactor-design tradeoff, not a universal reactor lineage

A 1958 ORNL natural-convection reactor concept explicitly considers replacing circulation pumps to improve reliability and maintenance while accepting increased fuel-salt inventory in risers and exchanger (S40, Romie–Kinyon, ORNL-CF-58-2-46, Introduction PDF4/printed1; S40-C01). Its 60 MW thermal rating is a design calculation, not an operated plant (abstract PDF3/ii; S40-C02). This is useful historical motivation because it connects a transport mechanism to a concrete engineering tradeoff rather than merely declaring natural circulation desirable.

It does not establish that all MSRs were designed for natural primary circulation. The 1965 MSRE design report describes a fuel pump, coolant pump and air radiator (S42, ORNL-TM-728, §2.4/PDF41/printed9 and§2.4.2/PDF44/12; S42-C01). Its design objectives include practical operation and sustained salt/material performance (§1/PDF35–38/3–6; S42-C02). A later 1969 natural-circulation operating test remains an original-report lead in this corpus; its exact power, duration and conditions have not been verified and are not repeated here. Pumped normal operation and a possible off-normal circulation test are different facts.

### 2.2 Circulating salt as an exposure environment

The 1967 ORR convection-loop report concerns fueled fluoride salt in contact with graphite and Hastelloy N under irradiation. Natural circulation enables an in-pile materials/fuel exposure mission (S41, ORNL-TM-1960, abstract/§1, PDF9/printed1; S41-C01). The operated loops experienced primary-system failures; the report qualifies aspects of proposed thermal-stress explanations rather than presenting every mechanism as proven (discussion PDF37–40/29–32; S41-C02).

This history gives a distinct motivation for loops: they provide an environment for salt handling, instrumentation, compatibility and structural behavior. An unirradiated oil/glycol or nitrate loop cannot claim that irradiation evidence, but it can still study a relevant thermal mechanism. The test purpose determines what must be represented.

### 2.3 A model system for transport and instability

Keller 1966 and Welander 1967 develop different idealized loop descriptions of thermal transport and oscillation. Keller's exact periodic example has a particular point-exchange law and zero momentum inertia, while Welander emphasizes advected thermal disturbances and delayed feedback under cross-sectional mixing and linear resistance (S54, §5/PDF4–6/602–604; S55, §§2–4/PDF4–10/20–26; S54-C01–C04/S55-C01–C04). Welander's earlier 1965 report is acknowledged in this lineage; publication dates alone do not establish discovery priority.

These works matter to TRIDENT because a few-state model can capture a mechanism only if it retains the states, phase and source law that produce it. A passive cooldown network, an inertialess steady circulation law and an advective stability model are not interchangeable. Later scaling, conjugate-wall, transition-friction and stochastic loop studies make that point more specific, rather than leaving “nonlinear natural circulation” an unexplored topic (S56/S57/S59/S65/S66; methods review A).

### 2.4 Scaled experiments and model assessment

Bardet–Peterson 2008 explicitly develops reduced-temperature/size/power experiments for selected liquid-salt/helium convection phenomena, including fluid/structure similarity and unavoidable distortion (S64, §IV.A/Eqs2–10, PDF5–6/348–349; TableV/PDF11/354). Modern salt and high-Pr surrogate facilities add detailed thermal/flow diagnostics and code comparisons. Several publications can share one apparatus, dataset or calibration chain; their count is not the count of independent demonstrations.

S50's molten-salt loop motivation includes high-temperature reactor, solar, instrumentation and operating/material experience (§1, PDF1–2/513–514; S50-C01). S52's lead–bismuth loop also serves thermal, materials and instrumentation purposes (§§1–3, PDF1–4/308–311; S52-C01). The latter is a methodological/physical analogy, not salt-property equivalence. A loop may therefore be valuable without being an MSR-specific passive safety demonstration.

### 2.5 What the MSRE heat-balance history actually motivates

The original Gabbard 1970 report separates power metrology, primary-exchanger design estimates and air-radiator performance. Revised physical properties resolved the reported primary-exchanger overestimate, while other discrepancies and metrology checks remained distinct (S47, ORNL-TM-3002, conclusionsPDF31–32/27–28; S47-C01–C03). Installed thermocouple and venturi checks also illustrate shared measurement chains and imperfect independent cross-checks (Table I/PDF9/5; calibrationdiscussion PDF9–13/5–9; S47-C04).

This original does not substantiate the raw-note claim of a generic “25% MSRE heat-balance discrepancy.” That claim is excluded. The defensible motivation is that properties, installed instrumentation and control-volume accounting can materially change inferred power and design interpretation. It argues for metrology and model adequacy before attributing residuals to new heat-transfer physics. It supplies no TRIDENT error magnitude.

## 3. Which different loop purposes require different evidence?

| Loop purpose | Scientific or engineering question | Evidence it can provide | Representation limit |
|---|---|---|---|
| Mechanism/separate-effect experiment | How do buoyancy, development, walls or local geometry alter response? | Controlled trends, discriminating observations, qualified closure tests | May intentionally omit whole-system similarity |
| Materials/salt exposure loop | What happens to salt/materials/instrumentation during circulation? | Compatibility, handling and structural observations | Nonirradiated surrogate tests do not reproduce radiation/chemistry |
| Code/model assessment facility | Does a specified model predict measured outcomes under declared conditions? | Numerical/physical assessment with uncertainty and independent cases | Parameter tuning and verification are not final predictive validation |
| Integral or scaled circuit experiment | Does a reduced system reproduce selected coupled behavior? | Evidence under quantified geometric/source/fluid/solid distortion | Must name target circuit and mission; not automatically a reactor replica |
| Passive heat-removal demonstration | Can a particular path reject a specified load/history within limits? | Circuit-specific duty, response and supported temperatures/flow | Required heat history, boundary conditions and failure criterion must be specified |
| Inference/reduction testbed | What can sparse observations distinguish, and how much model complexity is useful? | Identifiability, adequacy, uncertainty and experiment-design evidence | A software workflow alone is not new theory or physical understanding |

These categories can overlap. A project should state its primary purpose and distinguish additional useful evidence. This avoids two opposite mistakes: demanding full reactor equivalence before any loop result is useful, and treating any salt/surrogate loop as quantitative MSR validation.

## 4. Which MSR engineering decisions make our QoIs useful?

The decision must precede a numerical accuracy requirement. The following map is a synthesis of the inspected engineering and loop literature, not a statement that TRIDENT already measures or predicts every output.

| Engineering decision | Relevant QoIs | Physical reason and primary evidence | TRIDENT scope and condition |
|---|---|---|---|
| Can the chosen heat path reject the assigned load? | Net heat deposition, exchanger duty, ambient loss, stored energy, required circulation | Source–sink transport and heat removal; S13 §V.B–D/PDF20–25; S50/S51/S52 | Assessable facility duty/thermal response if energy metrology is supported; not reactor decay-heat certification |
| Are structures and fluid within an assigned thermal limit? | Particular wall/fluid temperatures; justified minima/maxima; uncertainty of margin | Structures and temperature-distribution consequences; S13 Table II/PDF17–19 | Sensor/regional predictions first; global extrema need spatial evidence |
| Is adequate circulation sustained after a change? | Signed circulation, response time, possible reversal or low-flow bound | Buoyant head, form/friction loss and transport; S13 §V.D/PDF23–25; S55/S57 | Flow claims depend on reference capability; thermal-balance estimates are dependent evidence |
| Which source/sink placement or resistance is acceptable? | Duty–flow–temperature tradeoff, hot/cold distribution, inventory | S40 pump/inventory tradeoff; S65 source/geometry stability, PDF8–10 | Conditional trends for a specified circuit; matching total power is insufficient |
| What follows a heater/cooling change? | Overshoot, settling, thermal/hydraulic time scales, time to assigned limit | Advection, fluid/solid storage and source partition; S50/S52/S65/S66 | Evaluate selected facility transitions; electrical heater-off is not nuclear shutdown |
| How should preheating/freeze protection be reasoned about? | Sensible-temperature margin above qualified liquidus, cooldown rate, time to cold limit | S51 temperature-threshold reliability; S38 solidification evidence | Predicting a sensible-heat margin differs from phase-change/blockage modeling |
| Does local flow alter a consequential thermal quantity? | Defined reverse-flow/exchange descriptor, wall flux, local or regional thermal consequence | S20 local CFD; S37/S46/S60 diagnostics | Conditional extension; no measured local recirculation in TRIDENT |
| Is more model or measurement complexity worthwhile? | Supported predictions, holdout error, uncertainty usefulness, identifiable combinations | S23/S67–S76 and official S32 measurement model | A feasible core even without CFD; requires a result beyond tool integration |

The thermal limits in the project facts concern allowable heat flux and material/sensor temperatures, not a default boiling critical-heat-flux problem. A single-phase model may address a qualified sensible-temperature margin. Resolving solidification, latent heat, evolving blockage, chemistry, gas/void transport or multiphase flow requires additional models and evidence. Such extensions should not be hidden inside the word “operational.”

## 5. Which MSR is represented: liquid-fuel primary, salt-cooled solid fuel or another circuit?

A liquid-fuel primary system has heat generated in moving salt and potentially in structures, plus couplings involving composition and delayed-neutron precursors. A solid-fuel salt-cooled reactor receives heat through fuel/solid structures. A secondary transport circuit receives heat through an exchanger. A passive residual-removal or drain-system path has its own topology, thermal storage, source history and mission. They need not share model assumptions or decision tolerances.

S13's detailed focus is liquid-fuel primary-system modeling; it does not fully analyze auxiliary and secondary systems (§I.B/PDF6; S13-C05). It therefore supports a primary-system motivation but cannot single-handedly justify every passive/secondary mission. S51 provides a more specific natural-circulation passive-cooling reliability precedent, with an identified DRACS prototype and high/low thermal failure criteria (§§1–2/PDF1–2/127–128; §4.1/PDF4/130; S51-C01–C03). Its model-choice uncertainty treatment is already prior art, and its numerical probabilities carry dossier-specific caveats.

S20 models a conceptual D-shaped internally heated salt/graphite arrangement to inform future CNL experiments. It is not based on a commercial design; it uses a fixed graphite-temperature sink, steady first-order RANS and substitute properties rather than exactly the original MSRE salt (§2/PDF3–4; S20-C01–C04). It supplies a source/path/geometry mechanism comparison, not direct quantitative transfer to an externally heated ACU/VCU loop. Its appendix separates a conventional boundary-heated chloride loop from a microwave-heated surrogate proof-of-concept (AppendixA/PDF8–9; S20-C08). Those were development plans when written, not current TRIDENT resources.

S29 similarly illustrates relevant electrically driven loss-of-sink and reduced-power protocols, but such a protocol does not reproduce nuclear decay-heat history simply because it is called decay-heat removal (§2.4/PDF9–10). A source analogy can be useful when the heat history is deliberately specified; it should remain an analogy until the relevant differences are bounded.

The project has not selected one reactor architecture/branch as its quantitative target. That is a consequential open fact. A defensible first proposal can motivate the importance of heat transport across these circuits while claiming a narrower facility/model contribution. It should not state that a particular glycol or nitrate experiment represents all MSRs.

## 6. What similarity is necessary, and what can remain distorted?

### 6.1 Match the phenomenon and output, not just a fluid label

Re and Pr compare inertia/viscosity and momentum/thermal diffusion, but geometry, source/sink distribution, buoyancy, development lengths and solid response also matter. S56 explicitly includes fluid, solid and interface similarity (Eqs1–16, PDF2–3/412–413; S56-C01/C02). S64 distinguishes interface and solid-transient matching and shows that examples matching major groups can retain property-variation distortion (Eq8–10, PDF6/349; TableV/PDF11/354; S64-C01–C04).

Use consistent definitions and scales for Re, Pr, buoyancy/Richardson/Rayleigh or Froude measures, exchange/Stanton/Biot and solid Fourier/time ratios. Different papers define some groups reciprocally or use different reference lengths; matching a name is not matching a number. Simultaneous matching can impose incompatible length, velocity, power, property and wall-time requirements with real materials. Whether a distortion is tolerable depends on the target and horizon, not solely on a small dimensionless mismatch.

| Transfer issue | Why it can change a prediction | Required qualification |
|---|---|---|
| Geometry, elevation, hydraulic diameter and local restrictions | Buoyant head, resistance, development and local mixing change | Full flow path and component loss/area definitions |
| Fluid/property envelope | Density and viscosity affect circulation; cp/k affect transport and storage | Qualified property data and temperature dependence, not one matching state |
| Source deposition | Wall, immersed and distributed fluid heating have different storage/gradient paths | Spatial/time distribution and solid heating share |
| Sink and ambient losses | External losses change temperatures and buoyant head | Insulation/contact/radiation and heat-sink histories |
| Solid/fluid time scales | A steady match may lose overshoot or stability | Capacity/conductivity/diffusivity and initial-state similarity |
| Observation scale and location | Sensors can report different averages even with similar global transport | Point/wall/bulk definitions and response/calibration |
| Nuclear/material/phase physics | Surrogate may omit feedback, chemistry, irradiation or solidification | Explicitly exclude, model separately, or obtain additional evidence |

### 6.2 Modern similarity work is a challenger, not a blank space

S74 performs a modern H2TS comparison across three oils and several reference designs. Its global equations assume simplified steady 1D constant-property behavior, no external loss and negligible leg-wall inertia (§4.1/PDF8; S74-C01/C02). Its near-equal Nu values result from using the same correlation at matched Re/Pr (Table 4.10/PDF17; S74-C05). That is useful internal consistency but not independent demonstration of salt/oil local heat-transfer equivalence or a probabilistic output-error bound. The dossier also flags normalization/hydraulic-diameter issues requiring clarification before literal implementation.

S29 supplies a concrete separation between fluid selection and achieved test similarity. The oil is a candidate surrogate, but Figure 22 and the conclusion do not establish its tested Pr as salt matched; higher power is proposed to reach the stated range (PDF30–31; S29-C08). Loss-inclusive CFD improves selected thermal comparisons while circulation and response discrepancies remain material (PDF21–23; S29-C06). Thus a “surrogate fluid” label does not establish that a particular operating dataset reproduces a target reactor regime.

### 6.3 Similarity and sensitivity complement rather than replace one another

S76's synthetic example shows that a validation experiment matching initial Re can fail to challenge the approximation that matters to the target (Figure 5/PDF19–20; S76-C05). Its remedy matches model response sensitivities, but the article explicitly does not propagate model errors to the target or guarantee a correct validity decision (PDF12/20; S76-C02/C08). Physical similarity identifies potentially relevant mechanisms; target sensitivity helps determine which differences matter within a model. Both still require credible source/observation assumptions and evidence testing the important uncertainties.

For TRIDENT, classify each claim as **direct facility prediction**, **conditional quantitative scaling**, **mechanism analogy**, or **incompatibility**. A good facility model remains useful if reactor-scale quantitative transfer is unsupported. Conversely, a group-matched calculation does not independently validate an unobserved local field.

## 7. What does the strongest prior work already accomplish?

### 7.1 Physical reduction, walls and nonlinear dynamics

Conjugate 1D models, losses, source partition, wall storage, transport phase and stability are established topics (S50/S52/S54/S55/S57/S59/S65/S66; original locators in review A). S59's restricted Fourier reduction is an exact asymptotic result under particular forcing/transport assumptions; S18 already compares a conjugate Fourier model with CFD. S30/S62 add stochastic transient/event behavior and S63 finite-disturbance dynamics. A thesis cannot claim that few-state modeling, wall thermal inertia, nonlinear response or stochastic natural circulation has been ignored.

The useful unanswered project question is which of those physical distinctions matter for the actual measurable TRIDENT predictions, under its inputs, regime and tolerances. That is not answered by citing that the mechanism exists or by adding every available physical state.

### 7.2 Thermal-network learning and identification

S23 establishes profile-likelihood tools; S67/S68 apply identification, observation selection and model reduction to thermal networks; S69/S70 show why predictive fit and physical material interpretation can diverge. S26 learns thermal structure within a specified candidate family and exposes posterior/recovery limitations. Their building settings permit conditional methodological transfer; they do not validate a circulating-salt/glycol model. Nonetheless they are strong enough prior methods to invalidate novelty based only on applying an RC fit, profile likelihood, hidden nodes or Bayesian topology discovery.

A precise advance would need to characterize a specified conservative thermal/advective model class or an assessable QoI under consequential input/observation uncertainty, and demonstrate a consequence beyond better training fit. Model nomenclature alone does not supply that result.

### 7.3 Goal-oriented calibration, design and predictive credibility

S71 already computes nonlinear target-information experimental designs with separate observation and prediction maps (Eqs10–14/PDF5; S71-C01–C04). S72 already calibrates toward a goal-weighted discrepancy criterion, but does not beat ordinary MLE on its reported model-only validation metric and cannot directly propagate observable discrepancy to a different unobserved target (Table8/PDF24; §2.5/PDF7; S72-C02/C05).

S75 addresses the latter issue by embedding inadequacy in a physical closure so it propagates to observations and targets (Eq8a–c/PDF12; S75-C01). Its predictive assessment asks whether target-sensitive features are constrained/tested and whether the embedded-model regime is supported (§3.3/PDF19–23; S75-C02–C04). It does not offer a universal guarantee or remove unknown omitted phenomena. S76 subsequently selects validation scenarios/observables by influence-matrix matching (Eqs14–17/PDF13–15), while retaining certainty assumptions on controls/sensors and explicitly leaving target-error propagation outside scope (S76-C01/C03/C08).

These papers make the contribution challenge more demanding and more useful: a TRIDENT result must identify a concrete limitation or extension of established prediction-oriented methods, not merely introduce the idea of predicting what matters. Possible increments concern conservative transport, nuisance uncertainty, attainable observation support and independently assessed adequacy. Whether a particular increment is new remains to be established.

### 7.4 Modern loop experiments, CFD and indirect flow

S19 and S29 already connect thermal observations, circulation estimates and CFD. S19 lacks direct flow validation and its reported 5.5% does not mean measured flow accuracy (Table7/PDF8; S19-C01–C04). S29 also uses indirect energy-balance flow, and its numerical/model selection is not a locked independent predictive assessment (S29-C02/C04/C10). S20 already investigates internally heated local recirculation numerically but explicitly leaves experimental assessment to future work (S20-C06/C07).

These limitations identify evidence that our study should handle honestly. They do not prove that every existing model is inadequate or that all such limitations can be resolved with our sparse observations. They also prevent the proposed local-flow extension from claiming novelty merely for showing recirculation contours.

## 8. What local-flow question is feasible without promising unsupported reconstruction?

The original brief distinguishes extent and thermal effect. Extent could mean signed reverse-flow volume/area fraction, separation/reattachment distance or an exchange/transport measure. In 3D buoyant flow it requires a direction/frame, threshold and averaging convention; temporal intermittency can differ from a persistent recirculation region. A scalar net circulation estimate cannot determine these quantities.

Thermal effect is also more precise than “recirculation improves heat transfer.” It could mean a change in regional heat rate, wall flux, temperature asymmetry or an extreme under controlled source/sink conditions. A local HTC can be ill-conditioned when its chosen temperature difference approaches zero or changes sign. Alternative heat-rate/enthalpy or gradient measures may be more robust. Correlated changes in power, circulation and local contours do not establish causality.

| Evidence level | Feasible claim | Claim to withhold |
|---|---|---|
| No qualified CFD or local-flow measurement | Measured/regional thermal predictions; justified balance/response bounds; limits of inference | Experimentally validated recirculation extent, full velocity reconstruction or global extrema without additional support |
| A few qualified CFD cases | Conditional observation maps or local thermal corrections; tests of a defined descriptor under stated assumptions | Broad regime/geometry transfer or experimental local-flow validation |
| Adequate qualified spatial/reference campaign | Case/regime-out descriptor/reconstruction and controlled thermal-effect comparisons | Unmeasured physical truth merely because CFD agrees with bulk temperatures |

This ladder preserves a feasible core. Local-flow work is a gated extension of H03, not an implicit requirement that delays all proposal progress. No assumption is made about the timing, quality or volume of TRIDENT CFD. Ethan discrepancies remain outside this pass.

## 9. What proposal story follows from this evidence?

**Proposed problem statement.** MSR-relevant heat-transport decisions require useful predictions of duty, temperatures and response under uncertain operating inputs and incomplete observations. Natural-circulation and surrogate loops provide accessible experiments for selected coupled transport mechanisms, but source, geometry, property and fluid/solid differences limit transfer. Existing physical reduction, stochastic estimation and goal-oriented assessment methods offer powerful ingredients; the unresolved project challenge is to determine which conservative reduced descriptions and parameter combinations the available evidence supports, when omitted physics changes a declared prediction, and how uncertainty and applicability should be assessed independently.

**Proposed research question.** For a specified class of conservative low-order thermal/transport models and the actual ACU/VCU observation contract, which combinations of retained states, parameters and feasible experiments yield assessable thermal/duty/response predictions, and when can a simpler description be ruled out or retained? A follow-on transfer question asks which unavoidable distortions matter to a named circuit/QoI, rather than whether the loop “is an MSR.”

The minimum program can be useful without qualified CFD. It can establish an explicit model/measurement contract, characterize supported combinations and ambiguities, compare a simple and richer conservative model fairly, and challenge predictions under withheld conditions when approved evidence is available. If the necessary energy anchor or independent assessment cases are unavailable, narrow the claim and demonstrate the consequence rather than manufacture physical parameters. If qualified local fields arrive, they can extend the question with additional evidence rather than retroactively make the core valid.

Operational assistance should present scenario/horizon, input provenance, uncertainty, domain limits, stale/unavailable data and competing explanations. Those are proposed result-contract requirements, not claims about Ben Booth/NeutronOS's existing architecture. Dashboard development remains collaborative with them. Automatic control, unattended operation and phase-change protection are not established capabilities. A polished interface cannot strengthen the underlying validation evidence.

The candidate aims below retain H01–H04's identities and combine them into three provisional work packages. They are intended to make the proposal testable and feasible, not to imply that novelty or project acceptance has already been established.

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
