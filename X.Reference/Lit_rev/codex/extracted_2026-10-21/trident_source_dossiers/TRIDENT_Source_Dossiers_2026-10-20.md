> **Updated continuation:** This is an earlier checkpoint. S43/S46 and the S26 supplement now have scoped extractions; S47 and selected methods readings were added. Use [P0_Research_Memo_2026-10-20.md](P0_Research_Memo_2026-10-20.md), [README.md](README.md) and the current registry/acquisition queue for current status. Earlier pending/acquisition statements below are historical.

# TRIDENT source dossiers and critical appraisal

20 October2026. This pass consolidates **nine distinct uploaded works**, preserves their stable source IDs, and adds a scoped history/motivation checkpoint. Each dossier has bibliographic/version checks, PDF/printed-page locators, equations and assumptions, evidence appraisal, coverage/readiness and stable claims. The package contains69 new source-scoped claims plus the earlier ledger. It does not select a final model or establish a thesis novelty claim.

## Read this first

The most defensible motivation is to connect a **specific natural-circulation phenomenon** to a **specific MSR engineering decision**, then state the limits of the experiment. Historically, loop research served several purposes: investigating pump-free circulation, exposing circulating salt and materials to irradiation, understanding stability, and providing measurements for model assessment. A research loop can be valuable without being a complete reactor analogue.

The historical checkpoint examines original passages from Romie–Kinyon1958 (S40), Savage et al.1967 (S41), and Robertson's1965 MSRE design report (S42). The first explicitly weighs pump reliability/maintenance against increased fuel-salt inventory; the second concerns fueled in-pile exposure; the MSRE design includes circulation pumps. These purposes should remain distinct. A reported1969 MSRE natural-circulation test is still a lead requiring its original operating record.

Read [Natural_Circulation_History_and_MSR_Motivation.md](Natural_Circulation_History_and_MSR_Motivation.md) for the problem–decision–QoI map, primary-source locators and exact historical reading limits.

## Uploaded work index

| Source | Work and dossier | Evidence extracted | Readiness and unresolved issues |
|---|---|---|---|
| S09 | [Vijayan2002](dossiers/S09_Vijayan_2002.md) | Scaling, steady flow, stability, geometry/regime limits | Ready for qualified scaling/theory comparison; not universal geometry/closure transfer |
| S36 | [Vijayan–Austregesilo1994](dossiers/S36_Vijayan_Austregesilo_1994.md) | Original water-loop scaling experiments and differing steady/stability requirements | Ready for the scoped scaling/history synthesis; hydraulic constants are conditional |
| S37 | [Reis–Seo–Hassan2024 flow visualization](dossiers/S37_Reis_2024_flow_visualization.md) | Eight water/salt states, PIV, reconstructed thermal profiles, friction and Nu, UQ audit | Ready for reported-case and observation-method appraisal; uncertainty formulas need reconciliation before reuse |
| S38 | [Reis–Seo–Hassan2024 solidification](dossiers/S38_Reis_2024_solidification.md) | Accidental cooling event, observed damage, inferred blockage and measurement limits | Ready for qualified cold-margin motivation; no validated pressure/blockage causal model |
| S16 | [Reis–Hassan2025 SAM](dossiers/S16_Reis_Hassan_2025.md) | Prescribed versus predicted quantities, two friction treatments, recovered journal tables | Ready for conditional comparator appraisal; source-informed heat/temperature/friction inputs limit independence |
| S21 | [Carson et al.2026 local heating](dossiers/S21_Carson_2026_local_heating.md) | Three local-heating cases, history/transient confounders, velocity and assumed Nu | Ready for local-heating prior-work appraisal; no independently established recirculation extent/causal heat effect |
| S26 | [Manikkan et al.2026 entropy switch](dossiers/S26_Manikkan_2026_entropy_switch.md) | RC equations, inference/selection, three example settings, multimodality and R,C recovery limits | Main article extracted; SupplementA–D now received,extraction pending. Ready for qualified methods comparison, not faithful reproduction |
| S35 | [Rozak2026 CFD thesis](dossiers/S35_Rozak_2026_CFD.md) | Reconstructed geometry/losses, comparison operators, BC verification, two-grid loop analysis, steady CFD/local reversal | Earlier uploaded thesis included. Ready for qualified V&V lessons; main/appendix property and enthalpy issues need code/revision checks |
| S39 | [Carson dissertation manuscript](dossiers/S39_Carson_dissertation.md) | Fiber/PIV observations, development, flow inference, spectral methods, scaling/equation audit | Ready for qualified measurement-interpretation synthesis; supplied title dateDec2026 and final status unverified |

