# S46 — Headley (2021): molten-salt PIV and local-flow evidence

Extraction date: 2026-10-20. **Ready for scoped motivation, prior-art and observation-limit synthesis. Not a validated TRIDENT closure or executable POD specification.**

## Identity, completeness and scope

William Milija Headley, *Flow Velocity and Temperature Measurements of Natural Circulation Flow in a (FLiNaK) Molten Salt Loop*, Texas A&M University, PhD dissertation, December 2021. Supplied file: HEADLEY-DISSERTATION-2021.pdf, 103 PDF pages. Title, abstract, contents, body through conclusions and references are present; no appendix is listed. Printed Arabic page = PDF page − 14, verified against Chapters 1 and 6. Final repository version/handle has not been independently matched; cite the supplied dissertation identity, without inventing a DOI.

All relevant chapter text was inspected, including facility construction, PIV, UQ, results and conclusions. Selected visual checks cover Table 3.2, methods equations, Table 5.1, reverse-flow figures and uncertainty tables. Not every reconstruction panel was visually inspected or digitized. Raw PIV videos, processing scripts and independent supplementary data were not supplied.

## Contribution, prior work and actual evidence

The contribution is demonstration of high-temperature molten-salt 2D2C PIV and characterization of an unexpectedly complex cooling transient, rather than a full autonomous loop predictor. Conventional PIV/POD methods are cited prior work. Chapter 6 (PDF 96/82) frames successful optical access and follow-on benchmark potential as principal outcomes. Chapter 1’s general reactor history is background, not original historical evidence; some terminology/composition statements are imprecise and should not anchor a reactor-family classification.

The measurements already show opposing local axial flow and growing shear structures after opening the visualization insulation (Chapter 5, especially Figs. 5.6,5.9,5.20,5.23,5.37; PDF 54/40,57/43,69/55,72/58,87/73). Hence “first observe molten-salt recirculation” and “first use POD on a molten-salt NC loop” are not viable broad novelty claims. These measurements do **not** establish 3D recirculating volume, heat-transfer enhancement caused by recirculation, or a dynamically predictive ROM.

## Facility and operating evidence

| Item | Evidence and locator |
|---|---|
| Geometry | Rhombus loop, nominal 1/2 inch schedule-40 316 steel, four 2 ft legs and 45° connections; quartz viewing section 12 mm ID, 16 mm OD, nominal 162 mm long. This is not the later 23.6 mm TAMU geometry. §§3.1–3.2, PDF 21–29/7–15. |
| Heating/cooling | Trace tapes with manual controls; two heat guns rated 1750 W each below test section. Ratings are not measured deposition. Opening the insulation for imaging creates the thermal transient. Table 3.1/§3.1, PDF 24/10. |
| Fluid | Reported FLiNaK composition is called **mass fractions** 0.465/0.115/0.42 (PDF 32/18). Those familiar numerical fractions must not silently be reinterpreted as molar fractions. Verify preparation/source records before property transfer. |
| Temperatures | Seven immersed probes, 15 wall thermocouples, nominal 0.4%-of-reading accuracy, DAQ 1.1 Hz; test-section inlet/outlet TP4/TP5, loop ΔT = TP6−TP1. §3.3, PDF 30–31/16–17. |
| Operating cases | Table 5.1: Re 27.6–92.7, Pr 8.6–12.2; test-section temperature 555.4–613.5 °C; tabulated mean midplane axial velocity 0.0062–0.0183 m/s. These are **plane averages**, not independently measured cross-sectional net flow. PDF 49/35. |
| Independence | One successful test, 2 March 2021 as labeled in figures; successive videos form datasets 3–5. These are not eleven independent experiments. Cases follow removal of insulation; one gap of about four minutes precedes case 5.3. PDF 47–49/33–35,89/75. |

## Mathematics and processing audit

Reported \(\omega_z=\partial v/\partial x-\partial u/\partial y\) uses horizontal x/u and vertical y/v (Eq. 4.4, PDF 36/22), units s⁻¹. The time mean and fluctuation decomposition are Eqs. 4.7–4.11 (PDF 37–38/23–24). These averages include evolving transients; statistical stationarity is not automatically satisfied. The text’s assertion that Reynolds averaging removes time dependence is not generally valid for an unsteady ensemble mean.

Snapshot POD is applied to **vorticity**, Eqs. 4.12–4.16 (PDF 38–39/24–25). Its covariance inner product is vorticity-based. Calling these eigenvalues kinetic energy, as later figures do, is not justified by those equations: a velocity norm and a vorticity norm are different. Spatial/temporal indices in Eqs. 4.12,4.15,4.16 also require clarification before literal implementation. This is a data reconstruction, without an identified evolution law or held-out predictive demonstration. More modes improve some visual reconstructions; more complicated/stagnating cases retain unresolved detail even with 45 modes (PDF 58/44,85/71,88/74).

Vortex detection uses a chosen size cutoff and vorticity regions (Eq. 4.17, PDF 40/26), not a topological proof of closed 3D recirculation. The stated 20-pixel ≈34 mm² conversion is not consistent with multiplying the stated 0.8 mm by 1.7 mm grid spacings: that product gives 27.2 mm² for 20 cells. Treat as an ambiguity until scripts clarify grid/cell conventions; do not silently correct the reported sizes. Threshold sensitivity and out-of-plane transport limit descriptor transfer.

