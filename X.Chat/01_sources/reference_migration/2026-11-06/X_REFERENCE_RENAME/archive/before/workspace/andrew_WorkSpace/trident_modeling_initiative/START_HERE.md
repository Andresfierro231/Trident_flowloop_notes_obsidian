---
title: Start here
status: maintained
last_updated: 2026-11-06
tags: [project/trident, doc/index, facility/shared]
---

# Start here

**Reference storage moved to notes Git:** [Current source guide](box/Trident_FlowLoop_Notes/X.Chat/01_sources/REFERENCE_INPUTS.md) and [preservation/compatibility record](box/Trident_FlowLoop_Notes/X.Chat/01_sources/reference_migration/2026-11-06/README.md). The old `reference/` path is a compatibility link. [New Moser feedback and draft gaps](box/Trident_FlowLoop_Notes/X.Chat/02_synthesis/MOSER_PROPOSAL_THROUGHLINE.md) is the current interpretation; original feedback stays immutable.

## Literature tools and initial documents

Start with the [agent quickstart](../../../Papers/UTexas_Research/PhD_internal_litRev/knowledge/AGENT_QUICKSTART.md). It names the separate PhD_internal_litRev owner, initial review/source documents, commands from Trident or the literature checkout, and the meaning of returned evidence. Read its AGENTS.md and latest handoff before edits. Use the current decision guide before historical gap reports. Retrieval is read-only and does not activate experiments or certify physical applicability.

**November 5 TAMU-EXP-013 — completed steady-film and source assessment:** [Full report and figures](reports/data/2026/11/tamu_experimental_inventory/2026-11-05/TAMU-EXP-013_steady_film_and_evidence/REPORT.md) · [Equation-to-code definitions](docs/theory/TAMU_STEADY_FILM_NET_LOSS.md). Owner Trident modeling / historical TAMU. Separate cooler amount/allocation/wall resistance, 167 comparison points, qualified restart controls, local parameter support and source-authority update. Modest June training gain fails consistent transfer; prescribed flow, unknown duty and hydraulic/observer limits preclude independent validation. Earlier issued reports remain preserved.


**Implemented five steady priorities — RES-002:** [Results and remaining acceptance gates](reports/research/2026/11/historical_study_value/2026-11-04/steady_evidence_implementation/README.md) — UQ contracts/controls,73 VCU payloads with recovered native October9, joint TAMU repair/order comparisons and prepared Luciano request. Numerical/source implementation complete for review; actual facility uncertainties and experimental commitments remain open.


**Proposal work right now:** [Current state and navigation](reports/proposal/2026/10/phd_research_framework/2026-11-04/committee_nine_day_plan/NOW.md), with current agent prompts, actual saved receipts, author answers and next owners.

**Continue the research:** [Steady-first studies, open work and delegable questions](reports/research/2026/11/historical_study_value/2026-11-04/research_continuation/README.md) — user-selected steady temperature/heat-balance milestone, uncertainty and evidence priorities, completed-study review, October9 VCU native-source lead and Ethan email draft.

**Active November13 delivery sprint — SPR-001:** Andres + Codex execute; Cole/Clarno review. [Control and parallel queue](reports/proposal/2026/10/phd_research_framework/2026-11-04/committee_nine_day_plan/CONTROL.md), board SPR-002–009, 46 subtasks and eight track workspaces. Final proposal AND matching Markdown PowerPoint outline with figure assets and exact speaker script due November13. Source-preparation queue is ready; scientific study/compute gates and existing owners remain in force.


**Find TAMU experimental plots and useful runs:** [Stable TAMU experiments map](docs/maps/TAMU_EXPERIMENTS.md) — most promising runs, grouped TP/TW, marked time regions, conditions, usable/unusable inventory and current model studies.

**November 4 completed overnight assessment:** [Heat paths, temperatures, regional pressure, circulation, recirculation and cost](reports/data/2026/11/tamu_experimental_inventory/2026-11-04/TAMU-EXP-009_overnight_assessment/README.md). Seven original jobs received; 1,474 unique attempts, 1,426 accepted states rechecked, 27 conditional histories and 71 PNG/SVG figure pairs. Numerical receiving is complete; phase, source/observer and corner-range limits prevent physical adoption. This expands the original November 3 TAMU report (two work dates; no promotion). Earlier submitted-status descriptions below are historical.

Tags: #project/trident #doc/index #facility/shared

## Current approved research scope — 2026-10-20

