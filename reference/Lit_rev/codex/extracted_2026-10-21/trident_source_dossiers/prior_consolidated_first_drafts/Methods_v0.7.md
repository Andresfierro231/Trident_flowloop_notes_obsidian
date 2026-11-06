# Methods and theory for TRIDENT thermal-hydraulic reduction

**Working review v0.7, 21 October 2026.** Integrated with purpose-scoped S19/S29/S71v2/S72final/S73/S74 dossiers. S75/S76 are newly retrieved but technically unread. This is a substantial methods/theory working synthesis, not a validated implementation, exhaustive review or selected thesis direction.

## 1. The predictive task determines the model

TRIDENT's methods problem is to predict useful thermal-hydraulic quantities from independently available inputs with sparse observations. The steady task includes heat removal, losses, circulation and thermal margins; subsequent stages concern transitions and operational what-if assistance. A model supplied measured later fluid-temperature histories solves a conditional wall-response problem. A model supplied heater/cooler/ambient conditions and initial state to predict later fluid temperatures solves a different, autonomous task. Their accuracy cannot be compared without declaring this distinction.

Existing loop literature makes the distinction consequential. LeBENC incorporates nonuniform flow area, fluid/wall thermal states, axial conduction and losses, but S52 infers cooler and regional loss coefficients using experimental thermal balances (§§4.1–4.6,PDF5–8). S50 similarly fits/applies ambient coefficients across operating powers (§4.1,PDF7). Those are valuable physical baselines; their agreement does not establish a wholly independent prediction of the same measurements used to characterize exchange. Current M1/M2/M3 implementations are project facts, not validated models.

For each candidate, specify inputs, states, outputs, observations, adjustable parameters, fixed independently supported quantities, calibration data and withheld assessment data. The same contract must govern every comparison.

## 2. A model hierarchy worth testing

| Family | Retained information | Main value | Critical qualification |
|---|---|---|---|
| Global steady energy balance | Total duty/loss and selected temperature differences | Energy consistency and measurement qualification | Does not uniquely identify regional losses or circulation |
| Regional effective thermal network | Participating storage and inter-region exchange | Interpretable response/settling with few states | Effective states and coefficients need not equal bulk-fluid temperatures or material properties |
| Separate fluid/pipe/insulation network | Distinct storage/exchange paths | Compare wall response, contacts and delayed losses | Sparse observations may not distinguish every path |
| Conjugate 1D finite-volume loop | Signed circulation, advective transport, wall coupling and spatial loss | Direct conservation and component-level physical comparison | More closures/parameters; numerical diffusion can affect dynamics |
| Fourier loop reduction | Mean temperature plus spatial modes and circulation | Low-dimensional dynamics and stability | Truncation may preserve global response while missing local extrema or observation detail |
| Inferred or hybrid dynamical model | Learned operators/closures with selected physical constraints | Test whether data support a better reduced description | Requires an appropriate state/data basis and explicit extrapolation/UQ limits |

These alternatives have established precedents. S52 is a conjugate finite-difference model; S30 is an eight-state Fourier circulation/thermal system (§2,PDF3–6). S18's inspected preprint couples two buoyancy-driven loops through a conducting/storage wall with Fourier modal convolutions; its journal/preprint comparison remains pending. S08 supplies a cross-domain grey-box selection precedent; S26 supplies Bayesian thermal-network discovery. Their existence rules out generic “physical network,” “learned thermal topology,” or “few-state ROM” novelty.

## 3. Conservation, source deposition and state meaning

Reported equations should be treated as scientific evidence rather than trusted code specifications. The S52 dossier records source-unit, wall-area, signed-drag and discrete-coefficient ambiguities. The S30 dossier records reversal-sign, Fourier-forcing and stochastic-convention ambiguities. None is an established finding about the inaccessible executed code.