The latest upload batch has10 files representing8 works: S38 has two text-identical copies; S16 has a22-page publisher-web print and the complete11-page journal PDF. The earlier139-page S35 thesis makes9 distinct uploaded works in this consolidation. Duplication/version history is in `inventory.json`; neither duplicate is additional independent evidence. The S16 journal PDF resolves the earlier missing-table access issue. S21 and S26 PDFs establish online dates11September2026 and26July2026 despite later assigned issue dates.

The registry deliberately avoids a global “fully read/fully validated” label. Each source's coverage and purpose-specific readiness govern use. All relevant technical text in these dossiers was inspected; selected consequential equations/tables/figures were visually checked. Figures were not comprehensively digitized, code/results were not independently reproduced, and missing supplements remain missing. Historical reports have **selected-passage notes**, not full-report dossiers.

## Findings that affect the proposal and methods review

1. **Do not count reused data as independent validation.** S37's eight experimental states underlie S16 and S35. Different codes or friction variants are additional model comparisons, not additional experiments. Later S39 campaigns require their own run identity before independence/overlap can be assessed.
2. **A comparison operator is part of the model.** A centerline thermocouple, wall probe, fiber path, planar PIV magnitude, area-average signed flux and velocity-weighted enthalpy temperature are not interchangeable. S35/S39 expose reconstruction assumptions; the dossiers distinguish observed quantities from derived ones.
3. **Heat bookkeeping and uncertainty must be joint.** A net duty inferred from flow and probe ΔT is not an independent flow-validation target. Loss estimates share inputs; property errors share temperature dependence. Several printed propagation formulas or conventions need correction/clarification, not blind implementation.
4. **More uncertainty machinery does not guarantee physical identification.** S26 already tackles Bayesian network topology/parameter inference. Its main numerical reporting is conditional on a single chain in a multimodal problem; its physical-parameter intervals often miss the known synthetic truth. Unknown inputs and unrestricted discrepancy remain confounders.
5. **Local flow remains a gated contribution.** S35 already predicts local reverse axial flow. S21/S37/S39 offer relevant diagnostics but do not independently validate a3D recirculation extent or its causal effect on heat transfer. Sparse TRIDENT temperatures and a single circulation state cannot supply those missing fields.
6. **Steady agreement does not establish transient or stability transfer.** S36/S09 distinguish their scaling requirements; S35's pseudo-transient procedure targets a steady solution and does not supply physical transient validation. Wall resistance, wall storage and boundary-source distribution are different modeling decisions.

Each statement is qualified in its dossier and the [claim ledger](Claim_to_Evidence.md), with original findings separated from analyst derivations/audits. Apparent source errors are flagged for reconciliation; they are not automatically evidence of a new research gap.

## Contribution hypotheses after this reading

These preserve H01–H04 from the earlier research state; none is an established field-wide gap.

| ID | A more precise contribution to investigate | Feasibility and prior-work test |
|---|---|---|
| H01 | Conservation-constrained thermal/transport reductions with identifiable parameter groups and honest withheld-condition QoI intervals | Plausible with existing measured thermal outputs if power/observations/protocols are adequate. Must exceed S08/S26 and established identifiability/discrepancy methods. Simple G/C ambiguity alone is insufficient. |
| H02 | A QoI-dependent criterion for retaining wall storage, directional transport or additional closure physics | Test nested physical models and prediction failures under declared tolerances. Adding wall nodes or reproducing a case alone is established practice. Unobserved extrema require richer references. |
| H03 | What local thermal information is inferable from sparse observations, and when spatial enrichment provides independently assessable benefit | Current no-CFD scope is measured temperatures or justified bounds. Quantitative local-flow extent/heat effects remain contingent on qualified local data/CFD. S35/S39 are strong existing prior work. |
| H04 | How similarity distortion, property/loss uncertainty and measurement interpretation limit a declared surrogate-to-salt prediction | Requires a named target reactor architecture/path and operating envelope. Match the phenomenon and QoI; high-Pr fluid choice alone is not the contribution. |

