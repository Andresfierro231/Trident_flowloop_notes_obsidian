---
title: Immutable reference inputs
status: maintained
last_updated: 2026-11-05
tags: [project/trident, doc/index, facility/shared]
---

# Reference inputs

Tags: #project/trident #doc/index #facility/shared

This folder contains immutable source material and reviewed source snapshots.
Presence here does not make a source scientifically authoritative. Checksums,
origin, revision, applicability, and known conflicts must accompany imported
material. Runtime code must consume reviewed portable configuration rather than
depend on user-specific external paths.

[`MANIFEST.sha256`](MANIFEST.sha256) records the supplied bootstrap references.

Selected Box documents follow the pull-only
[Box access workflow](../docs/workflows/BOX_DOCUMENT_ACCESS.md) and are packaged
under [`box_imports/`](box_imports) with source manifests and checksums.

## November5 bootstrap relocation verification

`make references-check` uses [explicit relocation routes](manifest_routes.json)
to verify all15 original digests from the unchanged `MANIFEST.sha256`. Twelve
Nick-plan sources moved under their2026-09-14 edition; the missing bootstrap
specification is recovered byte-for-byte under [its original-source archive](bootstrap/README.md).
The two SAM inputs remain at their original paths. An extant old path is also
verified, so a changed original cannot be concealed by a routed copy. This
checks source integrity only, not scientific correctness or plan acceptance.
