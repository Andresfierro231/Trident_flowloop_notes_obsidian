# Dissertation proposal — expanded committee bullet draft


## Motivation and Research Problem


### Engineering purpose

- Predict circulation, heat-removal duty, losses, and relevant fluid and wall minimum and maximum temperatures as operating inputs change.
- Connect fast physical prediction to operator what-if questions, operating-limit awareness, and freezing and trace-heating margins.
- Molten-salt reactor (MSR) thermal-hydraulics involves temperature distributions, bulk and local salt velocities, heat-source and removal distributions, and material properties. Nonnuclear loops test selected mechanisms; their evidence does not establish reactor neutronics, chemistry, or complete safety behavior. [^8]
- **Engineering decisions served by each output.** Duty/losses support heat-path and cooler sizing; circulation supports resistance and heat-transport comparisons; wall/fluid temperature distributions support material and freezing-margin reasoning; response and settling support operating-change planning. [^8]
  - Add a decision--output--mechanism table for duty, losses, circulation, temperature extrema and response; state which are measured or model-inferred.

- **Metrology and the single-phase scope.** The Molten Salt Reactor Experiment provides a historical example of the need to distinguish reactor-power metrology, heat-exchanger property assumptions, and air-radiator performance. [^9]
  - Heat-balance interpretation requires a stated control volume, measurement basis, and property model. Critical heat flux lies outside the proposed single-phase, sensible-heat scope.



### Why a reduced model is needed

- Natural circulation couples heating, heat rejection, temperature-dependent density, and hydraulic resistance. A change to one heat path can alter circulation and therefore the temperatures and heat-transfer conditions elsewhere in the loop.
  - A model useful for engineering decisions must preserve this coupling while resolving the quantities needed for the decision. Correct total heat removal alone does not establish a correct wall-temperature distribution or freezing margin.
  - Detailed CFD provides spatial information for examining developing flow, local heat paths, and sensor placement. Repeated scenario evaluation and parameter estimation motivate a cheaper model whose approximations can be examined directly.

- A reduced model will retain axial transport, selected fluid and solid storage, heat exchange, and a circulation relation, while representing unresolved cross-sectional behavior through closures and observation maps.
  - Reduction therefore includes a physical selection: which states, exchanges, and spatial descriptors are consequential for the intended output? A small state count is useful only if the retained representation supports that output.
  - The principal challenge is to determine when a conventional one-stream description is adequate, when its closure or sensor mapping should change, and when richer states are required. [^1][^2]

- The experimental loops provide a progression from measured temperature reproduction to prediction under changed operating conditions. Their value is a controlled connection among hardware, measurements, CFD, and reduced models, with explicit limits on transfer to reactor systems. [^8]


### Why ACU and VCU?

- Apply the reduction framework separately to the Abilene Christian University (ACU) salt loop and the Virginia Commonwealth University (VCU) surrogate-fluid loop, accounting for their distinct purposes, configurations, and available evidence.
- For VCU, use the documented propylene-glycol formulation and qualify its run-specific composition and properties.
- **Which salt system or circuit is represented?.** Liquid-fuel primary systems have moving-fluid heat generation and possible nuclear feedback; solid-fuel salt-cooled systems receive heat through fuel/structures; secondary circuits receive it through exchangers. [^8]
  - Separate liquid-fuel primary, salt-cooled solid-fuel, secondary/passive circuit and test-facility purposes before making an MSR relevance claim.

- **Mechanism relevance and transfer limits.** Match the target mechanism through geometry, elevation and source/sink distribution as well as Re, Pr, a declared buoyancy measure, hydraulic/thermal development and fluid/solid response ratios.
  - Specify the target and compare Re/Pr, buoyancy, development and solid-response distortions; identify what cannot be matched simultaneously.

- **Source, property and loss differences.** Equal total power does not establish equivalent thermal forcing. [^8]
  - Declare electrical-wall versus volumetric heating, composition/property range and nonuniform losses; keep omitted reactor physics outside the representation claim.



### Reduction problem and research gap

- Developing and asymmetric profiles can separate a local sensor temperature from the temperature associated with conserved bulk enthalpy transport.
- Research question: how can conservative closures and temperature observation maps improve useful predictions, and when are simpler models adequate?
- Use the completed Texas A&M University (TAMU) study as preliminary evidence, with its case-specific assessment limits. [^1][^2]
- Preliminary work establishes an executable computational fluid dynamics (CFD)-to-one-dimensional (1D) reduction process and shows why temperature agreement alone does not settle the physical interpretation. The proposed PhD research adds qualified experimental and CFD integration and assessment of the reduction and closure-selection procedure. [^1]


### Research premise

- The proposed research will test whether a reproducible, conservation-based reduction procedure, informed by flow development and the actual sensor response, produces more useful temperature predictions than a conventional fixed-correlation model at comparable information and parameter flexibility.
- The contribution will be evaluated through the effect of specific modeling decisions: retained storage and heat paths, closure descriptors, observation operators, and the evidence used to learn parameters. Lower fitting error alone will not establish the contribution.
- An equally useful outcome is a defensible adequacy boundary: the operating conditions and outputs for which a simpler model is sufficient, and the additional information or physical representation needed beyond that boundary.


## Preliminary Work and Research Readiness


### Master's work: an existing end-to-end reduction example

- The completed master's work establishes feasibility for an end-to-end CFD-to-1D reduction process. The next experimental demonstration will test data interpretation and temperature reproduction in the ACU or VCU setting. [^1]
- The TAMU study relates CFD fields and sensor meanings to matched mass, energy, pressure, and temperature quantities, with explicitly defined averaging windows. [^1]
- The steady model includes energy transport around the loop, temperature periodicity, a buoyancy--resistance balance, separate thermal paths, and distinct fluid and wall observations.
- Assess temperature versus loop location with the case population, supplied inputs, fitted choices, and sensor policy stated explicitly.
- The master's assessment is retrospective: nominal CFD cases informed development and the heater-power cases had been encountered previously. These results support feasibility and lessons for assessment design; they do not establish independent ACU or VCU validation.


### Quantitative evidence from the completed study

- The completed study assessed four nominal CFD cases and six previously encountered heater-power cases. The reported balanced temperature metric combines the fluid-probe and wall-probe comparisons under the thesis's declared sensor-inclusion policy. [^1]

  | Model setting | Four nominal cases: balanced temperature RMSE (K) | Six power cases: balanced temperature RMSE (K) |
  |---|---:|---:|
  | Global thermal compensation | 9.280 | 12.853 |
  | Localized thermal setting | 4.957 | 5.989 |
  | Localized, flow-calibrated setting | 7.090 | 5.970 |

- The separate localized, flow-calibrated setting achieved CFD mass-flow mean absolute percentage errors of 0.967% and 1.310% for those two case groups. Its hydraulic setting was selected using known nominal CFD flow; the six power cases had also been seen previously. These are development and retrospective assessment results. [^1]
- The lower temperature errors did not establish the correct heat-removal distribution. Among the three compared heat sinks, the localized model assigned 6.9--7.3% to the cooler, compared with 57.4--60.8% in CFD, and 56.1--57.0% to junction regions, compared with 15.3--16.5% in CFD.
  - These fractions refer to the explicitly compared sinks, not an unrestricted fraction of all generated power. The fitted residual thermal conductance is an effective model term rather than a measured hardware property.
  - The result motivates a PhD assessment that scores measured temperatures, circulation evidence, and regional energy accounting separately. A single aggregate temperature score can conceal compensating heat-path errors.

- The primary temperature metric omitted a declared subset of wall channels; restoring some of those channels increased the earlier global-compensation errors from roughly 9--10 K to roughly 14--15 K. A corresponding restored-channel grade was not reported for the localized model. Sensor-policy sensitivity is therefore part of the evidence, not an optional presentation choice.


### Lessons that motivate the PhD

- Temperature and circulation objectives can favor different fitted settings; show both rather than selecting a temperature score as evidence of correct flow.
- A lower temperature error can coexist with incorrect allocation of cooler and junction heat removal. Carry local energy budgets alongside temperature agreement.
- The primary wall-temperature aggregate used a declared channel-selection policy. Restoring previously omitted channels changes the earlier models' assessment; channel exclusion therefore requires explicit reporting and sensitivity analysis.
- Use hydraulic/thermal development and observation meaning to choose candidate repairs; a fitted residual loss or resistance is not automatically a measured hardware property.
- The tested two-stream heat exchange did not improve temperatures, and the fixed-inlet alternative violated mixing. Recirculation in TAMU motivates a bounded question; it does not establish ACU/VCU recirculation or a transferable coefficient.
- PhD step beyond this work: assess a reproducible reduction/closure/observation procedure using qualified experiment and CFD evidence, with uncertainty and unused assessment conditions. Reproducing a temperature trace is an initial demonstration; an additional method benefit or supported limit is the research contribution.


### TRIDENT 1D groundwork and evidence status

