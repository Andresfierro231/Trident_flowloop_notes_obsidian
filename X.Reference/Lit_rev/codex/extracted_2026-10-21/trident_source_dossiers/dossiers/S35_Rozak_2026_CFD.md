# S35 — High-Fidelity CFD Simulation of Single-Phase Natural Circulation Loop Experiments: Verification and Validation

Audit: 2026-10-20. Ethan Rozak, Master of Science in Engineering thesis, University of Texas at Austin, title page May2026. User-supplied139-page PDF; final repository/deposit version not established. A cited software patch is dated July2026 (bibliography, printed101/PDF115), after the title-page date, reinforcing the need to confirm the revision date rather than assuming this is the deposited May version. Source hash remains the Stage2 hash. This is the earlier uploaded Ethan thesis, now included alongside the eight distinct works in the newer upload batch.

Pagination: PDF1 title; PDF2 abstract printed i; PDF14 nomenclature printed xiii; Arabic printed1 at PDF15. **Arabic printed page = PDF−14**, through printed125/PDF139. Main text begins printed3/PDF17. All relevant technical chapters3–7, literature chapter2, AppendicesA–C, tables and captions were read. Intro motivation/objectives read; outline-only continuation PDF22–23 was not extracted. Selected equation/table/flow-field pages were visually inspected. Graphs were not digitized; source code, dictionaries, meshes, raw fields and execution logs were not available for an independent audit. No apparent missing technical pages. Unresolved “Section??” and table placeholders in the supplied copy are recorded, not filled in by inference.

## Problem, contribution and prior evidence

The thesis reconstructs the TAMU water/HITEC natural-circulation facility and compares OpenFOAM calculations with S37's eight experimental states. Contributions claimed are a scripted simulation/V&V pipeline, a segmented energy-loss reconstruction, and a multilayer cylindrical Robin thermal boundary condition. It also reports strong temperature gradients and local reverse axial flow that can undermine simplistic point-temperature and planar-PIV interpretations.

The evidence is a **retrospective, partly calibrated steady-state comparison**. Insulation and geometry were reconstructed, a first-order model uses experimental wall temperatures, different water/salt insulation configurations were selected, and turbulence treatments were chosen partly by agreement with the same data (§4.1–4.5,5.1,5.7,6.4). This does not constitute an untouched out-of-sample autonomous validation set. The thesis is useful prior work; neither its “fully validated” language nor its blanket rejection of a data case should be inherited without appraisal.

The cited strongest comparators include S09/S36, S16/S37, Britsch2019, DYNASTY CFD/LES and RANS work, Simamora–Lee2026, and the Celik/Roache/ASME numerical-uncertainty literature (printed10–20/PDF24–34; bibliography100–106/PDF114–120). Original papers cited here remain leads unless separately read. They already challenge a generic claim that experiment–CFD learning, thermal-loss reconstruction or multidimensional salt-loop modeling is unexplored.

## Facility and data contract

Geometry is reconstructed as a rhombic/inclined four-leg loop, roughly0.9144m per nominal leg and total modeled path4.353m. Stainless ID0.93in (23.622mm), quartz ID0.83in (21.082mm), quartz exposed length186mm; cooler approximately1ft (304.8mm). Nominal incline20° became21.5° after image reconstruction; the left leg was inferred about1.35cm longer than the right. Fitting and unused-stub geometry matters (§4.1 printed33–35/PDF47–49; §5.1 printed48–52/PDF62–66; AppendixA107–110/PDF121–124). These are this thesis's reconstructed dimensions, not a correction to every TAMU paper or TRIDENT geometry. Insulation composition/thickness and probe azimuths were incompletely recorded. AppendixA also labels the right leg “riser,” conflicting with the main circulation description; retain actual coordinates.

Water heater settings58.8–129W and salt232.3–337.6W; air cooling188L/min water and37L/min salt (Tables4.2–4.3 printed41/PDF55; §4.2.3 printed37/PDF51). Salt nominal reported Re74.86–158.92 and Pr54.29–31.74; water Re711.78–1806.52 and Pr4.23–2.96. AppendixC contains conflicting reconstructed salt global/local groups; do not treat its changed Pr and Re columns as harmonized with S37 or Table4.2. Its salt “global Pr” is nearly constant while copied Ra trends differ, so the property/reference-temperature definitions need reconstruction.

