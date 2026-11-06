# S16 Reis and Hassan 2025 SAM assessment

## Identity and synthesis readiness

Jadyn Reis and Yassin Hassan. *SAM Code Validation for High Prandtl Number Flow in Molten Salt Natural Circulation Facility*. Nuclear Technology 211(9), 2135–2144. DOI: https://doi.org/10.1080/00295450.2025.2480974.

Two supplied versions are now available: **J**, the newly supplied 11-page publisher PDF (one cover plus ten article pages), and **W**, the earlier 22-page publisher-HTML print. J printed page = J PDF page +2133 for J PDF 2–11; J PDF 1 is the cover. Both report first online 28 May 2025, which now has stronger direct support than the previously consulted ANS date of 7 August 2025. Detailed prose locators below retain **W page numbers** unless prefixed J; do not confuse these with journal pagination.

J includes readable Tables I–IV and Figures 1–4. The collapsed W tables are now resolved, not a current acquisition request. J Tables I–II: PDF 5/printed 2138; Tables III–IV: PDF 8/2141. J Eqs. (1)–(3): PDF 4/2137; Eq. (4): PDF 5/2138; property Eqs. (5)–(8): PDF 6/2139; Eq. (9): PDF 7/2140. J conclusions: PDF 10/2143; data/references through PDF 11/2144. Table pages and consequential equations visually inspected. These versions have the same article identity; no complete revision-by-revision redline is claimed. No separate supplement, case data or SAM input decks supplied.

**Ready:** input/observation-contract synthesis and reported-case quantitative appraisal. **Not ready:** independent reproduction, closure implementation without property-source checks, or fully uncertainty-qualified comparison. Full prose, recovered tables and relevant figures read.

## Problem, contribution and prior work

The paper tests a SAM 1-D natural-circulation model against four water and four HITEC operating conditions, each simulated with default and experimentally estimated friction: 16 calculations, eight experimental operating cases, not 16 independent experiments. Its original result is a conditional comparison of those friction treatments. It does not establish an autonomous prediction from electrical heater power and secondary cooling alone.

Introduction, PDF pp. 2–4, cites Ahmed/Scarlat/Hu’s DRACS benchmark, Lin’s FHR dissertation, SAM–CIET work S17, and a Minnesota-loop analysis. Their findings are cited background here, not originals independently read in this dossier. The central motivation is validation of closure-based system analysis for passive heat removal in high-Pr fluids. This facility is a separate-effects thermal-hydraulic experiment; it does not reproduce a fueled reactor, distributed fission heating or neutronic feedback.

## Facility, operating conditions and observations

Section II.A, pp. 4–6: four nominal 3 ft legs, nominal 1 in diameter; upper/lower legs inclined 20 degrees; transparent quartz section in the rising leg downstream of the main heater; expansion/melting pot. Do not substitute nominal diameter for the actual hydraulic ID. Three 1-in fiberglass layers around the main facility; transparent-section heater supplied enough power to suppress wall-cooling backflow. Ambient reported 22.8 °C. Heater inputs: water 58.8, 77.6, 93.0, 129.0 W; salt 232.2, 265.7, 297.5, 337.6 W. Those are supplied heater powers, distinct from model Q_net. Overall Pr range 2.96–54.29, pp. 4 and 16. Recovered case ranges are tabulated below from J Tables I–II.

Cooling-air settings are reported as 188 L/min for water and 37 L/min for salt, p. 6, despite being called “mass flow rate.” L/min is volumetric; do not convert to kg/s without reference temperature/pressure/density. Six K-type centerline probes, 11 wall locations, secondary inlet/outlet temperatures and dual-camera full-field/near-wall PIV. Probe centerline location is explicitly acknowledged as limiting radial-gradient capture. Area-weighted PIV velocity is the reported flow comparator; the axisymmetry/spatial reconstruction warrants checking in S37.