- **Ambient and startup-conditioned temperature comparisons.** Preliminary studies examine alternative ambient and initial-state assumptions using observed-versus-predicted temperature traces and channel residuals.
  - Keep other-run learning, previously inspected windows and supplied later boundaries explicit; mixed performance is not a universal winner.

- The physical model includes segmented fluid, pipe, and optional insulation states; zero, prescribed, or coupled steady flow; and conservation outputs. Synthetic examples demonstrate numerical behavior rather than facility prediction.
- Ambient-only, startup-assumption, and startup-conditioned comparisons provide groundwork for assessing how supplied initial and boundary information affects temperature reproduction.


### Next feasibility demonstration: understand data and reproduce temperatures

- Assemble a documented experimental case with facility configuration, timestamps, units, channel mapping, calibration, heating, cooling and ambient histories, and known data gaps.
- For each temperature, state whether it is a primary-fluid probe, wall/contact sensor or fiber measurement and specify the corresponding model observation. Separate measured values, averaged values and inferred bulk states. [^11]
- First reproduce an accepted development case using declared inputs and fitted quantities; report per-sensor residuals, spatial patterns, energy closure and uncertainty. Call this reproduction or calibration when target data inform the model.
- Then freeze those choices and compare against a separate eligible condition when available. Identify whether assessment information was previously inspected; avoid relabeling retrospective cases as blind.
- Show what the temperature comparison teaches about boundary conditions, loss paths and observation mapping. A CFD-conditioned map, measured-startup trajectory and autonomous forward prediction receive separate labels and scores.


### Developing profiles and conditional wall response

- **Developing-profile and transfer studies.** Use temperature, transport, and buoyancy comparisons to assess whether a low-order profile representation warrants extension to the TRIDENT loops.
  - TAMU geometry and fluid, inherited hydraulic and exterior-boundary laws, prescribed cooler inputs, and numerical-refinement requirements limit direct transfer to other facilities.

- **Conditional wall and exterior-boundary studies.** Compare radial, regional, downcomer, and exterior-boundary representations using explicit fitted quantities, initialization scenarios, and regional errors.
  - Measured primary temperatures are supplied inputs; insulated-region shell response does not resolve every bare-patch contact sensor.

- VCU run-condition, boundary, regional-resistance, and downcomer comparisons provide further preliminary evidence. Their supplied temperatures and boundary assumptions must accompany any interpretation.
- Use the isolated TAMU developing-profile work as a mechanism/reduction benchmark with explicit transfer limits.
  - Distinguish temperatures associated with transported enthalpy, area-averaged density and buoyancy, and local probe response. Assess the thermal and hydraulic assumptions separately.



## Research Questions, Aims, and Staged Goals


### Framework contribution

- Develop and assess a CFD--experiment order-reduction framework that produces a fast, interpretable, physics-based reduced-order model (ROM).
- Use a custom physical 1D solver as the principal model; CFD and experiments inform reduction, closure selection, parameter learning, and assessment.
- Proposed aims: (1) reduction and development-informed closures; (2) parameter learning and observation-consistent temperature reconstruction; (3) independent assessment and applicability.
- Organizing question: what information and reduced physics are needed to reproduce observed temperatures and then predict new conditions with defensible uncertainty? Keep the development-case demonstration distinct from the independent predictive test.
- For each aim, define a target output, permitted inputs, comparator, and assessment evidence.
- **Closest prior methods and completed groundwork.** The closest work includes thermal-network structure/identification and physical interpretation, goal-oriented reduction/calibration/design, embedded discrepancy, conjugate/stochastic loop dynamics, conservative/stable learned reduction and similarity. [^1][^7]
  - Compare the proposed approach with existing thermal-network, goal-oriented, discrepancy, conjugate and stochastic, and structure-preserving methods, as well as completed preliminary modeling studies.

- **Candidate contributions.** Evaluate supported-target and anchoring analysis, finite-time retained-physics adequacy, qualified transfer, and the thermal consequences of local flow as possible contributions within the reduction framework.
  - For each candidate, specify the added-value claim, closest prior method, fair baseline, information requirements, failure test, and fallback. The dissertation need not pursue every branch.

- **Potential methodological advances.** Candidate outcomes include a reproducible development-informed reduction and closure rule, observation-consistent temperature reconstruction with an assessed domain, experiment--CFD parameter learning under shared uncertainty, or a qualified physical limit.
  - Test a precise closure/reconstruction/learning procedure or qualified applicability limit; use temperature/circulation/duty relevance rather than the novelty of software integration.

- **Method, procedure, physics and facility demonstration.** Method development supplies a new or meaningfully improved rule and shows why/when it works.
  - State which kind of contribution each work package would establish and what evidence separates it from implementation or a retrospective fit.

- **A useful negative result.** State a model or evidence class, a consequential ambiguity or adequacy boundary, and reproducible evidence that advances beyond established scale or rank limitations and prior preliminary findings.
  - A failed fit or unavailable CFD alone is insufficient; a negative result should identify a consequential limit on prediction or physical interpretation.



### Testable research hypotheses

- **Reduction and closure hypothesis.** At matched development data, online inputs, and calibration flexibility, a conservation-based model using justified development descriptors will improve selected withheld temperature predictions or identify an operating domain in which conventional closures are already adequate.
  - Evidence will include paired case comparisons, regional heat budgets, and numerical sensitivity. An improvement that depends only on more fitted parameters or target-informed boundary conditions will not isolate the value of the proposed closure rule.

- **Observation and learning hypothesis.** Explicitly representing the distinction among transported temperature, local fluid measurements, and wall or contact response will reduce structured residuals and improve the interpretation of learned parameters.
  - Compare a common bulk-temperature observation assumption with the proposed sensor-specific map under the same physical model and fitting cases. Assess both fitted residuals and eligible withheld predictions.
  - Where several parameter combinations remain compatible with the measurements, assess whether the engineering output is nevertheless constrained. Parameter uniqueness and useful prediction are separate questions. [^7][^15]

- **Retained-physics hypothesis.** Added wall storage, profile information, or local exchange is warranted when it improves an identified output under changed conditions and passes conservation, admissibility, and information-availability checks.
  - Test added mechanisms one at a time where feasible. A more detailed representation that cannot be learned or assessed with the available evidence will remain a bounded candidate rather than a claimed improvement.



### Aim-level evidence and expected products

- **Aim 1 --- conservative reduction and closure selection.** Produce an explicit mapping from qualified CFD and facility definitions to the retained states, signed transfers, closure candidates, and model equations. The product is a reproducible selection procedure and an assessed physical baseline.
- **Aim 2 --- parameter learning and observation-consistent reconstruction.** Produce supported parameter or parameter-combination estimates, temperature observation maps, and uncertainty descriptions using the experimental and computational information appropriate to each quantity.
- **Aim 3 --- independent assessment and applicability.** Produce comparisons on eligible unused cases, an output-specific applicability statement, and an operator-oriented example that communicates the model's qualified estimates or scenarios.
- Each aim will report what was supplied, learned, and predicted; which cases informed model development; the comparison that tests the proposed improvement; and the limitations that remain. This creates a common scientific basis across the steady, transition, and operational stages.


### Staged research goals

- Stage 1: steady heat removal/losses, circulation, temperature extrema and supported operating margins.
- Stage 2: transitions between operating conditions, thermal and hydraulic response, settling, and time-dependent margins.
- Stage 3: operational assistance and operator-facing model/data dashboard; collaborate with Ben Booth and NeutronOS. Controls and unattended operation need a separate agreed scope.
- Uncertainty estimation and propagation are central to all three stages.
- The immediate feasibility demonstration emphasizes experimental-data interpretation and temperature reproduction, building on the completed master's work.


### Spatial questions and boundaries

- Temperature first: centerline and radial profiles, with angular dependence where supported; richer velocity mapping is a later capability.
- Overall circulation and local recirculation are separate outputs; investigate local extent and thermal consequence with qualified CFD, without inventing local experimental measurements.


## Experimental and Computational Evidence


### Facility configuration, measurements, and power

- **Facility and case definition.** Record facility configuration, run and time window, channel mapping, candidate steady conditions, nominal and measured power, and the role of each case in calibration or assessment.
  - Keep alternative window-selection rules and facility-specific sensor mappings distinct. Nominal electrical generation is separate from measured net heat delivered to the fluid.

