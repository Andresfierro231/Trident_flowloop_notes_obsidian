# A. Which physical and reduced models can support TRIDENT predictions?

> **Critical-synthesis addendum, 21 October 2026:** see [cross-source synthesis](Critical_Cross_Source_Synthesis_2026-10-21.md). Newly inspected S77 strengthens the prior-work challenge to basic thermal identifiability/minimum-sensor claims. CP01/CP02 are the provisional no-CFD core; no precise novelty is certified. S78 corrected original is now scoped-read;the earlier conditional request is closed. Its linear multiport response assumptions limit transfer to the loop. The v1.0 comprehensive body below is retained with its original IDs.

**Comprehensive first review draft, v1.0 — 21 October 2026.** Methods and theory for ACU/VCU model development and staged Codex comparisons. This synthesis continues `Markdown collé.md` and the existing registry; it does not restart discovery. It addresses the original questions through a feasible no-CFD core and explicitly conditional extensions. It is not a validated implementation, exhaustive systematic review, final thesis direction or certification of novelty.

Evidence labels used throughout are **established** for the inspected source result under its stated assumptions; **conditional transfer** for application beyond that setting; **proposed** for our derivations, comparisons and research. Stable source and claim IDs refer to `source_registry.json` and `claim_ledger.json`. A locator such as “PDF6/349” means PDF page 6, printed page 349. Manuscript page numbers are not silently converted to journal pages. The dossiers contain version, completeness, coverage and source-notation checks; the complete original-question matrix and ranked gaps conclude this review.

Bibliographic identity, publication/version and reading depth: [source index](Review_Source_Index.md); exact claim records: [claim ledger](Claim_to_Evidence.md). These preserve the reading-depth distinctions needed to audit this synthesis.

## 1. What prediction must the model make, and what information can it use?

The central problem is an evidence-limited prediction task: determine which thermal-hydraulic outputs a small physical model can predict from inputs available at the time of use, what its measurements actually constrain, and whether omitted physics materially changes a declared engineering prediction. Reproducing a thermometer trace, identifying a physical parameter and predicting an unobserved field are different achievements.

The project record specifies three stages: steady performance/margins, transitions, then operational assistance. Current M1, M2 and M3 are implemented steady formulations: no-flow energy, prescribed-flow energy, and scalar buoyancy–resistance circulation respectively. Their existence is a project fact, not facility validation. A previous radial wall calculation driven by measured future primary-fluid temperatures is a conditional diagnostic; it must not be compared as an autonomous forecast against a model given only heater, cooling and ambient inputs. PF01's facility and observation distinctions govern this review: VCU/STNCL is one experimental lane, ACU is separate, and TAMU literature is external evidence. No qualified TRIDENT CFD or new instruments are assumed.

Every candidate requires the following contract before fitting:

| Item | Required declaration | Why it changes the scientific comparison |
|---|---|---|
| Scenario and horizon | Facility/revision, geometry, fluid, source/sink history, initial state, steady or transient horizon | A model may be adequate for one operating point and inadequate for a transition |
| Inputs available at use | Actual deposited power, secondary cooling, ambient and any prescribed flow, with provenance | Future measured primary temperatures cannot be hidden forecast inputs |
| State meaning | Fluid bulk/enthalpy, wall, insulation, effective regional temperature, circulation | An effective temperature need not equal a centerline or contact-wall reading |
| Observation map | Location, average, sensor response, bias, clock, sampling | Apparent transport error may be observation mismatch |
| Target | Duty, specific observed temperature, response time, circulation or qualified spatial quantity | A model preserving duty can lose a local maximum |
| Adjustable and fixed quantities | Parameters, initial states, closures and independently supported anchors | Giving one model more calibration information invalidates a fair comparison |
| Assessment | Development, selection and untouched test cases; scores and tolerances | Calibration agreement is not independent predictive evidence |

This distinction is established in different mathematical forms by S71's separate observation/target maps (Eqs1–5, PDF3–4; S71-C03), S72's distinction between observable and nonobservable QoIs (§2.5, PDF7; S72-C02), and S75's governing/observation/target operators (Eqs1–8, PDF9–12; S75-C01). It is also practical: S19's steady CFD uses measured thermal boundaries, and S29 infers primary flow from measured cooler enthalpy balance (S19-C01–C03; S29-C02). Those are useful conditional comparisons, not independent measurements of every predicted quantity.

## 2. Which conservation structure should survive reduction?

### 2.1 Energy before temperature fitting

**Proposed implementation formulation.** For a fixed control volume with mass and kinetic-energy effects treated consistently with the selected low-Mach model, write stored sensible energy and net energy rates rather than fitting temperature equations independently:

