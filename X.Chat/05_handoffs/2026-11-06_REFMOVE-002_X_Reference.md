---
title: X.Reference canonical rename and source-path repair
status: review
owner: agent-root-xreference-20261106
updated: 2026-11-06
tags: [project/trident, doc/report]
---

# X.Reference canonical rename and source-path repair

Tags: #project/trident #doc/report

The author’s local rename was verified and checkpointed before synchronizing notes. X.Reference is the sole physical source collection. The modeling reference symlink now points directly to it. Active maps, notes/proposal links and verifier defaults use the new name. No second notes reference directory is created.

[Full record, old/new source routes and checks](../01_sources/reference_migration/2026-11-06/X_REFERENCE_RENAME/README.md). Original manifests and source contents retain their issued identities; the resolver handles recorded old names and fifteen bootstrap relocations. All 1,003 original source hashes match, and 3,009 recorded/current source paths resolve. Nine geometry/ignore tests and 21 subtests pass; no scientific execution or image/CAD inspection.

Proposal main `19127c6` is pushed and its local 45 page PDF is clean. Notes publication is the commit containing this handoff after the finish/push succeeds; no local pull is inferred. Modeling navigation/tool changes are present in the shared HPC checkout; its unrelated pre-existing dirty work was not discarded, staged or blanket-committed.

On another machine, pull notes main, open X.Reference/INDEX.md and run `python3 tools/relocate_reference_inputs.py --check`. For an old recorded source: `python3 tools/resolve_reference_path.py reference/MANIFEST.sha256 --json`. The optional HPC compatibility symlink is outside the notes clone and is not required for local source verification.
