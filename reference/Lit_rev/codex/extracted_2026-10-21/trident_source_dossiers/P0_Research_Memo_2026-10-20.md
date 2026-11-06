> **New evidence update:** S10 and S48 now have scoped full-document dossiers, and original Nick Phase0–4 protocols are available. Read [New_Batch_Synthesis_2026-10-20.md](New_Batch_Synthesis_2026-10-20.md) and [Nick_Plan_Reconciliation_2026-10-20.md](Nick_Plan_Reconciliation_2026-10-20.md) before using earlier acquisition/protocol assumptions. The main change requests now address explicit scale, graph and observation/assessment issues. The current acquisition queue requests S50/S51, not S10/S48 or the protocols.

# TRIDENT: evidence-backed P0 research memo

20 October 2026 · Provisional research framing and scoped synthesis · Original brief: **Markdown collé.md**

The original document is available and was reread. This memo advances its priorities using PF01 project facts, the existing scoped dossiers, newly extracted S43/S46/S26 supplement, and additional primary-method/report passages. It does not certify an exhaustive review, a final thesis direction, or a complete implementation theory. The accompanying **Question_to_Literature_Matrix.md** covers every original A1–K5 identifier, including unanswered questions. Dossiers and the claim ledger supply page-level evidence and reading limits.

## 1. Decision summary

**The most defensible near-term research question is what a sparse, uncertainty-qualified loop experiment can identify and predict—not whether modern reduced models can be applied to a molten-salt facility.** Physical1D loop models, conjugate transient CFD, thermal-network selection, Bayesian operators, local reverse-flow observations and POD reconstruction already have substantial precedent (S09/S36; S44; S08; S04; S46). A PhD contribution must distinguish itself from those methods through a new result, procedure, transferable mechanism or independently assessed capability.

| Priority | Recommended action | Confidence and boundary |
|---|---|---|
| P0 | Declare a small set of decisions/QoIs; compare a simple baseline, a constrained regional network and a segmented fluid–wall loop model. Audit identification and absolute energy scale before adding learned closures. | High confidence in the need; model adequacy remains to be tested. S08/S06 and the source audits support this framing. |
| P0 | Establish uncertainty dependencies, observation operators and independent assessment cases. Propose Nick-plan changes that create energy anchors and discriminate retained physics. | High methodological value; exact protocols require facility/adviser agreement. |
| P0 | Frame motivation around heat removal, temperatures/margins, stability and test interpretation, with explicit reactor-system transfer limits. | Supported by S12/S43/S44/S47; no assertion that TRIDENT is a scaled reactor. |
| P1 | Add transient momentum, goal-dependent spatial enrichment or experiment–CFD learning when a failed QoI or an evidence contract justifies it. | Conditional on data and qualified CFD; a broad field gap is not established. |
| P1 | Study the limits of recirculation extent/thermal-effect inference. | Sparse thermal evidence can constrain consequences; local velocity/3D extent remains unvalidated without independent evidence. |
| P2 | Develop an advisory dashboard/result contract with Ben Booth/NeutronOS after outputs and validity are defined. | A collaboration task, not standalone methodological novelty. No contact or product-stack assumptions. |

**Minimum comparison:** (i) persistence/steady energy or first-order input–output baseline, (ii) positive-parameter regional fluid/wall/loss network, (iii) conservative segmented loop with a buoyancy–resistance relation. Fit only identifiable parameter groups. Add transient circulation inertia if branch changes, flow timescales or instability matter. Full POD/OpInf/NEMO comparisons are conditional additions, not requirements to implement every fashionable family.

## 2. Motivation: history, reactor relevance and engineering decisions

The inspected history supports several distinct purposes. S40 investigates a proposed natural-convection reactor system; S41 concerns irradiation/material exposure in convection loops; S42 describes a pumped MSRE system. S43 describes the older corrosion-loop tradition and a modern FLiBe thermal-hydraulics facility. S44 explicitly targets distributed-heating dynamics and passive heat-removal questions. These are related research tools, not one historical claim that all natural circulation loops reproduce MSRs (see historical note and S43 dossier).

