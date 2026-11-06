# S59 — Rodríguez-Bernal and Van Vleck (1998): exact reduction and diffusion

## Identity and reading limits

Aníbal Rodríguez-Bernal and Erik S. Van Vleck, “Diffusion Induced Chaos in a Closed Loop Thermosyphon,” *SIAM Journal on Applied Mathematics*58(4),1072–1093. DOI:https://doi.org/10.1137/S0036139996304184. Supplied SIAM publication PDF,22 consecutive pages; PDF n=printed n+1071. Title, theorem/equation sequence, numerical figures and terminal references are present. All extracted text inspected; governing model and reduced-subsystem theorem visually checked onPDF2,12. No appendix/supplement identified.

Purpose-scoped readiness: mathematical model structure and qualified reduction claims can enter synthesis. **Proofs were read for assumptions and logical structure, not independently verified line by line.** No numerical result was reproduced. Relevant original questions: C reduction/closure choices, D learning, G uncertainty/verification, A3–A4 transfer.

## Problem and established results

The paper studies an ideal constant-area loop completely filled with fluid, spatially uniform scalar circulation velocity v(t), prescribed spatial heat input/removal h(x), geometry/gravity f(x), friction G(v)v and axial diffusion ν. The authors establish well-posedness under stated regularity assumptions, dissipativity/attractor properties when ν>0, and a reduced nonlinear subsystem determined by overlap of heating and geometry Fourier supports. Special cases connect to Lorenz equations. This is a mathematical result about a specified coupled ODE–PDE, not an empirically validated ROM for arbitrary loops.

Earlier work discussed includes Keller and Welander, general-geometry models, Newton-cooling reductions and inertial-manifold work. Cited originals beyond our inspected sources remain leads.

## Equations, assumptions and conventions

Reported Eq.(1.1),PDF2/1073, visually checked:

\[
\dot v+G(v)v=\int_0^1Tf\,dx,\qquad
T_t+vT_x=h(x)+\nu T_{xx}.
\]

The periodic path is normalized to x∈(0,1). Physical constants have been absorbed into G,f,h and scaling choices. Thus ν cannot simply be copied as dimensional water/salt diffusivity. Analysis assumes \(G(v)\ge G_0>0\), with local Lipschitz conditions on the drag map. The introductory pure quadratic G=|v| does not satisfy the strict lower bound at zero; the numerical example instead uses |v|+10^-4.

The average energy equation is \(\frac d{dt}\int T\,dx=\int h\,dx\). Nonzero net prescribed heating makes mean temperature grow; the authors remove the mean and analyze zero-mean functions (§2,PDF3–4/1074–1075). This is a change of variables, not physical control of mean temperature. It does not justify suppressing an evolving mean in an unequally heated/cooled TRIDENT model.

Fourier convention is \(T=\sum_{k\ne0}a_ke^{2\pi ikx}\), with conjugate pairs for real fields. Eq.(3.1),PDF8/1079:

\[
\dot a_k+(2\pi ikv+4\pi^2\nu k^2)a_k=b_k.
\]

Advection rotates phase; positive ν damps modes at a k²-dependent rate. There is no generic nonlinear mode cascade as in full Navier–Stokes: coupling occurs through scalar velocity. Fixed, state-independent spatial h is essential. Spatially localized cooling proportional to evolving temperature can couple modes and invalidate this exact closure.

Let K be nonzero heating Fourier support and J geometry support. The nonlinear subsystem uses K∩J. Theorem3.6,PDF12–13/1083–1084 identifies an attractor relation and finite odd-dimensional ODE system if K∩J is finite. Modes outside that subsystem may still be forced and require linear reconstruction with history. **Exact reduced asymptotic circulation dynamics is not exact arbitrary-initial-condition temperature reconstruction using only those coefficients.**

Theorem3.5,PDF11/1082 distinguishes an attracting invariant manifold and a tracking condition. Section3.1.3,PDF15–16/1086–1087 obtains a Lorenz special case with one conjugate pair and constant friction, after variable/time transformations. Standard Lorenz parameter meanings cannot be imported without those transformations.

