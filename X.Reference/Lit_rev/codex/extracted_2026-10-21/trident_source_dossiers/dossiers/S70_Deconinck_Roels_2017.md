# S70 — Deconinck & Roels (2017): physical meaning of fitted thermal parameters

Extraction date: 2026-10-20. Purpose: methods/theory and contribution-boundary synthesis. **Scoped ready**, with the numerical-reference and uncertainty caveats below. Not reactor evidence; no reproduction performed.

## Identity, version and completeness

An-Heleen Deconinck and Staf Roels. *Is stochastic grey-box modelling suited for physical properties estimation of building components from on-site measurements?* Journal of Building Physics 40(5), 444–471 (2017). DOI: https://doi.org/10.1177/1744259116688384. Publisher metadata independently checked by web on 2026-10-20; the uploaded typeset article matches title, authors, DOI, venue and pagination. Publisher/version of record appearance, not an author manuscript. 28 readable PDF pages, no cover offset: **printed page = PDF page +443**. The last page is printed471, Appendix1/Figure10. No missing page, encryption or truncated main article observed. Equations and selected tables checked against rendered pages; all three appendix figures inspected visually for their qualitative relationships. No separately supplied code, data or supplement; external supporting originals were not read merely because cited here.

## Question and original contribution

The authors ask whether standard boundary-temperature and inner-face heat-flux observations identify physical wall resistance/capacity, as opposed to only reproducing input–output behavior. They examine profile likelihood, lumped parameter combinations and statistical validation across model orders and two excitation histories. Their original evidence is a **synthetic, one-dimensional, constant-property cavity-wall case**, not on-site experimental confirmation. Their principal result is that total resistance can remain stable despite non-identifiable internal coefficients, while effective capacity need not (PDF13–15/456–458, Figures5–6; PDF21–22/464–465). An identifiable internal network can still distribute its coefficients differently from the material layers (PDF21/464).

Important cited foundations: S23 Raue2009 for profiling; S08 Bacher–Madsen2011 for thermal model selection; S69 Reynders2014 for effective capacity; Kristensen–Madsen–Jørgensen2004 for stochastic estimation/structure improvement; Ramallo-González–Eames–Coley2013 for distributed-to-lumped constructions. Only our separately recorded extraction depths apply to those originals.

## Physical and observation model

Application/Case study, PDF8–10/451–453, Table1 and Figure2: south-facing insulated masonry cavity wall, Belgian Uccle climate; only heat transfer retained in HAMFEM despite that program's broader capabilities. Layers outside→inside: 0.090m brick, 0.127m insulation, 0.140m brick, 0.015m plaster. No loop fluid, momentum equation, Re/Pr/Ri range or flow instrumentation applies. Resistances are **per unit area**, m² K/W; capacitances J/(m² K), not total K/W and J/K. Input histories are external and internal **surface** temperatures; output is heat flux at the internal face. They are not bulk-air or internal-state measurements.

Synthetic generator: 200 elements/201 nodes, one-minute calculation time step over one year, averaged to hourly values for fitting (PDF9/452). This is a reported resolution, not a demonstrated grid/time-convergence study. Constant properties exclude moisture/temperature dependence. Winter indoor air set20°C; summer free-floating, no heating/cooling; selected windows10 winter days and9 summer days (PDF10/453). These are different information contents, not a controlled experiment changing one variable only. Surface temperatures inherit wall/weather dynamics.

Added white noise (PDF8–9/451–452): heat-flux measurement standard deviation5% of flux, temperature standard deviation0.25°C, plus heat-flux system-noise standard deviation1.78W/m². Hour averaging changes noise and temporal bandwidth. This does not provide a calibrated TRIDENT sensor covariance or prove a continuous diffusion coefficient. Exact random realizations and a repeat-trial coverage assessment were not supplied.

**Reference-value integrity flag:** visually verified Table1/PDF8 prints capacitances 3.57e5, 7.44e3, 2.36e5, 1.80e5 J/(m² K), but a total6.18e5. Our arithmetic sum of the printed entries is **7.8044e5**, inconsistent with that total. Resistances0.113+3.614+0.187+0.088 =4.002m²K/W, compatible with printed4.00 after rounding. Do not silently repair a layer or the total, or use this table as an implementation benchmark until reconciled. Their effective-capacity interpretation also does not equate the fitted sum with all material heat capacity.

