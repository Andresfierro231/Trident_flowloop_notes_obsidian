# Claim-to-evidence ledger

Canonical: `claim_ledger.json`. Original-source versions/coverage in dossiers. SYN-C claims are analyst cross-source interpretations; SYN-D are explicitly non-novel elementary derivations. Historical claim IDs and records remain unchanged.

| ID | Claim | Source / type | Original locator | Qualification |
|---|---|---|---|---|
| C01 | A fundamental-safety-function PIRT exists for liquid-fuel MSRs; its accident-scenario gaps cannot be adopted wholesale as TRIDENT loop gaps. | S12 | Title; scenario framing; I15–I16 entries, PDF p. 55 | Selected excerpts only; no full PIRT ranking extraction. |
| C02 | Surrogate-fluid FHR testing, code assessment, and scaling/distortion are established research activities. | S14,S15,S17 | S14 Section 2.1 and executive summary; S15/S17 abstracts | No claim that TRIDENT matches their similarity conditions. |
| C03 | The Reis–Hassan abstract explicitly prescribes net heat input and minimum loop temperature as model inputs. | S16 | ANS abstract | Initial abstract-only limit superseded by S16 scoped dossier; conditional measured inputs/calibration dependence now extracted. |
| C04 | Grey-box thermal model selection by increasing model complexity and evaluating extensions has strong existing precedent. | S08 | Section 4.1/Fig. 2; manuscript PDF pp. 7–8 | Building dynamics are a cross-domain comparator, not a verified model for an advecting loop. |
| C05 | Physical-parameter calibration and model discrepancy can be confounded. | S06 | Fig. 7/discussion, author manuscript PDF pp. 17–19 and Section 5 opening p. 22 | Specific TRIDENT identifiability requires a defined model, observations and inputs. |
| C06 | Operator-posterior uncertainty and a complete predictive uncertainty budget are different claims. | S04,S06 | S04 abstract/introduction; S06 confounding discussion | No assertion that S04 purports to solve every discrepancy or input-uncertainty problem. |
| C07 | NEMO's advertised inverse structure is nonlinear in model parameters and linear in inversion variables. | S05 | arXiv v1 abstract; related S05a abstract | Fitting TRIDENT conductances/capacities is not automatically in that class. |
| C08 | Bayesian thermal network discovery and stochastic reduced NCL dynamics already have relevant prior work. | S26,S30 | Publisher abstract excerpts; S26 author-code README | No performance/novelty judgement until full-text extraction. |
| C09 | The official 2026 GUM amendment adds guidance for significant nonlinearity in measurement models. | S33 | PDF p. 5, printed p. 1; amendments to 4.1.4/H.1.7 | Measurement propagation guidance does not establish model-form uncertainty coverage. |
| C10 | Fast system-level MSR analysis is already an active capability area; generic speed or a digital-twin label is not a sufficient research gap. | S27,S11 | Institutional/publisher abstracts | TRIDENT-specific comparator selection and costs remain unassessed. |
| C11 | Heat-loss and wall-storage effects deserve consideration in loop dynamics, with prior conjugate low-order work to compare. | S14,S18 | S14 Section 4.2.2.2; S18 abstract | Their importance for our chosen regime/QoI is not established. |
| C12 | The approximately 25% MSRE heat-balance claim is not verified in this pass and is excluded as motivation. |  | Targeted searches returned no traceable supporting primary passage | Search failure is not proof that the historical claim is false. |
| C13 | The retrieved SAM–CIET manuscript simplifies cooler heat exchange using prescribed outlet-temperature control and describes heat-loss calibration; comparison to TRIDENT must account for that input and calibration contract. | S17 | Section 2.2, manuscript PDF pp. 5–6; related temperature-profile modification p. 16 | Not a full appraisal of SAM or evidence that TRIDENT already predicts these quantities better. |
| C14 | The retrieved conjugate-loop preprint contains 1-D momentum/energy equations, wall thermal coupling and Fourier reduction, with explicit Boussinesq/axial-conduction/lumped-normal-wall assumptions. | S18 | Sections 2–3, PDF pp. 3–10 | Coupled-loop geometry and boundary conditions differ; equation transcription and journal changes remain to be checked. |
| C15 | The identifiability manuscript explicitly separates model states from an observation map and sets out a likelihood under Gaussian measurement noise. | S23 | Section 2, Eqs. 1–6, PDF p. 3 including repository cover | TRIDENT covariance, bias, autocorrelation and input errors require their own appropriate likelihood; profile calculations alone are not a universal structural-identifiability proof. |
| C16 | The supplied thesis title page identifies Ethan Rozak’s May 2026 MSE thesis at The University of Texas at Austin; its abstract identifies Texas A&M’s experimental facility. | S35 | PDF pp. 1–2 | User-supplied copy; final institutional deposit/version not verified. No thesis results evaluated in this acquisition pass. |
| S35-C01 | Retrospective modeled TAMU geometry and losses require reconstruction/calibration (reported method) | S35 | §4.1,5.1,5.7; printed33–35,48–56,67–71/PDF47–49,62–70,81–85 | No untouched validation partition |
| S35-C02 | Water PIV profiles digitized; salt raw profiles available to author (data provenance) | S35 | printed43–47/PDF57–61,Eqs4.9–4.11 | Not independent new experiments |
| S35-C03 | Cylindrical multilayer Robin condition with area convention (original implementation) | S35 | printed63–64/PDF77–78,Eqs5.23–5.25 | Steady radial resistance, no wall storage |
| S35-C04 | Full-loop refinement uses two completed levels (reported limitation) | S35 | printed79/PDF93,§6.2 | BC four-grid study does not establish full-loop order |
| S35-C05 | Pseudo-transient stepping sacrifices physical temporal accuracy (reported assumption) | S35 | printed64–66/PDF78–80,§5.5 | Steady targets only |
| S35-C06 | Seven aggregate PIV-style comparisons inside reported bands; Salt1 fails (original table result) | S35 | printed95/PDF109,Table6.10 | Calibrated inputs, chosen closures/operators, mean metrics |
| S35-C07 | Local reverse axial flow and point-temperature sensitivity predicted (original CFD result) | S35 | printed85–94/PDF99–108,Figs6.10–6.20 | Local fields not independently validated |
| S35-C08 | cp(T)T difference is not general sensible enthalpy (analyst equation audit) | S35 | printed54/PDF68,Eq5.6 | Need source code to distinguish print/implementation error |
| S35-C09 | Main and AppendixB salt-property sets disagree (source audit) | S35 | printed58 vs111/PDF72 vs125 | Cannot identify final run properties from prose alone |
| S35-C10 | Salt1 labeling-failure explanation remains unproved (critical appraisal) | S35 | printed96/PDF110,§6.5; TableC.1 printed116/PDF130 | Keep discrepancy and alternatives |
| S39-C01 | Supplied manuscript dated Dec2026; final status unverified (identity finding) | S39 | PDF1 | Do not present as already awarded/deposited |
| S39-C02 | Fiber temperatures differ from sparse interpolation (original observation) | S39 | printed54–61/PDF66–73,Figs5.3–5.9 | Fiber path is not a cross-sectional bulk measurement |
| S39-C03 | Near-wall scale is fitted/model-based (reported qualification) | S39 | printed59–65/PDF71–77,§5.2 | No directly measured radial BL thickness |
| S39-C04 | Insulated riser retains measured nonmonotonic thermal structure (original observation) | S39 | printed66–77/PDF78–89,Figs5.12–5.15 | Mechanism/offset/configuration confounders |
| S39-C05 | Chord reconstruction can fail a parabolic-flow limiting test (analyst derivation) | S39 | printed26/PDF38,Eqs4.5–4.7 | Does not measure actual case error |
| S39-C06 | Tested heat disturbance fails defensible time-of-flight inference (original result) | S39 | printed109–120/PDF121–132 | For this setup/forcing; not universal impossibility |
| S39-C07 | Smallest reported flow uncertainty is temperature-only (reported limit) | S39 | printed129–130/PDF141–142,Table7.2 | Not total uncertainty or validation |
| S39-C08 | Scaling derivation has sign, area, dimensional and exponent conflicts (equation audit) | S39 | printed136–143/PDF148–155,Eqs8.7–8.22,§8.3 | Verify originals/code before implementation |
| S39-C09 | PSD/CWT/SPOD textual frequencies do not establish identical peaks (audit) | S39 | printed100–106/PDF112–118 | Timebase/code/figures need reconciliation |
| S39-C10 | Re fit is a screening feasibility test (original fit and stated limit) | S39 | printed143–145/PDF155–157,Fig8.4 | No withheld transfer validation |
| S38-C01 | Continuous temperatures, but only pre-failure PIV and no pressure data, support the event reconstruction. | S38 | §2.2 p. 3 | Direct measurement contract; later mechanism claims remain inferred. |
| S38-C02 | Local heat-source changes and backup availability preceded leakage, further heater failures and freezing. | S38 | §3 pp. 4–7; §4 pp. 7–8 | Original event account; not isolated causal validation. |
| S38-C03 | Claimed blockage at 52 min is inferred from the thermal history rather than a continuous flow meter. | S38 | Phase V p. 7; §2.2 p. 3 | Author event interpretation plus evidence restriction. |
| S38-C04 | Printed magnitude-uncertainty Eq. 3 is dimensionally inconsistent as written. | S38 | Eq. 3 p. 3, rendered verification | Analyst audit; reported uncertainty not independently reconstructed. |
| S38-C05 | HITEC property-polynomial T is explicitly Kelvin here. | S38 | §2.5/Eqs. 4–7 p. 4 | Author convention; does not establish fit validity range. |
| S16-C01 | Eight experimental conditions are each simulated with two friction treatments. | S16 | IV p. 12; V pp. 16–17 | Author study design; do not call them 16 independent experiments. |
| S16-C02 | Q_net and measured minimum temperature are prescribed model inputs. | S16 | II.C Eq. 3 p. 8; III p. 11 | Original method; conditional prediction contract. |
| S16-C03 | Experimental friction and velocity assessment share PIV information. | S16 | II.C pp. 6–7; IV p. 13 | Original method plus dependence inference; no held-out independence established. |
| S16-C04 | Maximum salt velocity errors are reported as 17.30% default and 8.67% experimental friction. | S16 | W V p. 17; J Tables III–IV, PDF8/2141 | Author numerical summary checked against recovered tables; rounding prevents exact reconstruction of every percentage. |
| S16-C05 | Centerline temperature measurements limit high-Pr radial-gradient capture. | S16 | II.B p. 6; IV p. 13 | Author measurement limitation; not quantified TRIDENT error. |
| S16-C06 | Tables I–IV omitted from W are present in J and expose differing temperature-difference columns. | S16 | W PDF pp. 7,13–14; J PDF 5,8/2138,2141 | Version-specific completeness finding, gap resolved. |
| S16-C07 | The two table groups use different experimental ΔT values without an explicit reproducible transformation. | S16 | J Tables I–IV, PDF 5,8/2138,2141; IV PDF 7/2140 | Direct table comparison; possible bulk-observation correction, not silently resolved. |
| S16-C08 | Experimental friction improves salt velocity comparisons but does not uniformly improve temperature differences or every water velocity case. | S16 | J Tables III–IV, PDF 8/2141 | Original reported results, arithmetic/interpretation checked. |
| S09-C01 | Steady and stability similitude demand different group/geometry matching. | S09 | §§3.1–3.2, Eqs. 24–31, PDF 5–6/143–144 | Author analysis under ideal assumptions. |
| S09-C02 | Local losses and mixed friction regimes constrain the simple steady law. | S09 | §§4.1.1–4.1.3, PDF 7–10/145–148 | Author comparative analysis, not new isolated mechanism experiments. |
| S09-C03 | Wall heat storage matters for quantitative transients even in insulated pipes. | S09 | §4.2.3, PDF 11/149 | Author argument citing earlier work; not first discovery claimed here. |
| S09-C04 | Natural-circulation loops serve many applications besides MSRs. | S09 | §1, PDF 1/139 | Author historical overview; originals needed for an origin chronology. |
| S09-C05 | Printed Eq. 29 needs reconciliation with Eq. 14's L_t/H factor. | S09 | Eqs. 14,24,29, PDF 4–5/142–143 | Analyst algebraic check, explicitly unresolved. |
| S37-C01 | The work supplies eight water/HITEC steady PIV operating states and reconstructed thermal/friction results. | S37 | IV.A p. 8/-7; V, Tables VI–VIII | Original dataset, reused by S16. |
| S37-C02 | f is Fanning here and converts to S16 Darcy by ×4. | S37 | Eq. 14 PDF 10/-9; Table VII PDF 19/-18; S16 Tables I–II | Original convention plus analyst cross-source arithmetic. |
| S37-C03 | Local heater temperatures/h are reconstructed from sparse probes and a global power balance. | S37 | IV.E Eqs. 18–21, PDF 10/-9 | Original method, not resolved local temperature measurements. |
| S37-C04 | Salt off-center peaks and delayed centerline-temperature response motivate observation-aware reduction. | S37 | V.B–C/Figs. 8,11–12; PDF 12,14–15/-11,-13–14 | Original velocity/temperature evidence; thermal profile mechanism partly inferred. |
| S37-C05 | Reported uncertainty formulas contain dimensional/propagation issues requiring code-level reconciliation. | S37 | Eqs. 23,25–27, PDF 11–12/-10–11 | Analyst audit, not a declaration that measurements are unusable. |
| S37-C06 | Apparent correlation agreement does not establish validity outside its cited geometry/regime. | S37 | Table II PDF 5–6/-4–5; V.D–E PDF 16,18–19/-15,-17–18 | Analyst applicability appraisal. |
| S21-C01 | HITEC is used for high-Pr mechanism similarity, not one-to-one fluoride-salt performance. | S21 | §2.1 pp. 2–3 | Authors' explicit transfer restriction. |
| S21-C02 | Three local heating measurements are transient and have different time/history conditions. | S21 | §2.3 pp. 3,5; §4.3 p. 10; §5 p. 12 | Original protocol; not independent steady Pr sweep. |
| S21-C03 | Profiles are asymmetric and near-wall scaling is resolution-limited; thermal boundary layer was not measured. | S21 | Figs. 11–13/§4.3 pp. 10–12 | Direct velocity evidence plus author limitation. |
| S21-C04 | Bulk-flow estimation assumes revolving a half-profile and uses speed magnitude. | S21 | Eqs. 5–9, pp. 5–6 | Original analysis; not guaranteed true signed flux. |
| S21-C05 | Reported Nu is estimated from a flat-plate-type correlation. | S21 | Eqs. 30–31 pp. 9–10; Table 4 p. 11 | Closure-derived quantity; not independent experimental closure validation. |
| S21-C06 | Eq. 19 and heat-balance interpretations need reconciliation before implementation. | S21 | Eqs. 19,24–26 pp. 7–8 | Analyst dimensional/measurement audit; no claim experimental dataset itself is invalid. |
| S36-C01 | The tested diameter reduction preserved approximate steady collapse but not observed instability. | S36 | §§3.3,4.1,5; PDF 6–8,15/336–338,345 | Original three-loop evidence, water/glass regime. |
| S36-C02 | Transient/stability similarity requires more than matching Gr_mD/L. | S36 | Eqs. 18–21; PDF 5/335 | Author ideal-model analysis. |
| S36-C03 | Some operating points showed path-dependent stability. | S36 | §4.2/Fig. 8; PDF 13/343 | Author repeated-observation account; not a global bifurcation reconstruction. |
| S36-C04 | The 0.3548/0.43 fit implies an effective f=22.26/Re^0.6744. | S36 | Eqs. 22–23; PDF 8/338 | Author empirical conversion, independently checked algebra. |
| S36-C05 | Motivation included generic reactor scaling and earlier non-reactor uses. | S36 | §1, PDF 1–2/331–332 | Historical discussion; cited origins are acquisition leads. |
| S26-C01 | Signed latent/ReLU switches jointly represent coefficient and inclusion uncertainty (original method) | S26 | pp3–6, Eqs7,10–20 | Conditional on specified prior network |
| S26-C02 | Inputs exact, no process noise, iid Gaussian observations (reported assumptions) | S26 | pp4–5, Eqs11–14 | Explicit, high confidence |
| S26-C03 | Synthetic chains fail to mix; quantitative results use one chain (reported limit) | S26 | p7 §3.2; p16 §3.6 | Not full posterior model averaging |
| S26-C04 | Sparse high-noise single-observation model has test RMSE 1.31°C (original result) | S26 | p9 Table3 | Noise-free test target; exception to generic accuracy claim |
| S26-C05 | Seven finite R,C truths: only C2 inside displayed interval (audit of original table) | S26 | p10 Table4 | Table audit, not frequentist coverage estimate |
| S26-C06 | Four-office and house examples support case-specific predictive reduction (original results) | S26 | p13 Table5; p14 §3.5 | No NCL validation or universal horizon |
| S26-C07 | S(gamma)=0 freezes a node, not zero-capacitance elimination (analyst limiting-case audit) | S26 | p4 Eqs8–10; p9 Fig8 discussion | Must resolve physical interpretation before coding |
| S26-C08 | Supplement and original measurement papers needed for reproducibility (coverage finding) | S26 | p17 AppendixA/data statement; pp7,11–14 | Not yet synthesis-ready for reproduction |
| S40-C01 | Pump reliability/maintenance versus increased salt inventory explicitly motivated a natural-convection reactor concept. | S40 | PDF4/printed1, Introduction | 1958 calculated concept |
| S40-C02 | Report considers a60MW thermal system. | S40 | PDF3/printedii, Abstract; PDF4/printed1 | Design rating, not demonstrated power |
| S41-C01 | ORR salt convection loops were intended for irradiation of representative fuel with graphite/Hastelloy N. | S41 | PDF9/printed1, Abstract/§1 | Different purpose from passive decay-heat testing |
| S41-C02 | Operated loops experienced primary-system failures; thermal-stress causes remain qualified. | S41 | PDF9/printed1; PDF37–40/printed29–32,§7 | Observed failures versus proposed mechanism |
| S42-C01 | MSRE normal circulation design included fuel and coolant pumps. | S42 | PDF41/printed9,§2.4; PDF44/printed12,§2.4.2 | Does not rule out later natural-circulation tests |
| S42-C02 | MSRE aimed to demonstrate practical operation and long-duration salt/material performance. | S42 | PDF35–38/printed3–6,§1 | Original design purpose |
| S43-C01 | Corrosion and material exposure were important historical motivations for salt NC loops | S43 | §1, PDF 1–3/970–972 | Author historical account; originals distinguished |
| S43-C02 | Selected operating conditions are high-Pr, low-Re FLiBe tests, not a reactor analogue by default | S43 | Table 4, PDF 8/977; §2 | Geometry/heating/source distortions remain |
| S43-C03 | Flow is inferred by thermal pulses without an independent accuracy demonstration | S43 | §§2.2,3.4, PDF 4,9/973,978 | Repeatability is not accuracy |
| S43-C04 | Temperature profiles do not establish recirculation-induced heat-transfer enhancement | S43 | §3.1, PDF 5–7/974–976 | Physical interpretation remains provisional |
| S43-C05 | Reported UQ excludes installation/sheath bias and assumes uncorrelated propagation | S43 | §2.2/Eq.1, PDF 4/973 | Not a complete predictive budget |
| S43-C06 | Eq.13, Table2 conventions and Table1 distances need resolution before implementation | S43 | PDF 4,5,9/973,974,978 | Visual checks; analyst audit, not corrected source mathematics |
| S43-C07 | Campaign-dependent Nu offsets do not isolate a mechanism | S43 | §3.5/Fig.15, PDF 10–11/979–980 | Different baselines and confounders |
| S46-C01 | High-temperature PIV and reverse local axial flow precede TRIDENT | S46 | Ch.2; Figs.5.6,5.9,5.23 | Local planar evidence, different facility |
| S46-C02 | Insulation removal initiates the observed transient | S46 | Ch.3; Ch.5 opening, PDF47–49/33–35 | Boundary perturbation, not passive observation |
| S46-C03 | Vorticity POD reconstruction is already demonstrated | S46 | §4.1.2; Ch.5 reconstruction figures | Not predictive dynamics or kinetic-energy optimality |
| S46-C04 | Tabulated Reynolds numbers use plane-mean axial velocity | S46 | Eq.4.5/Table5.1, PDF36/22,49/35 | Not independently measured net flow |
| S46-C05 | Statistical errors omit important systematic/dependence questions | S46 | §3.3/4.2.2, PDF31/17,43/29 | No complete PIV accuracy budget |
| S46-C06 | Vortex threshold area, lag/stride and property conventions require clarification | S46 | PDF32–34/18–20,40/26,46/32 | Analyst audit; do not silently repair |
| S47-C01 | Reported power-metrology disagreement is not the alleged25% claim | S47 | Abstract; power measurement | PDF5–10/1–6; calibration versions differ |
| S47-C02 | Property revision resolved the primary-HX design overestimate in this report | S47 | Conclusions | PDF31/27; author's historical conclusion |
| S47-C03 | Air-radiator discrepancy and power-metrology discrepancy remained distinct unresolved issues | S47 | Conclusions | PDF31–32/27–28 |
| S47-C04 | Installed metrology and independent energy-scale checks matter | S47 | Table I; calibration discussion | PDF9–13/5–9; direct mechanism, not TRIDENT numerical error |
| S26-C09 | OFF-gate likelihood flatness is a local sensitivity property | S26 | SUP1 AppendixA/Eqs25–29, PDF1/32 | Assumptions on dependencies and θ≠0 |
| S26-C10 | Synthetic forcing noise is realized before simulation | S26 | SUP1 B.1, PDF1/32; CODE1 generator | Not full errors-in-input inference |
| S26-C11 | Full-chain diagnostics limit posterior model-probability claims | S26 | SUP1 B.10–12/Figs30–32, PDF14–16/45–47 | Plot inspection, no recomputation |
| S26-C12 | Repository is a synthetic single-chain implementation with explicit gates | S26 | CODE1 README; utility128–208,764–811 | No full-paper reproduction |
| S26-C13 | Units, time and normalization differ or need clarification across assets | S26 | SUP1 B.1–B.2,C.1,D.1; code303–370,449–500 | Do not silently standardize |
| M-S08-01 | Progressive thermal-network selection is established prior work | S08 | §4/Fig2; PDF7–8/6–7 | Cross-domain; no advective loop physics or independent regime prediction implied |
| M-S08-02 | Individual fitted capacities change physical interpretation with model topology | S08 | §5.5.2/Table3; PDF20/19 | Not material-property identification |
| M-S06-01 | An arbitrary discrepancy and calibration parameters are confounded | S06 | §4.2/Eq17; PDF17 | Selected theory; known controls assumed |
| M-S06-02 | Ignoring discrepancy can concentrate calibration around biased best fits | S06 | §4.1; PDF15–16 | Under the source model assumptions; not a numerical TRIDENT result |
| M-S04-01 | Bayesian inferred operators are propagated by integrating posterior-drawn ROMs | S04 | §3/Algorithm1; PDF4–7 | Conditional on data matrix/basis/hyperparameters/model |
| M-S04-02 | Posterior-drawn ROMs need not be stable | S04 | Conclusion; PDF18 | Author explicitly states stability remains an issue |
| M-S05-01 | NEMO uses externally characterized m and a linear inverse unknown q | S05 | §2.1/Eqs1–4; PDF3–4 | Does not justify relabeling coupled G,C,circulation as linear unknowns |
| M-S05-02 | Closed-form covariance is conditional in a reduced inverse subspace | S05 | §2.3/Eq14 PDF7; limitations PDF17 | Not complete uncertainty in m, model discrepancy or basis |
| M-S12-01 | Heat removal is a fundamental need; this PIRT has a liquid-fueled accident/spill scope | S12 | Table1/PDF16/5; summaryPDF65–67 | PIRT gaps are not automatically pipe-loop research gaps |
| M-S44-01 | Tank/open-boundary representation changed predicted stability in this CFD study | S44 | Conclusion; PDF13/12 | No universal boundary rule; system-specific numerical finding |
| M-S44-02 | Experimental validation of the DYNASTY quantitative stability boundary was future work | S44 | Conclusion; PDF13/12 | Do not call reproducing prior computations experimental validation |
| S10-C01 | Salt-loop steady/transient experiment–CFD comparison precedes TRIDENT | S10 | §§1,6,7; PDF3,6–11/562,565–570 | Main measured comparisons are temperatures |
| S10-C02 | Presented property polynomials were evaluated at300°C for these simulations | S10 | §3.4/Tables1–2,PDF4/563 | Not full temperature-dependent transport |
| S10-C03 | Effective loss BCs use empirical surface-temperature information | S10 | §3.5,PDF4/563 | Calibration independence/uncertainty not fully specified |
| S10-C04 | Expansion-tank participation materially changes heater-trip prediction | S10 | §6.2.3–4/Fig20,PDF8–9,11/567–568,570 | Case-dependent geometry treatment |
| S10-C05 | Spatial/time checks are useful but do not quantify every QoI's numerical uncertainty | S10 | §§4–5,PDF5–7/564–566 | No formal error estimate or smaller-than0.1 s reference |
| S10-C06 | Published operating-power statements disagree | S10 | Table3/§6.1.1/§7,PDF6–8,11/565–567,570 | Do not import as a validated envelope |
| S10-C07 | Trip/loss-of-forced-air tests are limited system analogies | S10 | §6.2.4–5,PDF8–11/567–570 | Neither decay-heat physics nor zero ambient loss established |
| S48-C01 | Adjoint natural-circulation QoI sensitivity is established application prior art | S48 | §§2–3,PDF3–8 | Few objectives/many parameters; oil-based forward model |
| S48-C02 | Published validation compares derivative methods for the same model | S48 | §3.3/Table2,PDF7–8 | Not a new independent experimental validation campaign |
| S48-C03 | h, energy, cp units and reference/periodic BCs require clarification for implementation | S48 | Eqs11,14,16,20–21; PDF4–5 | Analyst audit of visually checked mathematics |
| S48-C04 | Some functional derivative discrepancies exceed5% | S48 | TablesB1–B3,PDF16 | Temperature15.22%,Nu13.87%; source table values |
| S48-C05 | Viscosity-function gradients change reported sensitivities | S48 | §4.1/Eqs17,38–39/Figs8–12,PDF9–11,14 | Source-specific; no universal multiplier |
| S48-C06 | High-Pr reliability/stability interpretation is limited to local normalized sensitivity | S48 | §5/§6/Figs20–21,PDF14,16–17 | Not a probability-of-failure or dynamic stability proof |
| S48-C07 | Source functionals are integrated mass flux, temperature and cooler Nu | S48 | AppendixB/EqsB1,B4,B8,PDF18–19 | Not extrema; endpoint/normalization conventions matter |
| PF03-C01 | Covariance and autocorrelation-aware mean/drift methods already exist in plan | PF03 | Phase1 §§TechnicalBasis/Uncertainty,245–603 | Project-text evidence, not executed validation |
| PF04-C01 | Directed coefficients need node balance/common-temperature invariance in addition to total cancellation | PF04 | Phase2 Eqzonebalance/conductancematrix,275–305 | Analyst derivation from reported model |
| PF04-C02 | Passive fitting needs an explicit independently anchored scale | PF04 | Phase2 model/fit sequence,273,309–317,456 | Analyst identification consequence |
| PF04-C03 | Two-fill and continuous-recirculation preparation descriptions conflict | PF04 | Phase2 lines237,249,355–394,448 | Project-text consistency finding |
| PF04-C04 | Withheld Phase2 runs participate in model selection | PF04 | Phase2 lines313–314,458,462 | They are selection evidence, not final untouched assessment |
| PF05-C01 | Both required Phase3 cases are blind and cannot validate a revised fit to themselves | PF05 | Phase3 lines257–267,358–372 | Existing safeguard; preserve/reallocate explicitly |
| PF06-C01 | Primary-flow estimates are separate balances with common model/metrology dependencies | PF06 | Phase4 lines261–334 | Not independent flowmeter truth |
| PF06-C02 | Mean-temperature matrix coordinate is achieved by cooler adjustment | PF06 | Phase4 lines246–254 | Conditional/controlled response, not independent autonomous validation |
| PF03-C02 | Unweighted storage diagnostics do not by themselves bound total stored-energy rate | PF03 | Phase1 lines506–548 | Analyst scope qualification |
| PF03-C03 | The printed Newey–West white-noise equality needs a finite-sample qualification | PF03 | Phase1 lines424–451 | Analyst statistical audit; implementation not tested |
| S50-C01 | Motivation includes HTR, solar power, instruments and operating/material experience | S50 | §1, PDF 1–2 / 513–514 | Direct description; not universal MSR similarity |
| S50-C02 | Conjugate 1D circulation, trace heating and losses already have precedent | S50 | §3, PDF 3 / 515 | Described capabilities; implementation deferred to ref. 24 |
| S50-C03 | S50 uses temperature-dependent property fits and Nu = 4.36 | S50 | Eq. 1/Table 3/§3.2, PDF 5 / 517 | Audit closure validity and viscosity units |
| S50-C04 | Loss coefficients use an average-power fit and remain fixed across cases | S50 | §4.1, PDF 7 / 519 | Calibration dependence limits independence |
| S50-C05 | Forced-air interruption retains cooling and has model mismatch | S50 | §4.2.2/Fig. 9, PDF 8 / 520 | Proposed mechanisms not separately measured |
| S50-C06 | Heater-trip mismatch is attributed to omitted tank storage | S50 | §4.2.3/Fig. 10, PDF 8 / 520 | Existing prior art; causal inference qualified |
| S50-C07 | Claimed broad applicability exceeds demonstrated regimes | S50 | §4.2.3–5, PDF 8–9 / 520–521 | Reviewer's scope appraisal |
| S50-C08 | Reported LOHS temperature change/time and hourly rate disagree | S50 | §4.2.2, PDF 8 / 520 | Source statement plus explicit arithmetic audit |
| S51-C01 | NNCL uses DRACS as prototype | S51 | §§1–2, PDF 1–2 / 127–128 | Conditional system analogy; not liquid-fuel MSR validation |
| S51-C02 | UQ and model switching for salt-loop reliability predate our proposal | S51 | §§3–4.4/Table 1, PDF 2–6 | Existing methodology topic; not exhaustive uncertainty |
| S51-C03 | Failure criteria are high/decomposition and low/melting thresholds | S51 | §4.1, PDF 4 / 130 | Salt-specific numerical limits |
| S51-C04 | 43 inputs, 229 runs, 11 unsuccessful; reported probability .039 | S51 | §§4.4–4.6, PDF 5–7 | Authors' result, statistical interpretation unresolved |
| S51-C05 | Stated 229-run 99/95 fifth-order claim conflicts with standard iid one-sided audit | S51 | Eq. 4/§§4.4–4.6, PDF 6–7 | Our derivation; implementation not inspected |
| S51-C06 | Shell-side model choice materially affects computed margins | S51 | §4.8/Fig. 11, PDF 8–9 | Conditional numerical result; inadequate discriminating data acknowledged |
| S51-C07 | Equation 5 needs separate high/low failure signs | S51 | Eq. 5/prose, PDF 6 / 132 | Mathematical appraisal, not executed-code finding |
| S51-C08 | Correlation ranges, joint dependencies and normal-range conventions need qualification | S51 | Tables 1–3/Eq. 7 | No silent copying as a complete UQ specification |
| S51-C09 | Independent physical validation is not demonstrated in this article | S51 | §4.2/ref. Cai2017; entire results coverage | Cited validation original remains unread |
| S52-C01 | HANS serves reactor-relevant thermal, materials and instrumentation purposes | S52 | §§1–3, PDF1–4 / 308–311 | LBE/CHTR context, not MSR validation |
| S52-C02 | Nonuniform-area momentum and separate fluid/wall conduction predate this thesis | S52 | §§4.1–4.4, Eqs7–23, PDF5–7 | Printed implementation ambiguities remain |
| S52-C03 | Cooler coefficients are inferred from experiment at each power | S52 | §4.5/Eq24/Fig8, PDF7–8 | Calibration dependence; not independent validation |
| S52-C04 | Regional ambient coefficients and experimental flow use thermal balances | S52 | §4.6/Eq25/§5.1, PDF8 | Shared-input uncertainty and identifiability matter |
| S52-C05 | Structural/tank storage affects interpretation of transients | S52 | §5.2/Figs12–14, PDF9–11 | Authors' mechanisms not isolated experimentally |
| S52-C06 | Momentum/source/area/discrete-coefficient conventions need audit before coding | S52 | Eqs7–22/Table2, PDF5–7 | Our mathematical appraisal, not an executed-code finding |
| S52-C07 | Negligible axial conduction is a limited source conclusion | S52 | §5.1/Fig11/§6, PDF9/11 | No standalone error bound or controlled ablation |
| S30-C01 | Eight-state Fourier circulation/thermal model with unequal instantaneous duties is established prior work | S30 | §§2.1–2.2/Eqs2.20–2.26, PDF3–5 | Water HHHC, prescribed cooler wall |
| S30-C02 | Effective axial diffusivity is selected using stability data | S30 | §2.1, PDF3 | Effective closure, not material property; independence limited |
| S30-C03 | Stochastic minor-loss forcing uses channel DNS and is not loop-specific uncertainty calibration | S30 | §2.4, PDF5–6; conclusion12 | Authors explicitly qualify magnitude transfer |
| S30-C04 | Friction, forcing and SDE conventions need audit before coding | S30 | Eqs2.20–2.34, PDF5–6 | Our mathematical appraisal; actual code unread |
| S30-C05 | Stability validation case counts are internally inconsistent | S30 | §3.2/Fig4, PDF7 | Reported14 and16;10 correct from stated classifications |
| S30-C06 | Correlation switching affects part of the stability map | S30 | §§2.5/3.2, PDF6–7 | Model-choice sensitivity, not universal boundary |
| S30-C07 | Local stability and finite perturbation behavior differ | S30 | §4/Figs5–7, PDF7–9 | Numerical model evidence, not TRIDENT regime proof |
| S30-C08 | Dynamic noise can change escape behavior without large limiting-PDF change | S30 | §5/Figs9–12, PDF10–12 | Illustrative cases; no complete reliability estimate |
| S30-C09 | Supplied article references a missing appendix derivation | S30 | §2.2, PDF5; ending13 | Missing material recorded, not invented |
| S56-C01 | Single-phase similarity includes fluid, solid and interface physics | S56 | §2.1/Eqs1–16, PDF2–3 / 412–413 | 1D/Boussinesq; axial solid conduction omitted |
| S56-C02 | Pr matching alone is insufficient for general loop similarity | S56 | §§2.1–2.2/Eqs12–35, PDF3–5 | Our direct synthesis of the required groups |
| S56-C03 | h-dependent similarity is regime-sensitive and difficult to satisfy | S56 | §2.2/Eqs36–41, PDF5 / 415 | Illustrative correlations, not modern universal closures |
| S56-C04 | Relaxing Biot/Stanton has a target/time-scale qualification | S56 | §2.3, PDF6–7 / 416–417 | Not permission to ignore wall/local errors |
| S56-C05 | Transport/conduction and clock scaling differ from simple geometric scale | S56 | Eq12/Eqs56–59, PDF3/6 | Conditional same-material/fluid simplifications |
| S56-C06 | LOFT application is preliminary feasibility, not new matched-data validation | S56 | §2.4/§4, PDF6–7/13–14 | Fluid/geometry application differs from TRIDENT |
| S56-C07 | CHF is a separate two-phase scope | S56 | §1/§3/§4, PDF1–2/7–14 | Detailed two-phase derivations not extracted |
| S60-C01 | Local high-Pr flow already has planar PIV/CFD prior evidence | S60 | §§3–4/Figs12–18, PDF7–12 | Oil surrogate, not reactor flow |
| S60-C02 | PIV covers100–300W while CFD reaches600W | S60 | §3.2/§4.2/Table7, PDF9/11 | Do not merge observation and simulation ranges |
| S60-C03 | Full3D helical extent is inferred, not independently measured throughout | S60 | §4.1/Figs13–18, PDF8/11 | Planar observation plus numerical interpretation |
| S60-C04 | Power/temperature/Pr and other mechanisms covary | S60 | §4/Table7/Figs19–23, PDF9–13 | No isolated causal Pr manipulation |
| S60-C05 | Boundary-layer equation/range conventions need checking | S60 | Eqs5–7/Table8, PDF6/13 | Sign/range/observation-definition ambiguity |
| S60-C06 | CFD comparison and numerical checks do not give full predictive UQ | S60 | §3.3/Table4/Table6, PDF5/7/9 | No formal local-field/time-step uncertainty |
| S60-C07 | Centerline/free-stream and bulk velocities are different observation quantities | S60 | §4.3/Table7–8, PDF9/13 | Important for sparse thermal/flow reduction |
| S57-C01 | Closure choice can switch predicted stability for the reference loop | S57 | §§2–3.1/Figs3–12, PDF5–17 | Water-loop cases; not universal friction selection |
| S57-C02 | Numerical diffusion can suppress or alter predicted instability | S57 | §2/§3.1, PDF5–6/16–17 | Discretization-specific; refine time/space/observables |
| S57-C03 | BC/coefficient changes must be retained in comparisons | S57 | §3.1, PDF12 / 1844 | Later h/ambient differ from initial cases |
| S57-C04 | Fanning/Darcy and discrete/continuous stability conventions differ | S57 | Fig5/Eqs1–3, PDF9/12/15 | Our implementation mapping and source ambiguity |
| S57-C05 | Finite initial perturbations affect finite-window behavior | S57 | §3.2/Figs15–17, PDF18–27 | Some RELAP pulses are two-phase |
| S57-C06 | Preliminary CFD shows local asymmetry and instability | S57 | §4/Figs18–20, PDF28–31 | Not full V&V or measured3D local truth |
| S57-C07 | The paper does not settle a universal natural-circulation friction law | S57 | §§4–5, PDF19–21/29–31 | Geometry/regime/closure dependence remains |
| S13-C01 | The expert panel defines primary temperature distribution and bulk/potentially local salt velocity as explicit figures of merit | S13 | §V.A/TableII, PDF17–19 | This is expert elicitation, not measured TRIDENT model performance |
| S13-C02 | Temperature concerns include structures, transport/release and feedback; power deposition and flow influence thermal conditions | S13 | §V.A–B, PDF18–21 | Coupled composition/neutronics effects exceed our current loop model |
| S13-C03 | Both forced and natural circulation, including loss-of-pump transition/reversal, are relevant; form losses may need scaled empirical determination | S13 | §V.D, PDF23–24 | Not every reactor normally operates by natural circulation |
| S13-C04 | The panel did not formally rank research priorities as in a full PIRT | S13 | §V.A, PDF17 | Do not cite this article as a completed ranked-gap inventory |
| S54-C01 | The paper uses an ideal rectangular point-heated/cooled loop with uniform velocity and linear drag. | S54 | §2,Fig.1,Eqs2.1–2.4; PDF2–3/600–601 | Reported model; not measured geometry. |
| S54-C02 | Temperature is transported without axial diffusion between the exchange points. | S54 | Eq2.2,PDF2/600 | Direct equation evidence. |
| S54-C03 | Heat-exchange maps depend on flow; the heater is not a prescribed constant-power source. | S54 | Eqs2.3–2.4,PDF3/601 | Source-law applicability limit. |
| S54-C04 | An exact positive-velocity periodic solution is constructed with zero momentum inertia and discontinuous exchange. | S54 | §5,PDF4–6/602–604; Eq5.18 | Existence for this special model, not all loops. |
| S54-C05 | The continuous-ramp analysis establishes steady-motion instability, not a general periodic-orbit existence theorem. | S54 | §6,PDF7–8/605–606 | Direct result plus distinction in inference. |
| S54-C06 | Keller credits an earlier Welander report; publication year alone cannot assign conceptual priority. | S54 | §1,PDF1–2/599–600; references PDF8/606 | Historical attribution; report itself not acquired. |
| S54-C07 | The printed density/expansion convention needs resolution before implementation. | S54 | §2,PDF2/600, beforeEq2.1 | Analyst audit; plus sign visually verified. |
| S55-C01 | Cross-sectional thermal uniformity and linear instantaneous resistance are assumptions. | S55 | §2,PDF4/20 | Not observations of TRIDENT. |
| S55-C02 | Laminar flow can require additional mixing to justify cross-sectional uniformity. | S55 | §1,PDF2/18 | Explicit applicability warning. |
| S55-C03 | q is volumetric flow and heat transfer follows a prescribed-wall-temperature relaxation law. | S55 | Eqs4–5,PDF4/20 | Visually verified; not constant heater power. |
| S55-C04 | Advected thermal perturbations lead to delayed oscillatory instability despite a restoring static argument. | S55 | §§3–4,Eq26,PDF7–10/23–26 | Mechanism within the ideal model. |
| S55-C05 | Numerical responses include damped oscillations, pulsations and irregular flow reversals. | S55 | §5,Fig9,PDF10–13/26–29 | Numerical illustrations, not new measured reversal data. |
| S55-C06 | Cell discretization shifts the calculated stability limit. | S55 | §5,PDF12–13/28–29 | Numerical sensitivity acknowledged; no full modern uncertainty estimate. |
| S55-C07 | Temperature-pocket phase and exchanger exposure explain amplification in this model. | S55 | §6,PDF13–14/29–30 | Conditional mechanism, not universal MSR behavior. |
| S59-C01 | Scalar uniform velocity, fixed prescribed heat flux and axial diffusion define the model. | S59 | Eq1.1,PDF2/1073 | Not arbitrary conjugate-loop physics. |
| S59-C02 | Net prescribed heating evolves the mean; zero-mean analysis follows subtraction. | S59 | §2,PDF3–4/1074–1075 | Physical accumulation remains. |
| S59-C03 | Mode advection rotates phase; diffusion damping scales as k². | S59 | Eq3.1,PDF8/1079 | Direct model structure. |
| S59-C04 | Heating/geometry Fourier-support overlap determines a reduced nonlinear subsystem. | S59 | Thm3.6,PDF12–13/1083–1084 | Finite exact asymptotic reduction under assumptions. |
| S59-C05 | Omitted/slave modes can need reconstruction despite a small circulation subsystem. | S59 | Eq3.12,PDF14/1085;Thm3.6 | Sensor/extrema predictions remain separate. |
| S59-C06 | A special three-variable case transforms to Lorenz form. | S59 | §3.1.3,PDF15–16/1086–1087 | Constant drag and restricted supports. |
| S59-C07 | Diffusion examples switch nonmonotonically between periodic and Lorenz-like behavior. | S59 | §4,Figs1–2,PDF19–21/1090–1092 | Numerical examples, not measured phase diagram. |
| S59-C08 | Some nondiffusive solutions are unbounded while bounded examples also occur. | S59 | Prop2.5,PDF8/1079;§4,PDF19–20 | Quantifiers matter. |
| S62-C01 | Eight-state dynamics and earlier validation are inherited from S30. | S62 | §II,PDF3;TablesI/III | No new independent loop validation of noise. |
| S62-C02 | Minor-loss forcing compares six generators trained/constructed from channel DNS. | S62 | §III,PDF3–5 | Not TRIDENT-specific calibration. |
| S62-C03 | Stochastic first-reversal distributions shift earlier on average but can extend later. | S62 | §IVA,Fig2,PDF5–6 | Selected initial condition/system. |
| S62-C04 | OU approximately matches the common-data bootstrap for the studied QoI. | S62 | §IVA,PDF5–6 | Empirical agreement, not general equivalence. |
| S62-C05 | Initial transient and long-run dwell-time distributions have different noise sensitivity. | S62 | §§IVA–B,Figs2/4,PDF5–7 | Model-specific QoI dependence. |
| S62-C06 | The log-plus-linear CDF fit has smaller reported selected-point RMS error. | S62 | Eqs12–15,TableII,PDF8 | No held-out likelihood/support validation. |
| S62-C07 | Printed Eq13 is not the derivative of printed Eq12 for general a2. | S62 | Eqs12–13,PDF8 | Visually verified text; derivative is our audit. |
| S62-C08 | Nonexponential dwell times do not alone disprove Markov dynamics in a richer state. | S62 | §IVB,PDF8 plus analyst mathematical qualification | Narrows the authors' interpretation. |
| S63-C01 | Local linear stability can coexist with large-amplitude responses to finite initial-flow disturbances. | S63 | §3.2,Figs6–7,PDF5–8 | Selected model trajectories, not all-state basin certificate. |
| S63-C02 | The model uses 1D Boussinesq flow, external heating and an overall cooler law. | S63 | §2.1,Eqs1–6,PDF3 | No resolved conjugate wall storage. |
| S63-C03 | Regime-dependent Darcy laws enter the stability calculation. | S63 | Eq6,PDF3;§3.1,PDF5 | Transition discontinuities are model choices. |
| S63-C04 | A5mm/2.5mm grid comparison supports the chosen local stability map resolution. | S63 | §3.1,Fig4,PDF5–6 | Does not establish nonlinear tail/statistic convergence. |
| S63-C05 | Reversal-like switching and transient switching followed by settling occur in examples. | S63 | §§3.3–3.4,Figs8–10,PDF6–10 | Not measured TRIDENT behavior. |
| S63-C06 | The chaos appraisal uses projected box-counting and initial-condition sensitivity. | S63 | AppendixA,PDF10–11;§3.3 | Evidence is limited; numerical fractal estimate is not a proof. |
| S63-C07 | Signed-drag and reverse-advection conventions are under-specified by the printed equations. | S63 | Eqs5,8,12,14–22,PDF3–5 | Analyst implementation concern; code not audited. |
| S63-C08 | The paper's basin/subcritical interpretation is inferred from transients rather than a complete cycle-continuation study. | S63 | §3.2,PDF5–6 | Preserve inference strength. |
| S66-C01 | Separate inner/outer wall capacities and radial conduction are established loop-model states. | S66 | §2.1,Eqs1–6,PDF3–4/413–414 | Specific lumping and excluded axial conduction/loss. |
| S66-C02 | Constant outer-cooler temperature and uniform distributed fluid heating define the reference source/boundary problem. | S66 | §2.1,Fig1,PDF3/413 | Not TRIDENT secondary-loop equivalence. |
| S66-C03 | α is a temperature-rise split using internal heating outside the cooler. | S66 | Eqs23–26,PDF5/415 | Not automatically total-power fraction. |
| S66-C04 | The nondimensional capacity ratio is fluid/wall; h's flow derivative enters stability. | S66 | Eqs41,46,PDF6/416 | Ratio direction and derivative matter. |
| S66-C05 | Table1 diameter conflicts by a factor of ten with the stated length/diameter ratio. | S66 | Table1,PDF8/418;§6.1 | Printed value visually checked; intended input unresolved. |
| S66-C06 | Real-material combinations can enlarge unstable regions despite stabilizing isolated-property trends. | S66 | §6.1;§7,PDF17/427 | Reject universal stabilization claim. |
| S66-C07 | Distributed external heating can approximate internal-heating stability in the analyzed long/slender case. | S66 | Eqs61–62,Fig13,PDF12/422;§7,PDF18/428 | Conditional source/layout/QoI transfer. |
| S66-C08 | Nonlinear stability labels use a finite-window variance ratio with threshold10^-3. | S66 | §3.4,PDF7–8/417–418 | Numerical diagnostic, not proof. |
| S66-C09 | Agreement among O-O/RELAP/CFD is code comparison; experimental validation is explicitly future work. | S66 | §6.3,Fig21,PDF14–17;§7,PDF18/428 | No new measurement-based validation/UQ. |
| S66-C10 | Three-dimensional comparison deliberately uses laminar CFD. | S66 | §5.3,PDF10–11/420–421 | No universal turbulent validation. |
| S07-C01 | Parameter, prediction and discrimination goals require distinct utility choices. | S07 | §2.1,PDF4 | Demonstrations target parameter information. |
| S07-C02 | Expected parameter-information gain averages posterior/prior KL over prospective data. | S07 | Eqs4–8,PDF6–7 | Conditional on prior/model/likelihood. |
| S07-C03 | Joint experiment information is generally nonadditive. | S07 | §2.2,PDF7;AppendixA,PDF49–50 | Assumed conditional independence; repetition can serve other goals. |
| S07-C04 | Finite inner sampling and sample reuse contribute estimator bias. | S07 | §2.3,PDF8;AppendixB,PDF50–51 | More outer samples alone do not remove bias. |
| S07-C05 | The surrogate spans parameter and design variables and approximates outputs, not internal state reduction. | S07 | §3,PDF10–14 | Not interchangeable with a physical loop ROM. |
| S07-C06 | Observable selection and prior support can change the preferred experiment. | S07 | §§5/6.5,PDF16–17/20–21 | Example-specific; define TRIDENT observations first. |
| S07-C07 | A surrogate adequate for design can be inaccurate for posterior inference. | S07 | §6.7,PDF23–24 | Need target-specific surrogate verification. |
| S07-C08 | Demonstrations infer from simulated data; structural inadequacy remains an explicit limitation. | S07 | §6.5,PDF20;§7,PDF24–25 | No new loop/combustion experiment validation. |
| S07-C09 | Printed SPSA sign and perturbation conventions require checking before implementation. | S07 | Eqs11–13,PDF9 | Analyst audit, not code verdict. |
| S18-C01 | The model couples two buoyancy loops through a conducting/storage wall and Fourier reduction. | S18 | §§2–3,PDF3–10 | Not a single-loop/prescribed-secondary equivalent. |
| S18-C02 | CFD uses fictitious fluid at Pr.000125. | S18 | Tables3/5,PDF12 | No direct glycol/salt material validation. |
| S18-C03 | Localized thermal coupling produces modal convolutions. | S18 | Eqs24–28,PDF6–7 | Contrasts restricted S59 closure. |
| S18-C04 | Three retained mode orders are checked against bulk Re/average temperature. | S18 | §3.6,Fig2,PDF10 | Not three total states or local-field convergence. |
| S18-C05 | Main conjugate transient assessment is against CFD; experiment comparison is indirect/single-loop. | S18 | §§4.2.3/4.4,PDF13–17 | No direct new coupled-loop experiment validation. |
| S18-C06 | Inclination-dependent heat-transfer correction is informed by the same CFD study. | S18 | Eq55,Figs12–13,PDF17–19 | Not independent generalization evidence. |
| S18-C07 | Reported Re/temperature differences are approximately5%/15% for specified cases. | S18 | §4.4.2,PDF16 | Comparison errors, not uncertainty bounds. |
| S18-C08 | Printed preprint equations need source/sign/prefactor/conjugacy reconciliation. | S18 | Eqs2–5/19/26/30–36/74,PDF4–7/27 | Analyst audit; code not evaluated. |
| S18-C09 | Appendix large-step sensitivity ratios do not prove negligible change of the QoIs. | S18 | Tables6–8,PDF27–28 | Analyst qualification; endpoint changes calculated above. |
| S18-C10 | Wall-parameter settling interpretation differs between body and conclusion. | S18 | §5.2,PDF21;§7,PDF26 | Unresolved preprint inconsistency. |
| S23-C01 | Initial states and observation scale/offset can belong to the parameter vector. | S23 | Eqs1–3,PDF2/1924 | Appropriate likelihood/inputs still needed. |
| S23-C02 | Profile construction reoptimizes all remaining parameters. | S23 | Eq10,PDF4/1926 | Not a fixed-parameter slice or posterior integral. |
| S23-C03 | Structural invariance differs from shallow practical uncertainty. | S23 | Eq9/§2.3,PDF3/1925 | Finite numerical flatness alone is not proof. |
| S23-C04 | Hessian and profile intervals can differ substantially in a practical ambiguity. | S23 | Table1,PDF6/1928 | Biological example, not thermal uncertainty magnitude. |
| S23-C05 | Profile trajectories guide suggested measurements and reduction. | S23 | §4,PDF4/1926 | Predictive validity under changed conditions remains to be tested. |
| S23-C06 | Added measurement effects are demonstrated with hypothetical data. | S23 | §5,PDF6/1928 | Not a newly executed experiment. |
| S23-C07 | One-dimensional relation recovery has an explicit manifold-dimension restriction. | S23 | §5,PDF5/1927 | Higher-dimensional ambiguity needs more analysis. |
| S23-C08 | Detailed profile algorithm/runtime analysis is in uninspected supplementary material. | S23 | §§4–6,PDF4–6/1926–1928 | Main-paper readiness does not cover supplement. |
| S67-C01 | The demonstration is a two-state R3C2 building network with measured power/outdoor inputs. | S67 | Fig1/§3.1/Eq24,PDF6–7/205–206 | No circulation/advection physics. |
| S67-C02 | Likelihood uses innovations and their covariance including a log determinant. | S67 | Eqs7–14,PDF3–4/202–203 | Conditional Gaussian/filter approximation. |
| S67-C03 | Data are filtered/resampled and artificial temperature noise added. | S67 | §3.2,PDF6/205 | Not a reconstruction of traceable original metrology. |
| S67-C04 | UKF is efficient relative to EnKF in this small linear example. | S67 | Tables3–6/§4.5,PDF7–9 | Not general algorithm dominance. |
| S67-C05 | Calibration replay and fitted bands are used as validation evidence. | S67 | §4.4/Figs5–6,PDF8/207 | No independent predictive coverage established. |
| S67-C06 | Bounds and parameter dependence materially alter reported profiles. | S67 | §4.6/Figs8–11,PDF9–10 | Global identifiability/coverage needs further justification. |
| S67-C07 | The printed likelihood-ratio normalization needs reconciliation. | S67 | Eqs12/14/20/21,PDF3–5 | Analyst mathematical audit; executed objective unknown. |
| S67-C08 | Serial residual diagnostics alone do not establish Gaussianity or held-out validity. | S67 | §§2.5/4.4,PDF5/8 plus analyst qualification | Preserve separate statistical questions. |
| S67-C09 | Exhaustive pair profiles have substantial optimization cost. | S67 | §4.5.1,PDF9 | Select consequential groups before exhaustive scans. |
| S68-C01 | Sensor comparison also changes wall construction and observed physical component. | S68 | §3,Fig2,PDF4–5/54–55 | Placement/material effects are not isolated. |
| S68-C02 | Warm-started pair-profile calculations reduce reported computation. | S68 | §2.1,PDF3/53 | Local/implementation-specific result, not guaranteed global coverage. |
| S68-C03 | Sensor choice changes selected parameter profiles and reveals bound-related dependence. | S68 | §§4.1–4.2,Figs6–7,PDF5–6 | A calibration/inference result, not universal sensor ranking. |
| S68-C04 | One proposed storage reduction fails residual assessment; removing a loss branch is retained after refitting. | S68 | §§4.3/4.5,PDF6–7 | No unchanged independent holdout demonstrated. |
| S68-C05 | Total resistance/time-scale combinations remain stable across different fitted components. | S68 | §4.4,Table3,PDF7/57 | Direct prior art for grouped inference; no material-property proof. |
| S68-C06 | Observation choice, model structure and identifiability are already treated jointly. | S68 | §5,PDF8/58;§§3–4 | TRIDENT novelty must go beyond combining these ingredients. |
| S69-C01 | Two synthetic IDEAS dwelling simulations provide the identification reference. | S69 | PDF2–4/264–266;§§2–4,Table1–2 | Not experimental reactor validation. |
| S69-C02 | Delivered radiator heat bypasses upstream heating-system dynamics and effective storage depends on heat-emission system. | S69 | PDF3–4/265–266;§4 | Boundary lesson transfers conditionally; no TRIDENT finding. |
| S69-C03 | Good temperature prediction need not determine physical coefficients; added virtual flux observations change inference. | S69 | PDF5–7/267–269;§5.1,Figures3–6 | Actual extra measurements not assumed available. |
| S69-C04 | Effective capacity and combined massless-window/ventilation loss require explicit parameter interpretation. | S69 | PDF7/269;§5.1,Figures6–7 | Effective parameters depend on model and excitation. |
| S69-C05 | Specified biased observations change coefficients without a comparable temperature-RMSE change. | S69 | PDF10/272;§5.3,Figures8–11 | Synthetic cases, not universal bias tolerances. |
| S69-C06 | Increasing order can worsen longer-horizon predictions and parameter estimation. | S69 | PDF5–7/267–269;§5.1,Figures3,5–6 | Order5 failure is case-specific. |
| S69-C07 | Reduced/detailed simulation differences depend on season and source representation. | S69 | PDF10–11/272–273;§6,Figures12–15 | No locked independent physical validation or calibrated predictive coverage established. |
| S69-C08 | Printed Eq1 omits dt on drift terms; conventional SDE normalization is an interpretation requiring explicit notation. | S69 | PDF3/265;§3,Eq1 | Visually verified notation issue; no silent implementation correction. |
| S70-C01 | Synthetic one-dimensional wall uses surface-temperature inputs and internal-face flux output. | S70 | PDF8–11/451–454;Table1,Figure2,Eq5–6 | Not real on-site validation or a circulating loop. |
| S70-C02 | Nuisance-reoptimized profiles use a normalized likelihood ratio and asymptotic confidence threshold. | S70 | PDF5–6/448–449;Eq1–4 | Profile is not a marginal; regularity/finite-scan limitations apply. |
| S70-C03 | Total resistance can remain stable despite internally non-identifiable coefficients while total effective capacity can fail. | S70 | PDF13–15/456–458;Figures5–6;PDF26–28/469–471;Appendix1 | Case-specific evidence, not a theorem for all aggregate loop quantities. |
| S70-C04 | One-step residual agreement can mask free-simulation inadequacy. | S70 | PDF16–17/459–460;Figure7 | Whiteness does not guarantee independent predictive accuracy. |
| S70-C05 | Identifiable reduced RC coefficients need not map to material layers. | S70 | PDF21/464;Discussion | Internal distributions are model/signal dependent. |
| S70-C06 | Non-identifiable nuisance coefficients can assist estimation of the target aggregate. | S70 | PDF21–22/464–465;Discussion/conclusion | Insignificance does not justify automatic deletion. |
| S70-C07 | Printed Table1 capacitances sum to7.8044e5, inconsistent with printed6.18e5J/(m²K). | S70 | PDF8/451;Table1 | Our arithmetic from visually checked entries; do not repair source silently. |
| S70-C08 | Summer order2 Table3 reports Rtot3.7m²K/W with SD.21 and Ctot2.8e5J/(m²K) with SD9.3e3. | S70 | PDF18/461;Table3 | Standard deviations, not95% interval widths; capacity reference unresolved. |
| S64-C01 | Similarity includes boundary/initial conditions and solid response beyond fluid groups. | S64 | §IV.A,PDF6/349,Eq8–10 | Specific single-phase scaling assumptions. |
| S64-C02 | Matched Re/Fr couples velocity/length scales; buoyancy adds βΔT similarity. | S64 | Eq2–7,PDF5–6/348–349 | Common gravity and geometric scaling. |
| S64-C03 | Pr matching does not ensure solid transient similarity. | S64 | Eq8–10,PDF6/349 | Steady and transient solid constraints differ. |
| S64-C04 | Example group-matched cases retain viscosity-variation distortions. | S64 | TableV,PDF11/354 | Source-era illustrative property estimates, not measured reactor-transfer errors. |
| S64-C05 | Low-temperature surrogates do not automatically reproduce radiative heat transport. | S64 | §III,PDF4–5/347–348 | Each physical configuration needs assessment. |
| S64-C06 | The laminar radiation illustration has an h–Nu–D inconsistency under its stated property context. | S64 | §III,PDF5/348 | Our dimensional check; do not use its numerical fraction as a validated general result. |
| S64-C07 | The printed Fourier group is reciprocal to a common definition; its time-ratio convention must be retained. | S64 | §II,nomenclature,PDF3,13–14 | Definitions may differ across papers. |
| S64-C08 | Scaled experiments support selected mechanism and model tests with explicit distortion. | S64 | §VI–VII,PDF10–13/353–356 | Not proof of full reactor equivalence. |
| S65-C01 | The1D model combines localized wall heating and uniform fluid heating including the cooler. | S65 | §2.1,PDF2,Eq1–4 | Constant-property Boussinesq and ideal cooler assumptions. |
| S65-C02 | Source partition changes studied dimensionless stability regions. | S65 | §4.1,PDF8–9,Fig10–11 | Not a mapped fluid-specific operating trajectory. |
| S65-C03 | Heater/cooler arrangement changes the stability comparison. | S65 | §4.2,PDF9–10,Fig12–13 | Studied VHHC/VHVC only, not universal ranking. |
| S65-C04 | Linearization freezes transition-factor and heat-transfer variations. | S65 | PDF4,footnote3;PDF9,Fig11 | Particularly affects transition region. |
| S65-C05 | Actual fluid-specific operating curves were not mapped onto the stability diagrams. | S65 | §4.2,PDF9 | Do not infer realized reactor operating failure. |
| S65-C06 | Cross-method agreement does not provide experimental validation. | S65 | §4–5,PDF7–10 | Authors explicitly call for experimental validation. |
| S65-C07 | The defined α uses internal generation outside the cooler in its denominator. | S65 | Eq11,14,PDF3–4 | Our clarification; prose total-power fraction is not exact for all-loop generation. |
| S65-C08 | Stanton nomenclature conflicts with Eq11, and local-loss convention needs care. | S65 | Eq11–12,PDF3–4;PDF10,nomenclature | Keep implementation normalization/coefficient ambiguities explicit. |
| S13-C05 | The elicitation targets liquid-fuel primary-system modeling, not detailed auxiliary/secondary circuits. | S13 | §I.B,PDF6;§IV.C,PDF16 | Other subsystem missions need additional literature. |
| S13-C06 | Properties, heat transfer, source allocation and solid response enter engineering temperature/flow questions. | S13 | §V.B–C,PDF20–23 | Qualitative need, not a numerical uncertainty budget. |
| S13-C07 | Natural-circulation resistance and multidimensional pool dissipation are identified modeling concerns. | S13 | §V.D,PDF23–25;§VIII,PDF41 | Pool effects are not evidence of TRIDENT local pipe flow. |
| S13-C08 | Flow/source/reactivity coupling limits a nonnuclear thermal surrogate. | S13 | §VI.A,PDF27–29;§VIII,PDF43 | No kinetics model technically audited for implementation. |
| S13-C09 | Heat-removal/reactivity/freezing wording needs a sign/sequence qualification. | S13 | §IV.C,PDF16–17 | Our limiting-case check; no silent source correction. |
| S13-C10 | Source-era concept/knowledge statements are not current vendor/regulatory specifications. | S13 | §III/TableI,PDF9–12;§II,VIII | Current status was not established by this historical article. |
| S19-C01 | Surface thermometry provides the experimental comparison; no direct flow benchmark | S19 | §2.1–2.4,PDF2–3 | Velocity not independently validated |
| S19-C02 | Steady CFD uses measured/averaged thermal boundaries | S19 | §3.1,PDF6–7;Table4/PDF5 | Not autonomous transient prediction |
| S19-C03 | Surface- and calculated-bulk-based flow estimates differ from CFD | S19 | Table7,PDF8 | Model-to-model, shared observation ingredients |
| S19-C04 | Quoted5.5% is a discrepancy increase, not measured flow-error bound | S19 | Table7/PDF8;§4/PDF11 | Rounded table≈5.4percentage points |
| S19-C05 | Stated common refinement ratio conflicts with tabulated adjacent h ratios | S19 | §2.4.4,Table5,PDF5 | Our arithmetic; uncertainty estimate needs clarification |
| S19-C06 | Modeled local profiles/vortices are not measured extent/causality | S19 | Fig7–10,PDF9–10 | No direct local flow/thermal-effect validation |
| S19-C07 | Printed energy formulation is ambiguous in sign and E units | S19 | Eq2,PDF3 | Actual implementation not inferred from typo |
| S19-C08 | Analytical h closure comes from an open-vertical-pipe correlation | S19 | Eq24/PDF6;Ref29/PDF12 | Original applicability not read |
| S74-C01 | Modern multi-fluid/reference-design H2TS similarity is established prior art | S74 | §1–4,PDF3,8–17 | Analytical design study |
| S74-C02 | Scaling assumes no external loss/negligible leg-wall inertia,constant-property1D flow | S74 | §4.1,PDF8 | Not the full TRIDENT model |
| S74-C03 | Oil fits and calculations use distinct data representations and unit conventions | S74 | §3.2,Table3.4,PDF7 | Interpolation used in actual scaling |
| S74-C04 | Zero group distortion is a construction result,not output-error coverage | S74 | §4.2–4.3,PDF11–13 | Uncertain inputs/omitted physics remain |
| S74-C05 | Nu matching uses the same Dittus–Boelter correlation at matched Re/Pr | S74 | §4.5/Table4.10,PDF16–17 | Consistency,not independent physical validation |
| S74-C06 | Source-power and solid-time identities need normalization clarification | S74 | §4.2,PDF11 | Our mathematical checks; no silent correction |
| S74-C07 | Core diameters become hydraulic diameters without sufficient wetted-geometry justification | S74 | Tables2.1–2.3,4.7–4.9,PDF3–5,16 | Quantitative pipe-correlation transfer conditional |
| S74-C08 | Table4.2 provides nonunit scale ratios and mean-state matching | S74 | PDF10–12,Tables4.1–4.2 | Not an envelope-wide uncertainty analysis |
| S72-C01 | Goal-oriented physical calibration with nested discrepancy fitting is existing prior art | S72 | §4,PDF11–13,Algorithm1 | Not new merely to apply this structure |
| S72-C02 | Observation-level discrepancy does not directly propagate to unobserved QoIs | S72 | §2.5/PDF7;§6/PDF24–25 | Needs additional model/evidence |
| S72-C03 | Calibrated parameters depend on predictive objective and discrepancy family | S72 | §5.1/PDF15–18 | Demonstrations,not material-property identification |
| S72-C04 | Synthetic thermal challenge separates calibration and validation runs | S72 | Table6/PDF20;§5.3.2/PDF22 | 126validation values; no physical loop experiment |
| S72-C05 | Ordinary MLE has lower reported validation metric than both goal-oriented fits | S72 | Table8/PDF24 | Metric of h alone; normalization flag applies |
| S72-C06 | Printed Eq28 minimizes likelihood contrary to prose and surrounding MLE definitions | S72 | Eq28/PDF11 | Not evidence of actual solver behavior |
| S72-C07 | Printed Eq46 denominator1134 conflicts with2×63summed validation residuals | S72 | Eq46/PDF22;Table6/PDF20 | Our arithmetic; do not silently rescale reported results |
| S72-C08 | Quantile discrepancy objective is a fitted pointwise-Gaussian error quantity | S72 | Eq35–37/PDF12 | Not simultaneous/full-predictive empirical coverage |
| S72-C09 | Existence,uniqueness,stability and robust QoI weights remain unresolved by the article | S72 | §6/PDF24–25 | Author limitations,not automatically a feasible TRIDENT gap |
| S72-C10 | Small-dimensional nested optimization and discrepancy choice impose practical constraints | S72 | §4.3/PDF13 | No proven scalable loop implementation |
| S71-C01 | Nonlinear target-information experimental design is established prior art | S71 | §2/Eq10–14,PDF5 | Extracted arXivv2,not journal-equivalence claim |
| S71-C02 | Parameter and target EIG can rank designs differently | S71 | §4.1/Fig4–6,PDF12–15 | Synthetic numerical demonstrations |
| S71-C03 | Separate observation and target maps underpin the design utility | S71 | Eq1–5,PDF3–4 | Conditional independence and design-invariant target |
| S71-C04 | MCMC/KDE bias,bandwidth and cost affect design estimation | S71 | §3.2/PDF7–8;§5/PDF24–25 | EIG optimum not automatically robust |
| S71-C05 | Transport illustration uses prescribed convection and synthetic fields | S71 | Eq37–39,PDF19–20 | No buoyancy/conjugate loop validation |
| S71-C06 | DNN test split shuffles individual field points | S71 | §4.4,PDF20 | Does not establish held-out source-parameter independence |
| S71-C07 | Reported flux functional is diffusive with explicit−1to1integration | S71 | Eq42/PDF21 | Not total advective–diffusive flux;ROI wording differs |
| S71-C08 | Oracle chain initialization applies to simulated design utility samples | S71 | §3.2.1/PDF7 | Not an oracle for real experimental inference |
| S71-C09 | The flat target branch creates an atom smoothed by continuous KDE | S71 | Eq29/PDF12 | Our measure appraisal,not a reproduced bias estimate |
| S73-C01 | Continuous-time stochastic grey-box estimation already handles partial noisy discrete observations | S73 | Eq1–2,§2.1,PDF2/226 | Itô,state-independent diffusion |
| S73-C02 | EKF likelihood is a Gaussian/local-linear approximation | S73 | §2.2.1,PDF3/227 | Check nonlinear/sampling effects |
| S73-C03 | Continuous diffusion intensity and measurement covariance are distinct | S73 | Eq1–2,12,18,PDF2–3/226–227 | Units and identifiability still required |
| S73-C04 | Multiple-run fitting assumes stochastic independence | S73 | Eq33–36,PDF4/228 | Shared systematic effects can violate it |
| S73-C05 | Missing outputs require reduced-dimension likelihood treatment | S73 | Eq44–52,PDF5–6/229–230 | Not merely infinite observation variance |
| S73-C06 | Inverse-Hessian uncertainty is local/asymptotic | S73 | §2.5/Eq53,PDF6/230 | Not full predictive or model-form coverage |
| S73-C07 | A two-state thermal wall/heat-flow example is existing grey-box prior art | S73 | §4.2,PDF9/233 | Simulated wall,not circulating loop |
| S73-C08 | Comparison uses single simulation fits and optimizer-start reproducibility | S73 | §4.2.1–2,PDF9–12/233–236 | No extensive bias/variance MC or physical holdout |
| S29-C01 | Therminol-loop experiments plus3Dloss-inclusive CFD are close existing prior art | S29 | §2–5,PDF5–30 | Specific facility/operating cases |
| S29-C02 | Primary circulation is inferred from cooler enthalpy balance,not directly metered | S29 | Eq3/PDF9;§6/PDF30 | Shared temperature/flow/property ingredients |
| S29-C03 | Case power and cooling conditions change together | S29 | Table5/PDF17 | Cross-case trends not isolated power causality |
| S29-C04 | Mesh/time choices partly optimize experimental agreement | S29 | §4.1/PDF14–16 | No locked independent validation split |
| S29-C05 | Half-mesh-spread is used as a discretization sensitivity estimate | S29 | Eq18/PDF16 | Not demonstrated asymptotic/GCI uncertainty |
| S29-C06 | Loss-inclusive results improve selected temperature metrics but retain strong flow/dynamic mismatch | S29 | PDF21–23,Fig13–15 | Flow reference indirect |
| S29-C07 | Local temperature/velocity maps are CFDoutputs | S29 | Fig16–18/PDF24–26 | Not measured recirculation extent/causal HTC effect |
| S29-C08 | Tested Pr range is not established as molten-salt-matched | S29 | Fig22/PDF30;§7/PDF31 | Candidate oil selection differs from achieved similarity |
| S29-C09 | Quoted±5.22%flow uncertainty lacks a fully reproducible run-specific covariance budget | S29 | Fig21/PDF28;Table2/PDF9 | Not adopted as total uncertainty bound |
| S29-C10 | Separate experimental/energy-balance flow curves lack demonstrated independent provenance | S29 | Eq3/PDF9;Fig21/PDF28;§6/PDF30 | Curve agreement not two independent validations |
| S29-C11 | Current-pressure calibration prose/equations need ampere-versus-mA clarification | S29 | Eq1–2/PDF8 | Our endpoint/unit check,not a corrected calibration |
| S29-C12 | Loss descriptions and omitted geometry/power split confound mechanism attribution | S29 | §4.5/PDF20;§5/PDF21,25–28 | Plausible explanations,not isolated identified effects |
| S29-C13 | Some temperature-plot bars are explicitly model–experiment differences | S29 | Fig19/PDF26 | Not independent experimental uncertainty bars |
| S20-C01 | Conceptual internally heated D-loopCFD is established prior art | S20 | §2–4,PDF3–8 | Not a measured reactor/test-loop validation |
| S20-C02 | Steady first-order RANS may underresolve unsteady local flow | S20 | §2.2/PDF3 | Author limitation;not a universal closure rejection |
| S20-C03 | Methods substitute thorium-bearing salt properties for original MSRE salt | S20 | §2.2/PDF4 | Exact MSRE-fluid equivalence not established |
| S20-C04 | Fixed-temperature graphite removes heat while fluid boundaries are adiabatic | S20 | §2.2/PDF4 | Source/sink differs from external-heater pipe loop |
| S20-C05 | Mesh comparison targets a location-Ctemperature peak | S20 | §3.1/Table3,PDF4–5 | Not converged recirculation extent/total uncertainty |
| S20-C06 | Local recirculation and its change with power are numerical predictions | S20 | Fig10–15,PDF6–7 | No measured extent or isolated thermal-effect counterfactual |
| S20-C07 | Experimental assessment is future work | S20 | §4/PDF8 | No experimental validation claimed from this source |
| S20-C08 | Appendix distinguishes boundary-heated and proposed microwave-heated facilities | S20 | AppendixA/PDF8–9 | Source-era development plans,not available TRIDENT resources |
| S75-C01 | Embedded discrepancy can propagate through state to both observations and unobservedQoIs | S75 | Eq8a–c,PDF12 | Requires a valid,informed correction model |
| S75-C02 | Calibration,validation and predictive assessment answer distinct questions | S75 | §3,PDF16–23 | No generic sufficiency certificate |
| S75-C03 | Target-relevant untested directions and closure applicability determine credibility | S75 | §3.3.1–2,PDF20–22 | Depends on physical/modelknowledge |
| S75-C04 | Unknown omitted mechanisms can evade predictive assessment | S75 | §3.3.3/PDF23 | Framework does not eliminate unknownunknowns |
| S75-C05 | HPRDobservation plausibility is distinct from predictive adequacy/useful precision | S75 | Eq21/PDF19;§3.3/PDF20,23 | Not empiricalcoverage or decisiontolerance |
| S75-C06 | Demonstration uses synthetic oscillator data and information-state assumptions | S75 | §4/PDF23–38 | Not loopvalidation or universalmethodguarantee |
| S75-C07 | Example likelihood independently draws damping per observation | S75 | §4.2/PDF28 | Ensembleconstruction,not correlated thermal trajectory |
| S75-C08 | Second mass dataset is separately recalibrated during hypothesis assessment | S75 | PDF36–37,Fig6–7 | Not untouched finalholdout after all modeldevelopment |
| S75-C09 | Sourceversion has2014arXivstamp and2018compilationline | S75 | Firstpage | Finaljournal equivalence unverified |
| S76-C01 | Target-specific validation scenario/observable design is established priorart | S76 | Eq14–17/Algorithm3,PDF13–15 | Distinct from informationdesign/calibration |
| S76-C02 | Designmatches gradientsecondmoments,not modelerror | S76 | Eq14–17/PDF13–15;PDF20 | No guaranteed correctvalidationdecision |
| S76-C03 | Controls/sensors are certain and parameterlaw shared acrossscenarios | S76 | §2.3–2.5,PDF5–8;§5/PDF25 | ImportantTRIDENTuncertainties excluded |
| S76-C04 | Trace normalization handles outputscale but parametercoordinates still matter | S76 | Eq17/PDF15;§5/PDF25 | OurDᵀMDcoordinatecheck |
| S76-C05 | InitialRe-matched syntheticexample fails tochallenge wrongdragmodel | S76 | Fig5,PDF19–20 | Not a universalrejection ofsimilarityanalysis |
| S76-C06 | Transportexample usesfixedStokesvelocity and certaindiffusivity | S76 | §4.2/PDF20–24;AppendixA/PDF28 | Not naturalcirculation orexperimentalvalidation |
| S76-C07 | Appendicesprovideadjointgradients and demonstratenonunique/localdesignsolutions | S76 | AppendixB–C,PDF28–31 | Gradient/numericalverification stillneeded |
| S76-C08 | Targetmodelerrorpropagation and validitydecision are outside article scope | S76 | §2.7.2/PDF12;§5/PDF25 | Validationdesign doesnot certifyQoIaccuracy |
| S02-C01 | Formulation,propagation andsummarizing are separate uncertainty-evaluation activities | S02 | §5.1–5.3,PDF16/printed8 | Numerical propagation cannot fix bad model/input information |
| S02-C02 | Monte Carlo propagates samples of the specified joint inputdistribution | S02 | §5.9/Fig4,PDF22–23/14–15 | Not a complete model-formvalidation procedure |
| S02-C03 | Adaptive stabilization checks outputestimate,uncertainty andinterval endpoints | S02 | §7.9.4,PDF40/32 | Stochastic tolerance is not guaranteed;no universal trialcount |
| S31-C01 | Vector first-order uncertainty retains covariance via sensitivity matrix | S31 | §6.2.1/Eq3,PDF23/15 | Local linear approximation |
| S31-C02 | Implicit-model covariance requires a nonsingular output Jacobian | S31 | §6.3.1/Eq8–10,PDF25/17 | Directinverse discouraged;not an identifiabilityproof |
| S31-C03 | Joint coverage regions differ from separate marginal intervals | S31 | §6.5.1–2,PDF27–28/19–20 | Distribution/dimensional assumptions matter |
| S31-C04 | Vector Monte Carlo samples jointinputs and retains outputdependence | S31 | §7.1,PDF31–32/23–24 | Does not validate inputlaws or physicalmodel |
| S32-C01 | Measurand specification depends on use and can require spatial/temporal/reference conditions | S32 | §6,PDF13–15/5–7 | Does not supply TRIDENTsensor maps |
| S32-C02 | Known measurement effects belong in the model/uncertaintyassessment | S32 | §5.3–5.6,PDF11–12/3–4 | Missing information cannotbe repairednumerically |
| S32-C03 | Shared effects introduce correlation or require commoninputs | S32 | §10.5,PDF43–44/35–36 | No invented covariance magnitudes |
| S32-C04 | Adequacy and extrapolation are scoped to model/use/range | S32 | §12.1–2/PDF65/57;§13.2/PDF69/61 | Not universalreactor/ROMvalidation |
| S77-C01 | Three temperatures, four resistances and three capacities form a conductive RC model driven by power at node 1. | S77 | §2, Eqs1–10, PDF3–4/414–415 | Known power/ambient; no advection or buoyancy. R in K/W and C in J/K follow dimensionally from the balances. |
| S77-C02 | Full observation is identifiable; single T1 is not; T1 plus either other temperature supplies a minimum identifiable configuration in this model. | S77 | §§3.2–3.4, Eqs20–65, Table1, PDF5–7/416–418 | Minimal-realization/isomorphism assumptions; constant ambient in partial-observation analysis. Not a universal two-sensor rule. |
| S77-C03 | Different parameter sets produce the same observed T1 and different unobserved temperatures. | S77 | §4.2, Figures5–7, PDF8–9/419–420 | Constructed model example, not a measured flow field. |
| S77-C04 | Fitting uses moving-average-filtered experimental traces and constrained optimization. | S77 | §4.1, Eqs66–69, Table2, PDF7–8/418–419 | No separate untouched physical test or complete covariance budget is demonstrated in this article. |
| S77-C05 | State-isomorphism analysis addresses structural input–output equivalence under a specified model. | S77 | §3.1, Eqs11–19, PDF4–5/415–416 | The theorem's cited original is not thereby read; structural uniqueness does not establish practical precision or physical-model truth. |
| S78-C01 | Authors describe passive multiport RC identification using time constants and convex residue fitting. | S78 | Publisher abstract; DOI metadata | A claimed method in an abstract, not independently appraised passivity conditions or performance. |
| SYN-C01 | Conjugate storage,source pathways and transport are established loop physics;importance remains target/regime-specific. | S50,S52,S65,S66 | S50 §3/PDF3/515;S52 Eqs7–23/PDF5–7;S65 §4/PDF8–10;S66 Eqs41/46/PDF6/416 | No common universal mechanism ranking or new TRIDENT result. |
| SYN-C02 | A restricted exact/asymptotic circulation reduction does not ensure finite-time observation or extrema reconstruction. | S59,S18 | S59 Thm3.6/Eq3.12,PDF12–14/1083–1085;S18 Eqs24–36/PDF6–7 | Different forcing/coupling assumptions;not a contradiction between originals. |
| SYN-C03 | Observation-dependent identifiability and stable aggregate predictions despite internal ambiguity already have close thermal prior work. | S23,S68,S70,S77 | S23 Eq10/PDF4/1926;S68 §4.4/PDF7/57;S70 Figs5–7/PDF13–17/456–460;S77 §§3.2–3.4/PDF5–7/416–418 | No new sensor rule,physical property recovery or project supported-combination result established. |
| SYN-C04 | Observation-level and embedded discrepancy have different propagation scopes;their reported restrictions are compatible. | S72,S75 | S72 §2.5/PDF7;S75 Eq8/PDF12 | Useful unobserved-target constraint still requires credible model and informative evidence. |
| SYN-C05 | Parameter information,target information,model discrimination and validation relevance are distinct design objectives. | S07,S71,S76 | S71 Eqs10–14/PDF5;S76 Eqs14–17/PDF13–15;S07 dossier | They do not imply the same ranking,predictive error or decision value. |
| SYN-C06 | MSR transfer depends on circuit,source/solid/boundary conditions and target,not a high-Pr or matched-correlation label. | S13,S56,S64,S66,S74,S29 | S13 §I.B/PDF6;S64 Eqs8–10/PDF6/349;S66 §6.2/PDF12–14;S74 Table4.10/PDF17;S29 Fig22/PDF30 | No actual quantitative TRIDENT-to-reactor scaling demonstrated. |
| SYN-C07 | Indirect/shared thermal agreement does not independently establish local recirculation extent or its causal thermal effect. | S19,S20,S29 | S19-C01–C04;S20 §3–4/PDF6–8;S29 Eq3/PDF9 and Fig21/PDF28 | No claim that all computed contours are false;local evidence remains gated. |
| SYN-C08 | Propagation under a specified uncertainty model,local parameter precision and independently assessed predictive credibility are distinct. | S02,S31,S32,S73,S75 | S02 §5.1–5.3/PDF16/8;S31 §6.5/PDF27–28/19–20;S73 Eq53/PDF6/230;S75 §3/PDF16–23 | No calibrated predictive coverage or rare-event reliability inferred for TRIDENT. |
| SYN-C09 | A new application or combination of existing frameworks is not sufficient evidence of methodological/theoretical novelty. | S23,S26,S59,S66,S71,S72,S73,S75,S76,S77 | Cross-source synthesis §4 closest-prior comparison and individual original locators | Analyst novelty boundary,not an exhaustive literature-gap proof;S78 full method remains unread. |
| SYN-C10 | Supported predictions plus retained-physics adequacy is a provisionally feasible no-CFD core,conditional on a nontrivial additional result and assessment evidence. | S23,S59,S66,S68,S70,S75,S77 | Critical_Cross_Source_Synthesis_2026-10-21.md §§6–7;PF01 project contract | Research recommendation,not established gap,selected thesis or guaranteed contribution. |
| SYN-D01 | For an assumed indistinguishable set,a scalar target spread above2ε precludes a uniformlyε-accurate point estimate;at regular points differentiable dependence of target on observations requires ker(JF)⊆ker(Jq). | Analyst derivation;related S23,S70,S77 | Critical_Cross_Source_Synthesis_2026-10-21.md §5 analytical checks | Elementary analyst deductions,not novel theory or computed TRIDENT bounds;Jacobian condition is first-order with nuisance columns and does not certify exact or singular-point identifiability. |
| SYN-D02 | Eliminating a positive linear wall state yields a frequency-dependent heat-flow admittance with distinct steady and fast limits. | Analyst derivation;related S66 | Critical_Cross_Source_Synthesis_2026-10-21.md §5 analytical checks | Conventional analyst derivation for fixed coefficients,zero initial perturbations,fixed ambient;not full-loop stability or target-error bound. |
| S78-C02 | Step-response impedance and impulse transfer are distinguished. | S78 | §2/Eqs1–8, PDF3 | Linear diffusion/zero-perturbation response; our units follow dimensionally. |
| S78-C03 | Positive time constants and PSD coefficient matrices define the fitted response family. | S78 | Eqs15–19, PDF5 | Restricted passive RC class, not arbitrary loop dynamics. |
| S78-C04 | Inner coefficient optimization is convex at fixed time constants; outer relocation is nonlinear. | S78 | Eqs19–31, PDF5–7 | No full nonconvex/global-optimum or parameter-uniqueness proof inferred. |
| S78-C05 | Foster realization introduces equivalent RC elements and ideal multiport transformers. | S78 | §4/Fig3, PDF7–8 | Not a unique material/geometry reconstruction. |
| S78-C06 | Demonstrations fit two FEM and one semianalytical thermal-response datasets. | S78 | §5, PDF8–11 | No independent physical/noise-coverage assessment demonstrated. |
| S78-C07 | Table1 improves displayed off-diagonal errors but worsens all six displayed diagonal errors in each first case. | S78 | Table1/PDF10; discussion/PDF9 | Our rowwise table audit, not a recomputed global comparison. |
| S78-C08 | Eq4's integration-variable notation and Eq11's exported general passivity reading require qualification. | S78 | PDF3–4 | Analyst limiting-case checks; not evidence of executed-code failure. |
| S78-C09 | Uploaded copy includes the post-publication Eq12 correction. | S78 | Footnote/PDF4 | Final issue2018/online2017 identity retained. |
