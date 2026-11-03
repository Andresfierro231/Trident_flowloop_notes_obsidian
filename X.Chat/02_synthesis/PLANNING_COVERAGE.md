# Planning-document coverage and recovered tasks

- Source: G01, exact text read earlier in this conversation; that same read is reused, with its captured revision. No new document change is asserted.
- The newly mounted snapshot was unavailable through the file reader; this comparison relies on the already obtained exact-source text, not that unreadable snapshot.
- All 580 returned paragraphs are assigned a topic/disposition in [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/planning_item_coverage.csv|item coverage]], including repeats, blanks and administrative/history content. Source indices are version-specific.
- The first outline already covered the central scientific story. This pass restores detailed workflow tasks/sub-bullets and explicitly marks superseded, optional and administrative material; it does not convert every historic TODO into a new requirement.

| Group | Planning subsection / task | Proposal destination | Literature / HPC route | Disposition |
|---|---|---|---|---|
| GP01 | Motivation, operator purpose and facility context; `t.0` 0–4006 | motivation/goals | B §§1–6; HC02 | Retain MSR outputs/mission; qualify fluid/source/similarity and historical software. |
| GP02 | States, boundaries, forward/inverse uses; `t.0` 4006–5151 | model/observation | A §§1–5 | Separate retained state, imposed input, observations, inference and controls. |
| GP03 | Formalized goals and sensor/data adequacy; `t.0` 5151–6863 | goals/assessment | A §§1,5–11; B §11 | Preserve prediction, sensor reliability/loss and additional-data questions. |
| GP04 | Theory motivation and method rationale; `t.0` 6863–7897 | methods | A §§2–12; B §7 | Show minimal governing equations and exact derivation pointers; explain tool choice. |
| GP05 | Tool landscape and observation resolution; `t.0` 7897–8225 | methods | A §16; B §7 | Use tools to explain roles/limitations, not as thesis objectives. |
| GP06 | CFD-to-1D scope and candidate ML models; `t.0` 8225–9301 | model/methods | A §§4–7,14,16 | Map needed CFD quantities, tunable physical terms and sensor outputs; retain NN/LSTM/GNN as candidates. |
| GP07 | Proposed workflow, provenance and offline-to-live use; `t.0` 9301–12983 | evidence/methods/plan | A §§10–11,14–16; HC03/13 | Recover the workflow substeps and model/data lineage; qualify local/average ratios. |
| GP08 | Initial work and straight-pipe prototype; `t.0` 12983–13878 | preliminary | B §7; MS01 | Use named master’s as primary feasibility groundwork; straight-pipe remains an optional test fixture. |
| GP09 | Historical milestones; `t.0` 13878–end | work plan | HC02 | Preserve sequence; do not repeat expired master’s dates or invent calendar approval. |
| GP10 | Moser discussion: measurable states, heat paths and analytical explanation; `t.oqk72z9ekxce` 0–1468 | model/preliminary | A §§2,4–5; MS01 | Explain model end to end; map parasitic heat/mechanical terms and insulation evidence. |
| GP11 | Historical input-builder and numerical controls; `t.oqk72z9ekxce` 1468–2708 | model/reproducibility | HC05; A §12 | Carry geometry units, defaults, discretization/refinement and convergence metadata; historical SAM-specific implementation is superseded. |
| GP12 | Developing shape-function thought experiment; `t.oqk72z9ekxce` 2708–end | methods/profile mapping | A §§4,13–14; HC07 | Compare inlet/adiabatic/heated development; retain flux and observation meanings. |
| GP13 | ACU ROM state vector and measurement/mean mapping; `t.z2o5qsfswqej` 0–1090 | model/methods | A §§1,5,7 | Recover allowed state/input definitions; ratios remain candidates, not adopted universal maps. |
| GP14 | Temporal history, slopes and state grouping; `t.z2o5qsfswqej` 1090–end | methods/transition plan | A §§1,11,16 | Distinguish nowcasting from future prediction; five-minute history and bins are exploratory choices. |
| GP15 | Raw/processed data, comparable observations and statistics; `t.8hf6j812amqb` 0–1344 | evidence/data organization | HC03/04; A §§5,8,15 | Raw/quality-controlled separation, measured/CFD/model values with uncertainties and lineage; retain flags. |
| GP16 | Physical calibration, bias correction and explanation; `t.8hf6j812amqb` 1344–3078 | methods/assessment | A §§4,6–8,11 | Separate closure correction, observation map and empirical discrepancy; compare correction size and out-of-case stability. |
| GP17 | Static geometry and thermal expansion at sensors; `t.8hf6j812amqb` 3078–3405 | evidence/observation | A §§5,8; HC03 | Record whether location/constraint changes matter; require evidence before adding an expansion correction. |
| GP18 | Steady operating groups and case-space coverage; `t.8hf6j812amqb` 3405–4032 | evidence/assessment | A §§9–11,15 | Group actual controls/configurations with qualified tolerances; old 5×5 bin counts are examples, not selected design. |
| GP19 | Shared data store and code/result identifiers; `t.8hf6j812amqb` 4032–4916 | evidence/work plan | HC03/13/15 | Specify dataset/model/case IDs and parents; historical tools do not select the current stack. |
| GP20 | Historical collaborator roles and VCU fluid; `t.8hf6j812amqb` 4916–5686 | work plan/evidence | HC02/13/15; N07 | Keep collaborator/program context; supersede SAM deployment/mineral-oil branch where current direction differs. |
| GP21 | Acquisition, state qualification, quality handling and deployment; `t.8hf6j812amqb` 5686–7457 | evidence/data organization | HC03/04/11; A §§8,10,15 | Keep immutable raw/flagged data and criteria/history; do not automatically remove every >4σ point. |
| GP22 | Real-time physical model and learned bias; `t.8hf6j812amqb` 7457–8252 | methods/work plan | A §§7,11,16; HC13 | Develop offline → replay → live where qualified; score uncorrected/corrected outputs separately. |
| GP23 | CFD updates, field ROM and pipeline roles; `t.8hf6j812amqb` 8252–8996 | methods/program integration | A §§14,16; HC15 | Distinguish field emulator, physical ROM and experiment prediction; preserve shared inputs and ownership. |
| GP24 | Uncertainty through measurements, CFD and reduced models; `t.8hf6j812amqb` 8996–9501 | uncertainty | A §8; HC14 | Separate temporal variance, reference error and total uncertainty; carry dependencies and unknowns. |
| GP25 | Transient model candidates; `t.8hf6j812amqb` 9501–9719 | transition methods | A §§11,16; HC02 | GNN is not a required architecture; choose retained physics/history based on assessed need. |
| GP26 | Sensor drift/loss, changing material/locations/losses; `t.8hf6j812amqb` 9719–9835 | assessment/operator branch | A §§5–8; HC03/13 | Preserve proposed diagnostics, time/version changes and sensor-loss assessment. |
| GP27 | VCU-to-ACU role and disagreement; `t.8hf6j812amqb` 9835–end | scope/assessment | B §§5–6; HC02/07 | Explain distinct facility contributions and transfer limits; mismatches motivate diagnosis, not pooled validation. |
| GP28 | Nick phases and absolute-scale/model-family reconciliation; `t.9u2zr362q8er` 0–end | experiments/methods | A §§9,15; HC12 | Preserve warm/cold preparation, scale-anchor alternatives and run-role changes; no protocol change inferred. |
| GP29 | Proposal feedback: feasibility, UQ, MSR relevance and schedule; `t.s748eovr9xd7` 0–end | motivation/preliminary/plan | B §§4,11; A §8; HC02 | Use master’s demonstration and sourced MSR motivation; schedule remains dated sketch; 25% claim not substantiated. |
| GP30 | Administrative candidacy/committee and older minimum-product notes; `t.wcv1ymyrszc4` 0–end | administrative context | current author decisions | Preserve as planning context; does not add physics requirements or settle current deadlines. |
| GP31 | Historical TRIGA/example outline; `t.6gjri81ohnp6` 0–end | historical structure reference | current author decisions | Do not import unrelated TRIGA objectives/results into the present thermal-loop proposal. |

## Useful sub-bullets restored in the prepared proposal

- Data lifecycle: raw → mapped/synchronized → quality-flagged → qualified window/group → calibrated/assessed comparison, with immutable parents and versioned transformations. [GP15/19/21]
- State groups: actual controls/configuration, within-group variability, source/sink independence and whole-case assessment; no fixed historical bin count. [GP14/18]
- Mapping/corrections: conservative bulk state → explicit sensor operator; separate physical parameters, observation correction and empirical discrepancy. [GP06/12/13/16/22]
- Numerical reproducibility: units, discretization, defaults, solver tolerances and sensitivity; numerical controls are not fitted physics. [GP11]
- Sensor evolution: calibration/drift, missing channels, sensor displacement and changing heat paths; quantify degradation before promising anomaly detection. [GP03/17/26]
- Program interfaces: versioned model/case/data identity, measured/inferred/predicted labels, uncertainty, replay/live modes and collaborator ownership. [GP07/19/20/23/24]
- Retained as historical/candidate material: SAM deployment, mineral-oil wording, raw local/average ratios, mandatory GNN, four-sigma deletion, old bin counts and expired master’s dates.