- For each facility list geometry revision, fluid, materials/insulation, heater/cooler boundaries, sensor meanings and uncertainties. Keep historical and current configurations distinct.
- Use explicitly versioned CAD and geometry records; retain historical and current configurations separately.
- VCU notes describe three mat and four band heaters; electrical input, deposition into solids/fluid, and net loop heat are different quantities. Use the accepted nominal dial-based specification where applicable and label its assumptions; metered electrical input and net fluid deposition remain separate evidence.
- Distinguish primary-fluid thermocouples, surface thermocouples, and fiber-optic measurements by facility and date. Historical exercises and current installations may use different sensor counts.
- Give every reusable case a record linking facility, geometry/property version, run/time window, channel/coordinate map, boundary histories, exclusions and uncertainty source. Link to original photos/drawings through their source note; do not copy dimensions from an unqualified picture.
- Track four power quantities separately: command/dial setting, electrical input, deposited heat and net control-volume duty. Record measured versus assumed values and source provenance. [^11]
- For exploratory VCU input calculations, assume nominal $20\,\Omega$ mat heaters and $48\,\Omega$ band heaters, with the transformer dial interpreted as loaded root-mean-square voltage: three parallel mat--band pairs and one remaining band. At equal settings $X$, $P_{\mathrm{nominal}}=(7/30)X^2$ W. This is a nominal electrical-input model; measured resistance and net thermal deposition remain separate quantities.
- Extra electrical characterization can improve confidence but is not a prerequisite to the accepted nominal calculation. Preserve run-specific settings/off events and source-to-solid/fluid storage/contact/loss accounting.


### From measurements to an experimental reproduction case

- The initial demonstration will trace one documented run from recorded channels to model observations before using it to estimate physical parameters. This establishes whether the temperature data, configuration, and forcing are understood well enough to support a model comparison.
  - Retain native timestamps, sampling intervals, units, and channel names. Apply only the calibration coefficients supported for that instrument and run; keep the original and corrected values distinguishable.
  - Map each channel to a physical location and sensing medium. Synchronize heating, cooler, ambient, and temperature histories without implying a timing precision beyond the records.
  - Summarize missing samples, changes in configuration, calibration limitations, and the windows used for statistics. A visually flat trace is not sufficient evidence that all fluid and solid storage terms are negligible.

- Estimate or bound the inputs available to the model: nominal or measured heater power, cooler conditions, ambient temperature, and initial fluid and solid states. Their evidence quality will enter the uncertainty and interpretation of the result.
- Fit a limited physical parameter set on a development case and plot measured and predicted temperatures on the same channel and time basis. Report channel bias, error magnitude, spatial pattern, and energy residuals alongside the fitted parameters.
  - A persistent regional pattern may indicate an omitted heat path, a boundary error, or an observation mismatch. Compare these explanations using the available configuration and measurement evidence rather than allowing an unrestricted residual correction to absorb the pattern.
  - After the reproduction choices are established, freeze their values and assessment rules before examining an eligible new condition. If all available cases have already informed development, report that history and seek genuinely new evidence for an independent test.



### Experiments and collaboration

- Align the experimental checkout and four-phase plan with configuration verification, noise and calibration, passive relaxation, energy anchoring, and controlled operating-condition assessment.
- Coordinate proposed experimental conditions and instrumentation requirements with Dr. Luciano and the experimental team.
- Freeze development, model-selection and assessment roles before fitting; supplied boundaries cannot also be scored as independent outputs.
- Phase 2 passive relaxation primarily supports response rates under its capacity/conductance assumptions. A Phase 3 case used to set an absolute energy scale becomes development evidence and cannot also remain blind assessment; preserve the original plan while recording a proposed role change.
- Document the experimental phase and version, available signals, target parameter or quantity of interest (QoI), supplied inputs, calibration or assessment role, and remaining limitations.
- **Smallest useful contrast set.** Select physically feasible contrasts from the existing experimental plan before proposing additional instruments or controls. [^13]
  - Compare feasible steady anchors, warm/cold relaxation, known-input holds/shutdowns and independent source/sink variation against the selected target and competing explanations.

- **Absolute heat scale and measurement planes.** Use either an independently supported deposited-duty/secondary-energy anchor at a steady condition or a justified inventory/capacity anchor, and propagate its uncertainty.
  - Distinguish measured and nominal electrical and secondary-side inputs, source partition, residual duty, and common biases. Preserve the nominal heater assumptions without treating them as measured heat delivered to the fluid.

- **Excitation, duration and sensor placement.** Choose durations and sampling from the modes/settling/event targets and their observation/initial-state uncertainties, not a universal number of time constants.
  - Justify rates/windows/repeats using bandwidth, thermal time scales, autocorrelation and conditioning; a stationary measured trace is not proof of negligible hidden storage.

- **Parameter information, target information and model discrimination.** Parameter design reduces supported parameter uncertainty; target design reduces uncertainty in a specified future quantity; discrimination separates competing model explanations; validation design selects evidence relevant to target-sensitive assumptions. [^13]
  - Compare actual feasible choices under nuisance/input uncertainty; report ranking sensitivity and computational cost rather than asserting a universal optimal experiment.

- **Value of extra measurements and honest fallback.** Retain assessable sensor/regional/duty predictions when evidence cannot distinguish all internal mechanisms.
  - Classify existing signals, feasible metadata, proposed instruments and CFD-only products; restrict only the unsupported claim when a desired measurement is unavailable.

- **Experiment-to-model alignment.** Relate checkout to the model and observation definition, repeatability to covariance, passive relaxation to rate ratios and hidden storage, energy anchors to absolute heat-loss scale, and controlled changes to response and applicability.
  - For each experimental phase, record the QoI, existing coverage, proposed changes, measurement location and bandwidth, timing, uncertainty, development or assessment role, and acceptance basis. Coordinate proposed amendments with the experimental team.



### CFD deliverable specification

- Jointly define steady cases, field/integral exports, signed section fluxes, conjugate budgets, development descriptors, temperature profiles and sensor footprints.
- Include units, geometry/property/boundary revisions, conservation and target-specific numerical sensitivity. Future transitions additionally require synchronized histories and initial-state information.
- **Fields, descriptors and qualified references.** Retain case metadata, velocity, temperature, pressure, properties, cell and face geometry, signed mass and enthalpy fluxes, source partition, interface and exterior heat rates, section profiles, and sensor footprints. Transitions additionally require synchronized physical time and initial storage.
  - Request the signed fields/integrals, source/geometry/boundary metadata and mesh/time sensitivities needed for the selected descriptor; withhold whole CFD cases for reconstruction tests.

- **TAMU applicability and levels of CFD access.** Qualify any TAMU reference by documenting geometry, fluid, boundary conditions, sensor operators, numerical verification, experimental validation, property conventions, and limitations before use.
  - Define demonstrations using thermal data only, limited CFD reference data, or qualified spatial fields; limit spatial and transfer claims to the evidence available in each case.

- **Experiment-to-CFD and CFD-to-ROM interfaces.** Operational inputs are boundaries, commands converted through source models, properties and allowed initial information.
  - Specify geometry/material/source histories and sensor operators in one direction, then conservative field/section/interface exports in the other; do not score imposed targets as predictions.

- **Verification at the actual local target.** Verify and assess the quantity actually claimed: profile/location/flux/extent needs its own resolution, threshold, plane and sampling checks.
  - Check local extent, heat flux and extrema separately from integrated duty; retain grid/time/regime/reference uncertainty and experimental validation distinctions.

- **Physical and numerical applicability of the CFD case.** Record regime and convention-specific Re/Pr/buoyancy measures, source and wall boundary conditions, geometry/reset/recovery, variable properties and conjugate fluid-solid times.
  - Qualify flow/thermal development, regime, buoyancy/gravity/pressure and conjugate-wall assumptions; do not select turbulence or laminar treatment merely for convenience.

- **Limited-CFD discrimination and no-CFD progress.** Prioritize cases that distinguish the conventional and proposed closure/reconstruction rules under the same online information: nominal conditions, source/sink contrast, property/development contrast and a weak-flow limit.
  - Choose a bounded set of independent contrasts with a declared comparator; continue data/steady/uncertainty work while limiting claims that truly require a spatial reference.



### Data lineage, quality and operating-condition groups

- Maintain a traceable data-to-model comparison record with consistent definitions and provenance.
  - Keep raw files and original timestamps/units unchanged; map native channels to physical sensors and model observations using explicit configuration, calibration and source-row identities.
  - Preserve mapped, synchronized, quality-flagged and accepted-window products as separate versioned transformations with parent IDs. Store measured statistics, CFD-reference quantities and model predictions with their distinct provenance and uncertainty.

- Group operating conditions by actual inputs and configuration, then report within-group variation and evidence coverage.
  - Group cases using source, sink, and environmental histories with justified tolerances.
  - Distinguish steady or transient classification, accepted statistical reporting windows, and physical energy equilibrium. Evaluate the consequences of alternative window-selection rules.

- Treat quality flags and exclusions as scientific choices requiring reasons and sensitivity checks.
  - Preserve flagged samples and assess genuine transients, autocorrelation, and channel roles before exclusion.
  - Record missingness, drift, calibration grouping and the effect of alternative window/channel policies; do not select a window because it minimizes the fitted-model residual.



### Power and thermal-boundary accounting

