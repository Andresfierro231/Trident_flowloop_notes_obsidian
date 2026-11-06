# S68 — Brastein, Sharma and Skeie: sensor location and identifiable thermal structure

## Identity and coverage

O.M. Brastein,R. Sharma,N.-O. Skeie, “Sensor placement and parameter identifiability in grey-box models of building thermal behaviour,” *Proceedings of SIMS2019*,Linköping Electronic Conference Proceedings170,51–58. DOI:https://doi.org/10.3384/ecp2017051.

Official publisher PDF retrieved,8 pages, PDF n=printed n+50. Printed proceedings identify2019; publisher webpage gives24Jan2020 online publication, while Crossref's date field gives24Jan2019. Preserve that date disagreement; do not infer scientific precedence from it.

All main text inspected; PDF4 and7 visually checked for model/sensor description and reduction results. All tables/captions inspected; not all numerical plots digitized. No appendix or separate supplement identified. Ready for scoped sensor/structure/identifiability synthesis; not independent numerical reproduction. Original questions B2/B4,F1/F4,H3/H5,K1/K3.

## Model, evidence and what is varied

This follows S67's R3C2 building model with indoor temperature Tb,wall temperature Tw,heater power and outdoor-temperature inputs. It compares a north-wall sensorN3 on a highly insulated wall with south-wall sensorS1 on a different wall construction (§3,Fig2,PDF4/54).

**The comparison changes both the observed physical location and wall construction.** It is not a controlled relocation experiment on one identical material state. In TRIDENT terms, changing a wall/centerline observation can change the physical meaning of an effective state as well as the information content.

Data recorded inFeb2018 at1min intervals are downsampled by taking every30th point (§3.3,PDF4–5/54–55). An anti-aliasing treatment is not specified there. Diagonal process/measurement noise parameters are estimated with the physical parameters, then the remaining analysis focuses on physical-component profiles. This choice does not automatically propagate all noise-parameter uncertainty.

The state equations correspond to S67's passive conductive network; no circulation momentum or advective transport is included. R values have K/W units,C values J/K. Sensor positions are shown diagrammatically; the detailed building dimensions were not extracted because no geometric transfer to TRIDENT is proposed.

## Identification and implementation

Profile Eq4 and pair-profile Eq6 optimize nuisance parameters while holding one/two coordinates fixed (PDF2/52). Neighbouring optimized points supply warm starts, with a reported4–10times reduction in profile computation versus the prior method (§2.1,PDF3/53). This is an algorithmic observation for this problem, not a global-optimization guarantee.

The paper uses BOBYQA and jointly estimates diagonal noise scales. It retains likelihood normalization/Hessian conventions requiring the same audit as S67: determine whether the objective is−logL or−2logL before applying thresholds or covariance factors. A profile is not a probability distribution; local ellipses need not capture a long asymmetric valley.

## Results and scientific implications

TheS1 observation provides narrower profiles for selected quantities thanN3 (§4.1,Figs6–7,PDF5–6/55–56). Rb/Rw dependence and a bound-induced kink remain. The comparison concerns model/data choices; it does not prove one universally best sensor placement.

An attempted reduction removing wall storageCw fails the authors' residual diagnostic (§4.3,PDF6–7). Another reduction removes the direct Rg branch, after which the authors report bounded profiles and similar total resistance (§4.5,Fig8,PDF7/57). **Removing a resistance branch means eliminating that heat path, not setting its resistance to zero.** Independent predictive equivalence is not established by recalibration.

Table3,PDF7/57 reports nearly constant total resistance and wall time constant across substantially different component values. The reported combinations are
\[
R_{\rm tot}=R_g\parallel(R_b+R_w),\qquad
\tau_w=C_w(R_b\parallel R_w).
\]
Units are K/W and seconds respectively. These are concrete prior examples of identifiable/useful combinations despite uncertain individual components. The three rows give Rtot=.088K/W and τw about66.5–67.0×10^3s; values were visually verified.

The reduced model's wall-capacity estimates differ substantially betweenS1/N3(Table4), consistent with a changed observed physical component. The paper's interpretation should not be generalized into a claim that more insulation alone increases material heat capacity.

As in S67, a cumulative periodogram is a serial-structure diagnostic, not a standalone normality test. Passing calibration residual checks does not certify future predictive intervals. Correlated profile contours are not by themselves proof of structural non-identifiability or statistical independence when they look elliptical.

## Claim-to-evidence table

| ID | Finding | Locator | Limit |
|---|---|---|---|
| S68-C01 | Sensor comparison also changes wall construction and observed physical component. | §3,Fig2,PDF4–5/54–55 | Placement/material effects are not isolated. |
| S68-C02 | Warm-started pair-profile calculations reduce reported computation. | §2.1,PDF3/53 | Local/implementation-specific result, not guaranteed global coverage. |
| S68-C03 | Sensor choice changes selected parameter profiles and reveals bound-related dependence. | §§4.1–4.2,Figs6–7,PDF5–6 | A calibration/inference result, not universal sensor ranking. |
| S68-C04 | One proposed storage reduction fails residual assessment; removing a loss branch is retained after refitting. | §§4.3/4.5,PDF6–7 | No unchanged independent holdout demonstrated. |
| S68-C05 | Total resistance/time-scale combinations remain stable across different fitted components. | §4.4,Table3,PDF7/57 | Direct prior art for grouped inference; no material-property proof. |
| S68-C06 | Observation choice, model structure and identifiability are already treated jointly. | §5,PDF8/58;§§3–4 | TRIDENT novelty must go beyond combining these ingredients. |

## Coverage checklist and next action

| Asset | Coverage | Remaining work |
|---|---|---|
| §§1–2 PDF1–3 | Inspected/extracted | Threshold/Hessian normalization not reconciled with code |
| §3 PDF3–5 | Inspected/extracted;PDF4 visual | All building dimensions/sensor metrology not transcribed |
| §4 PDF5–7 | Inspected/extracted;PDF7 visual | No optimization/holdout reproduction |
| §5/references PDF8 | Inspected | Cited originals not thereby read |

Use the paper to challenge a proposed “sensor-aware identifiable thermal network” contribution and to define appropriate grouped-parameter baselines. No upload needed for S68.
