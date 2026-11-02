# Local proposal researcher → HPC modeling researcher

- Request: HX-20261102, prepared November 2, 2026. This is a written file handoff, not evidence that the HPC chat has received it.
- Task: read existing documentation/results and answer the numbered questions; do not run new scientific pipelines, submit jobs, process held operating data, amend facility models or contact collaborators.
- User wants the literature review to be the foundation, a durable map/working understanding, and restored planning TODOs/sub-bullets in the proposal.
- Current contribution: CFD–experiment order-reduction framework producing a fast, interpretable physical ROM; custom 1D is active; steady → transitions → operational assistance, UQ throughout.
- Author wants preliminary work earlier and feasibility grounded in the master’s: understand experiment data and reproduce temperatures. This is not a claim current ACU/VCU predictions are independently validated.
- Literature owner: current `PhD_internal_litRev`; start with `Other_notes/Final_Cross_Source_Synthesis.md`, B §11, A §11, then A §§13–15/16 as relevant. Preserve the 62 original Q IDs and S/claim IDs; do not restart the completed generic literature review.
- Source baseline: October23 Box checkpoint, saved completion October26; `repository_10.bundle` HEAD `a9dd025ae1c4ce95cfb554da65d749dbe4402bd7`. Uncommitted working/report files are captured separately. Local proposal base is `863fb5098b7ba1fd550a6557feb4dbe6463843bb`; local literature HEAD is `b1f8c74200a61c86ba7aa3d5df30bb55f3f5fe7b`.

## What the local researcher already established from the saved documents

- HPC has a maintained `reports/IMPORTANT_REPORTS.md`; this should precede broad chronological searching.
- M1/M2/M3, prescribed-primary radial response and isolated TAMU developing/polar studies are distinct families.
- VCU run inventory/steady-window work continues beyond CAL-010; CAL-012 and CAL-016 use different rules.
- CAL-019 accepts the nominal constant-resistance/dial-voltage specification. Additional electrical characterization is not required before nominal modeling; nominal generation is not independently measured net fluid input.
- TAMU-TRIDENT-015 maps profile/temperature meaning, heat paths and hydraulic lessons to possible Trident extensions; it does not admit coefficients or claim facility validation.
- TAMU-TRIDENT-016 authorization is in the saved documents; later completed study evidence has not been established locally.
- Dashboard and UQ folders define active requirements, with Ben Booth/NeutronOS collaboration, without demonstrating completed predictive deployment/UQ.
- Do not ask the user again for Ethan’s thesis, goals, generic sensor inventories or Nick’s already supplied protocols; qualify consequential version/status changes instead.

## Questions

### HX-20261102-01 — Current project/report locations

- The checkpoint records the old outer workspace and `andrew_WorkSpace/trident_modeling_initiative/`. What are the current repository roots, branches/HEADs and main source/report entry points? Identify changes since the saved October26 state; retain owner boundaries.
- Existing route: HC01/02; release_index.json.

### HX-20261102-02 — Best existing temperature demonstration

- Which already-produced report/plot/table best demonstrates understanding VCU experimental data and reproducing temperatures? Compare the strongest available development-case reproduction and any eligible out-of-case test; name supplied primary/ambient/initial inputs, fitted quantities, excluded sensors and exposure history. Do not run a new comparison.
- Existing route: HC09/11/16; master’s groundwork.

### HX-20261102-03 — What the later boundary studies established

- Summarize the latest existing BC-004/005 and regional/downcomer conclusions with source paths: which assumptions improved which outputs, which alternatives failed or remained ambiguous, and which conclusions are conditional rather than full-forward predictions? Note results after the checkpoint if they exist.
- Existing route: HC09/16; A §§5–8/11.

### HX-20261102-04 — TAMU profile campaign outcome and transfer boundary

- The October26 decision authorizes TAMU-TRIDENT-016 but does not establish completion. Is there a completed receipt/report now? Give numerical qualification status and the smallest physically justified Trident follow-up; keep benchmark diagnostics distinct from any accepted facility-model change.
- Existing route: HC06–08; A §§13–14.

### HX-20261102-05 — Implementation versus intended functionality

- Using current tests/specs/reports, provide a compact status table for steady loop model, temperature-observation pipeline, transient circulation/storage, learned corrections, end-to-end UQ and dashboard/result interfaces. Separate implemented, numerically checked, calibrated, retrospectively assessed and independently assessed. Report changes; do not restate goals as implementation.
- Existing route: HC03–05/13/14; A §§1/10/16.

### HX-20261102-06 — Unresolved evidence that changes proposal wording

- Which remaining existing-evidence issues actually change the proposal’s claims or leading example: run power/history, source-to-fluid accounting, installed channel mapping, sensor contact, phase/run role, or independent assessment availability? Supply exact controlling decision/report and any already resolved item, especially the CAL-019 accepted nominal-power update.
- Existing route: HC10–12; A §§9/15.

### HX-20261102-07 — Reports and derivations we should read next

- Choose at most five additional high-value existing documents not already in the request’s source map; give exact paths, question answered, controlling date/version and why they change the proposal. Include moved/external-source paths or missing snapshot artifacts explicitly.
- Existing route: HC01; report catalog.

## Response format and return

- Preserve each question ID; answer with concise bullets and sub-bullets.
- For every material statement give repository-relative path, commit or resolved configuration/report date, exact section/figure/table and evidence status.
- Distinguish source-reported finding, your interpretation, proposed work, implementation and independent assessment. State inaccessible/missing evidence explicitly.
- Do not infer model truth from convergence, a good fit or agreement with a reference that supplied the boundary/target.
- Record current branch/HEAD, actual files inspected, any relevant uncommitted state, checks performed and unresolved issues; no credentials or raw data.
- Save a new response under this exchange’s `incoming/` directory (or return it for the user to place there), named `YYYY-MM-DD_HHMM_hpc_response.md`; copy the template without overwriting it or an earlier reply.
- Acknowledge the request by ID/date only after actually reading the transferred files. Do not claim local/remote receipt or notification from merely saving a file.