Six internal K-type thermocouples and eleven wall/jacket locations provide temperatures. TW10 is on the cooler jacket, not primary pipe wall. PIV full-field recordings:6,000frames at250fps; near-wall8,000 at1,000fps (§4.2 printed36–37/PDF50–51). Salt raw full-field data were available to the thesis author; original water full-field data were unavailable, so water profiles were digitized from published plots. Digitization was evaluated against available salt profiles; an assigned1.5% water contribution is based on pooled RMS1.36%, while individual salt comparisons reach3.65% RMS and14.10% maximum error (Table4.6 printed47/PDF61). A pooled digitization term is not a bound on every profile point.

The inferred experimental bulk velocity uses the right half of a planar profile, assumes axisymmetry and applies a test-section/pipe area ratio (Eqs4.9–4.10 printed43/PDF57). It reproduces reported bulk values within1.3%, but original scripts could not be recovered. This is a reconstruction of the original data-reduction operator, not proof of axisymmetry or true net mass flux. The CFD extracts both actual signed cross-sectional flux and a synthetic PIV-method quantity (printed29–31/PDF43–45; printed83–84/PDF97–98). Keep those quantities distinct.

## Governing and reduced equations, conventions and audits

The segmented first-order model has39 radial wall/loss segments plus seven composite fins (§5.1, printed48–56/PDF62–70). It prescribes nearby measured wall temperatures at segment inner boundaries and computes external natural convection/radiation with temperature-dependent layers. It approximates measured outer steel temperature as inner temperature while retaining steel resistance; the author acknowledges this small double count. Fins contribute a reported9–16% of loss in that model (printed55/PDF69); their unmeasured temperatures and solid-core approximation limit physical interpretation. Electrical power plus test-section heating minus cooler, passive and fin losses gives residual unaccounted power (Eq5.7 printed56/PDF70). Closing that residual with effective insulation is calibration, not independent heat-loss measurement.

**Consequential cooler equation error:** Eq5.6 (printed54/PDF68, visually verified) reports \(Q=\dot m[c_p(T_o)T_o-c_p(T_i)T_i]\) and calls it an enthalpy balance superior to mean-cp ΔT. **Analyst thermodynamic check:** for temperature-dependent cp, the sensible enthalpy difference is \(\int_{T_i}^{T_o}c_p(T)\,dT\), not a difference of cp(T)T. Differentiating cp(T)T gives cp+T dcp/dT. For a polynomial \(c_p=\sum a_nT^n\), the exact integral is \(\sum a_n(T_o^{n+1}-T_i^{n+1})/(n+1)\). It reduces to cp ΔT when cp is constant and must be independent of arbitrary temperature reference. The printed formula fails the general check. Code is needed to determine whether this is a reporting or implementation error; do not propagate its superiority claim.

CFD is temperature-dependent low-Mach density formulation: continuity, momentum with \(p_{rgh}=p-\rho\mathbf g\cdot\mathbf r\), and enthalpy/kinetic-energy conservation (Eqs5.8–5.18 printed57–58/PDF71–72). It is described loosely as “incompressible” but retains density variation in continuity and nonzero velocity divergence. Resolve the actual OpenFOAM thermodynamic/flux formulation before reproducing it; neither variable-density retention nor rejection of Boussinesq automatically establishes greater accuracy.

The selected property suite (§5.2.2 printed58/PDF72) uses Kelvin, rho=2293.6−.7497T kg/m³, exponential Jin viscosity (Pa·s), approximately constant cp1423.47J/(kg·K), and Santini k polynomial W/(m·K). Reported density validity470–870K means some lower-temperature cases lie below that stated range. **AppendixB.1 printed111/PDF125 instead lists the older cp≈5806−10.83T+.00724T² and cubic viscosity as properties used in the CFD.** These are materially different. Main text says it replaced them; the input dictionaries are necessary to establish what actually ran. Bibliographic claims that historical source compositions were wrong or new properties superior need original Janz, Jin and Parida evidence. Do not choose a property set from this thesis alone.

