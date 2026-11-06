---
title: Portable notes-repository tools
status: maintained
owner: notes coordination
updated: 2026-11-03
tags: [project/trident, doc/index]
---

# Portable notes-repository tools

Run from the notes Git root:

```bash
python3 tools/git_session.py begin
python3 tools/check_organization.py
python3 tools/check_organization.py --all-active --json-out /tmp/trident-notes-links.json
python3 tools/git_session.py finish --message 'Describe the task' --paths <explicit-task-paths>
```

The checker reads text/navigation metadata only. The default scope covers
maintained maps/indexes/agent guides; the broader option reports active notes.
It skips aliases, archives, dated proposal packages and images/CAD, and reports
external machine/library links separately. A clean report is scoped navigation
evidence, not scientific review or proof of external access.

Git session commands preserve existing work and fail on unsuccessful required
steps. Commit explicit paths and pull on a clean tree immediately before push.
Mac-specific historical inventory/link helpers are documented in
`X.Chat/tools/README.md`; inspect their paths and side effects before using them.

- Box literature discovery: [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/box_library/README.md|content catalog, bounded search and refresh]]. Tool: python3 tools/box_library.py; original PDFs stay in Box, source-specific notes and curation remain separate from generated records.
