> **Supplement update,20 October2026:** SUP1 was subsequently supplied and scoped-extracted. See [S26_Supplement_and_Repository_Addendum.md](S26_Supplement_and_Repository_Addendum.md). This main-article dossier preserves its original evidence/claims; statements below that the supplement was unavailable describe the earlier checkpoint. S08 selected methods have also now been extracted in the methods bridge.

# S26 — Entropy switch for Bayesian thermal network discovery

**Acquisition update,20October2026:** S26:SUP1 is now uploaded (28pages,printed32–59) and the author repository README is inspected at commit76ac6ecabab658a00dbf76a34abf24ae3b3dcb61. Supplementary proof/data/diagnostics and code remain unextracted/unexecuted. Earlier missing-supplement statements below describe the initial audit checkpoint; they are no longer outstanding upload requests. Purpose-specific readiness is unchanged until that extraction.

Audit date: 2026-10-20. Citation: Sreehari Manikkan, Panagiota Karava and Ilias Bilionis, *International Journal of Thermal Sciences* 230 (2026), 111148. DOI: https://doi.org/10.1016/j.ijthermalsci.2026.111148. Publisher PII: S1290072926004928. The supplied 19-page journal article reports acceptance 30 June and online publication 26 July 2026. It is the journal version, not the earlier SSRN record. PDF page = printed article page. All main-text pages and references were read; selected equations and Tables 3–4 were visually checked. No missing main-text pages or unreadable equation images were detected. Separate Supplementary Material is referenced but was not supplied or retrieved: this materially limits reproducibility readiness.

## Question and actual contribution

The paper infers a sparse thermal resistance–capacitance network and parameter values within a specified, possibly overcomplete prior network. Nonnegative heat-exchange coefficients are obtained by mapping signed latent coefficients through a ReLU; negative latent values remove a connection or freeze a node. Bayesian posterior samples describe both inclusion and coefficient uncertainty. This is a concrete alternative to choosing a thermal-network topology first and calibrating it afterward. It does not establish autonomous discovery of arbitrary governing physics or a natural-circulation model.

The strongest comparisons identified by the authors are automated RC structure simplification, stochastic grey-box identification, Bayesian calibration, joint state–parameter inference, and identifiability studies (Table 1, p3; references 46, 50, 59–60, 65, 70–71, 75, 78). Those originals have not been read through this paper. S08 Bacher–Madsen is already available in the earlier queue and should be read before making novelty claims about Bayesian thermal-network selection generally.

## Models, conventions and equation audit

Reported mathematics (pp3–5, Eqs1–14): a lumped temperature state obeys

\[
C\dot T=\sum_j(T_j-T)/R_j+Q.
\]

Here C has units J/K, R K/W, Q W, T temperature and t s. Temperature differences may use kelvin or Celsius consistently in this energy equation, but the entropy argument on p4 requires absolute positive temperatures. With scales \(t_s,Q_s,\bar T\), \(\alpha_j=t_s/(R_jC)\), \(\beta=Q_st_s/(C\bar T)\), and \(\gamma_j=C/C_j\). Secondary states have symmetric exchange coefficients \(\eta_{jk}=t_s/(R_{jk}C)\), and source fractions \(a_{jl}\) initially satisfy \(\sum_j a_{jl}=1\). Eqs7/10 replace coefficients by \(S(z)=\max(0,z)\). These quantities are dimensionless rates or ratios; they are not directly conductivities, material heat capacities, or local heat-transfer coefficients.

Implementation qualifications:

- **Freezing is not zero capacitance.** Eq10 with S(gamma)=0 gives dTj/dt=0. Since gamma=C/Cj, its physical limiting interpretation is an infinite-capacitance or prescribed-temperature limit, not removal of a zero-capacitance mass. A physical zero-capacitance node instead requires an algebraic balance. Connections from a frozen node can still influence other nodes. Reproduce this distinction explicitly.
- Positivity of pairwise exchange supports dissipative heat exchange; it does not by itself prove that every inferred network has the intended physical heat-source partition. Independent switch priors do not impose the original equality of source-coefficient sums across distinct heat inputs. Section 3.3 estimates beta separately from those sums and takes an envelope of resulting intervals. Treat physical recovery as an additional consistency test.
- Eq4 describes nonnegative entropy generation for finite temperature differences. The adjacent phrase about reversible exchange should not be taken to make finite-gradient conduction reversible.
- The posterior inclusion definition on p5 writes P(S(theta)>=0). ReLU is always nonnegative, so that event is certain. The subsequent integral over positive latent theta and the ON/OFF definition clarify the intended inclusion event. Flag the notation when translating it.
- On p7 the text equates beta_jl to dTj/dQl. In Eq10 beta is a source coefficient inside a rate equation; the temperature response sensitivity also depends on capacitance ratio, dynamics and time. Do not copy the stated equality as a general sensitivity formula.

