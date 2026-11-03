# Proposal outline — source-linked working bullets

- Expanded November 2, 2026; preliminary work precedes aims by author direction.
- This revision builds on the completed literature review, recovers planning substeps and uses dated HPC reports with their evidence limits.
- Active source after application: `sections/outline/`; the original proposal is still unchanged in this session.
- [Source map](doc_support/reconciliation/2026-11-02/SOURCES.md) · [Context expansion](doc_support/reconciliation/2026-11-02/RESEARCH_CONTEXT_EXPANSION.md) · [Author decisions](doc_support/reconciliation/2026-11-02/FOLLOWUP_DECISIONS.md).

## Motivation and Research Problem


### Engineering purpose

- Predict circulation, heat-removal duty, losses, and relevant fluid/wall minimum and maximum temperatures as operating inputs change. [N01; N03; R01]
- Connect fast physical prediction to operator what-if questions, limit awareness, and freezing/trace-heating margins. Distinguish requested functions from demonstrated capabilities. [N01; G01: Intro; R01]
- Fill with primary citations: MSR thermal-hydraulic decisions and loop-history rationale; use Review B Sections 2--6, rather than assuming whole-reactor similarity.
- Ground the reactor motivation in temperature distribution, bulk/local salt velocity, source/removal allocation and property effects; use Brown et al., Table II and Section V. Nonnuclear loops test selected mechanisms and do not validate reactor neutronics, chemistry or complete safety behavior. [primary citation: brown2020msrphenomena]
- Use the original MSRE report as a metrology/property lesson. The review does not substantiate the notes' repeated 25% heat-balance claim; distinguish power metrology, primary-exchanger property revision and air-radiator performance. [S47 dossier: conclusions, printed pp. 27--28] [primary citation: gabbard1970msre]

### Why ACU and VCU?

- Introduce ACU salt and VCU surrogate-fluid loops as distinct applications of the reduction framework; describe purpose and evidence separately. [G01: Intro; N05; N07]
- Use the documented Prop-30/propylene-glycol branch for VCU; historical mineral-oil wording is superseded. Run-specific composition and properties still need qualification. [N07; literature A Section 15]
- Figure placeholders: one hardware photograph and one geometry/sensor schematic per facility; choose from the figure-pointer index. [N05; N08]

### Reduction problem and research gap

- Explain how developing/asymmetric profiles can separate local sensor temperature from conserved bulk enthalpy transport. Avoid a universal salt-versus-water claim. [G01: Intro; literature A Sections 4--5]
- Ask how to select conservative closures and temperature maps that improve useful predictions or establish where simpler models are adequate. [literature B Sections 10--11]
- Use TAMU master findings as prior motivation, with their case and validation limits. [primary citation: fierro2026cfdoneD,reis2024molten]
- Introduce the following preliminary-work section as the bridge: the master's establishes an executable reduction process and shows why matching temperatures alone cannot settle the physical interpretation. The PhD adds qualified experiment/CFD integration and an assessed selection procedure. [MS01; Review B Sections 7, 10--11]

## Preliminary Work and Research Readiness


### Master's work: an existing end-to-end reduction example

- Author direction: use the completed master's work to establish feasibility before describing proposed aims. The next experimental demonstration should show that we understand the experimental data and can reproduce temperatures; it is proposed work, not a completed ACU/VCU result. [AD-20261102-02--03] [primary citation: fierro2026cfdoneD]
- Start with the TAMU problem, CFD reference and sensor meanings; show how fields become matched mass, energy, pressure and temperature quantities. Keep the distinct CFD time-averaging windows explicit. [MS01: Chapters 2--3; claim manifest]
- Explain the working steady model: energy transport around the loop, temperature periodicity, buoyancy--resistance balance, separate thermal paths, and fluid/wall observations. This establishes a practical implementation route. [MS01: Chapter 4]
- Present one temperature-versus-location comparison and its exact case population, supplied inputs, fitted choices and sensor policy. Link the underlying score rows and figure manifest; author selects the plot. [MS01: Chapter 5; figure-manifest F10/F11]
- Label the master's assessment retrospective: nominal CFD cases informed development and the heater-power cases had been previously encountered. These results support feasibility and lessons, not independent ACU/VCU validation. [MS01: abstract; Chapter 6]

