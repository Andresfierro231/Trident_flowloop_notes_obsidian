\---

title: Project facts that should shape the Trident literature review

status: review

last_updated: 2026-10-20

tags: [project/trident, doc/report, domain/experiments, domain/uncertainty, facility/shared]

\---



**# Project facts for the Trident literature-review conversation**



Tags: #project/trident #doc/report #domain/experiments #domain/uncertainty #facility/shared



**\*\*Read this alongside the literature-review prompt.\*\*** This is a self-contained

project-context attachment, not a literature review. It summarizes existing

project records through October20,2026. Local source links support project agents;

a separate ChatGPT conversation needs uploaded files to follow those links.

The prose below can be used without access to the repository.



Evidence labels: **\*\*author direction/report\*\*** means a recorded user decision or

statement, not an independently audited instrument or experiment;

**\*\*working configuration\*\*** means a selected, often provisional input;

**\*\*implemented\*\*** means an existing model, not facility validation;

**\*\*written proposal\*\*** means specified in a draft plan, not approved or executed;

**\*\*unresolved\*\*** means the retrieved records do not establish the fact. Absence

from these records is not proof that a collaborator has no such information.



**## 1. Target application and engineering decision**



**\*\*Author direction:\*\*** develop a fast, interpretable, physics-based reduced-order

model (ROM), and a reproducible CFD–experiment procedure for selecting retained

mechanisms and identifying supported physical-parameter combinations. Immediate

users are ACU/VCU loop researchers/operators. Predict temperatures and overall

natural-circulation flow, expose model/evidence inadequacy, and assess consequences

of changed heating, cooling and ambient conditions. Three formal stages are

steady performance/margins, transitions, and operational assistance. Uncertainty

estimation and propagation belong in every stage. Dashboard development is active

and must involve Ben Booth and NeutronOS. [S01]\(../../../../../../../../docs/project/RESEARCH_ROADMAP.md) [S02]\(../../../../../../../../AGENTS.md)



**\*\*Unresolved reactor mapping:\*\*** MSR relevance and natural circulation as a

separate-effects phenomenon motivate the work, but these records do not select

one reactor architecture or deployment: liquid-fuel primary system, non-fueled

salt transport, FHR heat-removal path, or a specific reactor safety function.

Do not choose one for us. Distinguish a useful loop demonstrator from proof of

reactor applicability; compare candidate applications with explicit similarity

and evidence requirements. No neutronic feedback, fuel chemistry, decay-heat

source history, reactor pressure envelope or licensing duty is established here.

The original Moser note explicitly asks how the work connects to MSRs. [S03]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/DECISIONS.md) [S04]\(../../../../../../../../reference/phD_goals/Raw_notes/14_Oct-moser_abstract.md)



**\*\*Prediction contract:\*\*** the intended autonomous forward mode takes geometry,

properties, selected closures and heater/secondary-cooling/ambient inputs;

primary temperatures and circulation are outputs. Conditional models driven by

measured primary temperatures are useful diagnostics with a different contract.

State-updated operational feedback is a later, separately assessed mode. The

author's earlier phrase “critical heat flux” meant allowable heat flux and

material/sensor temperature limits; **\*\*boiling is not intended\*\***. Numeric limits

and acceptance tolerances are not yet established. Faster-than-real-time is an

objective without a frozen latency requirement. [S03]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/DECISIONS.md)



**\*\*Search consequence:\*\*** emphasize conjugate single-phase natural circulation,

physical model reduction/identification, uncertainty and operational decisions.

Keep reactor-specific literature in explicitly qualified application branches;

do not center the review on boiling CHF correlations because of old wording.



**## 2. Facility, fluid and operating-envelope mapping**



\| Identity | Documented/working mapping | Evidence limits |

\|---|---|---|

\| **\*\*ACU\*\*** | Separate Trident facility/configuration. Current candidate property branch is HITEC. Reviewed written RevB geometry outranks approximate SAM-derived geometry. Cooler concept uses secondary air, countercurrent to the primary, with bare primary pipe inside a jacket and a separately exposed jacket shell. | HITEC composition/batch, property citations, uncertainty and physical validity range are not accepted merely because code supplies a property function. Runnable legacy geometry and reviewed geometry are distinct. Installed details and per-run conditions remain gates. ACU operating-data processing remains on user hold. |

