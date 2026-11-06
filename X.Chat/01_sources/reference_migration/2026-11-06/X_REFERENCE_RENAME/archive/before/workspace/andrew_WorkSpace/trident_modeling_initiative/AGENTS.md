---
title: Local instructions for coding agents
status: active
last_updated: 2026-10-20
tags: [project/trident, doc/specification, domain/agent_coordination]
---

# Local instructions for coding agents

Tags: #project/trident #doc/specification #domain/agent_coordination

The parent `andrew_WorkSpace/AGENTS.md` also applies here. Its shared policy
requires human approval before visual image inspection and sets the default
workflow for script reuse, compute receipts, and concise evidence reading.

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

## Mission

Build a traceable, conservative, modular thermal-network model for TRIDENT loop experiments. Scientific credibility is more important than minimizing residuals or rapidly adding features.

Honesty, transparency, and well-documented results and assumptions take
priority over progress, attractive results, or speed. State what was tested,
what was assumed, what failed, and what remains unknown. Never present
synthetic verification, numerical convergence, or calibrated agreement as
independent-person review or facility validation.

## Important report pointers — required maintenance

For model equations, numerical methods, assumptions or significant decisions,
consult the relevant rows in [important reports, derivations and decisions](reports/IMPORTANT_REPORTS.md)
and follow their exact sources before re-deriving or contradicting prior work.
This is targeted reading, not a request to inspect every report or activate
other tasks. When your task adds or materially revises a derivation, important
decision, evidence gate or major finding, update this index and its affected
category/map pointers before closeout. Include controlling document, purpose,
owner/facility, status/evidence limits and supersession where applicable.
Preserve historical decisions and keep canonical theory/decision records in
sync. Follow the report continuation/promotion policy below for all new work;
do not create a separate sibling report for a follow-up to the same study.

## Required reading order

Read only:

1. `START_HERE.md`;
2. `STATUS.md`;
3. `docs/project/as_understood_now.md` when the task changes scientific scope, facility assumptions, or experiment interpretation;
4. your row in `coordination/BOARD.md` for active work, or `coordination/REVIEW_BOARD.md` / `coordination/archive/BOARD_DONE.md` for an assigned review or historical task;
5. your named task packet;
6. any exact `coordination/questions/BOARD.md` rows linked by that packet;
7. the exact input/code files named by that packet.

Expand scope only when the task requires it. Record newly discovered dependencies on the board instead of scanning the whole repository.

"The board" means the lightweight active `coordination/BOARD.md`. Review and
completed task rows are in `coordination/REVIEW_BOARD.md` and
`coordination/archive/BOARD_DONE.md`. The separately named **open-question
board** is `coordination/questions/BOARD.md`; use its categorized answer records
instead of burying unresolved facility questions in journals or code comments.

When several agents share a worktree, use a unique owner label such as
`geometry / agent-geo-01`; a generic label such as `codex` is not sufficient to
distinguish concurrent work.

## Source hierarchy

### Dissertation-proposal context route

Newest direction: [master closure inventory and development-first HTC/temperature map](reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-028_cfd_closures_profiles/README.md)
records all three author clarifications. Analyze hydraulic/thermal development
before constructing HTC; first map centerline and radial/angular temperature.
Velocity mapping and detailed transient profiles are later. Coarse response
constants/settling estimates are the initial conditional transient direction.
RO-005 supplements RO-004. No new extraction, solver or operating-data work is
authorized by these proposal records.

Latest amendment (2026-10-14): [recirculation uncertainty and closure-selection goals](reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-027_closure_selection/README.md)
qualifies DP-02. Recirculation is a possible 3D-effect example, not established
ACU/VCU physics. RO-004 is the appended steady objective; CS-01--CS-08 are
proposed steps, not implemented or authorized research runs. Preserve previous
answers and apply the dated amendment when interpreting them.

