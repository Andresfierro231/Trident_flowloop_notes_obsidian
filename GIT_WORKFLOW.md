# Git collaboration and local Obsidian cutover

Agents use GitHub for notes, literature work and HPC/writer handoffs. The
author uses Box-backed Obsidian. After every successful notes Git push, publish
the exact pushed notes revision to the confirmed active Box folder and verify
it. Preserve verified backups before updating the active dated folder. Raw experimental data and the
initiative's code/reports are separate from this repository.

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
`finish` publishes to GitHub and reminds the agent of the mandatory Box step;
it does not itself transfer files to Box. Direct pushes have the same Box duty.

Keep one editor/task per shared worktree. Independent simultaneous work should
use separate clones/branches. If the remote moves before a push, fetch it,
reconcile commits and any conflicts without discarding work, check the result
and push. No force pushes or automatic resetting/stashing of unknown edits.
For a long session, synchronize again at a clean checkpoint before further edits.

## Current cadence: GitHub and Box after every push — November 6

The author clarified: “While the mac agent codex uses git, my obsidian still
uses box.” This supersedes the earlier archive-only treatment of active Box
notes. Preserve the old receipts as history rather than treating them as the
current vault configuration. Git pull happens at session start; **every notes
Git push requires an immediate Box update**, including direct pushes outside
this helper. There is no timer: the Git push is the publication trigger.

1. Latest direct author confirmation on November 6 (OPS-015): the author
   opens and edits `Trident_FlowLoop_Notes_pre_git_2026-11-03`. Use
   **`box:Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes_pre_git_2026-11-03`** after every push.
   This supersedes OPS-014’s undated target; the dated name does not make
   this folder an archive. Verified Mac mount:
   `/Users/andres/Library/CloudStorage/Box-Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes_pre_git_2026-11-03`.
   Save a hash-verified backup before changing it. The undated local path
   is a symlink to Git, so writing through it does not publish to Box.
   Verify service access and current content without changing vault setup.
2. Before editing/publishing, inspect active Box notes for independent author
   edits against the last successful Box publication manifest. Pull changed
   or new Box notes into separate staging, preserve their hashes and reconcile
   them with Git. If both sides changed the same note incompatibly, preserve
   both versions and resolve the content with the author. Do not overwrite an
   unresolved Box edit. Recheck Box immediately before the outbound copy.
3. Commit explicit task paths, pull on a clean tree, push, and record the exact
   pushed commit/branch. Serialize publication with other writers. Prepare a
   regular-file export of that committed tree outside the Git worktree and Box
   folder, preserving relative note/attachment paths. Exclude `.git`, secrets,
   untracked scratch/raw data and symlink targets; do not dereference repository
   aliases. Record skipped symlinks and any link limitations. The export must
   not be a later dirty worktree or a broad workspace copy. Use the portable
   exporter (destination must be new; receipt stays outside the export):

   ```bash
   python3 tools/export_box_notes.py --revision HEAD \
     --destination /verified/new/notes_export \
     --receipt /verified/new/export_manifest.json --workers 4
   ```

   It verifies each copied regular file against the pushed Git blob identifier,
   records SHA-1/SHA-256, and skips rather than follows tracked symlinks.
4. Preview the copy to the verified active Box folder. Preserve differing
   destination files under a unique dated/versioned notes-publication backup
   outside the active folder. With `NOTES_EXPORT`, `NOTES_BOX_TARGET` and
   `NOTES_BOX_BACKUP` set to those verified locations, use a checksum copy:

   ```bash
   rclone copy "$NOTES_EXPORT" "$NOTES_BOX_TARGET" --checksum \
     --backup-dir "$NOTES_BOX_BACKUP" --dry-run
   rclone copy "$NOTES_EXPORT" "$NOTES_BOX_TARGET" --checksum \
     --backup-dir "$NOTES_BOX_BACKUP"
   rclone check "$NOTES_EXPORT" "$NOTES_BOX_TARGET" --one-way --checksum
   ```

   The local rclone executable may be `$HOME/bin/rclone`. Use `copy`, never a
   deletion mirror (`sync`, `--delete`, `purge`). Preserve Box-only notes,
   `.obsidian` configuration and historical snapshots; list extra paths for
   reconciliation. A mounted-path copy is acceptable only after verifying it
   reaches the intended Box folder and checking Box service visibility; local
   filesystem success alone does not prove cloud publication.
5. Write a completion receipt with pushed commit, source file/hash manifest,
   exact Box target, copy/check exit codes, timestamp, preserved versions,
   Box-only/skipped paths and remaining conflicts. Report GitHub and Box
   separately. Failed/unavailable Box publication remains pending even after a
   successful Git push; retry the same committed export after reconciliation.
   Never claim the full communication triangle is synchronized on Git alone.
   Publish the successful receipt as `X.Chat/01_sources/BOX_PUBLICATION.json`
   in the active Box folder (operational Box-only metadata, not a Git input),
   including the verified commit and source manifest location. Preserve the
   previous receipt alongside versioned publication evidence. Do not write a
   success receipt before the full file check passes.

The earlier November 6 original-snapshot check remains historical evidence: all 371 original files matched the cutover manifest. See the
[original check](X.Chat/05_handoffs/2026-11-06_OPS-013_box_git_reconciliation.md)
and [current author amendment](X.Chat/05_handoffs/2026-11-06_OPS-014_box_communication_triangle.md).
Neither checking that snapshot nor pushing Git proves delivery to the author's
current Box-backed Obsidian. Git push also does not pull another Git checkout.

## Local-machine setup

Run on the local machine, in a directory outside Box's automatic sync tree:

```bash
git clone git@github.com:Andresfierro231/Trident_flowloop_notes_obsidian.git
cd Trident_flowloop_notes_obsidian
python3 tools/git_session.py begin
```

Keep the agent Git checkout outside Box. The author's active Obsidian notes
remain Box-backed under the November 6 direction; publish the committed notes
to that verified folder after every push. Do not redirect the author's vault
or stop/reconfigure local Box clients as part of a routine handoff.

Before switching, preserve any local notes not yet on Box/Git. Compare them with
the clone, incorporate the intended differences, then commit and push them.
Do not replace the local working copy blindly: the HPC intake only certifies
the Box snapshot at its recorded time. Verify internal links/attachment paths
in the local vault after choosing the arrangement; vault-wide references outside
this folder are not repaired by creating this repository.

The author has now identified the dated folder as active. Preserve its
before-publication backup as history and reconcile its current author edits
through the workflow above.
Git synchronization does not wake another chat; the other session must pull and
read the current handoff. Repository visibility/access are controlled in GitHub;
this task does not alter the supplied repository's access settings.

## November 3 recorded local setup — historical

- Canonical local checkout: /Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian/ (outside Box).
- Historical recorded vault route: MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/ is a per-machine symlink to this checkout. Box does not sync aliases. The author’s November6 statement that Obsidian uses Box controls the present workflow; verify the actual folder rather than assuming this old alias remains active. The original dated folder was preserved at Trident_FlowLoop_Notes_pre_git_2026-11-03.
- Local source-byte reconciliation and old/new paths: X.Chat/01_sources/LOCAL_GIT_CUTOVER.json. That initial receipt pins the preserved local input, not later Markdown maintenance.
- Pull/push this repository AND the separate proposal repository at task boundaries. No automatic cross-repository commit or atomicity is implied; record a result for each.
