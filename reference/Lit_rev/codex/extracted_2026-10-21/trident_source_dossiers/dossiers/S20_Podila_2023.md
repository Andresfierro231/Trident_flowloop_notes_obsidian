# S20 — Internally heated conceptual D-shaped salt loop

**Citation:** Krishna Podila, Chenguang Li, Chukwudi Azih and Qi Chen (2023), *Modelling of heat transfer in a molten salt loop using computational fluid dynamics*, Progress in Nuclear Energy164,104880. DOI https://doi.org/10.1016/j.pnucene.2023.104880 . Published online4September2023; accepted28August2023. Uploaded published9-page PDF; PDF=printed1–9. Extracted21October2026. S20 retains its existing ID; earlier unavailable-original request is resolved.

## Integrity, coverage and readiness

Title,authors,journal,DOI and final references match. Sections1–4,Tables1–3,Figures1–16,nomenclature and **Appendix A** are present. Main text and appendix read; references inspected for discovery,not their original findings independently verified. Pages3/5/7 rendered;Table3/Fig7–9 onPDF5 visually checked. Original bytes unchanged. Ready for scoped source-distribution/local-flow/prior-art synthesis. Case files and property-fit coefficients were not supplied; no numerical reproduction,complete solver specification or experimental validation claimed.

## Problem and established result

CNL investigates a conceptual core-section D-loop to guide future experimental design,not an operated MSRE reproduction or commercially specified reactor. Its original evidence consists of steady3D RANS predictions of temperature/circulation under internal heating and conjugate graphite conduction. Higher power changes predicted mixing/recirculation. Strong prior art therefore exists for CFD-informed loop design,internally heated source/solid coupling and local recirculation study. Experimental comparison is explicitly future work (§4,PDF8).

## Geometry,fluid,sources,boundaries and numerical model

Table1/PDF3: riser height3000mm,diameter25.4mm; downcomer height1500mm,diameter7mm; graphite thickness1.01mm; area ratio.076,riserH/D118. Upper plenum and connecting arms included; lower plenum/intricate features omitted. Those are source geometry,not TRIDENT facts. There are no measured instruments/data or independent flow truth.

§2.2/PDF3–4: incompressible steady RANS,STAR-CCM+16.02.007,segregated Rhie–Chow-type coupling,**first-order schemes**,standardkεtwo-layer/all-y+ treatment,two prism layers and local refinement;gravity,no-slip smooth walls,no periodic/symmetry or flow inlet/outlet. Steady solver may underresolve vortex shedding,as authors acknowledge. Density and viscosity vary with temperature;complete fitted coefficients,reference pressure/density convention and all turbulence settings are not given. “Incompressible” with variable density requires its actual solver convention to reproduce; do not silently assume Boussinesq.

Fuel receives cosine-shaped axial volumetric heating,plus selected graphite heating. Table2/PDF4 lists total.93/1.8/3.7/7.5/15kW at95%fuel/5%graphite and another7.5kW case100%fuel. Values describe **total power**,not volumetric W/m³ until normalized over heated volume. Graphite external boundaries fixed451.85°C;fluid walls adiabatic. Heat leaves through graphite boundary despite closed fluid circulation. Radiation omitted using a cited different-salt precedent;authors explicitly call for future assessment for the current salt (§2.2/PDF4). The source's quoted pure-salt radiation limit is **cited background**,not a measured bound here.

Although introduction/conclusion describe MSRE fuel,the methods explicitly **substitute LiF–BeF2–ThF4–UF4 properties for original LiF–BeF2–ZrF4–UF4** due to missing original data (§2.2/PDF4). Fuel/graphite conductivity fixed;fuelρ/μ and graphitecp fit in-house from cited He/Cantor data. No property-uncertainty propagation. Treat exact composition and property transfer as limited,not certified MSRE equivalence.

## Equations,uncertainty and results