Read the latest [author answers and DP decisions](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-026_author_decisions/README.md)
before proposing changes or asking already answered questions. The approved
question concerns needed mechanisms, predictive temperature/circulation and
model/evidence inadequacy. Closure selection and supported parameter combinations
are the method focus; states/paths are prerequisites. Record future changes as
dated DP amendments. Conditional CFD coordination and sensor-limit tasks are
staged in that bundle, not execution authorization.

For proposal/thesis contribution, physical reduction, prediction contracts,
uncertainty, validation roles or planned evidence needs, read the
[October 13 expanded briefing](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/REPORT.md)
and its [staged actions](reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/ACTION_ITEMS.md).
The author-confirmed dissertation core is a steady physics-based ROM and
CFD–experiment reduction/identification framework with ACU/VCU applications; SAM, transients, similarity and
real-time applications are bounded extensions. Proposed contribution choices,
tolerances, blind runs and one-facility contingencies are unresolved decisions.
Use action activation gates and existing task joins before promoting work;
the report neither authorizes execution nor lifts the ACU processing hold.
Keep this route separate from the broader project's solver/SAM research sequence.

### Scientific evidence precedence

1. conservation laws, units, and verified tests;
2. verified facility drawings/data and dated team decisions;
3. canonical reviewed configuration;
4. SAM/reference models;
5. informal prose and AI-generated specifications.

Never assume Claude, Clarno, SAM comments, or earlier code is mathematically correct. Preserve provenance and flag contradictions.

The declared solver-research sequence is the selectable ACU cooler,
then the M3 mesh/root-discrimination study, then a **like-for-like forward
benchmark against SAM**. The cooler is implemented synthetically; VNV-006
phase two now has source-hashed steady candidate curves, and SAM-001 has
both a bounded ACU source-sign probe and an actual synthetic one-pipe
energy-balance pilot. The latter checks shared M2 enthalpy physics only;
it is **not** a full M3 or facility benchmark. Future agents
should read `coordination/tasks/VNV-006.md`
and `coordination/tasks/SAM-001.md` before work in those phases. SAM is a
widely used comparison target, but agreement is not facility validation.
The [full-loop form crosswalk](config/examples/sam/acu_full_loop_form_crosswalk_v1.yaml)
is complete as a source-pinned **mismatch inventory**, not a matched case:
twelve fields differ and two remain unresolved. The comparison interface
requires an assessed, fully matched crosswalk before issuing M3/SAM deltas.
PHY-008 tracks the user's requested TAMU developing-flow profiles as an
optional follow-on **after** the forward-model gate; do not import them into
the baseline or create a runtime dependency on the external repository.
The current SAM ACU files use a positive-valued primary-fluid volumetric
cooler `heat_source`. A [paired one-step SAM run](reports/benchmarks/SAM_SOURCE_SIGN_DIAGNOSTIC.md)
shows its positive value warms the primary cooler outlet relative to the
negative value; this is **not** steady cooling or a like-for-like benchmark.
Physical equivalence to the jacket-wall sink, full source energy ledger,
geometry/topology/property crosswalk, and actual facility behavior remain
unresolved. The input's `T_amb` and `h_amb` are unused declarations.
Do not select a branch, hide a geometry/model-form mismatch, or tune a Python
closure merely to agree with SAM.

## Non-negotiable modeling rules

- SI units and kelvin internally.
- ACU and VCU configurations/datasets remain separate.
- M1 axial pipe-wall conduction is on by default when explicit positive wall
  axial areas and pipe conductivity are supplied; explicit off is a supported
  regression/assumption variant. No axial insulation conduction in M1.
- Do not assume the Jacobian is symmetric.
- Use one pressure reference for a closed loop; do not close it with two arbitrary pressure pins.
- Exit pipes use explicit topology modes; huge loss coefficients are not a sealed boundary.
- Heater input integrates to `eta_heater * Q_electrical` under every mesh.
- Cooler closures are swappable and their mode appears in results.
- Fit segment/zone parameters, never per-cell link values without an approved identifiability argument.
- Keep internal convection, wall conduction, insulation/contact, external convection, radiation, heater, cooler, and residual contributions separately reportable.
- Nick's effective reduced-zone model and Clarno's physical radial network are separate model families sharing common interfaces; do not silently interpret one as the other.
- Passive relaxation identifies time constants and some parameter ratios, not the absolute scale of both conductance and capacitance without a fixed or measured-power anchor.
- Do not interpret convergence as validation.
- Do not silently fix geometry or property conflicts.

