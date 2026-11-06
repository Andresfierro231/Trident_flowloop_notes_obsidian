# S73 — Parameter estimation in stochastic grey-box models

Extraction21October2026. Niels Rode Kristensen,Henrik Madsen,Sten Bay Jørgensen,*Automatica*40(2)(2004),225–237. DOI https://doi.org/10.1016/j.automatica.2003.10.001 .13-page typeset journal copy;PDF page n→printed n+224. Title/authors/journal/DOI match. All Sections1–6,references and bios present. Text extraction has damaged glyphs (notably θ,σ,Greek symbols); selected pages2–4,9–10 rendered and PDF3/227,9/233 visually checked. Equations below are normalized notation/paraphrase with reported identifiers,not a claim of character-perfect transcription. No appendices or separate supplement supplied. Ready for scoped stochastic-inference and baseline synthesis; no software reproduction/current software-status claim.

## Problem,contribution and prior art

The authors estimate discretely,partially observed continuous-time stochastic physical models using EKF-based approximate likelihood,MLE/MAP,multiple independent runs,irregular sampling,outlier handling and missing-data selection. CTSM is compared with source-era MoCaVa/IdKit approaches. SDE grey-box modeling,EKF,robust estimation and ML/MAP are existing foundations; the article’s advance is an estimation implementation and algorithmic comparison,especially nonlinear diffusion estimation. This is strong prior art against claiming that adding process noise,filtering sparse observations or separating process and measurement noise is itself new.

## Reported model,assumptions and unit contract

§2.1,Eq1–2/PDF2/226: dxt=f(xt,ut,t,θ)dt+σ(ut,t,θ)dωt;yk=h(xk,uk,tk,θ)+ek,with ek normal mean0,covariance S(uk,tk,θ). The SDE is **Itô**. Diffusion is independent of state x; the authors cite transformations for a restricted state-dependent class rather than treating arbitrary multiplicative diffusion. State/parameter spaces,known inputs and sensor function must be specified. Standard Wiener increments scale with square-root time. Thus a temperature-state σ has units K/√s if time is seconds;σ σᵀ has K²/s,S and state/output covariances have products of state/output units. These are **our dimensional consequences**,not separately listed source units.

Measurement white-noise covariance is not interchangeable with continuous diffusion intensity. Inputs are modeled as provided histories; unmodeled input uncertainty,correlated sensor bias and heat-loss ambiguity are not automatically identified merely by fitting σ and S. Gaussian driving increments plus additive diffusion do **not** guarantee Gaussian nonlinear transition densities; the article explicitly treats Gaussian conditional densities/EKF as an approximation and calls for checks,particularly for large sample times (§2.2.1/PDF3/227).

## Likelihood,filter and implementation equations

Eq5/PDF2/226 factors p(Y|θ) into conditional time-sequential densities. Eqs6–10/PDF3/227 use innovations εk=yk−ŷk|k−1 and Rk|k−1 to construct approximate Gaussian likelihood. **Our standard rearrangement:** negative log-likelihood,up to constants,½Σk[log det Rk+εkᵀRk⁻¹εk]. This scalar uses dimensionless standardized residuals;absolute density units must be consistent across models/output dimensions. Filter innovations are one-step predictions using past observations,not autonomous long-horizon forecasts.

Eqs11–18/PDF3/227: ŷ=h(x̂),R=CP Cᵀ+S,K=PCᵀR⁻¹,then observation update and covariance update;between observations,dx̂/dt=f(x̂,u,t,θ),dP/dt=AP+PAᵀ+σσᵀ. A,C are local Jacobians. Nonlinear propagation is subsampled and locally relinearized,not assumed globally exact. Eqs19–26/PDF3–4/227–228 use matrix exponentials and diffusion-covariance integration under local linearization;input may use zero/first-order hold. Eq21 has A⁻¹;Remark3 explicitly handles singular A through a transformation,so a literal inverse is not a general implementation. For A→0,the covariance increment must approach σσᵀΔt;this is our limiting-case check,not a new source result.

MAP adds a prior term (Eqs27–32/PDF4/228);this is point optimization,not a complete posterior sampler. Eq33–36 multiplies independent-run likelihoods with separate initial conditions. Shared calibration offsets or histories can violate that independence. Eqs37–40/PDF5/229 bound-transform parameters and add a boundary penalty;this can affect boundary-near solutions and is not evidence of an identified physical prior. The source’s mapping-invariance discussion should not be generalized to a MAP density under arbitrary reparameterization without Jacobian conventions.

§2.4/PDF5–6/229–230 handles irregular timestamps through continuous propagation;robust Huber-type innovations modify the objective;missing channels are removed by a row-selection matrix so likelihood dimension and determinant change. Setting missing-channel variance to infinity is insufficient for likelihood evaluation. §2.5/Eq53/PDF6/230 uses inverse curvature for approximate parameter covariance. This is local/asymptotic and conditional on likelihood/model/regularity;poor identification,boundaries,non-Gaussianity and misspecification require additional assessment. It is not full predictive/model-form uncertainty.

