# S21 Carson and colleagues 2026 local heating

## Identity, completeness and readiness

Thomas Carson, Hansol Kim, Joseph Seo, Theodore Kupper, Cole Gentry, Kevin Clarno and Yassin Hassan. *Experimental flow visualization and thermal-hydraulic characterization of local heating effects in a molten salt natural circulation loop*. Nuclear Engineering and Design 459 (2026), 115179. DOI https://doi.org/10.1016/j.nucengdes.2026.115179. Full journal article: 13 pages, PDF=printed article page. First page verifies accepted 24 August and **available online 11 September 2026**, resolving the previous online-date uncertainty; assigned issue date and online date are distinct.

All sections, Tables 1–4, figures/captions and references read. Eqs. (6)–(23) and Table 4 visually checked on rendered pp. 6–7,11. No separate supplement/raw PIV, uncertainty code or heater logs supplied. Data statement p. 13: on request. Figures readable for qualitative comparison; no digitized curve data admitted.

**Ready:** qualitative local-heating/measurement-limit synthesis and critique of reported dimensionless/heat-balance calculations. **Not ready:** quantitative recirculation-extent closure, independently validated heat-transfer coefficient or adoption of the printed uncertainty implementation.

## Problem, contribution and evidence boundaries

Three local test-section heating conditions are compared with full-field/near-wall PIV and loop temperatures. This is original transient/local-heating evidence in a non-nuclear HITEC loop, not a demonstrated reactor-safety margin or a new validated reduced closure. Prior work includes S37's steady PIV, S16/S17 system-code assessment, FLiBe experiments, DYNASTY distributed-heating studies and classic scaling. Those citations are leads, not originals independently read through this article. Its introductory statements about licensing standards are background; no regulatory compliance determination is made here.

The paper explicitly limits HITEC-to-fluoride transfer primarily to high-Pr thermal-hydraulic behavior (§2.1, pp. 2–3), not matching all properties or chemistry. That is a useful motivation precedent: an experiment can isolate a mechanism without being a one-to-one reactor surrogate. No natural-circulation origin chronology is established by this recent paper.

## Configuration, protocol and observations

§2/Figs. 1–3, pp. 2–4: HITEC NaNO₃/NaNO₂/KNO₃ 7/49/44 mol%, low-melting surrogate; nominal ID 0.0254 m, legs 0.915 m; quartz section 0.186 m with transparent electrical heater; air counterflow jacket nominal 0.051 m ID, 0.305 m length. Ceramic-fiber insulation is reported here, whereas S37 reports fiberglass: retain a facility/version difference, not a universal insulation assignment. Six centerline K-type probes and eleven clamped wall probes; secondary inlet/outlet T and volumetric airflow; 50-Hz DAQ. “Bulk” labels in the paper do not turn centerline probes into mixed-cup temperatures.

Initial main heating about 450 W, test section 50 W, secondary flow stated 37 L/min. The other printed conversion “7.993×10³ m³/h (37 L/min)” (§2.3 p. 3) is inconsistent: analyst conversion is 2.22 m³/h. Clarify operating log/units before reuse. After approximately 18 h operation, a local heater failure produced the heat-loss condition; after recovery to 50 W a PIV measurement occurred about 97 min later; at about 100 W measurement followed about 20 min later. Heater integrity limited the final duration. “Adiabatic” means estimated replacement of about 50 W heat loss, not a measured zero local flux.

The results explicitly state the measurements had not reached steady state (§4.3 p. 10; §5 p. 12). Three conditions vary local heat, global temperature, viscosity, time since perturbation and prior history together; this is not an isolated causal Pr sweep or a repeatability-qualified thermal-equilibrium comparison.

PIV: simultaneous center-plane views, full-field 250 fps/512×800 and near-wall 1000 fps/1024², 1-mm sheet, PRANA multi-pass/outlier handling, <5% rejected vectors; Table 1 p. 6 lists windows/overlaps. The current manuscript calls laser wavelength 542 nm versus 532 nm in S37; acquisition details should come from the applicable experiment record, not merged into one generic setup.

## Equation and convention audit