PIV processing uses PRANA, multigrid/multipass settings in Table 4.2 (PDF 46/32). Camera images are acquired at 400 Hz, with a five-frame displacement separation. **Analyst check:** forming pairs (1,6),(2,7),… changes lag to 12.5 ms but does not alone reduce vector-series sampling from 400 to 80 Hz. The author describes an effective 80 Hz rate; actual stride must be confirmed before PSD frequency replication. A 2048-point Welch window and 512 overlap are reported (PDF 39–40/25–26).

## Uncertainty, limitations and results

The mean-velocity standard error is \(\sigma/\sqrt N\), Eq. 4.22; RMS uncertainty \(\sigma/\sqrt{2(N-1)}\), Eq. 4.23 (PDF 43/29). These expressions presume effective independence/appropriate distributional conditions. Strongly overlapping PIV pairs, autocorrelation and an evolving transient reduce effective sample size. Optical distortion, refractive-index gradients and inability to calibrate in situ are acknowledged (PDF 31/17), but these standard errors do not quantify them.

Eq. 4.24 reduces a correlation expression by asserting planar 2D PIV permits \(\varrho_{ij}=0\). **Analyst critique:** measuring two components in one plane does not make their physical fluctuations uncorrelated, particularly when reporting Reynolds shear stress. Uncertainty Tables 5.3,5.5,5.7 (PDF 65/51,80/66,95/81) omit explicit unit/normalization labels; do not treat their numbers as absolute m/s error bars without clarification. Convergence against the longest finite record (Eq. 4.21, PDF 42/28) establishes finite-record consistency, not full metrological accuracy.

Observed reverse layers and shear evolution are useful prior evidence. Interpretations about complete cessation of loop flow are less secure: Table 5.1 still gives case 5.3 plane-mean velocity 0.0062 m/s while prose describes essentially zero flow (PDF 86/72). A planar mean cannot resolve the full-section net mass flow in an asymmetric field. Likewise a −5/3 guide on vorticity-mode coefficient spectra does not independently establish a classical velocity-energy cascade.

No measured wall-flux distribution, calorimetric recirculation counterfactual, full joint uncertainty model or independent predictive validation split is established. Those limits preserve the value of the experimental demonstration while restricting stronger claims.

## TRIDENT implications and acquisitions

**Direct prior art:** local reverse-flow observations and vorticity POD already exist. **Conditional transfer:** an externally exposed cold wall can change local flow and the integral circulation; local instrument access can perturb the experiment. **Analogy:** specific vortex thresholds and thermal histories. **Unsupported transfer:** exact recurrence, local heat-transfer coefficients or 3D extent in TRIDENT without matched evidence.

Retain signed axial velocity separately from speed magnitude, and distinguish plane, area and mass-flux averages. A future CFD observation operator should reproduce the actual PIV plane/lag/window rather than compare arbitrary volume averages. For sparse TRIDENT thermometry, first demonstrate which thermal quantities can discriminate model forms; do not train a field reconstruction without field evidence.

Useful cited leads: S43; Seo et al. (2021) adjoint natural-circulation sensitivity, DOI 10.1016/j.nucengdes.2021.111349 (S48); underlying PIV uncertainty propagation/validation articles. These cited originals were not read through this dissertation. Raw PIV timestamps/calibration/processing metadata would be needed only if reproducing the spectra or descriptor values becomes a thesis requirement; no upload is required to establish the present prior-art limit.

## Coverage and claims

| Component | Status | Scope |
|---|---|---|
| Front matter; Chapters 1–2 | Inspected/extracted | Identity, objectives, motivation; background originals not presumed read |
| Chapter 3 | Text inspected/extracted | Geometry, sensor/heating/property definitions; construction photographs not exhaustively inspected |
| Chapter 4 | Text inspected/extracted; selected equation visuals | Processing, reduction, UQ; no implementation or raw-data replication |
| Chapter 5 | Relevant text/captions inspected; selected visual checks | All three usable datasets; no panel-by-panel digitization |
| Chapter 6/references | Inspected/traced selectively | Limits and next leads |
| Raw videos, scripts, independent supplements | Unavailable | Not claimed as reviewed |

| Claim ID | Claim | Locator | Limit |
|---|---|---|---|
| S46-C01 | High-temperature PIV and reverse local axial flow precede TRIDENT | Ch.2; Figs.5.6,5.9,5.23 | Local planar evidence, different facility |
| S46-C02 | Insulation removal initiates the observed transient | Ch.3; Ch.5 opening, PDF47–49/33–35 | Boundary perturbation, not passive observation |
| S46-C03 | Vorticity POD reconstruction is already demonstrated | §4.1.2; Ch.5 reconstruction figures | Not predictive dynamics or kinetic-energy optimality |
| S46-C04 | Tabulated Reynolds numbers use plane-mean axial velocity | Eq.4.5/Table5.1, PDF36/22,49/35 | Not independently measured net flow |
| S46-C05 | Statistical errors omit important systematic/dependence questions | §3.3/4.2.2, PDF31/17,43/29 | No complete PIV accuracy budget |
| S46-C06 | Vortex threshold area, lag/stride and property conventions require clarification | PDF32–34/18–20,40/26,46/32 | Analyst audit; do not silently repair |
