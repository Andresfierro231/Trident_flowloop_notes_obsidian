# S64 — Bardet & Peterson (2008): what salt-surrogate scaling does and does not establish

Extraction2026-10-20. **Scoped ready** for similarity/motivation synthesis and the liquid/solid scaling relations below. Not an experimental validation dossier or a validated TRIDENT scaling calculation.

## Identity and inspected version

Philippe M. Bardet and Per F. Peterson, *Options for Scaled Experiments for High Temperature Liquid Salt and Helium Fluid Mechanics and Convective Heat Transfer*, Nuclear Technology163(3),344–357(2008). DOI https://doi.org/10.13182/NT163-344. Primary publisher/institutional identity checked; retrieved Berkeley-hosted typeset article14PDFpages, printed=PDF+343. First/last pages match344/357; no missing page observed. Entire article text read; equations2–10 and critical example/nomenclature pages visually enlarged. No appendix in the article; no separately acquired underlying property measurements or supplementary data/code. No reproduction of a complete facility design.

## Problem, contribution and motivation

The paper develops fluid/structural material choices and scale relations for reduced-temperature/size/power experiments on salt/helium fluid mechanics and convective heat transfer. The mission includes high-temperature heat-transport systems, not exclusively natural-circulation MSR primaries. Original contribution is a scaling/design analysis with candidate materials and illustrative ratios. It does not demonstrate a reactor-sized integral experiment or guarantee that any high-Pr surrogate loop is similar.

§I/PDF1–2/344–345 provides historical context about fuel-salt programs and their test loops, but those histories are **cited background**, not independent measurements by these authors. For original history use S40/S41/S42/S47 at their recorded depths. Prior work includes Kline similitude, Zuber integrated scaling, ORNL salt properties, radiation analyses and matched-index diagnostics; those originals were not newly read through this citation.

## Physics, assumptions and data

§II–IV/PDF3–7/346–350 nondimensionalizes mass/momentum/energy and boundary conditions. Fluid geometry must scale; boundary/initial conditions and solid response matter in addition to fluid groups. Liquids are single phase/incompressible in the intended regime. Temperature dependence of density, viscosity and conductivity introduces additional fractional-change constraints. Helium examples assume ideal-gas/low-compressibility behavior; nitrogen is a gas analogue, not a substitute for liquid salt in TRIDENT.

TablesI–IV/PDF3,8–9 supply approximate salt/gas/simulant/structure properties. Some oil density/viscosity/surface-tension values are author measurements (TableII footnote); others are manufacturer/cited values. Their complete metrological uncertainty is not supplied. These old tables are **not current certified property functions**. No particular TRIDENT fluid, geometry, sensor map or operating envelope is identified by this paper.

TherminolVP-1 and light mineral oil are candidate salt simulants; fused silica/Pyrex/engineered solids can approximate structural properties. Refractive-index compatibility enables diagnostics, but an optical facility's instrumentation is not assumed available to TRIDENT. Radiation, free surfaces, property variations, material compatibility and gas compressibility impose separate limits. The specified material operating temperatures are source-era examples, not procurement/safety recommendations.

## Consequential mathematics with conventions

Reported groups (§II/PDF3/346; nomenclaturePDF13–14): Re=UL/ν, Fr=U²/(gL), Pr=ν/αf, Gr=gL³βΔT/ν². Their Strouhal-like time ratio is **τU/L**, rather than frequency×L/U; retain that convention. Their printed Fourier group is **l²/(αsτ)** (PDF13/356), inverse to the commonly used αsτ/l²; equality of the groups gives the same matching condition, but values cannot be interchanged silently. Fluid length L and solid thickness l are distinct; fluid conductivity k and solid conductivity λ are distinct.

Reported Eq2–7, PDF5–6/348–349, for model m/prototype p under common gravity and matched Re/Fr:

\[
\frac{U_mL_m}{U_pL_p}=\frac{\nu_m}{\nu_p},\quad
\frac{U_m}{U_p}=\left(\frac{L_m}{L_p}\right)^{1/2},\quad
\left(\frac{L_m}{L_p}\right)^{3/2}=\frac{\nu_m}{\nu_p},\quad
\frac{\tau_m}{\tau_p}=\frac{L_mU_p}{U_mL_p}.
\]

Buoyancy matching additionally uses βmΔTm=βpΔTp, with the buoyant scale Ub=(gLβΔT)^1/2. Pr must also be matched for the intended heat-transfer similarity. These equalities assume the selected equations/geometry/boundaries apply; they are not a proof that matching a small subset reproduces every local QoI. A closed completely filled loop need not impose every free-surface constraint used for an integral pool system.

Their modified Bi*=kl/(λL) and Eq8–10, PDF6/349, give

\[
\frac{\lambda_m}{\lambda_p}=\frac{k_m}{k_p}\frac{l_m}{l_p}\frac{L_p}{L_m},\qquad
\frac{\alpha_{s,m}}{\alpha_{s,p}}=\frac{l_m^2}{l_p^2}\frac{\tau_p}{\tau_m}.
\]

Both expressions are dimensionless ratios. The first addresses steady interface heat transport; the second adds transient solid response. Wall-thickness distortion can help satisfy one constraint but changes the other. Fluid Pr agreement alone says nothing about solid storage or heat-loss contacts.