## Mathematics and implementation checks

Reported Eq(5), PDF11/454, for i=1,…,n:

\[
dT_i=\left[\frac{T_{i-1}-T_i}{C_iR_i}+\frac{T_{i+1}-T_i}{C_iR_{i+1}}\right]dt+\sigma_i\,d\omega_i.
\]

Reported Eq(6): \(Q_{hfm}=(T_{n+1}-T_n)/R_{n+1}\). Here T0=Tse outside surface, Tn+1=Tsi inside surface. Positive reported flux runs from the inner surface toward the adjacent wall node; a loop implementation must declare its own direction. Node temperatures are effective lumped states, not established layer thermometers. Series totals are Rtot=ΣRi and Ctot=ΣCi. Rtot includes n+1 resistances; Ctot n capacitances.

Our dimensional check: RC has units seconds, drift K/s; Eq(6) gives W/m² although its symbol Q could suggest total power. If standard Wiener increments have units √s, σ has K/√s, while the prose calls σ the incremental variance. **The prose and diffusion-amplitude convention need clarification**; do not implement σ as a variance without checking the solver. Eq(6) as printed has no explicit measurement-error term, although measurement noise is described. A stochastic observation likelihood must specify that term/covariance separately. These are flags, not undocumented corrections.

Reported Eqs(1)–(4), PDF5–6/448–449: conditional likelihood, joint maximization, nuisance-reoptimized profile PL(θi), and ratio PL/Lhat. Their normalized profile statistic is −2log(PL/Lhat), with an asymptotic χ²1 threshold at95%. Profile ≠ fixed-nuisance slice ≠ Bayesian marginal. Quadratic/Hessian covariance and parameter t tests are separate local approximations (PDF7–8/450–451). Neither a finite scan nor a nonsignificant parameter alone proves structural non-identifiability; numerical bounds, multiple optima and nonregular asymptotics require scrutiny.

Our rearrangement for a deterministic implementation is Ci dTi/dt=(Ti−1−Ti)/Ri+(Ti+1−Ti)/Ri+1. Equal boundary/state temperatures produce zero deterministic flux/storage. Positive R,C give dissipative conduction with fixed boundaries; this observation does not guarantee that a learned TRIDENT model with advection is stable or physically adequate.

## Results, adequacy and uncertainty

- PDF11–13/454–456, Figure4: winter profiles leave many coefficients practically unbounded; summer supports all coefficients through order2, but not order3. Profiling and excitation-dependent identifiability are established prior art.
- PDF13–15/456–458, Figures5–6: nuisance trajectories maintain nearly constant Rtot while Ctot can vary dramatically. Appendix1 Figures8–10, PDF26–28/469–471, provides the winter analogues. This is specific evidence about their model and signals; not a theorem that every sum of resistances is identifiable.
- PDF16–17/459–460, Figure7: one-step residual diagnostics accept models whose free simulations expose missing dynamics. Both first-order models are rejected for long-term parameter characterization. The likelihood-ratio test prefers order3 while summer order2 is identifiable: best fit order is not automatically best physical-parameter order.
- Table3/PDF18/461 reports summer order2 Rtot3.7m²K/W with standard deviation0.21, Ctot2.8e5J/(m²K) with standard deviation9.3e3. These are reported **standard deviations**, not95% half-widths; model-conditional precision does not establish capacity agreement with the unresolved Table1 reference.
- Tables2–7/PDF17–20/460–463 include Hessian-based significance/correlations. The authors explicitly describe their association between nonsignificance and non-identifiability as not an established general rule (PDF20–22/463–465). Do not replace profiles with t tests.
- PDF21/464: even identifiable summer order2 does not map R/C placement onto actual wall layers. Non-identifiable nuisance coefficients can remain useful to estimate Rtot; deleting each is not automatically justified.

There is no reported locked, independent validation campaign demonstrating parameter or predictive interval coverage across new physical systems. Winter/summer diagnostics and same-data residual checks are not such a campaign. White residuals do not guarantee valid extrapolation, correct latent states or correct physical properties. No digitization of every profile point or full covariance recovery was performed. No optimization/code execution, finite-sample coverage verification or generator verification reproduced.

