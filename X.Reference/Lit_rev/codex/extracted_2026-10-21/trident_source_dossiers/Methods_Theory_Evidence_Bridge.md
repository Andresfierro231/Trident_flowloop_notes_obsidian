> **New evidence update:** S10 and S48 now have scoped full-document dossiers, and original Nick Phase0–4 protocols are available. Read [New_Batch_Synthesis_2026-10-20.md](New_Batch_Synthesis_2026-10-20.md) and [Nick_Plan_Reconciliation_2026-10-20.md](Nick_Plan_Reconciliation_2026-10-20.md) before using earlier acquisition/protocol assumptions. The main change requests now address explicit scale, graph and observation/assessment issues. The current acquisition queue requests S50/S51, not S10/S48 or the protocols.

# Methods and theory evidence bridge — scoped primary readings

2026-10-20. This complements the facility dossiers. It is a **selected-section extraction**, not full-paper certification. Methods stated below are established prior work; proposed TRIDENT extensions appear in the P0 memo. No numerical success rates from unread examples are imported.

## S08 — Bacher and Madsen, thermal grey-box selection

Verified citation: Peder Bacher and Henrik Madsen (2011), “Identifying suitable models for the heat dynamics of buildings,” *Energy and Buildings*, DOI[10.1016/j.enbuild.2011.02.005](https://doi.org/10.1016/j.enbuild.2011.02.005). Retrieved DTU manuscript has25 PDF pages including a repository cover. Printed manuscript page=PDF−1 from PDF4/printed3 onward; the manuscript title page is unnumbered. It is not publisher pagination.

Inspected: title, introduction, §§2–4, model components and §§5.5–7 (PDF2,4–8,13,19–22); relevant tables/equations text. Not fully extracted: experiment details/plots PDF9–12,14–18, full network appendix PDF23–25. Figures were not independently digitized. **Ready for selection/observation precedent; not a replicated model.**

The source combines thermal RC states, measured heat/climate inputs, process-noise Wiener terms and discrete measurement noise (Eqs.1–3, PDF5/4). It fits by maximum likelihood using a Kalman-filter likelihood under linear/Gaussian assumptions (§2.1, PDF5–6/4–5), expands candidate networks and uses likelihood-ratio tests plus residual and physical-parameter checks (§§3–4, PDF6–8/5–7). Sensor, heater, envelope and interior-medium states are explicit options (PDF13/12). Thus thermal network discovery, progressive enrichment and sensor dynamics are established, not TRIDENT novelty.

Table3/PDF20/19 explicitly warns that physical parameter interpretation changes with the chosen model; similar aggregate properties need not make individual fitted capacities physical. The selected model is evaluated with in-sample residual statistics; this is not the same as a final independent regime-out prediction test. A TRIDENT extension should add circulation/advection where needed and assess independent QoIs. Do not automatically apply the source's5% likelihood-ratio rule to boundary-constrained nonnested models or many sequential comparisons; regularity and multiplicity must be checked.

Claim M-S08-01: model enrichment/selection has strong prior precedent (§4/Fig.2).
Claim M-S08-02: fitted thermal capacities can change interpretation with topology (Table3 and §5.5.2).

## S06 — Brynjarsdóttir and O’Hagan, calibration/discrepancy

2014, “Learning about physical parameters: the importance of model discrepancy,” *Inverse Problems*30,114007; DOI[10.1088/0266-5611/30/11/114007](https://doi.org/10.1088/0266-5611/30/11/114007). Author manuscript32 PDF pages, printed manuscript=PDF page. Inspected §§2,4.1–4.2 opening and discussion/conclusions PDF4–5,15–17,23–25; earlier example/figures were covered only in the existing selected-pass ledger. Full example calculation and MCMC appendices remain unextracted. **Ready for the confounding argument, not a reproduced Bayesian analysis.**

Source model Eqs.1–3/PDF4:
\[
z_i=\eta(x_i,\theta)+\delta(x_i)+\epsilon_i.
\]

Here x are known control inputs, θ calibration parameters, δ discrepancy, ε observation noise. The source distinguishes physical parameters from tuning parameters (§2.2/PDF5). Its general argument shows that increasing data under a misspecified calibration can concentrate around a biased best fit (§4.1/PDF15–16). Allowing arbitrary discrepancy also leaves θ/δ confounded: many combinations reproduce the same reality (§4.2, Eq.17/PDF17). Informative, defensible discrepancy restrictions or independent physics/data are needed; merely adding a GP does not identify material parameters. Known controls in the source are an assumption that must be expanded for uncertain TRIDENT boundaries.

Claim M-S06-01: predictive fit and physical identification are distinct (Eqs.3,16–17).
Claim M-S06-02: unconstrained discrepancy can hide parameter/physics deficiencies (§4.2/discussion).

## S04 — Bayesian operator inference

Mengwu Guo, Shane A. McQuarrie, Karen E. Willcox (2022), DOI[10.1016/j.cma.2022.115336](https://doi.org/10.1016/j.cma.2022.115336). Author-hosted22-page manuscript retrieved from the source registry URL. Title/authors/model identity match; typesetting differs from journal version, whose page-by-page text was not compared. Manuscript printed page=PDF. Inspected §§2–4, conclusion and Appendix1 (PDF3–9,18–19); selected Fig.10–11 captions/PDF17. Full numerical examples/Appendix2 not extracted. **Ready for data-requirement and UQ-scope assessment; numerical performance not cleared.**

Source Eq.2.2/PDF3 uses a reduced polynomial ODE:
\[
\dot{\hat q}=\hat A\hat q+\hat H(\hat q\otimes\hat q)+\hat B u+\hat c.
\]

State snapshots are projected into a basis; reduced derivatives are estimated. Eq.3.1/PDF4 models regression residuals as independent Gaussian; Eqs.3.4–3.7/PDF5 yield operator posteriors, with empirical-Bayes hyperparameters. Posterior operator draws are integrated through the nonlinear ROM (Algorithm1/PDF7). Appendix1/PDF18–19 explicitly supplies a correlated GP-residual alternative: the method is not limited in principle to iid residuals.

The regression conditions on a constructed data matrix and chosen basis; it does not by itself propagate every uncertainty in noisy regressors, calibration, boundary data, the basis or CFD truth. The conclusion/PDF18 expressly warns that posterior-drawn models can be unstable even with regularization. A Gaussian operator posterior does not automatically preserve conservation, capacities or thermal admissibility. Sparse TRIDENT thermometry does not directly supply full fields/basis coordinates; identifying a latent reduced state is an additional problem.

Claim M-S04-01: BayesOpInf already propagates inferred-operator variability (§3/Algorithm1).
Claim M-S04-02: field/derivative requirements and posterior stability limit direct transfer (§2,§4,conclusion).

## S05 — NEMO, conditional linear inversion

Julie V. Pham, Thomas O’Leary-Roseberry, Omar Ghattas, Karen E. Willcox, arXiv[2608.24833v1](https://arxiv.org/abs/2608.24833v1),25 August2026. Retrieved34-page version matches the v1 identifier and title; no journal publication is assumed. Printed page=PDF. Inspected §§2.1–2.3/PDF3–7 and limitations/PDF17. Application tests, proofs AppendicesA–D and speedup claims were not fully appraised. **Ready to decide structural suitability; not a reproduced or endorsed TRIDENT method.**

The source assumes \(A(m)u=Cq\), a linear observation \(d=F(m)q+\epsilon\), externally characterized m and additive Gaussian noise with known positive-definite Γ (Eqs.1–4/PDF3–4). It learns \(m\mapsto F(m)\Phi_r\), rather than a generic nonlinear inverse, and solves a regularized reduced linear system (Eqs.10–11/PDF6). Eq.14/PDF7 gives conditional Gaussian posterior covariance in that reduced subspace. The limitations/PDF17 explicitly defer analysis of errors in m.

For a thermal loop, unknown initial fields or heat-source amplitudes might enter linearly **only after** fixing suitable transport/operators. Unknown G,C, circulation, properties and nonlinear source/boundary effects generally change the forward operator. They cannot all be relabeled q while retaining the closed form. NEMO remains a later conditional-inversion comparator if training/operator data and a real amortization need exist. Its covariance is not a complete model-discrepancy budget.

Claim M-S05-01: linear/nonlinear unknown partition is a prerequisite (Eqs.1–4).
Claim M-S05-02: reduced conditional covariance does not quantify uncharacterized m/model error (Eq.14,PDF17).

## S12 — engineering-motivation anchor, restricted scope

David E. Holcomb, Alexander J. Huning, Michael D. Muhlheim, Richard S. Denning, George F. Flanagan, *Molten Salt Reactor Fundamental Safety Function PIRT*, ORNL/TM-2021/2176,September2021.129-page official PDF. Main printed page=PDF−11; AppendixB worksheets have their own printed labels and inconsistent repeated numbering, so always retain PDF page.

Inspected title, abstract/objectives (PDF3,12,16), selected background (PDF15), summary/conclusions (PDF65–67/54–56), worksheetII01 (PDF119–120/B-32–33). Other scenarios/appendix rankings remain unread in depth. **Ready for heat-removal motivation and scope distinctions; not a complete ranking synthesis.**

The PIRT addresses liquid-fueled MSRs, emphasizing accident progression including breached barriers/spills; it lists heat removal among three fundamental safety functions (§2.2/Table1,PDF16/5). Summary conclusions emphasize design-dependent decay-heat rejection and substantial spill-related unknowns (PDF65–67). Those gaps do not automatically become TRIDENT single-phase-loop gaps. WorksheetII01 connects power, heat rejection and heat capacity with overtemperature/barrier challenges; it also identifies precursor-transport physics outside a nonnuclear loop's capability.

Claim M-S12-01: heat rejection is a reactor-engineering need, but the PIRT's gap ranking has a broader, different scope (Table1;§5;II01).

## S44 — distributed heating and CFD boundary sensitivity

Battistini et al. (2021), DOI[10.1016/j.ces.2021.116520](https://doi.org/10.1016/j.ces.2021.116520). Institutional published-version copy14 pages including cover; article printed=PDF−1. Inspected abstract, introduction selections, facility/numerical formulation and conclusion (PDF2–6,13; selected results/captions PDF11–12). Mesh/time/statistics tables and all result details remain unextracted; no numerical reproduction. **Ready as a challenge to broad novelty and a CFD-contract warning; not a validated closure source.**

The source models fluid and solid domains, with distributed electric heating deposited **in pipe walls** (abstract/§§2–3). Distributed external heating emulates aspects of distributed reactor sources; it is not volumetric fission heating. Its conclusion/PDF13/12 reports different stability outcomes when a closed approximation is replaced by an open boundary plus filling-tank representation. It explicitly places validation of DYNASTY's quantitative stability boundary in future work, along with additional thermal mesh sensitivity. Thus reproducing a previous computed unstable transient is not independent experimental validation. Countercurrent flow and conjugate temperature effects already appear in this prior CFD work, further narrowing proposed novelty.

Claim M-S44-01: source placement, wall storage and tank/outlet representation can change the relevant dynamics (facility description/conclusion).
Claim M-S44-02: the paper does not supply completed experimental validation of the stability boundary (conclusion).

## Next methods reading

S23 profile-likelihood identifiability; S07 Bayesian experiment design; S24 stable quadratic dynamics; S25 goal-oriented reduction; S18 conjugate1D model; S14/S15 similarity and distortion; S45 developing mixed convection. Availability and reading status remain separate in the registry. Port-Hamiltonian/advection-network transfer, probabilistic score selection, modular multi-fidelity calibration and rigorous bounds for unobserved extrema need additional primary-method extraction before claiming theory coverage.
