# VS Code: note links and photos

- Native Markdown preview renders standard Markdown links and image links. Mac: Cmd+Shift+V preview; Cmd+K then V preview beside editor. Cmd-click standard links in source.
- For this vault's Obsidian syntax, install **Markdown Wiki Links** (ltvan.markdown-wiki-links) in Extensions. Its documented features include aliases, heading links, image embeds and width syntax in preview.
- Open /Users/andres/ObsidianVaults as the folder: MainVault/Box paths then share Obsidian's root. X.Chat alone excludes other vault sources.
- Use built-in Markdown preview with the extension. Test an existing full-path note link and photo embed before any conversion. Symlink indexing and non-Markdown targets (.tex/PDF) require checking in your installed extension/version.
- Preserve original embeds/attachments; do not bulk rewrite the vault for one editor. Not every Obsidian plugin feature is reproduced.
- Syntax examples below are patterns, not claimed existing targets.
```
markdown
[[MainVault/Box/path/to/existing-note.md|Readable label]]
![[MainVault/Box/path/to/existing-photo.png|400]]
![Caption](relative/path/to/existing-photo.png)
```

- Exclude .git, builds, dated source archives and repository aliases from broad indexes/search where possible. Consult extension index exclusions; avoid following aliases in recursive editors.
- References checked 2026-11-03: [VS Code Markdown](https://code.visualstudio.com/docs/languages/markdown), [Markdown Wiki Links](https://marketplace.visualstudio.com/items?itemName=ltvan.markdown-wiki-links).
- No global settings or extensions installed by this sweep.
