# Codex project audit to focus the TRIDENT literature reviews

Use this prompt in the repository-aware Codex session. The purpose is to retrieve current project evidence that a separate literature-review conversation cannot access. Do not select a thesis direction or invent missing acceptance criteria.

## BEGIN PROMPT

We have two evidence-backed first literature reviews and a critical synthesis for TRIDENT:

- A: physical/reduced model methods, conservation, closures, observation models, identifiability, discrepancy, design, uncertainty and V&V, including a model comparison plan.
- B: natural-circulation-loop history/purposes, specific MSR engineering decisions/QoIs, similarity/transfer limits, strongest prior work and feasible contributions.

Review the latest project documents and actual model code to answer the questions below. This is a **read-only evidence audit**. Do not modify model/thesis files, process operating data, load FlowTests5/6, run experiments, assume new sensors/CFD or reconcile Ethan discrepancies. You may create the requested compact audit deliverables. Inspect small metadata, configuration, protocol and code files; do not transfer raw datasets. Do not contact collaborators.

If supplied, read the latest TRIDENT literature checkpoint and original `Markdown collé.md`; preserve source/claim/question/hypothesis IDs. External literature S01–S78 and project PF01/PF02–PF06 are different namespaces from the repository's own numbered references. Do not merge them. The literature bundle need not exist in your repository: say which documents you actually have.

### Known context: confirm updates rather than asking us to repeat it

Three project stages are steady performance/margins, transitions and operational assistance, with uncertainty central. ACU and VCU are distinct; STNCL belongs to the VCU experimental lane; TAMU/Ethan is external evidence. Preserve implemented M1 no-flow steady energy, M2 prescribed-flow energy and M3 scalar steady buoyancy–resistance meanings. Distinguish a conditional measured-primary-temperature-driven diagnostic from an autonomous forward prediction.

PF01 reports VCU primary PTC1–4 as centerline observations, wall-contact STCs, secondary temperature channels and no direct VCU primary/local-flow measurement. ACU flowmeter is author-reported, not yet qualified here. Exact fluid/property, energy-deposition, observation and independent-assessment support must be documented, not assumed. Current selections may have changed: authoritative current repository evidence controls, with conflicts explicit. Written Nick phases are not automatically approved/executed/frozen holdouts.

Provisional literature packages: CP01/H01 supported parameter combinations and predictions; CP02/H02 when retained storage/transport changes a target; CP03/H04 quantitative surrogate transfer only for a named circuit; CP04/H03 local descriptor/thermal effect only with qualified evidence. These are candidate hypotheses, not accepted aims or established novelty. Existing literature already covers thermal identification, passive RC fitting, wall-aware reduction, target-oriented design/calibration and embedded discrepancy.

### Questions to answer, in decision order

**CQ01 — What is already approved?** Which objectives, stages, deliverables and restrictions are author/adviser-approved versus proposed, implemented or merely brainstormed? What current roadmap/decision record governs? Preserve the three stages, but identify which stage is the near-term proposal's main scientific task.

**CQ02 — What actual prediction decisions have been named?** For steady and transient stages separately, extract intended users, decisions, primary/secondary QoIs, horizons, tolerances or latency goals. Which numbers have an authoritative source? Where absent, write “user/adviser decision required”; do not manufacture one. Distinguish sensor temperatures, bulk temperatures, duty, circulation, extrema and margins. Supply candidate contracts from existing goals without selecting one for us.

**CQ03 — What is implemented mathematically?** For each actual M1/M2/M3 and current transient model, give code/config locations, states, known inputs, solved outputs, parameters, closures, initial/boundary conditions and simplifications. Are fluid, wall and insulation storage, advection, circulation inertia and radiation present? Which parameters are shared or fixed by convention? No future measured outputs may be hidden forecast inputs. Inspect equations/code; a README alone is insufficient when code differs.

**CQ04 — Which inputs have an independent physical scale?** What evidence establishes electrical watts, heat deposited where, secondary mass/volume flow and enthalpy duty, ambient histories, inventory or heat capacities? Separate commands, measured quantities and derived estimates. Record metrology/calibration/property provenance and known shared ingredients. Do not open or compute operating records to fill gaps.

