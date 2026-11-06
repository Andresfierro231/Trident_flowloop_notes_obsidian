# S65 — Ruiz, Cammi & Luzzi (2015): internal heating changes loop stability

Extraction2026-10-20. **Scoped ready** for source-distribution/stability motivation and model-class comparison. Exact implementation requires resolution of the conventions below; no reproduced stability boundary or experimental validation.

## Identity and version

D.E.Ruiz, A.Cammi, L.Luzzi, *Dynamic stability of natural circulation loops for single phase fluids with internal heat generation*, Chemical Engineering Science126,573–583(2015), DOI https://doi.org/10.1016/j.ces.2014.12.050. Primary publisher metadata checked. Retrieved institutional11-page article-layout manuscript matches authors/title and accepted17December2014/online1January2015 information. The copy lacks visible journal printed-page labels: cite **PDF page and equation/section**, not an assumed573-based mapping. All main text, methods, results, nomenclature/references read; selected equations/Table1/critical result figures visually checked. No appendix present. No code, detailed mesh/time-step study or data supplement acquired; no complete journal/manuscript diff established.

The supplied layout has **no abstract/keyword block or journal pagination/header**. Sections1–5 and terminal references are present, but complete journal front matter and final-version equivalence are not certified. This is a version limitation, not evidence that the technical body is missing a section.

## Problem and original evidence

The authors ask how uniform volumetric heating changes the stability of a single-phase rectangular natural-circulation loop with a localized external heater and a constant-wall-temperature cooler. Their original contribution is a semianalytical linear stability formulation and nonlinear numerical comparison for two heater/cooler arrangements. Internally heated salt offers an MSR motivation, but the model does not solve reactor kinetics, spatial fission deposition or precursor transport.

The paper's claim that this was previously unstudied is a source-era novelty statement, **not a current gap**. It cites Keller/Welander (S54/S55), Vijayan (S09 and later comparisons), Ambrosini/Ferreri and early internal-source studies. Those references do not become independently read through S65. Later S66 and retrieved follow-up leads already challenge a generic wall/source/stability thesis claim.

## Geometry, conditions and available data

§§2.1,3–4/PDF2,6–10;Figure1,4–5,Table1: single closed constant-area circular tube arranged as a rectangle. Studied VHHC (vertical heater/horizontal cooler) and VHVC (both vertical) arrangements; Table1 common loop length7.24m, height2.20m, diameter0.0269m, heater0.73m, cooler0.80m. Remaining segment lengths are explicitly tabulated. No particular working fluid/property set is mapped to all points in the dimensionless stability diagrams; do not treat the plotted Re range as a realized molten-salt campaign.

Assumptions:1D cross-section means; incompressible Boussinesq density variation only in buoyancy; constant viscosity; one common regime around the loop; no fluid axial conduction; no wall thermal state; constant external heat flux on heater; uniform volumetric generation throughout the fluid **including cooler**; constant cooler wall temperature and exchange coefficient for perturbation analysis; other sections adiabatic except internal generation. These omissions differ materially from TRIDENT wall/insulation losses and source path.

Temperature is periodic around the circuit. Coordinate s starts at cooler entrance and follows the chosen circulation; v≥0 in the declared orientation. This formulation is not an audited signed-flow-through-zero/reversal solver. Mass flux G=ρ*v has kg/(m²s), not kg/s. No physical instrument, measured uncertainty distribution, calibration campaign or independent holdout exists in this work.

## Equations and checks

§2.1/PDF2,Eq1–4: uniform mass flux; momentum with pressure, gravity and Darcy friction; energy with advection and piecewise source/sink; ρ=ρ*[1−β(T−T*)]. The reported energy balance is

