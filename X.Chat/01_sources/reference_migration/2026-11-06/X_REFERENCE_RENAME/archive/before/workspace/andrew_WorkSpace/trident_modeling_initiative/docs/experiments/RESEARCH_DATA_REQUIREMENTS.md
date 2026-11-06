---
title: Research quantities to Nick-plan data requests
status: active
last_updated: 2026-10-22
tags: [project/trident, doc/specification, domain/experiments, facility/shared]
---

# Research quantities to Nick-plan data requests

Tags: #project/trident #doc/specification #domain/experiments #facility/shared

Owner: experimental-planning requirements (EXP-008), coordinated with existing
EXP-001, EXP-002-VCU, DAQ-007 and EXP-005 owners. Scope authority:
[research roadmap](../project/RESEARCH_ROADMAP.md). Original sources:
[Nick plan index](../../reference/Nick_luciano_exp_plan/2026-09-14/README.md).
All new experimental needs must be communicated through the plan discussion
with Dr. Luciano. The table is a **candidate request list**, not confirmation
that these data exist or that protocol amendments are accepted. No message
has been sent and no collaborator commitment is implied.

## Initial gap/request matrix

| ID / target | Needed measurements or experimental design | Nick phase route | Current gap / acceptance condition |
|---|---|---|---|
| D01 / every output's uncertainty | Calibration/reference uncertainty, sensor installation/location, clocks, units/status, synchronized ambient and operating records; repeats and correlated baseline records. | P0 checkout + P1 baseline; carry into P2–P4. | Existing records are candidate evidence; confirm exact channels, revisions, duration/rate and systematic/temporal/cross-channel uncertainty. Never set unknown systematic uncertainty to zero. |
| D02 / steady G and heat balance | Measured net heat addition/removal at defined boundaries, secondary mass flow and inlet/outlet temperatures/property basis, electrical/secondary input and parasitic loss accounting, room history and stationary wall/fluid profiles. | P3 low-duty steady; P4 duty/temperature matrix. | Define which duties and loss paths are actually measurable; independent duty/temperature variation where feasible; qualify negligible storage rather than assume it from a plateau. |
| D03 / C and transition response | Measured-power steady hold then shutdown/step, or other documented input excitation; synchronized actual input/cooler histories, participating initial-state estimates and enough duration/rate to observe relevant modes. | Proposed P2 addition linked to P3 steady anchors; P4 transition records. | Original P2 is controlled two-fill passive relaxation. Obtain Dr. Luciano's disposition for added active/steady-anchor sequence; fixed trusted inventory is an alternative absolute scale. One steady case does not identify every regional G/C. |
| D04 / flow and circulation | Independent flow/direction reference where available; pressure/elevation/topology, fluid properties and heater/cooler boundary records. | P0 measurement feasibility; P4 operating matrix. | ACU/VCU reference capabilities differ; do not invent VCU direct-flow validation. A balance-derived flow reference has shared-input/model uncertainty and is not independent by default. |
| D05 / temperature extrema and limits | Qualified existing wall/fluid/optical spatial mapping, coverage of critical regions, possible additional measurements or discriminating conditions, thresholds and installation details. | P0 mapping; P2–P4 selected cases. | Sensor min/max are not full-field min/max. Discuss instrumentation changes with Dr. Luciano; use qualified CFD with uncertainty for unobserved spatial extrema. Thresholds and tolerances remain to agree. |
| D06 / independent assessment | Dedicated repeats and withheld warm/cold, steady and transition cases with fixed data roles and complete condition records. | P2 holdouts; P3/P4 calibration/validation allocation. | A steady case used to set scale cannot simultaneously validate that calibrated model. Confirm available runs before promising independent assessment. |
| D07 / freeze margin, startup/shutdown and operations | Trace-heating actual power/control history, ambient exposure, fluid composition/freezing information, initial inventory/state, observed transitions and available limit/event records. | Discuss P2/P4 extensions and P0 metadata with Luciano; do not assume original plan covers them. | Begin with qualified operating changes and assessed margins; no automatic instruction to conduct unsafe or out-of-envelope tests. Operational thresholds/Ben Booth–NeutronOS interface agreed separately. |
| D08 / local recirculation | Qualified Trident CFD fields, local geometry/BCs, regime and convergence/uncertainty, compatible observation/reduction descriptors. | CFD route, outside assumed experimental measurements; P1–P4 can constrain boundary and bulk thermal consequences. | No direct loop measurements reported. Upload Ethan thesis, review TAMU applicability, then assess Trident CFD. Do not promise local experimental validation. |

## Request lifecycle and required fields