\[
\frac{dU_i}{dt}=\sum_{f\in\partial i}\dot H_{f\to i}+\dot Q_{s, i}
+\sum_j\dot Q_{j\to i}-\dot Q_{i\to a}.
\tag{EQ-01}
\]

Here \(U_i\) is J and each rate is W. The signed advective enthalpy flux at a shared face is evaluated once and used with opposite signs. The same rule applies to fluid–wall and wall–insulation exchange. If \(c_p\) varies, use \(h(T)-h(T_*)=\int_{T_*}^T c_p(\vartheta)d\vartheta\); \(c_p(T)T\) is not generally enthalpy. These equations are our conventional formulation, not a corrected transcription of one source's printed equation.

A constant-capacity thermal network follows as a restricted case:

\[
C_i\dot T_i=\dot Q_{s, i}+\sum_jG_{ij}(T_j-T_i)-\dot Q_{i\to a},
\quad C_i>0,\ G_{ij}\ge0.
\tag{EQ-02}
\]

For paired reciprocal conduction, the exchange leaving one node enters the other. Positive capacity and conductance support passive relaxation; they do not by themselves enforce correct source deposition or describe directional fluid transport. Radiation adds \(\epsilon\sigma A(T_w^4-T_{sur}^4)\) under the appropriate surface/view-factor approximation and uses absolute kelvin. Contact resistance and insulation geometry are separate from material conductivity. A fitted regional coefficient can combine these effects but should then be called effective.

**Established precedents.** Separate fluid/wall conduction and nonuniform areas already occur in S52 (Eqs7–23, PDF5–7; S52-C02). S50 includes conjugate dynamics, trace heating and losses (§3, PDF3/515; S50-C02). S66 separates inner/outer wall capacities and radial conduction (Eqs1–6, PDF3–4/413–414; S66-C01). Thus adding wall states, losses or a physical network alone is not a new contribution.

### 2.2 Circulation is a separate state or closure

A thermal relaxation model need not predict circulation. A full loop model must distinguish a prescribed mass flow, an algebraic steady branch, and transient momentum. **Proposed constant-density inertia approximation**, with a declared positive coordinate \(s\) around the loop and upward \(z\), is

\[
\left(\oint\frac{ds}{A(s)}\right)\frac{d\dot m}{dt}
=-g\oint\rho(T, s)\, dz
-\sum_j\left[f_{D, j}\frac{L_j}{D_{h, j}}+K_j\right]
\frac{\dot m|\dot m|}{2\rho_j A_j^2}.
\tag{EQ-03}
\]

Both sides are Pa; its assumptions exclude arbitrary moving interfaces and require consistent mass/density treatment. Local density can provide buoyancy while a reference density supplies inertia only under an explicitly justified approximation. Do not combine incompatible compressibility, fixed-mass and property assumptions without checking continuity. Cross-section changes require their own area and loss conventions. At steady state the inertial term vanishes; that does not imply transient inertia is unimportant. A positive square-root solution does not predict reversal.

The closure's conventions matter as much as its name. Darcy and Fanning friction factors differ by four under standard definitions. Mass flow kg/s, mass flux kg/(m²s), volumetric flow m³/s and velocity m/s are not interchangeable. S55 uses volumetric flow, while later loop formulations use different variables (S55-C03, Eqs4–5, PDF4/20). S19/S29's reported steady balances illustrate the value and limits of algebraic circulation, not a universally transferable reversal law (S19, Eq17–27, PDF6; S29, Eq6–10, PDF11).

### 2.3 Source and sink paths must be retained when consequential

Wall heating, an immersed element, distributed fluid generation and nuclear heating of solid structures can have equal total power but different dynamics. S65 changes source partition and geometry in 1D stability calculations, but does not map actual fluid-specific operating trajectories onto its dimensionless boundaries (§4.2, PDF9; S65-C02–C05). S66 shows that wall storage and the flow derivative of heat transfer enter stability (Eq46, PDF6/416; S66-C04). Matching a steady coefficient therefore does not necessarily match a transient Jacobian.

S20 is a particularly clear conditional comparator: internal cosine-shaped salt heating and selected graphite heating are balanced through a fixed-temperature graphite boundary, with adiabatic fluid walls (§2.2, PDF4; S20-C04). Its source/sink is not an external-heater ACU/VCU pipe. Source fidelity is a model-class question, not an optional correction to attach after an unconstrained fit.

## 3. What minimum hierarchy should be compared?

Reduction can mean aggregating volumes, eliminating fast algebraic states, projecting fields, learning reduced operators, or approximating unresolved exchange. These operations retain different information. Call a model reduced relative to a declared richer description; “surrogate” describes its replacement role and need not exclude physical reduction.

