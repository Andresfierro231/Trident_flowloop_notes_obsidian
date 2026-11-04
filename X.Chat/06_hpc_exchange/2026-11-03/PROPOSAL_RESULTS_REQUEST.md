# HPC researcher prompt: committee proposal results

## Objective and startup
Supply a focused evidence package for a concise PhD proposal: introduce the project, demonstrate existing capability, and support a credible twelve-month research plan. Use undergraduate engineering language. The manuscript has styled planned-result boxes; replace them only with supported results.

Pull the notes and proposal repositories independently and read their AGENTS/current status and the HPC initiative's own instructions. Confirm actual host, source roots, branch and commit. Use an isolated task branch/worktree. Preserve the existing HX-20261102 question IDs; this request adds PRR-20261103-01 through -10. Saving/pushing this packet is not acknowledgment.

First inventory existing qualified studies, tables and figures. If a requested product is unavailable, return a proposed study card (question, inputs, model change, outputs, estimated cost, dependencies and applicable authorization) rather than inventing data. New operating-data processing, CFD/experiment execution and other held work require their existing explicit scope/approvals. This packet authorizes preparing requests, not executing held activities.

## Deliverables, shared format
- One concise RESULTS.md: main claim, supporting assets and exact source for each PRR ID; identify ready / partial / proposed / unavailable.
- figures/: vector PDF plus PNG preview and underlying CSV; tables/: LaTeX fragment plus CSV; manifest.json: source study/run/model/data IDs, commit/hash, units, geometry/fluid revision, inputs, sensor policy, fitted quantities, case roles, uncertainties and relevant exclusions.
- Caption draft: one claim, quantities/units, configuration/condition, measured versus supplied versus computed values, and source citation. Keep detailed case-use/exposure discussion in the internal manifest, outside committee prose. Do not upgrade a supplied-input reconstruction to an independent forecast.
- Existing literature source/claim IDs and original A1–K5 remain unchanged. Use fierroMasters2026 in new manuscript citations; fierro2026cfdoneD is a retained bibliography alias.
- Use legible axes and legends, consistent models/colors/units, uncertainty where available, and concise panel labels. No fabricated curves, scores, FLOP estimates or confidence bands.
- Organize figures by the requested claim, not by every available run. Prefer one representative plot plus a compact summary over many similar plots.
- Return analysis/report paths, source hashes and exact line/table/equation locators. No private credentials, whole raw data bundles or unrequested external communications.

## Requested products

### PRR-20261103-01 — Latest TAMU temperature comparison
Placement: Chapter 2, sections/outline/02_preliminary.tex, slot:tamu-temperatures.
Use the current best documented physics-based TAMU surrogate. Produce two panels: fluid temperatures and wall temperatures versus loop position (m or a clearly defined normalized coordinate). Overlay ROM, CFD and qualified experimental observations as distinct series. State actual heater/cooler condition, fluid and model setting. Add bias/RMSE by sensor family (K) and a small case-summary table. Keep CFD agreement and experimental agreement in separate columns. If experimental pairing is unavailable, provide the supported CFD panel and name the missing pairing.

### PRR-20261103-02 — Assessed operating range
Placement: Chapter 7, sections/outline/07_assessment.tex, slot:operating-range.
Map the actual tested heater and cooler conditions: use heater input (W) on x, an actual independently varied cooler quantity (with units) on y, and temperature RMSE (K) as color. If the data are not a rectangular grid, plot the observed points, without interpolating a fictitious tested region. Identify the selected model/configuration and give the tested property/temperature range. Supply companion CSV, case count and error definitions.

### PRR-20261103-03 — Forward-solve cost and operation count
Placement: Chapter 2, sections/outline/02_preliminary.tex, slot:accuracy-cost.
Plot number of axial volumes (x) versus steady forward-solve wall time (s, logarithmic y if helpful), with temperature/energy convergence in a companion panel. Table: model/version, volumes/states, hardware, compiler/settings, solver tolerance, repeat count, median and spread, and one-time versus online work. Report FLOP count per solve only if measured or justified from the algorithm; distinguish counts from FLOP/s. Never estimate FLOPs as runtime times peak hardware rating. If only existing timings are available, report those and propose a bounded benchmark for missing fields.