## Code rules

- Python 3.11+, `src/` layout, type hints, small functions, explicit configuration.
- Reusable logic belongs in the package, not notebooks.
- No `eval` for SAM/config expressions.
- No hard-coded machine paths or credentials.
- No explicit matrix inverse.
- Keep node IDs, vector-order IDs, and solver-algorithm IDs explicit in
  resolved inputs/results. Do not assume a dense solve exploits physical
  sparsity, or claim optimization without paired accuracy and timing evidence.
- Every solver returns diagnostics and conservation residuals.
- Every model/run writes a fully resolved configuration and an explicit model-form/property summary.
- User amendment2026-11-03: every new model prediction and failed attempt records elapsed wall-clock runtime with model, geometry, closure/parameter, observation, solver, input, initialization, source and hardware/thread identity. Separate prediction from later scoring/I/O, and report per-step costs for transient forecasts. Preserve old costs with their original forms; do not infer FLOPs from CPU peak times runtime.
- Geometry/reporting code must be able to plot the centerline, component boundaries, sensor points, and heater/cooler regions from canonical configuration.
- Add/modify tests with every physics change.
- Preserve user changes and unrelated worktree state.

## Task coordination

For durable scheduler jobs and backups, read
[the local Slurm batch-job workflow](docs/workflows/SLURM_BATCH_JOBS.md).
Submit `sbatch` from a login node, preserve job/log/receipt handoffs, and keep
the user conversation available. This local route incorporates Ethan's
scheduler guidance without activating its separate tasks or board.

### Facility-specific experimental evidence (2026-09-29 user direction)

ACU and VCU channel maps, installed sensor locations, units, calibration,
quality codes, clocks, run metadata, heater/cooler conditions, steady windows,
and data-role decisions are separate deliverables with separate board rows and
acceptance checks. Evidence or a completed task for one loop never satisfies
the other loop's requirement. Shared schemas and code may be reused, but each
dataset must retain its own facility ID, immutable geometry revision, run ID,
source hash, mapping revision, and reviewed physical meaning. A site-repository
channel/instrument declaration is candidate evidence until its source revision
and applicability to the exact experiment installation are checked. The user
paused ACU operating-data processing on 2026-09-29; preserve its documented
questions and do not resume that processing without new user direction.

Before editing, claim one task by setting its board status to `in_progress`, owner, and start date. A task packet must name permitted files and acceptance checks. Do not edit files owned by another active task without coordination.

Treat all three task registries, `STATUS.md`, and the current journal as serialized
integration files. Re-read each immediately before patching it, preserve changes
from other agents, and keep the edit limited to your own claim or closeout. If a
concurrent edit cannot be merged unambiguously, record task-local evidence first
and ask the coordinating agent to integrate the shared-file update.

On completion:

1. run the named tests/checks;
2. attach evidence paths/run IDs to the task packet;
3. update `STATUS.md` if project state changed;
4. add chronological detail to today's journal;
5. promote durable scientific findings to `docs/TAKEAWAYS.md`;
6. create a decision record for consequential choices;
7. mark the task `review`, not `done`, unless the packet names you as reviewer; move its row from the active board to the review queue. A named reviewer moves an accepted `done` row to the completed archive.

Never leave completed or review rows on the active board. Keep rows brief and
put details in packets and evidence. Preserve task packet paths and history;
archival removes old rows from the live board, not their provenance. Check
the registry split with the documentation audit after task transitions.

## Documentation maintenance

Run the documentation audit at least weekly and before checkpoints. It checks links, stale status, task references, orphaned outputs, and whether findings were promoted. It may create tasks but may not rewrite conclusions automatically.

Keep `START_HERE.md` and `STATUS.md` concise. Journals are chronological; takeaways are curated; decision records explain why; reports preserve checkpoint evidence.

