# S71 — Goal-oriented Bayesian experimental design

Extraction21October2026. Shijie Zhong,Wanggang Shen,Tommie Catanach,Xun Huan. *Goal-Oriented Bayesian Optimal Experimental Design for Nonlinear Models Using Markov Chain Monte Carlo*. Journal record:SIAM/ASA Journal on Uncertainty Quantification14(1)(2026),19–47,DOI https://doi.org/10.1137/24M1649344 . **Extracted version:**arXiv2403.18072v2,2February2025,https://arxiv.org/abs/2403.18072v2 .28PDF pages=manuscript printed1–28; no journal-page mapping asserted. Full journal/v2 text equivalence not established.

## Identity/completeness and question mapping

Title,four authors,v2/date agree;Sections1–5,Algorithm1,Figures1–19 and terminal references present. All pages readable as text; selected equations/transport pages rendered,PDF5/21 visually checked. No appendix appears; code/supplements not acquired. Main text1–25 read; references25–28 inspected as discovery,not all cited originals read. Scoped readiness: GO-design theory and novelty/budget/applicability appraisal. Not final-version extraction,algorithm reproduction or experimental validation.

## Original contribution and strongest prior work

This paper provides a nonlinear predictive GO-OED computational approach: nested Monte Carlo,posterior MCMC,predictive density KDE and Bayesian optimization. It distinguishes information about θ from information about a downstream z. Bayesian design/EIG,linear goal-oriented criteria,Bernardo’s expected utility and data-consistent prediction design are earlier cited work. Thus “design experiments for the QoI rather than parameters” is established prior art,not a TRIDENT novelty claim.

## Reported formulation,assumptions and units

§2/PDF3–5,Eqs1–14: y=G(θ,d)+ε; posterior p(θ|y,d)∝p(y|θ,d)p(θ),with prior unaffected by choosing d. Separate target z=H(θ,η),independent of acquisition design d given θ; nuisance prediction stochasticity η is incorporated through p(z|θ). U(d)=Ey|d[DKL(p(z|y,d)||p(z))]=I(z;y|d). Target d*=argmax U. The parameter-EIG criterion replaces z by θ. Eq13 states I(z;y|d)≤I(θ;y|d),with equality for a bijection; the inequality is cited to earlier theory. Conditional-independence assumptions matter: a target whose physical definition changes with the acquisition design requires a reformulation.

KL is dimensionless (natural logarithms→nats),with probability density ratios using the same reference measure. θ,y,z retain their physical/model-specific units; a density by itself has inverse-output units. The examples use mathematical/nondimensional variables; their numerical source strengths or transport coefficients are not salt-loop properties. EIG measures expected information under the assumed prior/likelihood/model,not automatically engineering loss,cost-weighted value,coverage or robustness to misspecification.

§3.1/Eq17/PDF6 uses outer prior-predictive observations and inner posterior parameter/QoI samples; prior-predictive entropy term can be reused or omitted when only ranking designs with unchanged target prior. §3.2/PDF7–8: emcee stretch move; oracle generating θ initializes simulated design-sampling chains,but actual experimental inference has no oracle. Unidentifiable/multimodal cases still require suitable samplers and convergence diagnostics. Gaussian isotropic KDE bandwidth selected on early outer samples via5-fold CV,then held for the design. Small/large bandwidth shifts utility; empirical tuning does not remove bias.

§3.3/PDF8–10: Matérn-GP surrogate of the **design utility**,UCB acquisition κ2.56,multistart L-BFGS-B; these GP confidence bands are optimizer uncertainty,not physical predictive intervals. Default1000outer×1000inner samples entails substantial model/inference cost; cost increases with both dimensionality and sample budgets (§4.3/PDF17–19). This is an algorithmic alternative,not a requirement to buy sensors or execute CFD.

## Evidence and validation independence

§4.1/PDF10–15 tests bijective/nonbijective targets and compares against fine-grid numerical reference for the special tractable benchmark. Bias/variance from KDE/MCMC remain; different target information can rank designs differently. Synthetic truth and data use the assumed observation family. These are numerical demonstrations,not independent physical calibration/validation or assurance under omitted physics.

§4.2/PDF14–17 extends toy dimension/design;§4.3 explores cost;§4.4/PDF19–24 uses a2D prescribed-velocity convection–diffusion source-inversion example. Eq37: ∂tc=∇²c−u(t)·∇c+S;u=(50t,50t),square[−1,2]²,uniform source-location prior[0,1]²,Gaussian source strength2,width.05,initial c=0,homogeneous-Neumann boundaries. Source location unknown; transport velocity/diffusivity prescribed. This is **not buoyancy-coupled natural circulation**,conjugate heat transfer or an MSR surrogate.