| Family | Retained physics and information | Data/cost and interpretability | Necessary limitation or failure test |
|---|---|---|---|
| Global steady balance/current M1 | Total source, rejection and losses | Lowest cost; useful metrology consistency baseline | Cannot determine regional losses, transport or circulation uniquely |
| Current M2 prescribed-flow model | Energy transport at given flow | Requires independently prescribed/justified flow | Conditional task; must not be scored as autonomous flow prediction |
| Current M3 buoyancy–resistance model | Scalar steady flow and thermal coupling | Geometry, property and resistance support | Branch/sign/regime and boundary uncertainty; no transient certificate |
| Small regional network | Participating thermal storage and exchange | Sparse observations may support grouped combinations | Effective states/parameters need not identify physical layers |
| Segmented conjugate fluid–wall model | Conservative advection, storage, losses; optional insulation/axial conduction | More states/closures and potential nonidentifiability | Added complexity must improve a declared held-out QoI |
| Fourier/projection reduction | Spatial transport phase and selected field modes | Requires basis, source/geometry and projection contract | Circulation accuracy need not preserve observations or extrema |
| Inferred operator/hybrid closure | Data-informed reduced dynamics or missing exchange | Requires suitable state/training data and physical constraints | Sparse probes do not supply full fields; extrapolation and stability conditional |
| Direct response surface/GP | Input-to-QoI mapping over a declared domain | Can be an inexpensive prediction benchmark | No automatic conservation, causal interpretation or unsupported-regime credibility |

Thermal-network structure selection is already substantial prior art. S26 jointly learns signed-latent/ReLU-gated structure and coefficients within a chosen network family (Eqs7–20, PDF3–6; S26-C01). Its posterior and physical-recovery qualifications matter: synthetic chains fail to mix, and the original Table 4 does not support reliable recovery of every finite physical resistance/capacity (S26-C03/C05, PDF7/10). The supplied supplement/repository addendum is part of its current dossier; old missing-supplement notices are historical. S67/S68/S70 add likelihood, profile and structural-reduction precedents. A conservative loop extension must demonstrate more than relabeling a building network.

Projection also has strong theory. S59 obtains a restricted asymptotic nonlinear subsystem from heating/geometry Fourier-support overlap (Theorem3.6, PDF12–13/1083–1084; S59-C04). This is stronger than generic few-mode fitting but does not make discarded sensor/extrema information vanish. S18's conjugate Fourier model couples modes through localized exchange, and its low-Pr fictitious-fluid CFD comparison is not direct validation for a high-Pr ACU/VCU loop (S18 dossier, §3/Eqs24–36, PDF6–7; comparison scope in §§4.2/4.5). POD, balanced or nonlinear/manifold approaches remain possible families, but the corpus has not technically cleared every one for implementation. Their names do not establish available state data or a fair advantage.

Bayesian operator inference propagates posterior-drawn operators through ROM integration, but posterior draws need not be stable (M-S04-01/02, §3/Algorithm1, PDF4–7; conclusion PDF18). NEMO's fast inverse treatment is conditional on its nonlinear parameter/linear inversion-variable structure and reduced inverse subspace; it is not general nonlinear loop calibration or total model-form UQ (M-S05-01/02, §2.1/Eqs1–4, PDF3–4; Eq14/PDF7). S24's stable quadratic-model original remains technically unread and is a conditional comparator, not an established implemented solution here.

## 4. Which closures can be transferred, and which require evidence?

Heat-transfer correlations are statements about geometry, boundary/source arrangement, property evaluation and regime. They are not material properties. Fully developed wall-heated pipe Nu values cannot be transplanted automatically to internally heated, developing, curved, mixed-convection or conjugate configurations. High Pr alone does not imply large Pe; \(Pe=Re\, Pr\). A fitted multiplier can absorb wrong power, area, sensor mapping or ambient loss rather than represent corrected physics.

S57 shows that friction-transition modeling and numerical diffusion can separately change stability predictions (§§2–3.1, PDF5–17). S60's local high-Pr measurements and CFD interpretations show nonuniform profiles, but its parameter sweep does not isolate Pr from all co-varying conditions (S60 dossier, §§3–4). S48 establishes adjoint QoI sensitivity for high-Pr natural circulation; comparisons of derivative methods verify sensitivities of the same model rather than experimentally validate that model (S48-C01–C04, §§2–3/PDF3–8 and AppendixB/PDF16).

The contemporary originals sharpen the limits. S19 uses an open-vertical-pipe correlation lineage for an analytical thermal/flow estimate; the original correlation's applicability was not independently audited in that pass (Eq24/PDF6, Ref29/PDF12; S19-C08). S20 uses steady first-order RANS and acknowledges limitations for shedding, substitutes thorium-bearing salt properties for original MSRE salt properties, and leaves experiments to future work (S20-C02/C03/C07, PDF3–4/8). S74's nearly matched Nu values apply the same Dittus–Boelter correlation to deliberately matched Re/Pr; they are consistency evidence, not independent heat-transfer validation (Table 4.10, PDF17; S74-C05).

