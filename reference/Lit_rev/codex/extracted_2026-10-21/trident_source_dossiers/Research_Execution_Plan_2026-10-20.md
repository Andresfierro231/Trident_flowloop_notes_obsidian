> Current21October2026: reviews v0.7;76sources,43purpose-scoped dossier sources,384claims. S19/S29/S71v2/S72final/S73/S74 read;S75/S76 retrieved,unread. Resume Checkpoint_Decisive_Evidence_2026-10-21.md;current requests Upload_Requests_Current.md. Earlier statuses below are historical.

> Current checkpoint21October2026: reviews v0.6; S13/S64/S65 scoped-read; S24/S29/S11 retrieved.74sources,37purpose-scoped dossiers,328claims. Current requests and next passes: Access_Gaps_and_Requests_2026-10-21.md and Next_Two_Prompts_2026-10-21.md. Earlier statuses below are historical.

> Latest status: S69/S70 also resolved and purpose-scoped read. No immediate upload request. Current synthesis: Physical_Interpretation_and_Data_Error_Synthesis_2026-10-20.md; reviews v0.5. Earlier status notes below are historical.

> Updated status: S23/S67 supplied and scoped-read; S68 retrieved/scoped-read. Current priorities and acquisition requests are in Strategic_Reading_and_Acquisition_Plan_2026-10-20.md and Upload_Requests_Current.md. Earlier access/reading statuses below are historical.

# Next decisions for the two TRIDENT literature reviews

Status: proposed research/implementation sequence,20October2026. This translates inspected literature into concrete decisions; it does not select a final thesis direction or authorize experiments, data reduction or CFD runs. The original62question brief remains governing.

## 1. Define the prediction before choosing the model

The initial comparison should address a small number of supported thermal quantities. Provisional candidates are sensor-consistent fluid/wall temperatures, independently supported heat-rejection/loss quantities, and response/settling metrics. Exact tolerances remain an adviser/project decision. Unobserved global extrema, local vortex extent, independently validated circulation and reversal probabilities are conditional claims.

Write a contract for each comparison:

| Element | Required specification |
|---|---|
| Mission | Chosen facility and revision; chosen reactor subsystem/mechanism analogy |
| Inputs | Available heater, secondary-cooler and ambient histories; independent energy anchors; uncertainty/dependence |
| Initial state | Measured versus inferred temperatures; hidden wall/insulation state treatment |
| Outputs | Specific temperatures/duties/response definitions, units, locations and evaluation horizon |
| Observations | Centerline/PTC, pipe-contact/STC, sensor lag/bias and synchronization; do not equate these with bulk-fluid states |
| Adjustable quantities | Small physically defined parameter groups; separately list fixed supported quantities |
| Assessment | Calibration, model selection and final held-out cases; reset roles after any refit |

PF01's primary-temperature-driven wall model is a conditional diagnostic. It must not be scored against a fully autonomous forward model without identifying the different available inputs.

## 2. Use a minimal model hierarchy

This is a proposed comparison set, not a literature finding that one family will win.

| Baseline | States/closure | Decision it tests | Evidence challenge |
|---|---|---|---|
| M0 energy/response reference | Global energy balance and a small effective response model | What is inferable before regional complexity? | S08/S26 already establish grey-box/network baselines |
| M1 conservative regional network | A few fluid/solid/insulation storage groups and passive exchange; explicit observation map | Does a small physically interpretable model predict withheld measured quantities? | S52 and S66 already include conjugate physics; identifiability must add value |
| M2 circulation/transport model | Signed loop momentum or qualified steady closure, conservative fluid advection, selected wall states | Does resolving transport improve the declared QoI enough to justify added uncertainty/parameters? | S18/S30/S59/S66 are established physical/modal comparators |

Only add inferred operators, richer closures or spatial reconstruction when there is a declared failure of these baselines and data capable of distinguishing the extension. Model complexity is not a contribution metric.

## 3. Derive the independent implementation

These are our proposed conservation requirements, not transcriptions from one paper:

\[
\frac{dE_{f,i}}{dt}
=\dot m\,(h_{\rm in}-h_{\rm out})+q_{w\to f,i}+Q_{f,i},
\]
\[
\frac{dE_{w,i}}{dt}
=-q_{w\to f,i}+q_{\mathrm{axial},i}+Q_{w,i}-q_{\mathrm{loss},i}.
\]

Use actual heat-source deposition and the same interfacial heat rate with opposite signs. With constant properties \(dE/dt=C\dot T\); with variable cp, use an enthalpy relation rather than cp(T)T as stored energy. Signed flow requires upstream reversal and dissipative drag conventions. A measured sensor output is a separate map from the states.

Verification targets: global energy cancellation, uniform equilibrium, passive exchange, zero-source limit, signed-flow consistency, and refinement of the chosen QoI. Stability/reversal statistics require their own temporal/spatial/modal checks. A converged average does not establish a converged extremum.

S18 is especially valuable as a derivation comparator, but its preprint contains selector/sign/prefactor inconsistencies. Its lowPr heat-transfer closure and inclination multiplier cannot simply be transplanted. S66's unresolved diameter also prevents faithful numerical reproduction until clarified.

## 4. Establish what can be learned before calibration