\[
\rho_*c_p\partial_tT+Gc_p\partial_sT=
\begin{cases}-h(P/A)(T-T_w)+q'''&\text{cooler},\\
q''P/A+q'''&\text{heater},\\q'''&\text{elsewhere}.\end{cases}
\]

P is wetted perimeter(m), A cross-sectional area(m²), q''W/m², q'''W/m³. Both sides W/m³. hW/(m²K); cpJ/(kgK). Distinguish prescribed Tw from prescribed coolant inlet/duty or a dynamic conjugate exchanger.

§2.1.1/PDF3,Eq5–8: Darcy f=a/Re^b, a=64^γ·0.316^(1−γ), b=γ+0.25(1−γ), γ=[1+exp((Re−2530)/120)]^−1. Low/high Re limits approach64/Re and0.316/Re^.25, but γ does not equal1 exactly at finite zero Re; the source uses an approximate low-Re limit. This is a smooth straight-tube-data transition, not a calibrated loop transition threshold. Do not infer that Re2530 is the observed transition of our facility.

§2.2/PDF3–4,Eq9–18: piecewise analytic steady temperature, periodicity, integrated buoyancy/loss balance and two source-associated geometric factors. Critical definitions are

\[
\Delta T_h=\frac{q''PL_h}{G_0c_pA},\quad
\Delta T_i=\frac{q'''(L_t-L_c)}{G_0c_p},\quad
\alpha=\frac{\Delta T_h}{\Delta T_h+\Delta T_i}.
\]

**Our interpretation check:** since ΔTi excludes generation inside the cooler, α as mathematically defined equals Qexternal/[Qexternal+q'''A(Lt−Lc)], not the fraction of **all** loop heating unless the cooler-source contribution is excluded from that denominator. The prose/nomenclature loosely calls it total-power fraction. Preserve the definitions; do not silently substitute a global fraction. α=1 removes internal generation; α=0 removes the external heater (nonzero remaining source assumed).

φ=hP/(G0cpA)=4Nu/(RePrD), with φLt the modified Stanton number (Eq11). The nomenclature on PDF10 prints St=Nu·Re/Pr, inconsistent with this relation and the conventional Nu/(RePr). This is a visually checked normalization flag, not an alternative to implement blindly.

Eq12/PDF4 puts f0 outside [Lt/D+ΣKj]. The paper describes Kj as local-loss factors without fully establishing equivalence to the conventional independent minor-loss coefficient convention. Reproduce its exact convention only after resolving this; do not replace usual [fLt/D+ΣK] with f[Lt/D+ΣK] unnoticed. In our own dimensional check, integrated loss and buoyancy both have pressure units; dimensional consistency alone does not settle the coefficient definition.

§2.2/PDF4–5,Eq19–31: small perturbations ∝exp(ωt), stability requires Re(ω)<0; dispersion relation solved on Re(ω)=0 using MATLAB trust-region-dogleg (§4/PDF7). Coefficients a,b and h are frozen in linearization (PDF4 footnote3). This is particularly consequential near transition: exact differentiation of a variable f would include their Re dependence. §2.3/PDF5,Eq32–34 nonlinear calculation retains a,b changes, MacCormack discretization/MATLAB, with initial small positive mass-flux perturbations (§4/PDF8). A numerical growth tolerance is invoked but a complete convergence/uncertainty study is not supplied.

## Results and limitations

- §4.1/PDF7–8,Figures6–9: external-heating limits reproduce earlier stability maps and linear/nonlinear calculations generally agree. This is verification/cross-method comparison, **not independent experimental validation**. The conclusion explicitly asks for future experimental validation.
- §4.1/PDF8–9,Figures10–11: lower α expands the unstable region in the studied VHHC dimensionless map. Re≈2500 produces linear/nonlinear differences due to frozen versus varying transition coefficients. Closure/linearization changes are a confounder near transition.
- §4.2/PDF9–10,Figures12–13: VHVC diagrams have smaller unstable regions and less growth with increasing internal-source share than the studied VHHC configuration. Geometry and source distribution both matter; no universal ranking for arbitrary loops follows.
- §4.2/PDF9: reduced thermal-barycenter separation can reduce the unstable region but also reduces driving head. Actual fluid-specific steady operating curves were **not placed on these maps**. Consequently, a larger unstable region in (Re,Stm) does not prove a particular physical reactor becomes unstable as power changes.
- §5/PDF10: cross-stream gradients, nonuniform power and fluid-property variations are acknowledged future issues. Uniform internal generation is an approximation, including for decay heat. It cannot establish liquid-fuel reactor safety or source-equivalent transient response by itself.

No posterior, input covariance, sensitivity-based uncertainty bounds, independently measured flow or validated instability onset is supplied. Wide formal map ranges do not certify closure validity at those extremes. No exact numerical boundary coordinates were digitized here.

## TRIDENT relevance and next evidence

**Direct model-class precedent:**1D conservation, source placement, buoyant-head/loss balance, local eigenvalue stability and closure sensitivity. **Conditional transfer:** compare actual source/cooler/geometry and thermal time scales; wall-heated and internally heated configurations need explicit equivalence assessment. **Incompatible claim:** matching heater power alone validates a liquid-fuel primary reactor transient. Without qualified flow/event evidence, keep reversal/instability an optional extension rather than the minimum dissertation endpoint.

For implementation, retain prescribed versus predicted h/Tw/duty, signed coordinate conventions, periodicity, mass flux versus mass flow, source-volume definitions, exact friction derivative and numerical convergence. A comparison across external/internal heating already exists; a thesis needs a more precise QoI-dependent adequacy or inferential result. S66 and available modern DYNASTY studies provide closer follow-up challenges.

## Stable claims

| ID | Claim | Locator | Qualification |
|---|---|---|---|
| S65-C01 | The model combines localized wall heating and uniform fluid heating | §2.1,PDF2,Eq1–4 | 1D constant-property/ideal cooler |
| S65-C02 | Source partition changes studied dimensionless stability regions | §4.1,PDF8–9,Fig10–11 | Not an operating reactor curve |
| S65-C03 | Heater/cooler geometry changes the stability comparison | §4.2,PDF9–10,Fig12–13 | Studied VHHC/VHVC only |
| S65-C04 | Linear analysis freezes transition-factor and h variations | PDF4,footnote3;PDF9,Fig11 | Particularly affects transition region |
| S65-C05 | Actual fluid-specific operating curves were not mapped | §4.2,PDF9 | Do not infer realized operating failure |
| S65-C06 | Cross-method agreement is not experimental validation | §4–5,PDF7–10 | Authors call for future experiments |
| S65-C07 | α mathematically uses internal generation outside cooler | Eq11,14,PDF3–4 | Our denominator clarification |
| S65-C08 | Stanton nomenclature conflicts with Eq11; local-loss convention needs care | PDF3–4,Eq11–12;PDF10,nomenclature | Not implementation-ready by transcription |

## Coverage checklist

| Section | PDF | Status |
|---|---|---|
| Introduction | 1–2 | Read/extracted; old novelty not adopted today |
| §2.1 equations/closures | 2–3 | Read/extracted; critical equations visually checked |
| §2.2 steady/linear methods | 3–5 | Read/extracted; Eq9–31 structure checked, not every geometric integral rederived |
| §2.3 nonlinear method | 5 | Read/extracted; numerical reproduction absent |
| §3 VHHC/VHVC integrals | 6–7 | Read/mapped; topology/Table1 inspected; full symbolic implementation deferred |
| §4 results/Fig6–13 | 7–10 | Read/extracted qualitatively; no curve digitization |
| §5,nomenclature | 10 | Read/extracted; normalization flag checked |
| References | 11 | Inspected as leads; originals not thereby read |
| External code/data/supplement | Outside copy | Not acquired; numerical settings/uncertainties not fully specified |