An MSR can mean liquid-fueled systems with moving heat sources/precursors, salt-cooled solid-fuel systems, or a secondary/auxiliary salt circuit. A nonnuclear ACU/VCU experiment may inform heat transport, buoyancy–loss competition, conjugate storage and selected closures. It cannot alone validate fuel kinetics, radiation-dependent chemistry, fission-product transport, full decay-heat removal or licensing conclusions. S12 is a liquid-fueled safety PIRT; its prominent salt-spill gaps must not be adopted as gaps in a single-phase pipe loop (S12 Table1/PDF16/5; summary PDF65–67/54–56).

The original “25% MSRE heat-balance discrepancy” claim should be retired unless a different original source establishes that exact metric. S47 reports distinct power-metrology and exchanger-design issues. It explains a primary-HX overestimate through revised property data and leaves radiator/power-metrology questions separate (S47 PDF31–32/27–28). This motivates trustworthy properties, installed metrology and uncertainty-aware margins, rather than a presumption that missing local flow physics caused the historical mismatch.

| Problem / decision | Proposed QoI and definition | Evidence and transfer check |
|---|---|---|
| Can a declared heat source be rejected in a steady operating condition? | Net cooler duty; power residual with all control-volume terms; equilibrium temperature distribution and circulation branch | S16/S43/S47; separate commanded, electrical and deposited heat. Do not prescribe the primary temperature being predicted. |
| How close is a component to its allowable temperature? | Margin \(T_{\rm limit}-\max T_{\rm wall}\); identify material/location, averaging interval and limit owner | S12/S44; a few point measurements do not validate an unobserved spatial maximum. |
| Is the salt approaching freezing? | \(\min T_{\rm fluid/wall}-T_{\rm solidus}\), with composition/property uncertainty and the relevant wall/fluid definition | S38/S43; single-phase margin is not blockage or phase-change prediction. VCU glycol cannot directly demonstrate salt freezing. |
| Will a transition overshoot or recover? | Peak temperature, time to threshold, settling criterion, minimum circulation, reversal occurrence | S09/S36/S44; steady similarity does not establish transient/stability similarity. |
| Which model or next test is useful? | Held-out QoI error, predictive interval calibration, identifiable groups, uncertainty reduction per feasible test | S08/S06/S04; parameter precision and decision usefulness are different objectives. |
| Is an advisory display actionable? | Measured present margin versus predicted future margin, horizon and validity status | Proposed contract; operational thresholds and latency remain owner-defined. |

**Similarity checklist before transfer:** geometric ratios and elevation/source/sink placement; Re/Pr/Ri or Gr as appropriate; development length and heat-flux distribution; wall/fluid capacity and conduction ratios; heat-loss fractions; property variation; boundary pressure/tank compliance; timescale ratios; freezing/phase/chemistry regime. Match the quantities controlling the chosen mechanism and disclose distortions. Matching one steady dimensionless curve is insufficient (S36 dossier). External wall heating, including distributed wall heating in S44, is not volumetric fission heating. “CHF” in the project is an allowable heat-flux constraint; no boiling critical-heat-flux claim is introduced.

## 3. Model and reduction comparison

The following equations are **analyst design templates**, not literal equations copied from a TRIDENT implementation. They illustrate fair model classes and expose assumptions; numerical parameters and discretization remain unspecified.

A conservative fluid region may satisfy
\[
C_{f,i}\dot T_{f,i}=\dot m(h_{\rm up}-h_i)+G_{fw,i}(T_{w,i}-T_{f,i})+Q_{f,i},
\]
with \(C_f=\rho c_pV\) only for the declared lump/property approximation; enthalpy differences replace constant-\(c_p\) temperature differences when needed. W and J/K units must be consistent. A wall region includes deposited power, fluid exchange, external losses, axial conduction and wall storage. Every internal heat exchange appears with opposite signs in the two connected balances. For reversed flow the upstream donor must change; one fixed upwind direction is invalid.

