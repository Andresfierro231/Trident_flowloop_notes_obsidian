# S39 — Thermal Development Study in Molten Salt Natural Circulation

Audit date: 2026-10-20. Thomas Scott Carson, Texas A&M University, Nuclear Engineering PhD dissertation, supplied author copy titled **December 2026**. That date is later than this audit. Repository deposit, degree award, final approval and persistent identifier are **not verified**. Cite as the supplied dissertation manuscript until final metadata are confirmed. It is not Ethan's separate thesis (S35).

The supplied PDF has 171 pages: title at PDF1, Roman-numbered front matter PDF2–12, body printed1–159 at PDF13–171. Thus **printed page = PDF page −12** throughout the Arabic-numbered body, including references and Appendix A. The TOC lists Appendix A starting at printed156 and its last listed figure at158; actual appendix text continues through printed159/PDF171. All supplied text, tables, captions, references and appendix text were read. Selected equation pages and figures were visually checked; the graphs were not digitized, raw data/code were not supplied, and no independent recalculation of reported spectra or regressions was possible. No apparent missing interior pages or unreadable selected equation images; final-version completeness remains unverified.

## Problem, contribution and prior evidence

The manuscript asks when sparse temperature measurements in a high-Prandtl molten-salt loop can legitimately support inference of circulation, buoyancy or heat transfer. It adds distributed fiber temperature measurements and uses planar PIV, POD and spectral analyses to interrogate development and downstream bend effects. It also compares temperature-driven and heat-input/momentum-based flow estimates. It explicitly presents the Reynolds correlation as a feasibility/screening exercise rather than a validated flowmeter or universal closure (printed132–148/PDF144–160).

The defensible original observations are spatial and temporal temperature nonuniformity along the fiber path, differences from sparse-probe interpolation, asymmetric planar velocity fields, and failure of the tested heat disturbance to behave as a trackable passive marker. Attribution to a unique mechanism, quantitative three-dimensional Dean vortices, a complete buoyancy field, and a universal inability to infer flow from temperature are stronger than these observations establish.

Prior work used for positioning includes S09/S36 scaling, S37/S38 experiments, S16 SAM comparison, Britsch et al.'s FLiBe loop, Headley’s FLiNaK dissertation, DYNASTY/CIET, and the Everts et al. developing mixed-convection study (literature survey printed7–12/PDF19–24; references printed149–155/PDF161–167). Original findings in those cited sources are not newly verified by this dissertation. Several bibliography entries are incomplete or questionable; check originals before proposal use. In particular, §2.1's broad MSRE description must be checked against original operation/design reports, and §3.1's Pr/Re/Ra matching statement does not establish complete reactor similarity.

## Facility, states, inputs and observations

Chapter3 (printed13–22/PDF25–34) describes the TAMU atmospheric-pressure, pump-free rectangular loop with inclined horizontal sections, nominal 0.914 m legs and roughly 2.4 cm primary ID. HITEC is specified as NaNO3/NaNO2/KNO3, 7/49/44 mol%. An approximately 18 cm quartz riser window permits PIV; wall electrical heating and an air-cooled cold leg establish circulation. The geometry is a research apparatus, with no verified scaling target to a particular MSR primary loop, decay-heat loop or drain tank.

Fiber temperature is measured inside a 1.59 mm stainless sheath. Heated-leg installation contacts the wall locally; the vertical installation replaces the quartz section with insulated steel. OFDTS is a Luna ODiSI-B with 2.6 mm spatial resolution, downsampled to 2.5 Hz; the uncertainty discussion covers 150–350°C (printed45/PDF57). This is not proof that all reported campaigns cover that entire temperature range. Main measurements include internal and wall thermocouples, heater settings, air cooling and planar PIV; the main text does not provide a complete run-by-run table of powers, boundary conditions, initial conditions and calibration records.

Two cameras sample the center plane: full-field 250 fps, 512×800; near-wall 1,000 fps, 1024×1024, with a nominal 1 mm light sheet and 50 μm silver-coated hollow glass spheres (printed16–25/PDF28–37). Particle Stokes estimates below0.1 support response to the selected flow timescale, not resolution of unmeasured three-dimensional velocities or absence of settling/optical errors.