An independently derived finite-volume implementation should use one fluid-wall heat rate with opposite signs in the adjoining energy balances. It should use actual inner/outer surface areas, conservative advective enthalpy fluxes, explicit source deposition and consistent property conventions. Its invariant/limiting checks include closed-system total energy, uniform-temperature equilibrium, passive exchange, zero-source limits, signed circulation and refinement. For variable heat capacity, enthalpy is an integral of cp; cp(T)T is not generally an energy state.

A regional state combining participating fluid, pipe and insulation storage can be useful, but its measurement map must explain how a wall or centerline sensor observes that state. Fitted effective conductance/capacity can compensate for omitted flow, boundary error or sensor response; physical naming alone does not establish unique material interpretation. The Nick-plan reconciliation also identifies the need for local balance/uniform-equilibrium checks in directed thermal networks.

Source location matters for transfer: heater energy deposited in a wall, an immersed element, or circulating fluid does not have identical thermal dynamics. S56 explicitly includes solid source scaling. S66 now supplies a directly inspected two-shell wall/internal-generation comparison; S65 now supplies the complementary source-partition/stability comparison, with its operating-curve and linearization limits retained.

## 4. Closures and local multidimensional effects

S57 provides a strong reason to treat closures as competing hypotheses. Changing the friction-transition law changes predicted stability for a water loop; first-order numerical diffusion separately changes growth and damping (§§2–3.1,PDF5–17). Neither result supports one universal natural-circulation multiplier. The paper's friction graph uses Fanning factors; S30 uses Darcy factors. Transformation must include the governing pressure-loss convention, not only the factor's name.

S60 demonstrates local high-Pr velocity nonuniformity using planar PIV and CFD (§§3–4). It also shows why a bulk-flow model and a centerline observation can disagree without uniquely identifying the missing mechanism. Its3D helical-flow interpretation is supported by combined evidence rather than measured full-volume velocity; its power/temperature/Pr sweep does not isolate Pr causally. Thus a proposed local-recirculation closure needs a defined descriptor, observable consequences and a qualified reference.

Fully developed Nu4.36 or standard forced-flow correlations require the correct geometry, source/boundary condition, development and regime assumptions. High Pr alone does not prove advection dominance: Pe also depends on Re. Simultaneously developing, mixed-convection and property-varying cases should be compared where our actual envelope requires them. S45 remains a targeted mechanism source; its full extraction is pending.

## 5. Identifiability and observations

Sparse temperatures may support a good predictor without uniquely identifying every physical coefficient. S06 explains calibration/discrepancy confounding. S23's now-inspected main paper distinguishes states, inputs, initial conditions and observation scale/offset, and profiles a parameter by reoptimizing the others (Eqs1–3/10,PDF2/4). Its detailed algorithm supplement remains unread.

Our simple energy-scale example illustrates a necessary diagnostic, not a new contribution:

\[
C\dot T=Q-G(T-T_a).
\]

For a passive constant-ambient cooldown, temperature dynamics constrain G/C. Independently known steady net duty at nonzero temperature rise can constrain G; independent inventory capacity is another anchor. A network can remain non-identifiable after that global ambiguity is removed. Inputs, regional losses and observation offsets can introduce further confounding.

Heater-side and cooler-side thermal-balance flow estimates share measurements and loss allocations. Their compatibility does not establish independent flow accuracy. As shown in the prior checkpoint, shifting heat loss between regions can preserve total loss and nearly preserve flow-estimate compatibility. The thesis must distinguish supported parameter combinations, measured thermal predictions and independently supported circulation.

## 6. Uncertainty must be attached to a prediction contract

Maintain separate uncertainty objects for measurement/calibration and covariance, inputs, initial states, properties, fitted parameters, model/reduction discrepancy, numerical solution and any CFD reference. Dependence matters: an instrument, property fit or derived duty appearing in several equations remains the same uncertain quantity. A probability distribution also requires justification; an unknown systematic bias need not become an independent Gaussian draw.