## TRIDENT implications and skeptical transfer

**Conditional method transfer:** choose the engineering output or parameter combination first; profile its uncertainty, reoptimizing nuisance coefficients; compare observed-data predictions with free simulations and withheld runs. Distinguish effective dynamic storage from independently anchored material ρcpV. Preserve covariance in aggregate uncertainty; do not sum marginal variances alone. Parameter or aggregate profiles are preferable evidence to an unexamined Hessian near a degeneracy, without assuming they eliminate discrepancy.

**Analogy only:** distributed-to-lumped wall storage may inform pipe/insulation reduction. The reported network has no advection, buoyancy feedback, heat exchanger or circulation reversal. No direct claim about local recirculation or an MSR follows. New heat-flux instrumentation is not assumed. If TRIDENT only has temperatures and uncertain net duty, its inverse ambiguity may be more severe.

**Contribution challenge:** identifiable aggregates, excitation-dependent identification, and nonphysical latent RC allocations are already demonstrated. A feasible candidate is to characterize which loop-specific QoIs survive boundary/observation uncertainty and what independent evidence distinguishes competing conservative models. That remains a hypothesis requiring loop-specific theory, baselines and holdouts.

## Claim-to-evidence ledger

| ID | Evidence/claim | Locator (PDF / printed) | Qualification |
|---|---|---|---|
| S70-C01 | Synthetic distributed wall, surface-temperature inputs and flux output | 8–11 /451–454;Table1,Fig2,Eq5–6 | No actual on-site validation |
| S70-C02 | Nuisance-reoptimized likelihood-ratio profiles | 5–6 /448–449;Eq1–4 | Asymptotic threshold |
| S70-C03 | Rtot can remain stable under internal non-identifiability; Ctot can fail | 13–15 /456–458;Fig5–6;26–28 /469–471 | Case-specific, aggregate not universally protected |
| S70-C04 | One-step diagnostic agreement can hide free-simulation inadequacy | 16–17 /459–460;Fig7 | Whiteness alone not predictive validation |
| S70-C05 | Identifiable RC coefficients need not correspond to physical layers | 21 /464;Discussion | Effective states remain signal/model dependent |
| S70-C06 | Nuisance coefficients may help estimate the target aggregate | 21–22 /464–465 | No automatic deletion from insignificance |
| S70-C07 | Printed Table1 capacity entries do not sum to printed total | 8 /451;Table1 | Our checked arithmetic; reference remains unresolved |
| S70-C08 | Reported summer order2 aggregate estimates/standard deviations | 18 /461;Table3 | Not95% widths or proof of physical accuracy |

## Coverage checklist

| Section/material | PDF / printed | Status and relevance |
|---|---|---|
| Identity,abstract,introduction | 1–4 /444–447 | Read/extracted; motivation and cited prior art |
| Theoretical concepts | 4–8 /447–451 | Read/extracted; likelihood, profiles, diagnostic assumptions |
| Application/case/data/model types | 8–11 /451–454 | Read/extracted; physical setup,noise,Eq5–6; key pages visually checked |
| Identifiability results | 11–15 /454–458 | Read/extracted; figures qualitatively inspected; not pointwise digitized |
| Statistical evaluation,Tables2–7 | 16–20 /459–463 | Read/extracted; Table3/4 visually enlarged; not all table entries transcribed |
| Discussion/conclusion | 20–22 /463–465 | Read/extracted; interpretation limits and nuisance parameters |
| Funding/references | 23–25 /466–468 | Inspected for provenance/discovery; cited originals not thereby read |
| Appendix1/Figures8–10 | 26–28 /469–471 | Inspected/extracted qualitatively; no exact curve values inferred |
| External code/data/supplements | Outside uploaded file | Not supplied or independently retrieved; reproduction unsupported |

Next leads: analytic distributed-to-lumped mapping (Ramallo-González2013), stochastic likelihood implementation (Kristensen2004), and original S23/S08 connections. Not immediate upload blockers; prioritize the available MSR motivation/similarity batch.
