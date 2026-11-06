# Literature-review prompt for the TRIDENT PhD proposal

Tags: #project/trident #doc/specification #domain/documentation #domain/uncertainty #facility/shared

**Use:** Copy everything between BEGIN PROMPT and END PROMPT into a research-capable ChatGPT conversation. The context below is self-contained. Upload the optional documents listed after the prompt if available; ChatGPT cannot access local filesystem paths merely because they are mentioned. A checked starting bibliography is supplied separately in `SEED_LITERATURE.md`; upload that file too. This is a request to perform a critical review, not a completed review or a claim of novelty.

---

## BEGIN PROMPT

Act as a critical research collaborator helping me develop a defensible PhD research proposal in thermal-hydraulic reduced-order modeling, experiment-informed physical identification, and uncertainty quantification. We aim to craft the proposal over the next seven days. I need a decision-oriented literature review: why the problem matters, what is already established, which approaches are worth testing, what data they require, and where a credible methodological contribution remains possible.

Do not merely summarize papers or validate my preferred approach. Find the strongest prior work that could invalidate a novelty claim, explain limitations of my proposed methods, and recommend a feasible minimum contribution with alternatives if data or CFD arrive late. Clearly distinguish established findings, your synthesis, hypotheses, and unresolved evidence.

### 1. Project context and approved direction

We are developing a fast, interpretable, physics-based reduced-order model (ROM) and, more importantly, a reproducible CFD–experiment framework for selecting retained physics, constructing reduced representations/closures, learning supported physical parameters, and assessing predictions and applicability. “ROM” describes reduced representation; “surrogate” describes a predictive replacement role. Do not assume these are mutually exclusive or that explicit physics alone makes a model novel.

Applications are the TRIDENT ACU and VCU thermal-hydraulic loops, with distinct configurations and evidence. The intended relevance is to molten-salt-reactor (MSR) heat transport and operational decisions. Experimental surrogate-fluid loops do not automatically establish molten-salt or reactor-scale applicability. Do not invent facility dimensions, fluid compositions, sensor layouts, regimes or accepted datasets. Request missing specifics in an evidence checklist while continuing work that does not require them.

The adopted development stages are:

1. **Steady performance and operating margins:** heat-removal duty, losses and energy closure, overall circulation magnitude/direction, relevant fluid/wall minimum and maximum temperatures and operating margins.
2. **Transitions between operating conditions:** temperature/duty/flow responses, thermal and hydraulic time scales, settling and time-dependent margins under changes in heating/cooling.
3. **Operational assistance:** what-if analysis, startup/shutdown and freeze-protection guidance, and an operator-facing model/data dashboard. All dashboard work must be collaborative with Ben Booth and NeutronOS. Their architecture, interfaces and commitments are not assumed known. Interface development can proceed alongside scientific work; automatic control and unattended operation are not established capabilities.

**Uncertainty estimation and propagation are central in every stage**, including measurement, parameters, model reduction/form, CFD reference, numerical solution, initial states, and prediction-to-decision margins.

We distinguish **overall loop circulation** from **local recirculation**. For local recirculation, **its spatial extent and its effect on heat transfer are useful targets**. We want to determine how much can be predicted with available information, rather than promise full velocity reconstruction. There are no direct local-recirculation measurements in the loop. Ethan's thesis on the TAMU loop will be uploaded later; its findings must be reviewed for applicability before informing Trident work. Trident CFD is pending. Do not claim to have read the thesis or assume TAMU physics/coefficients transfer to ACU/VCU. Bulk thermal agreement does not directly validate a local flow structure.

### 2. Current modeling and experimental position

Our physical approach distinguishes fluid, pipe and insulation states and separates convection, conduction, radiation, contacts, source deposition and losses where supported. A separate reduced regional model may combine participating fluid/solid storage and effective coupling. Compare these model families without silently equating their states or interpreting effective coefficients as material properties.

A historical local wall-response calculation supplied measured fluid-temperature and ambient histories to a radial pipe/insulation model. It showed substantial wall-temperature discrepancies and limited benefit from physical parameter fitting. This is motivation to examine boundary/observation/model inadequacy, not proof of a specific missing mechanism. It was conditional on measured later fluid inputs and was not an autonomous whole-loop prediction. Later diagnostic developments exist, but no validated facility parameter set or complete predictive uncertainty model is assumed.

All new experimental data we can expect must be requested through **Dr. Nick Luciano's experimental plan** and agreed with him. The source package has Phase 0 checkout followed by Phases 1–4:

- **P0:** configuration, measurement and instrument checkout.
- **P1:** ambient/equilibrium baseline, noise, drift, covariance and uncertainty qualification.
- **P2:** controlled warm/cold passive relaxation, including a mixed-tank two-fill initial-condition procedure and withheld runs; reduced regional response/settling analysis.
- **P3:** low-duty steady heat-loss/heat-gain measurements and model assessment.
- **P4:** an operating duty/temperature matrix, transitions and flow-related reduction.

These descriptions are summaries, not substitutes for the actual phase documents. If those documents are unavailable, mark exact protocol/section claims as unverified.

We are considering an addition: hold at an accepted steady state with **measured net power**, then record shutdown or a controlled input change. For a single effective state,

C dT/dt = Q_net − G(T − T_a),

so steady known power can constrain G, and the passive time constant τ = C/G can then constrain C. Steadiness without measured duty does not fix an absolute scale. Passive-only temperature histories cannot independently fix both free scales. Trusted fixed inventory/capacity is another valid anchor. A distributed network may remain non-identifiable after a total-scale anchor. Compare these routes without dismissing Nick's plan or assuming the proposed addition is agreed or performed.

Additional instruments, flow visualization, repeats or new excitation are **requests to negotiate**, not available resources. Flow-reference capability differs by facility; do not invent a direct VCU flow measurement or treat a shared-input heat-balance estimate as independent truth. Sensor extrema differ from unmeasured spatial extrema. Existing ACU operating-data processing is held; this review does not authorize processing or experiments.

### 3. Search, verification and evidence rules

Search foundational work and the latest accessible work through the actual search date; report that date and your search coverage. Use peer-reviewed primary research, authoritative laboratory reports, original theses and official metrology guidance. Use reviews to map the field and follow their references. Include both positive results and failures/negative findings, especially model inadequacy, poor transfer and misleading parameter fits.

Verify title, authors, year, venue and DOI or persistent URL. Separate preprint from journal version and deduplicate. For consequential claims, read the relevant full-text section where accessible and cite its section, equation, table or figure identifier. Distinguish full-text reading, abstract-only inspection and unverified leads. Do not invent citations, reported errors, experiment conditions, speedups, validation, uncertainty coverage or claims of a literature gap. Label inaccessible evidence and seek an author manuscript rather than treating the abstract as full verification.

For each transferable result, identify fluid, geometry, boundary/source arrangement, regime/dimensionless range, properties, observable quantity, initial/operating conditions, training/assessment split, uncertainty treatment and known failure modes. Do not infer absence of prior work from a sparse search or call an application new methodology simply because it is applied to TRIDENT.

Use the attached seed bibliography as search entry points, not an exhaustive canon. In particular, inspect the assumptions of Pham et al.'s NEMO work (arXiv:2608.24833) before recommending it. Determine which unknowns enter linearly versus nonlinearly and whether that structure exists in our inverse problem. Search beyond the Wilcox group and include competing methods.

### 4. Priority questions to answer

Label findings **P0: needed for next week's proposal**, **P1: early research-method selection**, or **P2: later extension**. Begin with P0; do not wait for Ethan's thesis or Trident CFD to produce a useful first synthesis.

#### A. MSR need, impact and similarity — P0

A1. Which specific MSR heat-transport decisions require the outputs we propose: cooling duty, heat losses, circulation, extrema, freezing margin, response/settling or startup/shutdown predictions? Connect each output to a decision, mechanism and primary source.

A2. How do requirements differ for liquid-fueled reactors, salt-cooled solid-fuel systems, primary/secondary loops and test facilities? Avoid one generic MSR justification.

A3. What can natural-circulation/surrogate-fluid loops establish, and what requires property, geometric, source-distribution and dimensionless similarity? Compare Re, Pr, buoyancy measures, development lengths and conjugate thermal time scales where relevant. Explain which cannot all be matched simultaneously.

A4. How do distributed volumetric heating versus externally applied heating, different coolant properties and nonuniform losses affect applicability? Do not imply neutronics, chemistry or other excluded physics are modeled.

A5. Verify the raw-note claim of an approximately “25% MSRE heat-balance discrepancy”: what was compared, which denominator/time period, and what primary report supports it? If unverified or wrong, say so and do not repeat it as motivation. Separately determine whether critical heat flux is relevant to our intended single-phase scope or belongs to a different problem.

#### B. Quantities of interest and what can be observed — P0

