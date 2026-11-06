---
title: "Canonical reference collection"
status: maintained
owner: REFMOVE-002 / notes coordination
updated: 2026-11-06
tags: [project/trident, doc/index]
---

# Canonical reference collection

Tags: #project/trident #doc/index

Work from `X.Reference/`. This is the only physical reference collection, versioned with the notes repository.

[Source categories and proposal feedback](../X.Chat/01_sources/REFERENCE_INPUTS.md) · [Rename, compatibility and verification record](../X.Chat/01_sources/reference_migration/2026-11-06/X_REFERENCE_RENAME/README.md)

Original filenames, source contents, hashes and issued manifests are preserved. The original `README.md` records the earlier HPC package and can contain historical relative paths; this index and the source guide are the current navigation. The separate PhD_internal_litRev repository continues to own active literature research.

For a recorded old path, from the notes repository:

```bash
python3 tools/resolve_reference_path.py reference/MANIFEST.sha256 --json
python3 tools/relocate_reference_inputs.py --check
```

The old modeling `reference` path is a compatibility symlink to this collection, not another data directory. Old notes `reference/` paths are resolved by the helper; a second physical folder must not be recreated. No source qualification, experiment or model result is implied by storage here.
