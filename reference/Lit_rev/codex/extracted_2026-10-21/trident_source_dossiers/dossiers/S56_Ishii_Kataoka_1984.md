# S56 — Ishii and Kataoka (1984): similarity and limits of loop representation

Extraction2026-10-20. M. Ishii, I. Kataoka, *Scaling laws for thermal-hydraulic system under single phase and two-phase natural circulation*, Nuclear Engineering and Design81(3),411–425. DOI https://doi.org/10.1016/0029-5493(84)90287-5.

## Identity and coverage

Supplied publisher scan,15 continuous PDF pages; printed page=PDF page+410. Title/authors/year/venue match verified DOI metadata. Text is readable but OCR corrupts symbols, exponents and subscripts. PDF3–6 were visually checked for the single-phase groups/scaling laws. Numerical transcription below is limited to those checked definitions. No appendix/supplement in supplied article; no experiment data or implementation acquired.

Relevant single-phase §2 fully inspected, including sample LOFT comparison. Introduction, conclusion and nomenclature inspected. §3 two-phase derivation was screened for scope; PDF8–12 detailed drift-flux/CHF derivations were **not fully read or extracted**. Their criteria are not imported into TRIDENT.

## Problem, contribution and engineering context

Natural circulation couples the integrated buoyant head to heat transport throughout a circuit. The paper derives similarity requirements from 1D area-averaged fluid balances, solid energy and interface conditions, then examines a LOFT/PWR example (§§1–2). It is a theory/scaling paper, not a new molten-salt experimental validation campaign.

Earlier liquid-metal scaling and two-phase work are cited as prior foundations; those originals are not read by reading S56. Its application is primarily water-reactor natural-circulation/decay-heat simulation. Transfer to a salt/glycol loop is conditional on retaining the relevant physics and satisfying or explicitly quantifying distortions.

## Assumptions and reported mathematics

§2.1/Eqs1–11, PDF2–3 / 412–413: incompressible Boussinesq fluid; spatially varying areas with one representative flow; loop-integral momentum; fluid advection and wall exchange; solid conduction normal to flow. The conclusion explicitly states axial solid conduction is neglected (§4, PDF13 / 423). No separate ambient/insulation/tank model is established by these equations. The solid carries the source; volumetric heat generated in circulating fuel is a different deposition mechanism.

Let l0 be reference axial length, u0 reference velocity, DeltaT0 reference temperature rise, ai fluid cross-sectional area, asi solid cross-sectional area, zeta_i wetted perimeter, di hydraulic diameter, delta_i conduction depth. Eq12 (PDF3 / 413) gives:

\[
R={g\beta\Delta T_0l_0\over u_0^2},\quad
F_i={f_i l_i\over d_i}+K_i,\quad
St_i={4h_i l_0\over \rho c_p u_0d_i},
\]
\[
T_i^*={\alpha_{s,i}l_0\over\delta_i^2u_0},\quad
B_i={h_i\delta_i\over k_{s,i}},\quad
Q_{s,i}={\dot q_{s,i}l_0\over\rho_s c_{p,s}u_0\Delta T_0}.
\]

Here qdot_s is **volumetric solid heat generation**, W/m³, and alpha_s solid diffusivity, m²/s. Each group is dimensionless with SI inputs. \(T_i^*=(l_0/u_0)/(\delta_i^2/\alpha_s)\) is transport time divided by solid conduction time. It is not a temperature or an absolute time.

Eqs13–16 define axial ratios Li=li/l0, area ratios Ai=ai/a0, di=4ai/zeta_i and delta_i=asi/zeta_i. For a cylindrical wall, delta is an area/perimeter equivalent depth, **not automatically the physical radial wall thickness**. Applying thin-wall approximations must be declared.

§2.2/Eqs20–35, PDF4–5: a convenient subsequent derivation assumes **same solid materials** between model and prototype, with geometrical restrictions. Under those conditions Stanton similarity is redundant given the other matched groups. Do not generalize that redundancy to arbitrary different solids, heating arrangements or missing physics.

Reference velocity/temperature scales are coupled through steady balances. Matching a selectable Prandtl number does not independently ensure these scales, area distributions, losses or solid time scales match. Source claims that orifices can adjust aggregate friction assume an available adjustable design; they do not authorize changing TRIDENT.

