---
title: "X.Reference canonical rename and source-path repair"
status: maintained
owner: REFMOVE-002 / notes coordination
updated: 2026-11-06
tags: [project/trident, doc/index]
---

# X.Reference canonical rename and source-path repair

Tags: #project/trident #doc/index

The author requested completion of the local rename and repair of source paths. The source collection is now named `X.Reference/` in notes Git. The local rename was first checkpointed after verifying all 1,003 original files against the issued move manifest; the remaining updates repair consumers and publication. The current index is the only new file in the source tree.

| Location | Current role |
|---|---|
| `Trident_FlowLoop_Notes/X.Reference/` | Sole physical source collection, synchronized by notes Git |
| Modeling `reference` | Relative compatibility symlink to `box/Trident_FlowLoop_Notes/X.Reference` |
| Old notes `reference/` | Historical name; no second folder or alias is created there |

[REFERENCE_ROUTES.json](REFERENCE_ROUTES.json) records the prefixes and symlink change. The original [MOVE_MANIFEST.json](../MOVE_MANIFEST.json) and all issued source manifests retain their original bytes and paths. `archive/before/` preserves changed navigation and tool text.

## Source resolution

From the notes root:

```bash
python3 tools/relocate_reference_inputs.py --check
python3 tools/resolve_reference_path.py reference/MANIFEST.sha256 --json
```

The resolver accepts current, original modeling, original notes and vault-root paths. It also follows the existing fifteen-entry bootstrap name map when an old filename predates that relocation. `--from-dir DIRECTORY` interprets a relative link from its original document directory. `--sha256 DIGEST` checks the exact source. Missing or escaping paths fail; nothing is overwritten or executed.

## Active consumers

Notes maps, source/feedback guides and tools now use X.Reference. Modeling `make references-check` and the standalone verifier default to the canonical path; legacy `--root reference` is still supported through the repaired symlink. Active proposal source links are updated and its PDF rebuilt. Current navigation paths are repaired; immutable manifests, original sources and frozen before-files remain as recorded and use the resolver for replay.

`checks.json` records source hashes, all original source routes, all fifteen bootstrap routes, current links, existing geometry-import checks, organization checks, symlink resolution and the local PDF build. These checks do not authorize or perform scientific simulation, raw operating-data processing, native CAD parsing or image inspection. The parent modeling checkout has unrelated pre-existing work; this task does not reset, stash or blanket-commit it.

## Verified outcome

All 1,003 original source files retain their initial SHA256 values; the new INDEX.md is additional navigation. All 3,009 canonical/recorded source paths and 15 old bootstrap filename routes resolve. Both canonical and legacy bootstrap verification pass 15 digests. Existing geometry/import and ignore-policy tests pass 9 cases and 21 subtests. Current path checks cover 82 local links; 9 pre-existing external machine aliases are classified separately. Notes organization passes 17 maintained documents. Proposal main `19127c6` is pushed, with a clean 45 page local PDF.

Reproduce scoped route checks from notes: `python3 X.Chat/01_sources/reference_migration/2026-11-06/X_REFERENCE_RENAME/verify_paths.py`. Reproduce the modeling checks: `make references-check` and `PYTHONPATH=src python3.11 -B -m pytest tests/geometry/test_sam_import.py tests/unit/test_gitignore_policy.py -q`. These are infrastructure/source-access checks, not physical validation.