**CQ05 — What does each observation mean?** Supply the authoritative current configuration/channel map, sensor type/location/averaging interpretation, timing/response/contact assumptions and any known shared calibration/bias. Identify which uncertainty is actually documented versus assumed. State which channels/configuration choices changed across historical runs. Do not infer bulk fluid temperature from a centerline probe label.

**CQ06 — What facility/domain can the literature comparison actually target?** Identify current geometry/revision and authority hierarchy; fluid/product/composition; insulation/heater/cooler footprint; accepted property functions and ranges; documented operating envelope. Separate software guards and nominal configurations from accepted operating conditions. Resolve simple document authority by citation; report unresolved scientific conflicts without silently choosing a value.

**CQ07 — What experiments and independent assessments are feasible?** From Nick's current written plan and status records, identify feasible perturbations, existing versus proposed repeats, which quantities each phase could constrain, and approval/execution status. Which cases are available for calibration, selection and genuinely independent assessment? Record prior development use of any claimed holdout. No new experiment approval or execution is authorized by this audit.

**CQ08 — What is already established by our own work?** Which statements/results belong to Andrés's completed CSEM thesis, earlier TRIDENT reports or external thesis work, and which remain proposed? Identify existing analyses of parameter combinations, retained mechanisms, prediction errors and reduction limits that would make a purported new PhD aim repetition. Distinguish implementation, verification, calibration and independent validation. Use exact source locators; do not reconcile Ethan discrepancies.

**CQ09 — What could remain scientifically uncertain within the project?** List the highest-value competing physical explanations or unsupported predictions documented by advisers/researchers. For each, say what existing observations could distinguish, what remains confounded and what additional evidence would be needed. Separate author statements from your deductions. Do not declare a field-level literature gap from absence in the repository.

**CQ10 — What resources and dependencies are real?** What qualified CFD/reference fields, run manifests, measurement capability, personnel commitments and computing resources are actually available or scheduled? Give scope/status, not large files. What is the scientifically useful no-CFD path? Preserve collaboration with Nick for experimental requests and Ben Booth/NeutronOS for the dashboard; do not claim their commitments without records.

**CQ11 — What planning constraints change feasibility?** Extract current proposal/committee milestones, dissertation horizon, dependencies and approved priorities from dated records. Do not substitute remembered or aspirational dates for current commitments. Identify work that is essential versus an optional extension and decisions that must come from advisers.

**CQ12 — What would materially change literature selection?** Rank at most five unresolved facts by the source/model/contribution decision they affect. For each, distinguish (a) repository answer found, (b) collaborator information needed, (c) author/adviser decision, and (d) scientific research still to perform. Do not respond with an undirected request for more data/papers.

### Required output

Create `TRIDENT_PROJECT_AUDIT_FOR_LITERATURE.md` and a compact accompanying JSON using CQ01–CQ12. For each answer include:

- Evidence status: approved direction / author report / working configuration / implemented / verified / calibrated / independently assessed / written proposal / unresolved.
- Exact relative path, section or line locator, document date/revision and current commit where available; include code evidence for implementation claims.
- Consequence for review A, review B and CP01–CP04.
- Remaining uncertainty and who can resolve it; do not turn a missing record into evidence that a collaborator lacks information.

Finish with:

1. A comparison of up to three candidate **prediction contracts**: intended decision, target/horizon, actual inputs/observations, unknown tolerance, supported assessment and no-CFD feasibility. Do not choose an MSR architecture or final aim without a recorded decision.
2. A dependency graph or table for measurements and derived quantities, showing why duty/flow estimates may share errors.
3. A short list of already-answered facts we should stop asking for, and at most five questions genuinely requiring the user's/advisers' judgment.
4. A list of small files or excerpts to return to the literature conversation. The Markdown audit plus JSON should be sufficient in ordinary cases; no raw operating data, whole repository or bulk CFD export.

If a requested fact is unavailable, say so and continue the other questions. This audit should reduce repeated clarification and focus the next literature/proposal work, not restart the project or discovery.

## END PROMPT

## What the author can supply independently

The repository audit can establish current evidence and documented decisions. Only the author/advisers can select an undocumented near-term priority, acceptable prediction tolerance, final scientific ambition or resource commitment. Those choices can be made after seeing the candidate contracts; exact numerical tolerances are not required merely to continue literature extraction and qualitative synthesis.
