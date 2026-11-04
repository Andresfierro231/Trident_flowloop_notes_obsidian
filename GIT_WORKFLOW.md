# Git collaboration and local Obsidian cutover

The GitHub repository is the primary transport for notes, literature work and
HPC/writer handoffs. Original Box content remains preserved. Raw experimental
data and the initiative's code/reports are separate from this repository.

## Each work session

```bash
python3 tools/git_session.py begin
# Read the current instructions/handoff, edit, and perform relevant checks.
python3 tools/git_session.py finish \
  --message 'Update the literature synthesis and task handoff' \
  --paths 'X.Chat/02_synthesis/example.md' 'X.Chat/05_handoffs/example.md'
```

Substitute real task paths. `begin` checks for a clean worktree and pulls with
`--ff-only`; `finish` refuses preexisting staged changes, stages only named
paths, runs `git diff --cached --check`, commits actual changes and pushes the
current branch after a fresh fast-forward-only pull. With no edits, `finish` checks/pushes pending commits without
creating an empty commit. Git reports authentication/network failures normally.
The helper exits nonzero if a required step fails; never claim synchronization
on failure. Ordinary Git commands are equivalent when the same checks are kept.

Keep one editor/task per shared worktree. Independent simultaneous work should
use separate clones/branches. If the remote moves before a push, fetch it,
reconcile commits and any conflicts without discarding work, check the result
and push. No force pushes or automatic resetting/stashing of unknown edits.
For a long session, synchronize again at a clean checkpoint before further edits.

## Local-machine setup

Run on the local machine, in a directory outside Box's automatic sync tree:

```bash
git clone git@github.com:Andresfierro231/Trident_flowloop_notes_obsidian.git
cd Trident_flowloop_notes_obsidian
python3 tools/git_session.py begin
```

Open that checkout as an Obsidian vault, or link it into the existing vault
using the local machine's chosen folder arrangement. Keep the checkout itself
outside a second file-sync engine. This HPC task cannot reconfigure local
Obsidian or stop local Box clients.

Before switching, preserve any local notes not yet on Box/Git. Compare them with
the clone, incorporate the intended differences, then commit and push them.
Do not replace the local working copy blindly: the HPC intake only certifies
the Box snapshot at its recorded time. Verify internal links/attachment paths
in the local vault after choosing the arrangement; vault-wide references outside
this folder are not repaired by creating this repository.

Do not make additional writer edits in the old Box copy after cutover. Treat it
as the original snapshot unless a later deliberate reference import is needed.
Git synchronization does not wake another chat; the other session must pull and
read the current handoff. Repository visibility/access are controlled in GitHub;
this task does not alter the supplied repository's access settings.

## November 3 verified local setup

- Canonical local checkout: /Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian/ (outside Box).
- Stable vault route: MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/ is a per-machine symlink to this checkout. Box does not sync the alias. The original Box directory is preserved at the sibling Trident_FlowLoop_Notes_pre_git_2026-11-03; do not author there.
- Local source-byte reconciliation and old/new paths: X.Chat/01_sources/LOCAL_GIT_CUTOVER.json. That initial receipt pins the preserved local input, not later Markdown maintenance.
- Pull/push this repository AND the separate proposal repository at task boundaries. No automatic cross-repository commit or atomicity is implied; record a result for each.