For the elementary passive model,
\[
C\dot T=-G(T-T_a),
\]
scaling both C and G by any positive common factor leaves the temperature trajectory unchanged. This is our direct symmetry argument, not a new thesis theorem. Passive relaxation alone identifies the ratio G/C under these assumptions. Independently known net steady duty at nonzero temperature rise gives \(G=Q_{\rm net}/(T_{\rm ss}-T_a)\); that conclusion depends on a valid steady balance and measurements.

Regional networks can retain additional ambiguities after the global scale is anchored. Hidden initial solid states, regional losses, nuisance biases and sensor dynamics must be included in the parameter/observation contract. A narrow posterior created mainly by bounds/priors is not automatically information supplied by data.

Proposed diagnostic order:

1. Analyze exact symmetries and conservation constraints.
2. Examine sensitivity rank and parameter combinations over plausible inputs/conditions.
3. Use multiple optimizer starts and synthetic recovery to detect competing fits.
4. Profile supported parameter groups and nuisance quantities with a defensible likelihood.
5. Compare their implications for predictions; nonunique parameters can still yield a well-constrained measured QoI.

The detailed profile construction and confidence-threshold assumptions remain pending S23 full-text extraction. S67 is an especially close thermal-network prior-art lead; its abstract already reports likelihood/filter-based identification and1D/2D profiles, so combining these ideas alone cannot establish novelty.

## 5. Choose experiments by the scientific objective

S07 explicitly separates parameter-learning, prediction and model-discrimination goals. Our proposed distinction is:

| Goal | Candidate utility | Required inputs | Main risk |
|---|---|---|---|
| Identify a physical parameter group | Expected information about that group after marginalizing nuisance uncertainty | Prior/support, joint likelihood, feasible excitation | Learning nuisance details while target remains unsupported |
| Improve a selected thermal prediction | Expected reduction in predictive loss/variance or decision error | Prediction scenario, QoI/tolerance and uncertainty model | Sharp but biased predictions under wrong model |
| Distinguish M1 and M2 | Expected discriminatory evidence/predictive separation | Competing models, allowed calibration and observation maps | Both can absorb differences through nuisance parameters |
| Qualify repeatability/metrology | Reduction in uncertainty of repeatability, drift or shared bias | Repeated conditions and calibration/clock metadata | Treating autocorrelated samples as independent repeats |

Parameter profiling and Bayesian nuisance marginalization are different operations; define which one each calculation uses. No single score should be called all four objectives.

Begin with a finite, feasible set of Nick-plan choices. Evaluate model separation and uncertainty at those choices before expensive global design optimization. This staged choice is our practical proposal, not a proven universally optimal algorithm.

## 6. Translate questions into proposed Nick-plan requests

| Proposed question | Existing lane | What must be resolved | Scientific role |
|---|---|---|---|
| Is the temperature difference stationary and metrically meaningful? | P0/P1 | Calibration, clock, drift/shared covariance, sensor map and ambient history | Qualify observation/likelihood |
| Which passive rates are reproducible? | P2 | Preparation, initial hidden states, residual heater/cooler duty, autocorrelation | Ratio/response evidence |
| What anchors absolute energy/storage scale? | P3 or independently supported inventory | Actual deposited/net duty, cooling/ambient losses and covariance | Separate scale from response ratios |
| Which feasible change separates wall storage from advective transport? | P4 or a separately approved variant | Actual independent controls, safe range, horizon and prediction target | Model discrimination |
| Does the selected model generalize? | Frozen holdout cases | Cases withheld from calibration and topology/closure selection | Independent predictive assessment |

These are proposed questions, not agreed changes. Nick's written proposals are not proof of execution. If P3 becomes a calibration anchor, it cannot remain the unchanged final holdout for that claim. No new safe setpoint, sampling rate, instrument or repetition count is invented.

## 7. Two testable contribution hypotheses

**H01 — identifiable conservative prediction.** At a specified observation/input contract, a parsimonious model based on identifiable groups predicts held-out thermal quantities at least as reliably as a detailed unconstrained fit. Required difference from prior art: a nontrivial identifiability/uncertainty result or reproducibly better independent prediction. Falsification: no benefit beyond established baselines, or claimed groups remain unidentifiable under the available evidence.

**H02 — a criterion for retaining physics.** A criterion using transport/storage scales and observation/QoI sensitivity predicts where a simpler model exceeds a predeclared error/uncertainty tolerance. Required difference: prediction of adequacy before seeing the held-out result, over a stated model/regime class. Falsification: criterion fails under boundary/observation uncertainty or reduces to case-specific retuning.

Fallbacks can be scientific: demonstrate a precise observational nonuniqueness, an irreducible bound, or a regime where added physics is unnecessary. They require a clear model class and independent evidence; they are not automatically publishable because a fit failed.

## 8. What happens next

1. Acquire/read S23 and the thermal-network S67; finish the identifiability comparison.
2. Extract already available S64/S65 and remaining S13 engineering evidence, sharpening which reactor analogy/QoI is defensible.
3. Adjudicate H01/H02 against the closest prior work and original62questions.
4. Rewrite the two reviews into fuller synthesis with a model implementation matrix, equation/closure requirements, engineering decision map and contribution/falsification table.

No additional bulk data are requested. Current missing facility facts remain in research_state.json. No claim is made that the comprehensive reviews or novelty search are finished.