Section II.D, p. 8: heater meter specifications ±1% for 1–100 W and ±0.93% for 100–999 W; probe specification ±1.1 °C below 293 °C; stated temperature-difference uncertainty ±1.56 °C. The latter equals sqrt(2)×1.1 but is not by itself proof of independent errors or a specified confidence level. Maximum full-field/near-wall PIV percentages: water 1.80/1.67%, salt 2.33/1.65%. Source does not demonstrate a full joint input–output covariance budget or complete model-form uncertainty.

## Equation audit and implementation consequences

| Stable equation ID | Reported mathematics and locator | Definitions, checks and restriction |
|---|---|---|
| S16-E01 | τ_w = μ lim_(x→0) dU/dx; Eq. (1), p. 7 | x is distance from wall, U axial velocity, μ Pa·s. Units Pa. Sign depends on inward-wall coordinate and flow direction; use a stress magnitude consistently for positive friction. Local PIV shear is not a measured total-loop pressure drop. |
| S16-E02 | f_D = 8τ_w/(ρ U_∞²); Eq. (2), p. 7 | Dimensionless **Darcy**, not Fanning, friction; U_∞ defined as bulk velocity here. Requires correct cross-sectional averaging. Different conventions in other papers must be reconciled. |
| S16-E03 | Q_net = m_dot c_p ΔT; Eq. (3), p. 8 | W; ΔT is TP6−TP2, c_p at average loop temperature. Constant-c_p sensible-heat approximation; enthalpy difference is a possible analyst replacement, not the printed equation. Q_net inherits measured velocity/properties/temperature errors. |
| S16-E04 | Q_loss = Q_net − Q_HX; Eq. (4), p. 8 | W; source text also says Q_HX is calculated “using Eq. (4),” although Eq. (4) is the loss balance. Flag the apparent cross-reference problem. A difference of uncertain derived duties is not an independent loss measurement. |
| S16-E05–08 | μ=0.4737−2.30e−3 T+3.73e−6 T²−2.02e−9 T³; ρ=2293.6−0.7497 T; c_p=5806−10.83 T+7.24e−3 T²; k=0.78−1.25e−3 T+1.6e−6 T². Eqs. (5)–(8), p. 10 | Output units printed: Pa·s, kg/m³, J/(kg K), W/(m K). Visual transcription checked. S16 does not state T units/validity beside these equations; S38 Eqs4–7 explicitly use kelvin for the same coefficient family, providing cross-source convention support. Original property applicability/composition/ranges remain to be checked; S35 reports materially different modern property choices and contains its own main/appendix conflict. Coefficients are dimensional; do not implement from rounded prose alone. |
| S16-E09 | f_D=64/Re, Eq. (9), p. 12; stated SAM laminar regime Re<2200, p. 11 | Dimensionless, circular fully developed laminar reference. Combined with Darcy Δp=f_D(L/D)ρU²/2 gives 32μLU/D² (analyst dimensional/limiting-case check). Does not prove applicability of that limit to a developing buoyant profile. |

Section III, pp. 9–12: four 1-D legs, each ten elements; 0-D joints; expansion-tank branch and atmospheric pressure outlet. The entire rising leg is a single component; transparent local heater assumed to balance loss. Q_net is a volumetric source in the lower leg. Cooler is driven toward the measured minimum loop temperature using a very large wall-to-environment coefficient. Each joint uses K=1.8 based on a screwed-tee source, not a measured facility-specific loss. No supplied convergence study establishes ten elements as sufficient. SAM governing PDEs are delegated to a theory manual; no derivation of that manual was audited here.

## Results and critical assessment

Sections IV–V, pp. 12–17: authors report lower experimental friction than default SAM, improving predicted velocities. Conclusion states maximum salt velocity error decreased from 17.30% to 8.67%, p. 17. These numbers are verified **as statements in the prose**, also checked against the recovered J Tables III–IV below. Page 14 reports default-friction salt test 4 error 6.75%, and experimentally informed water errors from 0.53% to 16.57%. Temperature-difference accuracy does not improve uniformly: salt cases 1–3 worsen with experimental friction, while case 4 improves. Better flow matching is therefore not an unqualified improvement of all QoIs.