S73 gives a foundational continuous–discrete stochastic grey-box model, with Itô dynamics and discrete noisy observations (Eq1–2, PDF2/226). Its EKF likelihood approximates nonlinear conditional densities as Gaussian; diffusion is independent of state. Diffusion intensity has state²/time units, while measurement covariance has observation² units. They cannot be interchanged by using the same numerical variance. The two-state thermal-wall example is established prior art, although its simulated conductive wall contains no circulation momentum or advection (S73-C01–C03/C07).

A process-noise fit can improve a predictor without identifying the omitted mechanism. S73's inverse-Hessian uncertainty is local/asymptotic, and its reported comparisons use single simulated datasets and optimizer-start checks rather than a large coverage experiment (S73-C06/C08). A filtered one-step estimate, an autonomous forecast, a parameter confidence region and an interval for a future physical observation are different products. The comparison must name which is assessed.

S72 adds a distinct discrepancy representation: observed y=h(χ,θ)+E(χ)+Φ(χ), with independent GP discrepancy and observation error. Its procedure fits discrepancy for each physical θ and then minimizes a predictive-purpose-weighted discrepancy functional (Algorithm1, PDF13). The fitted pointwise normal quantile error is not a simultaneous-domain bound or uncertainty integrated over all hyperparameter choices (S72-C01/C08). Crucially, this output-level correction does not directly propagate to a different, unobserved QoI (S72-C02). An uncertainty band around fitted sensor temperatures therefore cannot be relabeled as an uncertainty band on a local velocity, global temperature minimum or freezing event.

S26/S04 operator or network posteriors, S30 fluctuation forcing, S51 reliability sampling, S73 diffusion and S72 discrepancy represent different uncertainties. Combining all of them without a generative/dependence model risks double counting the same residual. Official JCGM guidance anchors measurement definitions and propagation; structural discrepancy and predictive assessment require additional evidence. Available S75/S76 manuscripts are queued to challenge the unobserved-QoI and validation-design argument, but their methods remain unread.

Assess bias, dependence, sharpness and interval coverage on independent runs where sample size permits. Report uncertainty in that assessment. Neither a chosen posterior nor nominal 95% bands prove empirical 95% predictive coverage. A few stochastic trajectories do not establish a small failure probability.

## 7. Stability, transient response and numerical verification

Distinguish steady equilibrium, local linear stability, finite-disturbance behavior, finite-time thermal margin and long-time stochastic escape. S57's discrete amplification matrix and S30's continuous ODE Jacobian are not interchangeable. S57 also contains some RELAP pulses involving voiding; they must not be used as single-phase evidence.

Verification should target the claimed quantity: a converged bulk temperature need not establish converged local extrema, vortex extent, growth rate or reversal time. S60's mesh study and limited velocity comparison cannot substitute for TRIDENT CFD qualification. A reference calculation requires independent boundary/input provenance, property laws, spatial/time refinement and evidence concerning model assumptions.

For the minimum experimental program, preserve Nick's existing covariance/autocorrelation work and model freeze/holdout safeguards. Resolve preparation and sensor-map contradictions before interpreting data. If a dataset is used to select topology or revise a closure, reclassify it as development evidence and obtain a new holdout for the affected claim.

## 8. Experiment design and achievable contribution

Prioritize experiments that distinguish plausible models or reduce uncertainty in a decision-relevant QoI. Repeated passive relaxation may qualify noise/response ratios; independently anchored duty or capacity may address scale; distinct thermal conditions may discriminate loss/transport assumptions. Each proposal must be negotiated through Nick's plan, with actual controls, initial conditions and accepted operating limits.

S07's now-inspected Bayesian design formulation explicitly distinguishes parameter inference, prediction and model-discrimination objectives (§2.1,manuscriptPDF4), while demonstrating parameter-information designs. Information about all parameters is not automatically the most useful objective; prediction or model-discrimination utility may better match the thesis.

