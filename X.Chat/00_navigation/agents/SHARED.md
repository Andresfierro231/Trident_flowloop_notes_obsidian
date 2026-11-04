---
title: Shared notes-agent workflow
status: maintained
owner: notes coordination
updated: 2026-11-03
tags: [project/trident, doc/specification]
---

# Shared notes-agent workflow

1. Identify hostname/OS and actual Git root, origin, branch and worktree.
   Read exactly one machine map: `MAC.md` or `TACC.md`. For an unknown machine,
   verify owner paths before mutation; do not translate paths by substitution.
2. Synchronize notes and proposal independently under their existing Git rules.
   Read root `STATUS.md`, `PROJECT_MAP.md`, the relevant task/handoff and exact
   sources. Do not scan archives, inventories or the whole workspace at startup.
3. Claim a small scope with a unique owner/task in notes status; use the
   proposal status for manuscript edits and HPC board for scientific work.
   One agent edits a shared file at a time; use another clone/branch for
   simultaneous work. Preserve unrelated edits and source bytes.
4. Follow `X.Chat/00_navigation/ORGANIZATION.md`: one maintained topic owner,
   stable names/IDs, dated evidence and explicit current/historical roles.
   Record source/revision, facility/run, units and reading depth as relevant.
5. Add or revise map/index routes with important content. For a move, preserve
   hash/old/new path, update current incoming links, and leave issued evidence
   identities unchanged. Do not follow per-machine repository aliases in scans.
6. Run `python3 tools/check_organization.py` for maintained navigation and new
   conventions; use `--all-active` to report wider local/external link debt.
   Perform source/numerical/build checks when the task requires them. Treat
   images and CAD under the existing explicit-approval rules.
7. Leave one task handoff with changes, sources/limits, checks, Git commits,
   remaining work and actual acknowledgment state. Commit explicit paths,
   pull again on a clean tree immediately before push, and push each edited
   repository. A failed push is pending work; never force/discard unknown work.

HPC owns current research direction and qualified results; notes own literature,
synthesis and writing coordination. The proposal owns its rendered manuscript.
Explicit author direction controls intent. File recency does not alone resolve
a scientific contradiction or authorize execution.
