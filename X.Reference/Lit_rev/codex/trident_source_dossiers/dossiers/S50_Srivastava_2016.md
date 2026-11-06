# S50 — Srivastava et al. (2016): experimental and 1D molten-salt loop comparator

Extraction date: 2026-10-20. Scope: original prompt A1–A4, B1–B5 and physical-model, loss/storage, observation, validation and UQ questions. Claim IDs S50-C01–C08 are permanent.

## Identity and coverage

A.K. Srivastava, Jayaraj Y. Kudariyawar, A. Borgohain, S.S. Jana, N.K. Maheshwari, P.K. Vijayan, *Experimental and theoretical studies on the natural circulation behavior of molten salt loop*, Applied Thermal Engineering 98 (2016), 513–521. DOI: https://doi.org/10.1016/j.applthermaleng.2015.12.065. Uploaded publisher article: nine continuous pages; PDF page + 512 = printed page. Online 30 December 2015 is distinct from the 2016 volume date. Title/authors/DOI match the publisher discovery record. No supplementary material supplied or identified in the inspected article; absence elsewhere not established.

All main sections, nomenclature and references were inspected in extracted text; PDF pp. 5–8 additionally inspected visually for equations, tables and result figures. No raw data or LeBENC implementation acquired. The separate referenced formulation was not read through this paper.

## What was established and why this loop exists

The authors built a nitrate-salt facility for thermal hydraulics, operating experience, high-temperature instrumentation and material-related work. Their introduction connects it to BARC high-temperature-reactor and solar-power developments; it does not establish geometric/dynamic similarity to an arbitrary liquid-fuel MSR. The reported experiment supplies steady temperature responses, startup, power-step, forced-air interruption and heater-trip comparisons with LeBENC.

Earlier instability, orientation and scaling results are attributed to Welander, Creveling, Vijayan and others (§1, PDF pp. 1–2 / 513–514); these are cited prior work, not new findings of S50. The generic 1D formulation is referred to Borgohain et al. (2011), reference 24, rather than reproduced.

## Facility, observations and experiment contract

Tables 1–4, Figs. 1–3; PDF pp. 2–6 / 514–518:

- NaNO3/KNO3, 60:40 by mass; Inconel 625, nominal 15 mm NB SCH80; total circulation length 6.8 m. Four orientations are possible; this article reports vertical heater/horizontal cooler. Table 1 gives effective elevation 1.3 m for that orientation.
- External electric heating, ceramic insulation, tube-in-tube air cooler, partially filled expansion tank and argon cover gas. Main heater maximum in this experiment 2 kW; stated upper operating temperature 580°C. Those are this facility's stated limits, not TRIDENT limits.
- K-type temperature accuracy ±0.4% of reading; transmitter ±0.1% of range; DACS ±0.165% of range; gas-pressure transmitter ±0.1% of range. These component specifications do not constitute a propagated covariance-aware measurement uncertainty.
- Some fluid probes and many surface probes; exact sensing/averaging errors and response-time corrections not quantified. No independently qualified primary-salt flow measurement/reduction procedure is documented for Fig. 5's “experimental” Reynolds numbers. Do not certify that graph as independent flow truth.
- Air flow 0.02 kg/s before interruption. Table 4: 1200→1500 W, 1500→1600 W; loss of forced air from 1500 W; 2000→0 W heater trip. Transients were mitigated to maintain a stated 300–580°C safe range (§4). Long-term accident completion is not demonstrated.

## Model and mathematics audit

LeBENC is described as finite-difference, 1D mass/momentum/fluid-energy/solid-conduction modelling with Boussinesq buoyancy, axial fluid/wall conduction, losses and trace heating (§3, PDF p. 3 / 515). The complete PDEs, friction conventions, numerical method details and convergence evidence are deferred or absent. Table 2 lists 22 segments and segment node counts/local K values; do not silently reinterpret its unusually thick flange entries as ordinary pipe thickness.

**Reported Eq. (1)** (PDF p. 5 / 517): property polynomial \(\phi=a+bT+cT^2+dT^3\), with T in °C and stated 220–630°C range. Table 3 gives density kg/m³, conductivity W/(m K), heat capacity J/(kg K), and viscosity **mPa s**, requiring a factor \(10^{-3}\) for Pa s. Unlike S10's constant-at-reference-temperature implementation, S50 states temperature-dependent properties.

**Reported Eqs. (2)–(3)** (PDF p. 6 / 518):
\[
Re=0.1768[(Gr_m)_{\Delta z}D/L_t]^{1/2},
\quad (Gr_m)_{\Delta z}={D^3\rho^2\beta gQ\Delta z\over A\mu^3 C_p}.
\]
The first is attributed to Vijayan (S09), under uniform diameter, laminar flow and negligible local losses; it is not S50's new derivation. With the nomenclature's SI definitions, the modified Grashof group is dimensionless: numerator and denominator each have units kg³ m s⁻⁵ K⁻¹. The positive square-root relation predicts magnitude on the assumed circulation branch; it is not a general reversal/transient equation.

The paper adopts Nu = 4.36 for primary-side heat transfer (§3.2, PDF p. 5). This requires the appropriate fully developed laminar circular-pipe uniform-flux idealization. Laminar Reynolds number alone does not establish thermal development, negligible mixed convection or the same boundary condition in the cooler. Fluid-wall storage and tank coupling require independent audit before copying the closure.