Eq11 explicitly excludes input uncertainty and latent process noise. Eq12 uses a measurement mask H and independent Gaussian observation error; it does not model a point probe as a spatially averaged fluid temperature. Eqs13–17 infer coefficients, initial temperatures and noise scale with a signed ON/OFF prior. The ODE is integrated with differentiable Tsitouras 5/4 in diffrax/JAX; NUTS uses 1,500 warm-up and 2,000 retained samples per chain (pp5–6). Coefficient bounds and scaling factors materially affect the prior and solver behavior. Source-off coefficients are held at −1 when a selected topology is evaluated (p6).

The displayed 95% predictive interval is a median plus/minus twice the square root of predictive variance plus the squared median observation-noise scale (p6). This is a Gaussian-style approximation, not direct equal-tail posterior quantiles, and is particularly limited for skewed or multimodal predictions. Input error, discrepancy outside the candidate family, and missed posterior modes remain outside that band.

## Evidence, data and validation

**Synthetic 4R3C study:** three dynamic temperatures, one boundary-temperature node, two heat sources; observe one, two or all three states. Noise is 0.33% or 3.33% of temperature scale; first 20% of time series trains, remaining 80% tests; reported forward output step 600 s (p7, Fig4). Table 3 explicitly evaluates test error against the noise-free truth, whereas training compares noisy observations. Sfull means all posterior samples under the switch prior, not a separately fitted all-connections-on baseline (p6).

The four chains settle into different modes and do not mix; pooled split-Rhat is substantially above 1 and effective sample sizes remain low (p7). Numerical tables use the first, representative chain. Thus the results are **mode-conditional**, not converged averaging over topology uncertainty. The authors acknowledge that the first-chain selected model can have very low probability relative to modes found by other chains. For scenario 1 at high noise, Table 3 (p9) gives selected-model test RMSE 1.31°C, versus 0.414°C for Sfull and 0.467°C after recalibration. This is the explicit exception to general sub-0.5°C language. Table 2 sparsity ranges 21–57% (p8).

**Physical-parameter recovery:** Eqs24 and the unnumbered formulas in §3.3 (pp9–10) convert dimensionless coefficient intervals to R,C using known power and time/temperature scales. In Table 4 (p10), only C2 among the seven finite true R,C values lies inside the displayed interval; the removed R13=∞ also matches. For example C1 interval 4.34–10.66×10^5 J/°C excludes true 3.56×10^5 J/°C; R12 interval 2.87–3.48×10^-5 °C/W excludes true 3.75×10^-5. These values were visually checked. A single example is not an interval-calibration study, and the table does not justify claiming reliable physical-parameter recovery. Summing marginal interval endpoints and taking envelopes is not generally a joint-posterior credible-interval calculation; derive transformed R,C for each joint posterior draw in any implementation.

**Four-office case:** measured indoor/outdoor temperatures and supplied heating/cooling/solar inputs; offices unoccupied, intended to approximate negligible disturbance/input uncertainty. Four observed nodes, two selected hidden nodes, an external temperature node. One chain, 60 s forward step; one training day and nine test days. Table 5 (p13) selected-network test RMSE 1.038, 1.041, 0.822, 1.033°C for the four rooms; 36% sparsity. Hidden-node alternatives were manually tried (pp11–12), so the automated search is conditional on that prior-family choice. Instrument details are delegated to reference 95 and Supplement C, not established by this paper alone.

**Two houses:** one observed indoor temperature per house, outdoor temperature, inferred HVAC heat from measured power and fitted manufacturer COP, synthetic solar irradiance, selected internal appliances; six nonphysical hidden nodes. Missing data, unmeasured gains and uncertain inputs challenge the likelihood assumptions (pp13–14). Training 75 h; 36 h test RMSE 0.55°C and 0.73°C, with 0.28°C and 0.41°C training error. Single chains; 300 s forward step; about six hours inference per house. Sparsity 55% and 60%. Longer-horizon drift is explicitly discussed (§3.6, p16). The hidden states are forecasting constructs, not identified building materials.

## TRIDENT applicability and feasible questions

**Conditional methodological transfer:** useful for comparing retained wall/fluid storage nodes, passive conductance structure and source pathways, provided transport and observation models are appropriate. **Analogy:** building predictive tests demonstrate an inference workflow, not validity for molten-salt flow, spatial extrema or MSR safety. **Incompatibility as a complete loop model:** a pure symmetric RC network omits signed directional enthalpy transport, a momentum equation, flow-dependent closures, bends and temperature-dependent fluid properties unless added explicitly.