B1. What is the minimum input/output contract for a useful steady ROM and its transition extension? Which inputs are measured operationally, inferred, prescribed, or only available from CFD during development?

B2. Which QoIs require field reconstruction rather than bulk temperatures? How should bulk, mixing-cup, area-average, centerline, point, wall and sensor-filtered temperatures be related? Can reduction preserve duty while losing local extrema?

B3. How can a model estimate unobserved hot/cold spots with honest uncertainty when experiments sample only a few locations? What supports a location claim versus a conservative bound?

B4. How do interpolation, observation operators, wall conduction and sensor dynamics alter comparisons with experiments? What data would distinguish sensor placement/calibration from missing physical transport?

B5. Which tolerances should be set from operating decisions versus statistical/measurement resolution? Identify evidence needed before specifying numerical acceptance thresholds; do not choose arbitrary values for us.

#### C. Competing physical and reduced model forms — P0/P1

C1. Compare lumped RC/thermal networks, segmented conjugate fluid-wall-insulation networks, reduced regional grey-box models, 1D natural-circulation models and quasi-1D/low-order spatial models. State equations, physical meanings and reduction assumptions.

C2. Which physical states and heat paths are necessary to preserve thermal storage, losses, duty, buoyancy and local temperature gradients? How are axial wall conduction, insulation/contact, radiation, supports and source deposition treated?

C3. When do steady momentum closure, transient inertia and advection need separate treatment? Explain circulation branch/reversal, low-flow limits and stability concerns where relevant; do not conflate passive temperature relaxation with full coupled hydrodynamics.

C4. How should natural/mixed/forced convection, entrance/development effects, curved connections, conjugate heat transfer and property variation inform closure choices? Distinguish established correlation limits from proposed corrections.

C5. Compare fixed material/correlation models, a small fitted grouped-parameter network, conventional projection ROMs, operator inference, learned closure hybrids, Gaussian-process surrogates and other credible data-driven baselines. Include a simple model that can defeat an overcomplicated proposed method.

C6. For each family, explain accessible data requirements, cost, interpretability, conservation/positivity/stability, uncertainty, extrapolation and falsifiable failure modes. Recommend a minimal comparison set rather than requiring every family to be implemented.

#### D. Reduction operators and closure construction — P0/P1

D1. What does the reduction actually do: aggregate control volumes, lump resistances/capacities, project fields, infer operators, learn spatial reconstruction, or close unresolved transport? Distinguish those contributions.

D2. Can CFD support observable-consistent bulk-to-local temperature and wall-flux maps, or development-conditioned heat-transfer closures that improve predictions beyond fixed averages? What information would those maps require at online inference time?

D3. How do goal-oriented/adjoint, balanced, POD/Galerkin, nonlinear/manifold, structure-preserving and data-driven methods select states to retain? Which are feasible with sparse experiment data and delayed CFD?

D4. Compare closure correction, state enrichment and explicit extra physics. What diagnostics decide that a closure is inadequate rather than merely poorly calibrated? How do we prevent a fitted coefficient absorbing wrong geometry or boundary conditions?

D5. Which methods preserve energy, dissipation, positive capacities and appropriate transport direction? Are passivity/port-Hamiltonian or related frameworks suitable for dissipative thermal-advection networks, and which assumptions prevent direct transfer from mechanical/Hamiltonian examples?

D6. How should we split cases for closure training, method selection and final unseen assessment to avoid leaking CFD snapshots or experimental targets? Compare leave-regime/geometry/case-out assessment with random time-point splits.

#### E. Local recirculation extent and heat-transfer effect — P0/P1

E1. Define useful descriptors of extent: reverse-flow volume/area fraction, separation/reattachment length, recirculating region size, signed local axial flow or exchange/transport measures. Which are robust in 3D, sensitive to averaging/frame/threshold, or ambiguous in buoyant curved flow? Distinguish persistent structures from temporal intermittency.

E2. How can the heat-transfer effect be quantified: changes in wall heat flux, local/region-integrated transfer, fluid/wall extrema, effective transport or temperature asymmetry? HTC definitions may become ill-conditioned when the driving temperature difference is small or changes sign; examine alternatives.

E3. What are valid counterfactual or controlled comparisons for attributing a heat-transfer change to recirculation rather than changed flow rate, geometry, boundary condition or thermal development? Correlation of two CFD outputs is not by itself attribution.

E4. Compare an effective closure, a two-zone exchange model, a local spatial correction and a richer velocity/temperature reconstruction. What is the simplest representation that can predict extent and thermal effect sufficiently for a declared QoI?