Important confounders: Q_net uses measured flow and ΔT; experimental friction uses PIV also used for flow comparison; measured minimum temperature is a boundary. These comparisons test conditional model consistency and a friction substitution, not a wholly independent forward prediction. No withheld operating set is documented in the supplied text. Centerline/wall-based approximation to bulk temperature is consequential but insufficiently specified to reproduce. Net-power treatment relocates spatial loss effects to a global/source correction; local buoyancy can change even if the total duty is correct. Water/salt operating conditions vary temperature, properties and velocity together; the reported trend with Pr is not an isolated causal Pr experiment.

## TRIDENT transfer and next sources

Direct methodological use: reproduce a prescribed-versus-predicted comparator table and list all reused measurements. Conditional physical transfer: single-phase buoyancy/friction and high-Pr thermal development, after checking ACU/VCU fluid, geometry and regime. Analogy: system-code V&V practice. Incompatible claims: an experimental PIV friction estimate is not available from sparse TRIDENT temperatures; it is not a 316L material property; nor is this a validated model of TRIDENT's actual secondary cooler.

Keep M2 prescribed-flow, M3 circulation-predicting and measured-primary-temperature wall diagnostics distinct. Implement no new fitted loss/heat-transfer coefficient from these prose summaries. A useful experiment would independently constrain primary flow/pressure loss or secondary duty, subject to available instrumentation and approved protocols—not assume PIV or add instruments by fiat.

Acquire: SAM Theory Manual DOI 10.2172/1781819 for governing equations/closure definitions; S37 (supplied) for averaging, PIV/thermal data; original property reports for T units/ranges. Raw case data and SAM input decks would permit independent reproduction; they were not supplied.

## Coverage checklist

| Section/material | Relevance | Status | Reason/limit |
|---|---|---|---|
| Identity/abstract/I, pp. 1–4 | Motivation and comparator context | Read/extracted | Citation trails are leads, not independently verified originals. |
| II.A–D, pp. 4–8 | Facility, measurements, duty and UQ | Read/extracted | Case tables recovered in J; W had collapsed links. |
| III, pp. 9–12 | Inputs, discretization, properties, closures | Read/extracted; Eqs. 1–9 visually checked where consequential | Kelvin supported by S38; original property validity/range still unresolved. |
| IV–V, pp. 12–17 | Baselines, results, limitations | Read/extracted | Reported numerical results checked against recovered J tables; no raw-data reproduction. |
| Tables I–IV, J PDF 5,8/2138,2141 | Essential quantitative case data | Read/extracted and visually checked | Recovered from newly supplied J; W alone had collapsed links. |
| Figures 1–4 | Geometry and qualitative temperature comparison | Inspected; no digitization | Small plots; exact graphical coordinates not extracted. |
| Data availability/funding/references, pp. 18–21 | Acquisition/provenance | Read; relevant leads extracted | Underlying datasets not supplied. |
| Web navigation/footer, pp. 21–22 | No scientific content | Skipped after identification | Not article evidence. |
| Separate supplement/input decks | Reproducibility | Not supplied; not audited | Does not imply none exist. |

## Stable claim-to-evidence table