- The electrical input model and the thermal source model will be connected through an explicit heater control volume. For resistive elements under the stated voltage and resistance assumptions,

  $$
  P_{\mathrm{elec}}=\sum_j\frac{V_j^2}{R_j},\qquad
  P_{\mathrm{elec}}=\dot Q_{h\to p}+\dot Q_{h\to a}+\frac{dU_h}{dt}.
  $$

  Here $\dot Q_{h\to p}$ enters the pipe or modeled heated structure, $\dot Q_{h\to a}$ covers heater-to-environment losses within the chosen boundary, and $U_h$ is stored heater energy. Lead and support losses must be included in the declared boundary or separately accounted for.
- This accounting prevents a fitted thermal model from silently treating a dial setting as measured net fluid heating. It also distinguishes a steady deposition assumption from a transition in which heater and pipe storage matter.
- Cooler evidence will distinguish prescribed secondary inlet conditions, measured secondary heat removal, and a fitted equivalent boundary relation. Imposing a measured wall or primary-fluid temperature can support a conditional diagnosis, but that imposed quantity cannot also be scored as an independently predicted output.
- Regional ambient losses will retain the physical surface, insulation, contact, and support interpretation where supported. Effective residual terms will be reported with their fitted domain and sensitivity rather than relabeled as measured material properties. [^11]


## The Custom 1D Model and Observation Mapping


### Starting representation

- **Model hierarchy and numerical verification.** Compare stagnant, prescribed-flow, and coupled-circulation configurations using declared states, cooler representation, conservation residuals, and numerical sensitivity.
  - Numerical verification or a synthetic example does not establish facility accuracy.

- Divide the loop into axial cells with fluid, pipe and optional insulation temperatures; declare heater, cooler, ambient and axial/radial heat paths.
- Distinguish radial thermal diagnosis, a stagnant segmented loop, prescribed signed-flow transport, and coupled buoyancy--resistance circulation. These physical representations differ from an empirical regional response model.
- Define the governing balances, sign conventions, property choices, and conservation checks for the retained states.
- Use stored energy and signed enthalpy fluxes as the starting balance; evaluate each shared transfer once with opposite signs for adjacent volumes. Define state, units, positive loop direction and property temperature before presenting the reduced equations.
- For temperature-dependent heat capacity, obtain enthalpy differences by integrating $c_p(T)$ and distinguish fluid, pipe, and insulation storage. An algebraic steady circulation balance does not provide transient inertia.
- **State meanings across the physical hierarchy.** A lumped thermal resistance--capacitance model aggregates thermal storage/exchange; a segmented conjugate model retains fluid and wall/insulation and directional enthalpy; a regional grey-box model identifies effective storage/couplings; a 1D circulation model adds buoyancy/resistance and possibly inertia; a low-order spatial model retains profile/mode information.
  - Compare lumped/regional, segmented conjugate, circulating 1D and low-order spatial models by their actual states/equations and information requirements.

- **Retained storage and heat paths.** Retain paths that carry source, rejection, ambient loss, storage or transport relevant to the target.
  - Give each fluid/solid/insulation/source/support/cooler path an owner and sensitivity test; distinguish material properties from effective corrections.

- **Steady momentum, inertia and transport.** An algebraic steady momentum root supplies a circulation branch, not a transient stability result.
  - Treat steady circulation roots, transient momentum, and local counterflow separately; preserve signed-flow and zero-flow limits and identify the evidence needed for branch selection and stability.



### Governing balances and retained thermal states

- For each fixed control volume $i$, use stored sensible energy and signed transfers:

  $$
  \frac{dU_i}{dt}=\sum_{f\in\partial i}\dot H_{f\to i}
  +\dot Q_{s,i}+\sum_j\dot Q_{j\to i}-\dot Q_{i\to a}.
  $$

  $U_i$ is in joules and every right-hand term is in watts. A shared advective or conductive transfer is computed once and enters adjacent balances with opposite signs; only external sources, sinks, and storage remain in the summed loop balance.
- For a material with temperature-dependent heat capacity, define a compatible enthalpy law,

  $$
  h(T)-h(T_*)=\int_{T_*}^{T}c_p(\vartheta)\,d\vartheta.
  $$

  The approximation $h=c_p(T)T$ is not generally valid. Fluid and solid reference states and the selected low-Mach density and mass conventions will be stated consistently. [^3]
- The initial spatial model separates fluid, pipe, and optional insulation storage in axial cells. Interface heat exchange may take the restricted form $\dot Q_{f\to w}=G_{fw}(T_f-T_w)$ with $G_{fw}=h_c A_{fw}$, where $h_c$ is the heat-transfer coefficient on the declared area.
  - Cylindrical conduction, contact resistance, and exterior exchange enter distinct paths. For a constant-conductivity cylindrical layer of length $L$, $R=\ln(r_o/r_i)/(2\pi kL)$; multiple layers and contact terms must use compatible interfaces.
  - Radiation, if consequential, uses absolute temperature and an appropriate surface/view-factor model. A fitted exterior conductance may combine several paths and will be described as effective.
  - Adding wall states is established modeling practice. The proposed research concerns the supported selection and reduction of those states and paths for the intended predictions. [^6][^16][^17]

- Steady solutions require energy closure and a periodic fluid-temperature condition around the closed loop. Transition solutions additionally require physically interpretable initial fluid and solid energies; initialization is part of the prediction task, not a free fitting adjustment on the assessment case.


### Circulation and the distinction between steady and transient models

- In the steady circulating model, mass flow is selected by a signed balance between buoyant head and hydraulic losses. With positive coordinate $s$ around the loop and upward elevation $z$, a candidate transient extension under a consistent incompressible-inertia approximation is

  $$
  \begin{aligned}
  \mathcal I\frac{d\dot m}{dt}&=-g\oint\rho(T,s)\,dz-\Delta p_{\mathrm{loss}}(\dot m,T),
  &\mathcal I&=\oint\frac{ds}{A(s)},\\
  \Delta p_{\mathrm{loss}}&=\sum_j\left(f_{D,j}\frac{L_j}{D_{h,j}}+K_j\right)
  \frac{\dot m|\dot m|}{2\rho_j A_j^2}.
  \end{aligned}
  $$

  Both sides of the momentum balance have pressure units. The steady model sets the time derivative to zero; retaining this derivative is proposed transition-model development, not a statement that it is already implemented.
- The area, reference-density, Darcy-friction, local-loss, and property conventions will be declared. A spatially uniform mass-flow approximation with temperature-dependent buoyancy requires a compatible continuity and density treatment. [^16]
- A steady root does not establish transient stability or local recirculation. Assess root existence, sign, and sensitivity separately from temporal response; inspect multiple branches where the chosen model permits them.
- A correlation can match a steady heat-transfer value while giving a different response to changing flow. Transition assessment will therefore examine the retained storage and the sensitivity of heat transfer to operating state, in addition to the steady coefficient. [^17]


### Closures and observation operators

- Build on the closures tested in the preliminary study, characterizing hydraulic and thermal development before choosing transfer-law descriptors. Keep closure selection separate from sensor mapping.
- Compare bulk enthalpy, centerline/radial/angular fluid temperature and wall/contact sensor responses according to their distinct meanings.
- Test local-to-average mappings for conditioning, reference dependence, and conservation before adopting them as general closures.
- Write the observation model schematically as $y_k=H_k(x,u,\theta)+b_k+\varepsilon_k$: location/footprint and contact or filtering belong in $H_k$, shared calibration in $b_k$, and residual variation in $\varepsilon_k$. Choose those terms from evidence rather than inventing independent noise. [^11]
- If a proposed profile descriptor requires contemporaneous CFD or measured primary temperature, classify that result as conditional reconstruction. An autonomous forward closure must obtain its descriptors from the retained state and allowed inputs.
- **Bulk, area, transport and local temperature.** Point, centerline, wall and sensor-filtered temperatures need distinct operators. [^11]
  - State area/enthalpy/probe/wall meanings and test whether duty can remain correct while local extrema or buoyancy are wrong.

- **Sensor footprint, wall response and interpolation.** Apply interpolation, sensor footprint, contact conduction and response/timing in the forward observation operator before comparing predictions. [^11]
  - Specify sensing medium/depth/contact, node weights, response and calibration; identify evidence that distinguishes observation mismatch from transport inadequacy.

- **Development and correlation applicability.** Choose closures using hydraulic/thermal development, source and wall conditions, orientation, property variation, buoyancy and geometry. [^2]
  - Evaluate regime, property/entrance/bend and conjugate-wall assumptions before selecting heat-transfer coefficient and friction corrections; retain conventional-correlation comparators.



### Use-time information

- Steady forward prediction: prescribed operating inputs and qualified configuration predict withheld primary outputs.
- Startup-conditioned trajectories may use measured initial temperatures and supplied later ambient; label that information and do not call it an autonomous forecast.
- CFD-conditioned reconstruction, full-forward ROM prediction and later sensor-updated estimation need separate contracts and scores.
- **Input, observation and prediction contracts.** For steady prediction supply facility/revision, geometry and property laws, source deposition or a source model, cooler inlet/flow or an equivalent external boundary model, ambient and declared parameter uncertainty. [^12]
  - Write separate steady forward, initial-state-conditioned transition and supplied-primary diagnostic contracts; name allowed inputs, targets and forecast horizon.

