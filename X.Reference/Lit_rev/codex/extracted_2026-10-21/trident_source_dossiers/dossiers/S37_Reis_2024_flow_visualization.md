# S37 Reis Seo Hassan 2024 steady flow visualization

## Identity, file and readiness

Jadyn Reis, Joseph Seo and Yassin Hassan (2024), *Molten salt flow visualization to characterize boundary layer behavior and heat transfer in a natural circulation loop*, Physics of Fluids 36, 033605. DOI https://doi.org/10.1063/5.0197276. Published 6 March 2024. Supplied 22-page PDF includes an AIP cover: PDF 2–22 correspond to printed 033605-1 through -21; cover PDF 1 has no article page. All sections, Tables I–VIII and references read; key equations/tables visually inspected on PDF 10–11,19,21. Full-field/near-wall figure sequences inspected qualitatively; no plot digitization. No separate raw PIV/supplement supplied; data on request.

**Ready:** observation/closure-selection critique and qualitative high-Pr mechanism motivation. **Not ready:** direct implementation of selected “best” correlations, reproducing uncertainty numbers or assuming an independently measured local temperature field.

## Problem, original contribution and data relationship

Original work: design of an optically accessible HITEC natural-circulation loop with a transparent heated quartz section, four salt and four water states, dual-view PIV and temperature-derived heat-transfer/friction assessment. Prior work includes Headley's FLiNaK PIV dissertation, historical molten-salt natural-convection concepts, Britsch's FLiBe loop, CIET and prior nitrate loops. These originals remain separate reading leads. This study does not demonstrate that all high-Pr correlations fail, or establish one universally superior closure.

The eight operating states and friction data recur in S16. Treat them as an **evidence family**, not sixteen independent experiments or independent cross-publication validation. For example, S37 Fanning salt friction 0.153,0.162,0.114,0.088 becomes S16 Darcy 0.612,0.648,0.456,0.352 by exactly ×4. This convention check is valuable, but not new validation.

Motivation extends beyond MSRs to solar thermal transport/storage (§I, PDF 2–3/printed -1–2). Reactor use is passive decay-heat removal/closure validation, not a claim the facility duplicates a fueled reactor. HITEC is chosen for lower-temperature high-Pr accessibility and a controllable energy balance; composition/chemistry and volumetric heating are not thereby similar to an actual fuel salt.

## Facility, properties and metrology

§III, PDF 4,6–8/printed -3,-5–7: 316 steel four-leg loop, nominal legs 0.9144 m, ±20-degree horizontal-leg inclinations; air jacket 0.305 m×0.051 m; 0.186-m quartz section; three layers fiberglass; atmosphere-connected melting/expansion tank; six centerline salt/water probes, eleven wall sites, secondary temperatures/flow and test-section infrared check. Diameter is reported approximately 0.025 m in §III but 0.0266 m in conclusion; qualify exact ID from configuration records, not convenient rounding. Quartz/steel changes matter for velocity rescaling.

HITEC 7/49/44 mol% NaNO₃/NaNO₂/KNO₃, 5 kg from ≥99% assay components. Properties Eqs. (1–4), PDF 4/-3 match S16/S38 polynomials; T in K is explicit in S38, while this source's adjacent text omits its unit. Original temperature/range/property uncertainty still requires the INL/Santini originals, not extrapolation to ambient glycol conditions.

§IV.A, PDF 8/-7: water heater powers 58.8–129.0 W and secondary 188 L/min; salt 232.2–337.6 W and 37 L/min. Transparent salt heater 37 W is chosen to approach zero **probe** ΔT and suppress near-wall backflow; it is not proven adiabatic by a resolved heat ledger. Twenty-four-hour intervals used before steady PIV. Full field 6000 images at 250 fps/512×800; near wall 8000 at 1000 fps/1024². PRANA multi-pass/UOD (<5% interpolated) and radial optical calibration at operating temperature using a 2.794e−4-m mesh. Tracer diameter 50 μm, density 700 kg/m³; reported Stokes numbers <3.12e−4. Optical/particle quality checks do not establish cross-sectional completeness.

Table VI, PDF 14/-13: global Pr salt 54.29→31.74, water 4.23→2.96; diameter Re salt 74.86→158.92 and water 711.78→1806.52. Global Re uses a different length and must not be called a pipe-transition criterion. Global length is heater–cooler distance; local length D and properties at film temperature (Eqs. 7–12, PDF 9–10/-8–9). The global centerline ΔT salt 11.16→5.63 K and water 1.29→1.67 K differ in observation meaning from an actual mixed-cup enthalpy rise.

## Equations, averaging and UQ audit