The most defensible candidate core is a reproducible, conservation-consistent procedure linking retained physics, identifiable parameter groups, feasible experiments and independently assessed QoIs. Demonstrating this procedure across held-out conditions could advance understanding. Whether it is novel requires the pending comparisons; no theorem, accepted model or final direction is claimed.

## Completion gates

The physical-interpretation/input-error, source/similarity and decisive theory/loop comparisons now have scoped dossiers. Remaining gates are the actual operating/sensor contract, declared comparator performance, permissible calibration and unobserved-QoI/validation-design checks. S23/S67/S68 now have scoped dossiers. Relevant supplements and journal/manuscript comparisons remain explicitly limited. No operating-data processing, experiments, automatic control or TRIDENT CFD has been performed.

## 9. What the early loop theory can and cannot provide

Keller's exact solution and Welander's instability analysis offer distinct analytical models, not interchangeable justification for a generic “loop ROM.” Keller transports temperature around a constant-area rectangular loop, with point heater/cooler maps depending on flow. The special exact periodic solution removes momentum inertia and uses discontinuous exchange while retaining positive circulation (S54,§5,PDF4–6/602–604). The continuous-law extension establishes steady-state instability, rather than a universal attracting periodic orbit. Constant electrical power and finite walls are different source/state assumptions.

Welander uses prescribed-wall-temperature exchange, linear resistance and cross-sectional mixing. A thermal disturbance is advected; the phase between thermal pockets, circulation and exchanger residence time can amplify an oscillation (S55,§§2–6,PDF4–14/20–30). The mixing assumption is an explicit limitation in laminar flow. A temperature network that loses that circulating phase may miss the mechanism, but the paper does not prove that phase-resolving advection is needed for every measured relaxation.

This comparison explains why “thermal inertia” must be specified: fluid/solid heat capacity, momentum inertia and advective transport time are separate quantities. Keller's inertialess example does not refute the inertia balance in Welander's different heat-exchange problem. Both are useful verification cases only after their original sign, coordinate and heat-law conventions are resolved.

## 10. Exact reduction is a qualified prior-art benchmark

S59 gives a more rigorous reason to compare reductions by their prediction target. For prescribed spatial heat flux, scalar velocity and positive diffusion, Fourier transport has the reported structure
\[
\dot a_k+(2\pi ikv+4\pi^2\nu k^2)a_k=b_k.
\]
The nonlinear circulation subsystem is associated with the overlap of heating and geometry Fourier supports. A finite overlap permits an exact low-dimensional asymptotic subsystem under the paper's assumptions (Theorem3.6,PDF12–13/1083–1084). This already establishes considerably more than a generic claim that “a few modes can describe convection.”

The omitted modes may nevertheless carry sensor or temperature-extrema information. They can be forced and reconstructed through additional equations/history; exact asymptotic circulation reduction does not imply exact finite-time field reconstruction from the retained circulation variables. State-dependent, spatially localized heat exchange, conjugate walls and evolving source distributions can also break the simple diagonal modal structure.

The prospective TRIDENT theory question is therefore narrower: can a finite-time, observation/QoI-specific criterion identify when discarded thermal modes or wall states change the supported prediction beyond an accepted error budget? Such a result must identify its class of source/closure laws, observation maps and perturbations. It cannot be claimed merely by fitting a Fourier truncation or citing an inertial manifold.

## 11. Wall/source effects challenge a simple state-enrichment novelty claim

S66 explicitly separates fluid, inner wall and outer wall dynamics, includes distributed fluid generation, and retains the flow derivative of heat transfer in the linearization. Its logarithmic slope \(B=(G_0/h_0)(\partial h/\partial G)_0\) matters even if the equilibrium heat-transfer coefficient is fitted correctly (Eq46,PDF6/416). Matching a steady temperature profile alone may therefore leave transient stability poorly specified.

The study also separates a localized wall heater from distributed wall heating and fluid generation. For one long/slender analyzed case, distributed external heating outside the cooler approximates selected internally heated stability behavior; it does not reproduce every source-path transient or local field (Fig13/§7,PDF12/422 and18/428). This is a useful model-form comparison and a strong challenge to broad surrogate claims.

