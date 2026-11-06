# S52 — Borgohain et al. (2011): LeBENC formulation and calibrated assessment

2026-10-20. A. Borgohain, B.K. Jaiswal, N.K. Maheshwari, P.K. Vijayan, D. Saha, R.K. Sinha. *Natural circulation studies in a lead bismuth eutectic loop*. Progress in Nuclear Energy 53(4), 308–319. https://doi.org/10.1016/j.pnucene.2010.10.004.

## Document identity and coverage

Uploaded publisher PDF, 12 continuous pages. PDF page + 307 = printed page. Metadata/title/authors/DOI match the publication; acceptance in October2010 differs from 2011 volume year. All main sections and reference list inspected in text; PDF pp.5–8 additionally visually checked for governing/discrete equations, tables and heat-exchanger/loss procedures. Equations/figures readable on inspected pages. No code, run files, raw measurements or supplement supplied; cited originals remain separate sources.

Scope: original brief's loop motivation, conservation/reduction, fluid/solid states, closures, observed versus predicted circulation, loss calibration, transient assessment and transfer limits.

## Purpose, facility and evidence

The HANS LBE facility was built at BARC for thermal hydraulics, instrumentation and material compatibility in support of the proposed compact high-temperature reactor (§§1–2, PDF1–3 / 308–310). It is a liquid-metal experiment, **not a molten-salt experiment or evidence of MSR similarity**. Chemistry/oxygen control is an explicit additional purpose (§3); chemical equations1–6 are contextual, not a TRIDENT chemistry model.

Table1 (PDF4 / 311): LBE, SS316L, nominal 15mmNB SCH80 connecting pipe, center elevation difference750mm, stated total circulation length5500mm, stated inventory500kg, maximum experimental power2.5kW, operating temperature limit500°C, mass-flow range0.09–0.15kg/s. Inventory is a source design-table entry; do not assign all500kg to circulating thermal storage without a vessel/control-volume inventory. Table3 gives nonuniform heater, exchanger and tank diameters and fourteen segment lengths; reconcile definitions before rebuilding geometry. Our sum of Table3 segment lengths is6325mm, whereas Table1 states5500mm total circulation length; this unresolved geometry-definition discrepancy must not be silently merged.

External loop infrastructure includes an immersion heater, air-jacket exchanger, expansion tank, trace heaters and argon cover gas. Fifty-six K-type thermocouples, mostly surface-mounted and some immersed, are described (§2, PDF3). No complete sensor uncertainty, response correction, joint covariance or heat-input calibration budget is reported.

## Reported equations and implementation audit

Let W denote signed mass flow, kg/s; A cross-sectional area, m²; x loop distance; z elevation; rho0 reference density; f pipe friction factor; k local loss coefficient. The incompressible model makes W spatially uniform (§4.1), with Boussinesq density Eq8, separate fluid temperature T and wall temperature Tw, and axial conduction in both.

**Momentum:** Eqs7–9 (PDF5 / 312), followed by implicit time discretization12–14 (PDF6 / 313). The inertia coefficient is \(C_1=\sum_i\Delta x_i/A_i\), not simply total length for nonuniform area. Equation13 uses a signed \(W^{n+1}|W^{n+1}|\) drag. Reported Eq9 instead displays W²; source sign conventions must be checked before reversal calculations. Eq7's distributed-friction numerator appears as W rather than W², dimensionally incompatible with the pressure terms when W has its defined kg/s units. Do not silently copy it.

**Fluid:** Eq10 (PDF5) includes advection, axial diffusion, fluid-wall exchange and immersion-heater source \(qA_h/(\rho C_p A_f)\). The nomenclature defines q as W/m²; if Ah and Af both denote cross-sectional areas as the source notation suggests, the source expression lacks a length conversion for K/s. Exact heater-area definition is insufficiently specified. Treat the deposition term as unresolved until reconstructed from an explicit control volume.

**Wall:** Eqs11/19 (PDF5–6) retain axial conduction and two heat-exchange paths. The external exchange coefficient is multiplied by **inner diameter** \(D_i/(D_o^2-D_i^2)\), as is the inner exchange. Our cylindrical-area derivation gives outer perimeter/solid area \(4D_o/(D_o^2-D_i^2)\) for an outside-area coefficient; the printed expression would require a separately defined inside-area-referenced effective coefficient. Eq25 uses pipe outer area. Thus area conventions are unresolved, not automatically a code defect.

**Discretization:** first-order upwind convection, central diffusion, explicit wall/thermal updates, then implicit circulation (Eqs12–22, §§4.2–4.3, PDF6–7). Equations17/18/21 impose positivity-based step restrictions recomputed with flow; these are restrictions of the reported discretization, not accuracy/convergence evidence. Table2's fluid coefficients contain heater-source terms in diagonal/source positions with apparent unit/sign/index inconsistencies; Eq15 uses new wall temperature after the wall is advanced using old fluid temperature. Exact discrete exchange conservation and source treatment need verification from fresh conservative discretization, not literal Table2 transcription.

Suggested **independent implementation form**, not a transcription: integrate fluid/wall energy over each finite volume, use the same interface heat rate with opposite signs, use explicit surface areas and signed advective enthalpy fluxes, and use signed buoyancy/drag consistently. For temperature-dependent properties, establish a compatible energy/enthalpy formulation; numerical temperature updates alone do not guarantee conservation.

## Closures, calibration and results