Document every solver algorithm and model-form change against implemented
equations and tests. Version the algorithm and state-order contracts in code
and run bundles; update their implementation-linked notes, verification
reports, assumptions, and limitations whenever behavior changes. Report the
code revision and resolved configuration with results. If documentation is
behind code, flag the mismatch openly and repair it before using the claim.
Add or update an automated code/documentation contract test for changed
algorithm IDs, state-order IDs, and selection thresholds; `make check` must
pass before claiming the implementation and its documentation agree.

For the initial M0--M3 solver draft at
/scratch/09748/andresfierro231/projects_scratch/Papers/UTexas_Research/initial_solver_writeup,
do not open or visually inspect compiled PDFs or derived page images.
Check the LaTeX source, compiler status, and logs only, to conserve
tokens. Ask the user before any visual PDF/image review. Keep the
paper repository's own AGENTS.md aligned with this instruction.

Follow `docs/conventions/DOCUMENTATION_STANDARD.md`. New maintained Markdown documents use front matter, a controlled Obsidian-style `Tags:` line, exact relative links, and one clear topic owner. Every new durable topic folder gets a short `README.md` based on `docs/templates/SUBFOLDER_README_TEMPLATE.md`.

## Report continuation and promotion — approved 2026-10-20

One-off reports belong under `reports/<category>/YYYY/MM/DD/<report>/`, dated
by creation. Expand the original report using `YYYY-MM-DD/<expansion>/`
subfolders inside it; keep one README/current report and preserve dated evidence.
When the original and expansions record **three or more distinct work dates**,
promote that same report to `reports/<category>/YYYY/MM/<report>/`, anchored to
its creation year/month. Later calendar months or new task IDs do not create
another report home. Separate substantive investigations and categories remain
separate; ACU/VCU evidence ownership remains explicit.

Use `report_study.json` with `created_date`, `work_dates`, category, title and
expansion/source provenance. Actual date subfolders determine the count; count
neither elapsed calendar time nor experiment acquisition dates. Keep one-offs
at day depth. Snapshot text/manifests before path repairs, conserve scientific
bytes, update current incoming links/producers and retain documented legacy
aliases only for source-pinned consumers. Runs/raw acquisition ownership stays
unchanged. The [documentation standard](docs/conventions/DOCUMENTATION_STANDARD.md)
and [organization study](reports/operations/2026/10/07/report_organization/README.md)
record implementation and migration evidence.

Run `python3.11 -B tools/report_layout.py --index` after changes, then `--check`.
The audit accepts dated expansions and enforces the third-date promotion;
legacy date-only migration must not pull expansions out of their parent study.

Review the repository map, folder indexes, tags, and orphaned content at least every 14 days. Do not make agents scan broad directories to infer current work; update the hot navigation path and task packets instead.

The mathematical framework document is intentionally deferred until M0 and canonical model objects exist. When it is created, derive it from tested residual assembly and link equations to code; do not write a speculative matrix that the implementation must later imitate.

## Setup reminders and external references

At initial setup, check for `config/local/reference_repositories.yaml`. If it is absent or contains placeholders, explicitly remind the user to add the read-only repositories/revisions containing current ACU and VCU sensor locations. Continue only with clearly labeled virtual/provisional sensors, and block real-data calibration until the relevant sensor map is verified.

External repositories are read-only inputs. Import reviewed portable configuration with source path and exact revision; never create a runtime dependency on a user-specific path.

Treat externally created CAD as a high-risk evidence source, not an ordinary
document. Seriously hesitate before reading, opening, importing, recomputing, or
executing anything from a CAD file or CAD archive (`.FCStd`, `.STEP`, `.STP`,
`.STPZ`, embedded macros, or similar) that this project did not create. Ask the
user for explicit confirmation tied to a bounded task before doing so. Prefer
owner-supplied text, CSV, JSON, and other non-image derivatives; indexing a CAD
filename or checksum does not authorize opening its contents.

