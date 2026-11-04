---
title: Mac notes-agent map
status: maintained
owner: Mac writer
updated: 2026-11-03
tags: [project/trident, doc/specification]
---

# Mac startup and local sources

- Select this map for verified Darwin hosts. Recorded local notes checkout:
  `/Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian/`.
- Recorded proposal:
  `/Users/andres/projects/research/Paper_and_Presentations/Andres_Fierro_Dissertation_Proposal/`.
  Read its `doc_support/agent/LOCAL.md` for its own source/library routes.
- Existing vault root is `/Users/andres/ObsidianVaults`; `MainVault` is inside it.
  Stable notes route: `MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/`,
  a per-machine alias to the Git checkout. Preserve the original dated Box snapshot.
- The library and Papers aliases belong to this Mac. Verify them before use;
  keep `X.Chat/80_repository_links/` and `03_proposal/current` outside recursive
  writers/staging. Recreate aliases only through the existing explicit setup
  helper with this machine's verified paths; never copy external repositories
  into the notes tree to make links resolve.
- Use vault-root wikilinks to existing files under the established `MainVault/`
  layout. Preserve extensions and PDF fragments; escape `\|` in tables.
  `X.Chat/00_navigation/OBSIDIAN_LINKS.md` owns the detailed local convention.
- Full local link validation: `python3 X.Chat/tools/obsidian_links.py --vault-root "$HOME/ObsidianVaults"`.
  Do not run a bulk normalizer across historical records or external aliases.
- The Mac writer may lack live HPC state. Use scoped Git questions with exact
  source IDs and wait for the actual response; backup catalogs are historical.
- Build the proposal with its own script/toolchain and explicit output directory.
  Reconcile local unpublished notes before replacing a working checkout.

These are recorded Mac locations, not access claims from the current TACC task.
If they change, the Mac agent updates this map and `LOCATIONS.md` after checking.

## Skill discovery — OPS-012

The notes checkout carries the canonical `.agents/skills/` and generated
`SKILLS.md` on Git pull. Use native metadata first; no global install or full-pack
reading. For another verified checkout, run the notes pack's offline
`catalog.py link --target '<actual-owner-root>' --apply` after its dry run.
The command and collision/ignore rules are in
`.agents/skills/_support/README.md` inside this repository. Setup is once per
machine/checkout; never guess another machine's paths. Existing Git and research
ownership rules still apply.
