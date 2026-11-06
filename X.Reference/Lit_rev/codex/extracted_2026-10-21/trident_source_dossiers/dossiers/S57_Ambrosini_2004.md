# S57 — Ambrosini et al. (2004): closure slope, numerical diffusion and stability

2026-10-20. W. Ambrosini, N. Forgione, J.C. Ferreri, M. Bucci, *The effect of wall friction in single-phase natural circulation stability at the transition between laminar and turbulent flow*, Annals of Nuclear Energy31(16),1833–1865. DOI https://doi.org/10.1016/j.anucene.2004.05.011.

## Identity and inspection

Publisher article33 continuous pages; printed=PDF+1832. All main text/captions and references inspected in extracted text; PDF5,9,12,30 visually checked for geometry, friction convention, discrete stability equation and preliminary CFD. Figure-only time-series pages were inspected through extracted labels/captions, not all visually enlarged/digitized. No appendices/supplement, model decks or source code supplied. Geometry/BC/experimental data originate in prior Vijayan work; those originals are separate evidence.

## Problem and actual result

An experimentally unstable water-loop condition is predicted stable by one system-code configuration. The authors investigate friction laws, discretization and perturbation size with RELAP5/MOD3.3, TRANLOOP and LINELOOP, and provide preliminary FLUENT calculations. Their controlled model comparisons strongly support the conclusion that closure and numerical choices can change predicted stability. They do **not** establish one universally correct natural-circulation friction law.

## Conditions and model contract

§2 (PDF5–6 / 1837–1838): rectangular glass loop ID23.2mm, vertical legs2.1m, heated/cooled lengths.8m; water, four bends with K=.75 and three tees K=.4, roughness10^-7m. Main reference heater420W, unstable in the prior experiment. Cooler treated by a secondary boundary on a heat structure in the simpler models, initially h=1000W/(m² K),secondary31°C.

§3.1 (PDF9/12 / 1841/1844): power sweeps200–550W, secondary flow4.5L/min,temperature31°C for RELAP. Later simple-model cooler h=900W/(m² K) to align with RELAP, and ambient revised20→30°C with ambient h7W/(m² K), based on additional BC information. These configurations must not be merged as an identical-input independent validation set. Paper's assumption that expansion-tank omission is second order is case-specific; Boussinesq does not generally make thermal storage irrelevant.

TRANLOOP/LINELOOP include fluid and heat-structure states, Boussinesq loop flow and first-order versus low-diffusion methods (§1,PDF3–4). Full governing discretization is referred to earlier methodology papers. Friction functions are described and plotted rather than fully derived.

## Mathematics, conventions and findings

Fig5/§3.1 (PDF9 / 1841) explicitly uses **Fanning friction factor**, unlike S30's Darcy convention. In a conventional circular pipe \(f_D=4f_F\), and pressure-loss equations must be transformed consistently; numerical coefficients cannot simply be copied between conventions.

One closure takes max(Poiseuille,Colebrook–White), monotonically decreasing f, with the source reporting transition nearRe1100. Churchill/RELAP-like transition behavior has a nonmonotone branch. Reference420W is aroundRe2700, with local property variations. These are source-specific ranges, not universal transition thresholds.

**Reported discrete stability:** Eq1 (PDF12 / 1844) is
\[
\delta x^{n+1}=A\,\delta x^n,
\quad x=(W,T_{f,1},\ldots,T_{f,N},T_{w,1},\ldots,T_{w,N}).
\]
Eq2 defines \(z_R=\ln(\rho(A))/\Delta t\) and an angular frequency from an eigenvalue and the spectral radius; Eq3 gives period \(2\pi/z_I\) (PDF15 / 1847). These are **discrete update** quantities, not eigenvalues of a continuous ODE Jacobian.

There is an internal convention conflict: nomenclature identifies the eigenvalue with largest magnitude, while prose near Eq2 says maximum real part. Spectral radius requires largest modulus. For \(\lambda=\rho e^{i\theta}\), the corresponding derived continuous growth/frequency is log(lambda)/dt, with branch/aliasing qualifications. The printed arccos expression needs an eigenvalue on that modulus and does not determine frequency sign. Do not mix its result with S30's continuous-Jacobian eigenvalues without the mapping.