Facility model defaults must remain constructible from reviewed system objects
or portable external configuration. Implement and validate ACU first, then VCU,
without coupling their configurations. The reviewed ACU Rev B written/tabular
package is the best current ACU geometry evidence and has higher evidence weight
than approximate SAM values, but unresolved conflicts stay explicit. Review
machine-readable/text dimensions without opening the underlying external CAD.
Image-only or CAD-native review requires a separately confirmed task.

When a task exposes an unanswered scientific or facility question, add or
update one categorized row and answer record under `coordination/questions/`.
When evidence resolves it, preserve the earlier uncertainty in the record,
change the row status, and link the deciding evidence. At natural review points,
agents may nudge the user about one or two highest-impact `waiting_user` items.

## Data safety

Assume scratch can disappear. Raw data is immutable and never stored only on scratch. Verify checksums and durable-location manifests. Do not commit raw/large data or secrets to git. Cleanup/sync tools require narrow targets and dry-run support.

Box document access follows `docs/workflows/BOX_DOCUMENT_ACCESS.md`. It is
pull-only by default: inspect first, copy exact sources into ignored staging,
and promote only reviewed references with provenance and checksums. Never place
rclone/Box credentials in this repository or use `sync`, remote deletion, or an
outbound copy without a separately approved task.

## Output ownership

