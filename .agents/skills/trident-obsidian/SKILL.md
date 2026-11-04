---
name: trident-obsidian
description: "Maintain Obsidian wikilinks, embeds, properties and note organization when editing the Trident notes vault."
---

# Notes maintenance

The notes Git repository owns these files. Its `PROJECT_MAP.md` and
`X.Chat/00_navigation/OBSIDIAN_LINKS.md` define the current vault routes; do not
infer Mac paths from TACC paths.

- Preserve original subject-note names, attachments, embeds and source IDs.
  Original/frozen notes are exempt from mandatory new frontmatter.
- Use the established vault-root wikilinks under
  `MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/` for this vault.
  Keep extension/heading/block targets and escape table aliases as required.
  External URLs use ordinary Markdown links.
- Add concise properties to new maintained notes using the existing organization
  convention; preserve the author's requested bullet or prose format.
- Update the owning map/index for important additions. Before physical moves,
  follow the existing move-map/link-preservation workflow. Do not reorganize
  original source content just to make a new note look tidy.
- Run `python3 tools/check_organization.py` from the notes owner. Use the existing
  link checker for affected vault links; do not recursively traverse repository
  aliases or read the whole library.

Text/link checks do not authorize rendered-image inspection. Git is the notes
transport; existing session pull/scoped-commit/push rules remain in effect.
