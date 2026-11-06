# S72 — Goal-oriented calibration of a model and its modeling errors

Extraction21October2026. Antonin Paquette-Rufiange, Marc Laforest and Serge Prudhomme, *Computer Methods in Applied Mechanics and Engineering*448(2026),118486. DOI: https://doi.org/10.1016/j.cma.2025.118486 . Uploaded final typeset article;26PDF pages=printed1–26. Earlier S72:THESIS1 Chapter4 remains a related earlier asset, not the document extracted here; no complete thesis/article difference audit claimed.

## Identity, integrity and readiness

Title/authors/DOI, journal header and terminal references agree. All26pages yield text, complete Sections1–6,Tables1–8,Figures1–12 and references through[34]. No separate appendix appears. PyMuPDF reported an xref reconstruction warning for object692 on initial opening; this did not prevent text extraction or selected rendering. Original bytes unchanged. Pages11–12,21–22,24 rendered; page11 and22 visually inspected for consequential equation defects. No external code, source thermal-challenge data or supplements were acquired. Ready for scoped calibration/discrepancy/novelty synthesis; not a reproduced algorithm or validated loop model.

## Problem and original contribution

The authors distinguish a physical model, its observables, empirical discrepancy, observation error and predictive purpose. Their contribution is a nested calibration: fit a discrepancy representation for each fixed physical-parameter vector, then choose that vector to minimize a goal-weighted functional of the discrepancy. KOH discrepancy, MLE/MAP, confounding and intrusive equation corrections are cited prior approaches, not inventions of this paper. Brynjarsdóttir–O’Hagan is the cited synthetic example lineage. This final article is strong prior art against claiming novelty for prediction-oriented calibration or separating physical and discrepancy fits alone.

A central explicit restriction is that their observation-level KOH correction does **not** directly propagate modeling error to a distinct, unobserved QoI (§1/PDF3;§2.5/PDF7;§6/PDF24–25). Choosing an objective does not create information about an unobserved peak, local velocity or salt field.

## Model, observations, assumptions and units

§2.1–2.3/PDF3–5 introduces a constant-property,1D transient slab-conduction model with initial uniform temperature and imposed heat flux. Control p=(q,L,u0), material/model θ=(k,ρcp), sensor z=(x,t), combined χ=(p,z), observation h(χ,θ). Units for implementation: q W/m²,L/x m,t s,k W/(m K),ρcp J/(m³K),temperature degrees as specified by the thermal data (u0=25). Temperature differences in K or°C coincide; absolute-temperature conversions matter for other physics. The model is not a circulating fluid, wall/fluid conjugate loop or reactor.

Reported Eqs5–8/PDF4–6: y=h+E+Φ; E and Φ are independent Gaussian processes. Φ normally represents observation error, but incorrectly specified noise or hidden inputs can migrate into E. Thermal example assumes a small white noise standard deviation.01 (variance.01²) even though the originating challenge data were described as noise-free; this is a modeling choice, not sensor metrology. Four replicates at each of four calibration scenarios are treated as independent experiments, with within-run temporal correlation. Inter-run shared systematic error is not established absent.

Eqs13–27/PDF8–10 formulate MLE/MAP and KOH likelihoods; the Gaussian covariance adds discrepancy and observation covariances. Apparent physical parameters depend on the imperfect model, discrepancy family, sampled scenarios and calibration objective. A good corrected observation fit does not identify individual physical mechanisms.

## Consequential algorithm and checks

§4.1/PDF11–12: at fixed θ, either fit discrepancy mean/covariance simultaneously or sequentially (mean first, then covariance). Inner fits use multi-start Knitro; outer physical calibration uses NOMAD (§4.2–4.3/PDF12–13,Algorithm1). Multiple local optima and expensive nested fitting constrain application to relatively few physical parameters. The authors prefer sequential fitting after the illustrative simultaneous fit produces broad/biased discrepancy bands; this is an example-dependent comparison, not a general superiority theorem.

**Printed-mathematics flag:** Eq28/PDF11 writes argmin of the likelihood L, whereas the prose says maximize likelihood and Eqs30/32 use argmax. L was defined as positive likelihood, not negative log-likelihood. Do not transcribe Eq28 literally without clarification. We do not infer their optimizer minimized the likelihood.

Eqs35–37/PDF12 define the α central quantiles of E and εE(χ,α)=max(|Q((1−α)/2)|,|Q((1+α)/2)|), then minimize a chosen norm of ε. **Our algebra:** for a scalar normal E with mean m and standard deviation s, ε=|m|+z((1+α)/2)s; units are those of the observation. This is a pointwise, fitted-GP conditional quantity, not a simultaneous-domain error bound, posterior uncertainty in all hyperparameters, or empirically established coverage. The weighted integrals printed as a “norm” in Eqs44/47 omit the square root; minimizing a nonnegative integral versus its square root has the same minimizers, but values and dimensions differ. Keep that distinction in code and review.

The nonstationary covariance printed on PDF21 repeats χ′ in both prefactor factors; its symmetry/normalization should be checked against cited original covariance constructions before implementation. Exponent arguments and softplus input must be nondimensionalized if assigning physical units to coefficients. No silent repair supplied.

