# Methods and theory for TRIDENT thermal-hydraulic reduction

**Working review v0.3, 2026-10-20.** This connected draft includes the six-source batch plus scoped technical extraction of S18 and S07. It is not a completed systematic review, final method selection, or implementation specification. S23 full text is currently inaccessible; S67 is a newly verified abstract-level thermal-network comparator. Stable S IDs resolve to the registry and dossiers. Reading and reproduction are distinct.

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

Source location matters for transfer: heater energy deposited in a wall, an immersed element, or circulating fluid does not have identical thermal dynamics. S56 explicitly includes solid source scaling. S66 now supplies a directly inspected two-shell wall/internal-generation comparison; S65 remains available for the next comparison.

## 4. Closures and local multidimensional effects

S57 provides a strong reason to treat closures as competing hypotheses. Changing the friction-transition law changes predicted stability for a water loop; first-order numerical diffusion separately changes growth and damping (§§2–3.1,PDF5–17). Neither result supports one universal natural-circulation multiplier. The paper's friction graph uses Fanning factors; S30 uses Darcy factors. Transformation must include the governing pressure-loss convention, not only the factor's name.

S60 demonstrates local high-Pr velocity nonuniformity using planar PIV and CFD (§§3–4). It also shows why a bulk-flow model and a centerline observation can disagree without uniquely identifying the missing mechanism. Its3D helical-flow interpretation is supported by combined evidence rather than measured full-volume velocity; its power/temperature/Pr sweep does not isolate Pr causally. Thus a proposed local-recirculation closure needs a defined descriptor, observable consequences and a qualified reference.

Fully developed Nu4.36 or standard forced-flow correlations require the correct geometry, source/boundary condition, development and regime assumptions. High Pr alone does not prove advection dominance: Pe also depends on Re. Simultaneously developing, mixed-convection and property-varying cases should be compared where our actual envelope requires them. S45 remains a targeted mechanism source; its full extraction is pending.

## 5. Identifiability and observations

Sparse temperatures may support a good predictor without uniquely identifying every physical coefficient. S06 explains calibration/discrepancy confounding; selected S23 setup distinguishes states from observation functions. Full profile-likelihood extraction is still a priority before prescribing a particular procedure.

Our simple energy-scale example illustrates a necessary diagnostic, not a new contribution:

\[
C\dot T=Q-G(T-T_a).
\]

For a passive constant-ambient cooldown, temperature dynamics constrain G/C. Independently known steady net duty at nonzero temperature rise can constrain G; independent inventory capacity is another anchor. A network can remain non-identifiable after that global ambiguity is removed. Inputs, regional losses and observation offsets can introduce further confounding.

Heater-side and cooler-side thermal-balance flow estimates share measurements and loss allocations. Their compatibility does not establish independent flow accuracy. As shown in the prior checkpoint, shifting heat loss between regions can preserve total loss and nearly preserve flow-estimate compatibility. The thesis must distinguish supported parameter combinations, measured thermal predictions and independently supported circulation.

## 6. Uncertainty must be attached to a prediction contract

Maintain separate uncertainty objects for sensors/calibration/covariance, inputs, initial states, thermophysical properties, fitted parameters, structural/reduction discrepancy, numerical solution and any CFD reference. Dependence matters: a shared temperature, property fit or inferred duty cannot be sampled independently each time it appears.

S26's operator/network posterior, S04's Bayesian operator posterior, S30's dynamic fluctuation forcing and S51's parameter/model-choice sampling represent different uncertainties. None is automatically a complete TRIDENT predictive budget. S30 explicitly uses channel DNS for a general fluctuation form, not loop-specific amplitude. S51 already explores heat-transfer model choice and margin failure events, but its sampling/tolerance and failure-count conventions require qualification (S51 dossier,§§4.4–4.6).

Official JCGM measurement guidance should anchor measurement definitions/propagation, while model discrepancy and predictive assessment require additional analysis. Propagating uncertainty is not equivalent to validating it. Assess withheld residuals, bias, dependence and interval coverage where data support that assessment; retain numerical and observational ambiguity in claimed margins. A few illustrative stochastic trajectories do not establish a calibrated small failure probability.

