> Current deliverables: Methods_and_Theory_Review_Working_Draft.md, Motivation_and_Contribution_Review_Working_Draft.md and Upload_Requests_Current.md supersede prior reading/access statuses.

> Current checkpoint: see **Review_Progress_and_Next_Steps_2026-10-20.md**, S50/S51 dossiers and current acquisition requests. Earlier acquisition statuses below are historical.

# What S10, S48 and the original protocols change

20 October2026. Evidence extraction and critical appraisal complete for the declared scope; final thesis direction and field novelty remain undecided. The original governing brief, Markdown collé.md, is unchanged.

## Decisions strengthened or revised

| Decision | New evidence | Consequence |
|---|---|---|
| Is transient experiment–CFD comparison itself new? | S10 already treats steady behavior, startup, power changes, trip and loss of forced cooling | No. A contribution must add a method/result beyond another loop model and matching temperature curves. |
| Does a simple loop model need tank/solid storage? | S10's trip comparison changes when the expansion tank is included; S44 already treats conjugate dynamics | Include a tank/participating-solid option in the comparison hierarchy. Retain it only if the chosen QoI and independent evidence justify it. |
| Is adjoint QoI sensitivity new in salt-related natural circulation? | S48 already derives and compares sensitivities of mass flux, temperature and cooler Nu | No generic novelty. Direct/AD sensitivities may suffice for a small parameter set; an adjoint is justified by actual objectives/parameter count and a credible forward model. |
| Does S48 prove global reliability or dynamic stability? | The reported comparisons are local sensitivities, with cross-method numerical checks | No. Functional probabilities and stability boundaries require different analyses; read S51 for the closest probabilistic-reliability challenge. |
| Does Nick's plan lack UQ/holdouts? | Original Phase1–4 documents explicitly contain covariance, effective sample counts, freezing and blind/applicability checks | Earlier uncertainty about those provisions is resolved. Preserve them and address the narrower issues documented in the reconciliation. |
| Can passive relaxation calibrate absolute losses before blind Phase3? | Phase2 says capacities/inventories fixed “where practical”; the exact independent anchor is not specified | Make the anchor explicit. If it uses Phase3 duty, change the run's role and preserve new independent assessment; otherwise retain ratio/group-only claims. |
| Can total loss validation establish corrected primary flow? | Phase4 needs local heater/cooler losses and bulk enthalpy, not just a whole-loop total | Validate or bound the allocation/observation map separately. Reconciled energy estimates remain model-dependent. |

Source-level evidence is in the S10/S48 dossiers and **Nick_Plan_Reconciliation_2026-10-20.md**. These findings do not justify importing either paper's coefficients/equations without its qualifications.

## An especially useful identification counterexample

**Analyst derivation from the Phase4 measurement model; not claimed as a novel published theorem.**

Let the heater and cooler losses change by \(+\delta\) and \(-\delta\), leaving the measured total ambient exchange unchanged. With all other quantities fixed,
\[
\delta\dot m_H=-\frac{\delta}{\Delta h_H},\qquad
\delta\dot m_C=-\frac{\delta}{\Delta h_C}.
\]
When the two primary enthalpy changes are equal or nearly equal, the inferred flows shift together. Their difference may remain zero or small even though their common value changes. Small perturbations can respect any nonnegative-loss constraints where the original losses are positive.

Therefore a whole-loop heat-loss match plus compatible heater/cooler flow estimates does **not** uniquely validate each regional loss correction or the true primary flow. This is a concrete target for identifiability analysis and experiment-value assessment: what independent inventory, local thermal evidence, controlled intervention or verified spatial model removes the consequential ambiguity? A theorem for a useful model class plus independent empirical consequences would be more substantive than simply presenting this elementary algebra.

## Feasible contribution packages after the challenge

**H01 remains plausible, narrower:** characterize identifiable physical groups and QoIs for conservative regional/segmented loops with realistic boundary, observation and initial-state uncertainty. Include graph consistency and energy-scale assumptions explicitly. Compare established grey-box selection/topology methods; the elementary scaling and graph-balance checks are background, not PhD novelty.

**H02 needs a stronger distinction:** use independent QoI assessment and uncertainty/measurement constraints to decide when tank, wall, spatial or momentum enrichment is necessary. S10/S44 already show enrichment matters in particular cases; S48 already supplies adjoint local sensitivities. A proposed advance could be a tested selection/experiment procedure with an adequacy or identification boundary, rather than another sensitivity ranking.

