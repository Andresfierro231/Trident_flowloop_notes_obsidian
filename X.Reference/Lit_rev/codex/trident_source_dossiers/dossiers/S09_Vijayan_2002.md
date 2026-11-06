# S09 Vijayan 2002 scaling and stability

## Identity, file and readiness

P. K. Vijayan (2002), *Experimental observations on the general trends of the steady state and stability behaviour of single-phase natural circulation loops*, Nuclear Engineering and Design 215, 139–152. DOI https://doi.org/10.1016/S0029-5493(02)00047-X. Complete 14-page typeset article, printed page = PDF page +138. All sections, Appendix A and references read. Equations are legible in the PDF although text extraction corrupts Greek characters; consequential Eqs. (1)–(28) checked against rendered PDF pp. 3–5. Figures 1–8 present; curve-point data not digitized. No separate supplement/raw datasets supplied.

**Ready for:** qualified scaling/motivation synthesis and selection of analytical verification cases. **Not ready for:** copying the printed transient reduction without resolving the algebraic issue below, or asserting quantitative applicability to TRIDENT. This is principally a theoretical extension plus comparison with previously reported experiments; the many cited experimental originals were not thereby independently read.

## Problem, findings and historical role

Sections 1–2, PDF pp. 1–2/printed 139–140: seeks non-loop-specific groups to compare experiments and prototypes; extends prior uniform-diameter work S36 to non-uniform diameters. Constant-temperature-source and constant-flux-source problems have different information contracts: prescribed source ΔT is unavailable when heating power is the independent input. This is directly relevant to TRIDENT's forward contract.

The history in the introduction spans reactor cooling, transformer and solar cooling, geothermal extraction, corrosion loops and dynamical-systems experiments. Thus the apparatus class is not intrinsically an MSR surrogate. Section 4 names LWR/PHWR-oriented integral facilities and simple loops; its scaling is generic single-phase theory, not a demonstrated salt-reactor correspondence. Hamilton et al. 1954, Keller 1966, Welander 1967 and later scaling studies are **cited historical leads**, not primary histories read through this article.

Original contribution here: non-uniform-diameter dimensionless formulation, geometric resistance parameter N_G, steady limiting laws and a comparative appraisal of published data/stability behavior. Evidence is not an uncertainty-calibrated universal correlation across all fluids, geometries and local thermal mechanisms.

## Physical definition and assumptions

Section 3/Fig. 1, PDF pp. 2–3/140–141: ideal rectangular loop with horizontal constant-flux heater, cooler modeled by overall U to a secondary temperature T_s, and insulated connecting pipes. 1-D incompressible Boussinesq fluid; constant properties except linear buoyancy density, negligible axial conduction and viscous dissipation. Wall heat storage is absent from these basic energy equations. Reference density ρ₀ kg/m³; μ Pa·s; c_p J/(kg K); β K⁻¹; W is **mass flow kg/s**, not power. q_h is flux W/m² and Q_h is total power W. s runs around the loop, z is elevation. Dimensional lengths/areas/diameters have overbars in the paper; normalized quantities do not. No single operating/fluid range describes the collection of cited facilities. Do not present a heterogeneous literature plot as a characterized TRIDENT envelope.

## Audited equations and limits

