# S66 — Cammi, Luzzi and Pini (2016): wall inertia and internally heated loops

## Bibliographic identity and completeness

A. Cammi, L. Luzzi and A. Pini, “The influence of the wall thermal inertia over a single-phase natural convection loop with internally heated fluids,” *Chemical Engineering Science*153,411–433. DOI:https://doi.org/10.1016/j.ces.2016.06.060. Supplied Elsevier publication PDF23 consecutive pages, PDF n=printed n+410. Main text, AppendicesA/B, Tables1–8 and references are present. All main-text sections were text-inspected. Appendix formulas/tables were mapped and inspected for role, **not independently verified or completely transcribed**. Critical PDF3,5,6,8 were rendered/visually checked; other plots were assessed through text/captions, not digitized. No separate supplement identified.

Ready for scoped wall/source/stability synthesis. Not ready as a complete implementation of the appendix dispersion relation. Original questions: A3–A4 source/similarity, C physical states/closures/reduction, G numerical verification/UQ, transient QoIs.

## Problem, strongest prior work and established contribution

The authors analyze wall density, heat capacity and radial conductivity effects in a natural-circulation loop with localized external heating, distributed fluid heating, or both. A two-shell wall model enters linear stability analysis and nonlinear simulations; Modelica, RELAP5 and conjugate CFD results are compared. Distributed external wall heating is also considered as a possible substitute for difficult-to-create internal generation.

The introduction explicitly cites earlier wall-capacity/conductivity work and earlier internally heated-loop analyses (PDF1–3/411–413). Thus “wall inertia affects loop stability,” “use a conjugate loop ROM,” and “compare external and internal heating” are established topics before TRIDENT. The paper develops a particular combined analysis, not the first wall-aware loop model.

## Geometry, operating conditions and instrumentation

