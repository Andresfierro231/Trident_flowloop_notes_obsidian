# Obsidian link repair — November 2

- Task: ORG-PROP-20261102-05; author choice: live local symlinks.
- Confirmed actual vault root `/Users/andres/ObsidianVaults`; `MainVault` is an internal folder. Existing `MainVault/Box` and `MainVault/Documents` are folder symlinks.
- Created local `X.Chat/80_repository_links/Papers` → existing `/Users/andres/projects/research/Paper_and_Presentations`. No clone/move or source repository modification.
- Repaired 280 link/folder references across 26 notes; links now use vault-root wikilinks to existing files. Four folder references became plain nonclickable pointers where no real README exists.
- Initial validation checked 276 converted wikilinks with no missing/directory targets and no bare OS-path Markdown links. Later guide/handoff links are included in final validation.
- Obsidian’s quick switcher displayed the real `.tex` through the alias; opening it changed the window title. No `.tex.md` counterpart appeared; literature worktree stayed clean.
- [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/OBSIDIAN_LINKS.md|Linking guide]] explains portability and per-computer setup; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/tools/setup_repository_link.py|setup helper]] and [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/tools/obsidian_links.py|normalizer/validator]] are saved.
- The inventory generator now normalizes generated note links; recursive editors must not follow repository symlinks.
- Updated staged Markdown support links and pending patch; `git apply --check` passed. LaTeX/scientific content unchanged, so no manuscript rebuild needed.
- Current HPC request/export is revision 3 with the same seven questions. Earlier issued files/packages remain as superseded history. No reply or delivery acknowledgment is inferred.
- Next: use the repaired literature links normally. On another computer, set up the same internal alias before clicking repository-source links. Box does not synchronize symlinks.
