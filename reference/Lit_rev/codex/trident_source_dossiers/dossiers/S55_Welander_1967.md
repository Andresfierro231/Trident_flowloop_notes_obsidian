# S55 — Welander (1967): transport-driven oscillatory instability

## Identity and coverage

Pierre Welander, “On the oscillatory instability of a differentially heated fluid loop,” *Journal of Fluid Mechanics* 29, 17–30. DOI: https://doi.org/10.1017/S0022112067000606. Supplied publisher PDF, 14 consecutive pages; PDF n = printed n+16. Main text, figures and references present; no appendix or supplement identified. All text inspected; PDF3–4 visually checked. Other scanned algebra was inspected as extracted text and is not a verified equation transcription.

Ready for historical/mechanism synthesis and defining assumptions for a transport model. Not ready for reproducing every neutral curve or numerical calculation without a separate algebra/code audit. Relevant original questions: A1–A4, C model/closure alternatives, F uncertainty, verification and stability.

## Problem and authors' result

A steady buoyancy–friction balance can appear restoring under a static perturbation argument, while advected temperature disturbances create delayed oscillatory amplification. The paper derives linear instability and illustrates several nonlinear responses numerically. Motivation includes general convection and geophysical analogy, rather than an MSR facility qualification (§1,PDF1–3/17–19).

Assumptions include Boussinesq density, instantaneous linear resistance, cross-sectionally uniform fluid temperature and heat flux proportional to prescribed wall temperature minus fluid temperature. Section1 warns that maintaining cross-sectional mixing in laminar flow may require an artificial diffusor (PDF2/18). Thus “laminar” does not itself justify the well-mixed one-dimensional assumption.

## Geometry, variables and equations

The general formulation allows a closed tube path, with uniform area A. \(q(t)=\int \mathbf v\cdot d\mathbf A\) is **volumetric flow**, not velocity or mass flow. The illustrative reduction uses two long vertical branches and short connections, point exchange at the lower/upper ends, and otherwise insulated branches (§2,PDF4–6/20–22).

Reported heat equation, Eq.(5), PDF4/20, visually verified:

\[
\frac{\partial T}{\partial t}+\frac qA\frac{\partial T}{\partial s}
 = k\{T_0(s)-T\}.
\]

Here \(q/A\) has velocity units and k has inverse-time units. \(T_0\) is a prescribed wall-temperature distribution. It is not the initial fluid temperature and is not a measured primary-fluid history.

The whole-loop momentum equation follows integration of Eq.(4). Linear damping coefficient R has inverse-time units in the author's normalization. Density decreases with temperature according to Eq.(3). Heater and cooler point-jump laws result from a short-exchanger limit with exchange strength held finite. They retain residence-time dependence, rather than imposing fixed watts.

Dimensionless Eqs.(9)–(12), PDF5–6/21–22 introduce buoyancy/friction parameters. Linear perturbations lead to a characteristic equation with an advective delay (§3,Eq.26,PDF8/24). These conventions must be retained if reproducing the neutral curves.

## Evidence and numerical results

Section4 identifies neutral oscillatory modes and illustrates the first stability boundary. At its limiting first-mode point the reported nondimensional values include mean temperature0.265, flow1.84 and angular frequency3.60 times mean flow (PDF10/26). These values are source-specific dimensionless results, not reactor or TRIDENT operating bounds.

Section5 uses a moving/advected-cell numerical procedure, with examples using16 or32 cells and acceleration held constant during each cell-transit increment (PDF10–13/26–29). Figure9 shows damped, periodic/pulsating and irregular reversal behavior. The author compares cell counts and acknowledges a stability-boundary shift attributable to the difference approximation. This is useful numerical sensitivity evidence, but not a modern spatial/time error budget.

The interpretation in §6,PDF13–14/29–30 links warm/cold pockets, their phase relative to flow, and changing exposure to the heaters/coolers. Too little response of flow or too little lag can weaken this particular amplification mechanism. This does not prove that all real NCL oscillations require exactly the same inertia balance.

No new independently instrumented experimental dataset or calibration/validation split is provided. Laboratory observations and private communications in the discussion must remain separate from original evidence extracted here. Irregular computed motion is not, by itself, a modern independently verified chaos diagnosis.

## Claim-to-evidence ledger

| Claim ID | Finding | Locator | Qualification |
|---|---|---|---|
| S55-C01 | Cross-sectional thermal uniformity and linear instantaneous resistance are assumptions. | §2,PDF4/20 | Not observations of TRIDENT. |
| S55-C02 | Laminar flow can require additional mixing to justify cross-sectional uniformity. | §1,PDF2/18 | Explicit applicability warning. |
| S55-C03 | q is volumetric flow and heat transfer follows a prescribed-wall-temperature relaxation law. | Eqs4–5,PDF4/20 | Visually verified; not constant heater power. |
| S55-C04 | Advected thermal perturbations lead to delayed oscillatory instability despite a restoring static argument. | §§3–4,Eq26,PDF7–10/23–26 | Mechanism within the ideal model. |
| S55-C05 | Numerical responses include damped oscillations, pulsations and irregular flow reversals. | §5,Fig9,PDF10–13/26–29 | Numerical illustrations, not new measured reversal data. |
| S55-C06 | Cell discretization shifts the calculated stability limit. | §5,PDF12–13/28–29 | Numerical sensitivity acknowledged; no full modern uncertainty estimate. |
| S55-C07 | Temperature-pocket phase and exchanger exposure explain amplification in this model. | §6,PDF13–14/29–30 | Conditional mechanism, not universal MSR behavior. |

## TRIDENT implications and skeptical appraisal

Use this source to explain why time-resolved spatial temperature structure can matter to circulation stability. A few regional RC states might reproduce settling while losing a circulating anomaly's phase. That is a hypothesis to test against observations, not a reason to choose a high-order model automatically.

Temperature measurements do not directly establish volumetric circulation, a local reversal, or cross-sectional mixing. Distinguish a predicted whole-loop circulation reversal from local recirculation; the source has one scalar flow and cannot resolve a vortex.

Source law, mixing, friction and wall assumptions differ from glycol/salt loops with finite heat capacity walls and separately controlled secondary cooling. The paper supplies no fluid property range or realistic uncertainty for those facilities. Its early date supports a history of scientific loop models; it cannot establish the earliest use of all thermosyphons.

## Coverage checklist

| Section/asset | Status | Reason/remaining work |
|---|---|---|
| §1 PDF1–3 | Inspected/extracted | Motivation and mixing caveat |
| §2 PDF3–6 | Inspected/extracted | Core equations checked visually onPDF4; full nondimensional transcription deferred |
| §3 PDF6–9 | Inspected; characteristic structure extracted | Root calculation not independently reproduced |
| §4 PDF9–10 | Inspected/extracted | Neutral-mode interpretation; full curve digitization unnecessary |
| §5 PDF10–13 | Inspected/extracted | Algorithm, behavior and discretization caveat |
| §6 PDF13–14 | Inspected/extracted | Physical mechanism and transfer limits |
| Figures/references | Text/captions inspected; selected visuals | No full numerical digitization or cited-original reading |

Next: compare the source law with S54 and finite-wall/source effects in S66. Those originals are now available; no acquisition help is needed for this comparison.