## Results, assessment and limitations

- Steady correlation overprediction reaches the authors' reported 28%; LeBENC temperature overprediction reaches reported 7% (§4.1, PDF pp. 6–7 / 518–519, Figs. 5–6). Denominator and Celsius-versus-absolute relative-temperature interpretation are not sufficiently specified for a transferable accuracy target. No error bars/full metric table.
- Segment ambient coefficients were calculated at average 1600 W and fitted/applied across cases, held constant; estimated maximum heat loss about 17% at 2000 W (§4.1, PDF p. 7). This is not an independently frozen, uncertainty-qualified loss calibration/holdout experiment.
- At 1200→1500 W, heater outlet rises 311→371°C in about 8086 s; cooler inlet 309→369°C in about 8141 s (§4.2.1, PDF p. 7, Fig. 7). These are source-reported changes, not independently digitized time constants.
- Forced-air loss retains about 29°C across the cooler; authors suggest structural absorption and local air circulation (§4.2.2, PDF p. 8 / 520, Fig. 9). Stopping a blower does not impose zero total heat removal. Reported 45°C/2850 s corresponds to 56.8°C/h by our arithmetic, whereas the prose says about 36°C/h: unresolved internal inconsistency, neither rate adopted as verified.
- Heater trip retains about 12°C heater inlet–outlet difference; computed cooling is too fast. Omitted expansion-tank salt inventory is offered as the explanation (§4.2.3, PDF p. 8, Fig. 10). Plausible interpretation, not isolated causal identification of the tank effect.
- No formal mesh/time refinement, parameter posterior, discrepancy budget, blind calibration/validation partition or independent salt-flow validation was found in the article. Previous water/LBE validation is cited; those originals remain separate reading tasks.

## Claim-to-evidence ledger

| ID | Supported claim | Locator | Appraisal |
|---|---|---|---|
| S50-C01 | Motivation includes HTR, solar power, instruments and operating/material experience | §1, PDF 1–2 / 513–514 | Direct description; not universal MSR similarity |
| S50-C02 | Conjugate 1D circulation, trace heating and losses already have precedent | §3, PDF 3 / 515 | Described capabilities; implementation deferred to ref. 24 |
| S50-C03 | S50 uses temperature-dependent property fits and Nu = 4.36 | Eq. 1/Table 3/§3.2, PDF 5 / 517 | Audit closure validity and viscosity units |
| S50-C04 | Loss coefficients use an average-power fit and remain fixed across cases | §4.1, PDF 7 / 519 | Calibration dependence limits independence |
| S50-C05 | Forced-air interruption retains cooling and has model mismatch | §4.2.2/Fig. 9, PDF 8 / 520 | Proposed mechanisms not separately measured |
| S50-C06 | Heater-trip mismatch is attributed to omitted tank storage | §4.2.3/Fig. 10, PDF 8 / 520 | Existing prior art; causal inference qualified |
| S50-C07 | Claimed broad applicability exceeds demonstrated regimes | §4.2.3–5, PDF 8–9 / 520–521 | Reviewer's scope appraisal |
| S50-C08 | Reported LOHS temperature change/time and hourly rate disagree | §4.2.2, PDF 8 / 520 | Source statement plus explicit arithmetic audit |

## TRIDENT transfer and next sources

Directly useful for the experiment/model comparison structure and known mismatch mechanisms. Conditional transfer for property dependence, heat-loss/storage retention and transient selection. Nitrate-to-glycol/HITEC transfer needs regime, boundary and time-scale checks; liquid-metal LeBENC ancestry is an analogy until its assumptions are audited. No coefficient is accepted as a TRIDENT material property.

S50 and S10 describe closely related BARC equipment, authors and scenarios. Exact run independence is not established: count them as related evidence, not two independent replications. The stronger prospective question is whether identifiable retained states/closures improve a declared held-out QoI and uncertainty requirement beyond these established models.

Acquire S52 (Borgohain 2011, ref. 24) for the actual equations, averaging/friction conventions and numerics. Property source ref. 26 is titled equimolar while this loop is 60:40 by mass; ref. 27 is also used. Verify composition provenance before reusing Table 3. No blanket rejection of the fits is implied.

## Coverage checklist / readiness

| Portion | Status | Reason / remaining limit |
|---|---|---|
| §1 history/motivation | Inspected/extracted | Cited originals not read through citation |
| §2 geometry/instrumentation; Figs. 1–2 | Inspected/extracted | Exact probe response/calibration records absent |
| §3 formulation; Fig. 3/Tables 1–3/Eqs. 1–3 | Inspected/extracted, relevant pages visually checked | Full LeBENC equations in separate source |
| §4 setup/steady/transients; Table 4/Figs. 4–10 | Inspected/extracted; pp. 5–8 visual check | No raw data/digitization or simulation replication |
| §5/nomenclature/references | Inspected/extracted selectively | Bibliography not equivalent to reading originals |
| Supplement/code/data | Not acquired | No claim of their contents |

Ready for qualified motivation, closest-prior-work and model-assumption synthesis. Not ready for literal LeBENC implementation, independent flow accuracy certification, or reactor-scale validation.