## 7. Stability, transient response and numerical verification

Distinguish steady equilibrium, local linear stability, finite-disturbance behavior, finite-time thermal margin and long-time stochastic escape. S57's discrete amplification matrix and S30's continuous ODE Jacobian are not interchangeable. S57 also contains some RELAP pulses involving voiding; they must not be used as single-phase evidence.

Verification should target the claimed quantity: a converged bulk temperature need not establish converged local extrema, vortex extent, growth rate or reversal time. S60's mesh study and limited velocity comparison cannot substitute for TRIDENT CFD qualification. A reference calculation requires independent boundary/input provenance, property laws, spatial/time refinement and evidence concerning model assumptions.

For the minimum experimental program, preserve Nick's existing covariance/autocorrelation work and model freeze/holdout safeguards. Resolve preparation and sensor-map contradictions before interpreting data. If a dataset is used to select topology or revise a closure, reclassify it as development evidence and obtain a new holdout for the affected claim.

## 8. Experiment design and achievable contribution

Prioritize experiments that distinguish plausible models or reduce uncertainty in a decision-relevant QoI. Repeated passive relaxation may qualify noise/response ratios; independently anchored duty or capacity may address scale; distinct thermal conditions may discriminate loss/transport assumptions. Each proposal must be negotiated through Nick's plan, with actual controls, initial conditions and accepted operating limits.

S07's now-inspected Bayesian design formulation explicitly distinguishes parameter inference, prediction and model-discrimination objectives (§2.1,manuscriptPDF4), while demonstrating parameter-information designs. Information about all parameters is not automatically the most useful objective; prediction or model-discrimination utility may better match the thesis.

The most defensible candidate core is a reproducible, conservation-consistent procedure linking retained physics, identifiable parameter groups, feasible experiments and independently assessed QoIs. Demonstrating this procedure across held-out conditions could advance understanding. Whether it is novel requires the pending comparisons; no theorem, accepted model or final direction is claimed.

## Completion gates

Complete S23/S67 technical extraction and the relevant source/similarity comparisons; verify the actual operating/sensor contract; define comparator performance and permissible calibration; then revise this into a comprehensive implementation-oriented review. S18 and S07 now have scoped dossiers, with version/coverage limitations. No operating-data processing, experiments, automatic control or TRIDENT CFD has been performed.

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

## 14. Design around identifiable predictions and verify the utility computation

S07 chooses expected information gain about parameters, averaging posterior/prior KL divergence over prospective data. This objective requires a specified prior, likelihood, forward observation map and feasible design set. It differs from minimizing error in a future thermal prediction or discriminating model structures, even though all can be expressed within an expected-utility framework.

The distinction is practical. Repeats can qualify drift and repeatability, independent duty anchors can break a scale ambiguity, and an independently varied boundary can discriminate transport from storage. Their value cannot be ranked by sensitivity magnitude alone. Shared calibration/ambient uncertainty must remain in the joint likelihood; conditional independence of repeated data is an assumption to justify.

Joint information is generally nonadditive; selecting a batch by repeating the best single experiment may be suboptimal (S07,§2.2/AppendixA,PDF7/49–50). Conversely, this does not remove the metrological value of repeats. S07 also shows that a surrogate sufficient for ranking designs can distort a posterior used for inference (§6.7,PDF23–24). Verify numerical error for the actual use.

Our proposed minimum is therefore to enumerate a small set of executable Nick-plan alternatives, examine identifiable groups and model/QoI separation, and only then consider expensive Bayesian optimization. A full PC/SPSA pipeline is an option if cost warrants it. It is not a prerequisite to a defensible experiment request.

S67's verified abstract describes thermal RC-network calibration and profile-based parameter-interdependence analysis. Full extraction is needed before we claim a novel combination of thermal networks, uncertainty and identifiability. S23 is also pending full extraction: current access failures do not erase earlier metadata/setup reading, but they prevent an honest complete source dossier.