The Chapter6 representative PIV case is 184.5°C, Re127, Pr45.2, Gr6.405×10^8, Ra2.896×10^10, Gz148.4, De89.8 (Table6.1 printed94/PDF106). These are **reported values**, not harmonized against S37/S38 values with different reference scales. Gr/Ra depend strongly on length and temperature definitions; do not compare their magnitudes across papers before resolving those conventions. The value Ra/Gr≈45.2 is internally consistent. The vertical-fiber heat disturbance is approximately1 kW for20 min near TW6 (printed73–74/PDF85–86); it changes the driving system, not just a passive tracer concentration.

## Reported equations and implementation audit

### Observations and averaging

Printed26/PDF38, Eqs4.5–4.7 define signed axial area-average velocity and approximate it by weighting center-plane column velocities with chord length \(b(x)=2\sqrt{R^2-x^2}\). This assumes the measured center-plane value is representative across the unmeasured chord; it does not reconstruct that dimension. The unweighted discrete sum also assumes uniform x spacing. **Analyst limiting-case check:** for exactly axisymmetric parabolic \(v(r)=v_{max}(1-r^2/R^2)\), extending the center-plane value unchanged along each chord gives \(3v_{max}/4\), whereas the true area mean is \(v_{max}/2\). Thus the method can overestimate even this simple reference case by50%. This is an audit of the reconstruction assumption, not a claim that the measured flow is parabolic or that actual error is50%.

The uncertainty derivation then switches to speed magnitude and radial annuli (Eqs4.29–4.32, printed43/PDF55), conflicting with the signed-axial/chord reconstruction. A net circulation estimate must use signed axial velocity; speed counts transverse and reverse motion positively. Correlated calibration/timing/optical errors do not disappear under independent annulus RSS. Diameters and reconstruction uncertainty must accompany the glass-to-steel area conversion (Eqs4.33–4.34, printed44/PDF56).

Distinguish \(T_{probe}\), cross-sectional area-average temperature relevant to Boussinesq density head, and the velocity-weighted mixing-cup temperature relevant to enthalpy transport. The dissertation often calls point temperatures “bulk”; that label does not establish equality. Smoothing along a fiber does not turn its spatial sampling into a cross-sectional enthalpy average.

### Thermal development

Gz=Re Pr D/x and Lth≈0.05 Re Pr D imply x/Lth=20/Gz (Eqs5.1–5.9, printed78–83/PDF90–95). These are dimensionally consistent screening estimates conditional on canonical straight-pipe laminar entry assumptions. Table5.1 (printed81/PDF93) is an interpretation classification, not an experimentally calibrated sensor-bias law. **Thermally fully developed does not mean radially uniform**, especially with continuing wall heat flux; no Gz threshold alone proves a centerline probe equals a bulk mean. A bend can also violate or reset the assumptions. Chapter5 uses Chapter8's approximate Re in this screening, so these are not independent validation results.

The local wall-contact fit uses an exponential relaxation and \(\delta_T=\lambda\cos\theta\), with theta described as the fiber angle to the wall (printed61–62/PDF73–74). For an angle measured to the wall tangent, a wall-normal projection would use sine; cosine would apply for an angle to the normal. **The angle convention must be resolved**, rather than silently altered. The comparison \(\delta_T=k/h\) is an effective conductive-resistance length, not a direct boundary-layer measurement. Both methods use model assumptions and related temperature information; agreement does not independently validate a geometric boundary-layer thickness.

### Momentum and scaling

Printed123–125/PDF135–137, Eqs7.13–7.22 give \(\Delta P_b=\rho g\beta\Delta T H\) and positive-flow Darcy resistance

\[
\Delta P_b=32\mu L U/D^2+\rho K U^2/2.
\]

For specified positive deltaP and K>0 the reported quadratic root is dimensionally consistent. **Analyst implementation qualification:** use a numerically stable root and the limit U=deltaP D²/(32μL) as K→0; use signed \(U|U|\) and proper buoyancy sign for reversal. The two-temperature/effective-height buoyancy approximation is not the full loop integral.

Eq7.24 (printed127/PDF139) couples heat input to the loop momentum balance and yields a cube-root expression only when its effective hydraulic resistance definition is retained; laminar f depends on flow, so it is not automatically a fixed-resistance explicit solution. Its derivation assumes ideal heater/cooler geometry and adiabatic connecting sections. Net fluid heat is required rather than unqualified electrical setting.

Chapter8 contains consequential printed inconsistencies, visually checked against PDF148/150/155:

| Locator | Reported issue | Audit / consequence |
|---|---|---|
| Eq8.7, printed136/PDF148 | Positive sign in density integral | Substituting Eq8.5 into the closed integral with the same z convention gives **minus** rho0 beta times the T integral. Eq8.8 uses the conventional buoyancy sign; trace the derivation explicitly. |
| Eq8.10, printed136/PDF148 | Resistance denominator Di Ai | Eq8.9 has Di Ai². Setting time derivative to zero cannot remove an area factor; printed Eq8.10 is dimensionally inconsistent. |
| Eq8.15, printed137/PDF149 | Flow power omega^(2−2b) | A friction law f∝Re^-b gives a signed positive-branch resistance proportional to omega^(2−b); verify the complete nondimensionalization rather than copying. |
| Eqs8.17–8.18, printed138/PDF150 | gamma sums li/Ai; deltaTr=Qh H/(A μ cp) | With stated dimensional Ai and Qh in W, gamma is not dimensionless and deltaTr has units K·m. Missing normalization or conflicting symbol definition must be resolved against the original scaling source. |
| Eqs8.20–8.22 vs §8.3, printed138/143 (PDF150/155) | r=1/(3−b) but prose says laminar≈1/3, turbulent≈1/2 | The stated law gives laminar b=1 → r=1/2; Blasius b=0.25 → r≈0.364. Constant friction b=0 gives1/3. The regime interpretation of fitted r=.376 does not follow from the prose. |

S09/S36 provide the original equation definitions; they also have limits and one recorded algebra ambiguity. Do not “repair” this manuscript into an authoritative independent derivation or use fitted C,r as material properties.

## Results, uncertainty and validation limits

**Heated leg, Chapter5:** fiber-path temperatures depart from a two-probe linear interpolation, changing inferred local film temperatures and Nu (Figs5.3–5.9, printed54–61/PDF66–73). The wall-contact segment around x=.01–.08m is excised and replaced with interpolation (printed58/PDF70). Small/large smoothing windows 4.4/18.4cm change retained structures (printed55–58/PDF67–70). Appendix A examines second-order SG windows about2–26cm; derivative changes plateau near18–22cm, with nonzero relative change about4.5–5.5% (printed156–159/PDF168–171). This is smoothing sensitivity, not proof of true bulk temperature or physical convergence of an underlying cross-sectional solution.

**Near-wall estimate:** effective millimeter-order lengths and approximately10% agreement between exponential/projection and k/h estimates are reported (printed63–65/PDF75–77). The manuscript explicitly limits these to model-based estimates. No exact fitted lambda, angle, fit covariance or independent radial temperature traverse is tabulated. Do not convert “a few millimeters” into a verified thermal-boundary-layer thickness.

**Riser:** nonmonotonic fiber temperature and gradient reversals persist in insulated steel, with comparison to sparse thermocouples and a heat-step response (Figs5.12–5.15, printed67–76/PDF79–88). This supports a nonuniform measured thermal field. Probe offsets, sheath conduction/contact, reference drift and the changed steel-versus-quartz boundary must be considered before uniquely attributing differences to curvature or applying them to a PIV campaign. Velocity and fiber measurements are not a simultaneous full three-dimensional velocity–temperature field.

**Mixing/spectra, Chapter6:** planar fields exhibit skewed profiles and weak unsteadiness. Dean and Kelvin–Helmholtz explanations are interpretations, not directly resolved transverse vortex pairs. The claimed cross-method frequency agreement needs checking: POD PSD text reports about.25Hz for modes1/2 and .45–.5Hz for3/4 (printed100–102/PDF112–114), CWT text reports2.13Hz and1.03Hz (printed102–104/PDF114–116), while SPOD examples use .69/1.381/2.071Hz (printed106/PDF118). These cannot simply be declared identical peaks. §4.3.2 uses256-frame SPOD blocks (printed32/PDF44); the effective snapshot interval/decimation must be reconciled with the much lower displayed frequencies. Zero-padding does not improve independent frequency resolution. The PSD normalization in printed35/PDF47 is squared FFT amplitude/N² without spectral-bin width and without the normal one-sided interior-bin doubling; treat plotted amplitudes as a spectrum until code confirms PSD units. A −5/3 reference line and modal pairing do not prove turbulence, a particular instability, or a heat-transfer enhancement.