### PRR-20261103-04 — TRIDENT temperature-reproduction demonstration
Placement: Chapter 4, sections/outline/04_evidence.tex, slot:experiment-demo.
Select the strongest existing documented ACU or VCU example. Three aligned time panels: measured/model temperatures (C or K), sensor residuals (K), and actual heater/cooler/ambient inputs. Show initialization, fit quantities and uncertainty in caption/manifest. Primary temperatures used as forcing must be labeled as supplied inputs. Prefer a few interpretable probes spanning the relevant heat paths. Summary table: sensor group, time span, bias, RMSE, and the main physical lesson. This is the core first-year feasibility example.

### PRR-20261103-05 — Compact setup and readiness table
Placement: Chapter 4, sections/outline/04_evidence.tex, slot:facility and slot:evidence-readiness.
Provide one simple existing/approved schematic for each selected configuration, indicating heater, cooler, fluid path, gravity direction and used sensor positions. Use the actual revision and fluid. No new CAD parsing/execution without its applicable approval. Table: facility/case, available observations, CFD availability, supported comparison, existing result and next dependency. Keep detailed geometry inventory in the manifest.

### PRR-20261103-06 — Probe-to-bulk temperature meaning
Placement: Chapter 5, sections/outline/05_model.tex, slot:probe-map.
Use an existing CFD section/field and corresponding profile: temperature versus radial position (or clearly defined local cross-section coordinate), with bulk/transport temperature, wall and probe locations identified. Add velocity/profile information only where it explains the temperature interpretation. State how averages and sensor projections are calculated. Supply a small table quantifying the difference between the simple bulk-observation assumption and the mapped probe value under the same condition.

### PRR-20261103-07 — A controlled model-choice comparison
Placement: Chapter 6, sections/outline/06_methods.tex, slot:model-comparison.
Compare a conventional physical model and one justified change (closure, observation map or added state). Use the same actual cases and input information. Report temperature error (K), a physically matched heat-budget quantity and forward runtime (s). A grouped chart or paired-point plot should show what the change buys. Include parameter/state count and the result's physical explanation. If extra complexity does not help, report that result and the evidence for retaining the simpler model.

### PRR-20261103-08 — Evidence for the PhD contribution
Placement: Chapter 3, sections/outline/03_research.tex, slot:contribution.
A three-row table: aim, exact model/method change, closest comparator, evidence product, result/insight and next test. Each result must cite an existing study or be explicitly marked proposed. Prioritize one defensible study per aim. For parameter ambiguity, report which output remains constrained and the observation that would distinguish competing explanations; avoid presenting a failed fit alone as the contribution.

### PRR-20261103-09 — Response, settling and useful uncertainty
Placement: Chapter 7, slot:operating-range, and Chapter 8 operator scenario.
For an existing assessed heating/cooling transition, plot temperature versus time with prediction/measurement, supported uncertainty and input change. Define settling time using a stated tolerance and observation duration; do not invent an agreed acceptance threshold. Give initial-state information, measured boundary histories and the physical explanation of the dominant lag. If no such study exists, propose a bounded transition study and list missing inputs.

### PRR-20261103-10 — Matched heat-path interpretation
Placement: Chapter 6 model-choice comparison and optional Chapter 2 supporting figure.
Produce a regional heat-rate (W) comparison using common physical boundaries for CFD and ROM. Separate cooler, ambient and relevant local paths; show whole-loop energy residual. If the groupings do not match, provide a mapping table and avoid computing a misleading component error. State one conclusion about what temperature agreement does or does not constrain; keep the committee caption direct and the detailed attribution caveats in the manifest.

## Placement and integration
Each slot label is in the active source. Write new asset fragments in a dated internal results directory on your branch, with suggested includes/captions; do not silently merge or replace active writer text. Deliver a proposed study/asset index even if some results are unavailable. The local writer will select figures and integrate the shortest supporting claims.

The twelve-month plan is proposed: months1–2 first reproduction; 3–5 steady/closure comparisons; 6–8 selected transitions; 9–10 operator example; 11–12 synthesis and dissertation. Identify existing results that accelerate the early milestones, and list a practical fallback for missing CFD/experimental evidence.

Finish by committing/pushing the task branch and reporting its name/commit, ready assets and unresolved requests. Record actual acknowledgment separately from publication.