For each facility and candidate request, record the motivating objective/QoI,
existing plan revision/section, exact missing data, sensor/location/units,
sampling/clock needs, input variation and initial state, repeats/duration,
uncertainty requirement, data role/acceptance check, feasibility question,
collaborator disposition, and resulting revised-plan version. Unknown numbers
stay unresolved rather than being fabricated. Distinguish proposed, prepared
for user review, communicated, agreed, acquired and qualified. These are request
states, not claims of acquired data. Record why rejected or unavailable requests
change the corresponding research claim or require a CFD/model-based fallback.

## Useful work while CFD is pending

Prepare an observability/identifiability and uncertainty budget using reviewed
sensor and plan evidence; prioritize requests by how much a missing measurement
limits a QoI or independent test. Small synthetic sensitivity studies may be
proposed as separate tasks. Do not launch data processing or simulation from
this document alone. EXP-008 produces a concrete plan-change brief for the user
to discuss with Dr. Luciano. It does not edit his source plan or contact him.


## October22 user update and VCU priority brief — EXP-008 / CAL-018

User-directed continuation: [external evidence review and PowerPoint outline](../../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/comparisons/regional_resistances/2026-10-22/CAL-018_external_data_review/README.md), [two-acquisition request and phase mapping](../../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/comparisons/regional_resistances/2026-10-22/CAL-018_external_data_review/EXPERIMENT_REQUESTS.md). Trident modeling owns derived VCU comparisons/planning; original Luciano phase sources retain external ownership and are snapshotted read-only. These are prepared requests, not agreed revisions or executed procedures. ACU processing remains paused.

- D01/D02: the user will obtain better heater-power estimates and information to interpret secondary flow. Delivered instrument conversions, actual histories, uncertainty, measurement planes and net-deposition accounting remain pending. Do not infer watts from voltage alone or duty from a VFD/setpoint.
- D01/D05: insulation exterior-temperature instrumentation has been ordered; installation, channel mapping and first measurements are pending. It is not installed data. Further experimental results are awaited.
- D03/D06: no untouched reserve runs are confirmed. Prior records have development exposure. Propose a measured-power warm anchor plus documented shutdown and an independently restarted, prospectively withheld repeat. This pair addresses one regime; cold counterparts and wider coverage remain subsequent requirements.
- D01/D02/D03: user attributes persistent oscillations to HVAC and drift to the window. Preserve this as operational context, not a quantified causal source. Current Phase1 provisional calibration timing is45-minute evaluation+45-minute continuing hold, with30-minute reporting after the settling precondition. Longer waiting cannot remove sustained environmental forcing. Cycle-average or measured-input transient alternatives require explicit qualification and plan disposition.
- D07: synchronized input/control/environment histories and qualified state/transition limits remain applicable to later operational studies. These two requests do not authorize automated decisions or complete startup/freeze/operating-envelope evidence.
- D08: no direct local-recirculation measurement is supplied by these requests. Qualified Trident CFD and its applicability/uncertainty route remain separate from loop experimental validation.

The current Phase0 checkout, Phase1 baseline/acceptance, Phase2 relaxation/withheld cases, Phase3 warm/cold energy anchors and Phase4 transitions/repeatability already contain most requested objectives. Exact section names and source copies are in the brief. A joined powered-anchor/shutdown protocol, repeat allocation and any forced-transient replacement for unattainable constant states need agreement. Phase2 source includes inconsistent two-fill and in-place recirculation descriptions; obtain the controlling procedure rather than selecting one silently. The installed VCU electrical-heater boundary must be reconciled with source-plan secondary-heater duty notation.

The user reports experimental delay with unknown cause. Ask for current phase/run dispositions, the specific blocker, owner, next action and review date; do not invent a personnel, hardware, schedule or prerequisite explanation. A bounded priority slot is proposed, not a blanket cancellation of the progression. [EXP-009](../../coordination/tasks/EXP-009.md) is the user/agent TODO to finalize the presentation and bring the evidence-based case for repeat/assessment runs. No message has been sent.

## CAL-019 nominal heater input — October22 update

[User-supplied audit and accepted assumptions](../../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/comparisons/regional_resistances/2026-10-22/CAL-018_external_data_review/2026-10-22/CAL-019_heater_audit/README.md) now provide the best available nominal heater input. Constant20/48ohm resistances and dial=RMS are explicitly accepted; the package supplies continuous/common-dial defaults with explicit overrides. Additional electrical measurements are optional characterization, not prerequisites to nominal calculations or proposed documented-input repeats. At25/85V total nominal generation is145.833/1685.833W, with reported1500/5100W preserved. Actual voltage error, R(T), net fluid delivery and schedule/date applicability remain unqualified; no uncertainty bound is invented. Secondary-flow alternatives are documented but not admitted as measured duty. Revise the presentation/priority case accordingly; no external contact or new experiment is implied.