E5. What can sparse bulk/wall experiments constrain about thermal consequences, and what is structurally unobservable without local flow measurements? Can multiple distinct flow fields explain the same measured temperatures?

E6. Specify the Trident CFD dataset needed: fields/integrals, geometry/BCs, source placement, regime coverage, mesh/time/domain sensitivities, uncertainty and descriptors. Explain how we can test descriptor/reconstruction transfer on held-out CFD without claiming experimental local-flow validation.

E7. When Ethan's TAMU thesis arrives, what exact evidence should be extracted, and which applicability checks must precede use in Trident? Give a no-CFD/minimal-CFD/adequate-CFD feasibility ladder and a stopping criterion for claims that cannot be supported.

#### F. Parameter learning, identifiability and discrepancy — P0

F1. What are the structurally and practically identifiable parameter combinations for steady and passive/transient thermal networks with sparse temperature observations? Compare sensitivity rank, Fisher information, profile likelihood, posterior geometry and synthetic recovery.

F2. Derive the common G–C scale ambiguity, the conditions under which measured steady net power or fixed inventories break it, and the remaining ambiguities in multiregion networks. When is sequential steady-G then transient-C defensible versus a joint fit?

F3. How do uncertain initial insulation/structure temperatures, hidden fluid-wall splits, parameter variation and unknown residual heater/cooler duty confound capacity estimates? Compare approaches for treating those nuisance quantities.

F4. Compare deterministic constrained fits, regularization, Bayesian/hierarchical identification and model-discrepancy approaches. Which parameters can remain physical, and when does an effective correction lose that interpretation?

F5. How can boundary error, parameter error, observation error and structural discrepancy be distinguished? What priors/independent experiments are required, and how can a flexible discrepancy model conceal missing physics?

F6. How should experiment and CFD be fused without counting the same calibration information twice or treating CFD as exact truth? Compare multi-fidelity, modular/cut approaches and explicit cross-facility discrepancy where appropriate.

#### G. Uncertainty estimation and propagation — P0

G1. Build a source/dependence taxonomy covering random and systematic measurement effects, calibration, drift, correlated channels/time, geometry, material properties, boundaries/power, initial states, parameters, numerics, CFD and reduction/model discrepancy. Distinguish a lack of knowledge from a justified probability distribution.

G2. Compare local linear propagation, Monte Carlo/quasi-Monte Carlo, polynomial-chaos/collocation, ensembles, posterior predictive propagation and surrogate-assisted methods. Identify assumptions, computational budgets and failure near strong nonlinearities or regime changes.

G3. How should covariance from shared instruments, derived duties/flow estimates, common ambient forcing and jointly estimated parameters be retained? Distinguish conditional Type A mean uncertainty from full prediction accuracy.

G4. How can uncertain closures/operators be propagated through steady and transient ROMs while maintaining physical constraints? Compare Bayesian operator inference and neural/operator methods against simpler constrained networks with uncertain parameters.

G5. What does “calibrated uncertainty” mean in this setting? Compare coverage, interval width/sharpness, likelihood or proper scores and conditional/regime checks, with small independent sample sets. Avoid equating bootstrap bands, confidence intervals, credible intervals and scenario envelopes.

G6. How should uncertainty in time/location of extrema, threshold crossing, settling time and freeze margin be reported? What can be bounded if a full probabilistic model is unjustified?

G7. How can we separate numerical/CFD error and model discrepancy, and avoid double-counting residuals? Which uncertainty sources dominate the decision and should guide experimental/CFD effort?

G8. What exactly can real-time inverse/UQ methods such as NEMO estimate, under what linear/nonlinear parameterization and noise assumptions? Does that match our unknowns and data, or should it remain a later comparator? Differentiate acceleration of inference from a complete treatment of model-form uncertainty.

#### H. Experiments that select between approaches — P0

H1. What is the smallest informative design for separating net heat loss, regional G, participating C, ambient effects and fluid/solid coupling? Compare steady duties at multiple temperatures, warm/cold relaxations, known-power holds/shutdowns and independent heater/cooler changes.

H2. What must be measured to establish an absolute energy scale? Address secondary flow/temperature/property uncertainty, actual versus commanded input, electrical deposition/parasitics, residual duty and common sensor biases.

H3. What is an evidence-based choice of input excitation, duration, rate, repeat count and sensor placement? Discuss bandwidth, time-scale separation, autocorrelation, thermal equilibrium versus stationary operation, and conditioning. Do not invent facility-safe setpoints or assume arbitrary protocols can be executed.

