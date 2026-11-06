# S07 — Huan and Marzouk: Bayesian experimental design

## Identity, version and inspection

Xun Huan and Youssef M. Marzouk, “Simulation-based optimal Bayesian experimental design for nonlinear systems,” *Journal of Computational Physics*232(1)(2013),288–317, DOI:https://doi.org/10.1016/j.jcp.2012.08.013. Extracted version: https://arxiv.org/pdf/1108.4146v3,53PDF pages. ArXiv margin states v3,30Nov2012; first-page compilation footer says27Nov2024. Record both; the footer is not a new publication date. **No complete journal/manuscript comparison is claimed.** Printed=PDF page in this manuscript.

Sections1–7 and AppendicesA/B inspected as extracted text; selected key equations and version header rendered/visually checked onPDF1,6,8,9,50. Figure/table block PDF32–48 mapped and selected-read, not exhaustively digitized. AppendixC combustion equations were mapped, not fully extracted because this pass concerns design methodology rather than chemical kinetics. Main article is complete; no separate supplement identified.

Ready for scoped design/utility/computational-cost synthesis. Not a reproduction or universal prescription. Original questions H1–H6,F identification,G uncertainty,D5/D6,K1/K2.

## Problem and actual contribution

The study constructs an expected-utility design framework for nonlinear simulation models, estimates expected parameter-information gain with nested Monte Carlo, accelerates repeated model evaluations with polynomial chaos, and compares stochastic optimizers. Algebraic and combustion examples illustrate parameter inference, sensor/observable selection and joint design of experiments.

Section2.1 explicitly distinguishes inference of parameters, prediction of model outputs and discrimination among model structures. **The implemented demonstrations target parameter learning**, not every alternative utility. Using this reference does not by itself supply a TRIDENT model-discrimination or thermal-margin design algorithm.

## Mathematical objects and assumptions

θ denotes uncertain parameters, d experimental choices, y prospective data and G(θ,d) the forward observation model. A prior p(θ), likelihood p(y|θ,d), feasible design domain and target must be specified. Prior independence from design is assumed in the simplified formulation. Measurement/discrepancy noise enters through \(y=G(\theta,d)+\epsilon\), Eq14,PDF10; the generic formulation allows more than constant iid noise.

Reported expected information gain, Eq6,PDF6, visually checked:
\[
U(d)=E_{y|d}\left[D_{\rm KL}\{p(\theta|y,d)\Vert p(\theta)\}\right].
\]
It averages over prospective data and equals parameter–data mutual information under the stated model. It is measured in nats with natural logarithms; it is not temperature variance, calibration accuracy or a frequentist coverage guarantee.

The equivalent likelihood/evidence form is Eq8,PDF7:
\[
U(d)=E_{\theta,y|d}[\log p(y|\theta,d)-\log p(y|d)].
\]
Inner integration over the prior estimates evidence and an outer Monte Carlo average estimates U (Eqs9–10,PDF8). Finite inner sampling produces bias; increasing only outer sample count does not remove it. Their sample-reuse strategy reduces distinct forward evaluations but introduces a further bias contribution, empirically assessed in AppendixB.

For several experiments the paper assumes conditional independence given θ/design in its joint-likelihood argument (§2.2,PDF7;AppendixA,PDF49–50). This differs from marginal independence: shared uncertain parameters make experiments informative about the same unknowns. Shared calibration drift/ambient forcing in TRIDENT requires an expanded joint model, not automatic multiplication of independent likelihoods.

AppendixA establishes nonadditivity of information from conditionally independent experiments. The best batch need not repeat the single best condition. It does not imply that repetition has no value; repeated runs can establish noise, drift and repeatability outside a pure parameter-information objective.

## Surrogate, optimization and validation procedure

The PC surrogate approximates the forward map over **both parameter support and design domain**, not only a calibrated point or one trajectory (§3). It approximates outputs versus inputs rather than reducing deterministic internal state dimension. Basis/truncation, dimension-adaptive sparse quadrature, common random numbers and stochastic optimization address computational burden.

Section2.4 compares SPSA and a noisy Nelder–Mead variant. Constraint projection and objective noise can affect convergence; no universal global-optimum guarantee for TRIDENT follows from the examples.

An algebraic example shows distinct optimal conditions for different prior supports, and mixed-condition batches for a broad prior (§5,PDF15–17). In combustion, the selected unknowns are two kinetic parameters and the design variables initial temperature/equivalence ratio. The study uses **simulated noisy data** for inference comparisons, not new shock-tube measurements validating the whole design framework (§6,PDF17–23).

