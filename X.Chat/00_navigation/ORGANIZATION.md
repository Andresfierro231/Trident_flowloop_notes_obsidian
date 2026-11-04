---
title: Notes organization and maintenance conventions
status: maintained
owner: notes organization
updated: 2026-11-03
tags: [project/trident, doc/index]
---

# Notes organization and maintenance conventions

## Owners and reading order

- Root `PROJECT_MAP.md` is the canonical domain/source map. `RESEARCH_MAP.md`
  maps research questions; `LOCATIONS.md` records cross-machine/source locations.
- Read root AGENTS → shared workflow → exactly one Mac/TACC map → notes STATUS
  → project-map route → the relevant task/handoff and exact sources. Inventories,
  archives and all historical handoffs are on-demand references.
- Original top-level subject notes own author observations and source embeds.
  X.Chat owns navigation, registered sources, synthesis, decisions and exchange.
  The separate LaTeX Git repo owns current proposal prose/outline/bibliography.
  HPC owns current research direction, implementation and qualified evidence.
  Explicit author instructions govern intent; newer text alone does not resolve
  a scientific or source-version conflict.

## Folder contract

| Layer | Put here | Keep out |
|---|---|---|
| `00_navigation/` | Stable maps, machine instructions and conventions | New research results or source duplicates |
| `01_sources/` | Source registers, inventories, exact evidence/figure routes and provenance | Copies of library/raw-data collections |
| `02_synthesis/` | One maintained topic/question reconciliation | Another daily copy of the same conclusion |
| `03_proposal/` | Route to current Git proposal; frozen dated package receipts | An additional editable manuscript |
| `04_decisions/` | Verbatim author answers, dated amendments and interpretation | Silent rewriting of prior directions |
| `05_handoffs/` | One dated handoff per coherent task | A competing scientific task board |
| `06_hpc_exchange/` | Versioned requests, unchanged replies, acknowledgment/reconciliation state | Assumed delivery, invented responses or automatic execution |
| `80_repository_links/` | Ignored per-machine aliases and their README | Tracked external Git working trees |
| `90_templates/` | Templates/examples | Live findings or invented sources |
| `tools/` | Documented notes-navigation maintenance | Scientific algorithms or automatic broad edits |

Every durable new topic folder gets a short README naming its purpose, owner,
current entry and frozen material. Root STATUS tracks notes editing claims only.
Scientific tasks remain on the HPC board; manuscript claims use proposal status.

## Names, metadata and IDs

- Preserve original subject-note titles, assets, N01–N12/R01–R05, literature S/
  claim IDs and questionnaire A1–K5. Existing numbering/history is not renumbered.
- New maintained agent notes use descriptive `UPPER_SNAKE_CASE.md` names;
  indexes use `README.md`; scripts use `lower_snake_case.py`. Never use `final2`,
  `latest_new` or machine names to create competing topic copies.
- New handoffs use `YYYY-MM-DD_TASK-ID_short_topic.md`; exchanges use
  `06_hpc_exchange/YYYY-MM-DD/NN_direction_topic.md`, retaining request IDs and
  explicit revision numbers. Earlier numeric handoff names remain historical.
- New maintained documents include title, owner, status, updated date and tags
  in front matter. Original sources, frozen records and legacy notes are exempt;
  add a tagged wrapper rather than modifying issued evidence for metadata.
- Distinguish document state (`working`, `maintained`, `frozen`, `superseded`)
  from evidence state (`proposed`, `implemented`, `numerically checked`,
  `calibrated`, `retrospectively assessed`, `independently assessed`). Approval of
  scope is separate. State exactly which sources were read; inventory is not reading.

## Expand topics without fragmentation

- Prefer extending the existing maintained synthesis. Keep dated changes and
  sources traceable; one substantive investigation keeps one current entry.
- A standalone evidence study may use `02_synthesis/studies/YYYY/MM/DD/topic/`
  with a README and `report_study.json` (created_date, actual work_dates, owner,
  sources and expansion provenance). Expand under that original study's
  `YYYY-MM-DD/topic/` subfolder. At three distinct recorded work dates promote
  the whole study to its creation month, preserving the creation year/month.
  Count work dates, not elapsed/acquisition dates. This adapts Trident's report
  policy; ordinary small notes/handoffs do not need report directories.
- With an expansion/promotion, preserve prior evidence/hashes, update map/index
  routes and record the old/new move map in the same task. An issued source
  manifest retains its as-recorded identity; document the resolver separately.
- A new scientific claim records source, exact locator/revision, facility/run,
  units, inputs/assumptions, implication and evidence limit. Separate bulk,
  probe and wall temperature; nominal electrical heat, net heat and source/sink
  histories. ACU and VCU evidence and holds remain distinct.

## Links, archives and assets

- Use the established vault-root wikilinks for authored Obsidian navigation,
  real extensions for non-Markdown files, escaped alias bars in tables, and
  existing file targets. Root Git/tool documentation may use checked relative
  Markdown links. Keep unverified external paths as qualified code pointers.
- Mac and TACC maps own their verified local paths. The checker can validate
  repository-owned vault links on TACC without assuming a mounted Mac vault.
- Never follow `80_repository_links/`, `03_proposal/current`, other symlinks,
  root `archive/`, dated `archive/` trees or builds in recursive edit scans.
  Dated `staged` symlinks resolve old package links, not active authoring owners.
- Preserve original notes, photo embeds/page fragments, attachments, bibliography
  keys and frozen packages. Before a physical move, make a SHA-256 old/new map
  and check current inbound links. Do not rewrite frozen patches/logs to clean
  whitespace. Keep big data/plots/library assets with their existing owners.
- Image/PDF visual inspection and native external CAD need the existing explicit
  human approval. Metadata/hash/link checks do not imply content inspection.

## Task closeout

1. Reconcile any active claim/remote changes; validate changed routes, metadata
   and relevant numerical/build results. `python3 tools/check_organization.py`
   checks maintained navigation; `--all-active` reports broader scoped link debt.
2. Update map/index/status where the task changes them, and write one handoff
   with source/evidence limits, checks and pending actions. Mark superseded
   directions explicitly, retaining original answers.
3. Commit only task paths. Pull on a clean tree immediately before push;
   reconcile/recheck any incoming change. Push notes and proposal independently,
   recording the actual commits/failures. No blind stash/reset/force push,
   background pull loop, Box bidirectional sync or automatic chat wakeup.

The organization tools only maintain notes. Repeated scientific logic stays
in its owning package, with documented inputs/parameters/results and compute
receipts under the owning HPC policy.
