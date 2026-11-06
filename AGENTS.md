# Trident writer and literature notes — agent instructions

First identify Mac/TACC/unknown from hostname, OS, TACC markers and verified paths. Read `X.Chat/00_navigation/agents/SHARED.md` and exactly one of `MAC.md` or `TACC.md`. These notes-owned maps distinguish machine instructions; the proposal keeps its own `doc_support/agent/` rules. Synchronize BOTH repositories independently. Then read `STATUS.md`, `PROJECT_MAP.md` and the relevant task/handoff; never infer HPC paths from Mac paths.

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
   This stages only those paths, checks whitespace, commits them, performs a
   fresh fast-forward-only pull, then pushes the current branch. Use
   `git status --short` to confirm what remains.
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

Agents collaborate through Git; the author reads and may edit the Box-backed
Obsidian notes. November 6 explicit author direction supersedes the earlier
archive-only assumption: **after every successful notes Git push, update the
confirmed active Box Trident notes folder with that exact pushed revision**.
This applies to direct Git pushes as well as `tools/git_session.py finish`.
Confirmed active destination: `box:Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes`
(author’s `Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes`). Preserve the
separate dated `pre_git` snapshot.
A notes handoff is incomplete until both GitHub and Box are verified, or the
Box failure/blocker is reported explicitly. Follow GIT_WORKFLOW.md for the
required Box-edit reconciliation, preserved versions and hash receipt. Never
mirror `.git`, follow external aliases, delete Box-only files or overwrite
unreconciled author edits. This authorizes notes publication, not experimental
deposit uploads or unattended bidirectional synchronization.
Large experimental raw data live outside this repository under the initiative's
`box/data/`; do not add them to Git here.

Preserve notes, citations, source IDs, image embeds and attachments. Do not
move/restructure source content without a move map and link checks. Reading
filenames or copying/hashing files is not scientific review.
Never visually inspect images, screenshots, plots or rendered PDF pages without
explicit human approval for the image set and purpose. Do not parse or execute
external CAD without the applicable explicit approval. Do not expose secrets.

## November 3 local cutover

- Local notes owner: /Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian/. The November3 receipt recorded a local alias and preserved Trident_FlowLoop_Notes_pre_git_2026-11-03. That receipt is historical: the author clarified November6 that current Obsidian uses Box. Verify the actual active Box folder; do not infer it from the old alias or change the vault setup. Preserve the dated original unless the author identifies it as the active folder. Reconcile Box edits before publication.
- Read X.Chat/05_handoffs/2026-11-03_03_notes_git_sync.md for reconciliation, source move map and receipt limits. Preserve both local and HPC directions; latest explicit author instructions control intent.

## Committee proposal direction — November 3
- Introduce the project, demonstrate PhD merit and a credible twelve-month plan. Undergraduate engineering language, short claims and specific planned results.
- Avoid retrospective-case/exposure discussion in rendered proposal; keep evidence provenance internally and preserve supported claim levels.
- Internal instructions/study requests belong in notes or proposal doc_support/committee/. Current prompt: X.Chat/06_hpc_exchange/2026-11-03/PROPOSAL_RESULTS_REQUEST.md. Prepared, not acknowledged; execution holds remain.

- Latest outline direction: motivation → experimental/high-fidelity evidence (including preliminary results) → integrated research methods → aims and one-year delivery plan. Introduce concepts just before use; follow proposal doc_support/committee/STRUCTURE.md. This supersedes earlier chapter-specific aim/method placement.

- Proposal authoring format is bullet points for now. Preserve this during restructuring; switch to narrative prose only when explicitly requested. Equations, tables and the four-chapter structure remain.

## Organization and expansion

- `PROJECT_MAP.md` is the canonical notes domain/source map; maintain it and affected README indexes with important additions/moves. `X.Chat/00_navigation/ORGANIZATION.md` owns names, metadata, source IDs, evidence status and continuing-study lifecycle.
- Keep original subject notes/assets and frozen packages intact. One current topic owner, dated evidence/handoffs, and explicit old/new/hash maps for physical moves. Do not follow external aliases or archived staged trees during edits/staging.
- Run `python3 tools/check_organization.py` before handoff; record actual checks and current Git results. Use `--all-active` to report broader link debt without rewriting original sources.

- Material citation direction (November 4): internal notes and candidate libraries are provenance/discovery records, not proposal bibliography sources. Use verified originals or the master's/Rozak definitions only for equations actually supported there. See X.Chat/01_sources/MATERIAL_CITATION_GUIDE.md; preserve unresolved-fit status rather than invent attribution.

<!-- BEGIN TRIDENT_SKILL_DISCOVERY -->
## Task-specific skills

At task start or a meaningful scope change, use available skill names/descriptions
to select relevant guidance. For specialized work without that metadata, consult
[SKILLS.md](SKILLS.md); routine work may need none. Read only the matched
`SKILL.md` and needed references. Do not load the whole pack or call a model to route.
Owning AGENTS.md and explicit user scope still control. If local links are missing,
use the notes checkout from the current machine map and its documented catalog
`link` command; preserve existing catalogs/skills. No global installation is needed.
<!-- END TRIDENT_SKILL_DISCOVERY -->


## Canonical reference collection — November6

`X.Reference/` is the sole physical and editable source collection. Use [its current index](X.Reference/INDEX.md) and the [current migration record](X.Chat/01_sources/reference_migration/2026-11-06/X_REFERENCE_RENAME/README.md). Do not create another notes `reference/` folder. The modeling repository’s `reference` symlink is compatibility only. Preserve immutable sources and issued manifests; `python3 tools/resolve_reference_path.py ORIGINAL_PATH --json` resolves recorded old names and bootstrap relocations without changing the records.