§4.4 (PDF7 / 314): fourteen segments/280 nodes; temperature-dependent LBE properties updated each time step from OECD/NEA2007; SS316 properties from a heat-transfer text; local losses from Idelchik. Eq23 uses liquid-metal \(Nu=A+0.018Pe^{0.8}\) with piecewise A. This is an LBE closure, not a high-Pr glycol/HITEC closure.

**Heat-exchanger characterization is experiment-informed.** Eq24/§4.5 (PDF7–8 / 314–315): infer W from heater power and measured heater temperature difference, infer exchanger heat transfer and logarithmic temperature difference, estimate overall U, average U at each power, subtract primary/wall resistance to obtain a secondary coefficient. This is a resistance calculation requiring a common area basis, not direct subtraction of coefficient values. The prose has incorrect equation cross-references to23/22. Predicted temperatures/flow assessed using these coefficients are not wholly independent predictions of an uncalibrated cooler.

§4.6/Eq25 (PDF8): regional equivalent ambient coefficients are obtained from inferred regional heat loss and measured temperature drop, with \(Q_{p,j}=h_{o,j}A_{p,j}(T_{s,j}-T_a)\). Thus “experimental flow,” exchanger U and regional loss estimates share inputs. They are not three independent validation measurements.

§5.1/Figs9–10 (PDF8–9): flow is inferred calorimetrically. Reported maximum heater temperature-difference disagreement20%; no full uncertainty interval or denominator definition beyond the chosen difference. Reported typical1800W piping loss50W/m and fluid drop4°C/m are local campaign observations, not TRIDENT coefficients. The claim of insignificant axial conduction (§5.1/Fig11, PDF9) relies on agreement with a correlation omitting it; no isolated conduction-off/on sensitivity or uncertainty bound is shown. Keep the source claim qualified.

Startup1200/1800W (§5.2.1, PDF9–10) shows smooth measured thermal behavior and source-reported outlet peaks318°C/400°C. “Zero flow” initial conditions were inferred by approximately equalizing temperatures using trace heat, not independently established by a flowmeter. The source's percent temperature overshoots use Celsius-reference values; use temperature differences or an explicit physical normalization for comparison.

Airflow interruption from1200W (§5.2.2/Fig13, PDF10): residual exchanger temperature difference about30°C and faster initial predicted warming; structures/flanges/support storage are proposed explanations. At t=37500s the heater is turned off, bounding the experiment. Step1500→1800→1500W (§5.2.3/Fig14, PDF10–11) is damped by expansion-tank inventory/mixing. These are relevant existing demonstrations of retained-physics issues, not direct identification of a unique mechanism.

## Stable claim-to-evidence table

| Claim ID | Claim | Locator | Limit |
|---|---|---|---|
| S52-C01 | HANS serves reactor-relevant thermal, materials and instrumentation purposes | §§1–3, PDF1–4 / 308–311 | LBE/CHTR context, not MSR validation |
| S52-C02 | Nonuniform-area momentum and separate fluid/wall conduction predate this thesis | §§4.1–4.4, Eqs7–23, PDF5–7 | Printed implementation ambiguities remain |
| S52-C03 | Cooler coefficients are inferred from experiment at each power | §4.5/Eq24/Fig8, PDF7–8 | Calibration dependence; not independent validation |
| S52-C04 | Regional ambient coefficients and experimental flow use thermal balances | §4.6/Eq25/§5.1, PDF8 | Shared-input uncertainty and identifiability matter |
| S52-C05 | Structural/tank storage affects interpretation of transients | §5.2/Figs12–14, PDF9–11 | Authors' mechanisms not isolated experimentally |
| S52-C06 | Momentum/source/area/discrete-coefficient conventions need audit before coding | Eqs7–22/Table2, PDF5–7 | Our mathematical appraisal, not an executed-code finding |
| S52-C07 | Negligible axial conduction is a limited source conclusion | §5.1/Fig11/§6, PDF9/11 | No standalone error bound or controlled ablation |

## TRIDENT implications and skeptical appraisal

Useful directly as a model-family and calibration-dependence comparator. Transfer of full model structure is conditional on our geometry, observation map, sources and accepted properties; LBE transport/chemistry coefficients are incompatible with direct high-Pr adoption. Retaining wall storage, ambient loss, nonuniform geometry or an expansion tank is established prior art. A stronger prospective contribution is identifying which states/parameter combinations are supported, and demonstrating better independent QoI predictions with a declared uncertainty contract.

Before Codex implementation: build a corrected, explicitly derived conservative formulation; document every departure from reported equations; test closed-system energy conservation, exchange cancellation, uniform-temperature equilibrium, zero-input limits, signed flow reversal and numerical refinement. The printed table is not implementation-ready.

## Coverage and readiness

| Portion | Status | Outstanding |
|---|---|---|
| §§1–2/Table1/Figs1–2 | Text inspected/extracted | Exact calibration/layout records unavailable |
| §3/Eqs1–6/Figs3–6 | Context inspected; chemistry detail not extracted | Not a TRIDENT chemistry model |
| §§4.1–4.4/Eqs7–23/Tables2–3 | Inspected/extracted; PDF5–7 visual audit | No executable implementation; ambiguities recorded |
| §§4.5–4.6/Eqs24–25/Fig8 | Inspected/extracted; PDF7–8 visual audit | No independent loss/flow data |
| §5/Figs9–14/§6 | Text/results inspected/extracted; PDF8 visual audit | No digitization or numerical replication |
| Nomenclature/references | Inspected/selectively extracted | Cited originals not thereby read |

Ready for qualified prior-art/motivation/assumption synthesis. Not ready for literal code reproduction or independent flow-validation certification.
