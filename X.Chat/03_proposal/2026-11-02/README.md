# Prepared proposal expansion — November 2, 2026

- Status: **prepared and not applied**. Automatic approval review rejected a write outside this session’s project workspace. The original proposal is unchanged.
- Base proposal commit: `863fb5098b7ba1fd550a6557feb4dbe6463843bb`. Every changed file has a base hash in [manifest](manifest.json).
- Compiled preview: [proposal_outline_preview.pdf](proposal_outline_preview.pdf), 16 pages after the follow-up expansion; source/log checks passed; no rendered-page review.
- Review the [expanded bullet outline](EXPANDED_OUTLINE.md) and [unified patch](proposal_expansion.patch); complete changed source files are under `staged/`.
- Main changes: preliminary work follows motivation; master’s evidence/limits lead feasibility; experimental-data interpretation and temperature reproduction are expanded; primary citations and exact evidence routes are added; Markdown and LaTeX bullets align.
- Images and earlier prose are preserved. Existing dated source records remain; new follow-up decisions and citation pointers are appended as separate notes.
- Applying later: use a session with the proposal folder available for writing. Run `git apply --check` on this patch from the proposal root, inspect the diff, then apply and build. If the source has changed, reconcile the patch rather than overwriting it.
- This package does not execute operating-data processing, experiments, CFD or solver studies.
- Build and link-check results are recorded in [handoff](../../05_handoffs/2026-11-02.md).

## Follow-up expansion

- Added nested planning tasks for data lineage/quality/groups, reproducible numerical inputs, physical/observation/discrepancy separation, sensor-change assessment and operator-result interfaces.
- Added exact HPC report routes and the CAL-019 nominal-power correction; used literature as a source/answer resource.
- Planning coverage: all580 paragraphs grouped into31 topics/dispositions. HPC exchange:7 prepared questions; no responses received.
- The patch now replaces the first-pass pending patch; do not apply both versions. Original proposal remains unchanged.
