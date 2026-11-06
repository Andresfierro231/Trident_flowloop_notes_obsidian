---
title: "Reference move into notes Git — November 6"
status: maintained
owner: REFMOVE-001 / notes coordination
updated: 2026-11-06
tags: [project/trident, doc/index]
---

# Reference move into notes Git — November 6

Tags: #project/trident #doc/index

The author explicitly requested this move so references travel through the notes Git repository to the local computer. The physical folder was moved, not copied into a second editable collection.

| Role | Path |
|---|---|
| Former HPC location | `trident_modeling_initiative/reference/` |
| Canonical location | `trident_modeling_initiative/box/Trident_FlowLoop_Notes/reference/` |
| Compatibility route on HPC | Former path is a relative symbolic link to `box/Trident_FlowLoop_Notes/reference` |
| Git owner / transport | `Andresfierro231/Trident_flowloop_notes_obsidian`, branch `main` |
| Source inventory | [MOVE_MANIFEST.json](MOVE_MANIFEST.json), one row per original file |

**Result:** all 1,003 files, 209,346,794 bytes, match their pre-move SHA256 values. The original directory structure, filenames, images, PDFs, ZIPs, supplied manuscripts, source manifests and feedback remain unchanged. No archive contents, images or native CAD were interpreted. This is preservation and organization, not a scientific review of the collection.

Original documents can retain historical HPC-relative links and paths. Use the [current reference guide](../../REFERENCE_INPUTS.md) for maintained navigation. The HPC compatibility link preserves current scripts and source-pinned receipts; it is outside the notes clone and is not needed for pulling/verifying the collection on the local computer. No new source material should be created in a second physical `reference/` folder at the old location.

## Repeatable verification

From the notes repository:

```bash
python3 tools/relocate_reference_inputs.py --check
```

This works after a local Git pull and requires no HPC source path. It compares the received collection to the move manifest. The helper's `--source /verified/initiative/reference` mode is a dry run; `--apply` performs the original atomic rename and creates the compatibility link. Do not reapply it to an already migrated alias.

The [dry-run plan](PLAN.json) and `archive/pre_move_navigation/` preserve pre-change navigation. Source contents were not edited to fix historical paths or formatting. Git whitespace checking is disabled only for the imported source tree and frozen migration snapshots; maintained notes retain normal checks. No large file exceeds 50 MiB; no LFS conversion was needed.

## Ownership and limitations

Notes Git now owns storage and transport of these references. HPC modeling retains current research direction, runtime code and qualified evidence. The separate PhD_internal_litRev repository remains the owner of current literature work; the moved `Lit_rev/` tree is supplied/reference history, not a replacement active literature checkout. Existing source/facility/revision limits, ACU processing hold and image/CAD inspection rules remain.

A successful push makes files available to the local notes checkout; it does not prove the local computer has pulled or another agent has acknowledged them. Root/modeling map edits remain local to the shared HPC workspace; unrelated dirty parent-repository work is not staged or committed by this notes migration.

## Proposal integration and current checks

The matching Moser update is published in proposal `main` at `0c3a27478fdd5278005c97b6c415ae0dd314156c`: an aims overview before methods and a connected model-choice/parameter/validation table; active slide3 states the same aims. Local main PDF is45pages with clean compiler/reference/overflow checks. Application/MSRE mapping, a quantitative master’s case and full-circle physical assessment remain open. No simulation inputs/results changed.

`checks.json` collects move verification,15bootstrap checks, notes organization and scoped navigation checks. `navigation_before_manifest.json` pins historical maps. Notes publication is the commit containing this receipt and is complete only after its push succeeds; local receipt is still unconfirmed.
