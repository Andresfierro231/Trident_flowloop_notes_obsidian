# S43 — Britsch et al. (2019): natural circulation FLiBe loop

Extraction date: 2026-10-20. Purpose: history/motivation, observation limits, closures, and experimental design. **Ready for these scoped syntheses; not ready to reproduce the heat-transfer reduction.**

## Identity and coverage

Karl Britsch, Mark Anderson, Paul Brooks, Kumar Sridharan, “Natural circulation FLiBe loop overview,” *International Journal of Heat and Mass Transfer* **134**, 970–983. DOI: [10.1016/j.ijheatmasstransfer.2018.12.180](https://doi.org/10.1016/j.ijheatmasstransfer.2018.12.180). Journal article, available online 29 January 2019. Both uploaded copies contain 14 pages with identical extracted page text; they are one source. Printed page = PDF page + 969. Main text, Appendix A and references are present. Appendix B is a separately linked supplement and is absent from the uploaded article. Equations and selected tables were visually checked at PDF 4, 5 and 9; remaining figures were inspected through their text/captions, without digitization.

## What the work establishes

The authors describe a working UW FLiBe facility, observed thermal behavior, estimated circulation speeds, and heat-transfer trends. Their historical account describes earlier ORNL salt loops as corrosion/mass-transfer testbeds: temperature gradients and long exposures motivated inexpensive, reliable natural circulation. That cited history is not independent reading of every ORNL original (PDF 1–3/970–972, §1).

The modern purposes include high-temperature natural circulation, thermal gradients, freezing and code/benchmark development. A nonfueled salt loop is relevant to these mechanisms; it does not reproduce reactor neutronics, fuel chemistry or a full passive heat-removal system. The paper distinguishes ARE/MSRE systems from natural-circulation heat-transfer loops. Its 7.5 versus 10 MW MSRE account concerns attainable power, not a measured 25% heat-balance closure error. For the latter, use the original S47, not this narrative.

## Facility, conditions and observations

| Item | Extracted evidence and locator |
|---|---|
| Fluid and structure | FLiBe LiF–BeF₂ 66–34 mol%; 316 dual-certified steel tube, OD 25.4 mm, wall 3 mm. ID 19.4 mm is an **analyst subtraction**, not a reported measurement. PDF 3/972, §2. |
| Geometry | Flow path 6.97 m; top inclined 10°, bottom 20°; large tank and upper reservoir; most bends radius 12.7 cm, one Y connection. As-built drawing Fig. A.16, PDF 12/981, dimensions in inches: not transcribed as a complete CAD definition. |
| Heating/cooling | Four 61 cm radiant heater banks; top co-current air exchanger with active length 1.17 m; another cold-leg jacket not actively air-cooled in these tests. External losses persist. Heater input is not automatically net fluid duty. PDF 3–4/972–973, §2.1. |
| Operating range in selected table | Ten tests: mean salt temperature 513–693 °C, ΔT 50–85 °C, estimated speed 2.75–6.72 cm/s, Re 79–448, Pr 12–31, heater input 952–1644 W; durations 5.02–20.50 h. These are Table 4 conditions, not the entire facility design envelope. PDF 8/977. |
| Measurements | Ten centerline K-type thermocouples, 39 additional air/wall/heater temperatures; eight fiber paths, spatial sampling 0.625 mm. Radial, axial and wall paths differ. Centerline/path temperatures are not mixing-cup temperatures. PDF 4/973, §2.2, Fig. 3. |
| Flow inference | Cooling/blower pulses and some torch pulses, time-of-flight between TC pairs; peak times and distances averaged. No independent flowmeter. Standard deviation describes repeated estimates; accuracy and disturbance bias were not established. PDF 4/973 and 9/978, §§2.2,3.4. |

The recorded salt radial gradients and hot-side fluctuations support spatially nonuniform temperatures. Proposed M-shaped velocity profiles and thermal eddies are interpretations of thermal observations, not PIV measurements. Heat-transfer enhancement caused by those eddies is not demonstrated: the authors explicitly describe the preliminary thermal evidence as insufficient (PDF 5–7/974–976, §3.1). Cold-side spikes/plateaus are associated with a proposed frozen-film mechanism; its thickness and motion were not measured directly (§3.2).

## Equations, definitions and implementation cautions

The reported nondimensionalization uses \(Re=\rho V_{est}D/\mu\), \(Gr=g\beta(T_f-T_b)D^3/\nu^2\), \(Pr=\mu c_p/k\), \(Pe=RePr\), \(Ra=GrPr\), \(Ri=Gr/Re^2\), and \(Gz=(D/L)Re_ePr_e\) (PDF 5/974, Eqs. 2–8). Here D is internal diameter, \(T_b\) is the arithmetic mean of measured inlet/outlet temperatures, and L is a whole leg; neither definition establishes a spatially resolved bulk field. Cooler film temperature is assumed 460 °C at a freezing interface. Heater inner-wall temperatures are inferred from conduction and one measured outer-wall location; an equal heater-face-to-wall offset is transferred to other heaters. These conventions are essential to reproducing their Nu comparisons.

PDF 9/978, Eqs. 9–10 balance a Darcy 64/Re pressure loss plus minor losses against a simplified buoyant head. Eq. 11 is a heuristic temperature/ΔT proportionality, not a transferable temperature-dependent viscosity law. Eq. 12 is a developing-flow correlation. **Eq. 13 visibly prints Nu on its own right-hand side** in the position conventionally occupied by Re in a Sieder–Tate expression; do not silently replace it in code. Verify the cited original and the authors’ analysis scripts. Main-text descriptions alone do not establish every heat-duty, area and wall-temperature transformation used for Appendix A Nu values.

Other verified ambiguities:

- Table 2 (PDF 5/974) prints conductivity units as W °C/m and defines positive expansion coefficients with \(\rho^{-1}d\rho/dT\), missing the conventional minus sign for an expanding liquid. Correct dimensional/convention choices require explicit analyst intervention, not literal copying.
- Table 1 (PDF 4/973) gives TC24→32 = 0.479 m, TC24→35 = 1.87 m, TC32→35 = 1.47 m. The two consecutive distances sum to 1.949 m. Resolve against as-built paths/scripts before using thermal transit speed quantitatively.
- A thermal pulse perturbs the quantity it measures. The authors estimate a 10 °C pulse against a 50 °C loop difference could alter driving head by 20%, with viscosity and freezing effects also possible. This is an author estimate, not a measured correction (PDF 9/978).

## Results, uncertainty and competing explanations

The paper’s heat-transfer comparisons depend on campaign, region and correlation. Campaign 4 heating data were about 12% above the Sieder–Tate comparison in the riser and 23% above in the bottom; campaign 5 was about 18% and 37% below the *developing-flow* comparison respectively (PDF 10–11/979–980, §3.5, Fig. 15). These percentages use different baselines and must not be combined into one degradation factor. Chemistry, property changes, radiative transport and instrument changes are candidate explanations, not isolated causes. No chemistry-controlled paired experiment proves a recirculation correction.

Uncertainty uses an uncorrelated first-order RSS expression (Eq. 1, PDF 4/973). Thermocouple terms include 0.75%-of-value, 2.2 °C wire bias and test variability; installation and sheath conduction effects are explicitly excluded despite strong gradients. Table 2 lists property bounds, including 3% \(c_p\), 10% k, 20% μ and 23% Pr. Their stated 95% property bounds and repeatability standard deviations must not be combined as identical standard uncertainties. Shared thermometry and derived quantities create dependencies not represented by independent RSS. No train/select/independent-test separation is defined for the empirical speed regressions (PDF 9/978).

## TRIDENT implications and next acquisitions

**Direct methodological relevance:** audit net power, the observation operator, shared-temperature covariance and pulse-induced changes. **Conditional physical transfer:** conjugate losses, freezing-adjacent behavior, development and nonuniform temperature profiles. **Analogy only:** numerical correlations and facility-specific speed regressions. **Incompatible claims:** direct TRIDENT flow/recirculation validation, reactor licensing adequacy, or a universal heat-transfer deficit.

Model inputs must separate actual electrical input, deposition, external loss, cooler exchange and ambient conditions; outputs should distinguish centerline, wall and bulk temperatures. A model fitting one temperature definition cannot silently predict another. The conflicting TOF outcomes in S43 and S39 motivate a feasibility test, not a blanket assertion that thermal transit either always works or always fails.

Acquire S43:SUP1 (publisher Appendix B) for missing analysis details; S49 dataset [10.17632/mkbbwtztzy.1](https://doi.org/10.17632/mkbbwtztzy.1) for as-built dimensions and analysis code. Its catalogue is accessible; file bytes were not retrieved in this pass. First inspect the reduction scripts/README, not all raw data. Cited older heat-transfer originals and purification/property reports remain independent leads, not sources read through S43.

## Coverage checklist

| Component | Status | Relevance / remaining limit |
|---|---|---|
| Identity, abstract, §1 | Text inspected/extracted | History and motivation; cited originals not all read |
| §§2.1–2.3 | Text inspected/extracted; selected visual checks | Geometry, observations, reduction conventions |
| §§3.1–3.5 and §4 | Text inspected/extracted | Mechanisms, UQ, limitations; no figure digitization |
| Appendix A | Tables/captions inspected/extracted selectively | Nu/TC definitions; full drawing not reconstructed |
| References | Traced selectively | S47 retrieved; other original histories remain leads |
| Appendix B / complete data reduction | Inaccessible here | Blocks implementation-ready Nu/flow reconstruction |

## Claim-to-evidence ledger

| Stable claim ID | Claim | Locator | Qualification |
|---|---|---|---|
| S43-C01 | Corrosion and material exposure were important historical motivations for salt NC loops | §1, PDF 1–3/970–972 | Author historical account; originals distinguished |
| S43-C02 | Selected operating conditions are high-Pr, low-Re FLiBe tests, not a reactor analogue by default | Table 4, PDF 8/977; §2 | Geometry/heating/source distortions remain |
| S43-C03 | Flow is inferred by thermal pulses without an independent accuracy demonstration | §§2.2,3.4, PDF 4,9/973,978 | Repeatability is not accuracy |
| S43-C04 | Temperature profiles do not establish recirculation-induced heat-transfer enhancement | §3.1, PDF 5–7/974–976 | Physical interpretation remains provisional |
| S43-C05 | Reported UQ excludes installation/sheath bias and assumes uncorrelated propagation | §2.2/Eq.1, PDF 4/973 | Not a complete predictive budget |
| S43-C06 | Eq.13, Table2 conventions and Table1 distances need resolution before implementation | PDF 4,5,9/973,974,978 | Visual checks; analyst audit, not corrected source mathematics |
| S43-C07 | Campaign-dependent Nu offsets do not isolate a mechanism | §3.5/Fig.15, PDF 10–11/979–980 | Different baselines and confounders |