### Lessons that motivate the PhD

- Temperature and circulation objectives can favor different fitted settings; show both rather than selecting a temperature score as evidence of correct flow. [MS01: Chapter 6, answers to the research questions]
- A lower temperature error can coexist with incorrect allocation of cooler and junction heat removal. Carry local energy budgets alongside temperature agreement. [MS01: Chapter 5; figure-manifest F09]
- Preserve the sensor policy: the primary wall aggregate omits TW4--TW6 and unmatched TW10; restoring TW4--TW6 changes the earlier models' grades. Do not describe the omitted sensors as invalid. [MS01: claim provenance; final revision summary]
- Use hydraulic/thermal development and observation meaning to choose candidate repairs; a fitted residual loss or resistance is not automatically a measured hardware property. [MS01: Chapters 5--6; Review A Sections 4--7]
- The tested two-stream heat exchange did not improve temperatures, and the fixed-inlet alternative violated mixing. Recirculation in TAMU motivates a bounded question; it does not establish ACU/VCU recirculation or a transferable coefficient. [MS01: Chapter 6]
- PhD step beyond this work: assess a reproducible reduction/closure/observation procedure using qualified experiment and CFD evidence, with uncertainty and unused assessment conditions. Reproducing a temperature trace is an initial demonstration; an additional method benefit or supported limit is the research contribution. [Review B Sections 7, 10--11]

### TRIDENT 1D groundwork and evidence status

- Use the model-introduction note to explain segmented fluid/pipe/optional insulation states, zero/prescribed/coupled steady flow and conservation outputs. Its synthetic examples establish numerical behavior, not facility prediction. [N09]
- A saved October 20 modeling-project copy supplies dated research records; it is not asserted to be the newest executable checkout. No code-location decision is required to organize this outline. [R01--R05; AD-20261102-01]
- CAL-008 ambient-only comparisons, CAL-009 startup assumptions and CAL-010 startup-conditioned model comparisons are prior research groundwork. Preserve their supplied initial/boundary information and mixed results. [R03--R05]

### Next feasibility demonstration: understand data and reproduce temperatures

- Assemble a documented case: facility/configuration, timestamps, units, channel map, calibration, heating/cooling/ambient history and known data gaps. Use Nick's plan and existing notes to define the evidence needed; do not assume a new run exists. [N03--N08; Review A Section 15]
- For each temperature, state whether it is a primary-fluid probe, wall/contact sensor or fiber measurement and specify the corresponding model observation. Separate measured values, averaged values and inferred bulk states. [Review A Section 5] [primary citation: jcgm2020measurementmodels]
- First reproduce an accepted development case using declared inputs and fitted quantities; report per-sensor residuals, spatial patterns, energy closure and uncertainty. Call this reproduction or calibration when target data inform the model.
- Then freeze those choices and compare against a separate eligible condition when available. Identify whether assessment information was previously inspected; avoid relabeling retrospective cases as blind. [Review A Sections 10--11]
- Show what the temperature comparison teaches about boundary conditions, loss paths and observation mapping. A CFD-conditioned map, measured-startup trajectory and autonomous forward prediction receive separate labels and scores.
- Fill later: selected experiment, controlling data location and eligible assessment cases. Keep transition/operator stages visible; this answer defines the immediate feasibility emphasis, not their final minimum scope. [AD-20261102-02]

### Later HPC studies and what they add to readiness

- Use the maintained important-report index and the newer saved checkpoint to locate the strongest existing demonstration. [HC01/HC11/HC16]
  - The saved reports include later VCU run-condition/steady-window, boundary, regional-resistance and downcomer comparisons beyond CAL-008--010. Their assumptions and supplied temperature/boundary inputs must accompany any figure selected.
  - The local researcher cataloged report metadata and read selected source sections; this does not certify every result or establish the live HPC state. The written HPC request asks for the best existing reproduction and eligibility evidence.
- Use the isolated TAMU developing-profile work as a mechanism/reduction benchmark with explicit transfer limits. [HC06--HC08]
  - The reconstruction/manual and applicability report motivate distinctions among transported temperature, area-density/buoyancy and probe observations, and separate thermal/hydraulic ownership.
  - The October26 batch-study decision establishes bounded authorization, not completion or accepted ACU/VCU coefficients. Obtain the later receipt/report before presenting its outcomes.