**H03 remains conditional:** observation-consistent local thermal correction/reconstruction needs qualified spatial evidence. Sparse TRIDENT temperatures do not independently validate recirculating volume or causal local enhancement. No CFD availability is assumed.

**H04 remains open to stronger counterexamples:** generic uncertainty propagation and reliability analysis for salt loops already exist as literature leads, including S51. Read the original before promising a new uncertainty/reliability framework. A possible distinction is inference/transfer under shared calibration, model-dependent flow and incomplete observation, tested against established alternatives.

## Minimal useful work that does not require TRIDENT CFD

1. Specify a small conservative model family and explicit observation map, separating measured point/path values from effective and bulk temperatures.
2. Prove/check its scale, graph and observation ambiguities; state which QoIs change along unresolved parameter directions.
3. Compare simple response, reciprocal/regional and segmented loop baselines under the same evidence budget.
4. Rank feasible experiments by reduction of the consequential ambiguity or held-out QoI error; preserve original protocol assessment roles.
5. Use measured/regional temperature and net-duty claims as the minimum demonstration. Treat local extrema/extent as conditional extensions with explicit stopping criteria.

No operating data were analysed, no scientific test was executed and no new thesis result is claimed in this pass.

## The next manageable reading/acquisition batch

**Available:** S18 conjugate1D loop, S23 profile likelihood/identifiability, then S07 experiment design. Those can proceed immediately.

**Requested next, after targeted public retrieval failed:**

| Rank | Exact paper | Question it resolves | Why the current evidence is insufficient |
|---|---|---|---|
| 1 | **S50** A.K. Srivastava et al.2016, *Experimental and theoretical studies on the natural circulation behavior of molten salt loop*, Applied Thermal Engineering98,513–521, [DOI10.1016/j.applthermaleng.2015.12.065](https://doi.org/10.1016/j.applthermaleng.2015.12.065) | Closest experimental/1D comparator; how loss, properties, transients and possibly shared S10 data were treated | Verified metadata and publisher abstract only; full equations, uncertainty and independence cannot be inferred from S10/S48 citations. |
| 2 | **S51** X. Jiao et al.2018, *Functional reliability analysis of a molten salt natural circulation system*, Nuclear Engineering and Design332,127–136, [DOI10.1016/j.nucengdes.2018.03.024](https://doi.org/10.1016/j.nucengdes.2018.03.024) | Strong challenge to generic UQ/margin/failure-probability novelty; probability definitions, correlated inputs, model errors and validation | Primary abstract/identity checked; no complete manuscript retrieved. No reported failure probability or uncertainty coverage is accepted as extracted evidence here. |

For S50 request the full journal or matched accepted manuscript, including any used supplement. Inspect the lower-order balances/closures, experimental duty/flow measurement, property/heat-loss treatment, transient comparisons and calibration/assessment partition. Without it, retain the minimum comparison but keep closest-1D-method novelty unresolved.

For S51 request the full journal or matched accepted manuscript, including any supplement defining input distributions, model/correlation uncertainties, dependence, failure limits, sampling/convergence and experimental checks. Without it, avoid a claimed new probabilistic-reliability framework; temperature/duty identifiability work can continue.

S43's supplement and S49 documentation/code remain optional for reproducing that external dataset. S48's original MATLAB implementation would help resolve its printed conventions, but is not necessary to proceed with an independently specified forward model. No repeat upload of S10/S48 or the five protocols is needed.

## Coverage, limitations and records

Both main articles' relevant methods/results/limitations were read; S48 AppendicesA–B were inspected, with explicit limits on independent derivation/reproduction. All five original protocol bodies were inspected for the questions at issue; Phase1's worked examples were not fully audited, nor was the apparatus schematic matched to CAD. Draft requirements remain separate from installed/approved/observed facts.

Targeted web retrieval on20 October2026 checked publisher identities and the new S50/S51 leads using exact-title searches, publisher pages and Crossref metadata. Public full-text searches did not yield usable manuscripts; publisher routes were blocked/catalogue-only. This is not an exhaustive access or novelty search, and no subscription access was assumed.

The source registry, claim ledger,62-question matrix, project-document register, acquisition queue and research-state record are updated. Existing source/claim IDs remain stable. Prior P0 memo/readiness statements are superseded where this batch supplies new evidence.
