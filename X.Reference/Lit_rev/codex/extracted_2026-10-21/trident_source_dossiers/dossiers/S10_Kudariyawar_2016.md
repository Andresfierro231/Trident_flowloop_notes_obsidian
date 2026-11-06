# S10 — Kudariyawar et al. (2016): experiment/CFD steady and transient salt loop

Audit date20 October2026. **Ready for scoped motivation, closest-prior-work and retained-physics synthesis. Not cleared for literal reproduction of operating limits or boundary coefficients.**

## Identity, version and coverage

Jayaraj Yallappa Kudariyawar, Abhishek Kumar Srivastava, Abhijeet Mohan Vaidya, Naresh Kumar Maheshwari, Polepalle Satyamurthy, “Computational and experimental investigation of steady state and transient characteristics of molten salt natural circulation loop,” *Applied Thermal Engineering*99(2016),560–571, [DOI10.1016/j.applthermaleng.2015.12.114](https://doi.org/10.1016/j.applthermaleng.2015.12.114). Uploaded12-page publisher-formatted PDF; metadata, title, authors, journal and DOI agree. Accepted22 December2015; online29 January2016. Printed page=PDF+559. Body, Tables1–3, Figs1–22 and references are present. All body text and relevant references were inspected, with figure overviews and selected high-resolution checks. No external supplement, raw temperature histories, solver case files or uncertainty budget was supplied; no separate supplement is clearly identified in the inspected article. Publisher retrieval was blocked, but the uploaded full text resolves the former acquisition request.

## Problem, contribution and prior work

The paper studies an electrically heated nitrate-salt natural-circulation loop with steady conditions and startup, power-increase, power-decrease, heater-trip and loss-of-sink transients. Its advance over the authors' earlier CFD treatment is inclusion of the cooler air duct instead of only a prescribed overall heat-transfer coefficient, additional transients and comparisons with measured temperatures (§1,PDF3/562). Earlier water-loop validation and earlier salt-loop calculations are cited evidence, not independently read here. In particular, the current paper does not reproduce a salt startup-flow experiment merely by citing the earlier water result (§6.2.1,PDF7/566).

This is strong prior art against claiming that a salt-loop experiment–CFD transient framework, heat-loss treatment, operating-temperature assessment or expansion-tank enrichment is itself new. Its generic statement that an NCL represents a reactor heat-transport system is motivation, not a demonstrated similarity proof for a specific MSR.

## Facility, fluids and conditions

| Item | Reported evidence and locator |
|---|---|
| Salt | Solar salt, NaNO₃/KNO₃60:40 by mass; no fuel. Intro/§2,PDF1,3/560,562. |
| Geometry | Rectangular loop, tube ID13.88 mm, OD21.34 mm; Inconel625 solid included in CFD; expansion tank at top. Fig1/PDF2/561 gives dimensions. §2/PDF3/562. |
| Source/sink | Nichrome wire wound outside pipe; selectable heater/cooler arrangements, studied results mainly vertical heater/horizontal cooler. Cooler air annulus ID21.34 mm/OD102 mm. External heating is not volumetric fission heating. §2. |
| Measurements | Fluid and surface K-type thermocouples; stated TC accuracy±0.4% reading, transmitter±0.1% range. Counts, installation response, timing, run-to-run repeatability and full joint uncertainty are not sufficiently specified for reconstruction. Fig1/§2. |
| CFD properties | Polynomials are presented, but the authors explicitly evaluate properties at300°C and use the resulting constants, with Boussinesq buoyancy. Tables1–2/§3.4,PDF4/563. Do not describe this as fully temperature-dependent property simulation. |
| Boundary conditions | Outer heater heat flux; ambient-exchange coefficients5 and12 W/(m² K) on the two connecting paths, derived empirically using measured surface temperatures. Insulation represented by effective resistance, not an explicit thermal-storage region. Air inlet mass flow0.02 kg/s except the loss-of-sink event; inlet air temperature prescribed but its numerical value is not given in the inspected text. §§3.1,3.5,PDF3–4/562–563. |
| Initial condition | Startup stagnant at300°C; subsequent transitions start from previous steady solutions. §3.6,PDF4/563. |
| Studied conditions | Main steady figure spans1200–2000 W; computed Reynolds numbers are roughly350–410 in Fig9, read as a plot range, not a digitized dataset. Specified step cases and other power-limit simulations are separate. PDF7/566. Pr is not tabulated; no observed dimensionless range is invented. |

The lumped property values in Table2 areρ1899.2 kg/m³, k0.501 W/(m K), cp1494.6 J/(kg K), μ3.26×10⁻³ Pa s. Eq1 takes T in kelvin and uses T−273.15 in the polynomials. **Viscosity coefficients in Table1 produce mPa s, whereas Table2 uses Pa s.** Preserve that conversion. Property provenance is cited Nissen/Ferri; these originals require separate evaluation before broad-range use.

## Governing/numerical treatment and verification

FLUENT solves3D laminar momentum and thermal transport with gravity, Boussinesq density and conjugate pipe conduction; power-law convection/diffusion and SIMPLE are reported (§3.3–3.4,PDF3–4/562–563). Full conservation equations, solid-property functions, radiation allocation, solver residual criteria, inlet-air numerical temperature and case-specific tank boundaries are not supplied in enough detail for faithful replication.

Spatial tests compare butterfly cross-section grids and axial distributions;11×11×5×499 is selected, about301895 nominal cells under the described count (**analyst multiplication**, not a reported complete primary+air+solid cell count). Axial descriptions contain1368/1369 variants. Comparison with an analytical fully developed laminar pipe profile atRe500 is an additional solution check (§4,PDF5–6/564–565). This checks that benchmark, not every local-loop QoI.

Time-step comparison uses0.1,0.5,1,2.5,5 s and selects0.1 s (§5,PDF6–7/565–566). No smaller-step reference, formal observed-order/GCI result or propagated numerical uncertainty is reported. The text/caption uses VHVC at one point while other descriptions refer to VHHC; identify the actual verification case before transfer. These are useful sensitivity checks, not a complete local-extrema verification budget.

## Results and appraisal

- Steady and transient **temperature** comparisons are shown in Figs8,13–21 (PDF7–11/566–570). The paper calls agreement excellent, but provides no RMSE table, joint experimental prediction bands or preregistered calibration/selection/test split. Surface-informed loss coefficients limit a claim that every boundary input was independent of comparison data.
- Power rises1500→1600,1600→1700 and1800→2000 W, and decreases2000→1800→1600→1400 W, are reported (§6.2.2–3,PDF8/567; Figs13–18). Smooth transitions in these cases do not prove global stability over arbitrary conditions.
- The step-back discussion says the expansion tank was **not** included in those simulations, despite the general-domain description mentioning it. Heater-trip simulations compare with/without tank; including it improves the heater-outlet cooling comparison (PDF8–9/567–568; Fig20,PDF11/570). This is explicit case-dependent model enrichment, not one uniformly documented tank treatment.
- Heater-trip: power2000→0 while cooler remains active; heating is restored as temperatures approach the study's lower operating range (§6.2.4,PDF9/568). Zero external heater duty is not reactor scram with decay heat.
- Loss of sink: forced cooler air flow is stopped after a1500 W steady state; temperatures and simulated flow are discussed (§6.2.5,PDF9–11/568–570). Stopping forced air does not prove zero total ambient heat loss. The phrase “without getting rejected anywhere else” should not replace an audited balance when external losses are otherwise included.
- Table3 (PDF8/567) gives950 W:237.5/289.2°C minimum/maximum;2500 W:463.1/567.3°C. Text then suggests1000–2500 W, while conclusions say1200–2500 W and elsewhere call2000 W the maximum permissible value. **These are inconsistent reported limits, not a verified TRIDENT envelope.** A single-phase solution below the cited238°C melting point signals model invalidity/risk, not a simulated solidification/blockage result.

The comparisons primarily assess temperature; mass-flow/Re histories in the salt startup and loss-of-sink figures are computed. No independently measured salt-flow uncertainty is established in the inspected paper. An excellent-looking temperature match cannot independently validate an unmeasured flow field.

## Implications for TRIDENT and implementation

Direct methodological relevance: define source/sink and observation boundaries; account for expansion-tank and solid participation; test independent physical cases; verify the actual QoI. Conditional transfer: buoyancy–resistance feedback, external-loss and conjugate-storage mechanisms. Analogy only: numeric5/12 W/(m² K), constant300°C properties and power bounds. Incompatible: direct glycol→salt or test-loop→full-reactor validation.

A fair minimal comparator includes1D/conservative regional storage versus the same model enriched by tank/wall participation. Select enrichment on training/selection cases, then assess untouched transitions and duty/temperature QoIs. Do not borrow the paper's values to explain TRIDENT discrepancies without facility evidence.

Acquire/read next: the related Srivastava et al.2016 experiment/1D study (S50, DOI10.1016/j.applthermaleng.2015.12.065) for the closest lower-order comparator and overlapping dataset provenance; Ferri et al.2008 property treatment if adopting solar-salt functions; the cited earlier2015 CFD study for what was already established. Citing S10 does not mean those originals were read.

## Coverage checklist and claims

| Component | Coverage | Remaining limitation |
|---|---|---|
| Identity/§1 | Inspected/extracted | Historical/application examples are cited background |
| §2/§3 | Inspected/extracted; selected visual checks | Actual raw calibration/BC/case files unavailable |
| §§4–5/Figs2–7 | Inspected/extracted | No independent convergence study or plot digitization |
| §6/Figs8–22/Tables1–3 | Inspected/extracted | No raw data/full joint UQ or independent salt-flow truth |
| §7/references | Inspected/traced selectively | Related originals not presumed read |
| External raw data/code/supplements | Not supplied | No execution/reproduction claim |

| Claim ID | Claim | Locator | Qualification |
|---|---|---|---|
| S10-C01 | Salt-loop steady/transient experiment–CFD comparison precedes TRIDENT | §§1,6,7; PDF3,6–11/562,565–570 | Main measured comparisons are temperatures |
| S10-C02 | Presented property polynomials were evaluated at300°C for these simulations | §3.4/Tables1–2,PDF4/563 | Not full temperature-dependent transport |
| S10-C03 | Effective loss BCs use empirical surface-temperature information | §3.5,PDF4/563 | Calibration independence/uncertainty not fully specified |
| S10-C04 | Expansion-tank participation materially changes heater-trip prediction | §6.2.3–4/Fig20,PDF8–9,11/567–568,570 | Case-dependent geometry treatment |
| S10-C05 | Spatial/time checks are useful but do not quantify every QoI's numerical uncertainty | §§4–5,PDF5–7/564–566 | No formal error estimate or smaller-than0.1 s reference |
| S10-C06 | Published operating-power statements disagree | Table3/§6.1.1/§7,PDF6–8,11/565–567,570 | Do not import as a validated envelope |
| S10-C07 | Trip/loss-of-forced-air tests are limited system analogies | §6.2.4–5,PDF8–11/567–570 | Neither decay-heat physics nor zero ambient loss established |