Our implementation implication: compute consistent eigenmodes of the implemented discrete map, verify their continuous-time limit with refinement, then compare transient growth/period under the same closure/BCs. Zero growth is a boundary requiring further analysis, not automatically a robustly stable operating point.

§§2–3.1/Figs1–12 (PDF5–17): low-diffusion method captures instability with coarse/fine meshes where first-order coarse treatment suppresses it. Changing friction to Churchill yields a stable intermediate band that is absent with the alternative transition law in the illustrated maps. Numerical diffusion changes the band size/growth rates but does not wholly explain its existence. Thus matching a steady flow rate is insufficient to verify dynamic predictions.

§3.2/Figs15–17 (PDF18–27 / 1850–1859): different initial flow, with the same initial thermal field, changes finite-window transient outcomes. Local stability does not determine every finite-disturbance trajectory. Some low-power RELAP pulses involve **voiding/boiling** (PDF19 / 1851); those cannot be cited as demonstrated single-phase oscillations or imported into TRIDENT's intended regime.

§4/Figs18–20 (PDF28–31 / 1860–1863): preliminary FLUENT6.0 calculation,45920cells,transientdt.05s,conjugate heat structures,900W/(m² K) cooler/31°C. It reproduces instability and roughly100s period, and shows asymmetric profiles/separation/reattachment from bends. Authors explicitly call it preliminary; no formal grid/time uncertainty, independent local-velocity validation or full turbulence-model assessment. CFD is a possible research tool, not assumed available TRIDENT truth.

## Evidence strength and applicability

The strongest contribution is a model-discrimination demonstration: with comparable discretization, changing transition friction changes the predicted dynamic state. However, boundary revisions, uncertain loss coefficients, prior experiment limitations and absent propagated UQ constrain a universal accuracy claim. The paper explicitly leaves geometry-dependent forced-flow closure suitability unresolved (§§4–5,PDF19–21/29–31).

No reported experiment-calibration/untouched-test split or posterior distribution. Previously cited percentage discrepancies and elevated natural-circulation friction are **prior authors' findings**, not new measured quantities in S57.

## Claim ledger

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S57-C01 | Closure choice can switch predicted stability for the reference loop | §§2–3.1/Figs3–12, PDF5–17 | Water-loop cases; not universal friction selection |
| S57-C02 | Numerical diffusion can suppress or alter predicted instability | §2/§3.1, PDF5–6/16–17 | Discretization-specific; refine time/space/observables |
| S57-C03 | BC/coefficient changes must be retained in comparisons | §3.1, PDF12 / 1844 | Later h/ambient differ from initial cases |
| S57-C04 | Fanning/Darcy and discrete/continuous stability conventions differ | Fig5/Eqs1–3, PDF9/12/15 | Our implementation mapping and source ambiguity |
| S57-C05 | Finite initial perturbations affect finite-window behavior | §3.2/Figs15–17, PDF18–27 | Some RELAP pulses are two-phase |
| S57-C06 | Preliminary CFD shows local asymmetry and instability | §4/Figs18–20, PDF28–31 | Not full V&V or measured3D local truth |
| S57-C07 | The paper does not settle a universal natural-circulation friction law | §§4–5, PDF19–21/29–31 | Geometry/regime/closure dependence remains |

## TRIDENT consequences / coverage

For any stability/settling claim, vary closure, numerical resolution, admissible initial conditions and BC uncertainty. Preserve steady and dynamic targets separately. A stable fitted temperature response need not identify physical hydraulic damping. A proposed thesis criterion should predict observable errors/margins under withheld conditions, not simply reproduce an existing stability map.

| Portion | Coverage | Outstanding |
|---|---|---|
| §§1–2 and BCs | Inspected/extracted; PDF5 visual | Original experimental metrology/decks not supplied |
| §3.1/Eqs1–3/Figs5–14 | Inspected/extracted; PDF9/12 visual | Earlier full discretization originals not read |
| §3.2/Figs15–17 | Text/caption/axis inspection | No raw series/digitization or complete visual audit |
| §§4–5/Figs18–20 | Inspected/extracted; PDF30 visual | Preliminary CFD not reproduced |
| References | Inspected selectively | No implied reading of cited originals |

Ready for qualified closure/V&V/stability and prior-art synthesis. Not a literal code specification or a validated TRIDENT stability envelope.