- **Unobserved hot and cold locations.** Sparse observations alone do not determine arbitrary unobserved hot/cold spots. [^15]
  - Define the admissible profile/closure and boundary-support family; report a location, region or bound only at the resolution supported by observations/reference fields.



### Reproducible inputs and numerical choices

- Specify the model from resolved configuration through conservation outputs to observation predictions.
  - Declare geometry units, state order, property basis, source assignment, cooler form, axial/radial discretization and observation locations.
  - Record defaults and overrides, refinement, nonlinear tolerances and root-selection outcomes. Numerical parameters belong to verification/sensitivity, not physical calibration.

- Keep the three temperature roles explicit when evaluating developing-profile additions.
  - Transported enthalpy, area-density/buoyancy and local probe response need not share one temperature; test whether a low-order profile or covariance relation materially changes the target.
  - Historical local/mean temperature or pressure ratios are candidates; test reference dependence, small denominators and flux preservation before adopting them. Do not transfer TAMU coefficients or sensor meanings automatically.



### Conservation quantities and measurement quantities

- For a section with declared positive normal velocity $u_n$, extract

  $$
  \dot m=\int_A\rho u_n\,dA,\qquad
  \dot H=\int_A\rho u_n h(T)\,dA,\qquad
  \overline T_A=\frac{1}{A}\int_A T\,dA.
  $$

  Where net mass flow is well resolved, define $h_b=\dot H/\dot m$ and recover a transport temperature from the same enthalpy law. This temperature generally differs from an area mean, a centerline probe, and a wall contact.
- Near zero net flow or substantial countertransport, retain positive and negative stream fluxes rather than dividing by a poorly resolved net mass flow. Such cases test the limits of a single transported temperature and may motivate an additional state or a restricted applicability claim.
- The sensor model will map the retained state to the actual measurand:

  $$
  y_k(t)=\mathcal H_k[x(t),u(t);\eta]+b_k(t)+\varepsilon_k(t).
  $$

  Here $\eta$ includes supported position, contact, interpolation, and response conventions; $b_k$ represents shared or drifting bias and $\varepsilon_k$ residual measurement variation. A sensor-response time constant will be introduced only when instrument evidence or a controlled comparison supports it. [^11]
- Closure learning and observation reconstruction will use the same averaging definitions during development and assessment. Supplying contemporaneous CFD fields or measured primary temperatures to a map creates a conditional reconstruction; a forward predictor must obtain its descriptors from the retained state and permitted operating inputs.


## Theory Motivation and Research Methodology


### Closest prior methods and why these choices

- Compare conservation-based and developing-flow reduction, closure identification, observation reconstruction, parameter learning, uncertainty quantification, and validation methods.
- Explain each chosen method's role, required information and failure limit; keep derivation details in appendices or linked sources.
- Identifiability/profile tools support physical interpretation; neither generic fitting nor ordinary scale ambiguity is itself a new contribution. [^7]
- Use the completed master's work as the nearest project baseline, including its negative tests, prior case exposure, and heat-path discrepancies. Additional wall storage or another fitted state alone does not establish a methodological contribution. [^1]
- **Choice of reduction method.** Aggregation gives interpretable compartments; Proper orthogonal decomposition (POD) prioritizes snapshot reconstruction in a chosen norm; balanced methods incorporate input-output behavior; goal-oriented methods target a functional; nonlinear manifolds address nonlinear state representation; constrained methods preserve declared structure.
  - Explain what POD, balanced/goal-oriented, manifold and structure-preserving alternatives optimize and require; select only branches supported by the intended data.



### Position relative to established loop modeling

- Existing loop studies already retain conjugate fluid and wall energy, nonuniform geometry, heat losses, and coupled circulation. Borgohain et al. provide a liquid-metal example with separate fluid/wall balances and experimentally informed cooler and ambient-loss relations; those liquid-metal coefficients are not transferred to the salt or glycol loops. [^16]
- Cammi et al. examine wall thermal inertia, internal and external source distributions, and stability. Their work establishes that source placement and wall dynamics can affect response; it does not establish a universal stabilizing effect or a TRIDENT-specific closure. [^17]
- These precedents make the research gap more specific than building a thermal network or fitting a heat-loss coefficient. The proposed work will assess a procedure linking physical reduction, development descriptors, sensor-consistent inference, and independent engineering-output assessment.
- The completed TAMU study supplies the nearest project baseline and a reason for this integrated assessment: thermal and hydraulic fits can favor different parameter settings, and lower temperature error can coexist with an incorrect regional heat-removal distribution. [^1]


### Aim 1: reduction and closure selection

- Declare control volumes, retained states, conventional baseline and closure inventory.
- Derive descriptors from consistent CFD budgets; require descriptors needed at prediction time to be available from ROM states and prescribed inputs.
- Change transfer/hydraulic assumptions in controlled comparisons to attribute improvement rather than merely adding fitted freedom.
- **Operations that constitute reduction.** Declare separately the aggregation from fields to conserved quantities, elimination/lumping of states, projection onto a basis/manifold, closure of unresolved transport and reconstruction to observations/fields.
  - Write the aggregation, state elimination/projection, unresolved-transport closure and reconstruction operators separately; identify which one is the proposed methodological advance.

- **Development-conditioned closures and observation maps.** Paired interface heat rates, signed enthalpy fluxes, and cross-sectional temperature and velocity information can support development-conditioned transfer closures and sensor or profile maps.
  - Require online descriptors to come from retained states/allowed inputs; assess separately any map supplied with contemporaneous CFD fields.

- **Closure correction versus added states or physics.** First verify geometry, source/sink accounting and observation operators, then compare closure correction and state enrichment under the same data and nuisance flexibility.
  - Use controlled model-form comparisons and local budgets to distinguish poor calibration from missing structure; do not fit away wrong geometry or boundary assumptions.

- **Conservation and admissibility.** Use shared face enthalpy fluxes and paired internal exchanges, positive capacities, admissible conductances and consistent signed flow.
  - Check paired internal transfers, uniform equilibrium, positive capacities/temperature and signed transport separately; derive suitable ports/storage before invoking passivity.



### Aim 1 work sequence and closure candidates

- **Construct the common reference.** Integrate CFD fields over the same sections, interfaces, source regions, and averaging windows used to define the reduced model. Check source totals, paired interface transfers, section mass flux, and the residual in each regional energy budget.
- **Establish the conventional comparator.** Use the same geometry, property families, boundaries, sensor operators, and small calibration set with conventional friction and heat-transfer relations valid in their declared regimes.
- **Build candidate descriptors.** Begin with Reynolds number, Prandtl number, axial location relative to a fitting or thermal boundary change, property variation, and selected profile moments. For example,

  $$
  \mathrm{Re}=\frac{|\dot m|D_h}{A\mu},\qquad
  \mathrm{Pr}=\frac{\mu c_p}{k_f},\qquad
  \mathrm{Nu}=\frac{h_cD_h}{k_f}.
  $$

  Reference temperatures, characteristic lengths, and the distinction between mean flow and local reverse transport will be specified for each use.
- **Learn the smallest supported correction.** Compare an effective transfer or hydraulic correction with a richer profile or state representation only when the latter addresses a documented residual or target sensitivity. Constrain shared exchanges, positive storage, and physically admissible transport.
- **Test the selection rule.** Withhold whole CFD cases or conditions for reconstruction and closure assessment. Report the effect on sensor temperatures, circulation, regional heat rates, and computational cost, retaining failures as evidence about the rule's domain.
- **Expected product.** A documented reduction procedure and closure inventory with required inputs, applicability range, training and assessment cases, conservation checks, and an explanation of the improvement or adequacy limit attributed to each changed modeling decision.


### Aim 2: learning and reconstruction

- Learn only supported physical parameters/combinations from development experiments; carry uncertain power, properties, calibration and observations jointly.
- Test centerline/radial temperature and regional heat transport separately; assess ambiguity and thermal consequences of spatial structure.
- Distinguish physically identified closures, observation correction, and empirical discrepancy. Select a machine-learning architecture only when it addresses a documented limitation.
- Apply the data-understanding demonstration first: reconcile labels, units, installed sensor meaning and supplied inputs before optimizing parameters. Diagnose persistent spatial residual patterns instead of allowing one fitted loss to absorb every mismatch.
- Compare parameter combinations and output sensitivity over justified nuisance ranges; a well-matched trace does not establish unique conductance, capacity, deposited power or local heat-transfer interpretation. [^7]
- **Supported parameters versus a good fit.** Use exact invariance/structural analysis for a specified model, local sensitivity/Fisher information for local practical support, nuisance-reoptimized profile likelihood for nonelliptic ambiguity, posterior geometry for prior-conditioned uncertainty and synthetic recovery for implementation/information checks. [^7]
  - Use invariance, sensitivity/Fisher rank, nuisance-reoptimized profiles, posterior geometry and synthetic recovery for their distinct purposes; report target/combination support.