Two implementation cautions are consequential. Its capacity ratio is fluid/wall, so larger relative wall storage means a smaller ratio at fixed fluid. Its Table1 diameter differs by a factor of ten from the diameter implied by the stated length/diameter ratio. Those printed facts are retained in the dossier rather than repaired silently. Modelica/RELAP/CFD comparisons are verification/intercomparison evidence; the authors explicitly leave experimental validation to future work.

## 12. Local stability, finite disturbances and stochastic events need different tests

S63 numerically demonstrates a selected loop's different response to small and large initial-flow perturbations at the same linearly stable condition (§3.2,Figs6–7). That is strong motivation to distinguish local eigenvalue stability from finite-disturbance recovery, but the inferred unstable-cycle structure is not a complete basin certificate. Its finite-grid chaos diagnosis likewise does not replace a reproduced dynamical-systems analysis.

S62 adds a different distinction. For one post-bifurcation model, stochastic minor-loss forcing changes first-reversal time substantially, whereas much of the recurrent dwell-time distribution changes less (§IV,Figs2/4). OU noise approximates a common-DNS-data bootstrap benchmark for those studied outputs. It is not an independently calibrated loop-loss distribution, a total predictive uncertainty budget or a reactor damage-time prediction.

The paper's fitted log-plus-linear CDF and printed PDF contain a derivative mismatch; the dossier gives the reported equations and our differentiation separately. Nonexponential dwell times challenge a simple memoryless switching law, but do not by themselves exclude a Markov process with a richer state. This distinction matters when choosing statistical model classes.

For TRIDENT, compare models first on supported thermal/duty/response outcomes. Add reversal-time or stochastic escape predictions only after establishing a relevant operating regime, an observable event definition, a justified disturbance/noise model and numerical convergence of that event distribution. A stochastic closure should earn its complexity through improved independent prediction, rather than be included because stochastic loop models are modern.

## 13. A conjugate Fourier comparator sharpens the implementation requirements

S18 extends Fourier modelling to two loops coupled through a heat-exchanger wall, retaining both wall and fluid axial diffusion. The localized heat-exchange operator couples Fourier modes through convolution, unlike S59's restricted fixed-source thermal structure. Three retained orders mean conjugate mode pairs and means across several fields, not three total states (S18,§3,Eqs24–36,preprintPDF6–7).

Its value is a physical/reduction baseline; its direct transfer is limited. The CFD comparison uses a fictitious fluid with Pr.000125, square ducts and both sides buoyancy-driven. The heat-transfer correlation is selected for that lowPr regime. VCU's actual glycol circuit and secondary cooling contract require their own closure justification.

The inclination correction is obtained from the same CFD study subsequently used for the corrected comparison. It demonstrates a possible closure-enrichment workflow, but does not supply an independent predictive assessment. Similarly, mode/grid independence is assessed through circulation and average temperature rather than every local quantity (S18,§§3.6/4.2/4.5,PDF10/13/17–19).

The preprint also illustrates why a theoretical review should produce checked equations rather than a collection of copied formulas. Source selectors, dimensional cooling sign, a wall-equation variable, modal prefactors and real/imaginary conventions need reconciliation. Its large-step sensitivity ratios do not establish that wall parameters are negligible for a declared tolerance. These observations remain specific to the inspected preprint; the final journal text and executed solver have not been compared.

## 14. Design for an identifiable and assessable prediction

S07 distinguishes parameter, prediction and model-discrimination utility. S71 now supplies a nonlinear predictive design comparator: a separate observation map y=G(θ,d)+ε and target z=H(θ,η), with utility U(d)=E[KL(p(z|y,d)||p(z))]=I(z;y|d) (arXivv2, Eq1–14, PDF3–5). Its synthetic examples demonstrate that parameter-information and target-information designs can differ. This is established methodology; using the phrase “QoI-driven experiment design” is not a new contribution (S71-C01–C03).