## Thermal comparator and results

§4.2/PDF8–10/232–234 contains a fed-batch bioreactor and a **two-state thermal wall network**. Thermal states T1,T2;inputs outdoor Te,indoor Ti;measurement is heat flow qi=(Ti−T2)/H3+noise (un-numbered equations PDF9/233). Drift factors1/(Gi Hj) imply H are thermal **resistances**,G are capacities under a lumped heat-flow convention;these symbols must not be casually relabeled conductances. **Our dimensional interpretation:** if qi is total W,Hi K/W,Gi J/K;if qi is an areal flux,the matching area-normalized units are needed. The paper does not supply a complete wall geometry/material/area/units specification for independent conversion. Do not assign G/H to TRIDENT materials. Cross-coupling signs give passive relaxation for positive coefficients,not natural-circulation momentum/transport.

The thermal example generates719samples over718h,with/without diffusion;bioreactor101samples over3.8h,three diffusion levels. These are **simulation studies**,not measured building/loop data. Tables1–5/PDF9–10 compare single-fit parameter errors;Tables6–9/PDF11–12 vary diffusion initial guesses. “Reproducibility” here means sensitivity to optimizer starts,not independent physical replication or broad Monte Carlo bias/variance consistency. Authors explicitly say extensive Monte Carlo assessment was not performed because interactive processing was prohibitive (PDF9/233). Table5 includes sizeable thermal resistance/state errors even with CTSM;do not summarize every parameter as accurately recovered.

The nonlinear comparison favors CTSM for substantial diffusion,while linear results are closer. Baselines differ in allowed diffusion representation,current-state Jacobians,finite-difference derivatives and termination rules (§4.1,PDF7–8);this is not a controlled one-factor proof that one named algorithm always dominates. No independent physical validation partition,empirical predictive-coverage campaign or direct circulation inference appears.

## TRIDENT implications and skeptical appraisal

Applicable as an inference baseline for conservative reduced ODE states and sparse observations,subject to Itô/additive diffusion and verified time/units/initial-state treatment. Process noise can expose inadequacy but cannot by itself prove the missing physics,resolve structural nonidentifiability or measure unobserved flow. Positive heat-storage/loss parameters and conservation constraints need to come from the physical model,not a Gaussian filter. Compare deterministic covariance-aware fits with stochastic fits using common held-out runs,long-horizon predictions,innovation diagnostics and uncertainty scores;these are proposed review implications,not executed tests.

The most promising increment must involve identifiable QoIs,uncertainty separation or a transferable adequacy criterion beyond established stochastic grey-box estimation. No CTSM installation,current package recommendation or operating data processing undertaken. Cited CTSM2003 technical manual would clarify exact numerical settings if implementation proceeds;Nielsen–Madsen2001 concerns state-dependent diffusion;both are discovery leads,not read originals. Consult existing registry before assigning IDs.

| Coverage | PDF / printed | Status/reason |
|---|---|---|
| Intro/model | 1–2 /225–226 | Read/extracted;source-era scope retained |
| Likelihood/EKF/MAP | 2–4 /226–228 | Read/extracted;selected equations visually checked |
| Optimization/data/uncertainty | 5–6 /229–230 | Read/extracted;regularity/units limits |
| Software/comparison setup | 6–8 /230–232 | Read;no current software-state verification |
| Simulation/thermal example/results | 8–12 /232–236 | Read/extracted;not rerun or all table entries recalculated |
| Conclusion/references | 11–13 /235–237 | Read/discovery;bios skipped as irrelevant |
| Code/manual/supplement | External | Not acquired/read;no implementation completeness claim |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S73-C01 | Continuous-time stochastic grey-box estimation already handles partial noisy discrete observations | Eq1–2,§2.1,PDF2/226 | Itô,state-independent diffusion |
| S73-C02 | EKF likelihood is a Gaussian/local-linear approximation | §2.2.1,PDF3/227 | Check nonlinear/sampling effects |
| S73-C03 | Continuous diffusion intensity and measurement covariance are distinct | Eq1–2,12,18,PDF2–3/226–227 | Units and identifiability still required |
| S73-C04 | Multiple-run fitting assumes stochastic independence | Eq33–36,PDF4/228 | Shared systematic effects can violate it |
| S73-C05 | Missing outputs require reduced-dimension likelihood treatment | Eq44–52,PDF5–6/229–230 | Not merely infinite observation variance |
| S73-C06 | Inverse-Hessian uncertainty is local/asymptotic | §2.5/Eq53,PDF6/230 | Not full predictive or model-form coverage |
| S73-C07 | A two-state thermal wall/heat-flow example is existing grey-box prior art | §4.2,PDF9/233 | Simulated wall,not circulating loop |
| S73-C08 | Comparison uses single simulation fits and optimizer-start reproducibility | §4.2.1–2,PDF9–12/233–236 | No extensive bias/variance MC or physical holdout |