| Equation ID | Reported relation and locator | Audit/use |
|---|---|---|
| S09-E01 | ∂W/∂s=0; Eq. (1), PDF 3/141 | One loop-wide circulation state for incompressible 1-D model; cannot describe simultaneous cross-sectional counterflow. |
| S09-E02 | γ_bar dW/dt = ρ₀gβ∮T dz − W²/(2ρ₀) Σ_i[(f_i L_i/D_i +K_i)/A_i²], γ_bar=Σ_i L_i/A_i. Eqs. (2),(4), PDF 3/141 | Both sides Pa. γ_bar has m⁻¹. f is Darcy (Appendix A). Printed positive-flow branch uses W²; an analyst extension to reversals needs a signed resistance formulation, not silent reuse. Reference constant T cancels around a closed loop. |
| S09-E03 | T_t+[W/(ρ₀A_h)]T_s=q_hP_h/(ρ₀c_pA_h); connecting-pipe RHS=0; cooler RHS=−UP_c(T−T_s)/(ρ₀c_pA_c). Eqs. (3a–c), PDF 3/141 | K/s; s derivative is coordinate, while T_s in cooler expression is secondary temperature. Clarify notation before coding. Cooler sink assumes specified secondary temperature/U, not the full TRIDENT jacket. |
| S09-E04 | K_i=f_i L_ei/D_i, Eq. (5), PDF 3/141 | Equivalent-loss length is not a measured physical length. If f varies with Re while K is fixed, L_e varies too; a purely geometric N_G needs a consistent assumption about this dependence. |
| S09-E05 | A_r=V_t/L_t; D_r=ΣD_i L_i/L_t; t_r=ρ₀V_t/W_ss. Eq. (8), PDF 3/141 | A_r and D_r are separate length averages; do not assume A_r=πD_r²/4 for a non-uniform loop. t_r seconds. |
| S09-E06 | ΔT_r=Q_h H/(A_r μ c_p); Gr_m=D_r³ρ₀²βgΔT_r/μ²; Re_ss=D_r W_ss/(A_r μ); Pr=c_p μ/k; St=Nu/(Re_ss Pr), Nu=UD_r/k. Eq. (12), PDF 4/142 | All groups dimensionless; ΔT_r is an imposed-power reference scale, not measured hot–cold ΔT. St uses **overall U**. |
| S09-E07 | N_G=(L_t/D_r)Σ_i[l_eff,i/(D_i*^(1+b) A_i*^(2−b))]; Eq. (15), PDF 4/142 | Stars added here solely to distinguish normalized D_i/A_i; this is notation clarification, not a new equation. l_eff is effective segment length divided by L_t. Assumes one friction exponent b across segments. |
| S09-E08 | Re_ss=[2Gr_m/(p N_G)]^(1/(3−b)); f=p/Re^b. Eqs. (13),(24)–(28), PDF 4–5/142–143 | Under the ideal steady geometry ∮θdZ=1. Laminar p=64,b=1 gives 0.1768(Gr_m/N_G)^0.5; Blasius p=0.316,b=0.25 gives 1.96(Gr_m/N_G)^(1/2.75). Independent arithmetic gives 0.1767767 and 1.9561287. Exact **within the stated model**, not exact reactor predictions. |
| S09-E09 | Stability/transient groups Gr_m^[b/(3−b)]/N_G^[3/(3−b)], St_m plus geometry; St_m=St P_c L_t/A_c. Eqs. (29)–(31); Appendix A; PDF 5–6,13/143–144,151 | Matching the steady ratio Gr_m/N_G is insufficient. Heater/cooler length scales, area ratios and geometry must also be retained. |

**Algebraic ambiguity:** substitution of Eq. (24) into Eq. (14) appears to retain a factor L_t/H on the RHS of Eq. (29), absent from its printed form. Analyst derivation: γ dω/dτ = (L_t/H)(p/2)^[3/(3−b)] {∮θdZ−ω^(2−b)}/[Gr_m^[b/(3−b)]/N_G^[3/(3−b)]]. This follows from Eq. (14), under its definitions, and is **not a claimed author correction**. Resolve against the original derivation/other versions before transient implementation. In the uniform-diameter limit γ=L_t/H, the factor cancels consistently with S36's uniform-loop equation. Qualitative similarity arguments with fixed geometry do not depend on adopting a silently altered equation.

## Results, verification and uncertainty

Section 4.1/Figs. 2–6, PDF 7–10/145–148: laminar data generally follow the theoretical curve; turbulent uniform-loop data depart when local losses are neglected. Non-uniform loops dominated by distributed resistance fare better. This is not evidence that minor losses are universally negligible: the paper explicitly attributes important deviations to their omission. Near mixed-regime conditions (discussion PDF 10/148 gives 1000<Re<4000), one law across the loop is not strictly applicable. Area-reducing equivalent parallel paths require identical channels with same-direction flow; metastable channel reversals invalidate that replacement.