## Research Questions, Aims, and Staged Goals


### Framework contribution

- Develop and assess a CFD--experiment order-reduction framework; the resulting model is a fast, interpretable physics-based ROM. [R01; October 14 approved directions]
- Use the custom 1D solver as the main model now; CFD and experiments inform reduction, closure selection, learning, and assessment. [November 2 author direction; N09]
- Proposed organizing aims: (1) reduction and development-informed closures; (2) learning and observation-consistent temperature maps; (3) independent assessment and applicability. Refine these sentences with the author. [literature B Section 11]
- Organizing question: what information and reduced physics are needed to reproduce observed temperatures and then predict new conditions with defensible uncertainty? Keep the development-case demonstration distinct from the independent predictive test. [AD-20261102-02; Review A Sections 1, 10--11]
- For each aim specify one output, the permitted inputs, a comparator and an evidence product; organize by scientific question rather than by software package or a sequence of paper summaries. [G01: Theory motivation; Review B Section 11]

### Approved staged goals

- Stage 1: steady heat removal/losses, circulation, temperature extrema and supported operating margins. [R01--R02]
- Stage 2: transitions between operating conditions, thermal/hydraulic response, settling, and time-dependent margins. Stage approval is distinct from implementation readiness. [R01--R02]
- Stage 3: operational assistance and operator-facing model/data dashboard; collaborate with Ben Booth and NeutronOS. Controls and unattended operation need a separate agreed scope. [R01--R02]
- Uncertainty estimation and propagation are core across all stages. The older outline's blanket optional-transient/dashboard wording is superseded by R01/R02.
- Immediate feasibility emphasis is experimental-data interpretation and temperature reproduction, leaning on the master's work. This does not remove approved transition/operator goals or establish their minimum dissertation demonstration. [AD-20261102-02]

### Spatial questions and boundaries

- Temperature first: centerline and radial profiles, with angular dependence where supported; richer velocity mapping is a later capability. [October 14 directions; G01: Shape functions]
- Overall circulation and local recirculation are separate outputs; investigate local extent and thermal consequence with qualified CFD, without inventing local experimental measurements. [R01]
- Fill: distinguish minimum dissertation demonstration, staged research goals, and later capabilities; retain symbolic criteria until justified.

## Experimental and Computational Evidence


### Facility/source table to fill

- For each facility list geometry revision, fluid, materials/insulation, heater/cooler boundaries, sensor meanings and uncertainties. Keep historical and current configurations distinct. [N05--N08]
- Use Rev9/Rev8 records with explicit revision labels; do not select authoritative dimensions from appearance or an older generated drawing. [N05]
- VCU notes describe three mat and four band heaters; electrical input, deposition into solids/fluid, and net loop heat are different quantities. Use the accepted nominal dial-based specification where applicable and label its assumptions; metered electrical input and net fluid deposition remain separate evidence. [HC10] [N04; N06]
- Clarify PTC/STC/Luna roles by facility and date; do not merge the older six-PTC resistance exercise with the four-internal-TC VCU plan. [N08; N10; literature A Section 15]
- Give every reusable case a record linking facility, geometry/property version, run/time window, channel/coordinate map, boundary histories, exclusions and uncertainty source. Link to original photos/drawings through their source note; do not copy dimensions from an unqualified picture.
- Track four power quantities separately: command/dial setting, electrical input, deposited heat and net control-volume duty. Record measured versus assumed values and source provenance. [N04; N06; Review A Sections 8, 15] [primary citation: jcgm2020measurementmodels]
- The October22 CAL-019 decision accepts constant nominal20-ohm mats/48-ohm bands and dial=loaded RMS voltage for exploratory input calculations: three parallel mat/band pairs and one remaining band. For equal settings $X$, $P_{\mathrm{nominal}}=(7/30)X^2$ W. This is an accepted nominal assumption, not a measured resistance law, delivered thermal duty or recommended operating setting. [HC10]
- Extra electrical characterization can improve confidence but is not a prerequisite to the accepted nominal calculation. Preserve run-specific settings/off events and source-to-solid/fluid storage/contact/loss accounting. [HC10; Review A Sections 2, 8]

### Experiments and collaboration