Finite-volume Δx=.01,Δt5e−4;AB2 convection/CN diffusion and QUICK. DNNs predict concentration at t1=.05,t2=.2;2000source samples,~2×10⁷space/parameter points per time,random pointwise80/20split. Reported test MSE~1e−6/1e−7 and~1e5speedup (§4.4/PDF20) are source-reported numerical metrics. Pointwise splitting does not establish held-out source-parameter independence because points from the same simulated field can appear in both partitions. No mesh/time/surrogate-error propagation into design ranking or physical-loop validation is supplied here.

Design selects one to three sensor positions in[0,1]²;data noise standard deviation.05;targets future concentrations and a flux functional. Results show target-dependent sensor patterns,not simply nearest-to-target placement. Eq42/PDF21 defines **diffusive** flux−∂c/∂x1 at x1=1 integrated x2 from−1to1. The prose describes the region-of-interest right boundary,though ROI earlier[0,1]²;also advective contribution u1c is absent. Do not implement this as total contaminant/thermal transport or silently change its integration limits. At the outer domain,homogeneous derivative Neumann is not automatically zero total flux when advection is nonzero.

**Our measure check:** T2 Eq29/PDF12 has constant z=5 over a positive-measure θ interval,hence an atom in predictive probability,whereas a continuous KDE smooths that mass. This does not invalidate mutual information,but cautions against reading a smoothed density integral as an exact mixed/discrete-target estimator. Event probabilities or maxima similarly require support/measure care. No numerical reanalysis performed.

## TRIDENT transfer and skeptical novelty appraisal

Direct methodological transfer is the separate observation/target contract and comparison of parameter-EIG,QoI-EIG and simple feasible designs. Conditional application can rank existing heater/input histories,observation times or repeated runs if experimentally allowed; the article’s sensor-placement examples do not authorize new instruments. Include nuisance boundary/sensor/model uncertainty and common budgets. A design that maximizes information under an incorrect closure can be confidently misleading. A proposed contribution needs demonstrable robust design/adequacy/identifiability behavior for the available loop evidence,not just a GO-OED implementation.

Numerical ranking uncertainty must be below meaningful design separation; independent held-out predictive assessment is still needed. A manageable baseline may use finite feasible experiment choices and low-dimensional conservative models,not the complete nested sampler immediately. No final method selected.

Next originals: existing S07 and registered goal-oriented validation/design work should be cross-compared before new IDs. Bernardo1979 and linear GO-design cited here are foundational discovery leads,not read originals. Journal S71 is an optional exact-version acquisition; v2 suffices for this explicitly scoped analysis.

| Coverage | PDF | Status/reason |
|---|---|---|
| Intro/formulation | 1–5 | Read/extracted;novelty lineage distinguished |
| Numerical algorithm | 5–10 | Read/extracted;not code-reproduced |
| Toy benchmarks/cost | 10–19 | Read/mapped;no plot digitization or reruns |
| Transport example | 19–24 | Read/extracted;conditional transfer and split/flux flags |
| Conclusion/references | 24–28 | Main conclusions read;references discovery-inspected |
| Journal differences/code/supplement | External | Unavailable/not compared;not claimed equivalent |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S71-C01 | Nonlinear target-information experimental design is established prior art | §2/Eq10–14,PDF5 | Extracted arXivv2,not journal-equivalence claim |
| S71-C02 | Parameter and target EIG can rank designs differently | §4.1/Fig4–6,PDF12–15 | Synthetic numerical demonstrations |
| S71-C03 | Separate observation and target maps underpin the design utility | Eq1–5,PDF3–4 | Conditional independence and design-invariant target |
| S71-C04 | MCMC/KDE bias,bandwidth and cost affect design estimation | §3.2/PDF7–8;§5/PDF24–25 | EIG optimum not automatically robust |
| S71-C05 | Transport illustration uses prescribed convection and synthetic fields | Eq37–39,PDF19–20 | No buoyancy/conjugate loop validation |
| S71-C06 | DNN test split shuffles individual field points | §4.4,PDF20 | Does not establish held-out source-parameter independence |
| S71-C07 | Reported flux functional is diffusive with explicit−1to1integration | Eq42/PDF21 | Not total advective–diffusive flux;ROI wording differs |
| S71-C08 | Oracle chain initialization applies to simulated design utility samples | §3.2.1/PDF7 | Not an oracle for real experimental inference |
| S71-C09 | The flat target branch creates an atom smoothed by continuous KDE | Eq29/PDF12 | Our measure appraisal,not a reproduced bias estimate |