For a single incompressible loop with mass flow w, a useful integral template is
\[
\left(\oint ds/A\right)\dot w=-g\oint\rho\,dz-\Delta p_{\rm loss}(w,T).
\]
Here z increases upward, positive w follows the chosen arc coordinate, and the loss is signed against w. The inertance coefficient has units1/m, so its product with \(\dot w\) is Pa. Setting the left side to zero is a **quasisteady momentum assumption**, not a model of thermal relaxation alone. Tank/pressure/branch assumptions and property models can change this relation.

The observation model is separate:
\[
\tau_s\dot T_s=T_{\rm local}-T_s,\qquad y=H[T_f,T_w]+b+\epsilon
\]
with either a sensor-state representation or a direct observation mapping, as appropriate. Avoid counting the same lag twice. A centerline TC, fiber path, area mean, mass-flux mean and wall value require different H. A reduction preserving duty can still lose extrema.

| Family | States/data and retained physics | Constraints/UQ and risk | Place in comparison |
|---|---|---|---|
| Simple energy/persistence/first-order response | Few observed/regional temperatures; known inputs | Very cheap; uncertainty in input/response; cannot establish local extrema or circulation physics | Essential baseline that can defeat unnecessary complexity |
| Regional grey-box network | Fluid/wall/participating-solid nodes; actual heat/cooler/ambient histories | Positive C/G, shared exchange and known source partition; fit grouped parameters; nuisance initial states and discrepancy | Essential. S08/S26 are strong prior methods; transport must be justified |
| Segmented conjugate loop + steady momentum | Axial fluid/wall states, elevation, losses/properties; endogenous circulation | Conservation and sign checks; branch choice, low-flow and closure limits; uncertain parameters propagated jointly | Essential physics comparator, with granularity chosen by QoI |
| Same model + transient inertia | Adds w as a dynamic state; requires informative transitions | Can represent inertial timescales/reversal; stability depends on wall/source/BC fidelity | Add when a specified transition test requires it |
| Fixed-correlation versus fitted closure hybrid | Same states; small correction to h/friction/loss | Fit only justified groups; avoid fitting BC/geometry error as physics; uncertain correction validity | One controlled enrichment, not an unrestricted residual learner |
| Projection/POD or goal-oriented ROM | Fields and a basis/operator or reconstructable coordinates; perhaps adjoints | Basis norm/QoI selection, conservation/stability, training-domain uncertainty; POD energy need not preserve a critical local QoI | Conditional CFD-supported comparator. S46 is reconstruction prior art |
| OpInf/Bayesian OpInf | Projected states, inputs and derivative data (S04 §§2–3) | Polynomial operator regression; posterior draws can be unstable; basis/CFD/input uncertainty needs additional treatment | Later if field data and a meaningful speed/accuracy benchmark exist |
| GP input–QoI surrogate | Independent operating cases covering an input domain | Predictive uncertainty is conditional on kernel/training/noise; weak extrapolation/branch handling | Optional small-data baseline; no mechanism claim from a good fit |
| NEMO | Many reduced forward operators over known m; inversion linear in q | Conditional Gaussian/noise assumptions; m uncertainty and surrogate error need separate analysis (S05 Eqs1–14) | Later only if its unknown partition matches the actual inverse problem |
| Passivity/port-Hamiltonian/manifold models | Additional mathematical structure or field training | Thermal dissipation/advection and boundary work need a valid formulation; a mechanical analogy is insufficient | Theory search still open; no evidence-backed selection yet |

**Reduction meanings:** lumping changes control volumes/participating inventories; projection approximates fields; operator inference fits evolution coefficients; an observation map reconstructs measured/local values; a closure supplies unresolved transport. They are distinct operations and should be tested separately. Diagnose failures by an intervention ladder: correct geometry/BC/observation errors; examine residual patterns and parameter drift; enrich a state; change a closure; then add new physics. Good fit alone cannot select the cause (S06).

## 4. Identification and uncertainty design

### Identifiable combinations and energy anchors

**Analyst derivation, established type of ambiguity, not a novelty claim:** for passive
\[
C\dot T=-L(G)T+r(G,T_a),
\]
simultaneously replacing every C and G by aC and aG for a>0 leaves temperature trajectories unchanged. For one region only \(G/C\) is inferred from passive relaxation. Known steady net power q at a known temperature difference gives \(G=q/\Delta T\); a valid single-mode time constant then gives \(C=\tau G\). Unknown deposition efficiency transformed with the same scale preserves an ambiguity. A fixed participating inventory or independent duty breaks the global scaling under its assumptions; it does not identify every internal resistance/capacity.

