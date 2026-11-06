---
title: TACC notes-agent map
status: maintained
owner: TACC researcher
updated: 2026-11-06
tags: [project/trident, doc/specification]
---

# TACC startup and authoritative sources

Verified November 3 on `c318-009.ls6.tacc.utexas.edu`, Linux,
`TACC_SYSTEM=ls6`, `SLURM_CLUSTER_NAME=lonestar6`:

| Owner | Verified path / short entry |
|---|---|
| Outer Trident router | `/scratch/09748/andresfierro231/projects_scratch/Trident/PROJECT_MAP.md` |
| HPC initiative | Outer root + `andrew_WorkSpace/trident_modeling_initiative/`; `AGENTS.md`, `START_HERE.md`, `coordination/BOARD.md` |
| Notes checkout | Initiative + `box/Trident_FlowLoop_Notes/`; separate notes origin |
| Proposal checkout | `/scratch/09748/andresfierro231/projects_scratch/Papers/UTexas_Research/Andres_Fierro_Dissertation_Proposal/`; `AGENTS.md`, `doc_support/agent/SHARED.md`, `TACC.md` |
| Materials | Initiative `config/materials/README.md`, selected candidate YAML and resolved run configuration |
| Geometry | Initiative `docs/geometry/second_extraction/README.md`; current VCU Rev9 decision |
| Box experimental imports | Initiative `box/data/`; original data paths remain compatibility symlinks |

- Re-verify the current host/paths, actual Git roots and expected origins before
  editing; another TACC allocation may differ. Read only assigned scientific
  tasks. Notes organization does not claim existing campaigns or lift holds.
- Mac vault/library/Papers aliases are not assumed here. The tidy checker maps
  repository-owned vault links logically to this checkout and reports external
  aliases as unavailable. Missing Mac mounts do not imply a missing source.
- Retrieve only task-required external references through approved local access
  workflows. Do not bulk mirror Box, library or external repositories.
- For proposal builds use `bash scripts/build_proposal.sh <output-directory>`;
  load `module load texlive/2023` in the same shell when needed and record the
  actual compiler version. Compile/text checks do not authorize viewing pages.
- Expensive processing/transfer belongs on a compute allocation. Durable work
  uses a saved sbatch submitted from a login node and atomic receipts, following
  initiative `docs/workflows/SLURM_BATCH_JOBS.md`. No detached-shell substitute.
- Preserve exact source paths/hashes, model/facility status and active study
  ownership when responding to the writer. A Git push establishes transport,
  not the other agent's scientific acknowledgment.

## Skill discovery — OPS-012

The notes checkout carries the canonical `.agents/skills/` and generated
`SKILLS.md` on Git pull. Use native metadata first; no global install or full-pack
reading. For another verified checkout, run the notes pack's offline
`catalog.py link --target '<actual-owner-root>' --apply` after its dry run.
The command and collision/ignore rules are in
`.agents/skills/_support/README.md` inside this repository. Setup is once per
machine/checkout; never guess another machine's paths. Existing Git and research
ownership rules still apply.

## Required notes Box publication — November 6

The author reads Box-backed Obsidian while agents collaborate through Git.
After EVERY successful notes Git push, publish the exact pushed revision to
the confirmed active Box notes folder and verify its file hashes. This applies
to direct pushes and git_session.py alike. Root GIT_WORKFLOW.md controls the
single workflow: reconcile independent Box edits, preserve differing versions,
copy only committed notes/attachments with no deletion mirror or alias/Git/raw
data export, and record destination, commit and copy/check results. GitHub-only
success leaves Box publication pending. Verify the actual target rather than
using the historical alias. Author-confirmed destination:
`box:Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes`; preserve the dated
pre_git snapshot. Restore/update the confirmed folder if absent.
Do not alter Obsidian/Box client setup or unrelated repositories as part of it.
