---
title: Reconcile the active dated Obsidian folder with Git
status: maintained
owner: OPS-015 / agent-root-active-box-20261106
updated: 2026-11-06
tags: [project/trident, doc/handoff]
---

# Active dated Box notes and Git

The author explicitly answered **The dated pre_git folder** when asked which
folder they open and edit in Obsidian. This supersedes OPS-014’s undated target
and the earlier archive-only assumption. Keep their vault setup unchanged.

- Agent Git owner: `/Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian`.
- Active author folder: `/Users/andres/Library/CloudStorage/Box-Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes_pre_git_2026-11-03`.
- Box target: `box:Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes_pre_git_2026-11-03`.
- The undated Mac notes path is a symlink to Git; writing there is not Box publication.
- Backups: `/Users/andres/projects/research/Trident/reconciliation/20261107T000512Z_active_box_notes/box_before` and `git_worktree_before`, with SHA-256 manifests in `before.json`. No symlinks followed.

## Reconciliation

All 371 cutover source files in Box still match the issued SHA-256 manifest.
352 shared paths are identical; 18 contain newer Git versions. No conflicting
author edits were found. Git has 1,164 additional files, including X.Reference
and the author’s unpublished meeting note, report and embedded image.

The sole new Box note, `0. Overview and intro/Update from git repo.md`, was
imported byte-for-byte. The old Markdown smoke test already exists unchanged
in Git’s issued OPS-008 archive; preserve the Box-only original without
restoring it to the active Git layer. Preserve all unpublished author-source
bytes, including the single trailing-space material-note edit. Exact source
paths have whitespace exemptions, following the repository’s existing source
preservation convention. No scientific source content was rewritten.

The shared, Mac and TACC maps and controlling Git/Box instructions now name
the active dated target. Existing undated vault-root links and local aliases
remain; those links can open the Git copy. Frozen records are unchanged.

## Verification and delivery

Organization check passed: 17 maintained documents, 93 resolving local links,
zero errors. Author source hashes and the report image target are verified.
Commit/pull/push the explicit task paths, then export that exact revision
with `tools/export_box_notes.py`. Recheck Box against `before.json` before
copying, preserve Box-only files and aliases, and checksum every regular
exported file afterward. No deletion mirror and no .git export.

Publication outcomes are recorded outside Git in the backup directory.
The active folder’s `X.Chat/01_sources/LOCAL_BOX_PUBLICATION.json` records
local mounted-file verification; it must state cloud verification separately.
This Mac has no configured rclone Box remote; noninteractive TACC SSH was
unavailable. A local copy alone must not create a cloud-success receipt.

Text/link/hash checks do not include image viewing, CAD parsing or scientific
review. The proposal and research execution holds are unchanged.

- Organization checker portability fix: ignore only `.DS_Store` when checking
  loose X.Chat files; keep the existing checks for actual loose notes.
