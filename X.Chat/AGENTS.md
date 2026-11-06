# Research organization instructions

- First identify local/TACC/unknown from hostname, OS and verified paths. Read README.md, 00_navigation/AGENT_START.md, latest relevant handoff and author decisions.
- Use concise bullets for intermediate notes. Prioritize ideas, citations, exact source locators and related-document pointers.
- Follow `00_navigation/ORGANIZATION.md`; keep one maintained synthesis and one authoring owner per artifact.
- Preserve original notes, embeds, attachments and scientific records. Do not relocate sources without a move map and link verification.
- Preserve the existing literature and project source/claim identifiers; inventory does not imply scientific reading.
- The custom physical 1D solver is the active model. The approved research stages are steady performance, transitions and operational assistance, with uncertainty throughout.
- November 2 author direction: try preliminary work earlier; use the named master's work to support understanding experimental data and reproducing temperatures.
- Reproduction, calibration, retrospective assessment and independent prediction are distinct. Preserve case exposure, sensor policy and supplied-input limits.
- Read canonical proposal AGENTS and doc_support/agent/SHARED.md plus one machine map. November 3 edits are applied; dated packages are frozen archives, not authoring owners.
- Check package status/base hashes before resuming. After application, maintain active bullets in the proposal repository and mark the dated package applied or superseded.
- Existing holds on operating-data processing and executing CFD/experiments remain; organizing and drafting do not authorize those activities or external communications.
- Dashboard development remains in collaboration with Ben Booth/NeutronOS; stage approval does not imply autonomous control authority.
- Unresolved file links and ambiguous revisions need source qualification; do not label files globally missing based on a scoped inventory.

- November 2 follow-up: use `00_navigation/LITERATURE_RESOURCES.md`, `00_navigation/LOCATIONS.md`, `01_sources/HPC_REPORT_MAP.md`, `02_synthesis/WORKING_UNDERSTANDING.md` and `02_synthesis/PLANNING_COVERAGE.md` before expanding research context.
- The user originally requested Box-mediated HPC Q&A under `06_hpc_exchange/`. Preserve dated incoming responses, question IDs and acknowledgment state; do not infer delivery or answer on the remote researcher’s behalf.
- CAL-019 accepts nominal dial-based heater input under declared assumptions; do not make new electrical measurements prerequisites to that nominal specification. Metered/net-fluid input and independent validation remain distinct.

- Controlling clarification AD-20261102-05: proposal/research goals and questions organize this project. The literature review is a source/answer resource, not the organizing backbone. Use the original 62-question crosswalk to enrich relevant bullets; do not replace author-approved scope/order with the review’s structure.
- Preserve original question IDs A1–K5. “Review complete” is a synthesis status, not proof of completed research or proposal integration.

- Obsidian convention: actual vault root is `ObsidianVaults`; `MainVault` is an internal folder. Use vault-root wikilinks under `MainVault/Box/...`, not bare absolute `/Users/...` Markdown destinations.
- External source access uses `80_repository_links/Papers`, a local symlink selected by the user. Keep it outside recursive note-edit scans; it exposes the real Git working trees.
- Only emit clickable file links after checking the target exists. Keep non-Markdown extensions; use real README files or plain text for directories. Follow `00_navigation/OBSIDIAN_LINKS.md`; validate with `tools/obsidian_links.py`.
- Box does not sync symlinks. Recreate the same internal alias per machine with `tools/setup_repository_link.py`; do not move/clone Git repositories into Box as an incidental link fix.

## Synchronization — November 3 follow-up

- Author requests pull and push for BOTH Trident_FlowLoop_Notes and the canonical LaTeX proposal. Treat them as separate synchronization checks; success in one never establishes the other's state.
- At startup/task boundaries inspect each actual Git root, origin, branch and worktree; fetch, pull --ff-only on clean main, and push reviewed task commits per proposal SHARED.md. Never discard unrelated work or force synchronization.
- Notes Git owner is /Users/andres/projects/research/Trident/Trident_flowloop_notes_obsidian/; origin git@github.com:Andresfierro231/Trident_flowloop_notes_obsidian.git. Existing vault route is a local alias to that checkout; original Box snapshot is read-only history by convention. Root AGENTS.md/GIT_WORKFLOW.md and tools/git_session.py define the notes session.

- Git now carries the notes/HPC exchange, incorporating the remote November 2 cutover. Historical Box records and HX acknowledgment states remain unchanged. HPC initiative controls current research evidence/direction subject to explicit author instructions; local writing does not supersede it by date alone.

## Committee proposal direction — November 3

- Introduce the project to the committee, demonstrate PhD-level research value and a credible one-year plan. Use short claims and undergraduate engineering language.
- Omit retrospective-case/exposure discussion from the rendered proposal; retain provenance and evidence roles internally. Put drafting instructions and result requests in internal notes.
- Request specific HPC figures/tables/results with placement, quantities, units and source requirements. Current packet: 06_hpc_exchange/2026-11-03/PROPOSAL_RESULTS_REQUEST.md. Active chapter files now follow reading order; see canonical proposal doc_support/committee/SECTION_MOVE_MAP.json.

- Latest author structure supersedes that aim-linked order: Chapter 1 motivation/impact; Chapter 2 experiments, existing/planned CFD and preliminary evidence; Chapter 3 integrated methods with theory, physical model, sensors, learning, assessment and uncertainty; Chapter 4 formal aims, one-year plan and deliverables. Define concepts just before use. Proposal doc_support/committee/STRUCTURE.md owns the current first-use map.

- Proposal authoring format is bullet points for now. Preserve this during restructuring; switch to narrative prose only when explicitly requested. Equations, tables and the four-chapter structure remain.

## Controlling author amendment — November 6 Box communication triangle

- The author says Obsidian still uses Box. Earlier November3 alias/archive-only assumptions are historical and do not establish the active vault path.
- After EVERY successful notes Git push, including direct pushes, update the confirmed active Box Trident notes folder with that exact committed revision. GitHub success alone does not complete the notes handoff.
- Follow root GIT_WORKFLOW.md: reconcile independent Box edits first, preserve differing versions, copy only the committed notes/attachments, exclude Git metadata/raw data/external aliases, avoid deletion mirrors, checksum-verify and record the exact Box destination/commit/receipt. If Box publication fails, report it separately as pending.
- Verify the real active folder; the target is awaiting author clarification in OPS-014. Do not silently use the dated snapshot, create/rename a vault or rewire Obsidian. Scope is notes publication, not unrelated Box writes.
