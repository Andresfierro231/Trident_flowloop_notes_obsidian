---
title: Trident notes project map
status: maintained
owner: notes navigation
updated: 2026-11-04
tags: [project/trident, doc/index]
---

# Trident notes project map

## Which Trident workspace?

| Explicit name | Owner / location | Consult it for |
|---|---|---|
| **Trident Notes** — this Git repository | HPC checkout: `/scratch/09748/andresfierro231/projects_scratch/Trident/andrew_WorkSpace/trident_modeling_initiative/box/Trident_FlowLoop_Notes/`; origin `git@github.com:Andresfierro231/Trident_flowloop_notes_obsidian.git` | Original geometry/material/model notes, literature, synthesis and writing coordination. `X.Chat/` is an organizational layer inside this repo. |
| **HPC Trident** — the research workspace | `/scratch/09748/andresfierro231/projects_scratch/Trident/`; entry `PROJECT_MAP.md` there; modeling owner `andrew_WorkSpace/trident_modeling_initiative/` | Current research direction, implementation, scientific tasks, decisions and qualified evidence. The outer workspace routes multiple repositories; it is not the notes Git repo. |

Either workspace can consult the other. Use the
[[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/HPC_CONTEXT.md|HPC return route]]
and the relevant Mac/TACC map; those absolute HPC paths are locators, not a
claim of Mac access. Name **HPC Trident** or **Trident Notes** in handoffs and
retain exact owner/path/revision. A source from the other side does not silently
supersede current direction or change authoring ownership.

Trident Notes is synchronized through GitHub. Its original Box source/snapshot
is preserved separately. The `box/` directory name and Mac vault alias do not
configure Box synchronization of this Git checkout.

Start with the question below, then read the named note and its exact sources.
This map locates evidence; scientific status remains with its owner. Keep this
map current when adding, moving or superseding an important note or source.

## Startup and ownership

- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/AGENTS.md|Agent entry]] → shared rules → exactly one Mac/TACC map → [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/STATUS.md|notes task status]] → relevant route/handoff.
- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/ORGANIZATION.md|Naming, ownership and lifecycle conventions]] govern new agent work. Original subject-note filenames and source IDs are preserved.
- HPC initiative: current research direction, implementation and qualified evidence. Notes: writer, literature and cross-project synthesis. Canonical proposal: separate LaTeX owner. Explicit new author instructions govern intent; discrepancies require reconciliation.

## Geometry, materials and measurements

For citations to numerical property laws, use the
[[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/MATERIAL_CITATION_GUIDE.md|material citation guide]]:
it distinguishes exact published equations, the notes' alternatives, product
data and configuration-only candidates. The proposal bibliography owns the keys.

| Need | Exact note / source route | What to read and how to use it |
|---|---|---|
| ACU/VCU geometry and revisions | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.1.0 Geometry notes.md\|Geometry notes]] | ACU assembly, tanks/heater and VCU revision sections. Use revision-qualified dimensions from the owning geometry record before calculation. Old conceptual drawings remain historical. |
| Geometry photographs and drawings | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.1.1 Geometry pics.md\|Geometry pictures]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/FIGURE_ROUTES.md\|figure routes]] | Original embeds, file/page references and selection purposes. A filename or photo is not a dimensional measurement. |
| Rev9 engineering tables | `1. Setup and Geometry/attachments/VCU_Rev9_CAD_Model_Package/data/VCU_Rev9_Engineering_Data.json` and `VCU_Rev9_Data_Dictionary.json` | Existing text derivatives; retain field/revision provenance. Current HPC geometry owner is `docs/geometry/second_extraction/README.md`; Rev9 controls current VCU analysis. Merely indexing these files does not authorize native CAD inspection or importing their values. |
| Earlier VCU geometry | `1. Setup and Geometry/attachments/VCU_Rev8_CAD_Model_Package/README.md`; `attachments/VCU_Rev7_Rev8_CAD_Comparison.md` in that same setup folder | Historical Rev7/8 comparison and source identity. Do not silently use these instead of current Rev9. |
| Pipe, insulation and fluid identities | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2 Main Material Props.md\|Main material notes]] | ACU/VCU insulation, nominal VCU pipe dimensions, products and the 30%-by-mass glycol note. November4 citation annotations and source table distinguish verified thesis/IAEA/manufacturer support from unresolved fits. Separate material identity, thickness and numerical property law. |
| VCU glycol properties | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2.1 Prop 30 ThermoPhys Props.md\|Prop-30 notes]] | Product/table and original-image routes. This note does not supply a complete text correlation library. HPC `config/facilities/vcu_provisional/fluid.yaml` still has no selected numerical property model; do not invent coefficients from images. |
| Steel correlations | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.2.2 Steel Pipe Properties.md\|Steel note]] | Suggested and crossed-out alternatives with original source pointers. Its suggested density/heat-capacity functions differ from the HPC VCU v3 candidate; select by explicit material/model ID rather than silently combining them. |
| Current executable material candidates | HPC `config/materials/README.md`, `vcu_candidate_materials_v3.yaml`, `acu_candidate_materials_v1.yaml` | The HPC owner records coefficients, units, library revision, allowed temperature range and evidence status. `materials/properties.py` owns Kelvin evaluation and out-of-range behavior. The proposal technical appendix transcribes these candidates; it does not select a new law. |
| Heater, cooler and insulation placement | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.1.0 Heaters and coolers.md\|Heaters and coolers]] | Heater coverage, insulation and cooler source routes. HPC CAL-019 owns accepted nominal dial/resistance estimates; generated electrical heat and net-fluid heat have distinct meanings. |
| Sensor meaning and locations | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.1.2 Sensors.md\|Sensor notes]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/1. Setup and Geometry/1.1.2.1 EPIC ACU Senor Names.md\|ACU channel names]] | Keep facility/channel/run/revision separate. The sensor note includes a Rev9 heading beside a Rev8 embed; check the actual asset revision. A point/probe reading is not automatically bulk temperature. |
| Historical specifications and additional pictures | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/A. Appendix/A.1 Interesting Pictures and drawing.md\|Additional pictures]]; `A. Appendix/local_version_drawings_frozen/` | Preserved drawings/specification notes; frozen history, not automatic current configuration. No image or CAD viewing is needed to navigate. |