- Map Nick's checkout and Phases 1--4 to configuration, noise/calibration, relaxation, energy anchors, and operating-condition/withheld assessments. Preserve original numbering and version. [N03--N04; R01]
- Any new data requirement enters the experiment-request matrix and discussion with Dr. Luciano; do not assume an uncommunicated run or sensor will be available. [R01--R02]
- Freeze development, model-selection and assessment roles before fitting; supplied boundaries cannot also be scored as independent outputs. [literature A Sections 10--11, 15]
- Phase 2 passive relaxation primarily supports response rates under its capacity/conductance assumptions. A Phase 3 case used to set an absolute energy scale becomes development evidence and cannot also remain blind assessment; preserve the original plan while recording a proposed role change. [G01: phase discussion; Review A Section 15]
- Create an experiment-to-model table: source phase/version, available signals, parameter/QoI addressed, supplied inputs, development/assessment role and remaining limitation. Communicate proposed changes through Dr. Luciano; this outline sends no requests.

### CFD deliverable specification

- Jointly define steady cases, field/integral exports, signed section fluxes, conjugate budgets, development descriptors, temperature profiles and sensor footprints. [literature A Section 14]
- Include units, geometry/property/boundary revisions, conservation and target-specific numerical sensitivity. Future transitions additionally require synchronized histories and initial-state information.
- Use current computational-team roles as planning context; older dated team notes do not verify November delivery or dataset readiness. [N11]

### Data lineage, quality and operating-condition groups

- Build a traceable data-to-model comparison record, following the existing data contract rather than a new disconnected spreadsheet. [GP15/19/21; HC03--HC04; Review A Sections 5, 10, 15]
  - Keep raw files and original timestamps/units unchanged; map native channels to physical sensors and model observations using explicit configuration, calibration and source-row identities.
  - Preserve mapped, synchronized, quality-flagged and accepted-window products as separate versioned transformations with parent IDs. Store measured statistics, CFD-reference quantities and model predictions with their distinct provenance and uncertainty.
- Group operating conditions by actual inputs and configuration, then report within-group variation and evidence coverage. [GP14/18; Review A Sections 9--11]
  - Use source/sink/environment histories and justified grouping tolerances; the historical five-bin examples are planning ideas, not a selected Cartesian test matrix.
  - Distinguish classification as steady/transient, accepted statistical reporting windows and physical energy-equilibrium claims. CAL-012 and the later CAL-016 recorded-channel screens use different rules. [HC11]
- Treat quality flags and exclusions as scientific choices requiring reasons and sensitivity checks. [GP21; HC03; Review A Sections 8, 15]
  - The historical four-standard-deviation deletion idea is not an adopted universal rule; preserve flagged samples and consider genuine transients, autocorrelation and channel roles before exclusion.
  - Record missingness, drift, calibration grouping and the effect of alternative window/channel policies; do not select a window because it minimizes the fitted-model residual.

## The Custom 1D Model and Observation Mapping


### Starting representation

- Divide the loop into axial cells with fluid, pipe and optional insulation temperatures; declare heater, cooler, ambient and axial/radial heat paths. [N09; N10]
- Explain M0 radial diagnostic, M1 stagnant segmented loop, M2 prescribed signed-flow transport, and M3 coupled buoyancy/resistance root. These are distinct from the empirical reduced-zone response family. [N09]
- Fill: minimal equations, sign conventions, property choices and conservation ledger; identify source derivation and implementation location. Do not rederive all background theory. [G01: Theory motivation]
- Use stored energy and signed enthalpy fluxes as the starting balance; evaluate each shared transfer once with opposite signs for adjacent volumes. Define state, units, positive loop direction and property temperature before presenting the reduced equations. [Review A Section 2, EQ-01--03]
- For temperature-dependent heat capacity, use an enthalpy difference obtained by integrating $c_p(T)$; distinguish fluid, pipe and optional insulation storage. A steady M3 algebraic circulation balance does not itself provide transient inertia. [Review A Sections 2--3]

### Closures and observation operators