No fully written RANS/conduction/closure system or numbered governing-equation catalogue appears. The reported Rayleigh definition is Ra=gβ(Tbulk−Twall)L³/(να) (nomenclaturePDF8);g m/s²,β K⁻¹,Lm,ν/αm²/s,Ra dimensionless. §3.3/PDF6 says bulk-to-local inner-wall temperature difference is used;Table2 reports2.44–30.91×10¹². L and averaging/property evaluation must be specified before reproduction. Ra is calculated from the resulting temperature difference here,so the power–Ra trend is not an independent experiment with all other effects controlled.

§3.1/Table3/PDF4–5:2.9/5.6/11.6million cells;location-Cmax509.43/505.21/500.96°C. Refinement ratios1.25/1.27 are consistent approximately with cube-root count ratios,not tabulated base-size ratios. Medium grid chosen on small relative peak-temperature differences. The authors invoke Richardson/GCI but provide no reproducible observed-order/GCI budget for every local QoI. Residual reduction of at least3orders and steady fluctuation do not alone certify local-field or heat-balance convergence. Percentages of absolute°Calso depend on the chosen origin;direct Kdifferences are safer for an error budget.

Figures10–12/PDF6 show predicted counterflow near walls,upward core velocity and radial temperature/velocity variation. Figures14–15/PDF7 compare power-dependent contours. The study does **not** extract a validated reverse-flow volume fraction,separation/reattachment length,uncertain extent metric or controlled recirculation-versus-heat-transfer counterfactual. Power changes source,buoyancy,flow andtemperature together. A correlation of two computed fields does not isolate recirculation causality.

AppendixA/PDF8–9 distinguishes two planned facilities:conventional boundary-heated chloride-salt loop under construction and a microwave-heated surrogate proof-of-concept,initially water,with possible R113 adaptation. These are **source-era plans**,not current2026 availability or demonstrated microwave equivalence. Data sharing permission withheld (PDF8). No held-out experimental calibration/validation split or measured uncertainty exists here.

## TRIDENT implications

Conditional mechanism analogy is justified;direct transfer of coefficients,local geometry or extent is not. A conservative externally heated ACU/VCU model must explicitly preserve source path,losses and observed-state definitions;it cannot inherit this core surrogate's volumetric heating/fixed graphite sink. Existing local-flowCFD is not vacant research territory. A useful additional result needs a specific descriptor,uncertainty/adequacy argument and independent consequence. Without qualified TRIDENT spatial evidence,retain supported thermal/duty/response outputs and label local extent unvalidated.

| Coverage | PDF | Status |
|---|---|---|
| Identity/background | 1–3 | Read;historical/status claims treated as cited/source-era |
| Geometry/model/BC | 3–4 | Read/extracted;full solver/property files unavailable |
| Mesh/results/local fields | 4–7 | Read/extracted;selected visual checks,not digitized/reproduced |
| Conclusion/nomenclature | 7–8 | Read/extracted |
| AppendixA | 8–9 | Read;planned facilities distinguished from this study's evidence |
| References | 9 | Discovery inspection;originals not thereby read |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S20-C01 | Conceptual internally heated D-loopCFD is established prior art | §2–4,PDF3–8 | Not a measured reactor/test-loop validation |
| S20-C02 | Steady first-order RANS may underresolve unsteady local flow | §2.2/PDF3 | Author limitation;not a universal closure rejection |
| S20-C03 | Methods substitute thorium-bearing salt properties for original MSRE salt | §2.2/PDF4 | Exact MSRE-fluid equivalence not established |
| S20-C04 | Fixed-temperature graphite removes heat while fluid boundaries are adiabatic | §2.2/PDF4 | Source/sink differs from external-heater pipe loop |
| S20-C05 | Mesh comparison targets a location-Ctemperature peak | §3.1/Table3,PDF4–5 | Not converged recirculation extent/total uncertainty |
| S20-C06 | Local recirculation and its change with power are numerical predictions | Fig10–15,PDF6–7 | No measured extent or isolated thermal-effect counterfactual |
| S20-C07 | Experimental assessment is future work | §4/PDF8 | No experimental validation claimed from this source |
| S20-C08 | Appendix distinguishes boundary-heated and proposed microwave-heated facilities | AppendixA/PDF8–9 | Source-era development plans,not available TRIDENT resources |