Section 4.2, PDF 10–12/148–150 separates rest-state stability, multiple-equilibrium/metastability and growing oscillations/reversals. Wall heat conduction/storage is explicitly required for quantitative transient predictions even if ambient losses vanish (4.2.3, PDF 11/149). Linear stability predicts small-perturbation growth, not arbitrary large perturbations or a universal safe operating boundary. The paper's statement that a particular instability is not observed in reactors refers to the discussed length/diameter regime; it must not become “MSRs cannot be unstable.” Its St_m≈9.7 threshold (PDF 12/150) belongs to the illustrated geometries/model, not a transferable design limit.

No common metrology/covariance budget, standardized calibration/holdout split, raw-data package or statistical interval around the combined correlations is established. Steady analytical limits are useful verification problems for M3; comparing code to them verifies that model's solution, not experimental validation of a facility. In a lossy/high-Pr developing loop, missing mechanisms must be tested independently.

## TRIDENT implications and skepticism

Direct applicability: construct dimensionless definitions and ideal M3 verification cases using the appropriate Darcy convention; distinguish power-driven and temperature-driven problems. Conditional transfer: actual source–sink elevation and source/sink distributions, variable properties, mixed friction, bends, axial conduction, wall storage and distributed losses must be assessed. Geometry-specific agreement cannot justify reconstructing an unmeasured cross-section from centerline temperatures.

For motivation, emphasize the value of a controlled loop for separating buoyancy generation, heat transport, resistance and thermal memory. A target MSR branch must name its heat-removal function before choosing QoIs/similarity groups. H02 is constrained by longstanding wall-storage awareness; H04 must exceed mere matching of a known steady ratio. Identical Re or Pr does not by itself transfer a stability boundary.

Read next: S36 (supplied); Ishii–Kataoka 1984 for integral-system scaling; mixed-friction extensions beyond one p,b law; Hamilton's ORNL-1624 for early corrosion/thermal-convection motivation; original nonlinear stability work if instability becomes a thesis target. These are acquisition leads until independently read.

## Coverage

| Material | Status | Relevance and remaining limit |
|---|---|---|
| §§1–2, PDF 1–2/139–140 | Read/extracted | History, boundary contracts, prior scaling. Cited originals remain unread. |
| §3, §§3.1–3.3, PDF 2–6/140–144 | Read/extracted | Governing equations, steady and transient groups; Eq. 29 ambiguity unresolved. |
| §4.1, PDF 6–10/144–148 | Read/extracted | Heterogeneous literature-data comparison; no point digitization or raw-data reconstruction. |
| §4.2–4.3, PDF 10–12/148–150 | Read/extracted | Stability classes, wall role, verification uses; no independent Nyquist-root computation. |
| §5 and Appendix A, PDF 12–13/150–151 | Read/extracted | Conclusions, units and Darcy convention. |
| Figs. 1–8 | Inspected qualitatively; governing-equation pages visually checked | No digitized stability boundary admitted. |
| References, PDF 13–14/151–152 | Read for leads | No inference that all referenced works were read. |
| Supplement/raw datasets | Not supplied | Cannot establish absent from all repositories. |

## Claim ledger

| Claim ID | Claim | Locator | Evidence type/limit |
|---|---|---|---|
| S09-C01 | Steady and stability similitude demand different group/geometry matching. | §§3.1–3.2, Eqs. 24–31, PDF 5–6/143–144 | Author analysis under ideal assumptions. |
| S09-C02 | Local losses and mixed friction regimes constrain the simple steady law. | §§4.1.1–4.1.3, PDF 7–10/145–148 | Author comparative analysis, not new isolated mechanism experiments. |
| S09-C03 | Wall heat storage matters for quantitative transients even in insulated pipes. | §4.2.3, PDF 11/149 | Author argument citing earlier work; not first discovery claimed here. |
| S09-C04 | Natural-circulation loops serve many applications besides MSRs. | §1, PDF 1/139 | Author historical overview; originals needed for an origin chronology. |
| S09-C05 | Printed Eq. 29 needs reconciliation with Eq. 14's L_t/H factor. | Eqs. 14,24,29, PDF 4–5/142–143 | Analyst algebraic check, explicitly unresolved. |
