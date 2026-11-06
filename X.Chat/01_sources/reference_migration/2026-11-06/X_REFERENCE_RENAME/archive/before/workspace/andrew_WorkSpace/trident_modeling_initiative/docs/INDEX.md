---
title: Documentation index
status: maintained
last_updated: 2026-10-26
tags:
  - project/trident
  - doc/index
---

# Documentation index

Tags: #project/trident #doc/index

Read [Start here](../START_HERE.md) first. This index routes by question; it is not required reading for every task.

| Question | Primary document/folder |
|---|---|
| Where are TAMU flow profiles, developing flow, velocity-temperature covariance and buoyancy explained? | [Tagged TAMU reading guide and exact report sections](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/README.md#search-and-reading-guide-tamu-flow-profiles-mixed-convection-and-buoyancy) |
| Where are important derivations, numerical explanations and significant decisions? | [Curated important-report pointers](../reports/IMPORTANT_REPORTS.md) |
| Why does the project exist and what is the finish line? | [Project charter](project/CHARTER.md) |
| What problem are we solving now? | [Problem as understood now](project/as_understood_now.md) |
| What is the development-first HTC and temperature-mapping direction? | [DOC-028 inventory, author answers and proposal method](../reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-028_cfd_closures_profiles/README.md) |
| What closure-selection goals and thesis-grounded steps come next? | [RO-004 / DOC-027 and recirculation amendment](../reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-027_closure_selection/README.md) |
| What has Andres decided, and what remains open? | [Author interview and DP decisions](../reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-026_author_decisions/README.md) |
| What testable PhD contribution, prediction contract and evidence plan are proposed? | [Expanded proposal briefing](../reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/REPORT.md) and [staged actions](../reports/proposal/2026/10/phd_research_framework/2026-10-13/DOC-025_phd_contribution_questions/ACTION_ITEMS.md) |
| How do Clarno's read-only program drafts expand thesis context, and how are they cited? | [Vision/ModSim comparison and citation records](../reports/proposal/2026/10/phd_research_framework/2026-10-21/DOC-035_clarno_program_context/README.md) |
| Where is the current 1D M0–M3 model report? | [Instructions](../../../../Papers/UTexas_Research/Trident_specific/1d_solver_writeup/AGENTS.md), [README](../../../../Papers/UTexas_Research/Trident_specific/1d_solver_writeup/README.md) — external manuscript owner; historical source snapshot |
| What is the current state or blocker? | [Project status](../STATUS.md) |
| What does the provisional C1 geometry/configuration/M0 checkpoint establish? | [C1 evidence assembly](../reports/checkpoints/C1_2026-09-16/README.md) |
| Which durable research objectives are active? | [Objective registry](../coordination/objectives/README.md) |
| Which scientific/facility questions are unresolved, and what have we answered? | [Open-question board](../coordination/questions/BOARD.md) |
| What must Codex implement? | [Implementation brief](specification/CODEX_IMPLEMENTATION_BRIEF.md) |
| What control-volume equations and inner iteration does M0 actually solve? | [M0 mathematical write-up](theory/M0_CONTROL_VOLUME_AND_SOLVER.md) |
| What equations and full matrix does the steady no-flow filled-loop M1 solve? | [M1 mathematical write-up](theory/M1_STEADY_NO_FLOW_CONTROL_VOLUME_AND_MATRIX.md) |
| How does prescribed signed flow change the M1 energy balances? | [M2 equation note](theory/M2_PRESCRIBED_FLOW_ENERGY.md) and [verification](../reports/verification/M2_VERIFICATION.md) |
| How does M3 solve signed natural circulation, and what can be audited? | [M3 implemented equations and solver flow](theory/M3_NATURAL_CIRCULATION_MOMENTUM.md), [implementation checks](../reports/verification/M3_IMPLEMENTATION_CHECKS.md), and [separate equation checks](../reports/verification/M3_VERIFICATION.md) |
| Which cooler form and secondary outlet does the solver predict? | [Implemented cooler equations and audit contract](theory/STEADY_COOLER_MODEL_FORMS.md) and [focused checks](../reports/verification/COOLER_IMPLEMENTATION_CHECKS.md) |
| How will roots be discriminated under finer meshes and operating inputs? | [M3 root study plan](workflows/M3_ROOT_DISCRIMINATION_STUDY_PLAN.md), [phase-two candidate curves](../reports/verification/M3_ROOT_CONTINUATION_PHASE2.md), and [VNV-006 task](../coordination/tasks/VNV-006.md) |
| How will the next research phase compare Python to SAM? | [Declared SAM benchmark plan](workflows/PYTHON_SAM_FORWARD_BENCHMARK_PLAN.md), [actual component pilot](../reports/benchmarks/SAM_ONE_PIPE_ENERGY_BALANCE_PHASE1.md), and [SAM-001 task](../coordination/tasks/SAM-001.md) |
| What state order and numerical algorithm do M0/M1/M2 runs actually use? | [Versioned solver numerics and state order](theory/SOLVER_NUMERICS_AND_STATE_ORDER.md) |
| Does the steady solver exploit sparsity, and what checks support it? | [Structural sparse solver verification](../reports/verification/SPARSE_SOLVER_VERIFICATION.md) |
| What geometry is currently known? | [Geometry](geometry) |
| Where is the provisional ACU centerline and virtual-sensor schematic? | [VIS-001 schematic package](../reports/checkpoints/VIS-001_2026-09-16/README.md) |
| Which reduced-zone parameters can synthetic tests identify? | [IDN-001 identifiability report](../reports/verification/REDUCED_ZONE_IDENTIFIABILITY.md) |
| What do the experiments need to provide? | [Data and uncertainty contract](data/DATA_CONTRACT.md) and [experiment reviews](experiments) |
| Where are the ACU/VCU Box deposits and what has actually been pulled? | [Box deposit guide and dated inventory](data/BOX_DATA_DEPOSITS_GUIDE_2026-09-16.md) |
| Why was a consequential choice made? | [Decision records](decisions) |
| What assumptions remain active? | [Assumptions register](ASSUMPTIONS.md) |
| What findings should survive individual runs? | [Durable takeaways](TAKEAWAYS.md) |
| What happened chronologically? | [Journal](journal) |
| How should documents/folders be organized? | [Documentation standard](conventions/DOCUMENTATION_STANDARD.md) |
| How is a new subfolder initialized? | [Subfolder README template](templates/SUBFOLDER_README_TEMPLATE.md) |
| How is a run summarized? | [Run summary template](templates/RUN_SUMMARY_TEMPLATE.md) |
| Where is a long-lived research thread summarized? | [Research topic maps](maps) |
| Where are stable dataset/run/artifact identifiers kept? | [Registries](../registry/README.md) |
| How is documentation/navigation integrity checked? | [`tools/docs_audit.py`](../tools/docs_audit.py) via the [tool guide](../tools/README.md) |
| How do I inspect or copy a source document from Box? | [Pull-only Box document workflow](workflows/BOX_DOCUMENT_ACCESS.md) |

The broader `theory/MATHEMATICAL_FRAMEWORK.md` remains planned after M0
outside review and later model stages; the current M0/M1/M2 derivations are
provisional and implementation-specific.

Historical initialization instructions are retained in the
[bootstrap archive](bootstrap/README.md); they are not part of the live startup path.

## Approved framework contribution — 2026-10-14

[DOC-029: author-approved direction](../reports/proposal/2026/10/phd_research_framework/2026-10-14/DOC-029_rom_framework/README.md) expands RO-004 to the
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

## October20 research-development routes

- [Research roadmap](project/RESEARCH_ROADMAP.md): three stages and theory-change protocol.
- [Experiment requests](experiments/RESEARCH_DATA_REQUIREMENTS.md): Nick/Luciano data route.
- [Uncertainty](uncertainty/README.md): core budgets and propagation design.
- [Dashboard](dashboard/README.md): active collaboration with Ben Booth and NeutronOS.

Ethan thesis BC assumptions and upcomer recirculation: [agent shortcut map](maps/ETHAN_THESIS_BC_AND_RECIRCULATION.md), with primary-text routes and documentary/runtime/Trident evidence distinctions.

[TAMU portable coupled benchmark](theory/TAMU_POLAR_COUPLED_BENCHMARK.md) — implemented experimental model/solver contracts and full engineering guide; separate from ACU/VCU defaults.

### Domain-safe TAMU continuation

[Controlling numerical contract](theory/TAMU_DOMAIN_SAFE_CONTINUATION.md) and [study/qualification route](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-20/TAMU-TRIDENT-013_safe_continuation/README.md) cover own-model conservative state projection, feasible/recycled Newton–Krylov, residual/pressure homotopy, radial/angular qualification and declared-power circulation. Scientific producers are `trident_thermal.benchmarks.tamu.continuation_study`, `bounded_continuation`, `circulation_continuation` and `continuation_assessment`. Read the study's commands before running; preserve original attempts and use a new task directory. Exact native nonconformal accounting is not a blocker under the user's2026-10-20 direction.

## TAMU-TRIDENT-014 reconstruction specification

Owner: Trident modeling initiative; historical TAMU benchmark, review pending. [Complete manual](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-20/TAMU-TRIDENT-014_rom_manual/ROM_RECONSTRUCTION_MANUAL.md), [exact inputs](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-20/TAMU-TRIDENT-014_rom_manual/reconstruction_inputs/README.md) and [continued analysis](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-20/TAMU-TRIDENT-014_rom_manual/REPORT.md) specify every implemented equation/closure, source ownership, solver, assumptions and evidence limits. Builds on012/013 issued guides. No facility admission or independent validation.

**October21 priority:** [Friday October23 1D report, VCU CFD boundary derivation and bounded study prompts](../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/README.md). Modeling owns RPT-001 coordination; Papers/UTexas_Research/Trident_specific/1d_solver_writeup owns the manuscript. Current draft/evidence limits and pending studies are explicit; no new data processing or CFD launched.

## TAMU-TRIDENT-015 application decisions —2026-10-21

Owner: Trident modeling initiative, review pending. [Application/implementation chapter](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-21/TAMU-TRIDENT-015_trident_applicability/REPORT.md), [next-study protocol](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-21/TAMU-TRIDENT-015_trident_applicability/NEXT_STUDIES.md) and [future figure walkthrough](../reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-21/TAMU-TRIDENT-015_trident_applicability/FIGURE_WALKTHROUGH_PLAN.md) distinguish existing Trident features, transferable principles, proposed small extensions and TAMU-specific inputs. Source-linked continuation of014; no numerical result, model/configuration update or facility validation is added.

**Current VCU analysis direction, October21:** [Rev9 locations for all analyses](decisions/2026-10-21_RPT-006_rev9_all_analysis.md), including October1/September17 and section-specific resistances. Earlier Rev8 comparisons remain historical; recompute current station/section interpretation.

[Current section-specific Rev9 steady resistance analysis](../reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/comparisons/regional_resistances/README.md) provides heater/upcomer/downcomer/exposed-cooler R′ and finite R/G, conditional temperature inferences and source/assessment limits; RPT-006 receiving owner.
