# S54 — Keller (1966): periodic thermal-convection motion

## Identity and extraction contract

Joseph B. Keller, “Periodic oscillations in a model of thermal convection,” *Journal of Fluid Mechanics* 26, 599–606. DOI: https://doi.org/10.1017/S0022112066001423. Supplied Cambridge publisher PDF, 8 consecutive pages; PDF page n = printed page n+598. Title, references, terminal page and equation sequence are present. Text was inspected throughout; PDF2,6,7 were also rendered and inspected for consequential mathematics. Scanned equations are visually readable but OCR is unreliable.

Purpose: historical mechanism and model-assumption synthesis, and a candidate analytical verification problem. This is not a validated TRIDENT model or a completed independent proof audit. Original questions: A1–A4 (motivation/transfer), C model forms, F identification, G uncertainty and numerical verification. Source claim IDs below are permanent.

## What the paper establishes

The paper constructs a particular periodic solution of an idealized loop model, then studies instability of a related continuous heat-exchange law. Its motivation is understanding convection oscillations. It does not establish MSR representativeness or report a new instrumented reactor experiment. Keller explicitly discusses Welander's 1965 Woods Hole report (§1,PDF1–2/599–600); journal publication order therefore does not establish discovery priority.

The loop has uniform cross-section, two vertical pipes and horizontal connectors, a point heater at the lower midpoint and point cooler at the upper midpoint (Fig.1,PDF2/600). Coordinate s increases counterclockwise from the heater; total length is 2L and cooler position L. Velocity u(t) is spatially uniform. Linear drag and negligible axial thermal conduction are assumed. Between exchange points temperature is transported without diffusion.

## Equations and conventions

Reported Eq.(2.2), PDF2/600:

\[
T_t+uT_s=0.
\]

Here T is temperature, u is length/time and s is length, so both terms have temperature/time units. Eq.(2.1) balances a whole-loop inertial term and linear resistance against the temperature integrals on the two vertical branches. The symbol μ there multiplies velocity as a total friction coefficient; it must not silently be treated as fluid dynamic viscosity.

**Printed convention requiring attention:** the density relation is printed \(\rho=\rho_0(1+\alpha T)\) on PDF2/600, despite α being called the volume expansion coefficient. Do not silently change it or implement it as a standard positive thermal-expansion law. Reconcile temperature/sign conventions and Eq.(2.1) first.

The heater/cooler outlet maps, Eqs.(2.3)–(2.4), depend on an even flow-dependent function f(u/u0). This is not a constant electrical-power heater. The later antisymmetry restriction relates temperatures half a loop apart, reducing the thermal state. The travel coordinate \(x=\int u\,dt\), introduced in §3, requires u to remain positive for the constructed solution; it is not a general reversal coordinate.

In §5 momentum inertia is set to zero and f is chosen discontinuously. The resulting exact solution is periodic in time while u stays positive. Thus the example is an oscillating unidirectional circulation, not periodic reversals. The admissibility restriction is \(2s_1<\gamma<1-2s_1\), implying \(s_1<1/4\), in the paper's dimensionless variables (§5,Eq.5.18 and following text,PDF6/604; visually checked). These are not dimensional facility thresholds.

Section 6 replaces the discontinuity with a steep continuous ramp and establishes unstable steady motion for sufficiently small ramp width. The author's inference is that a stable solution, if it exists, cannot be steady. This is weaker than proving existence, uniqueness or attraction of a periodic orbit for every continuous heat law (§6,PDF7–8/605–606).

## Results, validation and limitations

The primary result is analytical construction under a special heat law and zero momentum inertia. Figure2,PDF7/605 illustrates u and temperature versus travel distance, not directly a measured time trace. No measurement uncertainty, calibration split, posterior, experimental validation dataset or mesh study is supplied. Cited observations and reports remain cited evidence; they have not thereby been read in their originals.

For Codex, this paper can motivate a separate idealized transport-delay verification case after resolving its conventions. It cannot supply material properties, uncertain closure coefficients, a TRIDENT wall model, or a representative operating range. Adding constant power, finite wall storage, distributed heating or a flow reversal changes the problem.

## Claim-to-evidence ledger

| Claim ID | Paraphrased finding | Locator | Strength and limit |
|---|---|---|---|
| S54-C01 | The paper uses an ideal rectangular point-heated/cooled loop with uniform velocity and linear drag. | §2,Fig.1,Eqs2.1–2.4; PDF2–3/600–601 | Reported model; not measured geometry. |
| S54-C02 | Temperature is transported without axial diffusion between the exchange points. | Eq2.2,PDF2/600 | Direct equation evidence. |
| S54-C03 | Heat-exchange maps depend on flow; the heater is not a prescribed constant-power source. | Eqs2.3–2.4,PDF3/601 | Source-law applicability limit. |
| S54-C04 | An exact positive-velocity periodic solution is constructed with zero momentum inertia and discontinuous exchange. | §5,PDF4–6/602–604; Eq5.18 | Existence for this special model, not all loops. |
| S54-C05 | The continuous-ramp analysis establishes steady-motion instability, not a general periodic-orbit existence theorem. | §6,PDF7–8/605–606 | Direct result plus distinction in inference. |
| S54-C06 | Keller credits an earlier Welander report; publication year alone cannot assign conceptual priority. | §1,PDF1–2/599–600; references PDF8/606 | Historical attribution; report itself not acquired. |
| S54-C07 | The printed density/expansion convention needs resolution before implementation. | §2,PDF2/600, beforeEq2.1 | Analyst audit; plus sign visually verified. |

## Skeptical appraisal and transfer

Direct relevance: proof that a particular feedback model can oscillate, and a historically important reduced-loop construction. Conditional transfer: transport and source-response timing as candidate explanations for observed oscillations. Analogy only: use as an MSR system or a realistic ACU/VCU thermal model. It is incompatible with treating an externally specified heat-law map as a measured constant power input without rederivation.

Keller's inertialess oscillation and Welander's inertia-dependent amplification should be compared by heat law and geometry. They do not constitute a contradiction proving that inertia either always matters or never matters.

## Coverage and next actions

| Section | Relevance | Coverage |
|---|---|---|
| §1 PDF1–2 | Historical question and prior attribution | Text inspected/extracted |
| §2 PDF2–3 | Geometry, governing/source laws | Inspected/extracted; PDF2 visual check |
| §§3–4 PDF3–4 | Reduction and equilibrium | Text inspected; selected assumptions extracted; algebra not independently reproduced |
| §5 PDF4–6 | Exact periodic construction | Text inspected; positivity condition visually checked; full period formula not transcribed |
| §6 PDF7–8 | Continuous-law qualification | Inspected/extracted; PDF7 visual check |
| References PDF8 | Citation discovery | Inspected; cited originals not inferred read |

No appendix or supplement is identified in the supplied article. Ready for scoped historical/mechanism synthesis. Not ready as a transcription-complete implementation specification. The 1965 Welander report is a conditional historical-priority lead; S55 already provides the accessible later journal mechanism analysis, so there is no immediate upload request.