- Start from attempted master closures, then characterize hydraulic/thermal development before choosing transfer-law descriptors. Keep closure selection separate from sensor mapping. [October 14 directions; literature A Sections 4, 13--14]
- Compare bulk enthalpy, centerline/radial/angular fluid temperature and wall/contact sensor responses according to their distinct meanings. [G01: Proposed methodology; literature A Section 5]
- Treat simple local-to-average ratios as historical candidates; test conditioning and conservation before adopting a universal mapping. [G01 indices 8879--8950, 10284--10431; literature A Section 14]
- Write the observation model schematically as $y_k=H_k(x,u,θ)+b_k+ε_k$: location/footprint and contact or filtering belong in $H_k$, shared calibration in $b_k$, and residual variation in $ε_k$. Choose those terms from evidence rather than inventing independent noise. [Review A Section 5] [primary citation: jcgm2020measurementmodels]
- If a proposed profile descriptor requires contemporaneous CFD or measured primary temperature, classify that result as conditional reconstruction. An autonomous forward closure must obtain its descriptors from the retained state and allowed inputs. [Review A Sections 1, 14]

### Use-time information

- Steady forward prediction: prescribed operating inputs and qualified configuration predict withheld primary outputs.
- Startup-conditioned trajectories may use measured initial temperatures and supplied later ambient; label that information and do not call it an autonomous forecast. [R04--R05]
- CFD-conditioned reconstruction, full-forward ROM prediction and later sensor-updated estimation need separate contracts and scores. [literature A Sections 1, 11]

### Reproducible inputs and numerical choices

- Explain the model end to end using its resolved configuration and ledgers, as requested in the earlier Moser discussion. [GP10--GP11; HC05; Review A Section 12]
  - Declare geometry units, state order, property basis, source assignment, cooler form, axial/radial discretization and observation locations.
  - Record defaults and overrides, refinement, nonlinear tolerances and root-selection outcomes. Numerical parameters belong to verification/sensitivity, not physical calibration.
- Keep the three temperature roles explicit when evaluating developing-profile additions. [GP12--GP13; HC06--HC07; Review A Sections 5, 14]
  - Transported enthalpy, area-density/buoyancy and local probe response need not share one temperature; test whether a low-order profile or covariance relation materially changes the target.
  - Historical local/mean temperature or pressure ratios are candidates; test reference dependence, small denominators and flux preservation before adopting them. Do not transfer TAMU coefficients or sensor meanings automatically.

## Theory Motivation and Research Methodology


### Closest prior methods and why these choices

- Fill a compact primary-citation table: conservation/developing-loop reduction; closure identification; observation/reconstruction; learning/UQ; validation. Use the completed reviews, not a fresh generic review. [literature A Sections 2--11; B Section 7]
- Explain each chosen method's role, required information and failure limit; keep derivation details in appendices or linked sources. [G01: Theory motivation]
- Identifiability/profile tools support physical interpretation; neither generic fitting nor ordinary scale ambiguity is itself a new contribution. [primary citation: raue2009identifiability]
- Use the master's as the nearest completed project baseline; cite its negative tests, exposure history and heat-path discrepancy alongside useful temperature reproduction. Wall storage, RC calibration or another fitted state alone is not the proposed novelty. [MS01; Review B Section 7] [primary citation: fierro2026cfdoneD]
- For each method bullet retain a primary citation plus the review section/dossier locator that explains its applicability. New primary references in this pass are routed in the master's/citation pointer note; their original PDFs were not newly re-audited here.

### Aim 1: reduction and closure selection

- Declare control volumes, retained states, conventional baseline and closure inventory.
- Derive descriptors from consistent CFD budgets; require descriptors needed at prediction time to be available from ROM states and prescribed inputs.
- Change transfer/hydraulic assumptions in controlled comparisons to attribute improvement rather than merely adding fitted freedom. [literature A Sections 11, 13--14]

### Aim 2: learning and reconstruction

- Learn only supported physical parameters/combinations from development experiments; carry uncertain power, properties, calibration and observations jointly.
- Test centerline/radial temperature and regional heat transport separately; assess ambiguity and thermal consequences of spatial structure.
- Keep physically identified closures, observation correction, and empirical discrepancy distinguishable. ML architecture remains open; GNN/LSTM mentions in G01 are candidates, not commitments.
- Apply the data-understanding demonstration first: reconcile labels, units, installed sensor meaning and supplied inputs before optimizing parameters. Diagnose persistent spatial residual patterns instead of allowing one fitted loss to absorb every mismatch. [AD-20261102-02; MS01: Chapter 6]
- Compare parameter combinations and output sensitivity over justified nuisance ranges; a well-matched trace does not establish unique conductance, capacity, deposited power or local heat-transfer interpretation. [Review A Sections 6--8] [primary citation: raue2009identifiability]

