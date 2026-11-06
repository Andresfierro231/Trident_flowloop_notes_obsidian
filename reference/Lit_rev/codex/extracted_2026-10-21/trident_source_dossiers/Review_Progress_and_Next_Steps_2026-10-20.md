> Later checkpoint: reviews v0.3; S07/S18 scoped-extracted; current acquisition requests S23/S67. See Research_Execution_Plan_2026-10-20.md and Upload_Requests_Current.md. The earlier reading/access statuses below are historical.

> Current checkpoint: all six latest requested originals are received and scoped-extracted. Earlier request statuses below are historical. See Upload_Requests_Current.md and Six_Source_Synthesis_2026-10-20.md.

> Current deliverables: Methods_and_Theory_Review_Working_Draft.md, Motivation_and_Contribution_Review_Working_Draft.md and Upload_Requests_Current.md supersede prior reading/access statuses.

> Superseded acquisition status: S52/S30 now received and extracted. See Fifteen_Paper_Reading_Plan.md for current requests.

# Two-review progress and next steps

Updated 2026-10-20. Governing brief: supplied **Markdown collé.md**, reread this pass. Existing source, question and hypothesis IDs remain unchanged.

## What the two reviews must deliver

| Review | Audience and product | Central test |
|---|---|---|
| Methods and theory | Implementation reference for Codex: model hierarchy, equations/conventions, closures, state/observation definitions, identifiability, UQ and assessment requirements | What can each model predict from independently available inputs, and what evidence can distinguish it from alternatives? |
| Motivation and contribution | Proposal/dissertation narrative: loop history/purposes, specific reactor decisions/QoIs, transfer limits, strongest prior work and feasible contribution hypotheses | Why is this scientific question consequential, what is already solved, and what can TRIDENT credibly add? |

The reviews will share the claim ledger and source registry, but must not equate an implementation option with a demonstrated research contribution.

## Progress made in this pass

- S50 and S51 are now acquired publisher articles with purpose-scoped dossiers, page mappings, evidence tables and critical appraisal. Both earlier acquisition requests are resolved.
- S50 supplies a close 1D experiment/model comparator alongside S10. It already discusses losses, wall conduction and omitted expansion-tank storage. The facilities/scenarios are closely related; independent datasets are not established.
- S51 already combines uncertain parameters, competing heat-transfer correlations and computed thermal-margin failure events. Its reported numerical probability and sampling interpretation remain qualified; they cannot serve as a validated target.
- S49's supplied README identifies Wisconsin FLiBe-loop data and analysis software. Archive inventories were recorded; the scientific dataset's provenance is consistent with the earlier catalogue, but exact bytes/version-to-publication mapping is not independently certified.
- Flow Tests 5 and 6 are excluded at the user's direction. Flow Test 4 contains seven CSVs, about 1.539 GB uncompressed; no raw time-series processing performed. Codes and logs were inventoried only; no supplied code executed or analysis claimed.

## Motivation narrative now supported, with boundaries

Natural-circulation loops have several distinct roles: mechanisms/stability research, material and instrumentation testing, operating experience, and passive heat-removal studies. S50 is explicitly motivated by high-temperature-reactor and solar applications; S51 describes a DRACS-inspired facility. Earlier S40–S42/S47 and S43 history notes supply separate historical/materials/reactor evidence with their stated reading limits.

Therefore “this is a natural-circulation loop” is not sufficient to assert that it represents an MSR. For every application, the review needs a reactor subsystem, an engineering decision, a corresponding QoI, and a similarity/omitted-physics argument. Passive decay-heat transport, forced-circulation primary operation, externally heated test sections, and volumetrically heated liquid fuel must remain distinct. No new claim of a universal historical origin, reactor-scale validation, or a TRIDENT-specific dimensional match is made in this pass.

## Candidate contribution hypotheses after the new prior art