For implementation, retain competing closures only when their differences affect the selected QoI over the actual facility envelope. State the relevant entrance/development lengths, mixed-convection measure, heating direction, roughness and property temperature. Test zero-flow and reversal limits; a forced-flow correlation or constant multiplier may become inappropriate there. Preserve closure derivatives in transient/stability analysis when the underlying law varies with flow. An elaborate universal closure search is unnecessary before establishing the simpler model's information support.

## 5. What does each sensor observe, and what remains unobservable?

S32 requires the measurand to be specified for its purpose, including spatial, temporal and reference conditions (§6, PDF13–15/5–7; S32-C01). This gives a precise reason to separate point, centerline, wall, area-average and mixing-cup quantities. VCU primary PTC readings are not established bulk-fluid temperatures; wall contacts are not fluid measurements. The ACU flowmeter is author-reported but its range, calibration and synchronization remain unverified project facts.

**Proposed observation notation** is

\[
y_k=\mathcal H_k[x, u;\eta]+b_k+e_k,
\tag{EQ-04}
\]

where \(\eta\) contains location/contact/response conventions, \(b_k\) shared or drifting bias, and \(e_k\) stochastic error under a justified dependence model. A first-order sensor-response state is an optional model requiring evidence, not an assumed instrument specification. Position and clock uncertainty can act like phase/transport error.

For a cross-section, an area average is \(T_A=A^{-1}\int_A T\, dA\). An enthalpy-transport average uses signed flux: \(h_m=\int_A\rho u_nh\, dA/\dot m\) where \(\dot m\ne0\). Temperature inferred from it requires the same enthalpy/property law. In counterflow or near-zero net flow, that ratio can be ill-conditioned; separate directional contributions and their definitions may be more meaningful. These are our conventional definitions, not new measured TRIDENT quantities.

S19's wall-to-fluid offsets and S29's local contours are model outputs. Neither is independently observed bulk temperature or local velocity truth (S19-C01/C06; S29-C02/C07). S29 explicitly lacks a primary flowmeter and obtains flow from cooler enthalpy balance; separately labeled “experiment” and “energy balance” curves do not establish independent provenance (Eq3/PDF9; Fig21/PDF28; §6/PDF30; S29-C10). Agreement among quantities sharing thermometers, properties and duty allocation must retain their dependence.

A scalar circulation estimate also does not determine a 3D recirculation region. Candidate descriptors include reverse-flow volume/area fraction relative to a declared local axial direction, separation length, exchange flux or regional signed transport. Threshold, frame, averaging and intermittency affect the descriptor. A global loop velocity is not an extent metric. Thermal consequences may be tested at measured locations even when flow extent cannot be recovered; a location or global-extrema claim requires stronger support.

## 6. Which parameters or predictions are identifiable?

For the proposed single-state balance

\[
C\dot T=\dot Q_{net}-G(T-T_a),
\tag{EQ-05}
\]

passive constant-ambient relaxation identifies \(G/C\), or \(\tau=C/G\), under the stated assumptions. Multiplying both free scales by the same positive number leaves that passive trajectory unchanged. An independently supported steady net duty at nonzero temperature rise can constrain \(G=\dot Q_{net}/(T_{ss}-T_a)\), after which \(C=G\tau\). Independently trusted inventory capacity is another anchor. This is our elementary derivation and diagnostic, not a proposed novel theorem. Unknown residual heater/cooler duty or initial solid storage can defeat its premises.

A multiregion network can retain ambiguities after one total-scale anchor. Excitation, boundary variation, initial conditions and observation maps determine which combinations remain supported. Sequential steady-G then transient-C fitting is defensible only when the same exchange model and operating assumptions apply, the steady anchor is independent and nuisance quantities do not change in an unmodeled way. Otherwise compare joint fitting or retain identified groups instead of assigning physical values by convention.

S23 profiles one parameter while reoptimizing all others (Eq10, PDF4/1926; S23-C02), distinguishes structural invariance from practical uncertainty (S23-C03), and shows Hessian/profile intervals can differ (Table1, PDF6/1928; S23-C04). Sensitivity rank/Fisher information are useful local diagnostics, not global identification certificates. Priors, bounds and regularization can stabilize a solution without creating information in observations. Bayesian marginalization integrates nuisance parameters; profile likelihood optimizes them. A likelihood-ratio threshold must match whether the objective is −logL or −2logL.

The thermal literature provides direct counterexamples to equating coefficient identification with material characterization. S69 shows good temperature predictions with input/observation-dependent parameters (Figures3–6, PDF5–7/267–269; S69-C03). S70 finds that total resistance can remain stable despite ambiguous internal coefficients, while effective capacity and free simulation can fail (Figures5–7, PDF13–17/456–460; S70-C03/C04). S68 changes observed wall/construction as well as sensor choice and tests structural reductions (S68-C01/C04, PDF4–7). Those results are conditional cross-domain methodology, not proof of the particular TRIDENT identifiable groups. Deriving and testing the latter remains research.

