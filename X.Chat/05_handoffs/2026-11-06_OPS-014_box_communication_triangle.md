---
title: "Author amendment: keep Box Obsidian notes current after every Git push"
status: maintained
owner: OPS-014 / agent-root-box-triangle-20261106
updated: 2026-11-06
tags: [project/trident, doc/handoff]
---

# GitHub, agents and Box-backed Obsidian

Author direction November 6:

> While the mac agent codex uses git, my obsidian still uses box.

The author requests updating the Box Trident notes version after every Git
push so Box participates in the communication triangle. This supersedes the
archive-only/current-alias assumption for active Obsidian in earlier routes;
the November3 cutover and OPS-013 snapshot receipts remain historical evidence.

[[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/GIT_WORKFLOW.md|The controlling workflow]]
now requires: reconcile independent Box edits; push explicit committed task
paths; publish that exact revision to the confirmed active Box folder; preserve
differing versions and Box-only files; checksum-verify and record both GitHub
and Box outcomes. No deletion mirror, Git metadata, raw data or alias targets
may be exported. Shared, Mac and TACC agent instructions carry the requirement.
`git_session.py finish` prints the required Box reminder; it does not transfer
files automatically. Direct Git pushes carry the same duty.

## Active destination and delivery

The latest Box listing contained only
`Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes_pre_git_2026-11-03`.
The author has been asked whether to restore the standard active
`Trident_FlowLoop_Notes` folder or use that dated folder as active. This target
clarification is pending; no Box publication has been attempted, and no
Obsidian path/client has been reconfigured. Do not claim Box delivery until the
exact intended folder and checked copy are recorded.

Current task evidence is owned by Trident modeling at
`runs/2026-11-06_OPS-014_box_triangle/`. The resulting notes commit identifies
the instruction publication; its final run receipt records actual GitHub/Box
status and remaining work. No research goals, scientific execution holds,
experimental deposits or proposal working files changed.