\| **\*\*VCU\*\*** | Separate Trident facility/configuration. Written plan and author clarification identify **\*\*Prop-30 glycol\*\***. Current working geometry is **\*\*Rev9\*\***, with nominal ID26.64mm and OD33.401mm. Water-jacket cooling has PTC5 inlet and PTC6 outlet in the working mapping. | Exact glycol product, concentration/mixture definition, batch, supplier and accepted temperature-dependent property model/range remain unresolved. Earlier “mineral oil” wording is superseded; do not use mineral-oil properties on that basis. Older solver studies retain Rev8 rather than automatically acquiring Rev9. |

\| **\*\*STNCL\*\*** | Nick's source title is “Prop-30 Glycol Salt Twin Natural Circulation Loop (STNCL).” This plan is routed through the project's VCU experiment lane. | Treat STNCL as the source-plan naming, not an independently qualified third dataset, an ACU synonym, or the TAMU loop. A formally verified facility/configuration identity record is still needed for each experiment. |

\| **\*\*TAMU / Ethan thesis\*\*** | External master's natural-circulation experiment/CFD reference, including salt cases and reported local reverse flow. | Geometry, thermal boundaries, properties and measurement definitions belong to TAMU. They are not ACU/VCU evidence or transferable coefficients without applicability review. |



Sources: ACU configuration/geometry/cooler [S05]\(../../../../../../../../config/materials/acu_candidate_materials_v1.yaml) [S06]\(../../../../../../../../config/geometry_sources/acu_revb_reviewed.yaml) [S07]\(../../../../../../../../config/facilities/acu_provisional/cooler_model.yaml) [S37]\(../../../../../../../../config/facilities/acu_provisional/README.md) [S38]\(../../../../../../../../config/facilities/acu_provisional/material_assignments.yaml); VCU fluid

and selection [S08]\(../../../../../../../../config/facilities/vcu_provisional/fluid.yaml) [S09]\(../../../../../../../../config/facilities/vcu_provisional/rev9_working_selection_v3.json); Nick source title [S10]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex); TAMU map [S11]\(../../../../../../../../docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md).



**\*\*VCU thermal construction matters.\*\*** Current reported coverage is approximately

50.8mm fiberglass on the upcomer, downcomer and all four corners; the straight

heater has only approximately6.35mm ceramic-fiber strip, without an added

50.8mm fiberglass layer. The straight top/cooler D–E is bare; bare pipe under

the water jacket exchanges with coolant. Local bare STC contact does not make

the surrounding whole segment uninsulated. Product identity, exact endpoints,

contact resistance and thickness uncertainty remain incompletely documented.

Full projected lower-leg heating is a working assumption, not a surveyed heater

footprint. Rev9 sensor selection and current insulation records supersede older

blanket statements about uninsulated top corners. [S09]\(../../../../../../../../config/facilities/vcu_provisional/rev9_working_selection_v3.json) [S12]\(../../../../../../../../config/facilities/vcu_provisional/INSULATION_CURRENT.md) [S13]\(../../../../../../../../docs/decisions/2026-10-14_GEO-008_rev9_working_selection.md)



**\*\*No accepted common numeric operating envelope was retrieved.\*\*** A candidate ACU

property configuration's 400–605K domain is a software property-domain guard,

not an approved facility operating envelope. Nick's warm/cold offsets of roughly

ambient ±5°C, and ±10°C when practical, are provisional plan targets rather than

approved operating limits. Some VCU ambient records explicitly contain \*\*air

inside the primary pipe\*\*, heater0W and chiller off; they must not be represented

as glycol-flow experiments. Voltage schedules alone do not establish watts.

Historical geometry, fill, insulation and operating conditions need per-run

qualification. [S05]\(../../../../../../../../config/materials/acu_candidate_materials_v1.yaml) [S10]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex) [S14]\(../../../../../../../../coordination/tasks/EXP-002-VCU.md)



**\*\*Search consequence:\*\*** separate salt and glycol property/Prandtl/regime questions,

secondary-air versus water-jacket cooling, and ambient air-filled versus filled

operating tests. Request methods valid across a declared envelope rather than

inventing a single shared facility regime.



**## 3. Independent measurements and derived quantities**