### Aim 3: fair comparisons

- Compare a fixed-closure physical baseline, proposed framework and modest data-driven predictor under matched development cases and use-time information.
- Freeze cases/conditions and scoring rules before final assessment; distinguish emulator accuracy from facility prediction.
- For transition comparisons hold boundary/initial-state information and refitting opportunities common; score response/settling before promising full transient fields. [literature A Section 11]
- Report two explicit products: temperature reproduction on the development cases and prediction on eligible unused cases. Maintain the same sensor policy, input information and parameter-refitting opportunities for every comparator. [MS01; Review A Sections 10--11]

### Physical learning, observation mapping and residual correction

- Compare three distinct interventions instead of treating every improvement as a generic bias correction. [GP06/13/16/22; Review A Sections 4--8]
  - Physical learning: supported heat-path, transfer or hydraulic parameters change the conservative model and must retain an interpretable evidence basis.
  - Observation mapping: convert the reduced state to the actual probe/contact/fiber response; missing sensor physics is separate from the energy or momentum closure.
  - Residual correction: an empirical discrepancy model may improve a declared output, but its fit does not validate local heat-transfer or flow physics.
- Assess both the uncorrected physical model and the corrected alternative across conditions. [GP16/22; Review A Section 11]
  - Compare residual size, spatial/operating-condition structure, physical budgets, uncertainty and runtime at common inputs and refitting opportunities.
  - Test interpolation and out-of-condition behavior separately; a smooth correction or shrinking training bias is not independent predictive evidence.
- Choose temporal or machine-learning complexity only when it addresses a documented limitation. [GP14/25; Review A Section 16]
  - Start with physical/linear or modest data-driven references. GNN, LSTM, neural operators and richer field emulators remain candidate branches rather than required architectures.
  - Declare whether recent histories estimate the current state, forecast a later state, reconstruct supplied reference fields or update parameters; score those tasks separately.

## Assessment, Uncertainty, and Applicability


### Verification and independent evidence

- Check ROM conservation and numerical sensitivity; qualify CFD reference uncertainty separately from experimental calibration and validation.
- Assess temperatures, circulation, duty, loss budgets, spatial reconstruction and cost separately, with engineering units and location/time meanings.
- Qualify ACU flow evidence; CFD flow at VCU is an uncertain reference, not direct experimental circulation validation. [literature A Sections 10--11]
- Temperature report: residuals in K by channel/location, channel-wise bias and RMSE, and declared time/space aggregation; report flow/duty and local heat budgets separately. Retain excluded channels with reasons and a sensitivity route. [MS01: score-policy lesson; Review A Section 10]
- Use the same case names and configuration versions from source data through reduction, calibration, plotting and proposal claims. A figure caption should state whether each series is measured, CFD-referenced, calibrated or independently predicted.

### Uncertainty throughout

- Carry primitive calibration/channel, power/deposition, boundary, property, geometry and initial-state uncertainties with shared dependencies.
- Derived duty/flow inherit their ingredients; do not count them again as independent observations.
- Distinguish measurement variability, installed accuracy, model discrepancy and numerical uncertainty. Propagate through steady and transition outputs. [N02--N04; R01; literature A Sections 8, 15]
- Use covariance-aware propagation when a local linear approximation is justified; reuse common calibration, property and input variables wherever they appear. Joint input sampling must preserve those same dependencies. [primary citation: jcgm2011vectorcovariance,jcgm2020measurementmodels]
- Separate a scenario envelope, parameter interval and predictive interval; assess uncertainty against the intended output and available case count. Do not turn a few temperature comparisons into a calibrated rare-event probability. [Review A Section 8]

### Acceptance and limits

- Fill target/reference/metric/tolerance-symbol/runtime table; assign numbers only with an intended-use and evidence basis.
- Sensor minima/maxima and model-inferred spatial extrema require different evidence; freezing/temperature margins require a sourced threshold. [N01; R01]
- Discriminate physics, input, observation and numerical explanations for disagreement; report a simpler adequate domain or a supported measurement need when warranted.
- Report local recirculation inference limits separately from bulk prediction and thermal-consequence evidence.