Follow the [workspace-root ownership rule](../../AGENTS.md#workspace-root-artifact-ownership). Resolve modeling outputs under this initiative; the outer workspace must not acquire loose `reports/`, `runs/`, `sam_runs/` or `scripts/` directories. The OPS-004 map preserves legacy locations without root aliases.

Specialist workflows use the parent [skill catalog](../SKILLS.md) or native skill
metadata; read only a relevant skill when needed, following the parent discovery rule.


## Author-required Markdown readability — November5,2026

- Embed scientific figures inline as `![descriptive caption](path/to/figure.svg)` (or another supported image format). A plain `[label](...)` is a download/source link, not a displayed figure. Include a meaningful caption, units, data/source route and explanation of what the reader should notice.
- Delimit display math in Markdown with `$$ ... $$`, not LaTeX `\[ ... \]`. Define symbols and units before use. This rule applies to Markdown; LaTeX source uses its normal environments.
- Explain the engineering question and model before a plot. State whether values are specified inputs, constructed synthetic values, measured observations or predictions. Expand specialist terms (for example, assumed range rather than undefined support; independently checked result rather than undefined oracle).
- CSV files are data, not images: provide a normal link plus a small Markdown table preview with headings/units; do not use `![CSV](...)`.
- Preserve author comments and the pre-revision text before editing; record how each comment was addressed. If the author is actively editing a file, prepare a separate companion revision until coordinated.


## Latest author direction — prioritize heated VCU experiments

Near-ambient VCU records with very small STC/PTC differences are deferred. The author reports time-varying window heating and sensor-dependent view factors; do not continue ambient-only/passive material or wall-storage inference for these records. Prioritize heated VCU records and keep their ambient boundary input. Preserve historical reports. Constructed synthetic cooling examples remain method checks, not deferred experimental data. The separate100Wsynthetic SAM wall-storage failure still needs numerical/ledger diagnosis; do not attribute it to absent window forcing. See the sprint2026-11-05/HEATED_EXPERIMENT_PRIORITY.md for source, scope and evidence limits. No ACU hold is lifted.

## Author direction November6: editable math and purposeful figures

- Write equations as native editable math. In Markdown use display `$$ ... $$` (and ordinary inline math); in LaTeX use native math environments. Define symbols and units before use. Do not turn equations into SVG/PNG/PDF panels merely to fill a figure slot.
- Use a native Markdown or LaTeX table for a short comparison, parameter list, units/closure list or evidence matrix. Do not render a small table or prose as an image with oversized boxes and unused space.
- Create a figure when its graphical structure adds information: spatial geometry, a heat/flow path, a meaningful process relationship, data/response curves, an uncertainty/error map or a schedule. Keep the equation or small table beside it in editable text when that is the point being explained. An author request for figures does not require converting every explanation to an image.
- Preserve earlier assets/provenance when replacing a text-only figure; mark the preferred native presentation so later regeneration does not restore the image by default.
- The author welcomes specific requests for image review when appearance is uncertain. Ask which named image set may be viewed and for what purpose under the existing AGENTS visual-approval rule; this invitation is not blanket permission to inspect images or PDF pages. Continue text/numerical work while optional review permission is pending.

- Author font/layout amendment November6: fit the figure canvas to the information. For new slide diagrams, start near16–18pt body labels and22–26pt titles; for quantitative plots start near14–16pt axis labels and12–14pt ticks/legends. Reserve10–11pt for nonessential source notes. Prefer fewer well-labelled panels, a smaller canvas or native text/table over shrinking the argument into tiny labels or leaving large empty boxes. Use programmatic bounds/layout checks first; visually inspect only the approved named image set when needed.

- Direct-edit authorization: when the author explicitly requests edits in the active document, follow that instruction rather than creating a companion against their request. Preserve the latest annotated version, make scoped edits and record comment dispositions. The November6 active-outline request is such authorization.

## Author requirement November6: every simulation result needs its actual case

Whenever mentioning or showing a simulation result (including a failed run), include or link a comprehensive, reader-facing **model/assumption/boundary/input table before the claim**. A hash manifest, case name or figure caption alone is insufficient.

The case record must state: engineering question; physical vs synthetic vs algebraic status; solver/model form and unknowns; equations/closures and terms retained/omitted; geometry/topology/dimensions; material laws, units and applicability; all boundary and initial conditions; source magnitude, location and allocation; fixed parameters vs estimated/tuned parameters with bounds/data and uncertainty basis; mesh/basis/discretization, time scheme, requested AND accepted timestep/time horizon, solver controls and convergence/failure gates; output/observation definitions, reference and postprocessing; result scope and numerical/physical limits. Explain simulated time versus wall time and a transient extension versus a canonical steady model.

Link **all source input files actually run**, including the executed deck/config, resolved CLI overrides, geometry/mesh/material/closure files, scripts and execution/completion evidence. Pin revisions/hashes and preserve compact immutable input copies where appropriate. Distinguish an archived as-run input from a later template or prepared/unexecuted case; record missing provenance instead of substituting a plausible file.

Every displayed result needs a full engineering explanation in the report/technical appendix and a teachable short explanation in the presentation. Explain axes, units, cases, comparisons, sampling/interpolation and uncertainty before the plot. Define symbols before equations. Known/fixed, independently trusted, uncertain and estimated are different categories; never call a fixed synthetic value a well-measured physical property.

If the case/model/input explanation is incomplete, withhold the result from the presentation and rendered proposal until repaired. Preserve its issued sources as historical evidence. Do not hide an unexplained figure in an appendix. Do not claim numerical tests or matching hashes demonstrate human understanding, physical validity, an independently assessed prediction or publication readiness. Use the owning case-record template and record remaining questions explicitly. Direct active-document edits remain authorized by the author; preserve annotations and record their disposition.

Use [the simulation case-record template](docs/templates/SIMULATION_CASE_RECORD.md) before adding results. The [current explained-case example](../../../Papers/UTexas_Research/Andres_Fierro_Dissertation_Proposal/presentation/SIMULATION_ASSUMPTIONS.md) and [figure admission/disposition](../../../Papers/UTexas_Research/Andres_Fierro_Dissertation_Proposal/presentation/FIGURE_READINESS.md) demonstrate the required level of detail.


## Reference storage owner — November6

The author moved the complete reference collection into `box/Trident_FlowLoop_Notes/reference/` so notes Git transports it to the local computer. The old `reference` path is a compatibility symlink for existing source-pinned consumers; do not replace it with a second real directory. Read the [current reference guide](box/Trident_FlowLoop_Notes/X.Chat/01_sources/REFERENCE_INPUTS.md) and notes owner instructions before changing stored references. Scientific authority, immutable-source policy and execution holds remain with the modeling/source owners.