Multiregion observation and initial-condition ambiguities remain. Sequential steady-G then transient-C fitting is defensible only if the same G law/regime applies, duties and hidden states are controlled/modelled, and steady uncertainty is propagated into the transient fit. Otherwise use a joint constrained fit and inspect profile likelihood/sensitivity rank/posterior geometry; a narrow prior-induced posterior is not data identification. S06/S08/S26 strongly challenge claims that Bayesian inference alone recovers physical materials.

**Useful first-order test, also an analyst derivation:** let \(J_y\) be sensitivity of observations to parameters and \(J_Q\) sensitivity of a proposed QoI. If \(J_yv=0\) but \(J_Qv\ne0\), a locally unobservable parameter direction changes the QoI; the data cannot identify that QoI to first order. Conversely, \(J_Qv=0\) for every observation-null direction is a local criterion for QoI insensitivity to those ambiguities. It is not a global guarantee under nonlinearities, constraints or branches. A potentially substantive extension would characterize these conditions for a nontrivial conservative loop model class and test experiment choices against them.

### Dependence budget

| Source | Dependence to retain | Initial treatment / evidence needed |
|---|---|---|
| TC calibration, placement, lag and drift | Shared reference biases; same-time channels; autocorrelation | Calibration model + TypeA repeatability + justified TypeB components; installation effect is not erased by averaging |
| Secondary calorimetry | Shared flow calibration, properties and inlet/outlet thermometer biases | Joint measurement model; check phase/timing/storage and actual control volume |
| Electrical heat and residual duty | Command/voltage versus actual watts; deposition/parasitics; shutdown tail | Independent watts/deposition evidence or explicit unresolved efficiency; zero command does not prove zero duty |
| Geometry/material properties | Correlated dimensions, temperature laws/composition and participating mass | Records, ranges and provenance; scenario bounds when distributions are unjustified |
| Initial hidden states | Wall/insulation/fluid split and prior thermal history | Conditioning on history, nuisance initial-state estimation, repeated preparations |
| Closures/reduction/discrepancy | Joint parameter correlations; regime-dependent bias | Physical constraints, prior checks, alternative forms and held-out residuals |
| Numerics/CFD | Mesh/time/model/BC error, calibration dependence | Separate verification by QoI; no treating CFD as exact independent observations |

For \(\Delta T=T_o-T_i\),
\[
u^2_{\Delta T}=u_o^2+u_i^2-2\,\mathrm{Cov}(T_o,T_i).
\]
A common additive calibration offset cancels from this difference; differential biases and timing errors do not. For \(q=\dot m c_p\Delta T\), use \(u_q^2\approx\nabla q^\mathsf T\Sigma\nabla q\) with the full covariance, not three independently estimated error bars. If this q and the same temperatures enter validation, retain their dependency; if primary temperatures are prescribed, label the prediction conditional. This extends the GUM source family S01/S31/S32; selected passages are available, not fully extracted here.

Start with local linear propagation for smooth, well-conditioned measurements, then a joint Monte Carlo check through the actual model. Use posterior predictive draws for uncertain parameters **plus** justified boundary/initial/observation/discrepancy components, explicitly conditional on training evidence. QMC/PCE/surrogates are computational alternatives after smoothness/dimension/branch checks; they do not repair an unidentified probability model. Ratios like \(h=q/(A\Delta T)\) become ill-conditioned near zero ΔT; use region-integrated flux/duty and temperatures first, or report nonidentifiability rather than a misleading finite HTC interval.

Do not mix confidence intervals, credible intervals, noisy observation predictions and bounded scenarios. Evaluate held-out **runs/cases**, not random time points from the same transient: QoI bias/error, interval coverage with sampling uncertainty, width/sharpness, residual dependence and conditional performance by regime. Proper scoring-rule selection needs further primary extraction; do not claim nominal calibration from a handful of correlated samples. Each joint transient realization should produce extrema/time-to-threshold; intervals for fixed-time point values are not intervals for a time maximum or its location.