The expectation is conditional on a prior, likelihood and valid observation/target mapping. A highly informative design under an incorrect source or closure can be confidently misleading. An EIG utility is also not an engineering loss or cost criterion by itself. For TRIDENT, compare feasible existing protocol choices and existing observation times before considering new sensors. Repeats may qualify bias and dependence; an independent energy anchor may break scale ambiguity; independently varied boundaries may discriminate storage from transport. No safe setpoint, repeat count or unrestricted control authority follows from S71.

The computational design calculation needs verification. S71 uses nested Monte Carlo, MCMC, KDE and Bayesian optimization; bandwidth and posterior sampling can shift utility estimates and selected designs (S71-C04/C08). Its transport example uses prescribed velocity, synthetic data and a pointwise DNN split, rather than buoyancy-coupled loop experiments (S71-C05/C06). The published flux definition is diffusive, with integration limits that differ from the stated region-of-interest boundary; do not borrow it as a total heat-flow functional (S71-C07). Mixed/discrete target distributions also require an appropriate probability measure, rather than unquestioned continuous KDE.

Calibration has a separate goal. S72 fits a discrepancy at every physical θ, then selects θ using a goal-weighted quantile-error functional. Its final thermal-challenge example has disjoint synthetic calibration and validation scenarios. Goal2 improves its validation metric over goal1 and KOH, but ordinary MLE performs better than both goal fits (Table8, PDF24; S72-C04/C05). This rules out an assumed universal accuracy benefit. Its printed Eq28 likelihood direction and Eq46 normalization are flagged; absolute reported RMSE values should not become acceptance thresholds until clarified. S72 leaves existence, uniqueness, stability and principled observable-to-target weighting open (S72-C06–C10).

Use a fair comparison: the same physical hierarchy, information budget, nuisance uncertainty and development cases; then compare covariance-aware MLE, a justified stochastic baseline, and a goal/discrepancy alternative only when its added assumptions are supportable. Freeze model structure and settings before final withheld assessment. A case used to choose an observation map, closure, heat loss, mesh or time step becomes development evidence for that claim. Model discrimination, calibration design and validation-scenario design must remain distinct.

S67/S68/S23 already join thermal networks, profile likelihood, sensor choice and structural reduction. S69/S70 already challenge material interpretation of identified coefficients. The additional research result must concern a defined conservative loop/model class, consequential uncertainty and supported prediction, rather than integration of these existing tools. S75/S76 are the next targeted prior-method checks, already retrieved; no further unrestricted discovery is required to continue writing.

## 15. What thermal-network identifiability already accomplishes

S67 estimates a two-state conductive network using a component-list simulator and Gaussian innovation likelihood. It includes the covariance normalization term, compares filter/discretization methods and examines profiles whose shape changes with parameter bounds. These are important baselines for TRIDENT's inference workflow, although the demonstrated network contains no circulation momentum or advection.

S68 goes further than a generic sensor-placement argument: it compares two wall-temperature observations, examines joint parameter dependence, and tests structural reductions. One storage-removal attempt fails residual assessment, whereas deleting a direct heat-loss branch yields bounded profiles after refitting. Stable total resistance and a wall time-scale combination occur despite different fitted component values (Table3,PDF7/57). This is direct prior art for grouping parameters according to the information in data.

The sensor comparison also changes the material construction and physical wall observed. It cannot isolate placement as the only cause of an altered capacity or confidence profile. For TRIDENT, a centerline temperature, contact-wall reading and regional bulk state likewise require distinct observation maps. A better fit after changing an observation definition can alter what the fitted state represents.

These papers also impose implementation safeguards. Profile curves reoptimize nuisance parameters, whereas Bayesian marginalization integrates them. A confidence cutoff must use the same normalization as the objective: −logL and−2logL differ by two. S67's printed ratio identity needs reconciliation before reproduction. Serial whiteness, marginal Gaussianity and independent predictive coverage need separate checks. A filter-assimilated band on calibration data is not a held-out forward-prediction interval.

