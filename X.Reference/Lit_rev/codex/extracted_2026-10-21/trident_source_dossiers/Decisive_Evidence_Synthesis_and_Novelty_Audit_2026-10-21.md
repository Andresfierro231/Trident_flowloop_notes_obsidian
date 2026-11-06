# TRIDENT decisive evidence synthesis and contribution audit

21 October 2026. Continues the checkpoint and `Markdown collé.md`; no source, claim, hypothesis or original-question ID has been renumbered. Six purpose-scoped dossiers add **56 claims**: S19-C01–08, S74-C01–08, S72-C01–10, S71-C01–09, S73-C01–08, S29-C01–13. The count includes a source-plot uncertainty qualification. Source methods, cited results and our dimensional/arithmetic appraisal remain separate in the dossiers. Both reviews are now v0.7 working drafts.

## What this batch changes

The literature already supplies each broad ingredient of the favored approach: thermal networks and stochastic estimation; prediction-oriented design and calibration; conjugate loop reduction; modern oil/salt loop comparisons; and multigroup surrogate scaling. A thesis cannot establish novelty by collecting these ingredients. Its useful additional result must be narrower, falsifiable and assessable with the actual evidence.

| Source and inspected version | Established or reported result | Consequential boundary for TRIDENT |
|---|---|---|
| S71, arXiv2403.18072v2, 28pp | Nonlinear QoI-information design; separate observation and prediction maps | Utility depends on assumed physics/prior/noise and MCMC/KDE accuracy; no physical loop validation |
| S72, published CMAME448,118486,26pp | Nested discrepancy fitting and goal-weighted physical calibration | Observation-level discrepancy does not directly give unobserved-QoI error; ordinary MLE wins reported validation metric; printed metric normalization flagged |
| S73, published Automatica40,225–237,13pp | Continuous–discrete Itô grey-box ML/MAP/EKF; thermal-wall example | State-independent diffusion and approximate Gaussian filtering; simulated examples/local asymptotic uncertainty |
| S29, published PartII,36pp | Th-66 loop experiments and loss-inclusive CFD comparisons | Flow indirectly inferred; same-experiment numerical/model selection; residual flow/response mismatch; achieved salt similarity not demonstrated |
| S19, published ATE284,128986,12pp | LiCl–KCl external thermometry, steady CFD and thermal flow estimates | No direct flow validation; measured thermal boundaries; local structures modeled; grid-ratio discrepancy |
| S74, published ANE225,111757,19pp | Modern H2TS comparison of oils/reference designs | Idealized loss/storage assumptions; matched-correlation Nu agreement is consistency, not independent transfer validation |

Dossier locators are authoritative. Reported numerical deviations should not be promoted to universal uncertainty limits. In S19, “5.5%” concerns a difference between comparison discrepancies. In S29, some Figure19 bars are explicitly |CFD−experiment|, and Figure21's separately labeled flow curves lack demonstrated independent provenance. In S72, Table8's model-only validation ordering is informative, but Eq46 divides 126 summed residuals by1134; absolute “RMSE” values need clarification before reuse.

These qualifications do not make the studies useless. They identify what the experiments/calculations actually support and prevent our review from inheriting stronger validation claims than their evidence warrants.

## Hypotheses retained with narrower increments

| Existing ID | Closest challenge | Possible additional result | Minimum evidence and fair test | Falsifier/fallback |
|---|---|---|---|---|
| H01 — identifiable physical reduction | S23/S26/S67–S70; now S72/S73 and S19/S29 inference | A nontrivial invariant/identifiability result for a specified conservative loop/model class with uncertain boundary and observation maps; show which QoIs remain supported | State the class, observation map, nuisance quantities and energy anchor; compare grouped and overparameterized models under common data/holdouts | Known grouping already explains result or predictive effect absent; fall back to a precise limit on supported quantities, not a claim to new estimation theory |
| H02 — QoI-dependent retained physics | S18/S52/S59/S65/S66; now S71/S72 | A criterion predicting when omitted storage/transport/source physics violates a declared QoI tolerance across unseen conditions | Small nested physical hierarchy, independent inputs/thermal assessment, tested criterion beyond fit improvement; compare MLE/stochastic/goal alternatives only as justified | Criterion merely restates sensitivity or fails new conditions; retain measured thermal/duty/response scope |
| H03 — local consequences and extrema | S21/S35/S37/S46/S60; now S19/S29 local fields and S72 restriction | An observation-consistent local thermal bound or a rigorous ambiguity result for a defined descriptor; extent and thermal consequence remain separate | Qualified spatial reference for field claims; independent observations for experimental claims; controlled comparisons for causality | Different fields explain same observations; with no qualified reference, drop experimentally validated recirculation extent and retain supported thermal outputs |
| H04 — uncertain surrogate-to-salt transfer | S15/S36/S56/S64; now S74 and S29 | Quantify how unavoidable source/loss/storage/property/observation distortions change a specified prediction, rather than only matching groups | Explicit target circuit/fluid/envelope and source path; assess uncertainty and distortion against that QoI; compare existing scaling methods | Existing scaling already answers it, target undefined or uncertainty dominates; retain mechanism analogy and facility prediction |