For Codex, an implementation candidate would need a conservation-constrained thermal/transport graph, an explicit measurement operator for centerline/wall probes, a distinct circulation state, and joint propagation of input, measurement and model uncertainties. This is an appraisal and future experiment definition, not a final recommended method. Compare simple fixed physical alternatives and S08 before paying the computational cost of topology inference. Do not let hidden nodes compensate for unknown heater delivery or mislocated sensors without testing the confounding.

The paper already occupies “Bayesian discovery of uncertain thermal network structure” and documents nonidentifiability. A plausible TRIDENT contribution must be more specific: e.g. identifiable conservation-constrained transport reductions and predictive discrimination under sparse observations, with real withheld conditions and demonstrable engineering-QoI benefit. Whether that is new remains open.

## Coverage and readiness

| Coverage | Relevance | Status and limits |
|---|---|---|
| §1, Table1, pp1–3 | Positioning/prior work | Read/extracted; cited originals not implicitly read |
| §2, Eqs1–20, pp3–6 | Network, priors, likelihood, selection | Read/extracted; selected printed mathematics checked visually |
| §3.1–3.3, pp6–10 | Metrics, verification, physical parameters | Read/extracted; Tables3–4 visually checked |
| §3.4–3.5, pp10–15 | Real data and prediction limits | Read/extracted; instrumentation delegated to originals/supplement |
| §3.6–4, pp15–16 | Limits and conclusions | Read/extracted |
| Declarations/data/references, pp17–19 | Access, provenance, leads | Inspected; bibliography used for discovery |
| Separate Supplement A–D | Proof, data generation, priors, diagnostics, real-data setup | Unavailable; not read; acquisition priority 1 |
| Author code | Reproducibility | Repository tree located at commit 76ac6ecabab658a00dbf76a34abf24ae3b3dcb61; code/notebook not audited or executed |

Ready for **qualified methodological comparison and limitations synthesis**. Not ready for a faithful reproduction claim, entropy-proof assessment, full sampler-diagnostic audit, or physical-R,C implementation until supplementary coverage and code checks are complete. Publisher access was attempted; returned access-denial/403 content, not a supplement. The repository tree contains synthetic code/notebook and README, but no separate supplementary PDF.

## Claim-to-evidence ledger

| Claim ID | Evidence claim and type | Locator | Scope / confidence |
|---|---|---|---|
| S26-C01 | Signed latent/ReLU switches jointly represent coefficient and inclusion uncertainty (original method) | pp3–6, Eqs7,10–20 | Conditional on specified prior network |
| S26-C02 | Inputs exact, no process noise, iid Gaussian observations (reported assumptions) | pp4–5, Eqs11–14 | Explicit, high confidence |
| S26-C03 | Synthetic chains fail to mix; quantitative results use one chain (reported limit) | p7 §3.2; p16 §3.6 | Not full posterior model averaging |
| S26-C04 | Sparse high-noise single-observation model has test RMSE 1.31°C (original result) | p9 Table3 | Noise-free test target; exception to generic accuracy claim |
| S26-C05 | Seven finite R,C truths: only C2 inside displayed interval (audit of original table) | p10 Table4 | Table audit, not frequentist coverage estimate |
| S26-C06 | Four-office and house examples support case-specific predictive reduction (original results) | p13 Table5; p14 §3.5 | No NCL validation or universal horizon |
| S26-C07 | S(gamma)=0 freezes a node, not zero-capacitance elimination (analyst limiting-case audit) | p4 Eqs8–10; p9 Fig8 discussion | Must resolve physical interpretation before coding |
| S26-C08 | Supplement and original measurement papers needed for reproducibility (coverage finding) | p17 AppendixA/data statement; pp7,11–14 | Not yet synthesis-ready for reproduction |

## Acquire/read next

1. S26 Supplement A–D: proof, synthetic generation, exact priors/scales, multi/single-chain diagnostics, cases C/D measurement context. Upload the publisher supplementary PDF if available; the main article is already acquired.
2. S08 Bacher–Madsen (already available, not yet extracted): disciplined physical grey-box expansion and residual diagnostics; this may provide a more manageable comparator.
3. Raillon & Ghiaus (2018), DOI 10.1016/j.energy.2018.03.168; Yi et al. (2019), DOI 10.1016/j.enbuild.2019.06.012; Agbi et al. (2012), DOI 10.1109/CDC.2012.6425995: calibration/identifiability counterexamples and physical-parameter recovery. Metadata here comes from the paper bibliography; originals need verification/read before claims.