The immediate achievable product is a defensible model/observation/uncertainty comparison for measured TRIDENT quantities. Whether this becomes a theoretical result, a transferable selection procedure or a local-physics thesis requires the next reading and feasibility checks. No qualified TRIDENT CFD or new instrumentation is assumed.

## What is available to read next

A manageable next batch is **S12 → S15 → S44 → S08**, in that order: engineering decision/safety-function framing; actual similarity limits; source-distribution/dynamics and established CFD precedent; then disciplined physical-model selection before complex topology inference. S43 can precede S44 if obtained, because it is actual FLiBe-loop evidence and resolves claims cited by S35/S39.

- **S44 is retrieved:** White Rose's published version of Battistini et al.2021, DOI10.1016/j.ces.2021.116520,14PDF pages including repository cover. Identity verified; methods/results are **not yet extracted**. No upload needed.
- **S45 is retrieved:** Everts et al.2023, DOI10.1016/j.ijthermalsci.2023.108178,36-page institutional author manuscript. Title/authors match the21-page journal record; detailed revision comparison is pending. Read next when developing-flow assumptions become a decision. No upload needed.
- S12,S15,S08 and the official metrology PDFs already available from the previous stage remain usable. Their earlier reading depth is preserved; they were not silently promoted to full extraction in this pass.

## Acquisition update after the new uploads

The requested Britsch article(S43,14pages),Headley dissertation(S46,103pages) and Manikkan SupplementA–D(S26:SUP1,28pages) are now acquired. Britsch’s two copies have identical per-page extracted text; count one source. Their identities and first-page/contents metadata are checked; full evidence extraction is pending. Existing nine dossiers and69claims are unchanged in scientific reading depth.

The next reading batch is S43 → S46 → S26:SUP1 with the fixed-commit author repository. Ethan discrepancy reconciliation is deferred to Codex at the user’s direction. No further paper acquisition is needed to start this batch.

The most valuable user help is a one-page decisions-and-feasibility brief: what operator/engineering decision a prediction changes; priority QoIs and meaningful error; what measurements/runs/resources are confirmed versus tentative; near-term proposal milestones; and committee questions. Existing PF01 facts need not be repeated. Unknown reactor mapping or tolerances can remainTBD while the review compares alternatives.

## Reusable records and evidence rules

- `source_registry.json`:46stable source records, versions, access, reading depth and synthesis readiness.
- `claim_ledger.json` / `Claim_to_Evidence.md`: original C01–C16 plus69new Sxx-Cnn claims; qualifications and source locators remain attached.
- `acquisition_queue.json`: resolved main-document requests, specific missing materials, alternatives and next reading order.
- `research_state.json`: project facts/unknowns, H01–H04 updates, boundaries and next actions. `project_facts.json` and `PF01_project_facts.md` preserve supplied project context; their internal project-document IDs do not collide with literature IDs.
- `inventory.json`, `search_and_access_log.json`, `retrieval_log.json`, `checks.json`, `manifest.json`: source identity, reading/access provenance and artifact integrity. Earlier state is retained under `prior_stage2/`.

Search/check date20October2026. Routes included publisher, author, institutional, official/laboratory and original-report mirrors; queries and access failures are logged. Publisher403/site-unavailable and OSTI429/502 responses limit this session's retrieval. Search is targeted, not an exhaustive systematic review; no subscription access, outside-conversation files, cited originals, raw measurements or final deposited theses are assumed. Technical findings belong to their observed/modelled regimes and named quantities.