## 7. How should discrepancy be represented without concealing missing physics?

Output-level discrepancy and embedded discrepancy answer different questions. S72 writes observation \(y=h+E+\Phi\), calibrates discrepancy for each physical parameter vector, then chooses that vector with a goal-weighted error functional (Algorithm1, PDF13; S72-C01). It explicitly cannot directly propagate observation discrepancy to a different nonobservable QoI (§2.5/PDF7; S72-C02). Its final synthetic thermal-challenge example has disjoint calibration/validation scenarios, yet ordinary MLE has the lowest reported model-only validation metric (Table8/PDF24; S72-C04/C05). Goal orientation is not a guaranteed accuracy improvement.

S75 already provides an alternative for unobserved predictions. With a governing residual \(R\), an uncertain embedded closure \(\tau_m+\epsilon_m\) is used consistently in state, observation and target equations (Eq8a–c, PDF12; S75-C01). This creates a mathematical route for closure uncertainty to affect an unobserved QoI. It does not identify the correction uniquely, show that its prior/family is correct, or guarantee an informative prediction. Reliable governing and observation structure, verified numerics, trained/tested embedded-model conditions and target-sensitive evidence are assumptions and assessment requirements (§3.3, PDF19–23; S75-C02–C04).

For TRIDENT, a stochastic heat-exchange correction must preserve paired energy exchange and physical admissibility; a loss correction must not silently compensate for incorrectly deposited power. Observation bias, boundary error, parameter uncertainty and closure discrepancy should be separated as far as independent information permits. When they cannot be distinguished, report joint ambiguity and its QoI consequences. More flexible discrepancy can improve calibration fit while making mechanism attribution weaker.

S75's oscillator demonstration uses synthetic information states and an ensemble likelihood that independently draws a damping coefficient per datum (§4.2/PDF28; S75-C07). That is not a stochastic thermal trajectory model. S73 instead uses an Itô state equation with state-independent diffusion and discrete noisy observations (Eq1–2, PDF2/226; S73-C01). These are distinct stochastic structures and should not be blended as interchangeable “noise.”

## 8. What uncertainty should be propagated, and what would make it credible?

| Source of uncertainty | Representation to justify | Dependence and assessment issue |
|---|---|---|
| Sensor calibration, drift, timing and contact | Common effects plus channel/time residual structure | Shared systematic errors do not disappear by averaging |
| Inputs and energy scale | Net deposited power, secondary enthalpy/flow, ambient and residual duty | Commanded voltage is not watts; derived duties/flow reuse ingredients |
| Geometry and properties | Qualified ranges, correlations and uncertain fitted coefficients | One property-law draw must remain shared where it is reused |
| Initial fluid/solid/insulation states | Measured or inferred nuisance state with support | Hidden storage can mimic a capacity or exchange time scale |
| Parameters and topology | Likelihood/posterior/profile or a defensible set of alternatives | Bounds/prior/network family constrain apparent certainty |
| Reduction and closure inadequacy | Target-aware embedded or output discrepancy, with applicability | Flexible residual correction does not validate unobserved physics |
| Numerical/CFD reference | Solver, mesh/time, closure and input evidence | A computed field is not exact truth or an independent replicate |
| Domain transfer | Distortion and property/source/solid differences | Sampling within a surrogate model does not prove reactor transfer |

S32 explicitly treats shared effects as common inputs or covariance (§10.5, PDF43–44/35–36; S32-C03). For a vector measurement model, S31 gives first-order \(U_y=J U_xJ^T\) (Eq3, PDF23/15; S31-C01). The implicit form requires a nonsingular output Jacobian and discourages direct inversion (Eq8–10, PDF25/17; S31-C02). This local propagation is useful for well-conditioned regimes; near zero temperature difference, transition, reversal or a nonregular event, it may be inadequate.

**Proposed ratio example.** For inferred \(\dot m=\dot Q/\Delta h\), local propagation gives

\[
\frac{u^2(\dot m)}{\dot m^2}\simeq
\frac{u^2(\dot Q)}{\dot Q^2}+\frac{u^2(\Delta h)}{\Delta h^2}
-\frac{2\operatorname{cov}(\dot Q,\Delta h)}{\dot Q\Delta h}.
\tag{EQ-06}
\]

The equation does not account for omitted heat loss/storage or point-to-bulk bias unless those enter the model. Near \(\Delta h=0\), the ratio and its linear approximation can be ill-conditioned. S29's ±5.22% label does not supply a complete reproducible run-specific covariance budget (S29-C09, Table2/PDF9 and Fig21/PDF28); it is not a transferable total uncertainty bound.