\| Quantity | What the project currently supports | Independence caveat |

\|---|---|---|

\| Electrical heating | Author reports heating watts as a known input; historical records also contain voltage commands. | No complete qualified, synchronized per-run net-deposition record was established here. Commanded voltage, measured electrical power and heat deposited in primary fluid/solids are different quantities. Efficiency/source-location uncertainty matters. |

\| Secondary-side flow and inlet/outlet temperatures | Author reports these and dissipated power as available, but expresses uncertainty about coverage of both facilities. VCU working labels identify the water inlet/outlet temperature pair. | Presence of two temperature channels does not establish an independent flow measurement or complete calorimetry. Confirm instruments, time alignment and exact per-run availability. |

\| Cooler duty | Candidate calorimetry is \`Q_c = mdot_s [h_s(T_out) − h_s(T_in)]\`, positive for heat gained by secondary coolant. | A derived duty shares temperatures, flow calibration and properties with its ingredients. It is not an additional independent power observation. An independently instrumented duty channel would need its own evidence. |

\| Ambient loss at steady state | Nick Phase3 proposes integral loss from steady heater/cooler energy balance. | Requires negligible storage and a closed source/sink ledger. A total balance does not independently determine each region's loss or internal HTC. |

\| ACU primary flow | **\*\*User reports a flow meter.\*\*** | Calibration, range, response, uncertainty, operating coverage and usable synchronized records were not established in this extraction. Do not call it a verified flow ground truth yet. |

\| VCU primary circulation | **\*\*No direct primary-circulation measurement, per author.\*\*** Nick Phase4 proposes energy-balance flow inference. | Heater-side and cooler-side estimates can share duties, temperatures, properties and fitted corrections. Distinct balance equations do not make their errors statistically independent. CFD comparison is not independent experimental flow validation. |

\| Local upcomer recirculation | **\*\*No direct local-flow measurements in the Trident loop, per author.\*\*** | Overall throughflow, local reverse-flow extent and the effect on heat transfer are separate outputs. Temperatures may constrain thermal consequences without uniquely identifying the local velocity structure. |



Sources: author answers/decisions [S03]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/DECISIONS.md) [S15]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/AUTHOR_ANSWERS.md); data-request matrix [S16]\(../../../../../../../../docs/experiments/RESEARCH_DATA_REQUIREMENTS.md);

Nick Phase3/4 [S17]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex) [S18]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex).



A variable supplied as a boundary condition cannot also be counted as an

independently predicted validation target. For example, imposing secondary duty

computed from outlet temperature and then claiming that same duty/outlet as an

independent validation result needs an explicit accounting of the shared inputs.

Carry covariance through calorimetry and flow inference; compare observables

with compatible spatial and thermodynamic definitions.



**\*\*Search consequence:\*\*** prioritize identifiability with indirect flow information,

correlated calorimetric errors, independently anchored energy scales,

errors-in-variables and uncertainty propagation. Require a measurement-dependency

graph and feasible additions through Nick's plan rather than assuming extra data.



**## 4. Observation operators, sensors and acquisition**



**\*\*VCU working channel semantics:\*\*** the inspected September4 acquisition has

20 native temperature channels: STC1–12, PTC1–6, Tank and Amb. Working PTC1–4

operators represent primary centerline temperatures; actual penetration/tip

coordinates are not fully verified. STCs contact the outside pipe locally on

bare metal; exact junction footprints, mounting/contact effects and historical

installation applicability remain unresolved. The October14 Rev9 decision moves

STC5 to its Rev9 upcomer position, retains PTC4, excludes PTC-X as a suspected

artifact, and maps JTC-B to PTC5 water inlet and JTC-A to PTC6 outlet. The older

electrical/channel-name match does not by itself verify physical sensor location.

Luna LF1–4 declarations/plan references do not establish four additional qualified

channels in that 20-channel TDMS record. [S13]\(../../../../../../../../docs/decisions/2026-10-14_GEO-008_rev9_working_selection.md) [S19]\(../../../../../../../../docs/data/2026-10-05_VCU_WORKING_SENSOR_CROSSWALK.md) [S20]\(../../../../../../../../coordination/tasks/DAQ-007.md)



**\*\*Calibration and covariance:\*\*** current ambient studies use the author's

calibrated-probe assumption. This is not a retrieved set of traceable calibration

certificates or a complete systematic uncertainty budget. Detrended residual

covariance, common-mode behavior, autocorrelation and block-bootstrap diagnostics

exist. These are conditional TypeA estimates, not intrinsic sensor noise,

complete accuracy bounds, or a globally accepted calibration covariance matrix.

Unresolved TypeB uncertainty must not be set to zero. Sensor time constants and

full transfer functions are not established. [S21]\(../../../../../../../../docs/data/VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md) [S22]\(../../../../../../../data/2026/10/vcu_ambient_response/2026-10-19/CAL-007_ambient_offset_transfer_v2/README.md)



**\*\*Timing and sampling are record-specific.\*\*** Inspected native summaries give

approximately60Hz for June12 and30Hz for July14/September4. July14 contains

five separate short groups, approximately90s each; do not join them into a

continuous transient. One-second or one-minute reductions used in studies are

not the native acquisition frequency. A 1Hz example in a plan appendix is not

a confirmed DAQ specification. TDMS and written-log wall clocks can disagree;

exploratory common elapsed origins do not establish absolute synchronization.

The diagnostics method retains native group clocks, avoids invented time axes

and gap filling, and computes covariance only on aligned finite support.

June12 STC6 and PTC2/PTC3 are quarantined in current quality work; that does not

invalidate every channel or every experiment. [S14]\(../../../../../../../../coordination/tasks/EXP-002-VCU.md) [S21]\(../../../../../../../../docs/data/VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md) [S23]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_06_12_11c7dc8540/summary.json) [S24]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_07_14_7898ea1020/summary.json) [S25]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_09_04_791594aa47/summary.json)



**\*\*ACU:\*\*** do not transfer these VCU channel counts, mountings, calibration

assumptions or sample rates to ACU. Facility-specific observation qualification

remains separate and ACU data processing remains paused. [S02]\(../../../../../../../../AGENTS.md)



**\*\*Search consequence:\*\*** include centerline versus bulk/enthalpy-weighted

measurement operators, pipe-contact sensor dynamics, calibration drift/shared

bias, correlated noise, irregular/grouped acquisition and synchronization.

Avoid fitting “missing physics” to an observation-definition error.



**## 5. Nick Luciano's actual protocol status**



**\*\*Documented status:\*\*** supplied phase-specific sources are revision0.1 dated

August17,2026, marked **\*\*Draft for team review and facility-specific completion\*\***,

with blank approval signatures. The September14 storage date is not an approval

date. Retrieved records do not establish signed approval, phase Proceed

dispositions, execution of the specified run matrix, or a frozen independent

validation set. Existing temperature records are not proof that these phase

protocols were followed. [S10]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex) [S26]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase0_System_Checkout.tex) [S27]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase1_Ambient_Equilibrium_Baseline.tex)



\| Phase | What the draft specifies | What must not be assumed |

\|---|---|---|

\| 0 checkout | Facility configuration, calibration/channel records, synchronized acquisition, safety and readiness gates. | A source document is not a completed checkout receipt. |

\| 1 ambient baseline | Noise/correlation/uncertainty assessment, near-isothermal resolvability, steady-state criteria. | Numeric acceptance bands, approved block duration and calibration budgets are not established just by the prose. |

\| 2 relaxation | At least two warm and two cold runs: MF-WARM-01/MF-COLD-01 calibration; MF-WARM-02/MF-COLD-02 withheld repeat or preselected second target. Mixed-tank conditioning uses at least two spatial tank temperatures, preferably three; a two-fill method is specified, with prior approval for a single-fill exception. Define t0 after refill/isolation/gross fill motion ends and check preapproved uniformity criteria. Heating/cooling are off and secondary isolation/residual duties must be checked. | A label is not an acquired or frozen holdout. Near-isothermal initial conditions, residual circulation and unmeasured solid states need evidence. Valve positions alone do not establish negligible power. |

\| 3 low-duty steady | Required heater-only above-ambient and cooler-only below-ambient states; optional balanced state if discrepancies warrant. Evaluate the frozen Phase2 model before controlled revision. | These are not automatically no-flow states. Fitting on Phase3 changes its validation role. |

\| 4 operating/transition matrix | Five unique states: OP-A/B/C at middle temperature and low/middle/high duty; OP-D/E at low/high temperature and middle duty; OP-B-R repeat. Preselect one unique withheld applicability state; no primary-analysis Phase4 refit. | Actual approved temperature/duty values, executed transitions/repeats and untouched holdout records were not established. |



Sources: original phase documents [S10]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex) [S17]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex) [S18]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex) [S26]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase0_System_Checkout.tex) [S27]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase1_Ambient_Equilibrium_Baseline.tex).



**\*\*Important Phase2 distinction:\*\*** Nick's reduced-zone state is an effective

regional stored-energy temperature built from a frozen observation mapping;

it is not an independently resolved fluid and wall temperature in every region.

Passive relaxation identifies time constants and supported conductance/capacitance

ratios. A qualified known-power steady experiment can anchor absolute thermal

conductance combinations, followed by transient capacity inference \*\*to the

extent those combinations are observable and the same model applies\*\*. Multiple

heat paths, unknown source partition and hidden solid states can prevent unique

individual G/C identification. The author's steady-hold/shutdown idea is a

research direction to discuss; it is not an already approved amendment to Nick's

written Phase2. [S10]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex) [S28]\(../../../../../../../solver/2026/10/clarno_solver_guide/2026-10-19/DOC-032_phase2_comparison/README.md)



**\*\*Data-availability constraint from the author:\*\*** additional experimental data

must be requested through the Nick Luciano plan, discussed with Dr. Luciano,

and incorporated into an agreed revision. The user calls this the four-stage

route; the source set comprises checkout Phase0 plus Phases1–4. The review may

recommend changes, but must state instruments, excitation, repeats, initial

conditions, uncertainty and withheld roles needed, instead of assuming new runs

or sensors will appear. [S02]\(../../../../../../../../AGENTS.md) [S16]\(../../../../../../../../docs/experiments/RESEARCH_DATA_REQUIREMENTS.md)



**\*\*Search consequence:\*\*** compare experimentally feasible identification strategies

under these initial-state and data constraints; distinguish structural from

practical identifiability and propose minimum plan amendments.



**## 6. Confirmed CFD scope, evidence and resources**



**\*\*Trident-specific status:\*\*** the October13 author record says that available CFD

data are unknown, VCU was expected to drive the work, and progress was not then

established. No later qualified Trident delivery manifest, field inventory,

mesh/time-step verification, operating coverage, computing allocation or

committed delivery date was found in the retrieved project records. A raw-note

“CFD ready by December” item is an aspiration, not an agreed delivery commitment.

Do not interpret this extraction as a fresh status report from the CFD team.

[S15]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/AUTHOR_ANSWERS.md) [S29]\(../../../../../../../../reference/phD_goals/Raw_notes/rough_timeline_proposal.md)



**\*\*What is actually available for this handoff:\*\*** Ethan Rozak's May2026 TAMU

thesis has been uploaded, and a text/source-page BC and recirculation shortcut

map exists. The thesis reports closed-loop CFD, no-slip walls, a pressure

reference/flux-compatible pressure BC, and a custom annular-resistance plus

external convection/radiation thermal boundary closure. Exact executable custom

BC source and case-specific dictionaries/runtime settings are not verified by

the thesis intake. Its pseudo-time steady convergence is not validated physical

transient behavior; its full-loop two-grid comparison is not a universal

three-grid verification of every field/QoI. Measured-wall-temperature first-order

loss calculations are distinct from actual OpenFOAM thermal BCs. [S11]\(../../../../../../../../docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md)



External TAMU work has additional case/field analyses, but is separately owned

and is not a confirmed Trident CFD delivery or a blanket validation resource.

The present extraction does not audit those evolving external campaigns. No

TAMU coefficient, geometry, source distribution or local-flow validation is

admitted into ACU/VCU by this fact sheet. [S11]\(../../../../../../../../docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md) [S02]\(../../../../../../../../AGENTS.md)



**\*\*Needed outputs to assess, not promised fields:\*\*** for local recirculation and

heat-transfer impact, request what each candidate method needs—e.g. velocity and

temperature on native mesh/sections, density/property law, pressure definition

and gravity, wall heat flux and conjugate temperatures, signed fluxes, source

and cooler ledgers, BC code/configuration, and a verified parameter envelope.

Define extent and heat-transfer impact separately from bulk circulation and

from an attractive contour. The author wants to determine how much is feasible;

a full local velocity-field reconstruction from sparse Trident temperatures

is not an established deliverable. [S02]\(../../../../../../../../AGENTS.md) [S11]\(../../../../../../../../docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md) [S16]\(../../../../../../../../docs/experiments/RESEARCH_DATA_REQUIREMENTS.md)



**\*\*Search consequence:\*\*** provide an experiments-first route, a route contingent

on qualified steady CFD, and a later transient/field-rich route. Include CFD

model discrepancy and BC uncertainty, QoI-specific verification, domain-shift

checks and alternatives if field access or delivery slips.



**## 7. Current model equations and diagnostic contracts**



**\*\*Implemented steady hierarchy:\*\*** the physical network uses fluid \`F_i\`, pipe

\`P_i\` and insulation \`S_i\` temperatures in kelvin, with residuals in watts,

positive into the control volume. Conductances below are frozen values for the

equation display; configured closures/properties can introduce nonlinearity.



M1 (no advective throughflow) has representative residuals:



\`\`\`text

R_F,i = c\_(i-1)(F\_(i-1)-F_i) + c_i(F\_(i+1)-F_i) + g_i(P_i-F_i) = 0

R_P,i = a\_(i-1)(P\_(i-1)-P_i) + a_i(P\_(i+1)-P_i)

&#x20;       \+ g_i(F_i-P_i) + w_i(S_i-P_i) + q_i = 0

R_S,i = w_i(P_i-S_i) + q_ambient,i(S_i) = 0

q_ambient = -h_ext A_ext(S_i-T_ambient)

&#x20;           -epsilon sigma A_ext(S_i^4-T_surroundings^4)

\`\`\`



\`c/a\` denote fluid/pipe axial conduction, \`g\` fluid-to-pipe and \`w\` pipe-to-

insulation radial exchange. M1 includes pipe axial conduction when configured

with positive wall areas/conductivity; no insulation axial conduction is in

this baseline. Heater input is assigned to pipe nodes in the baseline; this is

a source-path assumption. Internal convection, radial/contact resistance,

ambient convection/radiation, heater and selectable cooler remain separately

reportable. M1 has neither heat storage nor a momentum equation. [S30]\(../../../../../../../../docs/theory/M1_STEADY_NO_FLOW_CONTROL_VOLUME_AND_MATRIX.md)



M2 adds conservative signed upwind enthalpy transport with **\*\*prescribed\*\***

throughflow \`m\`:



\`\`\`text

H_i = max(m,0) h(F_i) + min(m,0) h(F\_(i+1))

R_F,i(M2) = R_F,i(M1) + H\_(i-1) - H_i

\`\`\`



The same face flux enters adjacent cells with opposite signs on a periodic

main loop. Prescribing flow is not predicting it. [S31]\(../../../../../../../../docs/theory/M2_PRESCRIBED_FLOW_ENERGY.md)



M3 solves one scalar loop momentum balance alongside M2 energy:



\`\`\`text

0 = sum_i[-g rho_i delta_z_i] - sum_i L_distributed,i - sum_i L_local,i

L_local,i = K_i m abs(m)/(2 rho_i A_i^2)

\`\`\`



The documented diagnostic includes laminar resistance

\`128 mu L m/(pi rho D^4)\`, an inertial Darcy branch and a declared smooth blend,

with a linear Boussinesq density option for buoyancy. These are implemented

model forms, not accepted facility friction/property laws. One scalar periodic

throughflow does not resolve simultaneous local forward/reverse flow or its

thermal weighting. Local recirculation would need an additional justified

closure/reconstruction or richer representation. Do not confuse a scalar-flow

root with validation of a local 3D field. [S32]\(../../../../../../../../docs/theory/M3_NATURAL_CIRCULATION_MOMENTUM.md)



**\*\*Numerics and diagnostics:\*\*** layer-major state ordering; damped Newton energy

solves with declared Jacobian/linear-solver choices; nested signed-flow scan and

bracketed root solving for M3. Source/sink and interface conservation, momentum

residual, sign/branch behavior and mesh/root sensitivity matter. Numerical

convergence is not facility validation, nor evidence that a unique physical

branch was identified. [S33]\(../../../../../../../../docs/theory/SOLVER_NUMERICS_AND_STATE_ORDER.md)



**\*\*Separate existing transient/empirical studies:\*\*** July15 wall-response work

uses a local linear system \`C dx/dt = K x + B u(t)\`, with measured primary-fluid

temperatures and ambient supplied as forcing, plus assumed initial solid states.

The implementation includes exact linear propagation. [S36]\(../../../../../../../../src/trident_thermal/calibration/prescribed_radial.py) It has no autonomous

primary-fluid energy/momentum evolution in that local model. A later STC

interval can test conditional wall response, while later supplied PTC data

remain inputs; this is not a blind full-loop forecast. Current startup/ambient

comparisons also include empirical and physical model families with measured

initial states/later ambient and permitted other-run learned terms. They do

not establish a universal physical G/C estimate or an autonomous circulation

predictor. [S34]\(../../../../../../../data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_wall_response/REPORT.md) [S35]\(../../../../../../../data/2026/10/vcu_ambient_response/2026-10-20/CAL-010_startup_model_comparison/README.md)



**\*\*Diagnostic order to ask the literature to support:\*\*** first match facility/run,

geometry and fill; then source/deposition, cooler and ambient boundaries;

then sensor location, centerline/bulk/enthalpy definition and timing; then

properties, conservation and numerical verification; finally assess closure

inadequacy using independent evidence and uncertainty. This is a proposed

interpretation discipline, not a claim that a specific discrepancy has already

been attributed. Temperature fitting alone cannot reliably distinguish a wrong

boundary from missing recirculation physics.



**## Highest-impact facts still needed before narrowing the search further**



1\. Select the reactor use case and the actual engineering decision/QoI; define

&#x20;  acceptable uncertainty and the intended operating envelope.

2\. Confirm installed fluid/batch/property basis and historical configuration

&#x20;  for each facility/run, independently of numerical defaults.

3\. Obtain the instrument/dependency record for power, secondary calorimetry and

&#x20;  ACU flow; determine whether any flow/duty validation can be independent.

4\. Obtain sensor installation/calibration/response/time records and uncertainty

&#x20;  budgets, including shared systematic errors.

5\. Obtain Dr. Luciano's current approved plan revision, execution records and

&#x20;  agreed calibration/withheld roles; negotiate needed amendments through him.

6\. Obtain a dated Trident CFD delivery/field/verification/coverage/resources

&#x20;  contract, with a fallback plan if unavailable.

7\. Freeze the prediction mode and candidate model forms before comparing

&#x20;  methods; state what is measured input, inferred parameter and held-out output.



These are evidence requests for proposal planning, not instructions to defer

all useful work. The review should compare feasible approaches under the

current limits and identify which missing fact would change each recommendation.



**## Source ledger**



Sources are existing project records, not newly reviewed literature. Links and

SHA-256 hashes are recorded in [sources.json]\(sources.json); source dates and

qualification in the sections above govern interpretation. Original plan text,

issued reports and model implementations are unchanged by this attachment.



\- [S01: RESEARCH_ROADMAP.md]\(../../../../../../../../docs/project/RESEARCH_ROADMAP.md)

\- [S02: AGENTS.md]\(../../../../../../../../AGENTS.md)

\- [S03: DECISIONS.md]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/DECISIONS.md)

\- [S04: 14_Oct-moser_abstract.md]\(../../../../../../../../reference/phD_goals/Raw_notes/14_Oct-moser_abstract.md)

\- [S05: acu_candidate_materials_v1.yaml]\(../../../../../../../../config/materials/acu_candidate_materials_v1.yaml)

\- [S06: acu_revb_reviewed.yaml]\(../../../../../../../../config/geometry_sources/acu_revb_reviewed.yaml)

\- [S07: cooler_model.yaml]\(../../../../../../../../config/facilities/acu_provisional/cooler_model.yaml)

\- [S08: fluid.yaml]\(../../../../../../../../config/facilities/vcu_provisional/fluid.yaml)

\- [S09: rev9_working_selection_v3.json]\(../../../../../../../../config/facilities/vcu_provisional/rev9_working_selection_v3.json)

\- [S10: STNCL_Phase2_Thermal_Relaxation_Tests.tex]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase2_Thermal_Relaxation_Tests.tex)

\- [S11: ETHAN_THESIS_BC_AND_RECIRCULATION.md]\(../../../../../../../../docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md)

\- [S12: INSULATION_CURRENT.md]\(../../../../../../../../config/facilities/vcu_provisional/INSULATION_CURRENT.md)

\- [S13: 2026-10-14_GEO-008_rev9_working_selection.md]\(../../../../../../../../docs/decisions/2026-10-14_GEO-008_rev9_working_selection.md)

\- [S14: EXP-002-VCU.md]\(../../../../../../../../coordination/tasks/EXP-002-VCU.md)

\- [S15: AUTHOR_ANSWERS.md]\(../../../../phd_research_framework/2026-10-13/DOC-026_author_decisions/AUTHOR_ANSWERS.md)

\- [S16: RESEARCH_DATA_REQUIREMENTS.md]\(../../../../../../../../docs/experiments/RESEARCH_DATA_REQUIREMENTS.md)

\- [S17: STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase3_Low_Duty_Steady_Heat_Loss_Tests.tex)

\- [S18: STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase4_Initial_Test_Matrix_and_Transition_Characterization.tex)

\- [S19: 2026-10-05_VCU_WORKING_SENSOR_CROSSWALK.md]\(../../../../../../../../docs/data/2026-10-05_VCU_WORKING_SENSOR_CROSSWALK.md)

\- [S20: DAQ-007.md]\(../../../../../../../../coordination/tasks/DAQ-007.md)

\- [S21: VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md]\(../../../../../../../../docs/data/VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md)

\- [S22: README.md]\(../../../../../../../data/2026/10/vcu_ambient_response/2026-10-19/CAL-007_ambient_offset_transfer_v2/README.md)

\- [S23: summary.json]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_06_12_11c7dc8540/summary.json)

\- [S24: summary.json]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_07_14_7898ea1020/summary.json)

\- [S25: summary.json]\(../../../../../../../data/2026/09/vcu_native_trend_library/2026-10-07/VIS-013_vcu_july14_and_grouped/grouped/2026_09_04_791594aa47/summary.json)

\- [S26: STNCL_Phase0_System_Checkout.tex]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase0_System_Checkout.tex)

\- [S27: STNCL_Phase1_Ambient_Equilibrium_Baseline.tex]\(../../../../../../../../reference/Nick_luciano_exp_plan/2026-09-14/STNCL_Phase1_Ambient_Equilibrium_Baseline.tex)

\- [S28: README.md]\(../../../../../../../solver/2026/10/clarno_solver_guide/2026-10-19/DOC-032_phase2_comparison/README.md)

\- [S29: rough_timeline_proposal.md]\(../../../../../../../../reference/phD_goals/Raw_notes/rough_timeline_proposal.md)

\- [S30: M1_STEADY_NO_FLOW_CONTROL_VOLUME_AND_MATRIX.md]\(../../../../../../../../docs/theory/M1_STEADY_NO_FLOW_CONTROL_VOLUME_AND_MATRIX.md)

\- [S31: M2_PRESCRIBED_FLOW_ENERGY.md]\(../../../../../../../../docs/theory/M2_PRESCRIBED_FLOW_ENERGY.md)

\- [S32: M3_NATURAL_CIRCULATION_MOMENTUM.md]\(../../../../../../../../docs/theory/M3_NATURAL_CIRCULATION_MOMENTUM.md)

\- [S33: SOLVER_NUMERICS_AND_STATE_ORDER.md]\(../../../../../../../../docs/theory/SOLVER_NUMERICS_AND_STATE_ORDER.md)

\- [S34: REPORT.md]\(../../../../../../../data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_wall_response/REPORT.md)

\- [S35: README.md]\(../../../../../../../data/2026/10/vcu_ambient_response/2026-10-20/CAL-010_startup_model_comparison/README.md)

\- [S36: prescribed_radial.py]\(../../../../../../../../src/trident_thermal/calibration/prescribed_radial.py)

\- [S37: README.md]\(../../../../../../../../config/facilities/acu_provisional/README.md)

\- [S38: material_assignments.yaml]\(../../../../../../../../config/facilities/acu_provisional/material_assignments.yaml)