All four are **provisional contribution hypotheses**, not established vacant gaps or selected dissertation aims. An uncertainty-aware experiment request can serve H01/H02/H04 without becoming a fifth renamed hypothesis. S75/S76 must challenge any claim about unobserved-QoI adequacy or new validation design before that claim is described as novel.

A negative result can advance understanding if it identifies a precise indistinguishability class, regime/tolerance boundary or infeasible measurement-to-target inference, and demonstrates an engineering consequence. Failure of a single fit, failure to obtain CFD, or broad statements that sparse data are difficult are insufficient.

## Engineering motivation after the comparator checks

Natural-circulation loops have several documented missions: physical transport/stability studies, material/salt exposure, code/model assessment, scaled component/system testing and selected passive heat-removal questions. The earlier S40/S41/S42 historical evidence remains; normal pumped MSRE operation is not relabeled as natural circulation. This pass makes no first-loop discovery claim and does not repeat the unverified 25% MSRE story.

S29's loss-of-sink and reduced-power protocols illustrate relevant heat-removal questions, but they are electrically heated laboratory histories, not validation of nuclear scram/decay-heat behavior. S74's design comparisons distinguish liquid-fuel and solid-fuel salt systems. A quantitative MSR representation requires a named circuit, source distribution, geometry, property envelope, wall response, sink and relevant groups. A candidate surrogate fluid can still be operated outside the matched regime, as S29 explicitly acknowledges for Pr.

For the proposal, the defensible argument is that such loops permit assessable investigations of coupled heat transport whose models and uncertainties matter to engineering decisions. The scientific task is to determine which predictions can be supported, which physics the evidence requires and what additional evidence would resolve consequential ambiguity. Whole-reactor similarity is conditional and may be unnecessary for a valuable facility-level methodological result.

## Minimum model/inference comparison and evidence firewall

Begin with an energy-consistent simple baseline and a small conservative regional/segmented hierarchy. Retain a parameter only when its meaning and information support are explicit. Compare on measured thermal/duty/response QoIs first. Use the same inputs, adjustable quantities, nuisance uncertainty and development cases. More detailed states or a Bayesian label should not receive additional hidden calibration information.

Keep four assessment objects separate:

1. Numerical verification of the governing/discrete solution for the claimed QoI.
2. Parameter/state calibration and model/closure/observation selection.
3. Independent physical predictive assessment on withheld runs/conditions.
4. Transfer to an unobserved quantity or another fluid/circuit.

Success at one does not certify the others. A mesh selected by agreement with experiment is development evidence. Shared temperature-derived flow and duty are dependent observations. Pointwise snapshot splits are weaker than case/regime-out splits for transfer. Local contour fields are neither independent measurements nor proof of a heat-transfer counterfactual. The equation/convention companion specifies the code-facing implications without executing any model or operating data.

## Next batch and acquisition decision

The next high-value batch is **S75 then S76**, or jointly if distinguishing model-error propagation from validation design is easier. They were retrieved from S72's citations, not through a new broad search. S75's43-page author manuscript and S76's31-page arXivv1 are available; identity/related journal DOI checked, technical content unread and final-version differences unverified. Their original claims are not used in this synthesis. Then read targeted official measurement-model/covariance/Monte Carlo sections S32/S31/S02 to complete the implementation uncertainty contract. S24 is conditional on a feasible learned-model comparator; S11 is later terminology support.

No essential upload blocks progress. **S20** remains the most useful conditional request if H03/local-flow extension is retained: DOI10.1016/j.pnucene.2023.104880. S71's journal PDF is optional exact-version closure, DOI10.1137/24M1649344; its available v2 supports the current limited analysis. S19/S72/S74 requests are resolved. S75/S76 do not need uploads. Do not request bulk operating datasets, FlowTests5/6 or Ethan discrepancy reconciliation for this reading pass.

Remaining consequential gaps are the next two original-method readings, selected official metrology coverage, exact implementation conventions, project decision tolerances/energy/observation/holdout facts, and conditional local-reference evidence. No final method direction, qualified TRIDENT CFD, new instrument, completed experiment, novel theorem or independently validated reactor prediction is claimed.