Thermal wall condition (Eqs5.23–5.25 printed63–64/PDF77–78) uses an area-normalized cylindrical resistance

\[
R_{ps}=\sum_i r_0\ln(r_i/r_{i-1})/k_i
\quad[\mathrm{m^2 K/W}],
\]

and inner-area heat flux equals outer/inner area ratio times external convection+radiation; \((T_p-T_s)/R_{ps}=q_{out}\). Temperatures in the fourth powers are absolute kelvin. This is a steady radial resistance approximation with explicit area convention, not a dynamic wall-storage or axial-conduction model. Heating/source distributions and convection coefficients must accompany the condition. A network with capacities is required for wall transients if significant.

Fluid boundaries are no-slip, closed-loop pressure reference in the downcomer, gravity(0,−9.81,0)m/s², uniform initial temperature at the measured case mean, initially zero velocity (§5.4–5.5 printed62–66/PDF76–80). Initialization uses experimental temperature; independence requires demonstrating converged equilibria do not depend materially on it. Laminar and transitional k-omega SSTLM with/without a custom buoyancy-production term are assessed. Eq5.19's \(G_b=-C_g\nu_t\mathbf g\cdot\nabla\rho\) (printed60/PDF74) has units of a density-weighted production source; whether a 1/rho is needed depends on which solved k equation receives it. The source cannot be safely copied without that convention and code. Loop-height Ra>10^10 is not a universal turbulence criterion for a confined loop, and fitting a transition closure does not prove physical turbulence (§5.2.3 printed59–60/PDF73–74).

The solver uses pseudo-transient stepping with maximum Courant5 to converge a steady target, explicitly sacrificing temporal accuracy (§5.5 printed64–66/PDF78–80). It is **not evidence for physical startup, instability growth rate, turbulence spectra or resolved transient transport**. Backward time discretization, limited-linear advection, specified linear tolerances and a100-“simulation-second” convergence window are reported; do not interpret that pseudo-time window as an observed physical transient. Solid storage is absent from the radial resistance condition.

## Verification, validation and uncertainty evidence

Code verification tests the custom boundary condition in a simple cylinder with convection-only, radiation-only and mixed cases; four meshes and an analytical/correlation thermal circuit are compared (Ch3 printed21–31/PDF35–45; §6.1 printed72–78/PDF86–92). Finest integrated heat errors are about.062–.067%; Table6.5's flux extrapolation errors about.05–.057%. Small residual differences remain partly because the reference includes a developing-flow correlation, so it is not an exact manufactured solution of the full PDE. The BC test verifies those specified operations/conditions, not every CFD solver component or full-loop closure.

**Full-loop study has two completed refinement levels**, not a demonstrated three-level asymptotic study (§6.2 printed79/PDF93). A larger GCI safety factor3 is used. With only two grids the observed order/asymptotic regime cannot be established from those results; the order assumption and convergence residual must be retained. Geometry itself changes slightly with refinement (AppendixA TableA.4 printed110/PDF124). Main Table3.1 and AppendixA TableA.3 report different bulk-cell targets, another reproducibility ambiguity. Maximum y+ just below5 in part of a transition-model mesh is acknowledged (printed79–80/PDF93–94).

Validation defines E=S−D and uval²=unum²+uinput²+uD² (Eqs3.14–3.15 printed30/PDF44). These require consistent uncertainty levels and dependencies; calibration/derived-data covariance is not automatically zero. GCI estimates are not automatically Gaussian standard uncertainties. An error within that combined band means the comparison cannot distinguish discrepancy at that level; it is not a universal binary validation verdict or proof all local fields are accurate.

