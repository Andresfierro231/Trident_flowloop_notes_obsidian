# Implementation equation and validation contract

21 October 2026. Consolidated v1.0. Canonical context and staged comparison: review A §§1–11. These equations distinguish source mathematics from our proposed derivations. Source-reading clearance is not executed implementation verification.

## 12. Equation and convention catalogue for implementation review

The catalogue retains scientific provenance and separates source equations from our conventional formulations. It is a starting specification, not a claim that all source solver details have been reconstructed. The companion `Implementation_Equation_and_Validation_Contract.md` records source ambiguities; the table below is canonical for this first review draft.

| Catalogue ID | Equation or operation | Definitions, units and checks | Provenance / limit |
|---|---|---|---|
| EQ-01 | Stored-energy balance with shared signed face/exchange rates | U J, rates W; sum internal rates to zero | Our conservative formulation; S52 Eqs7–23/PDF5–7 supplies related prior model |
| EQ-02 | Positive thermal network C_i dT_i/dt=Q_i+ΣG_ij(T_j−T_i)−loss_i | C J/K, G W/K; paired exchange; effective versus material meaning | Our notation; S26 Eqs1–14/PDF3–5; S66 Eqs1–6/PDF3–4 |
| EQ-03 | Signed circulation inertia/buoyancy/resistance balance | mdot kg/s; f_D versus f_F; K and area definitions; all pressure terms Pa | Our stated approximation; S52/S19/S29 are conditional source comparators |
| EQ-04 | Observation y=H[x, u;η]+b+e | Location/average/response/clock; bias dependence | Proposed contract; S32 §6/PDF13–15/5–7; S73 Eq2/PDF2/226 |
| EQ-05 | Single-state energy scale and τ=C/G | Known net duty or capacity anchor; residual duty/initial-state assumptions | Our elementary derivation; not a novelty claim |
| EQ-06 | Ratio covariance for mdot=Q/Δh | Q W,Δh J/kg; ill-conditioned near zero | Our local derivation; S29 Eq3/PDF9 provides inference example |
| EQ-07 | h(T)−h(T*)=∫cp(T)dT; Qrad=εσA(Tw⁴−Tsur⁴) | cp J/(kgK), h J/kg; radiation temperatures K | Conventional proposed implementation; source/view-factor and property validity required |
| EQ-08 | SDE dx=fdt+σdW; yk=h(xk)+ek | Itô;σ state/√time; measurement covariance observation² | Reported S73 Eq1–2/PDF2/226; state-independent diffusion |
| EQ-09 | Pdot=AP+PAᵀ+σσᵀ; R=CP Cᵀ+S | Local Jacobians, substeps, initial covariance; singular-A handling | Reported S73 Eq12/18–26/PDF3–4/227–228; Gaussian/local approximation |
| EQ-10 | −logL=½Σ[logdetR+innovationᵀR⁻¹innovation]+constants | Missing channels reduce likelihood dimension; prior/MAP normalization declared | Our Gaussian rearrangement; S73 Eq6–10/44–52/PDF3,5–6 |
| EQ-11 | Uy=J Ux Jᵀ; Cy Uy Cyᵀ=Cx Ux Cxᵀ | Local linear explicit/implicit covariance; avoid unstable literal inverses | Reported S31 Eq3/8–10, PDF23/25, printed15/17 |
| EQ-12 | Joint-sample propagation X^(r)→f(X^(r)) | Reuse common variables; numerical tail/endpoint tolerance | Reported S02 Fig4/PDF23/15; §7.9.4/PDF40/32 |
| EQ-13 | Embedded discrepancy R(u,τm+εm; r)=0 with common observation/target maps | Correction units and physical constraints; tested closure domain | Reported S75 Eq8a–c/PDF12; does not guarantee identifiability |
| EQ-14 | U(d)=E_y KL[p(z\mid y,d) ∥ p(z)] | Dimensionless nats; fixed target definition, prior/likelihood and joint dependencies | Reported S71 Eqs10–14/PDF5, arXiv v2; estimator error assessed |
| EQ-15 | Mh=E[∇h∇hᵀ]; scenario/normalized-observation matrix matching | Parameter nondimensionalization; positive trace; regular functionals | Reported S76 Eq14–17/PDF13–15; relevance criterion, not error bound |
| EQ-16 | Profile likelihood reoptimizes nuisance quantities | Objective factor−logL versus−2logL; bounds/multistart; not marginalization | S23 Eq10/PDF4/1926; S67/S68/S70 comparators |

No literal production transcription is cleared for flagged source equations: S19 energy definition/sign and grid ratio; S72 likelihood direction, covariance prefactor and validation-RMSE normalization; S73 damaged extracted symbols and wall area/units; S29 pressure-current units, loss formulation and plot/flow provenance; S74 source/solid normalization and hydraulic diameter; S75 manuscript date/noise/thermal normalization; S76 derivative/coordinate conventions. A flag identifies ambiguity, not a proved bug in the authors' executed code.


Before implementation freeze control volumes, energy reference, sign/averaging conventions, property basis, source deposition, observation map, covariance and calibration/assessment split. Preserve existing M1/M2/M3 meanings. No operating data or model code was processed in this pass.