## Numerical evidence and appraisal

Section4,PDF19–21/1090–1092 uses five real variables, G=|v|+10^-4, k=1,j=2,A=C=0,B=30,D=20 and stated initial conditions. A fourth-order implicit Gauss–Legendre scheme uses step-doubling local tolerance10^-6 and Newton/LAPACK solves (PDF19/1090). Cases show a bounded orbit atν=0, Lorenz-like behavior atν=.01 and.025, periodic response atν=.015, and equilibria for largerν. These are normalized examples, not measured diffusivity thresholds.

Proposition2.5 supplies an unbounded-temperature solution without diffusion under particular orthogonality/initial conditions (PDF8/1079). This does not mean every ν=0 orbit diverges; bounded numerical examples are also reported. Diffusion does not change the illustrated dynamics monotonically.

No instrumented experiment, measurement uncertainty, calibration split or predictive interval is reported. Examples are not exhaustive bifurcation continuation or empirical validation.

## Claim-to-evidence table

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S59-C01 | Scalar uniform velocity, fixed prescribed heat flux and axial diffusion define the model. | Eq1.1,PDF2/1073 | Not arbitrary conjugate-loop physics. |
| S59-C02 | Net prescribed heating evolves the mean; zero-mean analysis follows subtraction. | §2,PDF3–4/1074–1075 | Physical accumulation remains. |
| S59-C03 | Mode advection rotates phase; diffusion damping scales as k². | Eq3.1,PDF8/1079 | Direct model structure. |
| S59-C04 | Heating/geometry Fourier-support overlap determines a reduced nonlinear subsystem. | Thm3.6,PDF12–13/1083–1084 | Finite exact asymptotic reduction under assumptions. |
| S59-C05 | Omitted/slave modes can need reconstruction despite a small circulation subsystem. | Eq3.12,PDF14/1085;Thm3.6 | Sensor/extrema predictions remain separate. |
| S59-C06 | A special three-variable case transforms to Lorenz form. | §3.1.3,PDF15–16/1086–1087 | Constant drag and restricted supports. |
| S59-C07 | Diffusion examples switch nonmonotonically between periodic and Lorenz-like behavior. | §4,Figs1–2,PDF19–21/1090–1092 | Numerical examples, not measured phase diagram. |
| S59-C08 | Some nondiffusive solutions are unbounded while bounded examples also occur. | Prop2.5,PDF8/1079;§4,PDF19–20 | Quantifiers matter. |

## Implications for TRIDENT

This is strong prior art against claiming that a small Fourier circulation model or mathematical mode selection is new. Distinguish modes needed for nonlinear circulation feedback from those needed to reconstruct sensors or spatial extremes.

A relevant extension would have to confront state-dependent sources, conjugate wall/sensor dynamics, actual heating/geometry supports, finite-time discarded-mode errors and sparse observations. These are candidate questions, not established literature gaps or proved TRIDENT results. Effective mixing/diffusion fitted to stability is not an identified molecular property.

## Coverage checklist

| Section | Coverage | Remaining work |
|---|---|---|
| §1 PDF1–3 | Inspected/extracted | Historical originals not all acquired |
| §2 PDF3–8 | Assumptions/results inspected/extracted | Independent proof audit deferred |
| §3.1.1 PDF8–11 | Attractor/manifold qualifications inspected | Functional-analysis details not reproduced |
| §3.1.2 PDF11–15 | Subsystem/reconstruction inspected/extracted;PDF12 visual | Reconstruction not implemented |
| §3.1.3 PDF15–16 | Lorenz connection inspected | Transformation not independently rederived |
| §3.2 PDF16–19 | Contrast inspected/extracted | Technical algebra not transcribed |
| §§4–5 PDF19–21 | Results/discussion inspected/extracted | No rerun/digitization |
| References PDF22 | Inspected for leads | No inferred original reading |

Available S18 is the next model comparator. Rodríguez-Bernal1995 and earlier general-geometry papers are conditional proof-depth leads if this becomes the selected theory direction; no upload request precedes an access check and concrete need.