- **Absolute energy scale and sequential learning.** For passive C dT/dt = -G(T-Ta), common positive scaling of C and G leaves the trajectory unchanged; only G/C is fixed.
  - State which measured-duty or inventory datum anchors scale; propagate that uncertainty and compare sequential steady/dynamic learning with joint inference when they share uncertain quantities.

- **Hidden initial states and residual duty.** Initial wall/insulation states, hidden fluid-solid splits, residual heater/cooler duty and changing heat paths can mimic a capacity or time constant.
  - Use common initial-state information and bounded hidden-solid participation; do not grant a richer model target-informed starts or identify every observed lag as material capacity.

- **Constrained fits, priors and effective parameters.** Begin with a constrained covariance-aware physical fit and profiles. [^14]
  - Compare deterministic/regularized and probabilistic alternatives where needed; report when a fitted group is predictive but cannot retain a unique physical interpretation.



### Aim 2 work sequence and inference problem

- Define a small parameter vector $\theta$ for supported heat paths, transfer relations, or hydraulic terms, and nuisance quantities $\eta$ for uncertain power, properties, calibration, boundaries, and initial states. Parameters and nuisance quantities will be shared across cases only where a common physical or calibration basis is justified.
- For the stacked observation residual $r(\theta,\eta)=y-\widehat y(\theta,\eta)$, a starting constrained objective is

  $$
  J(\theta,\eta)=r^T\Sigma^{-1}r+\mathcal R(\theta,\eta),
  \qquad (\theta,\eta)\in\mathcal A.
  $$

  $\Sigma$ represents the justified residual dependence, $\mathcal A$ the admissible parameter and nuisance set, and $\mathcal R$ any stated regularization or prior information. Uncertain inputs may be estimated jointly, profiled, or propagated; the same uncertainty will not be counted twice through multiple representations. [^7][^14]
- Use sensitivity and synthetic recovery to inspect implementation and practical support, then reoptimize nuisance quantities when profiling a parameter or target. Report whether the data support a physical coefficient, a combination of coefficients, or only a prediction interval.
- Assess observation maps independently where paired CFD fields are available: first reconstruct sensor or profile quantities from the reduced state, then test the complete forward model. This distinguishes reconstruction error from closure and boundary error.
- **Expected product.** A reproducible parameter-learning and temperature-reconstruction workflow, with supported quantities, uncertainty and dependence, evidence limits, and a comparison against the simpler observation and fitting assumptions.


### A worked identifiability example for experiment selection

- Consider the restricted single-capacity model $C\dot T=P-G(T-T_a)$ with constant $C$, $G$, and ambient $T_a$. Passive relaxation after power removal gives

  $$
  T(t)-T_a=[T(0)-T_a]\exp(-t/\tau),\qquad \tau=C/G.
  $$

  Relaxation alone constrains a rate ratio; it does not determine both absolute heat capacity and conductance.
- At a compatible steady state with a known deposited power, $G=P/(T_{\mathrm{ss}}-T_a)$ and $C=G\tau$. If deposited power is also unknown, a common scaling of $C$, $G$, and $P$ leaves the temperature response unchanged. An uncertain power anchor therefore limits the absolute energy scale even when the temperature fit is excellent.
- The actual loop has distributed and potentially hidden solid storage, changing boundaries, and several heat paths. The example motivates complementary relaxation and energy-anchor experiments; it does not justify assigning every observed time constant to a material capacity. [^7]


### Aim 3: fair comparisons

- Compare a fixed-closure physical baseline, proposed framework and modest data-driven predictor under matched development cases and use-time information.
- Freeze cases/conditions and scoring rules before final assessment; distinguish emulator accuracy from facility prediction.
- For transition comparisons hold boundary/initial-state information and refitting opportunities common; score response/settling before promising full transient fields.
- Report two explicit products: temperature reproduction on the development cases and prediction on eligible unused cases. Maintain the same sensor policy, input information and parameter-refitting opportunities for every comparator.
- **Strong physical and modest data-driven baselines.** Use a small fixed-correlation physical model with ordinary covariance-aware parameter learning as the serious baseline; compare the reduction/closure framework under matched information and a modest regularized response surface or GP.
  - Use a fixed-correlation physical model, small grouped-parameter alternative and modest predictor; add projection/operator/learned alternatives only for a named limitation.

- **The smallest informative model comparison.** Physical networks need geometry/properties and a limited parameter set; they are interpretable but can be nonidentifiable.
  - Compare data access, cost, interpretability, constraints, uncertainty and extrapolation at matched information; state a failure condition for every selected family.

- **Development, selection and final assessment roles.** Hold out whole cases, regimes or geometries according to the intended generalization claim.
  - Split by physical run/case/condition and record exposure/refitting history; do not use random time-point splits as evidence of independent physical generalization.



### Aim 3 work sequence and attribution

- Select assessment cases by the generalization claim: a new run at similar conditions, a changed heater or cooler input, a different mean-temperature or property range, or a qualified facility/geometry transfer. These tests make different claims and will be reported separately.
- Compare the conventional physical model, the proposed model, and a modest empirical predictor under common input information and development cases. Record the parameter count, offline learning cost, online solution cost, and any refitting permitted for each model.
- Use controlled changes to attribute improvement: closure change with a fixed observation map, observation-map change with fixed physical structure, and state enrichment with matched parameter and nuisance opportunities. Inspect local budgets as well as aggregate errors.
- Retain a simpler adequate model when added complexity offers no consequential gain. When every candidate fails, distinguish a missing observation, a boundary or configuration error, a numerical issue, and unsupported physical structure before proposing further experiments or CFD.
- **Expected product.** An assessment package that links case-level performance and uncertainty to a stated use domain, with an explanation of which reduction decisions earned their cost and which remain unsupported. [^15]


### Physical learning, observation mapping and residual correction

- Compare three distinct interventions instead of treating every improvement as a generic bias correction.
  - Physical learning: supported heat-path, transfer or hydraulic parameters change the conservative model and must retain an interpretable evidence basis.
  - Observation mapping: convert the reduced state to the actual probe/contact/fiber response; missing sensor physics is separate from the energy or momentum closure.
  - Residual correction: an empirical discrepancy model may improve a declared output, but its fit does not validate local heat-transfer or flow physics.

- Assess both the uncorrected physical model and the corrected alternative across conditions.
  - Compare residual size, spatial/operating-condition structure, physical budgets, uncertainty and runtime at common inputs and refitting opportunities.
  - Test interpolation and out-of-condition behavior separately; a smooth correction or shrinking training bias is not independent predictive evidence.

- Choose temporal or machine-learning complexity only when it addresses a documented limitation.
  - Start with physical/linear or modest data-driven references. GNN, LSTM, neural operators and richer field emulators remain candidate branches rather than required architectures.
  - Declare whether recent histories estimate the current state, forecast a later state, reconstruct supplied reference fields or update parameters; score those tasks separately.

- **Separate boundary, observation and structural error.** Boundary, parameter, sensor and structural errors can produce the same residuals. [^15]
  - Use independent anchors and residual/case contrasts to test competing explanations; a flexible discrepancy must not conceal omitted heat paths or unsupported target sensitivity.

- **Experiment--CFD fusion without double counting.** Use separate CFD and experimental observation/error operators with shared physical parameters only where appropriate. [^15]
  - Give each fidelity its own observation/error operator; track shared measured boundaries and calibrations, and disclose modular versus joint-inference assumptions.



### Local flow descriptors and thermal consequences

- **Definition of local recirculation extent.** Use section-normal signed velocity to define reverse area/transport fractions, and a declared region/connectivity convention for cell extent, separation/reattachment or exchange.
  - Define section normal/frame, reverse area/transport and connectivity/persistence conventions; distinguish local backflow, a closed cell and loop reversal.

- **Thermal consequences without a singular heat-transfer coefficient.** Prefer regional/interface heat rates, enthalpy redistribution, thermal asymmetry and fluid and wall extrema with a common boundary contract.
  - Compare regional heat rate, signed enthalpy redistribution and temperature asymmetry; report the heat-transfer coefficient only where its area/averaging/driving-temperature normalization is resolved.

- **Attribution rather than correlation.** Match source/sink histories, geometry, property range, net circulation or its declared control, and development information where feasible; change one representation/mechanism in a controlled model contrast.
  - Hold geometry, source/sink/property conditions and declared flow control common; state all effects changed by a CFD intervention before giving a causal interpretation.

- **Minimal representation of the consequential spatial effect.** Begin with one-stream conservation and a section loss/thermal closure; add a temperature reconstruction if the target is profile/observation mismatch.
  - Compare an effective closure, two-zone exchange, local correction and richer reconstruction only against a declared thermal target and complexity/cost criterion.

- **What sparse thermal data cannot identify.** Sparse bulk/wall temperatures constrain combinations of heat paths and transport under a selected model, not arbitrary velocity fields. [^15]
  - Construct observation-consistent alternatives to expose nonunique flow structure; assess thermal consequences without claiming direct experimental validation of local extent.



