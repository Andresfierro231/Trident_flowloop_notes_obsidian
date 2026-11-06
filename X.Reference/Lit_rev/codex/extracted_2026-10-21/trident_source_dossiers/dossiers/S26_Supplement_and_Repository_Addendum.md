# S26:SUP1 / S26:CODE1 — supplement and fixed-commit repository addendum

2026-10-20. Supplements the existing S26 dossier; existing S26-C01–C08 remain stable. **Ready to challenge method/novelty and define a comparator. Not a reproduced inference study.**

## Identity and completeness

Supplied “manikkan suplemental data.pdf”: 28 readable PDF pages, printed 32–59, Appendices A–D, Eqs.25–32, Tables6–7, Figs.19–44. Printed page = PDF page +31. Author-manuscript typesetting/line numbers differ from the 19-page journal main paper. Subject, symbols, cases and references to main figures match S26, but a complete journal-supplement revision match is not independently certified. PDF metadata dates 21 July 2026; use as a supplied author-format supplement rather than invent a publisher version. All appendix text and plot overviews were inspected; trace curves were not digitized and no chain diagnostics were recomputed.

Repository: [PredictiveScienceLab/entropy_switch_thermal_rc_paper](https://github.com/PredictiveScienceLab/entropy_switch_thermal_rc_paper/tree/76ac6ecabab658a00dbf76a34abf24ae3b3dcb61), fixed commit **76ac6ecabab658a00dbf76a34abf24ae3b3dcb61**, commit date 7 July 2026. README and selected code definitions were inspected. The repository explicitly targets the synthetic 4R3C example and a single-chain workflow. This does not establish reproduction of every journal example, multi-chain mixing, or real-building results. No MCMC or notebook was executed.

## Extracted evidence

Appendix A (PDF1/32, Eqs.25–29) argues an OFF ReLU latent parameter has zero likelihood gradient. For strictly negative latent θ, \(S(\theta)=\max(0,\theta)\) is locally constant, so this conclusion follows if all dependence enters through that switch and initial conditions are independent of θ. At θ=0 the derivative convention requires care. **Analyst qualification:** Eq.28’s written state-sensitivity chain is abbreviated: the general sensitivity also contains propagation through \(f_x\,\partial x/\partial\theta\). The zero-sensitivity result still follows from the homogeneous sensitivity equation under those assumptions. A flat likelihood direction is not evidence that the corresponding physical parameter is identified; its posterior depends on the prior and mixing across topology regions.

Appendix B.1 (PDF1/32) reports 2017 Euler-generated steps, 300 s sampling, retaining every other point (1009 points), noisy observed temperatures and noisy inputs generated before simulation. This is **known realized input forcing**, not inference with uncertain measured input channels. Appendix B.3/Table6 (PDF2/33) records the synthetic truth. Table7 gives inference/recalibration runtimes; these are machine/workflow observations, not a TRIDENT latency forecast. The input sinusoid in Eq.30 uses \(t/24\) while prose calls t seconds; the inspected generation code uses hour-like t values. Units must be resolved before replication.

A further source-unit issue persists: B.1/Eq.32 use W/m² for source scale, whereas C.1 calls solar irradiance and delivered heat W (PDF17/48); D.1 distinguishes appliance kW from synthetic solar kW/m² (PDF23/54). A source multiplier may therefore be an effective area/partition as well as a scaling coefficient. Do not interpret it as a dimensionless fraction or material property without the particular input definition.

Appendices B.6–B.12 (PDF4–16/35–47) provide traces, autocorrelation, split-R-hat and ESS. Full-chain diagnostic panels show substantial failures for some parameters, consistent with the main paper’s admission that chains do not explore common modes. Good within-chain split diagnostics cannot establish global posterior exploration. Configuration frequencies from a selected chain are conditional frequencies, not verified total posterior model probabilities.

Appendix C.1 (PDF17/48): four offices, 1-minute data subsampled to 5 minutes, first 300 points for inference and 2579 subsequent test points. Appendix D.1 (PDF23/54): residential measurements at 5 minutes, first900 points/75 h for inference, missing values interpolated and solar forcing synthesized from location. Input uncertainties and interpolation/model errors are not a complete predictive discrepancy treatment. The building data are cross-domain analogies for thermal learning, not natural-circulation transport evidence.

## Code checks and version differences

The fixed-commit `synthetic_4r3c_utils.py`, lines128–208, implements ReLU gates, shared conductive terms, and \(\dot T_j=g_j[Q_j+\sum_k\eta_{jk}(T_k-T_j)]\). Setting g_j OFF freezes its state; it does not impose a zero-capacity algebraic balance. Lines303–370 generate noisy forcing and Euler states. Lines449–500 use division by fixed positive scales with zero lower bound, which is not a general affine mapping onto [−1,1]. The synthetic train split here is 200 points; this is close to 20% of1009, but version/settings must be retained rather than claimed identical by description alone. The generator clamps the sinusoidal solar part before adding Gaussian noise, so negative realized values are possible.

Lines764–811 threshold posterior samples and count configurations; that computation does not itself solve multimodal mixing. MCMC defaults in the utility configuration include one chain. No full audit of the notebook, dependency pinning, random seeds, real-data processing or every physical back-transformation was performed. Supplied appendix and repository share the model family but differ in formatting, unit descriptions and configurable workflow; keep those assets separately identified.

## TRIDENT implications and coverage

Use a small constrained network and an explicit topology-selection baseline before entropy-switch inference. Compare physical admissibility, identifiable parameter groups, independent QoI predictions and posterior diagnostics. Source fractions must obey an energy-partition constraint if interpreted physically; independent nonnegative priors alone do not ensure their sum is one. Conservation of internal conductive exchange does not prove that external deposition is correct. Retain uncertainty in boundaries, initial hidden states and discrepancy separately from parameter-switch posterior variability.

| Component | Status | Remaining limit |
|---|---|---|
| Appendix A | Inspected/extracted | Derivation qualified; no formal independent theorem proof |
| Appendix B.1–B.4 | Inspected/extracted | Generation, priors/truth and runtime; unit conventions unresolved |
| B.5–B.12 | Text and plot overviews inspected | No digitization/recomputed convergence |
| C.1–C.4 and D.1–D.3 | Inspected/extracted selectively | Data preparation and diagnostic limits; no original raw-data replication |
| README and selected utility/class code | Inspected | Fixed commit; notebook not audited or executed |

| Claim ID | Claim | Locator | Qualification |
|---|---|---|---|
| S26-C09 | OFF-gate likelihood flatness is a local sensitivity property | SUP1 AppendixA/Eqs25–29, PDF1/32 | Assumptions on dependencies and θ≠0 |
| S26-C10 | Synthetic forcing noise is realized before simulation | SUP1 B.1, PDF1/32; CODE1 generator | Not full errors-in-input inference |
| S26-C11 | Full-chain diagnostics limit posterior model-probability claims | SUP1 B.10–12/Figs30–32, PDF14–16/45–47 | Plot inspection, no recomputation |
| S26-C12 | Repository is a synthetic single-chain implementation with explicit gates | CODE1 README; utility128–208,764–811 | No full-paper reproduction |
| S26-C13 | Units, time and normalization differ or need clarification across assets | SUP1 B.1–B.2,C.1,D.1; code303–370,449–500 | Do not silently standardize |