The prospective advance must therefore be more specific: an identifiability or adequacy result for a defined class of conservative thermal/advective models, under uncertain boundaries and actual observation maps, plus a demonstrated independent consequence for a chosen prediction. S69/S70 establish important physical-interpretation and data-error counterexamples; S71/S72 now establish strong goal-oriented prior art and limitations. S75/S76 must test the remaining unobserved-QoI/validation-design argument; no unoccupied niche has yet been certified.

## 16. Physical meaning is a separate requirement from identifiability

S70's simulated cavity-wall study directly challenges an inference shortcut. Internal coefficients can be non-identifiable while total resistance is robustly estimated; conversely, an identifiable low-order model can allocate its resistances/capacitances differently from actual material layers (S70,Figures5–6;Discussion,PDF21/464). Neither a good fit nor a bounded parameter profile alone establishes a material-property interpretation. This requires an appropriate reduction, observation/source mapping and independent physical support.

S69 shows why input and observation models belong in the comparison. It prescribes radiator-delivered heat to exclude upstream heating dynamics; a model supplied electrical consumption would solve a different problem unless it modeled that path (§4,PDF3–4). It also uses virtual component heat fluxes to strengthen physical-parameter inference, despite useful temperature-only prediction. Those channels are not assumed available in TRIDENT. Biased observations can change coefficients without a comparable temperature-RMSE change (§5.3,PDF10/272), so improving a temperature fit does not uniquely identify a missing heat-transfer mechanism.

Model assessment should therefore separate observed-temperature prediction, parameter or aggregate inference, and held-out engineering output. S70 rejects first-order models on free-simulation diagnostics even though one-step residuals look acceptable. S69 finds longer-horizon degradation for an overcomplicated case. These results support use-specific horizons and independent assessment rather than treating the best filtered fit as decisive.

Implementation needs the original conventions. S69's printed stochastic Eq1 lacks drift dt; our conventional SDE interpretation is explicitly labeled in its dossier. S70's Table1 capacities do not sum to its reported total; its noise-amplitude terminology also needs care. No benchmark constants are silently repaired. S73, the retrieved foundational stochastic-estimation article, awaits technical extraction before claiming a complete likelihood implementation specification.

For a potential thesis advance, the unresolved task is to establish which loop-specific output or parameter combination is supported under realistic source, observation and retained-physics uncertainty. Existing thermal profiling and aggregate examples rule out novelty based on those ingredients alone. The detailed comparative plan and contribution falsifiers are in Physical_Interpretation_and_Data_Error_Synthesis_2026-10-20.md.

## 17. Source and fluid/solid scaling belong in the model contract

S64 develops geometric/fluid and solid-interface/transient matching, rather than relying on a similar Prandtl number. Its Eq8–10 distinguish conductivity/interface scaling from solid diffusivity/time scaling (PDF6/349). Even group-matched examples retain viscosity-variation distortion. A physical hierarchy should therefore declare its dimensional scales, property envelope, wall storage, external losses, source/sink and initial histories before claiming transfer. Its numerical radiation illustration has a flagged inconsistency; only the conditional radiation requirement is used here.

S65 provides a close1D conservation/stability comparator with localized wall and uniform fluid sources. The energy equation includes internal generation in the cooler, while the source-share variable α uses a temperature rise generated outside it; our dossier preserves that definition. Constant-wall-temperature exchange, no wall storage, no fluid axial conduction and frozen linearized heat-transfer/transition factors sharply limit direct transfer. The printed Stanton nomenclature and local-loss convention also need reconciliation before transcription.

The studied source/geometry changes alter dimensionless stability regions, but the authors did not map actual fluid-specific operating trajectories onto them (§4.2,PDF9). Agreement between two calculations is useful verification rather than independent experimental validation. These distinctions prevent a broad claim that internal heating necessarily destabilizes our actual operating range, or that matching power makes an external heater a reactor source surrogate.