Generic derivation: constant circular bore, constant wall thickness, rectangular closed loop. Coordinate s increases clockwise from cooler entrance. G=ρu is **mass flux**,kg m^-2 s^-1, not mass flow. Fluid source q''' is homogeneous and distributed, including the cooler; external q'' acts on a heater segment. The cooler outer wall is held at Tc; the other outer walls are adiabatic except where heated (Fig1,§2.1,PDF3–4/413–414).

Applied HHHC example Table1/Fig4,PDF8/418:

| Quantity | Reported value | Qualification |
|---|---|---|
| Total length Lt |7.24m| Sum of reported segments |
| Cooler length Lc |.80m| Prescribed outer-wall temperature |
| Heater length Lh |.62m| Localized-heater case |
| Wall thickness |.001m| Reference case |
| Cooler temperature |303.15K| Imposed boundary |
| Bore Df |**.00269m in Table1**| Internal consistency issue below |

**Do not silently correct the diameter:** §6.1 uses Lt/Df=269.1, which with Lt=7.24m implies Df≈.0269m, ten times Table1. Table1's .00269m was visually verified. The ratio is model-derived cross-checking, not a replacement measurement. Any reproduction must resolve the intended geometry.

Table2,PDF8/418 gives properties at300K: AISI316(ρ8238kg/m³,cp468J/kg/K,k13.4W/m/K), aluminium(2702,903,237), copper(8933,385,401). These are reported model inputs, not TRIDENT fitted properties. Generic artificial fluid-property combinations are also used to explore the Re–Stability plane. No new instrumented experimental campaign or sensor uncertainty is reported.

## Governing equations, states and closures

Fluid assumptions: incompressible one-dimensional Boussinesq, common flow regime around the loop, negligible axial thermal diffusion and viscous heating, constant properties in the analytical treatment. Wall assumptions: two coaxial radially lumped shells with separate storage, radial conduction coupling, no axial wall conduction or ambient thermal loss (PDF3/413).

Eqs.(1)–(5),PDF3–4/413–414 specify fluid momentum/energy and inner/outer wall energy. Eq.(6) defines geometry/radial resistance; exact shell conventions should be retained before implementation. Eq.(7) uses **Darcy** λ=a/Re^b; equivalent length represents localized losses. Linearization fixes the friction-law coefficients within the selected regime.

Steady profiles, Eqs.(8)–(31), preserve periodicity. The source split is
\[
\alpha=\Delta T_{q''}/\Delta T_0,\qquad
\Delta T_0=\Delta T_{q''}+\Delta T_{q'''}.
\]
Reported Eqs.(23)–(26),PDF5/415, visually checked. Crucially \(\Delta T_{q'''}=q'''(L_t-L_c)/(G_0c_f)\). Thus α uses generation **outside the cooler**, and is not automatically external watts divided by all generated watts including the cooler. Source-power fractions must be derived using their actual domains/areas.

Perturbations are proportional to exp(ωt), Eq.(40),PDF6/416; complex ω is a growth/eigenvalue parameter, not only an oscillation frequency. Dimensionless Eq.(41) uses fluid-to-wall ratios \(\bar\rho=\rho_f/\rho_w,\bar c=c_f/c_w,\bar k=k_f/k_w\). Therefore \(\bar C=\bar\rho\bar c\) is a **fluid/wall volumetric-capacity ratio**. With fixed fluid, smaller Cbar corresponds to greater relative wall capacity.

The flow sensitivity of heat transfer is retained:
\[
B=\frac{G_0}{h_0}\left.\frac{\partial h}{\partial G}\right|_0
=\frac{\mathrm{Re}_0}{\mathrm{Nu}_0}
\left.\frac{\partial\mathrm{Nu}}{\partial\mathrm{Re}}\right|_0.
\]
Eq.(46),PDF6/416, visually checked. B is dimensionless. A model's steady h value and its flow derivative are separate requirements for transient stability. Correlation blending is given in Eqs.(47)–(48); this is not evidence for one universally valid closure in TRIDENT's actual envelope.

## Stability and numerical comparison

AppendixA gives sectional temperature-perturbation solutions and auxiliary tables; AppendixB integrates buoyancy perturbations to form the characteristic/dispersion relation. MATLAB root-solving is used for the linear boundary. These analytical appendices must be audited separately before coding, especially given geometry and normalization ambiguities.

The nonlinear O-O classifier labels a run unstable when variance in its last10% divided by whole-record variance exceeds10^-3 (§3.4,PDF7–8/417–418). This is a selected finite-window diagnostic, not a rigorous stability certificate or universal threshold. Window length and near-zero variance can affect interpretation.

Modelica uses an extended ThermoPower formulation; RELAP5 uses heat structures and fluid internal heating; OpenFOAM2.3.1 uses conjugate regions and laminar transient simulations (§5,PDF8–11/418–421). The expansion-tank representation is a pressure boundary rather than a qualified finite-inventory thermal tank model. The CFD is intentionally laminar and should not be presented as evidence across arbitrary turbulent states.

Reported spatial checks use changes in mass flux: under1% for selected1D grids, a few percent for CFD refinement, and under2% steady CFD–RELAP discrepancy at1000W for source endpoints (§5). Those are specific bulk-flow checks, not uncertainty estimates for local maxima or instability statistics. The equation-of-state description in §5.3 is incomplete in the supplied prose.

At200W and1000W the paper compares transient mass flux and model-predicted stable/unstable regimes (Figs17–21,PDF15–17/425–427). Different startup initialization and numerical diffusion can change individual pulses. These are **code-to-code comparisons**, not independent experimental validation. The conclusion explicitly says experimental validation remains future work (PDF18/428).

## Results and MSR transfer

Changing individual wall properties can shrink unstable regions; combined real-material effects can instead enlarge some unstable regions (§6.1;conclusion PDF17/427). “Wall inertia always stabilizes” overstates the result. Wall material affects transient delay/response, particularly unstable cases (§§6.2–6.3).

The alternative external-heating case distributes wall flux around the loop **except the cooler**, rather than using only one localized heater (Eqs61–62,Fig13,PDF12/422). The authors find similar stability behavior to uniform internal heating for a large length/diameter case, with differences at highRe and because the external case has no cooler source. Frequency responses and wall-source pathways also differ (§6.2,Fig15,PDF12–14/422–424).

This is conditional evidence that a carefully chosen distributed wall-source experiment can approximate selected internally heated-loop stability behavior. It does not prove equal local temperatures, wall stresses, startup response, field extrema or neutron-coupled reactor dynamics. A single localized electric heater is a different source case.

## Claim-to-evidence table

| ID | Finding | Locator | Qualification |
|---|---|---|---|
| S66-C01 | Separate inner/outer wall capacities and radial conduction are established loop-model states. | §2.1,Eqs1–6,PDF3–4/413–414 | Specific lumping and excluded axial conduction/loss. |
| S66-C02 | Constant outer-cooler temperature and uniform distributed fluid heating define the reference source/boundary problem. | §2.1,Fig1,PDF3/413 | Not TRIDENT secondary-loop equivalence. |
| S66-C03 | α is a temperature-rise split using internal heating outside the cooler. | Eqs23–26,PDF5/415 | Not automatically total-power fraction. |
| S66-C04 | The nondimensional capacity ratio is fluid/wall; h's flow derivative enters stability. | Eqs41,46,PDF6/416 | Ratio direction and derivative matter. |
| S66-C05 | Table1 diameter conflicts by a factor of ten with the stated length/diameter ratio. | Table1,PDF8/418;§6.1 | Printed value visually checked; intended input unresolved. |
| S66-C06 | Real-material combinations can enlarge unstable regions despite stabilizing isolated-property trends. | §6.1;§7,PDF17/427 | Reject universal stabilization claim. |
| S66-C07 | Distributed external heating can approximate internal-heating stability in the analyzed long/slender case. | Eqs61–62,Fig13,PDF12/422;§7,PDF18/428 | Conditional source/layout/QoI transfer. |
| S66-C08 | Nonlinear stability labels use a finite-window variance ratio with threshold10^-3. | §3.4,PDF7–8/417–418 | Numerical diagnostic, not proof. |
| S66-C09 | Agreement among O-O/RELAP/CFD is code comparison; experimental validation is explicitly future work. | §6.3,Fig21,PDF14–17;§7,PDF18/428 | No new measurement-based validation/UQ. |
| S66-C10 | Three-dimensional comparison deliberately uses laminar CFD. | §5.3,PDF10–11/420–421 | No universal turbulent validation. |

## Coverage checklist and synthesis readiness

| Section/appendix | Status | Remaining work |
|---|---|---|
| §1 PDF1–3 | Inspected/extracted | Earlier cited wall papers not all independently acquired |
| §2 PDF3–6 | Inspected/extracted;selected equations visually checked | Full coefficient transcription/rederivation deferred |
| §3 PDF6–8 | Inspected/extracted | Root search and classifier sensitivity not reproduced |
| §4 PDF8 | Inspected/extracted;geometry tables visually checked | Diameter unresolved |
| §5 PDF8–11 | Inspected/extracted | Executed decks/code not acquired |
| §6 PDF11–17 | Inspected/extracted via text/captions | Figures not exhaustively digitized; spectral/mesh results not rerun |
| §7 PDF17–18 | Inspected/extracted | Explicit future validation retained |
| AppendixA PDF18–21 | Mapped/selected inspected; not fully extracted | Long auxiliary expressions not independently audited |
| AppendixB PDF21–22 | Mapped/selected inspected; not fully extracted | Buoyancy-integral algebra not independently audited |
| References PDF22–23 | Inspected for discovery | Cited originals not assumed read |

For Codex: compare a conservative fluid/wall hierarchy, preserve source deposition and h/Re derivative conventions, resolve geometry before reproduction. For the proposal: use this as a strong prior-art challenge and a qualified external/internal-source analogy. S65, already available, is the next internally heated-loop comparator; S18 the conjugate reduction comparator. No immediate user upload is needed.
