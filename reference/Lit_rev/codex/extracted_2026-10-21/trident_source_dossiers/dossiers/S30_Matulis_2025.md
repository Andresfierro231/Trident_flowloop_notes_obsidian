# S30 — Matulis, Singh and Bindra (2025): Fourier dynamics and stochastic closure

Extraction 2026-10-20. John Matulis, Suneet Singh, Hitesh Bindra. *Stochastic perturbation and stability analysis of a reduced order model of natural circulation loops*. International Journal of Heat and Mass Transfer247,127052. https://doi.org/10.1016/j.ijheatmasstransfer.2025.127052.

## Identity and scope

Publisher article,13 consecutive PDF pages, printed numbering equals PDF numbering. Available online17April2025; issue1September2025. Title/authors/DOI match primary metadata. All main sections and references inspected in text; pp.4,5,7,13 visually checked. Equations/figures readable on those pages. No code/data acquired. §2.2 says “See Appendix” for the zero-mode derivation, but no appendix occurs in the supplied13-page article: derivation material remains missing. Data availability says available on request; no author contacted.

Relevant to original brief: physical model alternatives; conserved mean energy; model-reduction limits; closure/noise meanings; stability and transition QoIs; observation and validation dependence; novelty challenge.

## Actual contribution and model contract

A one-dimensional rectangular horizontal-heater/horizontal-cooler water-loop model is Fourier truncated through mode3, yielding eight real ODE states: uniform circulation v, mean temperature phi0, three real and three imaginary thermal modes. Heater flux fixed; cooler **wall temperature prescribed31.65°C**, with cooler removal responding to mean cooler-fluid temperature and a heat-transfer correlation (§§2.1–2.2, PDF3–5). Heater/cooler duties need not balance instantaneously, allowing mean temperature to evolve.

This is already close prior art for interpretable low-dimensional circulation/temperature dynamics, transient margins, nonlinear stability and stochastic closure. It is not a new salt experiment, a full CFD projection of TRIDENT or a model with separate wall/insulation/tank storage.

Water properties at101.3kPa are updated with mean loop temperature; cooler properties use mean cooler temperature. Effective axial diffusivity alpha=.001m²/s is selected to reproduce experimental stability (§2.1, PDF3). It includes eddy/molecular effects; **it is not water molecular diffusivity**. An independent holdout for this selection is not documented.

## Governing equations, definitions and coding hazards

§2.2/Eqs2.1–2.26 (PDF4–5): incompressible spatially uniform v, Boussinesq loop momentum; energy
\[
\partial_tT+v\partial_sT=H(s,t)+\alpha\partial_{ss}T.
\]
Here H has K/s units, alpha m²/s, s in m. For a round pipe, \(H=2q''/(\rho c_pr)\). Fourier basis uses loop length \(L=2(L_r+L_h)\), complex coefficients with real-field conjugacy, then real/imaginary states. The real reconstruction Eq2.26 includes factor2 for positive modes and a **minus** imaginary-sine contribution. Retain the origin in Fig1 and source/gravity Fourier conventions; changing coordinates requires changing coefficients.

The mean mode Eq2.21 permits net heating; an independently derived control-volume check is
\[
\rho c_p A L\,\dot{\bar T}=Q_h-Q_c
\]
for fixed properties and no other losses/storage. This is our limiting consistency test, not an extra equation claimed by the authors. With varying properties, define compatible energy rather than silently applying a fixed-property identity.

Eq2.20 friction is printed proportional to **v²**, although reversing solutions are later studied. Eq2.29 uses positive-Re pipe correlations, but Re is defined with v rather than |v|. A signed implementation needs opposing drag \(v|v|\), |Re|, and the finite low-flow viscous limit. The actual code is unavailable: do not assert it executed the printed form incorrectly.

