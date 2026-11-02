# Trident writer and literature notes — agent instructions

This is a separate Git repository for writing, literature reviews, Obsidian
notes and communication with the HPC research initiative. Start each work
session with the Git synchronization below, then read `README.md`,
`GIT_WORKFLOW.md`, `X.Chat/AGENTS.md` and the task's exact handoff/source notes.
Re-read instructions changed by the pull before making edits.

## Mandatory Git session workflow

1. Run `python3 tools/git_session.py begin` before editing. This requires a
   clean worktree and runs `git pull --ff-only`. If existing work, divergence,
   network failure or conflict prevents it, preserve the work and resolve the
   issue explicitly before continuing edits. Never discard another session's
   files, automatically stash unknown work, reset or force-push.
2. Make the requested edits and relevant checks. One agent owns a task in a
   shared worktree; use another clone/branch for independent concurrent work.
3. Before every handoff/end of an editing session, run
   `python3 tools/git_session.py finish --message 'Describe the change' --paths <explicit paths>`.
   This stages only those paths, checks whitespace, commits them, then pushes
   the current branch. Use `git status --short` to confirm what remains.
4. An editing task is not synchronized until the push succeeds. If another
   writer advanced the branch, fetch and reconcile without discarding work,
   rerun relevant checks, then push. Record any remaining failure and local
   commit ID in the handoff. Even a session with no edits checks/pushes pending
   commits using `finish`. Do not make an empty commit just to record a read.

## Research ownership — explicit user direction, November 2, 2026

The HPC Trident modeling initiative holds the latest project context, approved
research direction, task state and qualified evidence. This notes repository
supports the writer and literature work near the user's library. It can receive
organizational guidance, source maps and agent instructions from HPC agents.

Do not overwrite or redefine HPC research direction from a newer draft,
literature synthesis or local note. Record discrepancies and proposed changes
with exact sources and reconcile them with the initiative and explicit author
direction before adoption. New user instructions govern; dated claims still
need source qualification. A handoff is not an automatic research assignment.
Original manuscripts, library sources and facility records retain their owners.

The HPC initiative's entry points are `AGENTS.md`, `START_HERE.md`, the
research roadmap and `coordination/BOARD.md`; exact location and evidence
limits are recorded in `HPC_CONTEXT.md`. Keep scientific assumptions, facility
applicability, author decisions and implemented/validated status distinct.
Preserve the ACU operating-data hold and other documented execution gates.
Writing work does not authorize CFD, experiments, new data processing or
messages to third parties.

## Source and storage boundaries

Git is the primary edit and communication route for this repository after
the initial Box intake. Do not use Box/rclone/rsync as a second bidirectional
sync engine. Before moving a local Box working copy to Git, reconcile its
unpublished edits; the original Box source is preserved by this cutover.
Large experimental raw data live outside this repository under the initiative's
`box/data/`; do not add them to Git here.

Preserve notes, citations, source IDs, image embeds and attachments. Do not
move/restructure source content without a move map and link checks. Reading
filenames or copying/hashing files is not scientific review.
Never visually inspect images, screenshots, plots or rendered PDF pages without
explicit human approval for the image set and purpose. Do not parse or execute
external CAD without the applicable explicit approval. Do not expose secrets.