**Thermal velocimetry, Chapter7:** the forced response fails the coherent-marker criterion. A representative lag fit returns8.97×10^-3m/s, R²=.87 and median adjacent correlation.99, but a ridge-based composite score.23 and near-synchronous response lead the author to reject it (printed117–120/PDF129–132, Fig7.3/Table7.1). The score is a diagnostic heuristic, not a calibrated probability. This is evidence against this forcing/analysis/configuration, not all pulse, cross-correlation or temperature-based flow inference methods.

**Uncertainty:** Table4.1 (printed48/PDF60) gives OFDTS1σ2.63°C/1.47°C and ±2σ5.26°C/2.94°C for TC-reference/tare installations. These include assumed1°C humidity contribution and assumed negligible strain (printed45–47/PDF57–59). Manufacturer accuracy bounds are treated as standard uncertainties without an explicit distribution conversion; independence, spatial covariance and sheath/sampling bias remain unresolved. Table4.2 gives rho2%, mu16%, cp5%, k5% (printed49/PDF61); properties share temperature inputs, so independent propagation misses covariance. Eq4.44 omits a diameter term while Eq4.42 includes one; Eq4.46's n−1 degrees of freedom and simple-linear mean-band formula require matching the actual regression model, not blanket use for nonlinear/multiparameter fits.

Table7.2 (printed129/PDF141) reports mean temperature-propagated uncertainties28.62%,23.07%,25.69%,1.31% for sensible heat, buoyancy+Darcy, fully developed laminar and integrated momentum estimates. The text correctly says these exclude heat input, losses, geometry, hydraulic resistance and model-form uncertainty; the smallest band is not the most accurate flow estimate (printed129–130/PDF141–142).

**Reynolds feasibility fit:** §8.2–8.3 (printed139–145/PDF151–157) reports empirical Re≈4.354 Tave−762.36 (R²=.712), analytical trend3.4562 Tave−558.37 (R²=.948), and fitted scaling C=1.004,r=.376 (R²=.537). The temperature unit and exact fitting dataset must remain attached to coefficients; the paper’s average-temperature context is Celsius. The reported mean absolute error .342 lacks a clear normalization here and must not be interpreted as a verified absolute-Re error. A smoother analytical curve’s larger R² against its own temperature dependence is not evidence it is more accurate. No genuinely withheld run/geometry/fluid validation is demonstrated. Shared rho/mu temperature inputs generate correlation between inferred and PIV-based Re. Deviations cannot be assigned solely to experimental variability without evaluating model error.

## TRIDENT relevance and skeptical contribution test

**Direct methodological relevance:** use sensor-specific forward observation operators; test which combinations of conductance/storage/flow are identifiable; distinguish inferred flow from measured flow and conditional temperature reconstruction from autonomous prediction. **Conditional physical transfer:** high-Pr development and bend distortion are useful mechanisms to test after fluid, geometry, boundary and regime matching. **Analogy:** this TAMU salt facility does not automatically represent TRIDENT glycol VCU or HITEC ACU, much less a fueled MSR. **Incompatibility:** it contains no neutronic feedback, distributed fission/decay heating, reactor-scale core/exchanger network, chemistry or radiation validation of those effects.

The manuscript is strong prior work against claiming “first to recognize sparse-temperature inference limitations” or “first to relate high-Pr development and bend mixing to inferred closures.” Its unresolved equations, averaging conventions and validation uncertainty create **questions**, not automatically publishable gaps. A feasible contribution could establish observation-consistent reduced model discrimination, identifiable parameter groups and honest out-of-condition QoI intervals using existing sensors. Quantifying local recirculation extent or its causal heat-transfer effect remains gated on resolved data/validated CFD; no such TRIDENT capability is assumed.

Implementation inputs should be geometry, property laws, electrical delivery/thermal losses, ambient and secondary cooling; states could include wall/fluid storage and signed circulation. Outputs must distinguish centerline probes, wall temperatures, fluid averages and extrema. A simple RC network cannot substitute for directional transport; a global one-flow model cannot claim resolved vortex extent. Keep the original mathematical formulations separate from the analyst checks above and verify against S09/S36 before coding.

## Coverage and readiness

