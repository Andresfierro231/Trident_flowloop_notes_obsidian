# S62 — Matulis and Bindra (2025): stochastic first-reversal and dwell times

## Identity and inspection

John Matulis and Hitesh Bindra, “Effect of stochasticity on initial transients and chaotic itinerancy for a natural circulation loop,” *Physical Review E*112,044223 (published23October2025). DOI:https://doi.org/10.1103/42pn-wttx. Supplied APS publication PDF10 consecutive pages. PDF n maps to printed044223-n. All extracted text inspected, including Appendix/TableIII and references. PDF8–9 rendered and visually checked; equation/figure digitization and code reproduction not performed. No separate supplement identified in the supplied paper.

Ready for scoped stochastic-model/QoI synthesis and critical comparison with S30. Not a calibrated TRIDENT uncertainty model. Original questions: G uncertainty, C closures/reduction, F identification, transient decision/QoI questions.

## Problem and model provenance

This paper extends the deterministic/stochastic eight-state loop model developed in S30. Its new focus is the post-bifurcation initial transient to first reversal and subsequent chaotic itinerancy. It compares stochastic forcing structures and studies the distribution of reversal residence times.

The paper reports validation of the base ROM in the earlier work; this is not a new independent experimental validation of each noise model. Channel-flow DNS generates the noise training data, not an instrumented loop-specific turbulent-loss record.

SectionII,PDF3 describes a rectangular water loop with horizontal heat-exchange sections and vertical risers. **The prose says heater above cooler**, whereas S30's prior model context and usual HHHC arrangement need comparison before assigning vertical orientation. The scalar coefficients in TableIII alone do not resolve this inconsistency. Do not quietly substitute a geometry.

## Governing/reduced model and conditions

Momentum and energy balances are Eqs.(1)–(3),PDF3. Three complex temperature modes plus the mean and velocity give eight real ODEs,Eqs.(4)–(11). The mean temperature evolves through unequal source/sink terms; it is not silently fixed. TableI,PDF4 connects symbolic coefficients to geometry/properties; TableIII,PDF9 gives the evaluated example:

- Water properties at50.27°C; heater power1000W.
- Heater length1m, riser length2m, pipe radius.015m.
- Axial diffusivity.001m²/s.

That diffusivity is the effective transport coefficient inherited from the base model, not established molecular water diffusivity. The model uses velocity/temperature-dependent cooler correlations. It is solved using a custom fourth-order Runge–Kutta method with constitutive relations at intermediate states (§II,PDF3).

As in S30, printed Eq.(2) uses v² in resistance while the reduced Eq.(4) uses v|v|. Signed-drag conventions must be resolved before using reversal equations. TableI versus reduced coefficient ordering should also be checked against S30/code; symbolic/numeric labels are not a complete software specification.

## Stochastic forcing and what it represents