| Claim ID | Claim | Locator | Provenance and limit |
|---|---|---|---|
| S16-C01 | Eight experimental conditions are each simulated with two friction treatments. | IV p. 12; V pp. 16–17 | Author study design; do not call them 16 independent experiments. |
| S16-C02 | Q_net and measured minimum temperature are prescribed model inputs. | II.C Eq. 3 p. 8; III p. 11 | Original method; conditional prediction contract. |
| S16-C03 | Experimental friction and velocity assessment share PIV information. | II.C pp. 6–7; IV p. 13 | Original method plus dependence inference; no held-out independence established. |
| S16-C04 | Maximum salt velocity errors are reported as 17.30% default and 8.67% experimental friction. | W V p. 17; J Tables III–IV, PDF8/2141 | Author numerical summary checked against recovered tables; rounding prevents exact reconstruction of every percentage. |
| S16-C05 | Centerline temperature measurements limit high-Pr radial-gradient capture. | II.B p. 6; IV p. 13 | Author measurement limitation; not quantified TRIDENT error. |
| S16-C06 | Tables I–IV omitted from W are present in J and expose differing temperature-difference columns. | W PDF pp. 7,13–14; J PDF 5,8/2138,2141 | Version-specific completeness finding, gap resolved. |

## Recovered journal-table audit

All numbers below transcribed from the visually inspected J table pages. Ranges are analyst minima/maxima, not new experimental claims.

| Quantity | Water cases 1–4 | Salt cases 1–4 | Locator |
|---|---|---|---|
| Pr | 4.23, 3.78, 3.50, 2.96 | 54.29, 50.81, 41.65, 31.74 | J Tables I–II, PDF 5/2138 |
| Re_D | 711.8–1806.2 | 74.9–158.9 | Same |
| Experimental Darcy f | 0.064, 0.052, 0.048, 0.040 | 0.612, 0.648, 0.456, 0.352 | Same |
| Q_net (W) | 44.50–105.24 | 189.26–253.55 | Same |
| Q_HX (W) | 26.86–58.06 | 55.58–65.98 | Same |
| Q_loss (W) | 17.64–47.20 | 133.68–187.57 | Same; Q_net−Q_HX checks to displayed precision |
| Velocity (m/s) | 0.0190–0.0350 | 0.0185–0.0237 | Same |
| ΔT in Tables I–II (K or °C difference) | 1.29, 1.43, 1.54, 1.67 | 11.16, 10.09, 7.95, 5.63 | Same |
| ΔT_exp in Tables III–IV | 1.20, 1.24, 1.28, 1.56 | 7.81, 7.64, 6.23, 4.32 | J PDF 8/2141; **different from Tables I–II** |

The text describes approximating bulk temperature from centerline and wall temperatures (W p. 13; J p. 7/2140), but gives no explicit transformation that reconciles these two ΔT sets. Preserve both. Do not silently swap the assessment ΔT into the Q_net calculation or assume either set is an independently measured bulk difference.

Salt velocity errors, case order 1–4, J Tables III–IV: default 17.30, 15.82, 7.80, 6.75%; experimental friction 4.32, 8.67, −0.98, 1.69%. Signed convention is consistent with 100×(experiment−simulation)/experiment to rounding. Recomputing from rounded table velocities can differ slightly from printed percentages. For salt case 1, temperature-difference error worsens from 37.53% to 45.98%, despite velocity improvement. Water case 4 velocity error also slightly worsens, 16.29% to 16.57%; a universal all-case improvement claim would be false.

The stated ΔT uncertainty ±1.56 °C is comparable to the water driving differences themselves. Agreement within these intervals cannot, without a defined statistical test and covariance model, establish strong discriminatory validation of thermal physics. No numerical mesh-convergence, closure-parameter posterior or jointly propagated input/assessment covariance is supplied.

| Claim ID | Claim | Locator | Type/limit |
|---|---|---|---|
| S16-C07 | The two table groups use different experimental ΔT values without an explicit reproducible transformation. | J Tables I–IV, PDF 5,8/2138,2141; IV PDF 7/2140 | Direct table comparison; possible bulk-observation correction, not silently resolved. |
| S16-C08 | Experimental friction improves salt velocity comparisons but does not uniformly improve temperature differences or every water velocity case. | J Tables III–IV, PDF 8/2141 | Original reported results, arithmetic/interpretation checked. |