Eq2.11's complex buoyancy sum must be reconciled with Fourier conjugacy and the real Eq2.20 before copying. Odd-mode equations2.22–2.23 use an unsubscripted Gamma whereas2.17 distinguishes Gamma0 and Gamma1; their intended forcing must be reconstructed from the integral rather than silently guessed.

Friction (§2.3): Darcy f=max(Colebrook,64/Re), nearly smooth pipe; assumed four elbows K=.75 each and three tees K=.40 each. Correlation switches can affect derivatives and inferred stability. Actual minor losses of validation experiments are incompletely known.

Cooler (§2.5, PDF6): Hausen laminar/Graetz expression and Gnielinski turbulent expression; take maximum. The resulting stability boundary partly coincides with switching correlations (§3.2). Check developing flow, mixed convection, wall-temperature condition, validity ranges and differentiability; “maximum of correlations” is a modelling choice, not universal transition physics.

## Stochastic closure: what uncertainty it represents

§2.4/Eqs2.30–2.34, PDF5–6: expand local minor-loss \(\kappa(\bar v+v')^2\), neglect \(v'^2\), and replace kappa with \(\kappa(1+2\delta)\), delta=v'/mean v. Kramers–Moyal drift/diffusion are learned from JHTDB **channel-flow** DNS, with linear drift and quadratic diffusion functions. Time series use training-data step.043s and are generated independently of loop time integration.

The authors explicitly say this training captures a general form rather than loop-specific fluctuation magnitude, because geometry/Re differ. This is a model for dynamic fluctuation forcing; it is not a calibrated posterior for measurement bias, properties, model truncation, initial conditions or all predictive uncertainty.

Implementation concerns requiring evidence:

- Near mean-flow stagnation/reversal, delta=v'/mean v and dropping \(v'^2\) need a validity treatment. If delta<−.5, the multiplier is negative; support/clipping/passivity conventions are not supplied.
- Eq2.33 defines Dn as moment/dt without factorial, while Eq2.32 uses sqrt(2D2). Under the standard Itô moment convention D2=M2/(2dt), those printed definitions differ by a factor2. Clarify the convention and actual fitted functions before implementation.
- Gaussian eta is described as a zero-mean/unit-standard-deviation sample; continuous white noise versus a discrete increment is not fully specified. A Wiener-driven numerical scheme requires the appropriate sqrt(dt) increment, not an unqualified per-step Gaussian force.
- Fitted drift/diffusion coefficients, state bins, Markov-lag validation, numerical convergence, seeds and a predictive validation split are not supplied in a reproducible package.

These are reproducibility questions, not proof of flawed executed code or a new thesis gap.

## Results and validation strength

§3.1/Fig3 (PDF6–7): comparison to aggregated prior steady-flow data/correlations, with and without minor losses. Not new experiments. Missing experiment details constrain the inference that minor losses explain mismatch.

§3.2/Fig4 (PDF7): geometry r=.0116m, Lr=2.1m, Lh=1.14m, power100–5000W; cooler effectiveness varied. Text specifies14 cases (6unstable/8stable), correctly classifies3unstable+7stable, then says “10 out of16.” Preserve the inconsistency: arithmetic from stated counts is10/14, not10/16; original dataset must resolve the true denominator. Alpha was selected against stability evidence, so independent predictive accuracy is not established by this comparison alone.

§4/Figs5–8 (PDF7–10): numerical supercritical/subcritical Hopf behavior and coexisting attraction/chaos. Illustrations: Lr=1m,Lh=3m,r=.01m near105W; Lr=2m,Lh=1m,r=.015m near773W. These are source-specific model examples, not proposed TRIDENT operating regimes. Largest-real-eigenvalue<0 gives local asymptotic stability; zero real part requires separate analysis, and local stability does not guarantee a global basin or finite-time safety.

§5/Figs9–12 (PDF10–12): stochastic forcing can trigger escape from a metastable region and alter transition durations while leaving some limiting distributions similar. Illustrative escape times are not an ensemble-calibrated probability or universal acceleration factor. PDF/ACF comparison after transients shows response-time dependence. No complete sample-count/seed/confidence/convergence study establishing reliability is reported.

