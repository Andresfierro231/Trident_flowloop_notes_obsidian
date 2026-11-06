# S36 Vijayan and Austregesilo 1994 scaling experiments

## Identity and readiness

P. K. Vijayan and H. Austregesilo (1994), *Scaling laws for single-phase natural circulation loops*, Nuclear Engineering and Design 152, 331–347. DOI https://doi.org/10.1016/0029-5493(94)90095-7, verified against publisher metadata. Complete 17-page scanned/typeset article; printed = PDF +330. OCR is noisy, particularly Greek symbols and plots; important Eqs. (9b–21),(22–23) visually checked on PDF pp. 4–5,8. All scientific sections, nomenclature and references read; plots inspected qualitatively without digitization. No separate supplement/raw data supplied.

**Ready:** motivation/history and qualified scaling synthesis; ideal steady-limit tests after convention checks. **Not ready:** transporting the fitted friction correlation into TRIDENT or reproducing full stability maps without the original data and derivation details.

## Problem and original contribution

Sections 1–2, PDF 1–5/331–335 ask whether power-to-volume scaling with preserved elevations but reduced diameters preserves single-phase natural circulation. Their own three water-loop experiments and analysis show that steady collapse need not preserve transient/stability behavior. This is stronger evidence for the limitation than a generic assertion that a small loop “represents” a reactor.

The motivation was scaled nuclear-plant test facilities and advanced reactors envisaging normal natural-circulation cooling, not specifically liquid-fuel MSRs. Earlier heat-transport/corrosion applications are cited. Heisler 1982, Ishii–Kataoka 1984, and the authors' preceding experiments are prior work identified by this source, not all independently read here. The fitted steady law is linked to their 1992 work; distinguish that attribution from the present paper's comparison and scaling argument.

## Experiment and evidence

Section 3, PDF 5–7/335–337; Figs. 1–2: three rectangular borosilicate-glass water loops, IDs 6, 11 and 23.2 mm, same elevation/length, horizontal external-wire heater and tube-in-tube water cooler. Atmosphere-connected expansion tank; insulated heater/piping, bare cooler and expansion tank. 1-mm K-type centerline thermocouples across primary heater/cooler and secondary cooler, wattmeter and secondary rotameter. The paper does not provide a complete uncertainty-qualified primary-flow measurement chain; do not label its Re observations as independently metered primary flow merely because plotted as measured.

Heating up to 2 kW and cooling-water flow 1–5 dm³/min (same numerical units as L/min). Four-hour hotter preliminary circulation with intermittent venting aimed to remove dissolved air. Power and secondary flow held constant during each test. Volume ratios relative to 23.2-mm loop are approximately 1:4.5 and 1:15. These are water/glass experiments, not salt/steel property or thermal-inertia matches.

The 6 and 11-mm loops stayed stable over the reported single-phase range; instability occurred in part of the 23.2-mm loop range. Fig. 2 illustrates 420 W, secondary 4.5 L/min and 31 °C inlet, with flow-reversal-associated temperature oscillations. At about 1000 W irregular oscillations appeared (PDF 6–7/336–337). These are example observations, not universal thresholds. No predeclared independent calibration/validation split is reported; empirical friction extracted from the same family of steady data also enters stability predictions.

## Equations, definitions and checks

| Equation ID | Reported mathematics/locator | Audit and applicability |
|---|---|---|
| S36-E01 | (L/A)dW/dt=ρ₀gβ∮Tdz−(fL/D)W²/(2ρ₀A²); Eqs. (1)–(5), PDF 2–3/332–333 | 1-D incompressible Boussinesq; no axial conduction, viscous heating or ambient losses. W kg/s; RHS Pa. Darcy convention follows p=64,b=1 in f=p/Re^b. Positive-flow expression needs a separate signed extension for reversals. |
| S36-E02 | Gr_m=D³ρ²βgQH/(μ³ A c_p); Re_ss=DW_ss/(Aμ); St_m=4Nu_m/(Re_ss Pr); Nu_m=U_i L/k; Pr=c_pμ/k. Eqs. (9a–f), PDF 3–4/333–334 | Dimensionless. Nu_m uses total loop length L and overall U_i, not ordinary hD/k. Q W; H source–sink elevation in generalized comparisons. Do not copy conventional Nu thresholds into this definition. |
| S36-E03 | Re_ss=[(2Gr_m/p)(D/L)]^[1/(3−b)]; Eqs. (12–15), PDF 4/334 | Model result under stated geometry/friction law. b=3−1/r; p=2/C^(3−b) for Re=C[Gr_mD/L]^r. Analyst arithmetic reproduces subsequent fit conversion. |
| S36-E04 | Match Gr_m, D/L, L/H, L/L_h and St_m for steady/transient/stability similarity; Eqs. (18–21), PDF 5/335 | Uniform geometric ratio L_p/L_m=H_p/H_m=(L_h)_p/(L_h)_m=D_p/D_m. Steady alone needs Gr_mD/L; extra requirements cannot be dropped for stability. |
| S36-E05 | Re=0.3548(Gr_mD/L)^0.43; f=22.26/Re^0.6744; Eqs. (22–23), PDF 8/338 | Empirical effective-loop behavior. Arithmetic gives b=0.6744186,p=22.2628. Not a fluid material property or universal fully developed pipe law. No confidence interval given here. |
| S36-E06 | Stability grouping Gr_m^[b/(3−b)](D/L)^[3/(3−b)] with St_m and preserved length ratios; Eqs. (17),(29–33), PDF 4,12–13/334,342–343 | With fitted b, exponents round to 0.29 and 1.29. Linear perturbation/Nyquist analysis; not nonlinear global stability proof. Characteristic-equation implementation not independently reproduced. |
| S36-E07 | 1/U_i=1/h_i+[D/(2k_w)]ln(D_o/D)+D/(h_oD_o); Eq. (34), PDF 14/344 | Area basis is primary inner surface; each term m²K/W. This is cylindrical overall resistance, not a local intrinsic h. Wall-storage dynamics are not contained in a steady resistance sum. |

