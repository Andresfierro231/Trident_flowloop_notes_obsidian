# S18 — Dass and Gedupudi: conjugate Fourier loop model

## Identity, version and completeness

Akhil Dass and Sateesh Gedupudi, *Fourier series based modeling of the dynamics of inclined closed loop buoyancy driven heat exchangers with conjugate effect*, arXiv:2007.03878v1,8July2020. Related journal citation: *International Journal of Thermal Sciences*167(2021),106987, DOI:https://doi.org/10.1016/j.ijthermalsci.2021.106987. Journal title adds “1-D numerical.” **This dossier extracts the preprint, not an assumed identical journal version.**

Local preprint32 consecutive pages, printed=PDF page. Main text, §8 Appendix, nomenclature and references present. All main-text and appendix extracted text inspected; PDF4,5,7,12,27,28 rendered, with consequential equations/tables visually checked. Plots were read through text/captions and selected figures; no exhaustive digitization or solver reproduction. No separate supplement identified.

Purpose readiness: conjugate reduction/closure assumptions, claimed comparison and prior-art synthesis. Not ready as a copied implementation or a journal-equivalence audit. Original questions A3–A4,C1–C6,D1/D4/D5,G7,I2/I3,K1/K3.

## Problem and claimed advance

The system is two natural-circulation loops coupled through a finite-thickness common heat-exchanger wall. Both sides are buoyancy-driven; this is different from one primary loop cooled by a prescribed or pumped secondary circuit. The paper adds wall storage/axial conduction and in-plane inclination to a Fourier model, comparing with laminar3D CFD and earlier numerical work.

Its introduction cites earlier Fourier reductions, including S59 and S58, and previous conjugate loop work. It is strong prior art against novelty based only on combining low-dimensional Fourier states and a conducting wall. It does not demonstrate identifiability from sparse experimental sensors.

## Geometry, fluid, boundaries and ranges

The CFD model uses two square loops, each nominally1m high×1m wide, with square duct side/hydraulic diameter.04m. Common-wall cases are0,1,5mm; inclinations0° and45° are the four principal cases (§4,Tables1–2,PDF10–11). The1D comparison adjusts straight-leg dimensions to1−2R and neglects bend buoyancy (§4.4.2,PDF16); this is a modelling approximation, not the same exact geometry.

Fluid properties are intentionally fictitious: density50kg/m³,cp5J/kg/K,β.08K^-1, thermal diffusivity.8m²/s, dynamic viscosity.005kg/m/s. Wall values include density8978kg/m³,cp381J/kg/K,diffusivity.00011m²/s (Table3,PDF12). Thus ν=.0001m²/s and Pr=.000125, consistent with the reported very-low-Pr case. These are not salt or glycol properties.

Boundary heat flux magnitude is2000W/m² at heating/removal sections; initial temperature300K and velocity zero (Tables3–5,PDF12). Secondary loop removal is a prescribed flux, not a resolved external cooling mission. Coupling occurs through the common wall; other walls are treated according to the idealized problem.

No experimental sensors, calibration errors or repeatability campaign are reported. Dimensionless parametric studies vary St,Fow,CoB and inclination, but do not establish a real-material property domain for all combinations.

## Equations, reduction and conventions

Velocities ω1,ω2 are dimensional m/s. Momentum is loop-integrated Boussinesq balance; shear uses a **Fanning** convention, as explicitly defined in nomenclature (PDF29–30), distinct from S66's Darcy factor. Geometry functions encode gravity projection; λ selects wall coupling. Fluid equations contain axial diffusion; the common wall is lumped through thickness with axial diffusion and zero axial heat flux at its ends (§2,Eqs1–16,PDF3–5).

The author's reported wall equation, Eq3,PDF4:
\[
\partial_tT_w=\frac{U\lambda}{\rho_wc_{p,w}t_w}
(T_1+T_2-2T_w)+\lambda\alpha_w\partial_{xx}T_w.
\]
Here U has W/m²/K units, so U/(ρcp tw) has inverse-time units. It represents interface exchange in this model; do not confuse it with a separately resolved two-film overall cooler coefficient in another geometry.

Fourier functions use exp(iπks) on a normalized length2, coefficient normalization1/2 (Eq37,PDF8). Localized coupling creates modal convolutions, e.g. \(\sum_m\lambda_{k-m}(\theta_{1m}-Co_B\theta_{wm})\), rather than the uncoupled thermal-mode structure of S59's fixed-source problem (§3.1,Eqs24–36,PDF6–7).

The calculation retains modes k=−3…3 with real/conjugacy constraints. “Three Fourier nodes” does **not** mean a three-state model. MATLAB ode15s solves the truncated ODE system. Wall end conditions are enforced using relations among mode coefficients; the presented simplification assumes aspect ratio1 (§3.3,PDF8–9).

CoB is fluid-to-wall capacity scaling proportional to1/tw, while Fow represents axial wall diffusion over the selected time/length scale. These choices mix storage/coupling and dimensionless normalization; compare dimensional QoIs before interpreting parameter sweeps as physical wall changes.

## Closure, comparisons and what was fitted

The heat-transfer closure uses a Seban–Shimazaki liquid-metal correlation and a proposed circular-duct to plate scaling (§3.4,Eqs50–53,PDF9). Its selection follows the fictitious lowPr regime. It is not justified for VCU glycol by geometric rescaling alone.