## Stable claim ledger

| ID | Claim | Locator | Appraisal |
|---|---|---|---|
| S30-C01 | Eight-state Fourier circulation/thermal model with unequal instantaneous duties is established prior work | §§2.1–2.2/Eqs2.20–2.26, PDF3–5 | Water HHHC, prescribed cooler wall |
| S30-C02 | Effective axial diffusivity is selected using stability data | §2.1, PDF3 | Effective closure, not material property; independence limited |
| S30-C03 | Stochastic minor-loss forcing uses channel DNS and is not loop-specific uncertainty calibration | §2.4, PDF5–6; conclusion12 | Authors explicitly qualify magnitude transfer |
| S30-C04 | Friction, forcing and SDE conventions need audit before coding | Eqs2.20–2.34, PDF5–6 | Our mathematical appraisal; actual code unread |
| S30-C05 | Stability validation case counts are internally inconsistent | §3.2/Fig4, PDF7 | Reported14 and16;10 correct from stated classifications |
| S30-C06 | Correlation switching affects part of the stability map | §§2.5/3.2, PDF6–7 | Model-choice sensitivity, not universal boundary |
| S30-C07 | Local stability and finite perturbation behavior differ | §4/Figs5–7, PDF7–9 | Numerical model evidence, not TRIDENT regime proof |
| S30-C08 | Dynamic noise can change escape behavior without large limiting-PDF change | §5/Figs9–12, PDF10–12 | Illustrative cases; no complete reliability estimate |
| S30-C09 | Supplied article references a missing appendix derivation | §2.2, PDF5; ending13 | Missing material recorded, not invented |

## TRIDENT application and feasible questions

Useful alternative to spatial finite-volume models and effective regional RC networks. Make a deterministic conservative baseline first, include a sensor observation map, and test whether three modes resolve the declared QoI. Bulk averages may converge while extrema or switching-sensitive stability do not. Separate effective axial mixing from unresolved solid storage to prevent one fitted coefficient compensating for another mechanism.

Potential contribution **hypothesis**: infer observable, physically admissible closure/retained-state combinations and assess held-out thermal responses/margins under realistic input and sensor uncertainty. It must beat established deterministic alternatives and distinguish dynamic fluctuation noise from epistemic uncertainty. With only sparse temperatures, loop-specific stochastic friction identification may be unsupported. No new local-flow measurement or CFD is assumed.

Next sources: S57 friction/transition sensitivity, S58 earlier Fourier modelling/control, S59 diffusion/attractor theory, S62 later stochastic-transient study, S63 earlier nonlinear loop dynamics; S18 conjugate Fourier reduction and S23 identifiability are already in the registry.

## Coverage checklist / readiness

| Portion | Status | Limits |
|---|---|---|
| §1/nomenclature/§2.1 | Text inspected/extracted | Earlier history citations remain separate |
| §2.2/Eqs2.1–2.26 | Inspected/extracted; PDF4–5 visual audit | Missing appendix, no code replication |
| §§2.3–2.6/closures/SDE | Inspected/extracted; PDF5 visual audit | Drift/diffusion coefficients and numerical conventions unresolved |
| §3/Figs3–4 | Inspected/extracted; PDF7 visual audit | Dataset-count discrepancy; independent split unclear |
| §§4–5/Figs5–12 | Text/results/captions inspected/extracted | Not every plot digitized/visually enlarged; no ensemble replication |
| §6/data availability/references | Inspected/selectively extracted | Cited works not thereby read |
| Appendix/code/data | Not supplied | Cannot certify missing content |

Ready for qualified prior-art, alternative-model and uncertainty-meaning synthesis. Not ready for literal stochastic implementation, calibrated uncertainty, reactor margin certification or full reproduction.