| Equation ID | Reported relation/locator | Check and restriction |
|---|---|---|
| S37-E01 | St_p=d_p²ρ_pU/(18μD_h); U_i=αΔx_i/Δt; Eqs. (5–6), PDF 7–8/-6–7 | Dimensionless tracer response; velocity m/s. Shared optical/time calibration must not average down as independent vector noise. |
| S37-E02 | Pr=μc_p/k, Re=ρUL/μ, Gr=gβΔTL³/ν², Ri=Gr/Re², Ra=GrPr; Eqs. (7–12), PDF 9–10/-8–9 | Dimensional checks pass with ν m²/s. Global/local temperature and length definitions differ. Comparing Gr/Ri across papers requires reconstructing both scales. |
| S37-E03 | τ_w=μlim_(x→0)dU/dx; f_F=2τ_w/(ρU_b²); u_τ=sqrt(τ_w/ρ); U+=U/u_τ, X+=Xu_τ/ν. Eqs. (13–17), PDF 10/-9 | **Fanning**, so Darcy=4f_F. Stress based on linear near-wall fit, with a 20% departure threshold selected iteratively. Wall positions adjusted differently among cases. U+=X+ using stress inferred from the same near-wall gradient is partly a consistency check, not independent validation of τ_w. |
| S37-E04 | Q_loss=Q_h−Q_net; Q_net=m_dot c_p(TP6−TP2); h=Q_net/[A_s(T_w−T_b)]; Nu=hD/k. Eqs. (18–21), PDF 10/-9 | W, W/(m²K), dimensionless. T_b along heater is linearly reconstructed from two endpoint probes into 20 points; wall T from three probes. These are inferred spatial temperatures, not 20 measurements or direct radial thermal-field evidence. Distributed duty/loss and wall-vs-fluid temperature assumptions enter effective h. |
| S37-E05 | Component uncertainty Jacobian Eq. (22); magnitude Eq. (23); averaging Eq. (24), PDF 11/-10 | Eq. 22 dimensionally consistent under independent inputs. **Eq. 23 has same missing square-root denominator issue as S38 Eq. 3**, visually verified. Averaging common systematic calibration as independent errors is not justified. |
| S37-E06 | Power uncertainty Eq. (25), PDF 11/-10 | Printed relative RSS multiplied by Q_net is not the standard subtraction variance for Q_net=Q_h−Q_loss. Analyst formula is Var(Q_net)=Var(Q_h)+Var(Q_loss)−2Cov(Q_h,Q_loss). Q_loss itself derives from Q_net here, so the primitive measurement graph must be reconstructed before assigning either independent uncertainty. |
| S37-E07 | h uncertainty Eq. (26), PDF 11/-10 | Printed derivative for ΔT uses −Q_net/(A_sΔT) rather than −Q_net/(A_sΔT²). Units fail for that term as written. Analyst derivative is −h/ΔT; not a silently corrected author equation. |
| S37-E08 | τ_w uncertainty Eq. (27), PDF 12/-11 | Displays viscosity term only; gradient/wall-position uncertainty not fully represented in that equation. Quoted μ uncertainty 16% and maximum salt f uncertainty 2.08% require clarification of omitted terms/covariance/conventions before trusting total uncertainty. |

Table V, PDF 11/-10: ρ 2%, c_p 5%, μ 16%, k 5% property uncertainty; 20% assumed heat-loss-calibration uncertainty. Reported maxima: water h 58.6%/Nu 58.9%; salt h 21.8%/Nu 22.4%. Bulk-velocity uncertainty water 0.38%,salt 0.28%; full-field/near-wall PIV salt 2.33/1.65%, water 1.80/1.67%. These are source-reported results with the printed-formula caveats above, not independently recomputed accuracy. Thermocouples 1.1 °C, ΔT 1.56 °C; water ΔT is of similar magnitude, limiting discrimination.

## Results, comparison and skepticism

§V.B–C/Figs. 8–18, PDF 12–18/-11–17: centerline salt temperatures respond downstream of external heating/cooling, unlike lower-Pr water; salt has off-center/double velocity peaks while water is closer to parabolic, with entrance/bend effects at higher velocity. PIV observes velocity, not the claimed radial thermal boundary-layer profile. The thermal-development explanation is supported by coupled qualitative evidence, but source strength is less than direct cross-sectional thermometry. Pr, viscosity, mean temperature and velocity covary; “Pr matters more than ΔT” is an interpretation of this experiment, not a causally isolated universal law.

Table VII PDF 19/-18: Fanning friction salt 0.153,0.162,0.114,0.088; water 0.016,0.013,0.012,0.010. Table VIII PDF 21/-20: minimum local Nu salt 4.57–5.13, water 4.26–5.31; mean Nu salt 6.76–7.53, water 8.69–11.02. Those are reconstructed from the heat ledger and interpolated temperatures, not independent direct h measurements.