## Assessment, Uncertainty, and Applicability


### Verification and independent evidence

- Check ROM conservation and numerical sensitivity; qualify CFD reference uncertainty separately from experimental calibration and validation.
- Assess temperatures, circulation, duty, loss budgets, spatial reconstruction and cost separately, with engineering units and location/time meanings.
- Qualify ACU flow evidence; CFD flow at VCU is an uncertain reference, not direct experimental circulation validation.
- Temperature report: residuals in K by channel/location, channel-wise bias and RMSE, and declared time/space aggregation; report flow/duty and local heat budgets separately. Retain excluded channels with reasons and a sensitivity route.
- Use the same case names and configuration versions from source data through reduction, calibration, plotting and proposal claims. A figure caption should state whether each series is measured, CFD-referenced, calibrated or independently predicted.
- **Numerical reference error versus model discrepancy.** Estimate numerical sensitivity/error for the actual target using spatial, temporal, modal and sampling/extraction checks.
  - Qualify target-specific solver/CFD uncertainty and avoid counting the same residual twice; prioritize new evidence by consequential sensitivity rather than convenience.



### Uncertainty throughout

- Carry primitive calibration/channel, power/deposition, boundary, property, geometry and initial-state uncertainties with shared dependencies.
- Derived duty/flow inherit their ingredients; do not count them again as independent observations.
- Distinguish measurement variability, installed accuracy, model discrepancy and numerical uncertainty. Propagate through steady and transition outputs.
- Use covariance-aware propagation when a local linear approximation is justified; reuse common calibration, property and input variables wherever they appear. Joint input sampling must preserve those same dependencies. [^10][^11]
- Separate a scenario envelope, parameter interval and predictive interval; assess uncertainty against the intended output and available case count. Do not turn a few temperature comparisons into a calibrated rare-event probability.
- **Primitive uncertainty and dependence budget.** Start from primitive sources: shared calibration references/coefficient errors; channel noise, installation/drift/time; geometry/material/property laws; deposited power and secondary/ambient boundaries; hidden initial states; learned parameters/closure families; numerical error and CFD/reference inadequacy; and transfer distortion. [^11]
  - Populate calibration/channel/time, geometry/property/input, initial-state, parameter, numerical/reference and discrepancy components; leave unknowns explicit rather than assigning zero variance.

- **Propagation method and nonlinear failure limits.** Use linear covariance propagation for locally smooth, well-conditioned mappings and joint Monte Carlo for the primary nonlinear parameter/boundary/discrepancy propagation. [^10]
  - Compare local covariance and joint sampling on selected targets; justify any acceleration by dimension/smoothness/cost and check reversal/event/small-denominator behavior.

- **Shared instruments and derived outputs.** Compute secondary duty, loss allocation and inferred primary flow from one shared set of primitive draws/covariances. [^10][^11]
  - Reuse the same uncertain primitive wherever it appears in duty, flow or margins; retain temporal/channel dependence and distinguish repeatability from installed prediction accuracy.

- **Physical constraints for uncertain operators.** Parameterize or constrain positive capacities/conductances and paired exchanges; use energy-consistent signed fluxes and declared closure domains.
  - Check admissibility for individual parameter/closure draws; a stable mean operator does not establish stability, conservation or physical branch behavior for every realization.

- **Real-time inverse acceleration and its limits.** A candidate acceleration approach separates nonlinear parameter dependence from linear inversion variables and uses a reduced inverse representation.
  - Test whether the proposed nonlinear--linear factorization fits the actual inverse variables and hidden states before considering it as an optional acceleration method.



### Acceptance and limits

- Define each target, reference, metric, acceptance tolerance, and runtime requirement from its intended engineering use and the available evidence.
- Sensor minima/maxima and model-inferred spatial extrema require different evidence; freezing/temperature margins require a sourced threshold.
- Discriminate physics, input, observation and numerical explanations for disagreement; report a simpler adequate domain or a supported measurement need when warranted.
- Report local recirculation inference limits separately from bulk prediction and thermal-consequence evidence.
- **Decision tolerance, measurement resolution and numerical error.** Set operating usefulness from a declared decision or margin, measurement distinguishability from its joint uncertainty, and numerical adequacy from target-specific solver error.
  - Keep engineering acceptance symbols separate from sensor uncertainty, steadiness thresholds and solver tolerances; populate values only with a stated intended-use basis.

- **What uncertainty calibration would mean.** Report prediction error/bias, residual structure, interval width and proper predictive scores on whole independent cases. [^15]
  - Label scenario, confidence, credible and predictive intervals; assess bias, interval width and coverage/proper scores only at the independent-case scale the evidence supports.

- **Extrema, crossing and settling uncertainty.** Propagate joint state/closure/input/reference uncertainty into the complete extremum or event functional, not separate independent point bands.
  - Propagate joint uncertainty through the whole spatial/time functional; retain no-crossing possibilities, competing extrema and unsupported-location bounds.



### Sensor changes and adequacy of the available information

- Assess sensor reliability, sensor loss, and evolving installation or material conditions as bounded extensions of the assessment.
  - Compare full and reduced sensor sets at matched inputs and fitting access; quantify the resulting loss of temperature/target accuracy and uncertainty.
  - Record calibration/drift, sensor movement, thermal expansion or changing losses as competing explanations only where evidence supports them. A mismatch is not automatically a failed sensor.

- Connect a residual pattern to an evidence request before promising diagnosis or operator advice.
  - Separate input error, observation error, numerical error and model inadequacy; identify which existing or proposed measurement could distinguish them.
  - Keep ACU and VCU evidence separate. Similar processing or shared code does not make their configurations, calibration or validation interchangeable.



### Metrics and assessment products

- For temperature channel $k$ and declared comparison samples $n$, report bias and root-mean-square error in kelvin,

  $$
  \mathrm{RMSE}_k=\left[\frac{1}{N_k}\sum_{n=1}^{N_k}
  \bigl(\widehat y_{k,n}-y_{k,n}\bigr)^2\right]^{1/2}.
  $$

  Retain the channel and case results before aggregation. Dense sampling from one run will not be treated as an equivalent number of independent operating conditions.
- Report circulation, cooler duty, regional heat rates, and conservation residuals on their own measurement or reference bases. An output inferred from the same temperatures used for fitting will retain that shared provenance and covariance.
- For transitions, compare response and settling under declared input changes, initial-state information, and sampling. If a threshold crossing or spatial extremum is a target, assess its location or time resolution and the sensitivity to the chosen threshold or interpolation.
- Runtime assessment will distinguish the forward solve from offline CFD generation, extraction, and parameter learning. Report the hardware and problem size with the timing; assess numerical error at the resolution used for the performance claim.
- Present an output-specific applicability summary: operating and property range, boundary and initial information, observation coverage, assessed error and uncertainty, known failure modes, and the evidence supporting any transfer. Numerical tolerances and engineering acceptance targets will have separate stated bases.


### Joint uncertainty propagation and credibility

- Let $z$ collect the primitive uncertain measurements, inputs, property coefficients, geometry, initial states, and learned quantities appropriate to the selected inference formulation. For a locally smooth output map $q=f(z)$,

  $$
  U_q\simeq J_f U_z J_f^T,\qquad J_f=\frac{\partial f}{\partial z}.
  $$

  Shared calibration and property effects enter as shared variables or covariance, not independent copies. [^10][^11]
- Use joint sampling when nonlinearity, small driving differences, branch changes, or event definitions make local propagation inadequate. Each sample must reuse the same power, calibration, and property realization wherever that quantity appears.
- Report uncertainty sources that cannot yet be quantified, rather than assigning them zero variance. Separate numerical propagation convergence from evidence that the model and uncertainty description are adequate.
- Compare residual bias and structure, interval width, and predictive performance on whole eligible assessment cases. A confidence or parameter interval, a scenario envelope, and a predictive interval will be labeled according to the quantity they represent; finite-case coverage will not be presented as a calibrated rare-event probability. [^15]


## Work Plan and Deliverables


### Sequence and deliverables

- Begin with a documented experimental reproduction case, a declared prediction task, and matched physical and statistical comparators.
- Stage 1 deliverables: verified 1D specification, closure/observation procedure, steady predictions, uncertainty and applicability assessment.
- Stage 2 deliverables: qualified transition comparisons and response/settling/margin outputs, with physical-time and initial-state evidence.
- Stage 3 deliverables: operator interfaces for what-if questions and limit awareness, with Ben Booth and NeutronOS; distinguish interface prototype from assessed predictive functions.
- The initial demonstration will contain a case summary, temperature and channel map, declared boundary conditions and assumptions, reproduction plots, residual tables, conservation checks, and an uncertainty summary. Report calibration and assessment roles explicitly.


### From offline comparisons to operator-facing results