H4. Compare parameter-information objectives with QoI uncertainty reduction and model-discrimination experimental design. Which is most useful when several model forms fit the same sparse data?

H5. Which extra measurements offer the largest benefit, and which claims must be dropped if they cannot be obtained? Separate existing instruments, feasible metadata requests, additional instrument proposals and CFD-only evidence.

H6. Produce a concrete change-request matrix mapped to Nick's P0–P4. For each row: objective/QoI, exact missing quantity, current coverage/unknown, proposed change, instrument/location, clock/rate/duration/repeats to justify, uncertainty need, calibration/validation role, acceptance check and question for Dr. Luciano. Label every item proposed, not agreed. Identify case reallocation when an originally blind P3 case becomes a calibration anchor.

#### I. CFD evidence, coupling and delayed availability — P0/P1

I1. Which BCs, material/source details, operating histories and observation operators must experiments provide to CFD? What should CFD return to support closure/reduction work beyond attractive contour plots?

I2. What verification/validation and grid/time/regime sensitivity are needed for local recirculation, wall flux and extrema? Distinguish mesh convergence of integrated duty from convergence of local extent or peak temperatures.

I3. How do Reynolds/thermal development, transition assumptions, buoyancy treatment, gravity/pressure boundaries and conjugate walls affect applicability? Do not assume a turbulence model or a laminar regime from convenience.

I4. How can a limited CFD campaign discriminate candidate closures efficiently? What should be varied independently and held fixed? How should unavailable CFD change the minimum PhD demonstration rather than simply delay all work?

#### J. Operational assistance and dashboard research — P1/P2

J1. Which outputs are actionable, which require prediction versus state estimation, and which can be supported before full transient capability? Distinguish current measured margin from a forecast of future margin.

J2. What does evidence say about showing uncertainty, unavailable inputs, sensor coverage, out-of-domain predictions, stale measurements and competing model explanations? Separate model credibility from interface polish.

J3. What result/data contracts should be discussed jointly with Ben Booth and NeutronOS: units, clock, provenance, facility/revision, scenario, horizon, uncertainty, validity and threshold ownership? Do not infer their existing product/stack or contact them.

J4. Which later startup/shutdown, pressure/level, trace-heating and freezing questions require new physics or data? Distinguish single-phase margin prediction from resolving solidification, blockage or multiphase processes. Separate advisory prototypes from actual control or unattended operation.

#### K. A defensible contribution and alternatives — P0

K1. What are the closest prior methods—not only closest fluids/applications—for our proposed reduction/closure/identification/UQ framework? What do they already accomplish that we must not claim as new?

K2. Identify 2–4 candidate contribution packages, each with a narrow claim, closest prior work, specific methodological difference, required data, fair baselines, testable hypotheses, failure criteria and realistic fallback. Explicitly mark them provisional until the search supports them.

K3. Could contributions arise from QoI-driven physical reduction, uncertainty-aware model/closure selection, observable-consistent spatial reconstruction, experiment–CFD identification, or assessment of achievable recirculation extent/thermal-effect prediction? What existing work most strongly challenges each idea?

K4. Distinguish method development, a reproducible procedure, new empirical physics, and a facility demonstration. Which combination would advance knowledge beyond a software integration/application exercise?

K5. What could be a valuable negative result—for example, proving limits of sparse-data identification or showing when a richer spatial closure is unnecessary—and what evidence would make it publishable?

### 5. Required outputs and format

Produce a structured research memo with these deliverables. Use tables for comparisons; support substantive claims with verified citations close to the claim.