Eq11 adds We=ρU²L/σ for surface-tension effects where relevant. Eq17–18/PDF10/353 provide pumping/heating scaling: Qp~ρU³L² and Qh~ρcpΔTUL². Treat the equalities as characteristic scaling estimates with omitted geometry/loss factors, not exact pump power formulas for arbitrary components.

## Results and numerical integrity

TableV/PDF11/354 shows illustrative simultaneous Re/Fr/Pr/Gr matching with oil while viscosity-variation similarity remains distorted: listed γΔT ratios0.43–0.91 across feasible examples. For FLiBe600°C, model liquid80°C, length ratio0.44, velocity0.66, ΔT0.29, heating0.014 and pumping0.029 are reported. Our scale check τratio=.44/.66≈.667 is consistent with time compression of order two-thirds; rounded columns need not give an exact common ratio. The generic prose 'typically below2%' must not replace individual table entries, some of which exceed2%. These are example design calculations, not measured prediction errors or achieved TRIDENT ratios.

§III/PDF4–5/347–348 explicitly limits low-temperature surrogates when thermal radiation matters. **Do not universalize its laminar/turbulent examples.** Visually checked PDF5 states D=1mm, Nu3.66 and h0.178kW/(m²K) for the laminar illustration; with the preceding salt k=1W/(mK), Nu·k/D gives3.66kW/(m²K), not0.178. No alternative conductivity/reference diameter is specified in that paragraph. The radiative flux is also once printed as kW rather than kW/m². Keep these illustration inconsistencies flagged; do not export the cited40% radiation fraction as a verified general result. The qualitative need to assess radiation remains independently supported by their governing-physics discussion.

§VI/PDF10–12/353–355 explains geometric/module/stream-tube scaling distortions and varying conditions to reveal dominant phenomena. TableVI lists mineral-oil constraints; TableVII gas alternatives. No quantified total uncertainty propagation or independent experimental validation of every matching condition is provided.

## Transfer, implementation and skepticism

**Direct methodological use:** create a decision-specific similarity/distortion ledger: geometry; fluid groups; density/viscosity variation; wall conductance/storage; source/sink histories; external losses; initial conditions. Different QoIs need different tolerances. Existing measured-facility prediction remains worthwhile even if reactor-scale quantitative transfer cannot be justified.

**Conditional physical transfer:** salt-surrogate fluid/solid convection, within matched regimes and declared distortions. **Analogy only:** optical access or a high-Pr fluid by itself. **Incompatible as evidence for:** nuclear source generation, delayed-neutron transport, chemistry, irradiation, freezing/boiling or radiatively important salt behavior not represented in the experiment.

For Codex, retain explicit reference lengths and the paper-specific Fr/Fo/time-ratio definitions. Compute groups from uncertain property functions over the actual envelope, not one nominal point or TableV borrowed for a different fluid. This is an implementation requirement derived here, not a performed calculation or a selected final method.

## Stable claims

| ID | Claim | Original locator | Scope |
|---|---|---|---|
| S64-C01 | Similarity includes boundary/initial and solid conditions, beyond fluid groups | §IV.A,PDF6/349,Eq8–10 | Specific scaling assumptions |
| S64-C02 | Matched Re/Fr sets coupled velocity/length scales; buoyancy adds βΔT | Eq2–7,PDF5–6/348–349 | Common gravity/geometric scaling |
| S64-C03 | Pr similarity does not ensure solid transient similarity | Eq8–10,PDF6/349 | Steady/transient constraints differ |
| S64-C04 | Viscosity-variation distortion remains in example group-matched cases | TableV,PDF11/354 | Source-era property estimates |
| S64-C05 | Low-temperature surrogate experiments do not automatically reproduce radiation | §III,PDF4–5/347–348 | Case-specific radiative assessment |
| S64-C06 | The laminar radiation illustration contains an h–Nu–D inconsistency | §III,PDF5/348 | Our dimensional check, unresolved reference |
| S64-C07 | The source uses reciprocal-to-common Fo and a time-ratio convention | §II/nomenclature,PDF3,13–14 | Preserve definitions in comparisons |
| S64-C08 | Reduced size/power experiments permit selected mechanism/code tests with explicit distortions | §VI–VII,PDF10–13/353–356 | Not proof of reactor equivalence |

## Coverage

| Section | PDF/printed | Status |
|---|---|---|
| I introduction | 1–2/344–345 | Read/extracted; historical statements treated as cited background |
| II groups | 3/346 | Read/extracted; definitions checked |
| III radiation | 3–5/346–348 | Read/extracted; critical example visually checked and flagged |
| IV liquid/gas scaling | 5–8/348–351 | Read; liquid equations extracted; gas relations not transcribed for current scope |
| V fluids/materials,TablesI–IV | 8–9/351–352;TableI3/346 | Read/inspected; no full property-table transcription or current certification |
| VI examples,TablesV–VII | 10–12/353–355 | Read/extracted selectively; no uncertainty/reproduction claimed |
| VII,nomenclature,references | 13–14/356–357 | Read/inspected; convention flags retained; cited originals not thereby read |
| Supplement/raw measurements | Outside article | Not acquired; no full numerical reproduction |

Next questions: update similarity with actual facility inputs and a modern close surrogate comparator; determine whether radiation/wall/storage distortions matter to the chosen QoI. No facility scaling has been computed in this pass.