- **Uncertainty and operator interfaces.** Develop a source and covariance budget and a replay example that records provenance, forecast horizon, unavailable inputs, and applicability.
  - Requirement/interface development is distinct from implemented total uncertainty quantification, deployed decision support, control or independent facility assessment.

- Define traceable result interfaces and integration responsibilities.
  - Associate every result with model/case/data/configuration identity, source versions and parent transformations; preserve a route back to measured and reference inputs.
  - Agree result schemas and responsibilities with Ben Booth and NeutronOS before selecting a deployment architecture.

- Stage integration from offline reproduction to qualified replay and, where agreed, live data/model display.
  - Display measured, inferred and predicted quantities distinctly, with units, time/horizon, scenario, uncertainty or unknowns, applicability and stale/missing-data status.
  - Assess model predictions separately from display/communication functionality. Operator suggestions, alarms with authority, automated commands and unattended operation need separate scope and evidence.

- **Actionable estimate, diagnosis and forecast.** Present measured-location current temperatures/margins, a state estimate conditioned on data, a scenario forecast and conditional diagnosis as different products. [^12]
  - Label measured current margin, data-conditioned state estimate, scenario prediction and supplied-boundary diagnosis separately; state what is useful before a full transient model exists.

- **Communicate uncertainty and absent information.** Show target, units, source time/facility revision, scenario/horizon, uncertainty type, domain and missing/stale inputs. [^12]
  - Require units, scenario/horizon, provenance, applicability and stale/missing/out-of-domain flags; separate scientific credibility from interface polish.

- **Collaborative result/data contract.** Discuss facility/configuration ID, clock and sampling, quantity/state/observation identity, units and reference conventions, raw versus corrected provenance, scenario/forcing/horizon, parameter/model version, uncertainty/dependencies, applicability flags, stale/missing-data behavior and threshold ownership with Ben Booth/NeutronOS. [^12]
  - Define facility/revision, clock, input scenario, prediction horizon, uncertainty and threshold ownership jointly with Ben Booth/NeutronOS; infer neither product stack nor deployment readiness.

- **Later operating capabilities and added physics.** Startup/shutdown forecasting needs appropriate source history, fluid/solid initial states, transport and possible inertia.
  - Map startup/shutdown, pressure/level, trace heating and freezing questions to required states/data; distinguish sensible-temperature margin from phase change/blockage and advice from control.



### Research progression and decision gates

- **Establish experimental reproduction.** Complete one traceable case from raw channels through observation mapping, input accounting, a constrained fit, residual plots, conservation checks, and a documented uncertainty budget. This is the first feasibility demonstration.
- **Freeze and assess the steady model.** Select the physical model and calibration rule before examining an eligible unused condition. Assess the intended temperature outputs and the independently supportable flow and duty quantities; revise the applicability statement when a test fails.
- **Evaluate the reduction and closure procedure.** Use qualified CFD and experimental contrasts to test the selected development descriptors, observation reconstruction, and parameter groups. Retain the conventional comparator throughout so that improvement is attributable to an explicit modeling choice.
- **Extend to bounded transitions.** Add only the storage, momentum, or observation dynamics required by the chosen transition target, with synchronized boundary histories and defensible initial-state information. Compare temperature response and settling before claiming richer transient fields.
- **Demonstrate operational use.** Progress from an assessed offline scenario to recorded-data replay and, where supported by the collaboration, live result display. The demonstration will distinguish measured values, inferred states, and forecasts, and show uncertainty, applicability, and missing or stale data. [^12]
- Each progression step has an evidence gate rather than an assumed success. Missing CFD fields limit spatial claims; missing independent flow evidence limits circulation-validation claims; incomplete transition inputs limit forecasting claims. Data reconciliation, steady modeling, and supported temperature assessment can still advance while those dependencies are resolved.


### Expected dissertation outcomes

- A reproducible experimental/CFD-to-1D reduction framework with explicit conservation, closure, and sensor-mapping conventions.
- Evidence identifying which model states, parameter combinations, and profile corrections are consequential and supportable for selected loop-temperature and heat-transport predictions.
- Assessment of steady performance and bounded transitions, including uncertainty and limits on physical interpretation and transfer.
- An operator-oriented example showing how qualified model outputs can support scenario comparison and thermal-limit awareness, together with the conditions under which those outputs should be withheld or qualified.
- Reusable case definitions, extraction and comparison procedures, and research records that allow subsequent results to be extended and checked without losing their original evidence basis.


## References

[^1]: A. N. Fierro Lopez, *CFD-to-1D Model Reduction for Molten-Salt Natural-Circulation Loops: Local Closure Identification and Retrospective Model Assessment*, Master's thesis, Computational Science, Engineering, and Mathematics, The University of Texas at Austin, August 2026.

[^2]: J. Reis, J. Seo, and Y. Hassan, “Molten Salt Flow Visualization to Characterize Boundary Layer Behavior and Heat Transfer in a Natural Circulation Loop,” *Physics of Fluids*, 36, 033605 (2024).

[^3]: M. S. Sohal, M. A. Ebner, P. Sabharwall, and P. Sharpe, “Engineering Database of Liquid Salt Thermophysical and Thermochemical Properties,” Idaho National Laboratory Report INL/EXT-10-18297, Idaho Falls, ID, USA (2010).

[^4]: Y. Jin, J. Cheng, X. An, T. Su, P. Zhang, and Z. Li, “Accurate viscosity measurement of nitrates/nitrites salts for concentrated solar power,” *Solar Energy*, 137, pp. 385--392 (2016). DOI: <https://doi.org/10.1016/j.solener.2016.08.015>.

[^5]: D. R. Parida and S. Basu, “On the specific heat capacity of HITEC-salt nanocomposites for concentrated solar power applications,” *RSC Advances*, 13, pp. 5496--5508 (2023). DOI: <https://doi.org/10.1039/D2RA07384F>.

[^6]: A. Dass and S. Gedupudi, “1-D modelling and CFD study of the transient behaviour of a single phase Coupled Natural Circulation Loop,” arXiv:1804.10051 (2018).

[^7]: A. Raue, C. Kreutz, T. Maiwald, J. Bachmann, M. Schilling, U. Klingmüller, and J. Timmer, “Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood,” *Bioinformatics*, 25(15), pp. 1923--1929 (2009). DOI: <https://doi.org/10.1093/bioinformatics/btp358>.

[^8]: N. R. Brown, D. J. Diamond, S. Bajorek, and R. Denning, “Thermal-Hydraulic and Neutronic Phenomena Important in Modeling and Simulation of Liquid-Fuel Molten Salt Reactors,” *Nuclear Technology*, 206(2), pp. 322--338 (2020). DOI: <https://doi.org/10.1080/00295450.2019.1590077>.

[^9]: C. H. Gabbard, *Reactor Power Measurement and Heat Transfer Performance in the Molten Salt Reactor Experiment*, ORNL-TM-3002, May 1970. OSTI 4157686.

[^10]: JCGM, *Evaluation of measurement data---Supplement 2 to the GUM---Extension to any number of output quantities*, JCGM 102:2011. DOI: <https://doi.org/10.59161/JCGM102-2011>.

[^11]: JCGM, *Guide to the expression of uncertainty in measurement---Part 6: Developing and using measurement models*, JCGM GUM-6:2020. DOI: <https://doi.org/10.59161/JCGMGUM-6-2020>.

[^12]: M. G. Kapteyn, J. V. R. Pretorius, and K. E. Willcox, “A probabilistic graphical model foundation for enabling predictive digital twins at scale,” *Nature Computational Science*, 1, pp. 337--347 (2021). DOI: <https://doi.org/10.1038/s43588-021-00069-0>.

[^13]: S. Zhong, W. Shen, T. Catanach, and X. Huan, “Goal-Oriented Bayesian Optimal Experimental Design for Nonlinear Models Using Markov Chain Monte Carlo,” arXiv:2403.18072v2 (2025).

[^14]: N. R. Kristensen, H. Madsen, and S. B. Jørgensen, “Parameter estimation in stochastic grey-box models,” *Automatica*, 40(2), pp. 225--237 (2004). DOI: <https://doi.org/10.1016/j.automatica.2003.10.001>.

[^15]: T. A. Oliver, G. Terejanu, C. S. Simmons, and R. D. Moser, “Validating predictions of unobserved quantities,” arXiv:1404.7555v1 (2014).

[^16]: A. Borgohain, B. K. Jaiswal, N. K. Maheshwari, P. K. Vijayan, D. Saha, and R. K. Sinha, “Natural circulation studies in a lead bismuth eutectic loop,” *Progress in Nuclear Energy*, 53(4), pp. 308--319 (2011). DOI: <https://doi.org/10.1016/j.pnucene.2010.10.004>.

[^17]: A. Cammi, L. Luzzi, and A. Pini, “The influence of the wall thermal inertia over a single-phase natural convection loop with internally heated fluids,” *Chemical Engineering Science*, 153, pp. 411--433 (2016). DOI: <https://doi.org/10.1016/j.ces.2016.06.060>.