## 5. Proposed changes to Nick's P0–P4 plan

All rows below are **proposed**, based on PF01's summary, not a verified line-by-line reading of Nick's original TeX protocols. They neither authorize tests nor establish safe setpoints. Each acceptance criterion is a check to define with the advisers, not a numerical threshold invented here.

Shared protocol contract for every row: synchronized raw clocks and command/measurement histories; instrument/placement/calibration identifiers; selected rates justified by sensor bandwidth and fastest model timescale; duration justified by slow storage/drift; repeats justified by between-run variance and available independent cases; missing-data/settling rules; preserve a separately declared final assessment set. More samples in one run do not replace independent runs.

| Phase / priority | Objective/QoI and missing quantity | Proposed change / instrument location | Uncertainty and assessment role | Acceptance check / question for Dr. Luciano |
|---|---|---|---|---|
| P0 / first | Establish geometry/fluid/power/sensor model | Freeze as-built ID/wall/insulation/source inventory; resolve VCU glycol product/concentration; record clocks and actual power channel | Metadata before fitting; no new instrument assumed | Which revision and calorimetric/electrical chain can be authoritative? |
| P1 / first | Separate repeatability, shared bias and drift | Common-condition/baseline checks for existing temperature channels and ambient; obtain calibration linkage and installed response evidence | Estimate covariance; reserve repeat baseline to check drift | What common-condition test is feasible without assuming a uniform loop? |
| P2 / first | Identify time constants and hidden storage | Retain warm/cold relaxation and mixed-tank/two-fill ideas; log residual duty and preparation history; include existing wall/ambient channels where present | Fit rates/groups, not absolute C without anchor; hold out complete preparations | Can the actual residual heat/cooler tail be bounded or measured? |
| P3 / first | Break G–C/heat-deposition scale ambiguity | Convert one documented known-power loss/hold condition into an energy anchor, with actual watts and all major removal/storage terms | Anchor G or source efficiency; propagate its uncertainty into C | If this was formerly blind, **reallocate it as calibration and nominate a replacement blind case**. Which measurement establishes net rather than commanded power? |
| P3 / next | Distinguish fluid/wall/storage/loss effects | Contrasting steady temperatures and relaxation directions; use existing sensor locations; propose added wall sensor only after sensitivity screening | Independent excitation; nuisance initial states; source/loss confounding check | Which feasible intervention changes loss versus storage independently? |
| P4 / first | Test autonomous steady duty/temperatures | Vary heater and secondary cooling independently within approved envelope; retain independent operating cases | Use measured secondary boundary, not primary target temperature as a BC; joint duty UQ | What minimum decision-linked error/margin is useful and resolvable? |
| P4 / next | Test transition and branch physics | Separate heater/cooler changes and reversals only if permitted; record actual forcing and initial history | Compare quasi-steady versus dynamic circulation; entire-run holdout | Are circulation sign/rate observable independently? If not, which temperature QoIs remain assessable? |
| P4 / conditional | Test spatial/recirculation consequences | Request existing local wall/temperature evidence first; consider an additional sensor only if it discriminates models | Do not label local extent validated from bulk thermometry | Is any local-flow evidence actually obtainable? If absent, restrict the claim to observable thermal consequences. |

No requested rate, duration or number of repeats is numerically fixed without timescale/noise and feasibility evidence. Absolute energy anchoring and withheld-case allocation have greater immediate decision value than a large new sensor wish list. No ACU operating data were processed.

## 6. Separate CFD evidence contract and recirculation ladder