Inputs get stated rectangular/Gaussian distributions, geometry/insulation/emissivity/environment bounds (Table5.1 printed67/PDF81); some propagation uses Poiseuille scaling despite acknowledged developing flow and first-order-model sensitivities rather than a full coupled CFD ensemble (printed69–71/PDF83–85). Uncertainty in cooling-air flow is excluded because it was not reported, and insulation conductivity fit uncertainty is omitted despite limited in-range data. Missing uncertainty is not zero. A high polynomial-fit R² on manufacturer points does not justify extrapolation certainty. Effective water insulation thickness.40in was selected after.50in ran too hot (printed68/PDF82), so the subsequent same-case temperature comparison contains calibration information.

**Main table result:** Table6.10 printed95/PDF109 uses the PIV-style operator and mixed chosen closures (water2 SSTLM_Gb, water4 SSTLM; others laminar). Seven states fall within its reported aggregate bands; Salt1 fails: mass error−28.18%, velocity−29.21%, mean centerline temperature−24.43K. Salt4 mass error+9.32% is just within uval9.63%. Water2's selected-model PIV mass band15.17% is much wider than its actual-flux band4.44% (AppendixC TableC.8 printed120/PDF134). Apparent success depends on QoI/operator and uncertainty, not just model fidelity. Best-aligned wall azimuth and temperature means can mask errors at particular probes; Figs6.8–6.12 show notable local variation.

The thesis reports local reverse axial velocity from CFD extending from the lower corner through the riser (Figs6.16–6.20 printed91–94/PDF105–108), and sensor-location sensitivity exceeding10K in some cases (printed85–89/PDF99–103). These are useful **CFD predictions** of this reconstructed facility. Its statement that experimentalists subsequently confirmed recirculation is an author-reported communication (printed92/PDF106), not separately supplied flow-field evidence. No independently validated recirculation volume/length, reverse-flow exchange rate, or causal heat-transfer effect is established by the uploaded record.

The author's exclusion of Salt1 for suspected labeling/configuration problems (§6.5 printed96–97/PDF110–111) is an unresolved hypothesis, not a proven erroneous experiment. TW10 differs by only.36°C between Salt1 andSalt2 in TableC.1, below the stated1.1°C individual instrument uncertainty; nonmonotonicity alone does not prove mislabeling. A mismatch after calibration may arise from data, boundary reconstruction, property choice or model error. Retain Salt1 as a discrepancy case until reconciled. The concluding “99% confidence” statement (printed99/PDF113) is not supported by a demonstrated conversion from the preceding1σ-style comparisons.

## TRIDENT relevance and contribution boundary

**Direct methodological transfer:** require an explicit comparison operator; distinguish cross-sectional net flux from planar magnitude reconstruction; freeze calibration before held-out comparisons; carry geometry/probe-location, heat-input/loss and property uncertainty; separate BC verification from full-loop solution verification and validation. **Conditional physical transfer:** multidimensional stagnant/reverse-flow regions and local probe bias are mechanisms worth testing after geometry and boundary matching. **Analogy:** the TAMU CFD result does not supply TRIDENT CFD fields or a validated glycol/salt model. **Incompatibility:** pseudo-transient steady solutions and algebraic wall resistances cannot establish physical transient stability or wall storage response.

This source already attempts the experiment–CFD/ROM bridge and discusses local recirculation. A feasible TRIDENT contribution should demonstrate what sparse data can identify and what an added model level improves for a specified QoI, with new independent evidence or clearer uncertainty/observation consistency. Generic “first CFD,” “first reduced loss model,” or “first evidence of recirculation in this facility” claims are unsafe. No final method or thesis novelty is selected here.

## Coverage and synthesis readiness

