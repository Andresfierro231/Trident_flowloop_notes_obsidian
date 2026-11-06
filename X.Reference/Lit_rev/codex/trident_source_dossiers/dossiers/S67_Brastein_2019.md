# S67 — Brastein et al.(2019): thermal-network likelihood and profiles

## Identity, completeness and scope

O.M. Brastein,B. Lie,R. Sharma,N.-O. Skeie, “Parameter estimation for externally simulated thermal network models,” *Energy and Buildings*191,200–210. DOI:https://doi.org/10.1016/j.enbuild.2019.03.018. Supplied publisher article11 consecutive pages; PDF n=printed n+199. All main text and references inspected. Key likelihood, profile, state equations and tables visually checked onPDF3,5,6,7,9. No separate appendix/supplement identified; code/data not acquired or run.

Ready for scoped inference/model-comparison synthesis, not a verbatim implementation or independent validation of the reported confidence regions. Original questions C1/C5/C6,F1–F5,G1/G5/G7,D6,H1/K1.

## Problem and strongest prior work

The paper adapts stochastic grey-box calibration to thermal RC networks represented by an external component-list simulator. UKF/EnKF produce innovation residuals and covariance for a likelihood; an explicit linear model/standard Kalman filter supplies a baseline. One- and two-dimensional profiles reveal parameter dependence and sensitivity to bounds.

The underlying likelihood framework comes from earlier CTSM/Kristensen–Madsen work; profile methods include Raue and Deconinck–Roels. The new contribution is the external-simulator/filter comparison and associated profile application, not the invention of likelihood calibration or RC networks.

## Thermal model and experimental evidence

R3C2 has room/interior temperature Tb and envelope/wall temperature Tw, with measured heater power and outdoor temperature as inputs (Fig1,§3.1,PDF6/205). Rb links interior to wall,Rw links wall to outside,Rg links interior directly to outside. Cb,Cw store energy. Resistances have K/W units, capacities J/K.

Our rearrangement of its reported state matrices (Eq24,PDF7/206) is:
\[
C_b\dot T_b=\dot Q-\frac{T_b-T_w}{R_b}
-\frac{T_b-T_\infty}{R_g},
\quad
C_w\dot T_w=\frac{T_b-T_w}{R_b}-\frac{T_w-T_\infty}{R_w}.
\]
This shows cancellation of the shared exchange rate and a passive conductive network. It is not a buoyancy/advection model. Capacities describe participating building components, not automatically exact material inventories.

The calibration data come from a USN experimental building. Multiple acquisition subsets are combined, filtered and resampled; an artificial random component of covariance.1 is added to temperature measurements (§3.2,PDF6). Adding noise after filtering does not restore the original measurement covariance or establish traceable sensor accuracy.

Table2 nominal Rb=.1,Rw=.1,Rg=.25K/W and Cb=Cw=1.2×10^6J/K; initial feasible bounds are.3–1.7times nominal. These are calibration constraints, not independent confidence intervals.

## Likelihood and numerical procedure

Eqs4–5,PDF2/201 define continuous stochastic state evolution and discrete observations. The innovation is \(\epsilon_k=y_k-\hat y_{k|k-1}\); its covariance is \(E_{k|k-1}\). Reported objective Eq14,PDF4/203:
\[
g=\sum_k\{\epsilon_k^TE_{k|k-1}^{-1}\epsilon_k+
\log\det E_{k|k-1}\}.
\]
Up to constants this is−2log likelihood under the adopted Gaussian innovation approximation and initial conditioning. The log determinant must be retained when covariance changes with parameters. A fit to raw open-loop residuals and a filter innovation objective are different comparisons.

COBYLA optimizes constrained parameters. RCSimulator uses component balances and implicit Euler; comparisons include explicit Euler,RK4 and exact linear zero-order-hold discretization (§§3–4,PDF6–7). Continuous noise spectral density and discrete covariance need a time-consistent conversion; their symbols W are reused in both contexts.

Process noise is tuned by trial and error, W=diag(.004,.002); measurement V=diag(.1,.1) (§4.2,PDF7). These are study-specific effective noise choices, not a full calibrated TRIDENT uncertainty model.

## Results and assessment limits

The two-state linear example favors UKF over finite-ensemble EnKF for cost and agreement with an exact-discretized KF baseline. EnKF cases use50,500,2000,5000 members (Tables3–6,PDF7–8). This does not establish universal UKF superiority for high-dimensional/nonlinear systems.

Fig5 deterministic simulation explicitly reproduces **calibration** data; process noise is tuned on associated residual checks. Fig6's estimated outputs and2sd bands do not independently establish held-out autonomous predictive coverage (§§4.4–4.5,PDF8/207).

