# S75 — Validating predictions of unobserved quantities

Todd A.Oliver,Gabriel Terejanu,Christopher S.Simmons,Robert D.Moser. Journal citation:CMAME283(2015),1310–1335,DOI https://doi.org/10.1016/j.cma.2014.08.023 . **Inspected:**43-page arXiv1404.7555v1 manuscript,submission29April2014;PDF first-page compilation line says25September2018. Both stamps retained;no explanation or final-journal equivalence assumed. PDF=manuscript page2–43 where numbered;no journal-page mapping. Extracted21October2026.

## Integrity and purpose

Title/fourauthors/relatedDOI agree with primary arXiv record. Sections1–5,Tables1–2,Figures1–8,AppendixA and references present. Relevant main text1–41 andAppendixA read;references42–43 discovery-inspected,not independently read originals. PDF12/19/41rendered;PDF19HPRDdefinition visually checked. No code or external supplement acquired. Ready for scoped predictive-validation/discrepancy/novelty synthesis,not a guaranteed error estimator or physical-loop validation.

## Established methodology and reported mathematics

The paper distinguishes a reliable governing backbone from less reliable embedded constitutive/closure/boundary models. It embeds discrepancy at the source so the same correction propagates through the state to observations **and** unobservedQoIs. Equations1–4/PDF9–10: R(u,τ;r)=0,τ≈τm(u;s,θ),y=Y(u,τ;r),q=Q(u,τ;r). Scenario variables r for the full system need not equal embedded-model conditions s. Equations8a–c/PDF12 insert τm+εm into governing residual,observation andtarget maps. Equations13–18/PDF15 generalize multiple embedded models,experiment-specific nuisance models and consistent state-to-closure mappings.

These abstract symbols have no universal physical units. In athermal implementation,a corrected heat rate must beW,a resistanceK/W,and a pressure lossPa. **Our transfer requirement:**use the same uncertain internal heat rate with opposite signs in adjacent energy balances;an unconstrained output correction or arbitrary additive closure can violate conservation/positivity. The source offers a framework,not these TRIDENT-specific constraints or a unique discrepancy family.

Eq19–20/PDF17 gives a Bayesian joint posterior for physical θ and inadequacy hyperparameters α. Calibration,observation plausibility and predictive assessment are distinct (§3/PDF16–23). Eq21/PDF19 uses a highest-posterior-relative-density credibility metric:γ=1−integral of predictive density over points with density/reference-density ratio at least that at the observed datum. Reference q is required;this is not merely a±2σtest. It is intended to avoid ordinary HPD's dependence on variable transformation if reference measure is transformed consistently. A plausible observation under that metric does not by itself validate a futureQoI;it also does not enforce decision-useful sharpness.

## Necessary evidence and limitations

§3.3/PDF19–23 asks whether the QoI depends on parameters,embedded models or inadequacy features that calibration/validation did not constrain,and whether the embedded models are used outside tested applicability domains. A global scenario change may be acceptable if relevant local embedded conditions remain supported. This is a conditional physics/evidence argument,not arbitrary empirical extrapolation. The method assumes reliable backbone/theory/observation maps and verified numerics (§1/PDF3). Unknown omitted phenomena can escape its assessment (§3.3.3/PDF23). The authors explicitly give no universal sufficiency prescription for all systems.

Source-era statements about absence of established methods are historical claims,not evidence that a gap remains vacant in2026. S76 directly develops a later validation-design approach,and S72 is later calibration work. Merely embedding stochastic closure error or checking sensitivities is therefore established prior art.

## Demonstration and assessment independence

§4/PDF23–38 uses synthetic spring–mass–damper data,not physical experiments. A linear spring/damper model predicts maximal velocity for massm=5;data positions for m=1calibrate andm=2initially challenge. Three assumed information states distinguish no inadequacy,unexplained inadequacy and mechanism-informed damping variability. Narrow parameter posteriors in the first state still fail observation plausibility. Knowing only that residuals exist does not justify extrapolation. Mechanism-informed variability supports a conservative example prediction.

The second dataset is subsequently separately recalibrated to challenge the hypothesized change in damping spread (PDF36–37). That is informative additional model assessment,not an untouched final test after all development. The disclosed truth at m=5is a synthetic demonstration rather than a general coverage theorem. The example likelihood draws a damping coefficient independently for each datum before multiplying likelihood contributions (§4.2/PDF28);that is an ensemble observation model,not a single thermally coupled damping trajectory or a continuous process-noiseSDE. Do not transplant it into correlated loop histories as independent residual sampling.

AppendixA/PDF41 specifies an additional damper-temperatureODE with c(T)=exp(T0/T−1),coupled to dissipated mechanical energy and ambient relaxation. Numerical physical units/capacity normalization are not fully declared;the thermal equation cannot be copied as a dimensional heat balance without a capacity/normalization contract. The example noise is stated as standard deviation.01 onPDF26–27 but later normal notation onPDF29is inconsistent with the earlier variance convention. No numerical reproduction attempted. Qualitative predictive-validation distinctions do not depend on resolving that notation.

## Consequence for TRIDENT

This directly closes the claim that unobserved-QoI discrepancy has no prior treatment. It supplies a credible alternative to output-onlyGPcorrection,but requires informed/tested closure-errorstructure,applicability and observations that constrain target-relevant directions. Sparse temperatures may leave those directions unsupported;embedding a correction does not create measurement information. A feasible core should first assess thermal/duty/response outputs. Unobserved extrema/local extent remain conditional hypotheses or supported bounds,not experimentally certified fields.

| Coverage | PDF | Status |
|---|---|---|
| Motivation/framework | 1–16 | Read/extracted;prior work distinguished |
| Calibration/validation/predictive assessment | 16–23 | Read/extracted;HPRDchecked |
| Synthetic example | 23–38 | Read/mapped;not numerically reproduced |
| Conclusions | 38–41 | Read;source-era future work not certified2026gaps |
| AppendixA | 41 | Read;dimensional/normalization limitations |
| References/externalassets | 42–43/external | References discovery-inspected;code/supplement not acquired |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S75-C01 | Embedded discrepancy can propagate through state to both observations and unobservedQoIs | Eq8a–c,PDF12 | Requires a valid,informed correction model |
| S75-C02 | Calibration,validation and predictive assessment answer distinct questions | §3,PDF16–23 | No generic sufficiency certificate |
| S75-C03 | Target-relevant untested directions and closure applicability determine credibility | §3.3.1–2,PDF20–22 | Depends on physical/modelknowledge |
| S75-C04 | Unknown omitted mechanisms can evade predictive assessment | §3.3.3/PDF23 | Framework does not eliminate unknownunknowns |
| S75-C05 | HPRDobservation plausibility is distinct from predictive adequacy/useful precision | Eq21/PDF19;§3.3/PDF20,23 | Not empiricalcoverage or decisiontolerance |
| S75-C06 | Demonstration uses synthetic oscillator data and information-state assumptions | §4/PDF23–38 | Not loopvalidation or universalmethodguarantee |
| S75-C07 | Example likelihood independently draws damping per observation | §4.2/PDF28 | Ensembleconstruction,not correlated thermal trajectory |
| S75-C08 | Second mass dataset is separately recalibrated during hypothesis assessment | PDF36–37,Fig6–7 | Not untouched finalholdout after all modeldevelopment |
| S75-C09 | Sourceversion has2014arXivstamp and2018compilationline | Firstpage | Finaljournal equivalence unverified |