Monte Carlo propagates a **specified joint input distribution**, not independent draws of every repeated variable. S02 separates formulation, propagation and summarizing (§5.1–5.3, PDF16/8) and samples the joint input law (Fig4, PDF23/15; S02-C01/C02). Its adaptive procedure checks estimates, standard uncertainties and interval endpoints, with stochastic tolerance limitations (§7.9.4, PDF40/32; S02-C03). Sampling convergence and model validity therefore need separate checks. Polynomial chaos/collocation, quasi-Monte Carlo or surrogates may reduce cost when smoothness, dimension and domain justify them; this corpus has not completed a method-specific technical assessment of every accelerator, so they remain optional rather than mandatory implementation choices.

Parameter covariance, a fitted-GP pointwise interval, a scenario envelope, a posterior predictive interval and an empirical coverage estimate must be labeled separately. S31's joint coverage regions differ from marginal intervals (§6.5, PDF27–28/19–20; S31-C03). S73's inverse-Hessian parameter uncertainty is local/asymptotic, not total predictive coverage (Eq53, PDF6/230; S73-C06). S75's observation-plausibility metric still requires predictive assessment and useful precision (Eq21/PDF19; S75-C05). Report bias, sharpness, dependence and predictive scores on independent cases where justified, with the uncertainty of that assessment. Do not claim a calibrated rare failure probability from a few runs or widen bands merely to cover every observation.

## 9. Which experiments would distinguish models or support predictions?

Four design objectives should remain separate:

1. **Parameter information:** reduce uncertainty in supported parameter combinations; S07 is an inspected nonlinear Bayesian-design precedent.
2. **Target information:** reduce uncertainty in a specified prediction; S71 maximizes expected target-information gain under a separate observation/target map (Eqs10–14, PDF5; S71-C01–C04).
3. **Model discrimination:** select conditions where competing physical descriptions make detectably different observations under nuisance uncertainty.
4. **Validation relevance:** choose a test that challenges the assumptions important to the intended target, rather than simply improving calibration.

S76 establishes the fourth objective as prior methodology. Its influence matrix is the gradient second moment \(M_h=E[\nabla h\nabla h^T]\); it selects a realizable scenario by matrix-distance matching, then an observable using trace-normalized matrices (Eqs14–17, PDF13–15; S76-C01/C02). It does not estimate target model error or guarantee the validity decision. Controls and sensor parameters are treated as certain, and the model parameter law is shared across scenarios (S76-C03/C08). A TRIDENT adaptation must confront those omitted nuisance uncertainties.

**Our checks:** under \(p=D\xi\), \(M_\xi=D^TM_pD\), so parameter scaling affects spectral-distance rankings even after overall output normalization. Also, adding a parameter-independent output bias leaves gradients unchanged while changing the answer. These are reasons to test scaling and model-error alternatives, not claims that sensitivity design has no value (S76-C04 and dossier derivation). The paper's synthetic example shows that matching initial Re alone can fail to expose a bad drag model; it does not prove dimensional analysis is useless (Fig5, PDF19–20; S76-C05).

A manageable first design comparison enumerates actual feasible choices before costly nested optimization. S71's MCMC/KDE estimator has bandwidth and sampling bias/cost; its synthetic transport example is not a loop validation and uses a pointwise surrogate split (S71-C04–C08). Oracle parameter initialization used for simulated utility calculations is not available during real inference. These computational details can alter the design ranking and deserve numerical assessment.

All changes below are **proposals to negotiate through Dr. Nick Luciano**, not approved or executed protocols. Exact instrument names/locations, rates, durations and repeats require the actual phase documents, facility capability and purpose; no safe setpoints are invented.

| Nick phase | Proposed scientific purpose | Evidence/request and role | Acceptance or reallocation issue |
|---|---|---|---|
| P0 | Define input/observation contract | Configuration, fluid identity, source deposition, sensor map, clock and calibrations | Resolve provenance before parameter interpretation |
| P1 | Qualify baseline/noise/shared effects | Ambient/equilibrium histories and repeated calibration checks if feasible | Separate repeatability of means from installed accuracy/shared bias |
| P2 | Constrain thermal ratios and hidden storage | Existing warm/cold relaxation and initial-condition procedure; compare observation/initial-state alternatives | Passive data alone need not establish absolute G and C |
| P3 | Assess frozen reduced predictions or supply an energy anchor | Independently supported steady net duty at accepted conditions if available | If a blind case is used to identify energy scale/losses, it becomes development evidence; reserve a new assessment case |
| P4 | Test retained transport and transitions | Independently varied feasible source/sink changes; synchronized secondary duty and thermal response | Do not count a thermal-balance flow estimate as independent of its ingredients |