Profiles over constrained ranges reveal a Rb/Rw valley and kinks caused by bounds. Increasing upper bounds from1.7to6times nominal produces profiles crossing the selected thresholds (§4.6,Figs8–11,PDF9–10). The paper reports all five parameters as identified over the expanded range, albeit with large confidence regions. These reported labels depend on the inferential conventions noted below.

2D profiling is computationally expensive: a100×100grid for each of10pairs implies100000 nuisance optimizations. Reported30–60minutes per pair is hardware/model-specific, not a TRIDENT cost forecast (§4.5.1,PDF9).

## Statistical/implementation appraisal

**Objective normalization:** Eq12 defines ℓ=−logL, while Eq14 removes the factor1/2. Eq21 then prints a likelihood-ratio identity inconsistent in sign/factor with that definition (PDF3–5,visually checked). Our consistent choices are either \(2[\ell(\theta)-\ell(\hat\theta)]\) or \(g(\theta)-g(\hat\theta)\), up to the same additive constants. The implementation must establish what was evaluated before applying χ² cutoffs; we have not audited the executed code.

**Profile interpretation:** profiles are not normalized probability distributions. A bounded or unbounded scan does not by itself establish global structural identifiability. Flat exact invariance, finite ranges and optimizer limitations must be distinguished. A narrower interval with another parameter fixed is conditional information; it does not show that a wider nuisance-profile interval “overestimates” uncertainty. 1D and2D confidence cutoffs also answer different questions.

**Residual tests:** ACF/cumulative periodogram assess serial structure/whiteness, not Gaussian marginal shape by themselves. A visually satisfactory2sd band on fitted/filter-assimilated data is not independent predictive coverage. Nonlinear transformations of Gaussian state noise need not yield Gaussian innovations automatically.

The EnKF description as equivalent to MCMC should not be copied into an implementation specification: an ensemble propagation/filter update is not automatically a Markov-chain posterior sampler.

## Claim-to-evidence ledger

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S67-C01 | The demonstration is a two-state R3C2 building network with measured power/outdoor inputs. | Fig1/§3.1/Eq24,PDF6–7/205–206 | No circulation/advection physics. |
| S67-C02 | Likelihood uses innovations and their covariance including a log determinant. | Eqs7–14,PDF3–4/202–203 | Conditional Gaussian/filter approximation. |
| S67-C03 | Data are filtered/resampled and artificial temperature noise added. | §3.2,PDF6/205 | Not a reconstruction of traceable original metrology. |
| S67-C04 | UKF is efficient relative to EnKF in this small linear example. | Tables3–6/§4.5,PDF7–9 | Not general algorithm dominance. |
| S67-C05 | Calibration replay and fitted bands are used as validation evidence. | §4.4/Figs5–6,PDF8/207 | No independent predictive coverage established. |
| S67-C06 | Bounds and parameter dependence materially alter reported profiles. | §4.6/Figs8–11,PDF9–10 | Global identifiability/coverage needs further justification. |
| S67-C07 | The printed likelihood-ratio normalization needs reconciliation. | Eqs12/14/20/21,PDF3–5 | Analyst mathematical audit; executed objective unknown. |
| S67-C08 | Serial residual diagnostics alone do not establish Gaussianity or held-out validity. | §§2.5/4.4,PDF5/8 plus analyst qualification | Preserve separate statistical questions. |
| S67-C09 | Exhaustive pair profiles have substantial optimization cost. | §4.5.1,PDF9 | Select consequential groups before exhaustive scans. |

## Coverage and implications

| Section | Coverage | Remaining limitation |
|---|---|---|
| §1 PDF1–2 | Inspected/extracted | Earlier CTSM originals not all read |
| §§2.1–2.3 PDF2–4 | Inspected/extracted;PDF3 visual | Full filter code/table not reproduced |
| §§2.4–2.5 PDF4–5 | Inspected/extracted;PDF5 visual | Cutoffs and calibration not independently checked |
| §3 PDF5–7 | Inspected/extracted;PDF6–7 visual | Input histories/sensors/code not acquired |
| §4 PDF7–10 | Inspected/extracted;PDF9 visual | No rerun/independent holdout evaluation |
| §5/references PDF10–11 | Inspected | New leads remain uninspected unless separately recorded |

For TRIDENT, include initial/observation/boundary uncertainty, preserve the distinction between filtering and prediction, and use identifiable groupings without assigning material meaning by name alone. S69/S70 directly test that interpretation. S68 extends sensor-location and model-structure choices.
