---
title: X.Chat maintenance tools
status: maintained
owner: notes organization
updated: 2026-11-03
tags: [project/trident, doc/index]
---

# X.Chat maintenance tools

Run the portable `python3 tools/check_organization.py` from the notes repository
root first. It checks managed routes without traversing aliases, archives,
images or CAD. Use `--all-active` for a read-only broader scoped link report.

| Existing helper | Scope / machine requirement |
|---|---|
| obsidian_links.py | Mac vault link checks/normalization; use explicit verified --vault-root. Normalization mutates authored notes; inspect scope first. |
| setup_repository_link.py | Explicit per-machine alias setup; verifies target and refuses conflicting paths. |
| refresh_inventory.py | Legacy Mac-specific source/figure refresh, with hardcoded local library/master routes and normalization side effects. Inspect before use; do not run it on TACC or as startup. |
| inventory_box_literature.py | Bounded local Box library metadata inventory; verify source roots before use. |

Scientific logic belongs in the HPC packages; these scripts do not qualify
models, process experimental waveforms or authorize library/Box duplication.