| Existing hypothesis | Strengthening needed | Feasible minimum evidence |
|---|---|---|
| H01: identifiable physical reduction with sparse observations | Establish which parameter groups and QoIs are distinguishable when duty, regional loss and sensor uncertainty are included | Physically consistent model/observation map, an independent energy/capacity anchor, profiles or equivalent identifiability checks, withheld thermal predictions |
| H02: QoI-dependent retained-physics selection | Go beyond showing that wall/tank storage matters; test a criterion predicting when a simpler model becomes inadequate | Nested conservative models, declared QoI tolerance, multiple withheld transients/regimes; CFD optional for measured thermal QoIs |
| UQ/margin hypotheses already in state record | Distinguish interval width from calibrated predictive uncertainty and probability from a tolerance bound | Explicit sources/dependencies, independent assessment, numerical-error checks and physically appropriate threshold events |
| Local recirculation extension | Establish observable thermal consequences first; extent and causal heat-transfer changes remain conditional | Suitable local evidence or qualified CFD would be necessary for field claims; sparse temperature agreement alone is insufficient |

These are research questions, not established literature gaps. Elementary scale ambiguities, adding storage, Monte Carlo propagation, model switching or a dashboard are not by themselves sufficient thesis novelty.

## Next reading and production sequence

1. **S18 + S23:** complete the existing accessible conjugate/Fourier-model and profile-likelihood extractions. Produce a model/observation/estimand table, check conservation, signed circulation, temperature-dependent enthalpy, sensor mapping and non-identifiable parameter combinations.
2. **S07 + official S53:** retrieve/read available experiment-design and passive-reliability methodology. Relate design utility to achievable Nick-plan experiments, model discrimination and QoI uncertainty; avoid importing a probability convention from S51 without verification.
3. **S14/S15 + S44/S45:** finish similarity, heating-arrangement and mixed-convection evidence needed for the history/MSR-transfer chapter. Assemble application-specific transfer and distortion tables.
4. **Write the two first complete review drafts from the shared ledger.** Methods chapters: model hierarchy → governing/reduced models → observation/identifiability → experiment design → UQ → V&V/implementation contracts. Motivation chapters: historical purposes → reactor subsystem/decision/QoI → prior demonstrations → similarity limits → unresolved questions → feasible contribution tests.
5. **Adversarial revision:** compare proposed claims against S50/S10, S51, S26, S30 and other closest work; replace unsupported “gap” language with a question or remove it. Preserve a no-CFD minimum scope and conditional extensions.

Steps 1–3 can proceed without further uploads. The two requested papers below strengthen the theory/novelty comparison; they do not block drafting already supported material. This is a sequence, not a promise to finish all scientific work in seven days.

## Ranked help requested

The complete acquisition table is in **Literature_Acquisition_Requests.md**. Only two new priority PDFs are requested: S52 (actual LeBENC formulation referenced by S50) and S30 (recent stochastic NCL reduction). Publisher/author accepted manuscripts are both useful; retain cover/version information. Do not upload more bulk flow data.

An optional small project input would help more than additional datasets: identify the first two or three decisions/QoIs the proposal should prioritize and which independent duty/capacity/flow evidence is actually available. Existing PF01/PF02–PF06 unknowns remain open; this is not a request to repeat the documents already supplied.

## Search and reading limits

Search date 2026-10-20. Queries included both new DOIs; exact S52 title plus PDF/DOI; exact S30 title plus PDF/Purdue/repository; passive-reliability report title/number and Wilks/tolerance searches. Publisher identity records were checked; S30/S52 full-text routes did not yield a usable manuscript. Official IAEA-TECDOC-1752 PDF is accessible; only identity/front matter inspected this pass. OECD status-report URL was a discovery lead and failed retrieval, not a read source.

This is a focused continuation, not a systematic review with exhaustive database coverage. Search failure does not prove unavailability or absence of prior art. Source dossiers distinguish text inspection, selected visual checks, inaccessible implementations and unperformed reanalysis.