| Exchange / priority | Required evidence | Decision and consequence if absent |
|---|---|---|
| Experiment→CFD / P0 | Geometry/revision, actual deposition and cooler histories, ambient/loss paths, material laws/composition, initial fields or histories, gravity, tank/free-surface/pressure treatment, sensor locations/response and uncertainty | Otherwise BC error may be fitted as a closure; do not call differences model-form physics |
| CFD→reduction / P1 | Versioned meshes/settings, time-resolved velocity/T/pressure and solid T, boundary fluxes, signed mass/enthalpy integrals, matched observation outputs, conservation residuals | Contours alone cannot train/audit a conservative closure |
| Verification / P1 | Mesh/time/domain/averaging sensitivity for each claimed QoI: duty, local wall flux, extrema, reverse-flow fraction and descriptor persistence | Converged duty does not establish converged local extent; pseudo-time stepping does not validate physical transients |
| Validation / P1 | Comparison with withheld experimental observables and their joint uncertainty; disclosure of losses/BC/closure data used in calibration | Calibrated data cannot be counted again as independent validation |
| Campaign selection / P1 | Contrasting cases varying source placement, boundary/loss conditions and flow/development as independently as feasible; train/select/test split by case/regime | If cases covary, report association and transfer limits rather than mechanism attribution |

S35 remains useful external evidence; its document discrepancies are left for Codex as requested. They do not hold up this pass. S44 gives a concrete warning: filling-tank/outlet representation changed the predicted stability result, with experimental stability-boundary validation still future work (S44 conclusion,PDF13/12).

Define recirculation descriptors before fitting: signed axial direction relative to declared loop coordinate; reverse-flow area/volume fraction using a stated threshold and averaging window; separation/reattachment only where topology permits; exchange flux or residence/transport metrics where a geometric “bubble” is ambiguous. In3D, a region of negative axial velocity is not automatically a closed recirculating volume. Distinguish average instantaneous extent from extent of the time-mean field.

| Evidence level | Extent claim | Thermal-effect claim | Stop/fallback |
|---|---|---|---|
| No qualified CFD/local-flow measurements | Not independently identifiable from sparse bulk temperatures in general | Fit/assess measured temperatures and duties, with competing effective mechanisms | Do not publish a measured local extent. Study identifiability limits and observable consequences |
| Minimal verified CFD, limited cases | Report a simulation-defined descriptor with sensitivity; no experimental local-flow validation | Compare effective/two-zone/local corrections for declared CFD and experimental QoIs | Stop adding field richness if descriptor/numerical uncertainty overwhelms the proposed benefit |
| Adequate verified CFD and withheld regimes | Assess descriptor/reconstruction transfer on withheld CFD | Assess flux/extrema or duty improvements; pair with independent thermal observations where possible | Claims remain CFD-supported where no local experiment exists |
| Independent matched local-flow and thermal evidence | Can assess local predictions under measurement operator/UQ | Controlled thermal comparisons can test a mechanism | Requires actual new evidence; not assumed in TRIDENT scope |

For attribution, compare matched source/sink, geometry, properties and integral flow where feasible; acknowledge when suppressing a structure changes the physical problem. First compare integrated wall flux, wall/fluid extrema and temperature asymmetry. An HTC ratio near vanishing driving ΔT is a poor primary mechanism metric. S43/S46 establish local structure/temperature evidence, not causal heat-transfer enhancement.

## 7. Candidate contribution packages and strongest challenges

These are **hypotheses H01–H04**, not established literature gaps. A narrower paper may be possible than a whole package. No package is selected as the final thesis.

| Candidate | Closest challenges / precise possible difference | Falsifiable demonstration and minimum evidence | Risk / fallback |
|---|---|---|---|
| H01: identifiable, uncertainty-qualified physical reduction | S08 already selects thermal networks; S06 establishes confounding; S26 learns topology. Possible difference: a nontrivial conservative loop-model class with QoI identifiability conditions and experiment choices under uncertain power/observations | Derive beyond the elementary G–C symmetry; show synthetic equivalences/recovery and independent physical-case QoI assessment against simple and richer baselines | If no new condition/procedure or independent predictive benefit, treat as sound application, not method novelty; narrower empirical identifiability-limit paper |
| H02: QoI-dependent retained physics/model selection | S09/S36 scaling and S44 conjugate dynamics already exist; S04/S25 are reduction challengers; S48 directly challenges adjoint-sensitivity novelty | Compare duty versus extrema/transient QoIs at comparable information budgets; select state/closure enrichment using predeclared tests, then assess on untouched cases | If simple model is sufficient, a reproducible adequacy boundary can be valuable; avoid claiming universal hierarchy |
| H03: observable-consistent local thermal correction | S43/S46 local thermal/PIV evidence and S39 reconstruction challenge “first spatial model”; S35/S44 already simulate counterflows | Identify the smallest correction that improves a declared measured/local QoI on withheld evidence; distinguish field agreement from engineering utility | CFD/data dependent. If unavailable, retain honest bounds or conditional reconstructions and demonstrate nonuniqueness |
| H04: credible experiment–CFD transfer with discrepancy | S06/S04 and existing SAM/CFD validation prevent claiming generic calibration/UQ is new | Separate calibration information, propagate measurement/numerical/transfer uncertainty, test unseen regimes/facility cases against a no-transfer baseline | Modular/multifidelity closest-method search incomplete. Without sufficient independent cases, remain a protocol/evidence study |