A mode-count comparison uses n=2,3,4 for circulation and loop-average temperature in a selected high-response case (§3.6,Fig2,PDF10). CFD grid/time studies compare up to1.8million elements and.1/.2s steps, selecting1million/.2s, again using bulk Re and average temperature (§4.2.2,Fig5,PDF13). These are not convergence evidence for unobserved extrema or every mode.

The CFD “validation” compares a corresponding single-loop steady relation with Vijayan's correlation and references Borgohain data; the authors explicitly lack direct coupled-loop experiment data (§4.2.3,PDF13–14). Main conjugate transient comparisons are code-to-code.

The paper reports maximum differences around5% in Re and15% in average nondimensional temperature for cases(a)–(c), not a validated predictive uncertainty interval (§4.4.2,PDF16). At inclination45° the temperature mismatch motivates a piecewise multiplier1 below35° and1.9 above35°, extracted from its CFD study (Eq55,Fig12,PDF17–19). Fig13 then reuses that information. This is a correction/comparison within the same study, not a fully independent holdout assessment.

## Equation and interpretation audit

These are findings about the **preprint's printed expressions**, not unaudited executed code:

- Eqs9–13 contain an impossible first interval0<x<0; Eq2/5 lack the spatial heater/cooler selector made explicit later in Eq18/21, and the dimensional cooling-source sign needs reconciliation (PDF4–5).
- Eq3 has T1+T2−2Tw, whereas Appendix Eq74 prints T1+Tw−2Tw (PDF27, visually checked). Our energy-balance reading of Eq73 supports the former; report the distinction rather than silently replacing it.
- Eq19 and its Fourier stencil Eq26 differ by a visible prefactor4; λs in Eq19 is not separately defined there. Real/imaginary equations retain explicit i terms. Re-derive normalization and real equations before coding (PDF5–7).
- Positive-only resistance powers require sign-aware reversal conventions; K's Re and Dh conventions need checking before dimensional reuse.
- §5.2 says largerCoB gives faster settling, while conclusion2 states decreasingCoB does so (PDF21/26).
- Appendix sensitivity ratios divide large finite percentage changes, including900% changes inCoB; they are not local derivatives proving negligible dependence. For example Table7's endpoint Re changes15.50876→13.75766 and θAvg.016207→.013891 across the sweep, roughly11.3% and14.3% decreases by our calculation. “Insensitive” needs a QoI tolerance, not only the small ratio of percentages.

## Claim-to-evidence ledger

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S18-C01 | The model couples two buoyancy loops through a conducting/storage wall and Fourier reduction. | §§2–3,PDF3–10 | Not a single-loop/prescribed-secondary equivalent. |
| S18-C02 | CFD uses fictitious fluid at Pr.000125. | Tables3/5,PDF12 | No direct glycol/salt material validation. |
| S18-C03 | Localized thermal coupling produces modal convolutions. | Eqs24–28,PDF6–7 | Contrasts restricted S59 closure. |
| S18-C04 | Three retained mode orders are checked against bulk Re/average temperature. | §3.6,Fig2,PDF10 | Not three total states or local-field convergence. |
| S18-C05 | Main conjugate transient assessment is against CFD; experiment comparison is indirect/single-loop. | §§4.2.3/4.4,PDF13–17 | No direct new coupled-loop experiment validation. |
| S18-C06 | Inclination-dependent heat-transfer correction is informed by the same CFD study. | Eq55,Figs12–13,PDF17–19 | Not independent generalization evidence. |
| S18-C07 | Reported Re/temperature differences are approximately5%/15% for specified cases. | §4.4.2,PDF16 | Comparison errors, not uncertainty bounds. |
| S18-C08 | Printed preprint equations need source/sign/prefactor/conjugacy reconciliation. | Eqs2–5/19/26/30–36/74,PDF4–7/27 | Analyst audit; code not evaluated. |
| S18-C09 | Appendix large-step sensitivity ratios do not prove negligible change of the QoIs. | Tables6–8,PDF27–28 | Analyst qualification; endpoint changes calculated above. |
| S18-C10 | Wall-parameter settling interpretation differs between body and conclusion. | §5.2,PDF21;§7,PDF26 | Unresolved preprint inconsistency. |

## Applicability and coverage checklist

Direct: model-form prior art, conservative exchange and closure/reduction diagnostics. Conditional: a rederived two-loop conjugate model in a compatible regime. Analogy: sparse thermal inference in TRIDENT. Incompatible without new justification: transplanting the lowPr correlation or1.9 multiplier to VCU.

| Section | Coverage | Remaining limit |
|---|---|---|
| §1 PDF1–2 | Inspected/extracted | Cited originals not all read |
| §2 PDF3–6 | Inspected/extracted;PDF4–5 visual | Sign/selector/scaling questions unresolved |
| §3 PDF6–10 | Inspected/extracted;PDF7 visual | No reconstructed ODE/code |
| §4 PDF10–20 | Inspected/extracted;PDF12 visual | Figures not exhaustively digitized; no CFD rerun |
| §§5–6 PDF20–25 | Inspected/extracted | Sweeps and linear-profile steady assumptions not independently reproduced |
| §7 PDF26 | Inspected/extracted | Body/conclusion tension retained |
| §8 PDF26–28 | Inspected/extracted;PDF27–28 visual | Full derivation not independently verified |
| Nomenclature/references PDF29–32 | Inspected for conventions/leads | Journal/preprint full diff still absent |

Next: use as a comparator in the model hierarchy; verify the journal version before treating preprint ambiguities as final-publication errors. No immediate upload is essential for the scoped conclusion.