## Heat-transfer and time-scale limitations

§2.2/Eqs36–41, PDF5 / 415: h depends on the regime and constitutive relation. The illustrative turbulent correlation has stated1<Pr<20; it must not be applied to all high-Pr oil/glycol regimes. Fully developed laminar Nu4.36 is an illustrative closure with a particular boundary condition, not a general local mixed-convection rule.

§2.3/Eqs42–59, PDF5–6 / 415–416: same-fluid/same-solid restrictions simplify the scale relations. The time scale obeys \(t_R=l_R/u_R\), Eq56. “Real time” additionally requires tR=1; under the paper's assumptions this restricts source and diameter/conduction-depth scales. Reduced geometry does not imply time histories can be transferred without rescaling.

The authors argue Biot/Stanton mismatch may weakly affect **slow system-level** single-phase response, while boundary-layer drops and rapid transients may be distorted (PDF6–7 / 416–417). That is a conditional approximation, not a bound. It cannot justify neglecting mismatch when the target is wall temperature, local heat transfer, freeze margin or rapid response.

## Results, evidence and limits

§2.4/Table1/Figs2–3 (PDF6–7 / 416–417) compares CE System80 and LOFT geometry and argues approximate feasibility with modifications. This is a preliminary engineering scaling assessment, not newly reported matched time-series validation. §4 (PDF13–14) explicitly calls for more detailed analysis before modifications/program design.

No systematic uncertainty propagation, fitted parameter posterior, experimental holdout, quantitative distortion-to-QoI error bound or calibration/validation split is provided for a TRIDENT-like facility. The two-phase/CHF discussion concerns boiling/dryout mechanisms. It does **not** make critical heat flux an appropriate primary limit for our intended single-phase TRIDENT scope.

## Claim-to-evidence table

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S56-C01 | Single-phase similarity includes fluid, solid and interface physics | §2.1/Eqs1–16, PDF2–3 / 412–413 | 1D/Boussinesq; axial solid conduction omitted |
| S56-C02 | Pr matching alone is insufficient for general loop similarity | §§2.1–2.2/Eqs12–35, PDF3–5 | Our direct synthesis of the required groups |
| S56-C03 | h-dependent similarity is regime-sensitive and difficult to satisfy | §2.2/Eqs36–41, PDF5 / 415 | Illustrative correlations, not modern universal closures |
| S56-C04 | Relaxing Biot/Stanton has a target/time-scale qualification | §2.3, PDF6–7 / 416–417 | Not permission to ignore wall/local errors |
| S56-C05 | Transport/conduction and clock scaling differ from simple geometric scale | Eq12/Eqs56–59, PDF3/6 | Conditional same-material/fluid simplifications |
| S56-C06 | LOFT application is preliminary feasibility, not new matched-data validation | §2.4/§4, PDF6–7/13–14 | Fluid/geometry application differs from TRIDENT |
| S56-C07 | CHF is a separate two-phase scope | §1/§3/§4, PDF1–2/7–14 | Detailed two-phase derivations not extracted |

## Application and next work

For each TRIDENT-to-reactor claim, build a matrix of geometry, properties, source distribution, boundary conditions, area/loss distribution, and fluid/solid time scales. Classify a claim as direct facility prediction, conditional quantitative scaling, mechanism analogy or incompatible. The **criterion and quantified consequences of distortion for a declared QoI** may be a contribution hypothesis; dimensionless-group calculation alone is established work.

Read S64 Bardet–Peterson and existing S15 for salt-surrogate options; S65/S66 for internal heating and solid inertia. Their unread contents must not be inferred from S56.

| Coverage | Status | Reason |
|---|---|---|
| §1 | Inspected/extracted | Engineering motivation/scope |
| §2.1–2.4/Eqs1–61/Table1 | Inspected/extracted; PDF3–6 visual checks | Primary single-phase relevance |
| §3 detailed two-phase derivations | Screened, largely skipped | Outside approved single-phase model scope |
| §4/nomenclature/references | Inspected/selectively extracted | Conclusions/definitions; cited originals remain unread |

Ready for **single-phase similarity and transfer-limit synthesis**. Not a certified scaling design for TRIDENT or a two-phase/CHF dossier.