**What would advance understanding?** A theorem/identifiability condition, a validated procedure that changes model/test choice, a controlled mechanism result, or a demonstrated transfer boundary. A dashboard, a fitted model and a CFD visualization alone do not establish those advances. A publishable negative result needs a defined model/evidence class, fair competing explanations, reproducible tests and consequences: for example, multiple parameter/flow descriptions that agree with all sparse observations yet yield materially different extrema, or evidence that extra spatial physics adds no value for a specified duty decision.

## 8. Proposal kit

**Draft motivation paragraph:** Natural circulation can support passive heat transport, but a loop's ability to reject heat depends on the coupling of buoyancy, resistance, source/sink placement and thermal storage. Reactor safety assessments identify heat rejection as a fundamental need while emphasizing design-dependent phenomena and uncertainty (S12). Salt-loop experiments supply valuable thermal and local-flow evidence, but inferred flow, nonuniform temperature observations and changing boundary conditions can limit the conclusions drawn from them (S43;S46). Transient conjugate modelling and established thermal-network learning provide strong starting points (S44;S08;S26). This research will therefore investigate which physical reductions and experiments can support independently assessable engineering quantities under sparse measurements and uncertain inputs, while defining when local or reactor-system claims require additional evidence.

Candidate questions/objectives:

1. **Which physical parameter combinations and thermal QoIs are identifiable from the available loop measurements?** Hypothesis: targeted absolute-energy anchoring and independent excitation remove consequential ambiguities that additional passive temperature samples do not.
2. **What retained physics is necessary for each chosen decision?** Hypothesis: the smallest adequate model differs for steady duty, transient extrema and local margins; predictive evidence can discriminate useful enrichment from compensating calibration.
3. **When can CFD-derived observation/closure maps improve sparse-data predictions?** Hypothesis: matched observation operators and explicit transfer discrepancy improve unseen-case QoIs; this is a conditional aim with a no-CFD fallback.
4. **What cannot be inferred about local recirculation from thermal evidence?** Hypothesis: some distinct flow descriptions remain observationally equivalent, requiring bounded/conditional thermal claims rather than unique reconstructed extent.

Work packages: WP1 evidence/QoI/measurement specification; WP2 constrained model hierarchy and identifiability analysis; WP3 targeted experiment proposals and independent assessment; WP4 conditional CFD/local correction; WP5 advisory demonstration using qualified outputs. Central UQ runs through each. Suggested minimum preliminary demonstrations: a symbolic ambiguity and anchor test; a synthetic hidden-state/observation test; a conservation/sign/limiting-case audit; one existing-data prediction comparison **only after the data-processing hold is explicitly lifted**. These demonstrations have not been performed here.

Assessment criteria to agree: which measured/spatial temperatures matter; permissible decision error versus measurement resolution; independent case count; interval target/coverage evidence; acceptable extrapolation/domain; runtime/horizon and model-complexity budget. No invented numerical tolerance. Principal risks are uncertain power/deposition, insufficient independent cases, uncertain local observation maps and delayed CFD; each has a reduced-scope thermal/identifiability fallback.

## 9. Reading, acquisition and search scope

Read now: S43 and S47 for historical/metrological motivation; S08/S06/S26 plus supplement for closest-method challenges; S09/S36 for steady/transient similarity limits; S46 for what local-flow evidence already exists. These dossiers/selected readings are available.

