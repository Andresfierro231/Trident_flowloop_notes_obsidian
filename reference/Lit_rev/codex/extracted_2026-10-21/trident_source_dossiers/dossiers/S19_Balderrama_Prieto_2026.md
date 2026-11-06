# S19 — LiCl–KCl loop CFD and temperature-based flow inference

21October2026. **Scoped ready** for observation/flow-inference, CFD assessment and local-flow limitations. Original identity matches publisher metadata. Silvino A.Balderrama Prieto, Michael Shaltry, Robin V.Roper, Ruchi Gakhar, *CFD modeling of natural circulation in LiCl-KCl molten salt closed loop*, Applied Thermal Engineering284(2026),128986; online12November2025; DOI https://doi.org/10.1016/j.applthermaleng.2025.128986. Uploaded typeset12-page article, printed=PDF, complete through final reference **[29]**, PDF12; no appendix. All main text read; critical Tables5/7 and equations/results pages visually inspected. No external code/data/supplement inspected or simulations reproduced.

## What was established

The original work compares steady conjugate STAR-CCM+ calculations to exterior thermocouple measurements in an INL Mk-I chloride loop, and compares predicted velocities to two analytical estimates derived from surface or calculated bulk temperatures. **No directly measured bulk temperature or velocity reference is available** (§2.4,PDF3;§4,PDF10–11). The article's broad concluding language about validated flow rates therefore exceeds an independently measured velocity validation. Its measured thermal evidence and model-to-model flow comparison must be reported separately.

Cited foundations include S43 FLiBe loop, S50 molten-salt natural circulation, source-distribution studies and hydraulic/heat-transfer correlations. The open-vertical-pipe heat-transfer correlation in Ref29, DOI10.1016/j.ijthermalsci.2017.01.014, was not independently read here; its applicability to this closed loop remains a check rather than an established transferable closure.

## Geometry, conditions, observations

§§2.1–2.3/PDF2–3,Figures1–2,Tables1–2:316L tubing ID≈0.0111m,OD0.0127m,total effective length1.01m,fluid volume9.713e−5m³; entire primary loop wrapped in0.0254m alumina insulation. Eutectic59–41mol%LiCl–KCl; melting355°C. Four external resistance heaters and13 exterior K-type thermocouples; argon glovebox with oxygen/moisture reported below1ppm. Cold-leg gas-cooling jackets were not activated for the selected cases because cooling reached the freezing point too quickly.

Experiment1 changes hot-leg setpoint550→500→450°C, with roughly200s first hold and a further change after1000s (§3.1,PDF6). Experiment2 cycles450/500°C. **These are controller surface-temperature conditions**, not measured net deposited-power transients. CFD is steady with boundary conditions adjusted to measured/averaged temperatures for selected conditions (§§2.4,3/PDF3–7). This is not an independently driven prediction of the complete controller/heater transient.

Density2010−0.512T kg/m³, conductivity0.6143−2.8675e−4T W/(mK), cp1250J/(kgK), viscosity0.08703exp[20852.56807/(RT)] **mPa·s**, with T in K(Table2/PDF3). Property sources differ. No complete uncertainty/covariance functions, sensor calibration/drift budget or operating Re/Pr envelope is established. Convert mPa·s before combining with SI quantities. Do not import this chloride property set into TRIDENT.

## Model mathematics and numerical assessment

Eq1–3/PDF3 give steady mass, momentum and energy descriptions; steel/fluid conjugate regions and LEB k–ε with all-y+ treatment are selected (Table4/PDF5). Alternative-model superiority is largely based on cited work, not a controlled turbulence-model comparison in this paper. The model omits the feed inlet in constructing its CFD geometry (§2.4.2). The experimental insulation does not appear as a separate material region in Table4; a fully specified exterior thermal boundary/source reconstruction is not provided for independent reproduction.

**Reported-energy-equation flag:** Eq2 prints −∇·(k∇T) on the right and describes E as total energy per unit volume although the transport term also multiplies by ρ. Those signs/units do not give an unambiguous conventional conservative energy equation. The actual fluid solver is described as segregated fluid temperature, so do not infer that the implementation solves the printed equation literally. Record this as a source-notation ambiguity, not a corrected solver.

§2.5/PDF6,Eq17–27 builds a steady bulk balance: Δpb=−∮ρg dz; a simplified linear-temperature relation gives ρ0βgΔTH; Darcy/minor loss gives ρv²[fL/D+ΣKL]/2; solving yields v=[2βgΔTH/(fL/D+ΣKL)]^1/2. f64/Re below1187 and0.3164Re^−.25 above. G is not used: v m/s and mdot=ρAflowv kg/s. Qdot=mdot cpΔT W; a heat-transfer correlation determines h; Tbulk=Ts−Qdot/(hAheat). Aflow and Aheat are physically different despite reusing A. These relations are coupled through v,Re,h and temperature; the paper does not supply a fully independent source/flow anchor or complete iteration specification. A square-root positive branch does not establish reversal prediction.

