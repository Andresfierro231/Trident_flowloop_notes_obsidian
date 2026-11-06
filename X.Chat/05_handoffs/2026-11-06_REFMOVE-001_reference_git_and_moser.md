---
title: Reference collection Git migration and Moser feedback
status: review
owner: agent-root-reference-notes-20261106
updated: 2026-11-06
tags: [project/trident, doc/report]
---

# Reference collection Git migration and Moser feedback

Tags: #project/trident #doc/report

- Author request: move the entire initiative reference directory into notes Git so it reaches the local computer. All 1,003 files (209,346,794bytes) now live in `reference/`, with original names and bytes unchanged. The old HPC `initiative/reference` path is a relative compatibility symlink; do not recreate a real directory there.
- Current route: [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/REFERENCE_INPUTS.md|Reference guide]]. Exact move/hash/check record: [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/reference_migration/2026-11-06/README.md|Move receipt]].
- Newly supplied Moser part2 and the existing October 14 note were read as text. [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/02_synthesis/MOSER_PROPOSAL_THROUGHLINE.md|Coverage and next actions]] connects application → completed work/literature → proposal, with model choices, parameters and validation together. No source feedback was rewritten.
- Proposal main `0c3a27478fdd5278005c97b6c415ae0dd314156c` is pushed: early aims, connected methods table and corresponding exact slide 3 script. Local PDF 45 pages; no undefined/overflow errors. Scientific inputs/results and bibliography unchanged.
- Still needed: sourced reactor/testbed/MSRE relevance, one fully specified quantitative master's case, matched heated two-code reconstruction and independent assessment, and study resource estimates. Existing literature should be checked before a new review is commissioned.
- Checks: 1,003 SHA256 matches;15 bootstrap digests;17 maintained organization documents;63 scoped navigation links;0 ignored reference files; original navigation snapshots preserved. No archive/image/CAD interpretation or scientific execution.
- Notes base pulled: `bbd567c10d602db6e895589c5f8fdb0b3892523e`. Publication is the notes commit containing this handoff; push outcome must be checked. Git availability does not prove a local pull or agent acknowledgment.

## Local continuation

Pull notes `main` in the existing local notes checkout, then use `reference/` or the reference guide. Run `python3 tools/relocate_reference_inputs.py --check` there to verify the original files. Pull the separate proposal repository independently for its matching outline/source update. No symlink or Box transfer is needed inside the local notes checkout for these references.

HPC root/modeling maps and instructions are updated locally. The parent workspace has unrelated uncommitted work; it was not staged or committed by this notes task. Scientific ownership and source/facility limits remain with their original owners.