For Codex, use the reviewed models as a hierarchy of assumptions to test. Begin with observable thermal/duty/response outputs, explicit mass-flow versus mass-flux and point-versus-bulk conventions, correct conservation/source units and independently supported boundary inputs. Add closure, wall or spatial complexity when it changes a declared prediction beyond tolerance and the evidence can distinguish that change. Exact derivative treatment and grid/time convergence matter especially for stability/event outputs.

## 18. Contemporary loop evidence and the minimum comparison

S19 and S29 bring the methods review close to the intended application. S19 compares external surface temperatures with steady CFD under measured thermal boundaries and derives circulation estimates from thermal information. The reported “up to5.5%” concerns a change in discrepancies between comparison methods, not independently measured flow accuracy (S19-C01–C04). Its CFD vortices and wall-to-fluid offsets remain modeled quantities. The grid-ratio inconsistency also prevents adopting its reported numerical uncertainty without clarification (S19-C05–C07).

S29 compares a Therminol-66 loop with loss-inclusive and adiabatic CFD. Cooler enthalpy balance supplies primary-flow estimates; no primary flowmeter exists. Temperature agreement improves when losses are included, but circulation and settling-time discrepancies remain material (S29-C01/C02/C06). Some temperature-plot bars are explicitly CFD–experiment differences, not instrument uncertainty (S29-C13). Mesh/time choices partly use experimental agreement and no locked independent partition is demonstrated (S29-C04/C05). These papers establish useful prior experiments and workflows; they do not independently validate every local field or determine which omitted mechanism caused each residual.

S74 supplies modern high-Pr oil/reference-design similarity analysis under simplified 1D, constant-property assumptions with no external loss and negligible leg-wall inertia. Its near-equal Nu values use the same correlation at matched Re/Pr, so they test consistency rather than independent physical transfer (S74-C01–C05). S29's actual tested Pr range is not established as molten-salt matched despite the oil being a candidate surrogate (S29-C08). Fluid selection, achieved similarity and engineering output-error bounds are three separate claims.

| Minimal comparator | Purpose | Evidence needed | Fair limitation |
|---|---|---|---|
| Energy balance plus a small effective thermal network | Duty/loss consistency and supported response ratios | Actual inputs, observations, initial-state and energy-scale support | Can defeat a complex model; coefficients may remain effective |
| Conservative segmented fluid/wall model, with only justified insulation/transport states | Test retained storage and transport against thermal/duty/response QoIs | Geometry/source and boundary contract; observable parameter groups | More physical detail can reduce practical identifiability |
| Covariance-aware deterministic versus stochastic grey-box inference on the same model | Separate inferential benefit from state/closure benefit | Noise/dependence model, repeated and held-out runs | Diffusion is not an identified mechanism or full discrepancy budget |
| Goal/discrepancy or design alternative | Test whether a declared target or ambiguity benefits | Separate observation/target map and feasible design set | Compare against MLE and simple designs; sensitivity to assumptions matters |
| Learned operator/closure or local reconstruction | Conditional extension when the necessary state/reference evidence exists | Qualified training data and case/regime-out assessment | Sparse sensor histories alone do not provide full fields |

This is a literature-grounded comparison recommendation, not a selected thesis method or an implementation result. S24/S03 remain relevant only if the learned alternative's data/constraints justify it. The next available readings are S75/S76 for unobserved-QoI/validation-design credibility, followed by targeted metrology S02/S31/S32. S20 remains conditional on pursuing local-flow claims; its absence does not block a thermal/duty/response core.

Before coding a final method, use the companion Implementation_Equation_and_Validation_Contract.md to retain units, probability conventions, limiting cases and source defects. Do not copy an ambiguous printed equation into production code. The comprehensive reviews remain working drafts: incomplete supplements, exact journal/manuscript comparisons and project decision tolerances are still recorded as gaps.