The requested matrix is a literature-grounded rationale for a discussion, not evidence that every change is necessary. A simpler independently anchored model can be preferable to a sophisticated design whose nuisance inputs are unknown.

## 10. What counts as verification, calibration, validation or transfer?

**Code verification** checks whether implementation reproduces the mathematical model. **Solution verification** checks numerical error in the claimed output. **Calibration/selection** uses data to set parameters, topology, closures or observation conventions. **Independent predictive assessment** challenges the frozen physical and uncertainty model with new evidence. **Transfer assessment** asks whether that evidence justifies another scenario, quantity or circuit. S75 explicitly separates calibration, validation and predictive assessment (§3, PDF16–23; S75-C02). These categories must not be collapsed into a single “validated” label.

Numerical checks should include paired energy conservation, uniform-temperature equilibrium, passive exchange, source/sink sign, admissible parameters, zero-source/flow limits, steady recovery, signed circulation and target-specific mesh/time/modal refinement. A circulation-converged model need not have converged peak temperature, reverse-flow volume or event time. Keller/Welander and restricted Fourier models provide verification problems only when their own heat-law, mixing and inertia assumptions are retained (S54-C01–C04; S55-C01–C04; S59-C01–C04).

The recent comparators show the distinction in concrete form. S19's mesh table conflicts with the stated common adjacent refinement ratio (Table5/PDF5; S19-C05). S20 selects a medium grid using a location-C temperature peak, which is not evidence of converged recirculation extent (Table3/PDF5; S20-C05). S29 uses experimental agreement partly to choose mesh/time step and reports half-mesh-spread as uncertainty (PDF14–16; S29-C04/C05). None should be used as a blanket normative CFD-uncertainty template. ASME V&V20 has not been fully read, so no conformance claim is made.

Some S29 temperature bars are labeled |CFD−experiment| (Figure 19/PDF26; S29-C13); these are not independent metrology uncertainties. S19's “up to 5.5%” concerns a difference between comparison discrepancies, not direct measured flow accuracy (Table7/PDF8; S19-C04). Such source-specific caveats matter more to a fair assessment than borrowing a single attractive percentage.

Hold out complete runs/conditions when the claim concerns new runs/conditions. Random points from a shared field or time history can be useful for interpolation diagnostics but do not establish case transfer. Reusing a test to revise a closure, loss law, mesh, observation map or prior makes it development evidence for that claim. Report model-only and discrepancy-corrected outputs, one-step filtered estimates and autonomous forecasts separately. Dataset size is not the number of independent cases.

## 11. What should Codex implement, and in what order?

This is a **proposed staged comparison plan**, not authorization to process the held ACU data, run experiments or assume CFD. Each stage produces reviewable equations/configuration and tests on analytic or explicitly synthetic cases before a later authorized data application. Existing M1/M2/M3 labels are preserved.

| Stage | Concrete implementation product | Comparison and assessment | Stop/fallback condition |
|---|---|---|---|
| 0. Contract and conventions | Machine-readable geometry/source/state/observation/units contract; provenance and uncertainty dependencies | Reconcile configured equations with EQ catalogue; audit available versus unavailable inputs | Unknown net duty, fluid or observation meaning remains explicit; do not manufacture a validated case |
| 1. Existing steady baselines | Conservation/sign audit of M1/M2/M3 and a global balance | Common inputs/parameters; conditional M2 versus autonomous M3 scored for different contracts | Failure of energy closure or branch definition blocks further interpretation |
| 2. Small transient hierarchy | Grouped regional model and a conservative fluid–wall segmented alternative; insulation/axial states only as hypotheses | Synthetic invariance/recovery and nuisance-reoptimized profiles; same supported thermal targets | If evidence cannot distinguish states, retain groups or simpler structure |
| 3. Inference/UQ comparison | Covariance-aware constrained fit; optional S73-style stochastic fit and carefully defined discrepancy alternative | Same physical model, priors/bounds and information budget; free prediction distinct from filtering | Noise absorbs input/observation error or physical parameters are unstable; report conditionality |
| 4. Design and adequacy study | Finite feasible protocol comparison using parameter/target information, discrimination or S76-style validation relevance | Verify numerical utility/gradient/scaling; freeze choices before independent assessment | Ranking not robust to plausible nuisance/model alternatives; request metadata or narrow target |
| 5. Conditional enrichment and assistance | Optional reduced operator/closure/local reconstruction; operator-facing result contract with Ben Booth/NeutronOS | Case/regime-out evidence, qualified references, horizon/validity/uncertainty displayed | No qualified state/reference data: finish no-CFD core and omit local extent/control claims |

A fair first comparison need not implement every modern family. Start with the simple energy/regional model, one richer conservative model and a controlled inference comparison. Operator inference, neural models or full topology discovery earn their cost only when relevant state data and demonstrable target benefit exist. Instrument/CFD purchases are not prerequisites to completing the methodological core.

