---
title: Notes conventions, machine routes and proposal technical reference
status: review
owner: agent-root-notes-appendix-20261103 / TACC
updated: 2026-11-03
tags: [project/trident, doc/handoff]
---

# OPS-008 handoff

- User scope: improve agent ordering/naming/structure/maps, make X.Chat
  expandable, add proposed sub-bullets under existing proposal goals and a
  technical appendix with material correlations. User explicitly requires
  different Mac and TACC instructions.
- Received bases: notes `0a87c9f`, proposal `fe5064a`. Verified on
  `c318-009.ls6.tacc.utexas.edu` (Linux, ls6/lonestar6). These are separate Git
  owners; use actual resulting Git history/remote state for publication identity.
- Proposal publication completed at `8fa1ee8` after a fresh pull; its worktree
  was clean. This records the actual proposal push, not a Mac pull/acknowledgment.
- New root `PROJECT_MAP.md` routes geometry/revisions, materials, sensors,
  heaters/coolers, model/assignment notes, meetings, library and proposal owners.
  Original subject notes and attachments remain unchanged.
- Shared startup/conventions are in `00_navigation/agents/SHARED.md` and
  `00_navigation/ORGANIZATION.md`; exactly one of `MAC.md`/`TACC.md` supplies
  machine paths/access/build instructions. Mac paths are recorded by that
  machine; they were not independently verified by this HPC task.
- Indexed every maintained X.Chat layer, added topic/handoff/study templates,
  notes status and continuing-study lifecycle guidance. The research-question
  map now points to the current four-chapter proposal argument.
- Archived only the completed `codex_markdown_test.md`, preserving its SHA-256
  and original-manifest identity in `01_sources/OPS-008_MOVE_MAP.json`.
  Existing frozen proposal packages, aliases and source IDs are preserved.
- `tools/check_organization.py` checks maintained metadata/indexes/links and
  classifies external owners without traversing aliases/archives. Its broader
  read-only audit found no repository-local link debt. `tools/git_session.py`
  now performs a fresh fast-forward-only pull immediately before push; seven
  local Git preservation/synchronization checks passed.
- Proposal: three nested proposed tasks under each existing aim; four main
  chapters/bullet format retained. Appendix A documents current HPC candidate
  material laws, Kelvin/SI units, allowed ranges/extrapolation, nominal VCU
  pipe/layer inputs and the polynomial heat-capacity integral.
- Exact material-source hashes/IDs/provenance are in proposal
  `doc_support/committee/MATERIAL_SOURCE_RECORD.json`; the appendix renderer
  uses that pinned record, and 125 numeric comparisons across seven candidates
  match the owning HPC implementation. No material model/source was changed.
- Important source limits: steel-note suggested rho/cp differs from configured
  VCU v3; appendix documents v3 and the difference. VCU Prop-30 still has no
  selected numerical fluid law; image-table coefficients were not inferred.
- Proposal build: pdfTeX 1.40.24 / TeX Live 2022, latexmk 4.77;
  `build/OPS-008_2026-11-03/main.pdf`, 18 pages, no undefined refs/citations or
  overfull boxes. No PDF/image/CAD visual inspection.
- HPC evidence bundle: initiative
  `runs/2026-11-03_OPS-008_notes_proposal/`. It includes source/check/build and
  publication receipts. A reused old Git test harness replaced its old output
  log; that provenance correction is documented in OPS-007 and current test
  copies are retained in OPS-008. Original notes/data/migration receipts are intact.
- Next: Mac agent pulls both repositories, uses its verified map, and continues
  the writer's requested task. This organization pass does not answer or
  acknowledge the prepared scientific-result request, lift holds, execute
  experiments/CFD or establish a new approved research aim.
