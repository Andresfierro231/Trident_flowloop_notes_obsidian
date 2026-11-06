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

The author confirmed the active folder as
`Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes`.
The rclone destination is
`box:Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes`.
The service listing found that path absent; restore/update this confirmed
folder and preserve the separate dated `pre_git` original. The author is not
being asked again for permission. Do not reconfigure the Obsidian client.

Publication uses an immutable export of this handoff's actual pushed commit.
`tools/export_box_notes.py` copies only regular Git-tracked files whose blob
hash matches that revision, records SHA-1/SHA-256, and skips tracked symlinks.
A fresh target inventory, dry-run, preserved-version or immutable copy and
one-way checksum check establish service delivery. The successful Box-only
`X.Chat/01_sources/BOX_PUBLICATION.json` records the verified commit and final
outcome; the modeling run retains full logs and source manifests. Until that
receipt exists, Git publication alone does not prove Box delivery.

Current task evidence is owned by Trident modeling at
`runs/2026-11-06_OPS-014_box_triangle/`. The resulting notes commit identifies
the instruction publication; its final run receipt records actual GitHub/Box
status and remaining work. No research goals, scientific execution holds,
experimental deposits or proposal working files changed.