1. **Decision summary:** explain the problem/impact, strongest existing approaches, most consequential gaps, recommended minimum method comparison and immediate evidence requests. Separate P0/P1/P2 and your confidence.
2. **Evidence/search ledger:** databases/sites, dated search strings, inclusion/exclusion rules, forward/backward citation tracing, source versions and access/reading depth. Avoid claiming an exhaustive/systematic review unless justified.
3. **Question-to-literature matrix:** A1–K5 IDs, answer or unresolved status, strongest sources, applicability, contradictory findings, recommended next investigation. Do not silently omit hard questions.
4. **Model/method comparison matrix:** state/input/observation equations or essential structure, retained physics, training data, constraints, uncertainty, cost, extrapolation/identifiability risks, applicability and why it belongs in—or outside—our minimal comparison set.
5. **Uncertainty and identification design:** initial source/covariance budget, candidate propagation/inference approaches and a fair comparison plan. Give worked symbolic examples where useful; illustrative numbers must be labeled, not attributed to TRIDENT.
6. **Experiment and CFD request matrices:** concrete proposed Nick-plan changes and a distinct CFD/thesis evidence contract. Rank by impact on a QoI, model discrimination and feasibility. Explain consequences if a request is unavailable.
7. **Recirculation feasibility ladder:** no local-flow measurements; separate extent prediction, heat-transfer-effect prediction and optional full reconstruction. State which evidence can assess each and what remains unvalidated.
8. **Novelty/gap table:** proposed contribution, strongest prior method and result, precise remaining gap, evidence for that gap, counterargument, falsifiable test and minimum evidence. Search for reasons to reject our favored claims.
9. **Proposal kit:** a sourced problem/impact paragraph, 2–4 candidate research questions/objectives and hypotheses, an approach/work-package outline, assessment criteria to set, preliminary demonstrations needed, risks/dependencies and fallback scope. Do not claim experiments, CFD, approval or novelty that do not exist.
10. **Prioritized bibliography and reading order:** a manageable core reading set with annotations explaining the exact decision each informs, supplemented by further leads where needed. Include verified machine-readable/BibTeX metadata only; quality matters more than citation count. Separate “read now”, “read next” and “later”.
11. **Seven-day proposal sprint:** literature triage and closest-method check; QoIs/model selection; UQ and identifiability; experimental-plan changes; CFD/recirculation feasibility; aims and contribution challenge; integrated proposal/committee-question review. Specify the concrete artifact each day produces and work that can proceed without CFD/thesis. This is a suggested planning sequence, not a promise to finish all research in seven days.
12. **Unanswered questions for me/advisers:** group only consequential decisions about purpose, facility evidence, scope and acceptable claims. Explain why each answer changes the method or experiment, rather than asking an unprioritized list.

If the full scope exceeds one research pass, deliver a substantive P0 synthesis with verified core references first, plus an explicit continuation queue for P1/P2. Do not stop with only a generic search plan or a bibliography. Do not dilute depth by pretending all questions were answered. Suggest 3–5 high-value follow-up review prompts targeted to unresolved decisions.

### 6. Initial search families

Adapt, expand and log searches rather than treating these phrases as an exhaustive strategy:

- “single-phase natural circulation” scaling stability heat loss conjugate uncertainty; “molten salt” natural circulation experiment CFD transient; surrogate fluid similarity MSR.
- thermal network grey-box identification RC regional effective capacitance; thermal model structural practical identifiability; measured-power cooldown experiment design.
- conjugate heat transfer developing mixed convection curved junction recirculation; reattachment reverse-flow volume heat flux low Reynolds buoyancy.
- goal-oriented physical model reduction conservation positivity thermal advection; operator inference stability Bayesian; nonintrusive parametric ROM closure learning.
- inverse problem model discrepancy sparse temperature observations boundary uncertainty; multi-fidelity Bayesian calibration experiment CFD identifiability.
- uncertainty propagation ROM correlated inputs posterior predictive coverage; Bayesian optimal design QoI model discrimination; sensor placement heat transfer inverse.
- predictive digital twin uncertainty thermal operating margin freeze protection; uncertainty communication decision support model validity.

Do not restrict retrieval to these exact words; similar work may use “system identification”, “thermal impedance”, “network reduction”, “compact thermal model”, “lumped parameter”, “closure discovery” or other terminology.

## END PROMPT

---

## Optional attachments for the research conversation

Upload what is available; the prompt already carries the essential constraints.

- `docs/project/RESEARCH_ROADMAP.md` and `docs/uncertainty/README.md`.
- `docs/experiments/RESEARCH_DATA_REQUIREMENTS.md`.
- Nick's original Phase 0–4 `.tex` files, especially Phases 2–4.
- The five original `reference/phD_goals/Raw_notes/` Markdown notes, explicitly labeled raw notes rather than verified claims.
- Current proposal abstract/aims if the user chooses to provide them; do not assume a manuscript revision from a pathname.
- Ethan's TAMU thesis **when uploaded**; identify its exact revision. Its absence must not block the first literature pass.
- `SEED_LITERATURE.md` from this bundle.

The local paths above are upload suggestions, not accessible resources for another ChatGPT conversation. No raw experimental data are required to start this review. Keep confidential material under the user's chosen sharing constraints.