# S78 — Passive multiport RC identification: scoped original-source dossier

L. De Tommasi, A. Magnani, M. de Magistris, *Advancements in the identification of passive RC networks for compact modeling of thermal effects in electronic devices and systems*. International Journal of Numerical Modelling 31(3), e2296 (2018). DOI [10.1002/jnm.2296](https://doi.org/10.1002/jnm.2296). First online 15 September 2017; copyright 2017; issue citation 2018. These dates explain the uploaded filename, not a source mismatch.

## Identity, integrity and reading depth

User-supplied publisher PDF, 13 consecutive pages, printed “n of 13” = PDF page n. Title/authors/DOI and issue citation match publisher metadata checked 21 October 2026. The copy includes the 13 April 2018 post-publication correction to Eq12 on PDF4. §§1–6, Figures1–8, Table1 and references1–46 are present. All relevant main text read; PDF3/4/10 equations, correction and error table visually checked; other figures inspected by text/captions, not digitized. No appendix or external supplement is identified in the supplied article. Code, underlying FEM/semianalytical models and cited originals not acquired or executed. Ready for scoped method/novelty and conditional-baseline synthesis, not numerical reproduction or uncertainty validation. The earlier abstract-only access note remains historical; S78-C01 is preserved.

## What problem and model family does it address?

The authors identify a reduced thermal **port-response map**, using nested time-constant optimization and positive-semidefinite coefficient fitting, then describe a Foster multiport realization. The intended problem is a linear diffusion system with real decay poles, not nonlinear natural circulation. Earlier vector fitting, positive-fraction identification, Foster/Cauer realization and their own 2014 time-domain method are acknowledged foundations, not new inventions here (§1/PDF1–2; §4/PDF7–8).

Thermal ports use input power and output temperature rise above ambient. Reported “thermal impedance” Zth(t) means a normalized **step response**, not the Laplace/Fourier transfer function of an impulse (§2, Eqs1–8/PDF3). Their arbitrary-input representation uses the impulse kernel, which is the derivative of that step response. Initial perturbations are implicitly zero in the convolution formulation. A different initial wall state needs an additional state-response term.

## Equations, conventions and implementation relevance

Reported Eq10/PDF4 gives H(s)=Σ Hn/(s−pn)+H∞. Eqs15–19/PDF5 give, for the strictly proper step-response part,

\[
Y_{step}(t)=\sum_n A_n(1-e^{-t/\tau_n}),\quad
\tau_n=-1/p_n>0,\quad A_n=\tau_n H_n\succeq0.
\]

This is reported mathematics in normalized notation, not a complete solver transcription. For temperature/power ports, **our dimensional check** gives Ystep and An K/W, τn seconds, pn 1/s and Hn K/(W·s). H∞, if retained, is a separate instantaneous feedthrough and must not be silently dropped or fitted as a storage mode. A temperature difference may be K or °C; temperature-dependent properties and radiation invalidate a globally fixed linear map unless a restricted linearization is justified.

The inner fit is a convex positive-semidefinite coefficient problem **at fixed time constants**, while the outer relocation is nonlinear and may be local (Eqs19–22/PDF5–6). Convexity of the inner problem does not prove uniqueness of the entire time-constant/model-order identification. Eqs23–31/PDF6–7 describe Gauss–Newton/barrier calculations. Printed normal equations are not a recommendation to implement numerically fragile inverses. The authors refer to MATLAB/CVX; source code and actual tolerances are not supplied here. A direct reconstruction requires fresh checks of derivatives through the optimized inner fit and constraint handling.

Foster realization uses positive elements and ideal multiport transformers (§4/Fig3/PDF7–8). Those equivalent states/elements are not identified pipe layers, local wall inventories or material properties. A response-equivalent passive network may be useful without its internal realization being the unique physical thermal construction.

## Cases, evidence and limitations

§5/PDF8–11 uses two 5×5 thermal-impedance matrices from FEM power-module calculations and one 12×12 set from a semianalytical device calculation. The reported method uses 12 common time constants for each first case and 20 for the last (PDF9–11). These are fit-to-computed-response demonstrations; independent withheld physical experiments, sensor uncertainty, input-error inference and posterior predictive coverage are not demonstrated.

Table1/PDF10 compares with separately fitted exponential terms. **Our table audit:** all six displayed diagonal entries in each of the first two cases have higher RMS error under NLLS+CVX than the comparator, while the nine displayed off-diagonal entries improve. Thus the prose's broad accuracy claim should not become entrywise superiority. A shared low-order representation and full-response aggregate error are different criteria from each port's accuracy; choose a TRIDENT-relevant criterion. No new aggregate metric was recomputed here.

The two heat-sink coefficients are labeled 0.2 and 2.5 K/W, yet the latter is described as more efficient cooling (PDF8). K/W is resistance-like; the prose/convention needs clarification before borrowing these boundary values. They are not TRIDENT heat-transfer coefficients.

## Mathematical scope flags: our checks, not author findings

1. Eq4/PDF3 prints input PD(t) inside a convolution over τ. The conventional causal convolution uses PD(τ). Do not silently transcribe the printed expression into a general-input solver; the later Eq14/PDF5 uses the integration variable consistently.
2. PSD residues with negative real poles are a useful sufficient passive RC/positive-fraction restriction. The prose after Eq11/PDF4 should not be exported as a theorem that **every** real-pole positive-real transfer function has nonnegative residues. For example, in dimensionless s, our counterexample H(s)=1/(s+1)−0.5/(s+2) is analytic in the right half-plane and has positive real part there: for s=x+iy,x≥0, twice its real-part numerator has positive coefficient x on y² and positive constant (x+1)(x+2)(x+3). It nevertheless has a negative residue. This distinguishes a general positive-real class from the intended RC positive-fraction class; it does not show the paper's constrained algorithm fails for its intended class.
3. PSD is a matrix condition, not elementwise positivity. Arbitrary probe outputs and arbitrary heat-source locations need a justified port/duality/reciprocity contract before a positive-real multiport interpretation. The source's original circuit-theory references remain unread originals; a full general realization theorem is not claimed here.

## Cross-source and project consequences

S78 is strong prior art against claiming that fitting a low-order passive thermal response, sharing decay time constants or using nested nonlinear/convex optimization is intrinsically new. It complements S26's network selection and S67/S73's stochastic inference; they solve different problems and make different assumptions.

**Conditional use:** a linear conductive wall/insulation submodel or a controlled synthetic multiport benchmark. **Important mismatch:** TRIDENT currently reports sparse centerline/wall probes and a limited set of actuators, not the full independently excited thermal step-response matrix assumed by the examples. Advection, buoyancy feedback, variable properties, unknown inputs and shared measurement errors require additional treatment. Do not force a passive real-pole model onto oscillatory/advective loop dynamics or interpret its fitted Foster elements as local materials. No extra heaters, sensors or qualified CFD are assumed.

## Stable claim additions

| ID | Finding / appraisal | Original locator | Qualification |
|---|---|---|---|
| S78-C02 | Step-response impedance and impulse transfer are distinguished. | §2/Eqs1–8, PDF3 | Linear diffusion/zero-perturbation response; our units follow dimensionally. |
| S78-C03 | Positive time constants and PSD coefficient matrices define the fitted response family. | Eqs15–19, PDF5 | Restricted passive RC class, not arbitrary loop dynamics. |
| S78-C04 | Inner coefficient optimization is convex at fixed time constants; outer relocation is nonlinear. | Eqs19–31, PDF5–7 | No full nonconvex/global-optimum or parameter-uniqueness proof inferred. |
| S78-C05 | Foster realization introduces equivalent RC elements and ideal multiport transformers. | §4/Fig3, PDF7–8 | Not a unique material/geometry reconstruction. |
| S78-C06 | Demonstrations fit two FEM and one semianalytical thermal-response datasets. | §5, PDF8–11 | No independent physical/noise-coverage assessment demonstrated. |
| S78-C07 | Table1 improves displayed off-diagonal errors but worsens all six displayed diagonal errors in each first case. | Table1/PDF10; discussion/PDF9 | Our rowwise table audit, not a recomputed global comparison. |
| S78-C08 | Eq4's integration-variable notation and Eq11's exported general passivity reading require qualification. | PDF3–4 | Analyst limiting-case checks; not evidence of executed-code failure. |
| S78-C09 | Uploaded copy includes the post-publication Eq12 correction. | Footnote/PDF4 | Final issue2018/online2017 identity retained. |

## Coverage checklist

| Material | Inspected/extracted | Not completed |
|---|---|---|
| §1 PDF1–2 | Purpose and method lineage | Cited originals not thereby read |
| §2 PDF3–4 | Response/port definitions and dimensions; selected visual check | Full general realization proof |
| §3 PDF4–7 | Constraints, nested optimization and numerical procedure | Code, derivative and convergence reproduction |
| §4 PDF7–8 | Foster synthesis role and equivalent-state limits | Synthesis implemented or general theorem rederived |
| §5 PDF8–11 | Data provenance, reported model orders and Table1 visual audit | FEM inputs/raw responses, timing reproduction or independent experiment |
| §6 PDF11–12 | Claims and transfer limits | No new empirical conclusion |
| References PDF12–13 | Inspected for relevant leads | Earlier passive-realization and original data articles unacquired |

**Acquisition status:** requested original received; no re-upload needed. Further source acquisition is branch-specific, not a prerequisite to improving the two literature reviews.