The normalized DNS fluctuation \(\delta=v'/\bar v\) modifies the minor-loss coefficient as \(c_{12,\mathrm{stoch}}=c_{12}(1+2\delta)\), §III,PDF4. δ is dimensionless, so this preserves coefficient units. This is a particular fluctuation approximation, not an inferred complete distribution of loop resistance.

Six comparators are developed:

1. Gaussian draws using observed standard deviation.
2. Fractional Gaussian noise using a fitted Hurst exponent.
3. Ornstein–Uhlenbeck drift/diffusion fitted by likelihood.
4. Kramers–Moyal drift/diffusion functions.
5. KM plus an empirically selected Gaussian filter.
6. A constrained block bootstrap of the same DNS record.

OU coefficients are evaluated at time steps spanning Taylor microscale to twice that scale; bootstrap is used because the DNS sample lasts about170s, shorter than simulated transients (§III,PDF4–5). The bootstrap is a common-data benchmark, not independent physical truth. Numeric OU coefficients, Hurst exponent, filter width, block-length law parameters and complete loop-specific noise calibration are not tabulated here. Data availability points to the channel database; it does not establish that every processed signal and solver artifact is archived.

## Results and uncertainty

For the selected system a subcritical Hopf bifurcation occurs around770W (§IV,PDF5), a model-specific value. Initial conditions use a nominal1% displacement from the unstable fixed point, then small additional perturbations. There are1000 trials per stochastic model; Gaussian KDE and bootstrap95% confidence intervals summarize the first-reversal distribution.

The deterministic first reversal is reported near18071s. Stochastic models shift the average earlier while retaining tails later than the deterministic value (§IVA,Fig2,PDF5–6). OU/KM/filtered-KM results are close to the DNS-bootstrap result. This is approximate empirical distribution agreement, not a formal equivalence theorem or validated reactor intervention time.

About25000 reversals per model characterize long-run dwell times. Step spacing is72.2s versus74.4s circulation time at the unstable fixed point (§IVB,PDF6); the authors connect the timing to buoyancy–friction cycles. Approximately the fastest85% of dwell-time CDFs are similar, with greater differences in the longest15%. Thus startup and stationary/recurrent QoIs respond differently to the same noise model.

SectionIVB/PDF8/TableII compares five-parameter log-plus-linear and exponential-plus-linear fits to selected CDF corners below a cutoff. Reported RMS errors are.000124 vs.00411 for deterministic and.0000968 vs.00296 for stochastic cases. These are fits to chosen summaries, not held-out model-discrimination scores.

## Consequential equation/statistical audit

Reported Eq.(12),PDF8, visually verified:
\[
F_{\log}(t)=a_1\ln[a_2(t-a_3)]+a_4t+a_5.
\]
Printed Eq.(13) gives \(a_1a_2/(t-a_3)+a_4\). **Our differentiation**, for constant parameters and a valid log domain, gives
\[
\frac{dF_{\log}}{dt}=\frac{a_1}{t-a_3}+a_4.
\]
The extra a2 does not follow from Eq.(12). Do not silently propagate the printed PDF formula. An empirical finite-window fit also needs domain, monotonicity, normalization and support specified before use as a generative probability law.

The paper interprets nonexponential dwell times as evidence against a Markov model. Our qualification: this challenges a simple time-homogeneous memoryless switching model with constant escape rate. Nonexponential first-passage/dwell times alone do not exclude a Markov diffusion in a richer state. A dwell-time density is not itself a hazard; compute \(f/(1-F)\) before interpreting a constant rate. Fractional Gaussian noise also has temporal dependence by construction, so “state-independent” should not be generalized to “memoryless.”

The near-miss/high-mode mechanism and observed maximum residence time are model/evidence interpretations. A finite observed upper time is not a rigorous universal stochastic upper bound. No nuclear damage model justifies the paper's general intervention-before-damage language.

## Claim-to-evidence table

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S62-C01 | Eight-state dynamics and earlier validation are inherited from S30. | §II,PDF3;TablesI/III | No new independent loop validation of noise. |
| S62-C02 | Minor-loss forcing compares six generators trained/constructed from channel DNS. | §III,PDF3–5 | Not TRIDENT-specific calibration. |
| S62-C03 | Stochastic first-reversal distributions shift earlier on average but can extend later. | §IVA,Fig2,PDF5–6 | Selected initial condition/system. |
| S62-C04 | OU approximately matches the common-data bootstrap for the studied QoI. | §IVA,PDF5–6 | Empirical agreement, not general equivalence. |
| S62-C05 | Initial transient and long-run dwell-time distributions have different noise sensitivity. | §§IVA–B,Figs2/4,PDF5–7 | Model-specific QoI dependence. |
| S62-C06 | The log-plus-linear CDF fit has smaller reported selected-point RMS error. | Eqs12–15,TableII,PDF8 | No held-out likelihood/support validation. |
| S62-C07 | Printed Eq13 is not the derivative of printed Eq12 for general a2. | Eqs12–13,PDF8 | Visually verified text; derivative is our audit. |
| S62-C08 | Nonexponential dwell times do not alone disprove Markov dynamics in a richer state. | §IVB,PDF8 plus analyst mathematical qualification | Narrows the authors' interpretation. |

## Relevance, coverage and next steps

Direct: stochastic reduced-model prior art and a useful separation of first-event from recurring-event QoIs. Conditional: low-cost correlated closure noise where physical regime, correlation time and amplitude are independently supported. Analogy: reactor intervention time. Incompatible: calling the illustrated distribution a total predictive uncertainty budget.

| Section | Coverage | Remaining limitation |
|---|---|---|
| §I PDF1–2 | Inspected/extracted | Cited originals not all read |
| §II PDF3,TableI PDF4 | Inspected/extracted | Geometry/order/sign conventions require code comparison |
| §III PDF3–5 | Inspected/extracted | Training parameters/artifacts insufficient for full reproduction |
| §IVA PDF5–6 | Inspected/extracted | No rerun or interval recalculation |
| §IVB PDF6–8 | Inspected/extracted;PDF8 visual | CDF fit/hazard not re-estimated |
| §V,Appendix PDF8–9 | Inspected/extracted;PDF9 visual | Property/noise uncertainty not propagated independently |
| References PDF9–10 | Inspected | No inferred reading of cited originals |

No immediate upload request: S30, S63 and S59 are available. Code and processed-noise records would matter only if this stochastic direction is selected for reproduction.
