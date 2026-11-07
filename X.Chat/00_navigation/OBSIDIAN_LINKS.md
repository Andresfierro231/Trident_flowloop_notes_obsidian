# Obsidian links and local repository aliases

- Actual vault root on this Mac: `/Users/andres/ObsidianVaults`. `MainVault` is a folder within it, not the vault root.
- The existing `MainVault/Box` symlink exposes Box; `MainVault/Documents` exposes Documents.
- New local alias: `MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/80_repository_links/Papers` points to the existing `Paper_and_Presentations` repository parent.
- Repositories stay at their existing locations. No repository was cloned, moved, copied or modified to establish this alias.

## Link rules

- Use wikilinks with paths from the vault root, using forward slashes and no leading filesystem slash.
- Include the real extension for non-Markdown files, such as `.tex`, `.pdf`, `.csv` or `.json`.
- Use an alias after `|` for a readable label; escape that separator as `\|` inside Markdown tables.
- Link only to existing files. Folder paths are plain pointers or link to a real README; they are not missing-note links.
- Keep machine-specific source paths as code/provenance text, never as bare `/Users/...` Markdown destinations.
- Do not use `~` or `$HOME` in wikilink targets: Obsidian does not expand shell variables there.
- The `.tex` target is the real LaTeX file. “Show all file types” is already enabled; Obsidian’s handling of nonnative files may use its installed viewer or the system application. A link is not a conversion from LaTeX to Markdown.

### Working examples

```text
[[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/LITERATURE_RESOURCES.md|Literature resources]]

[[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/80_repository_links/Papers/Trident_papers/lit_rev_codex/PhD_internal_litRev/methods_notes_and_sections/sections/01_what_prediction_must_the_model_make_and_what_information_can_it_use.tex|Prediction question and permitted inputs]]
```

## What stays portable

- Moving the vault to another disk or user directory leaves these links valid when its internal `MainVault/Box/...` layout is preserved.
- Moving the repository requires updating the local `Papers` symlink; the note links stay unchanged.
- Another computer needs its own `Papers` symlink pointing to that computer’s local repository parent. Box does not sync symbolic links or the external files they point to.
- Without that local alias or its target, the links cannot resolve. There is no native wikilink that automatically discovers an arbitrary external repository on every computer.
- Keep repository history/synchronization in Git. Although a clone may work locally in a Box directory, Box’s ignored hidden files and symbolic links make it unsuitable as a replacement for Git synchronization.

## Set up another Mac

- Use the existing repository parent or clone the repositories with Git outside Box.
- From this `X.Chat` directory, run the helper with that machine’s actual path:

```bash
python3 tools/setup_repository_link.py --papers-root "$HOME/projects/research/Paper_and_Presentations"
python3 tools/obsidian_links.py --vault-root "$HOME/ObsidianVaults"
```

- The helper refuses to overwrite an existing real folder or a different symlink, and rejects a parent/child loop.
- Keep symlink targets disjoint from the vault root and other mounted targets. Do not add a broad `Users` alias or another alias to the same Box tree.
- Configure a different `--papers-root` or `--vault-root` if that computer uses a different local layout. The wikilinks themselves remain the same.

## Maintain links

- After generating new working notes, run `python3 tools/obsidian_links.py --normalize`; it converts resolvable links and validates targets without following repository symlinks during its edit scan.
- The inventory generator now performs that normalization automatically.
- Do not blindly run generic recursive editors across `80_repository_links/Papers`: it exposes the real working repositories.
- The accidental `Users/.../*.tex.md` notes mentioned by the author are not source files. This task does not remove them; the author said they would delete them.

## Primary documentation checked

- [Obsidian internal links](https://help.obsidian.md/links): vault-root paths, extensions, aliases and missing-note creation.
- [Obsidian symlinks](https://help.obsidian.md/symlinks): target-disjointness, loop and sync limitations.
- [Obsidian settings](https://help.obsidian.md/settings): show all file types and link formats.
- [Box ignored file types](https://support.box.com/hc/en-us/articles/360044195433-File-Types-Ignored-or-Blocked-by-Box-Sync-and-Box-Drive): hidden files and symbolic links.

## November 3 live proposal route

- setup_repository_link.py now also creates 03_proposal/current pointing through Papers to canonical proposal. Dated staged aliases point only to frozen archive/staged snapshots for historical link compatibility. Box does not synchronize these symlinks; recreate them on each local computer.

- [OPS-015: active dated Box folder and verified local reconciliation](../05_handoffs/2026-11-06_OPS-015_active_box_reconciliation.md). Existing undated vault-root links still resolve through the local Git alias; they can open the Git copy. No vault rewiring or frozen-link rewrite was performed.