| Section/appendix (printed; PDF) | Relevance | Status / limits |
|---|---|---|
| Front/title, PDF1–12 | Identity/version/index | Inspected; final deposit not verified |
| Ch1–2,1–12;13–24 | Motivation and prior work | Read/extracted; cited originals remain leads |
| Ch3,13–22;25–34 | Geometry, campaigns, instruments | Read/extracted; complete run manifest absent |
| §4.1–4.2,23–28;35–40 | Observation/averaging and groups | Read/extracted; averaging page visually checked |
| §4.3–4.4,29–40;41–52 | POD/SPOD/PSD/CWT/STFT | Read/extracted; selected result pages checked; code/timing not verified |
| §4.5,41–50;53–62 | Measurement/derived UQ | Read/extracted; selected printed equations checked |
| Ch5,51–85;63–97 | Temperature development/inference | Read/extracted; no graph digitization, radial profile not directly measured |
| Ch6,86–108;98–120 | Flow structure/spectral claims | Read/extracted; reported spectral agreement unresolved |
| Ch7,109–131;121–143 | Velocity inference and UQ limits | Read/extracted; no independent flow calibration |
| Ch8,132–145;144–157 | Reduced scaling and fit | Read/extracted; major equation checks recorded |
| Ch9,146–148;158–160 | Scope/conclusions | Read/extracted |
| References149–155;161–167 | Primary-source leads | Inspected; bibliographic errors not propagated as verified metadata |
| AppendixA156–159;168–171 | Filtering sensitivity | Read/extracted; no raw-data reproduction |
| Raw fields, scripts, instrument certificates | Reproducibility | Not supplied; not read/verified |

Ready for **qualified qualitative motivation, observation-model requirements and a prior-work/limitations synthesis**. Not ready to supply unqualified predictive closures, universal Dean/Graetz thresholds, quantitative recirculation extent/heat effects, verified spectral mechanisms, or implementation equations without the recorded corrections and source reconciliation.

## Claim-to-evidence ledger

| Claim ID | Evidence claim and type | Locator | Limit |
|---|---|---|---|
| S39-C01 | Supplied manuscript dated Dec2026; final status unverified (identity finding) | PDF1 | Do not present as already awarded/deposited |
| S39-C02 | Fiber temperatures differ from sparse interpolation (original observation) | printed54–61/PDF66–73,Figs5.3–5.9 | Fiber path is not a cross-sectional bulk measurement |
| S39-C03 | Near-wall scale is fitted/model-based (reported qualification) | printed59–65/PDF71–77,§5.2 | No directly measured radial BL thickness |
| S39-C04 | Insulated riser retains measured nonmonotonic thermal structure (original observation) | printed66–77/PDF78–89,Figs5.12–5.15 | Mechanism/offset/configuration confounders |
| S39-C05 | Chord reconstruction can fail a parabolic-flow limiting test (analyst derivation) | printed26/PDF38,Eqs4.5–4.7 | Does not measure actual case error |
| S39-C06 | Tested heat disturbance fails defensible time-of-flight inference (original result) | printed109–120/PDF121–132 | For this setup/forcing; not universal impossibility |
| S39-C07 | Smallest reported flow uncertainty is temperature-only (reported limit) | printed129–130/PDF141–142,Table7.2 | Not total uncertainty or validation |
| S39-C08 | Scaling derivation has sign, area, dimensional and exponent conflicts (equation audit) | printed136–143/PDF148–155,Eqs8.7–8.22,§8.3 | Verify originals/code before implementation |
| S39-C09 | PSD/CWT/SPOD textual frequencies do not establish identical peaks (audit) | printed100–106/PDF112–118 | Timebase/code/figures need reconciliation |
| S39-C10 | Re fit is a screening feasibility test (original fit and stated limit) | printed143–145/PDF155–157,Fig8.4 | No withheld transfer validation |

## Next acquisitions

Confirm the manuscript's final revision/deposit and, if possible, obtain the run-condition table, PIV/fiber processing definitions and spectral timebase. A revision may resolve printed conflicts; retain this supplied copy's hash for reproducibility. Priority originals: Britsch2019 for FLiBe inference; Headley2021 for earlier high-temperature diagnostics; Everts2023 DOI10.1016/j.ijthermalsci.2023.108178 for the actual heated horizontal mixed-convection assumptions; INL2013 property report DOI10.2172/1086824 for property conventions/ranges; original MSRE operational reports for reactor motivation. These are leads, not findings inferred from citations alone.