### Sensor changes and adequacy of the available information

- Retain the planning questions about sensor reliability, loss and evolving installation/material conditions as bounded assessment branches. [GP03/17/26; Review A Sections 5--8]
  - Compare full and reduced sensor sets at matched inputs and fitting access; quantify the resulting loss of temperature/target accuracy and uncertainty.
  - Record calibration/drift, sensor movement, thermal expansion or changing losses as competing explanations only where evidence supports them. A mismatch is not automatically a failed sensor.
- Connect a residual pattern to an evidence request before promising diagnosis or operator advice. [GP26--GP27; HC12--HC14]
  - Separate input error, observation error, numerical error and model inadequacy; identify which existing or proposed measurement could distinguish them.
  - Keep ACU and VCU evidence separate. Similar processing or shared code does not make their configurations, calibration or validation interchangeable.

## Work Plan, Deliverables, and Open Decisions


### Sequence and deliverables

- First: settle the bullet outline, input/output contract and evidence pointers; then expand selected sections into prose with primary citations.
- Stage 1 deliverables: verified 1D specification, closure/observation procedure, steady predictions, uncertainty and applicability assessment.
- Stage 2 deliverables: qualified transition comparisons and response/settling/margin outputs, with physical-time and initial-state evidence.
- Stage 3 deliverables: operator interfaces for what-if questions and limit awareness, with Ben Booth and NeutronOS; distinguish interface prototype from assessed predictive functions. [R01--R02]
- Use the October 14 schedule only as a dated sketch; confirm current proposal/defense dates and stage milestones. [N02; G01: Timeline]
- Next concrete demonstration package: source-linked case summary, temperature/channel map, resolved boundary/assumption list, reproduction plot and residual table, conservation ledger, uncertainty summary, and an explicit development/assessment label. Lean on the master's implementation and evidence practice. [AD-20261102-02; MS01]
- Keep the linked X.Chat research index as the navigation owner; proposal bullets, literature claims, facility notes and model results retain their own authoring locations. Dated handoffs record changes rather than spawning new competing outlines.

### Decisions made and remaining choices

- Decided November 2: place preliminary work after motivation and before proposed aims; reassess the story after reviewing the expanded bullets. [AD-20261102-03]
- Decided November 2: emphasize understanding experimental data and reproducing temperatures, using the master's work as groundwork. Do not infer that all three stages have been reduced to this demonstration. [AD-20261102-02]
- Open: which documented experiment and temperature comparison should lead the feasibility example? Organizing proceeds without an answer or a new code run.
- Open: minimum transition/operator-assistance demonstration and quantitative acceptance criteria; keep approved goals visible while settling these details.
- Open: newest 1D code/results location when implementation verification is needed. The saved October copy remains dated evidence, with no claim that it is current. [AD-20261102-01]
- Confirm dated milestones and geometry/photo choices at the relevant writing pass; earlier schedules and image labels are source context rather than new commitments.

### From offline comparisons to operator-facing results

- Use the planning document's provenance and integration tasks as concrete interface deliverables. [GP07/19/20/23; HC13/HC15]
  - Associate every result with model/case/data/configuration identity, source versions and parent transformations; preserve a route back to measured and reference inputs.
  - Agree collaborators, result schemas and ownership with Ben Booth/NeutronOS before choosing or claiming a deployment stack. Historical Model Corral/DeepLynx/GitHub mentions supply context, not a current architecture decision.
- Stage integration from offline reproduction to qualified replay and, where agreed, live data/model display. [GP07/21--GP24; HC13]
  - Display measured, inferred and predicted quantities distinctly, with units, time/horizon, scenario, uncertainty or unknowns, applicability and stale/missing-data status.
  - Assess model predictions separately from display/communication functionality. Operator suggestions, alarms with authority, automated commands and unattended operation need separate scope and evidence.
- Maintain a written local/HPC question-and-answer exchange alongside source-controlled research records. [November 2 author request]
  - Use dated outgoing questions, original incoming responses, a status register and local reconciliation; attach exact report paths, versions and evidence limits.
  - A prepared/exported Box file does not imply HPC receipt or an answer. Use the reply to update source maps and proposal bullets without fabricating current project status.