Section 4.3, PDF 14–15/344–345, explains two diameter effects: larger L/D modifies resistance and smaller diameter changes overall heat transfer/St_m. The stated reasoning sometimes neglects wall resistance; it cannot automatically apply to a thick insulated TRIDENT pipe. Effective equivalent lengths used for local losses depend on the assumed loss model and cannot replace surveyed geometry.

## Results, limitations and skeptical transfer

Fig. 3 and Eq. (22), PDF 8/338: own steady data collapse approximately when plotted against Gr_mD/L. Figs. 4–7 compare other authors' data; those datasets are cited evidence, not new runs or independently read originals. The paper recommends a different high-range correlation above about Gr_mD/L=10¹¹ (PDF 10–11/340–341); not all experimental correlation claims share one regime. The later S09 refines these comparisons and discusses local/mixed-regime limitations; neither paper globally supersedes the other.

Fig. 8, PDF 13/343, shows a stability collapse and reports some experimentally stable points inside the predicted unstable region. Repeating paths reveals conditional stability: power stepped up from a stable state differs from power decreased from an oscillatory state. A successful linear curve is not a unique operating threshold. No complete quantified Type A/B measurement budget, shared-error covariance, parameter uncertainty or raw time history is supplied here. No universal percentage error should be attached to the collapse.

Direct methodological relevance: specify what is being scaled, preserve dimensionless definitions, and use steady versus transient predictions as separate claims. Conditional physical transfer: water/glass-to-glycol/steel/salt requires fluid property, heat-source/sink and solid thermal-inertia checks. No neutronics, fission heating, chemistry, freezing or reactor safety demonstration follows. The inability of a small diameter loop to reproduce one larger loop's instability warns against advertising a TRIDENT stability result as an MSR safety limit.

Experiments should document initial thermal conditions, power-ramp direction, prior oscillation/stagnation and repeatability. Those are possible protocol metadata for Nick's draft plan, not assertions of approved tests. A fitted natural-circulation f can absorb unmodeled local losses and secondary convection; do not interpret it as a new material friction law.

## Coverage and next acquisition

| Material | Status | Relevance/remaining restriction |
|---|---|---|
| §§1–2, PDF 1–5/331–335 | Read/extracted | Historical rationale and scaling; key steady/group equations visually verified. |
| §3, PDF 5–7/335–337 | Read/extracted | Own test design, instruments and operating observations; complete metrology chain not specified. |
| §4.1, PDF 7–12/337–342 | Read/extracted | Own fit plus cited cross-loop datasets; no data digitization. |
| §§4.2–4.3, PDF 12–15/342–345 | Read/extracted | Linear stability, path dependence and heat transfer; no numerical root reproduction. |
| §5/Appendix A, PDF 15–16/345–346 | Read/extracted | Conclusions and nomenclature. |
| Figs. 1–9 | Present; inspected qualitatively | No pointwise results digitized; exact curve locations not admitted. |
| References, PDF 16–17/346–347 | Read for acquisition leads | Originals not claimed read. |
| Supplement/raw data | Not supplied | No complete uncertainty reconstruction. |

Next: original Ishii–Kataoka scaling, Heisler shutdown-cooling scaling, Alstad et al. ANL-5409 (1956) and Hamilton et al. ORNL-1624 (1954) for history; same-loop raw/calibration data only if a numerical stability benchmark is selected. S09 is already supplied and should be used for subsequent generalized-loop restrictions.

## Claim ledger

| Claim ID | Claim | Locator | Type/limit |
|---|---|---|---|
| S36-C01 | The tested diameter reduction preserved approximate steady collapse but not observed instability. | §§3.3,4.1,5; PDF 6–8,15/336–338,345 | Original three-loop evidence, water/glass regime. |
| S36-C02 | Transient/stability similarity requires more than matching Gr_mD/L. | Eqs. 18–21; PDF 5/335 | Author ideal-model analysis. |
| S36-C03 | Some operating points showed path-dependent stability. | §4.2/Fig. 8; PDF 13/343 | Author repeated-observation account; not a global bifurcation reconstruction. |
| S36-C04 | The 0.3548/0.43 fit implies an effective f=22.26/Re^0.6744. | Eqs. 22–23; PDF 8/338 | Author empirical conversion, independently checked algebra. |
| S36-C05 | Motivation included generic reactor scaling and earlier non-reactor uses. | §1, PDF 1–2/331–332 | Historical discussion; cited origins are acquisition leads. |