| Equation ID | Reported relation and locator | Verification and restriction |
|---|---|---|
| S21-E01 | St_p=ρ_p d_p² U/(18μL), Eqs. (1)–(4), p. 5 | Dimensionless Stokes-response estimate under Stokes drag; not a general guarantee of negligible settling, optical bias or cross-sectional representativeness. Fig. 4 property/velocity uncertainty bands not independently recomputed. |
| S21-E02 | U_mag=sqrt(U²+V²); ΔA_i=π(r_i²−r_(i−1)²); trapezoid U_i and annular weighted mean; Eqs. (5)–(8), pp. 5–6 | Units m/s and m². Uses one radial half-profile revolved under axisymmetry. Observed asymmetric profiles challenge that assumption. For mass/enthalpy transport the required quantity is signed axial flux, not positive speed magnitude. |
| S21-E03 | U_PIV=U_PIV,half (ID_g/ID_ss)², Eq. (9), p. 6 | Valid as a same-density mass-conservation conversion between different circular areas **if** the reconstructed mean is valid. Annular integration from 0 to R already spans full area; this is not an extra factor-of-two correction for “half” a diameter. Both IDs and uncertainty need qualification. |
| S21-E04 | Q_air=m_dot_air c_p,air(T_c,out−T_c,in); Q_max=C_min(T_h,in−T_c,in); ε=Q_air/Q_max; LMTD=(ΔT₁−ΔT₂)/ln(ΔT₁/ΔT₂). Eqs. (10)–(16), p. 6 | W, W/K, dimensionless and K. For equal positive terminal differences LMTD tends to that difference; near-equality requires stable numerical evaluation. Endpoint crossing or transient storage invalidates a simple steady exchanger interpretation. C_min may switch side. Actual salt bulk states and flow are uncertain. |
| S21-E05 | U=(Δp_U/Δt)M; V similarly; Eqs. (17–18), p. 7 | Rendered PDF shows M multiplying the fraction, with M m/pixel: dimensions correct. Text extraction can make placement look ambiguous; do not “correct” it from extracted text alone. |
| S21-E06 | Component RSS propagation, Eq. (19), p. 7 | As printed, coefficients do not correspond to derivatives of U=MΔp/Δt under the stated absolute σ_M,σ_p definitions. In particular calibration term uses U_i²σ_M². Correct analyst Jacobian coefficients are Δp/Δt, M/Δt and −MΔp/Δt², plus covariance if present. Relative versus absolute σ conventions/code must be reconciled before using reported uncertainty. |
| S21-E07 | σ_speed RSS with U/U_mag,V/U_mag; annular average Eq. (21); ΔT uncertainty sqrt(2)σ_T; property σ_f²=(f′σ_T)²+(s_f f)². Eqs. (20–23), p. 7 | Speed formula dimensionally consistent under independent components. Shared magnification/wall-position/property/sensor calibration creates covariance; annuli cannot all average down common error. sqrt(2) assumes equal independent temperature errors. Property derivative requires stated T convention and correlation range. |
| S21-E08 | Q_net=m_dot_s c_p,s(T_h,in−T_h,out), Q_loss,meas=Q_t−Q_net; Q_HX,air from air enthalpy rise. Eqs. (24–26), p. 8 | As stated, Q_net uses TB6−TB1, but nearby discussion says TB6 and TB2; source mapping inconsistent. Both derived duties reuse observations. During these non-steady tests Q_t−Q_salt is not proven ambient loss: unmodeled storage matters. |
| S21-E09 | Re=ρUD/μ; Pr=μc_p/k; Gr=gβ(T_w−T_b)L³/ν²; Nu=hD/k; estimate Nu=0.664 Re^0.5 Pr^0.33; Ra=GrPr; St=Nu/(RePr). Eqs. (27–33), pp. 9–10 | Dimensionless if ν is m²/s (text's m³/s is a unit error). Gr length is not necessarily Re diameter; exact “global/local” conventions must be fixed before cross-paper comparison. Flat-plate estimate is an analogy/assumed closure, not independently measured loop h. High Gr/Ra alone does not prove turbulence or quantify recirculation; low St does not imply a thick thermal layer relative to momentum at high Pr. |

## Results, baselines and UQ

Table 2 p. 7 adopts property uncertainties ρ 2%, μ 16%, c_p 5%, k 5%, attributed to INL. These are cited database assumptions, not fresh measurements. Reported mean velocity-magnitude uncertainty is 4.02%,1.97%,1.29%; bulk-velocity uncertainty 0.55%,0.22%,0.16% for loss/adiabatic/heating. Given Eq. (19) and common-error assumptions, these are **reported**, not independently verified total accuracy.

Table 3 p. 8: calculated residual system loss 76.3,190.1,156.5 W versus air duty 100.2,100.9,99.7 W. Different physical terms need not equal one another, and transient storage plus centerline sampling can affect them. Their disagreement alone does not identify a specific thermal-structure mechanism or violate conservation.

Table 4 p. 11: global/local Re 136/112,289/238,455/374; Pr 18.4/17.6,17.8/16.9,16.9/16.2. Global Gr 3.676e9,3.273e9,4.512e9; global Nu 20.3,29.2,36.0; global St 8.1e−3,5.7e−3,4.7e−3. The Nu are based on the adopted correlation, not independent evidence that heat-transfer performance increased. Table arithmetic Nu/(RePr) and Gr×Pr is approximately consistent with St/Ra to rounding. No new best-fit heat-transfer model is validated.

Full-field Figs. 11–12/§4.3 pp. 10–11 show asymmetric profiles with peaks of approximately 0.03,0.055,0.07 m/s as local power rises. These are maxima, not area means or net circulation. Near-wall Fig. 13 pp. 11–12 does **not** fully collapse to U+=x+; authors acknowledge finite-resolution/viscosity/position limits and that the thermal layer was not directly measured. No quantitative recirculation length, reversed-flow volume or independently validated heat-transfer effect of a recirculation zone is established. No CFD experiment or held-out ROM calibration appears in this paper.

## TRIDENT use and skeptical appraisal

Direct use: observation definitions, conditional local-heating comparison and evidence needed before interpreting sparse temperatures as bulk states. Conditional transfer: qualitative sensitivity of high-Pr buoyant flow to local wall conditions, only after fluid/geometry/BC checks. Analogy: PIV strategies that TRIDENT does not currently possess. Incompatible: replacing VCU sparse sensors with this paper's PIV-derived flow, calling a peak speed a circulation measurement, or using an estimated Nu as an independently observed closure target.

A better-supported H03 would initially target observable thermal consequences or bounds, not promised recirculation extent. Retain spatial heating/cooling, solid storage and observation operators in model comparisons. Claims that insulation makes axial wall conduction negligible need a scale/energy comparison; radial insulation alone is not such a proof. Claims that Pr reduction establishes increasing thermal diffusivity also require ν and α separately, not only their ratio. No code changes are authorized by these observations; unresolved formulas are implementation gates.

Acquire raw PIV/uncertainty post-processing and synchronized power/air/temperature logs if quantitative reuse is desired. New literature priorities: DYNASTY's distributed source experiments/CFD–LES and Romie–Kinyon 1958 for the historical natural-convection MSR tradeoff; S37 and S39 are already supplied and should not be requested again.

## Coverage

| Material | Status | Limit |
|---|---|---|
| §§1.1–1.4, pp. 1–2 | Read/extracted | Regulatory/history citations distinguished from originals. |
| §§2.1–2.3, pp. 2–5 | Read/extracted | Source/geometry/protocol; airflow conversion inconsistency retained. |
| §§3.1–3.2, pp. 5–6 | Read/extracted; key equations visually checked | Averaging/axisymmetry and HX assumptions remain conditional. |
| §4.1, pp. 6–7 | Read/extracted | Eq. 19/Jacobian and covariance issues; code unavailable. |
| §§4.2–4.3, pp. 7–12 | Read/extracted | Thermal analysis, nondimensional results and PIV; no numerical figure digitization. |
| §5, p. 12 | Read/extracted critically | Thermal-layer/near-wall limits retained. |
| Tables 1–4/Figs. 1–13 | Present; inspected; relevant numerical tables extracted | Not raw-data reanalysis or uncertainty reproduction. |
| Data/references, p. 13 | Read for leads | Supplement/raw datasets not supplied. |

## Claim ledger

| Claim ID | Claim | Locator | Type/limit |
|---|---|---|---|
| S21-C01 | HITEC is used for high-Pr mechanism similarity, not one-to-one fluoride-salt performance. | §2.1 pp. 2–3 | Authors' explicit transfer restriction. |
| S21-C02 | Three local heating measurements are transient and have different time/history conditions. | §2.3 pp. 3,5; §4.3 p. 10; §5 p. 12 | Original protocol; not independent steady Pr sweep. |
| S21-C03 | Profiles are asymmetric and near-wall scaling is resolution-limited; thermal boundary layer was not measured. | Figs. 11–13/§4.3 pp. 10–12 | Direct velocity evidence plus author limitation. |
| S21-C04 | Bulk-flow estimation assumes revolving a half-profile and uses speed magnitude. | Eqs. 5–9, pp. 5–6 | Original analysis; not guaranteed true signed flux. |
| S21-C05 | Reported Nu is estimated from a flat-plate-type correlation. | Eqs. 30–31 pp. 9–10; Table 4 p. 11 | Closure-derived quantity; not independent experimental closure validation. |
| S21-C06 | Eq. 19 and heat-balance interpretations need reconciliation before implementation. | Eqs. 19,24–26 pp. 7–8 | Analyst dimensional/measurement audit; no claim experimental dataset itself is invalid. |