## 12. Equation and convention catalogue for implementation review

The catalogue retains scientific provenance and separates source equations from our conventional formulations. It is a starting specification, not a claim that all source solver details have been reconstructed. The companion `Implementation_Equation_and_Validation_Contract.md` records source ambiguities; the table below is canonical for this first review draft.

| Catalogue ID | Equation or operation | Definitions, units and checks | Provenance / limit |
|---|---|---|---|
| EQ-01 | Stored-energy balance with shared signed face/exchange rates | U J, rates W; sum internal rates to zero | Our conservative formulation; S52 Eqs7–23/PDF5–7 supplies related prior model |
| EQ-02 | Positive thermal network C_i dT_i/dt=Q_i+ΣG_ij(T_j−T_i)−loss_i | C J/K, G W/K; paired exchange; effective versus material meaning | Our notation; S26 Eqs1–14/PDF3–5; S66 Eqs1–6/PDF3–4 |
| EQ-03 | Signed circulation inertia/buoyancy/resistance balance | mdot kg/s; f_D versus f_F; K and area definitions; all pressure terms Pa | Our stated approximation; S52/S19/S29 are conditional source comparators |
| EQ-04 | Observation y=H[x, u;η]+b+e | Location/average/response/clock; bias dependence | Proposed contract; S32 §6/PDF13–15/5–7; S73 Eq2/PDF2/226 |
| EQ-05 | Single-state energy scale and τ=C/G | Known net duty or capacity anchor; residual duty/initial-state assumptions | Our elementary derivation; not a novelty claim |
| EQ-06 | Ratio covariance for mdot=Q/Δh | Q W,Δh J/kg; ill-conditioned near zero | Our local derivation; S29 Eq3/PDF9 provides inference example |
| EQ-07 | h(T)−h(T*)=∫cp(T)dT; Qrad=εσA(Tw⁴−Tsur⁴) | cp J/(kgK), h J/kg; radiation temperatures K | Conventional proposed implementation; source/view-factor and property validity required |
| EQ-08 | SDE dx=fdt+σdW; yk=h(xk)+ek | Itô;σ state/√time; measurement covariance observation² | Reported S73 Eq1–2/PDF2/226; state-independent diffusion |
| EQ-09 | Pdot=AP+PAᵀ+σσᵀ; R=CP Cᵀ+S | Local Jacobians, substeps, initial covariance; singular-A handling | Reported S73 Eq12/18–26/PDF3–4/227–228; Gaussian/local approximation |
| EQ-10 | −logL=½Σ[logdetR+innovationᵀR⁻¹innovation]+constants | Missing channels reduce likelihood dimension; prior/MAP normalization declared | Our Gaussian rearrangement; S73 Eq6–10/44–52/PDF3,5–6 |
| EQ-11 | Uy=J Ux Jᵀ; Cy Uy Cyᵀ=Cx Ux Cxᵀ | Local linear explicit/implicit covariance; avoid unstable literal inverses | Reported S31 Eq3/8–10, PDF23/25, printed15/17 |
| EQ-12 | Joint-sample propagation X^(r)→f(X^(r)) | Reuse common variables; numerical tail/endpoint tolerance | Reported S02 Fig4/PDF23/15; §7.9.4/PDF40/32 |
| EQ-13 | Embedded discrepancy R(u,τm+εm; r)=0 with common observation/target maps | Correction units and physical constraints; tested closure domain | Reported S75 Eq8a–c/PDF12; does not guarantee identifiability |
| EQ-14 | U(d)=E_y KL[p(z\mid y,d) ∥ p(z)] | Dimensionless nats; fixed target definition, prior/likelihood and joint dependencies | Reported S71 Eqs10–14/PDF5, arXiv v2; estimator error assessed |
| EQ-15 | Mh=E[∇h∇hᵀ]; scenario/normalized-observation matrix matching | Parameter nondimensionalization; positive trace; regular functionals | Reported S76 Eq14–17/PDF13–15; relevance criterion, not error bound |
| EQ-16 | Profile likelihood reoptimizes nuisance quantities | Objective factor−logL versus−2logL; bounds/multistart; not marginalization | S23 Eq10/PDF4/1926; S67/S68/S70 comparators |

No literal production transcription is cleared for flagged source equations: S19 energy definition/sign and grid ratio; S72 likelihood direction, covariance prefactor and validation-RMSE normalization; S73 damaged extracted symbols and wall area/units; S29 pressure-current units, loss formulation and plot/flow provenance; S74 source/solid normalization and hydraulic diameter; S75 manuscript date/noise/thermal normalization; S76 derivative/coordinate conventions. A flag identifies ambiguity, not a proved bug in the authors' executed code.

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