[The research roadmap](docs/project/RESEARCH_ROADMAP.md) and
[DOC-034 author directions](reports/proposal/2026/10/phd_research_framework/2026-10-20/DOC-034_goal_integration/AUTHOR_DIRECTIONS.md)
expand the October14 steady-core scope to three formal stages: steady
performance/margins; transitions; operational assistance. Uncertainty estimation
and propagation are central across all stages. Dashboard requirements and
interface development are active, with **Ben Booth and NeutronOS required
collaborators for all dashboard work**. This is approved direction, not a claim
of implemented/validated capability or automatic control authorization.

All additional experimental needs must be mapped through
[the Nick-plan data requests](docs/experiments/RESEARCH_DATA_REQUIREMENTS.md),
prepared for discussion with Dr. Luciano, and reflected in an agreed plan
revision before assuming data availability. Original sources are Phase0 checkout
plus Phases1–4 (the user's four-stage experimental route). Do not contact others
without explicit messaging authorization or edit original plan records.

Local recirculation has no direct measurements in the loop per the user.
Keep it distinct from bulk circulation; build on Ethan TAMU thesis only after
applicability review and qualified Trident CFD when available. **Ethan's thesis
was uploaded on 2026-10-20:** [CFD-001 receipt and trust-audit proposal](reports/proposal/2026/10/20/2026-10-20_CFD-001_ethan_thesis_intake/README.md).
The uploaded May2026 text/PDF identity is hashed; scientific/runtime verification
and Trident applicability remain pending. Do not keep requesting this upload.
For thesis BC/upcomer questions, start with [the dedicated shortcut map](docs/maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md), then only the named source pages.
Do not confuse first-order measured-temperature inputs with actual CFD BCs or
package review conclusions with verified executable case settings.
Do not transfer TAMU closure or validation claims to ACU/VCU. Uncertainty and
observability limits must remain explicit. The ACU processing hold is unchanged.

For a changed theory/model/UQ assumption, record source, proposed/approved/
implemented status and a dated decision; update the affected objective,
implementation-linked theory and evidence/tests. Follow the roadmap's change
protocol rather than leaving new theory only in a journal. Earlier scope
summaries below are historical where this amendment expands them.

## Approved framework contribution — 2026-10-14

[DOC-029: author-approved direction](reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-029_rom_framework/README.md) expands RO-004 to the
CFD–experiment order-reduction and physical-identification framework. Its
result is a fast interpretable physics-based ROM with assessed limits and a
reproducible closure-identification procedure. Learning physical parameters
from experiments is core; use plain wording rather than emphasizing inverse
learning. CFD and experiments both inform reduction and identification.
RO-005 remains the development-first HTC and temperature-profile component.
Use ROM for the reduced representation and surrogate for its predictive role;
remove misleading standalone emphasis and omit SAM from active proposal prose.
Steady core, conditional response-time extension, unseen assessment, CFD
uncertainty and the ACU hold remain controlling. No scientific execution is
authorized by these goals. Earlier answers remain historical; this dated
amendment governs the current contribution. Novelty still needs literature comparison.

## Current purpose

This repository develops a shared, configurable foundation for Clarno's physical thermal-network goals and Nick Luciano's experiment/reduction goals. Facility-specific inputs are separated under `config/facilities/`; never mix ACU and VCU data implicitly.

## Important reports and report policy

[Historical study value and model comparisons](reports/research/2026/11/historical_study_value/README.md) is the reading route for what earlier studies still contribute:47sources,18model families, adverse cases, specific later corrections and proposed research priorities. Use it alongside the curated important-report index; source reports and current decisions retain authority.

Use the relevant rows of [important reports, derivations and decisions](reports/IMPORTANT_REPORTS.md)
to find matrix/time-step derivations, fitting reconstructions and consequential
geometry/research decisions. Read exact linked sources rather than scanning
report trees. Maintain these pointers when significant work changes.

All future reports follow the [creation-date and continuation policy](reports/README.md#creation-date-reports-and-continuations):
one-offs in creation-day folders; expansions inside the original report in
dated subfolders; promotion to its creation month at three distinct work dates.

## Read next

- Latest proposal direction: [master closure inventory, development-conditioned HTC and temperature profiles](reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-028_cfd_closures_profiles/README.md), with all three author clarifications.

- Current closure-selection goals and author amendment: [RO-004 / DOC-027](reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-027_closure_selection/README.md). Recirculation is a possible example, not assumed facility physics.

- Latest proposal author direction: [preserved answers, decisions and staged actions](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-026_author_decisions/README.md).

- PhD proposal/thesis planning: [expanded context report and ten contribution questions](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/REPORT.md),
  [staged actions](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/ACTION_ITEMS.md),
  and [structured register](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/action_items.json).
  Contributions and criteria are proposed; these records do not authorize campaigns.

- Scratch-loss recovery: [verified archives, Git preservation branch and restore instructions](reports/operations/2026/10/13/2026-10-13_OPS-002_scratch_recovery/README.md)

- Latest-session closeout: [checks and Monday October 12 PowerPoint checklist](reports/data/2026/10/09/2026-10-09_DOC-023_vcu_session_closeout/README.md)

- VCU current geometry: [Rev9–ACU/Rev7 plots and working selection](reports/geometry/2026/10/vcu_rev9_review/2026-10-14/GEO-008_rev9_comparisons/README.md); [October 14 sensor/boundary decision](docs/decisions/2026-10-14_GEO-008_rev9_working_selection.md). JTC-B = PTC5 inlet, JTC-A = PTC6 outlet; STC5 uses Rev9. Top leg uninsulated; lower-leg heating assumed. Historical run applicability remains open; existing solver inputs are Rev8.

- VCU all-run heater/cooler settings and strict raw-temperature steady screen: [updated experiment index](reports/data/VCU_EXPERIMENT_INDEX.md), [CAL-016 evidence/methods](reports/data/2026/10/vcu_radial_wall_response/2026-10-21/CAL-016_all_run_conditions/README.md). All staged native/CSV identities; missing settings, date conflicts and integrity limits explicit.

- VCU all-run uncertainty and classifications: [experiment index](reports/data/VCU_EXPERIMENT_INDEX.md), [methodology](docs/data/VCU_EXPERIMENT_DIAGNOSTICS_METHOD.md); complete reports/plots and verified receipts (producer 3496297, finalizer 3496597).

- Solver/Clarno expanded Draft 2: [solver, matrices, experiments and timeline](reports/solver/2026/10/clarno_solver_guide/2026-10-07/DOC-019_expanded_solver_experiments/README.md); [first 20-minute draft](reports/solver/2026/10/clarno_solver_guide/2026-10-07/DOC-018_solver_clarno_presentation/README.md)
- Current VCU boundary, uncertainty and cycling analysis: [October 8 CAL-004](reports/data/2026/10/08/vcu_experiment_diagnostics/2026-10-08/CAL-004_vcu_boundary_followup/README.md)
- Completed VCU native noise and local response study: [October 8 campaign](reports/data/2026/10/vcu_radial_wall_response/2026-10-08/CAL-003_vcu_noise_response/README.md)
- Latest completed conditional wall study and property inference: [July 15 wall response](reports/data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_wall_response/README.md)
- Current experiment/PPT report: [July 15 reconstruction](reports/data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_july15_reconstruction/README.md)
- Latest VCU material/run decisions: [5 °C properties and July triage](reports/data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_5c_properties_and_run_triage/README.md)
- Current VCU analysis and slide handoff: [October 7 ambient tracking](reports/data/2026/10/vcu_ambient_response/2026-10-07/CAL-003_vcu_ambient_tracking/README.md)
- Tomorrow's VCU study and undergraduate handoff: [October 7 CAL-003](reports/data/2026/10/vcu_radial_wall_response/2026-10-07/CAL-003_vcu_next_day_handoff/README.md)
- Current VCU trend-processing handoff: [2026-10-05 job 3489368](docs/workflows/2026-10-05_VCU_TREND_HANDOFF.md)
- Current VCU experiment handoff: [2026-09-30 warm start](docs/workflows/2026-09-30_WORK_PLAN.md)
- Frozen pre-fit baseline: [C2 checkpoint](reports/checkpoints/C2_PRE_FIT_2026-09-21/README.md)
- Immediate dated agent handoff and user prompt: [2026-09-25 work plan](docs/workflows/2026-09-25_WORK_PLAN.md)
- Previous pre-fit handoff: [2026-09-22 work plan](docs/workflows/2026-09-22_WORK_PLAN.md)
- Selectable cooler equations and diagnostics: `docs/theory/STEADY_COOLER_MODEL_FORMS.md`
- Next solver/root study: `docs/workflows/M3_ROOT_DISCRIMINATION_STUDY_PLAN.md`
- Following SAM forward benchmark: `docs/workflows/PYTHON_SAM_FORWARD_BENCHMARK_PLAN.md`
- Bounded SAM source-sign evidence: `reports/benchmarks/SAM_SOURCE_SIGN_DIAGNOSTIC.md`
- Current synthetic M3 candidate curves: `reports/verification/M3_ROOT_CONTINUATION_PHASE2.md`
- Actual SAM one-pipe energy-balance pilot: `reports/benchmarks/SAM_ONE_PIPE_ENERGY_BALANCE_PHASE1.md`
- Current full-loop Python/SAM form gate: `reports/benchmarks/SAM_FULL_LOOP_FORM_GATE_V1.md`
- Current state and blockers: `STATUS.md`
- Current working truth: `docs/project/as_understood_now.md`
- Stable project mission and finish line: `docs/project/CHARTER.md`
- Shared work board: `coordination/BOARD.md`
- Categorized open questions and current answers: `coordination/questions/BOARD.md`
- Research-objective registry: `coordination/objectives/README.md`
- Governing implementation requirements: `docs/specification/CODEX_IMPLEMENTATION_BRIEF.md`
- Documentation routes and conventions: `docs/INDEX.md` and `docs/conventions/DOCUMENTATION_STANDARD.md`
- Long-lived research topic maps: `docs/maps/`
- Reviewed geometry summaries: `docs/geometry/`
- Durable scientific findings: `docs/TAKEAWAYS.md`
- Decisions: `docs/decisions/`
- Data contract and manifests: `docs/data/`
- ACU/VCU Box deposit locations and intake handoff: `docs/data/BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md`
- VCU Box Slurm transfer, landing, and working copy: [VCU landing workflow](docs/data/VCU_BOX_LANDING_WORKFLOW.md)
- VCU data and plots side by side: [plot index](reports/data/VCU_PLOT_INDEX.md) and [working run view](box/data/staging/working/vcu/runs/README.txt)
- Pull-only Box document access: `docs/workflows/BOX_DOCUMENT_ACCESS.md`

## Repository map

```text
src/trident_thermal/       reusable Python package
  geometry/                SAM importer, canonical geometry, mesh
  materials/               property interfaces and implementations
  boundaries/              ambient/heater/cooler closures
  network/                 nodes, edges, residual assembly
  flow/                    none/fixed/solved flow modes
  solvers/                 steady and transient solvers
  observations/            sensor registry and observation operators
  data/                    raw-format adapters and steady reduction
  calibration/             grouped parameters, objectives, uncertainty
  reporting/               figures, tables, checkpoint reports
config/                    reviewed portable YAML configurations
  facilities/              separate ACU and VCU configurations
  materials/               property models/tables
  model_forms/             reproducible physics/toggle combinations
  experiments/             experiment registries
  examples/                small regression configurations
  local/                   ignored machine/repository/storage paths
reference/                 immutable input/reference files
tests/                     unit, integration, regression, synthetic twins
docs/
  project/                 current working truth
  specification/           governing implementation requirements
  theory/                  tested equation-to-code documentation (later)
  geometry/                reviewed and generated geometry summaries
  experiments/             plans, reviews, and campaign interpretations
  data/                    canonical schemas and dataset manifests
  conventions/             documentation and navigation rules
  templates/               folder and report templates
  decisions/               append-only architecture/science decisions
  journal/                 dated chronological work
coordination/              board and small task packets
  objectives/              stable questions, success signals, and evidence links
  questions/               open-question board and categorized answer records
registry/                  dataset, experiment, parameter, run, and artifact IDs
reports/checkpoints/       timestamped, versioned scientific reports
runs/                      resolved configs/manifests/results; large data excluded
tools/                     audits, importers, checksums, maintenance
```

## Canonical workflow

```text
immutable raw/reference input
-> versioned importer
-> reviewed canonical config/data
-> validated forward model
-> synthetic recovery
-> real-data calibration
-> identifiability/uncertainty
-> checkpoint report
```

## Navigation rule

Do not begin by reading the entire repository. Read `AGENTS.md`, this file, `STATUS.md`, your task row/packet, and only its named files.

Unless explicitly qualified, "the board" means the task board. The
`coordination/questions/BOARD.md` file is the **open-question board**.

## Lightweight integrity check

Run `make check` for the standard test, documentation, coordination, and
reference-integrity checks. To run only the documentation audit, use
`python3.11 -B tools/docs_audit.py --root . --check`; it validates the hot path,
metadata, controlled tags, links, task references, folder indexes, freshness,
duplicate topic owners, and orphaned evidence without changing files.

## Setup reminder

If `config/local/reference_repositories.yaml` is missing or incomplete, remind the user to add the current ACU and VCU geometry/sensor repository paths and exact revisions. Use `config/reference_repositories.example.yaml` as the template. Provisional/virtual sensors may support tests but not scientific calibration.