Read next: S10 for the closest steady/transient experiment–CFD/loss-treatment comparison (**upload requested**); S18 for a conjugate1D alternative; S23 for a full identifiability workflow; S07 for experiment-design objectives; S14/S15 for actual surrogate/similarity conditions; S44 full numerical/BC audit and S45 development evidence. These are not all inaccessible: the registry distinguishes available-but-unread, web-only and acquisition-needed sources.

Later: S04 full numerical assessment, S24/S25 structure/goal reduction, conditional S05/NEMO, S48 adjoint study (**upload useful if H02 progresses**), model-discrimination/multifidelity methods and operational uncertainty communication. See **Literature_Acquisition_Requests.md** for ranked exact requests and replaceable alternatives.

Search date20 October2026. This pass used publisher and institutional records, author repositories, arXiv, Crossref, OSTI/ORNL and an identified historical-report mirror; reviews were discovery aids. Searches included exact original MSRE report/title and ORNL4037; Britsch supplementary/data terms; NEMO title; Kudariyawar full title/PDF; adjoint high-Pr natural circulation; DYNASTY distributed heating. Backward tracing from S43 located S47 and S49; Headley led to S48; methods were checked against original accessible manuscripts. Recent leads include2026 MSRE MARS/TRANSFORM benchmarking; their full methods were not extracted and they do not support substantive findings here.

Limitations: language/database and citation-graph coverage are incomplete; some publishers return403/429 or catalogue-only content; no university access is assumed; original Nick protocols and authoritative facility records remain absent. Selected-section methods reading is explicitly not full-paper reading. Broad gaps concerning structure preservation, goal-oriented selection, modular calibration and operational UQ communication remain unresolved. Verified identifiers—not unverified filled-out citations—are used in the registry/BibTeX.

## 10. Seven-day proposal-planning sequence

| Day | Concrete artifact | Can proceed without TRIDENT CFD? |
|---|---|---|
| 1 | Closest-prior-method/novelty rejection table and source access requests | Yes |
| 2 | Decision–QoI definitions and minimal model specification | Yes |
| 3 | Symbolic identifiability/covariance budget and anchor design | Yes |
| 4 | Proposed Nick P0–P4 change matrix with withheld-case allocation | Yes |
| 5 | CFD evidence contract and recirculation stopping criteria | Yes; identify conditional work |
| 6 | Aims/hypotheses challenged by strongest prior work and fallback | Yes |
| 7 | Integrated committee-facing argument and methods appendix, unresolved decisions visible | Yes |

This is a planning sequence, not a promise to finish all literature, tests or scientific work in seven days.

## 11. Consequential decisions still needed

The most valuable help now is **S10's full paper**, then any feasible S48 access; details are in the acquisition table. The original Nick protocols/experiment matrix are a separate useful project upload, because the current phase mapping relies on PF01. No need to upload Ethan again or reconcile its discrepancies now.

Adviser decisions: (i) which reactor circuit/engineering decision is the primary motivation; (ii) which two or three QoIs and decision tolerances matter; (iii) what absolute energy anchor can actually be established; (iv) what existing cases may be used for fitting versus independent assessment; (v) whether a local-flow claim is an optional extension or a required deliverable. Each changes the achievable model/theory claim. No broad new questionnaire is needed before continuing available reading.

## 12. High-value continuation prompts

1. “Extract S10 and compare its heat-loss calibration, independent validation and transient QoIs against S16/S44 and our minimum method set. Update only claims the full paper supports.”
2. “Read S18/S23/S08 as a methods batch. Specify one conservative loop model, its observation equation and identifiable parameter groups; separate established theory from candidate extensions.”
3. “Read S14/S15 and the closest MSRE benchmark originals. Build a mechanism-specific similarity/distortion argument for the chosen ACU/VCU application.”
4. “Compare S07 and model-discrimination design methods. Rank proposed Nick tests by QoI improvement under uncertain power and hidden initial states, with no invented safe setpoints.”
5. “Challenge H01–H04 using S24/S25/S48 and newer primary work. Identify a narrow falsifiable contribution and the evidence that would reject it.”