The Nu correlation uses Gr,Pr andL/D, and its quoted Pr range is0.7–2014(Eq24). A range in one dimensionless variable does not establish geometry/regime validity; the original correlation concerns an **open vertical pipe**. Do not recommend it for our loop without that original applicability check.

§2.4.4/PDF4–6 uses three meshes and a safety-factor Richardson estimate, alongside GCI. Table5 lists5,611,893/1,976,147/652,316cells and h3.29e−4/4.73e−4/7.89e−4. The prose/derivation invokes a common adjacent r=2.4. **Our arithmetic check:** adjacent h ratios≈1.438 and1.668;2.4 is approximately coarse/fine, not both adjacent ratios. The base-size ratios are also not2.4. Consequently the reported numerical uncertainty cannot be adopted as independently verified without clarification/recalculation using the actual grids. TCs1,3,5–7 were excluded from this convergence comparison because heater-proximate values were nearly imposed/unchanged.

Table6/PDF6 reports average-velocity UFS7.67e−4m/s and temperature values up to9°C. These are discretization estimates under the chosen model, not complete experimental/CFD predictive uncertainty or a universal95% coverage statement. Normative ASME requirements and Xing–Stern statistical guarantees were not verified from cited originals here.

## Results and interpretation

Table7/PDF8 reports, for450/500/550°C respectively, CFD average velocities0.0493/0.0561/0.0625m/s; surface-based analytical0.0504/0.0653/0.0809; calculated-bulk-based0.0480/0.0620/0.0755. Its printed discrepancies are2.2/14.0/22.6% and2.6/9.5/17.2%. Rounded source values give the same denominator convention to rounding: analytical velocity in the denominator. The quoted 'up to5.5%' in§4/PDF11 is the **increase between these comparison discrepancies**, approximately5.4percentage points in the550°C rounded table. It is not an independently measured velocity error bound or total flow uncertainty.

Figures4–7/PDF7–9 show surface-temperature agreement/bias and modeled wall-to-fluid profiles. The reported13.82–20.07degree surface-to-center/section-average differences are **CFD estimates**, not internal thermometer observations. Section3.2/Figures8–10/PDF9–10 shows changes of modeled T-junction vortices; no measured spatial recirculation extent or controlled heat-transfer counterfactual is established. Uncertainty in conductivity is a proposed contributor to bias, not a separately identified cause.

No locked calibration/selection/validation partition, independent flow metrology or predictive interval-coverage campaign is demonstrated. Reproducing some surface measurements under measured thermal boundaries supports a conditional thermal assessment, not an autonomous whole-loop transient validation. The paper is nevertheless a very close comparator and a useful caution against conflating observables with inferred quantities.

## TRIDENT consequence and coverage

Source, observation and assessment contracts must distinguish prescribed wall temperatures, predicted fluid temperatures, model-derived bulk averages and independent measurements. Loop circulation and local recirculation require different evidence. Theoretical contribution must go beyond making velocity estimates from wall temperatures; a defensible uncertainty/identifiability result and independent consequence would be additional requirements. S19 supports conditional observation research, not adoption of its numerical coefficients.

| Coverage | PDF | Status |
|---|---|---|
| Identity/introduction | 1–2 | Read; original contribution versus cited background separated |
| Facility/properties | 2–3 | Read/extracted,Tables1–2 mapped |
| CFD equations/models | 3–5 | Read/extracted selectively; no rederivation of all LEB transport terms |
| Numerical convergence | 4–6 | Read; Table5 visually checked; r inconsistency retained |
| Analytical inference | 6 | Read/extracted; coupled-input and correlation-transfer limitations |
| Results/figures | 6–10 | Read/qualitatively inspected; Table7 checked; no full curve digitization |
| Conclusion/references | 10–12 | Read/inspected; cited originals not thereby read |
| Code/raw data/supplements | External | Not supplied/read; no numerical reproduction |

## Stable claims

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S19-C01 | Surface thermometry provides the experimental comparison; no direct flow benchmark | §2.1–2.4,PDF2–3 | Velocity not independently validated |
| S19-C02 | Steady CFD uses measured/averaged thermal boundaries | §3.1,PDF6–7;Table4/PDF5 | Not autonomous transient prediction |
| S19-C03 | Surface- and calculated-bulk-based flow estimates differ from CFD | Table7,PDF8 | Model-to-model, shared observation ingredients |
| S19-C04 | Quoted5.5% is a discrepancy increase, not measured flow-error bound | Table7/PDF8;§4/PDF11 | Rounded table≈5.4percentage points |
| S19-C05 | Stated common refinement ratio conflicts with tabulated adjacent h ratios | §2.4.4,Table5,PDF5 | Our arithmetic; uncertainty estimate needs clarification |
| S19-C06 | Modeled local profiles/vortices are not measured extent/causality | Fig7–10,PDF9–10 | No direct local flow/thermal-effect validation |
| S19-C07 | Printed energy formulation is ambiguous in sign and E units | Eq2,PDF3 | Actual implementation not inferred from typo |
| S19-C08 | Analytical h closure comes from an open-vertical-pipe correlation | Eq24/PDF6;Ref29/PDF12 | Original applicability not read |