## Results, independent assessment and failures

§5.1/PDF14–18 demonstrates goal-dependent slopes, dependence on discrepancy family and explicit θ/discrepancy-slope confounding. A stationary constant-mean/variance discrepancy collapses the tested goal distinctions; the broader claim that all stationary GPs fail is not established. §5.2/PDF19–20 manufactured perfect-model test recovers parameters with small errors, as do MLE and KOH baselines. It verifies a favorable synthetic case, not general existence/uniqueness/consistency.

§5.3/Table6/PDF20 separates16calibration runs,11times each (176values), from2validation runs at q=3000,L=.019,threepositions and21times (126values). Prediction target q=3500 extends beyond calibration q=1000/2000. These are **synthetic thermal-challenge data**, treated as experimental observations; no new physical experiment. The authors explicitly state validation data do not determine the calibrated parameters (PDF22). No held-out TRIDENT comparison exists.

Table8/PDF24 reports validation “RMSE”17.4(MLE),40.1(KOH),22.9(goal1),20.1(goal2), temperature units. Goal2 improves on goal1/KOH but **does not beat ordinary MLE** on this criterion. These are errors of h alone in Eq46, not necessarily error scores of h+E. **Normalization flag verified on PDF22:** Eq46 sums2×63terms but divides by1134, not126. Hence the reported absolute RMSE normalization cannot be certified without source code/raw residuals. A common denominator change preserves ordering and would change values by a factor3 if used literally; do not silently rescale the table. The method’s observed interval plots do not constitute a replicated coverage study.

§6/PDF24–25 explicitly leaves goal weighting, discrepancy-family robustness, existence/uniqueness/stability and transfer from observable discrepancy to distinct QoI error as future work. Thus goal orientation neither solves structural identification nor guarantees better predictions.

## TRIDENT consequences and next originals

Direct methodological relevance: separate observation and target maps, specify objective and weights in advance, compare ordinary covariance-aware MLE and discrepancy alternatives under the same held-out runs, and test sensitivity to discrepancy family. Conditional transfer: thermal/slab example motivates, but does not supply a loop closure or identify wall/storage/flow parameters. Unobserved extrema/local recirculation require a separate trustworthy map and independent support. Stochastic parameter uncertainty, GP discrepancy variability and metrology uncertainty are distinct.

Cited originals to check if those questions stay central: Oliver et al.(2015),DOI10.1016/j.cma.2014.08.023,for unobserved-QoI embedded corrections; Paquette-Rufiange et al.(2023),DOI10.1016/j.cma.2023.116182,for prediction-oriented validation design; Dowding et al.(2008),DOI10.1016/j.cma.2007.09.029,for challenge data definitions. Match to existing registry IDs before creating any new ID; these cited originals were not read by reading S72.

| Coverage | PDF | Status/reason |
|---|---|---|
| Identity/introduction/model | 1–7 | Read; predictive restriction and observation assumptions extracted |
| Standard calibration | 8–10 | Read; cited asymptotic theorems not independently proved/audited |
| Proposed algorithm | 11–13 | Read/extracted; selected math visually checked |
| Synthetic examples | 14–20 | Read/mapped; not numerically reproduced |
| Thermal challenge | 20–24 | Read/extracted; split/metric/math limitations checked |
| Conclusions/references | 24–26 | Read/discovery; original references not thereby read |
| Supplement/code/source data | External | Unavailable/unread; no completeness claim for external assets |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S72-C01 | Goal-oriented physical calibration with nested discrepancy fitting is existing prior art | §4,PDF11–13,Algorithm1 | Not new merely to apply this structure |
| S72-C02 | Observation-level discrepancy does not directly propagate to unobserved QoIs | §2.5/PDF7;§6/PDF24–25 | Needs additional model/evidence |
| S72-C03 | Calibrated parameters depend on predictive objective and discrepancy family | §5.1/PDF15–18 | Demonstrations,not material-property identification |
| S72-C04 | Synthetic thermal challenge separates calibration and validation runs | Table6/PDF20;§5.3.2/PDF22 |126validation values; no physical loop experiment |
| S72-C05 | Ordinary MLE has lower reported validation metric than both goal-oriented fits | Table8/PDF24 | Metric of h alone; normalization flag applies |
| S72-C06 | Printed Eq28 minimizes likelihood contrary to prose and surrounding MLE definitions | Eq28/PDF11 | Not evidence of actual solver behavior |
| S72-C07 | Printed Eq46 denominator1134 conflicts with2×63summed validation residuals | Eq46/PDF22;Table6/PDF20 | Our arithmetic; do not silently rescale reported results |
| S72-C08 | Quantile discrepancy objective is a fitted pointwise-Gaussian error quantity | Eq35–37/PDF12 | Not simultaneous/full-predictive empirical coverage |
| S72-C09 | Existence,uniqueness,stability and robust QoI weights remain unresolved by the article | §6/PDF24–25 | Author limitations,not automatically a feasible TRIDENT gap |
| S72-C10 | Small-dimensional nested optimization and discrepancy choice impose practical constraints | §4.3/PDF13 | No proven scalable loop implementation |