| Section (printed; PDF) | Relevance | Coverage status |
|---|---|---|
| Title/abstract/front matter, PDF1–16 | Identity, indexing, definitions | Inspected; deposit/revision unresolved |
| §1.1–1.2,3–7;17–21 | Motivation and objectives | Read/extracted; outline continuation PDF22–23 not extracted |
| Ch2,10–20;24–34 | Priors/theory/motivation | Read/extracted; cited originals not implicitly read |
| Ch3,21–31;35–45 | V&V definitions and QoIs | Read/extracted |
| Ch4,32–47;46–61 | Geometry, data, property/measurement reconstruction | Read/extracted |
| §5.1–5.3,48–62;62–76 | Loss model, PDEs, properties, mesh | Read/extracted; exact code absent |
| §5.4–5.7,62–71;76–85 | BCs, iteration, inputs/UQ | Read/extracted; selected equation checked visually |
| §6.1–6.3,72–84;86–98 | BC verification, two-grid loop uncertainty | Read/extracted; no independent run reproduction |
| §6.4–6.5,84–97;98–111 | Validation and discrepancy | Read/extracted; selected temperature/flow plots and Table6.10 visually checked |
| Ch7,98–99;112–113 | Stated scope/future work | Read/extracted |
| Bibliography,100–106;114–120 | Source provenance | Inspected; errors/incomplete entries retained as leads |
| AppendixA,107–110;121–124 | Geometry/mesh inputs | Read/extracted; main/appendix target mismatch flagged |
| AppendixB,111–114;125–128 | Exact property definitions | Read/extracted; salt-property conflict flagged |
| AppendixC,115–125;129–139 | Experimental values, closure-specific uncertainty/plots | Tables/captions read/extracted; additional plots not digitized or independently recomputed |
| Source code/run manifest/raw data | Reproduction | Not supplied; inaccessible in this batch |

Ready for **qualified V&V-method comparison, observation/energy-accounting lessons, and identifying existing CFD prior work**. Not ready as a trusted synthetic training dataset, a validated local-recirculation truth, a final property prescription, or a physical transient benchmark without code/version/input reconciliation and independent checks.

## Stable claim ledger

| Claim ID | Claim/type | Locator | Scope/limit |
|---|---|---|---|
| S35-C01 | Retrospective modeled TAMU geometry and losses require reconstruction/calibration (reported method) | §4.1,5.1,5.7; printed33–35,48–56,67–71/PDF47–49,62–70,81–85 | No untouched validation partition |
| S35-C02 | Water PIV profiles digitized; salt raw profiles available to author (data provenance) | printed43–47/PDF57–61,Eqs4.9–4.11 | Not independent new experiments |
| S35-C03 | Cylindrical multilayer Robin condition with area convention (original implementation) | printed63–64/PDF77–78,Eqs5.23–5.25 | Steady radial resistance, no wall storage |
| S35-C04 | Full-loop refinement uses two completed levels (reported limitation) | printed79/PDF93,§6.2 | BC four-grid study does not establish full-loop order |
| S35-C05 | Pseudo-transient stepping sacrifices physical temporal accuracy (reported assumption) | printed64–66/PDF78–80,§5.5 | Steady targets only |
| S35-C06 | Seven aggregate PIV-style comparisons inside reported bands; Salt1 fails (original table result) | printed95/PDF109,Table6.10 | Calibrated inputs, chosen closures/operators, mean metrics |
| S35-C07 | Local reverse axial flow and point-temperature sensitivity predicted (original CFD result) | printed85–94/PDF99–108,Figs6.10–6.20 | Local fields not independently validated |
| S35-C08 | cp(T)T difference is not general sensible enthalpy (analyst equation audit) | printed54/PDF68,Eq5.6 | Need source code to distinguish print/implementation error |
| S35-C09 | Main and AppendixB salt-property sets disagree (source audit) | printed58 vs111/PDF72 vs125 | Cannot identify final run properties from prose alone |
| S35-C10 | Salt1 labeling-failure explanation remains unproved (critical appraisal) | printed96/PDF110,§6.5; TableC.1 printed116/PDF130 | Keep discrepancy and alternatives |

## Follow-up requests

Highest value: final revised thesis plus the exact input/property dictionaries, wall-BC implementation, cooler enthalpy calculation, uncertainty script and case/model selection record. Raw water-PIV recovery cannot be assumed; request original publication numerical data if they exist, otherwise preserve digitization limitations. For physical-property claims acquire/read original Janz/INL, Jin2016 DOI10.1016/j.solener.2016.08.037 and Parida–Basu2023 DOI10.1039/D2RA07384F before deciding among property laws. These are source leads, not endorsed replacement properties.