§V.D–E, PDF 16,18–19/-15,-17–18 compare many correlations. Flat-plate-type friction is reported within about 20% for salt, and local Nu≈4.36/Sieder–Tate agreement is reported. This is a post hoc ranking on the same limited states, no withheld regimes or predictive intervals. Table II even lists a Re range 800–2.2e5 for the printed 0.027Re^0.8-type Sieder–Tate expression, while salt Re_D≈75–159: apparent accuracy outside the listed range does not validate transfer. Calling this a general laminar closure would be misleading. Flat-plate characteristic length and imposed boundary conditions also differ from an internal developing buoyant pipe. Read original correlation sources before implementing; some table/bibliography descriptors require correction/verification (e.g. the cited Sellars entry is a discussion, not the original full derivation).

## TRIDENT implications and coverage

Direct: distinguish centerline sensors, wall-contact sensors, derived h and true bulk observations; preserve Darcy/Fanning conventions and dependent data families. Conditional: high-Pr development and bend-induced redistribution merit tests in the actual property/geometry range. Analogy: optical measurements are a richer reference, not instruments TRIDENT is assumed to have. Incompatible: identifying local recirculation from scalar flow or treating fitted h/f as intrinsic material properties.

For M1–M3 comparisons, expose observation operators and independently held-out thermal targets. Sparse endpoints do not justify a unique 20-point fluid profile; profile uncertainty must survive into closure assessment. For CFD, compare the same measured plane/sensor observable and acknowledge reconstructed bulk-flow assumptions. H01/H03 must offer more than noticing this already reported observation mismatch.

| Material | Status | Relevance/limit |
|---|---|---|
| I–II, PDF 2–4/-1–3 | Read/extracted | Motivation/prior work/correlation catalogue; originals not assumed read. |
| III, PDF 4,6–8/-3,-5–7 | Read/extracted | Apparatus, properties, instrumentation/PIV; diameter inconsistency retained. |
| IV.A–E, PDF 8–10/-7–9 | Read/extracted | Protocol, calibration, non-dimensional definitions and derived coefficients. |
| V.A, PDF 11–12/-10–11 | Read/extracted; equations visually checked | Printed UQ issues; code/raw measurements unavailable. |
| V.B–E, PDF 12–19/-11–18 | Read/extracted | Profiles, regimes, friction/Nu comparisons; no numerical plot digitization. |
| VI, PDF 19,21/-18,-20 | Read/extracted critically | Qualified scope; no novel universal closure admitted. |
| Tables I–VIII/Figs. 1–22 | Present; relevant tables/plots inspected | Catalogue equations are not all implementation-ready; boundary/range checks pending originals. |
| References, PDF 21–22/-20–21 | Read for leads | No separate supplement/raw dataset supplied. |

Next acquire: Romie–Kinyon 1958, Headley FLiNaK dissertation, Britsch FLiBe loop, Shin high-Pr near-wall loop experiment, original internal-generation study and original property/correlation sources. S16 and S21 are already supplied; their overlapping data do not add independent repetition.

## Claim ledger

| Claim ID | Claim | Locator | Type/limit |
|---|---|---|---|
| S37-C01 | The work supplies eight water/HITEC steady PIV operating states and reconstructed thermal/friction results. | IV.A p. 8/-7; V, Tables VI–VIII | Original dataset, reused by S16. |
| S37-C02 | f is Fanning here and converts to S16 Darcy by ×4. | Eq. 14 PDF 10/-9; Table VII PDF 19/-18; S16 Tables I–II | Original convention plus analyst cross-source arithmetic. |
| S37-C03 | Local heater temperatures/h are reconstructed from sparse probes and a global power balance. | IV.E Eqs. 18–21, PDF 10/-9 | Original method, not resolved local temperature measurements. |
| S37-C04 | Salt off-center peaks and delayed centerline-temperature response motivate observation-aware reduction. | V.B–C/Figs. 8,11–12; PDF 12,14–15/-11,-13–14 | Original velocity/temperature evidence; thermal profile mechanism partly inferred. |
| S37-C05 | Reported uncertainty formulas contain dimensional/propagation issues requiring code-level reconciliation. | Eqs. 23,25–27, PDF 11–12/-10–11 | Analyst audit, not a declaration that measurements are unusable. |
| S37-C06 | Apparent correlation agreement does not establish validity outside its cited geometry/regime. | Table II PDF 5–6/-4–5; V.D–E PDF 16,18–19/-15,-17–18 | Analyst applicability appraisal. |