Selection of observables changes design optima (§6.5,PDF20–21). The paper uses peak/time summaries partly because raw fixed-time trajectories depend sharply on ignition time. For TRIDENT, any response/settling summaries similarly need a reproducible definition and uncertainty model; compression can discard information.

The low-order surrogate can identify good designs while giving visibly distorted parameter posteriors (§6.7,PDF23–24). Hence numerical accuracy needed for design ranking can differ from accuracy needed for inference. Claimed speedups include offline surrogate construction assumptions; they are not forecasts of our cost.

## Critical appraisal and equation checks

The mathematical design criterion is conditional on its forward model, prior, likelihood and feasible controls. The conclusion explicitly leaves structural model inadequacy, imprecisely imposed designs and rigorous sequential design as further work (PDF24–25). “Optimal” therefore cannot mean best real-world TRIDENT experiment under unspecified discrepancy.

Two printed implementation conventions need reconciliation if coding SPSA: Eq11 subtracts the Eq12 difference estimate although the stated target is maximization; the text calls perturbations symmetric with finite inverse moments but writes Bernoulli(.5), whose conventional0/1 encoding would violate that requirement (PDF9,visually checked). Resolve objective sign and ±1 coding from the algorithm definition before implementation. These observations do not establish errors in unaudited executed code.

Similarly, the footnote's linear-Gaussian D-optimal description names prior covariance where a consistent information-matrix derivation uses prior precision. Do not use that sentence as a dimensionally unchecked formula. Our recommended implementation starts from the prior/likelihood, not the footnote.

Monte Carlo bias estimates in AppendixB are a specific numerical study, not a universal small-bias certificate; ranking close designs requires design-dependent error checks. Priors can also regularize an unidentified physical model without making parameters data-identified.

## Claim-to-evidence ledger

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S07-C01 | Parameter, prediction and discrimination goals require distinct utility choices. | §2.1,PDF4 | Demonstrations target parameter information. |
| S07-C02 | Expected parameter-information gain averages posterior/prior KL over prospective data. | Eqs4–8,PDF6–7 | Conditional on prior/model/likelihood. |
| S07-C03 | Joint experiment information is generally nonadditive. | §2.2,PDF7;AppendixA,PDF49–50 | Assumed conditional independence; repetition can serve other goals. |
| S07-C04 | Finite inner sampling and sample reuse contribute estimator bias. | §2.3,PDF8;AppendixB,PDF50–51 | More outer samples alone do not remove bias. |
| S07-C05 | The surrogate spans parameter and design variables and approximates outputs, not internal state reduction. | §3,PDF10–14 | Not interchangeable with a physical loop ROM. |
| S07-C06 | Observable selection and prior support can change the preferred experiment. | §§5/6.5,PDF16–17/20–21 | Example-specific; define TRIDENT observations first. |
| S07-C07 | A surrogate adequate for design can be inaccurate for posterior inference. | §6.7,PDF23–24 | Need target-specific surrogate verification. |
| S07-C08 | Demonstrations infer from simulated data; structural inadequacy remains an explicit limitation. | §6.5,PDF20;§7,PDF24–25 | No new loop/combustion experiment validation. |
| S07-C09 | Printed SPSA sign and perturbation conventions require checking before implementation. | Eqs11–13,PDF9 | Analyst audit, not code verdict. |

## TRIDENT implications and coverage

Begin with a finite set of feasible Nick-plan choices and explicit models/observations. For small cheap models, enumeration and synthetic distinguishability can be a useful baseline before building a PC/SPSA workflow. This is our proposed staged implementation choice, not the paper's proven recommendation.

| Asset | Coverage | Remaining limit |
|---|---|---|
| §§1–2 PDF1–10 | Inspected/extracted;key equations visual | No optimizer reproduction |
| §3 PDF10–14 | Inspected/extracted | Quadrature/PC implementation not rebuilt |
| §4 PDF14–15 | Inspected;role extracted | No MCMC convergence study repeated |
| §5 PDF15–17 | Inspected/extracted | No objective surface recalculation |
| §6 PDF17–24 | Inspected/extracted | Combustion-specific constants/plots not exhaustively transcribed |
| §7 PDF24–25 | Inspected/extracted | Future-work distinctions preserved |
| References PDF25–31 | Selected discovery only | Cited originals not all read |
| Figures/tables PDF32–48 | Mapped/selected-read | Not exhaustively extracted or digitized |
| AppendixA/B PDF49–51 | Inspected/extracted;PDF50 visual | No independent estimator benchmark |
| AppendixC PDF51–53 | Mapped; detailed extraction skipped | Chemical mechanism outside current loop-method decision |

No upload required for this scoped dossier. Journal/manuscript version comparison remains unfinished.