## Model, research and writing

| Need | Exact route | Owner / limits |
|---|---|---|
| Explain the physical model | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/2. Model Notes/0.0 Intro to Model.md\|Model introduction]] | Cell states, heat paths and M0–M3 hierarchy. Verify current code and resolved model IDs in HPC before claiming implementation behavior. |
| Clarno/Nick steady exercise | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/Research/Clarno's Special assignment/Instructions.md\|Assignment]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/Research/Clarno's Special assignment/Nick's Steady State Heat Transfer Analysis.md\|Nick analysis]] | Original assignment/analysis context; does not activate a new study. |
| Introductory project context | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/0. Overview and intro/Trident - STNCL Loops.md\|Loop overview]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/0. Overview and intro/Digital I&C - Andres Notes.md\|I&C notes]] | Existing context notes; use dated decisions for current research direction. |
| Author goals and meeting context | `M. Meeting Notes/`; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/SOURCE_REGISTER.md\|N01–N12 register]] | N01 operator needs, N02 Clarno feedback, N03/N04 Luciano/VCU meetings, N12 Moser feedback. Original meeting dates and verbatim decisions remain identifiable. |
| Approved questions and synthesis | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/RESEARCH_MAP.md\|Question/workstream map]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/02_synthesis/RESEARCH_QUESTIONS_TO_PROPOSAL.md\|A1–K5 crosswalk]] | Goals/questions organize the work. Literature is an evidence resource; maintain existing source/claim/question IDs. |
| Literature and library sources | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/LITERATURE_RESOURCES.md\|Literature routes]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/BOX_LITERATURE.md\|Box library]] | Exact registries/review sections and source owners; inventory is not proof of reading. |
| HPC reports, code and decisions | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/HPC_CONTEXT.md\|HPC entry points]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/HPC_REPORT_MAP.md\|Saved report catalog]] | HPC `reports/IMPORTANT_REPORTS.md` and live task evidence govern current findings. Cataloged checkpoint reports are dated snapshots, not live status. |
| Current proposal and technical appendix | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/03_proposal/README.md\|Proposal route]] | Separate Git owner: `Andres_Fierro_Dissertation_Proposal`; `main.tex`, four `sections/outline/` chapters, then `sections/appendix/01_technical_reference.tex`. Verify availability in the machine map. Dated X.Chat packages are frozen. |
| Cross-machine questions and handoffs | [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/06_hpc_exchange/README.md\|Exchange]]; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/05_handoffs/README.md\|Handoffs]] | Git transports records; receipt, scientific answer and reconciliation are separate states. |

## Maintaining this map

For an important addition record purpose, exact owner/path, short entry point,
facility/revision when relevant, current/historical status and evidence limits.
Check local paths before publishing links. Keep unavailable machine-specific
paths as qualified pointers, never guessed clickable links. Update affected
folder indexes in the same edit; record physical moves in a hash-preserving map.

## Original material-equation sources — November4

See `X.Chat/01_sources/MATERIAL_CITATION_GUIDE.md` for exact support and limits.
The separate master's thesis owner is
`/scratch/09748/andresfierro231/projects_scratch/Papers/UTexas_Research/Master_support/csem-Masters_thesis/`:
`AGENTS.md`, `README.md`, `chapters/04_reduced_model_methodology.tex`.
It documents the adopted HITEC/legacy solid inputs. Rozak's separate CFD
appendix has differing laws; its exact page routes are in the guide.
The proposal owns `doc_support/committee/ORIGINAL_MATERIAL_SOURCES.json`.
Sources remain with existing owners; Mac locations require its machine map.

## Flowing and no-flow energy equations — November4

See [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/05_handoffs/2026-11-04_OPS-011_energy_balance_audit.md|OPS-011 energy-balance audit]].
The separate proposal owns `sections/outline/03_methods.tex` and
`doc_support/committee/ENERGY_BALANCE_AUDIT.json`. Latest author direction
restores combined fluid conduction and enthalpy transport; two short Peclet
sub-bullets explain their relative strength with a NIST citation, without a
high-Peclet requirement. This supersedes the initial advection-only draft.
Diagnostic M2/M3 conduction defaults are unchanged.96synthetic states verify
algebra, not facility applicability; no solver/configuration change was made.
