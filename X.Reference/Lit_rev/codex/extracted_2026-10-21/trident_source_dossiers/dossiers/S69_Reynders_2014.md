# S69 — Reynders, Diriken & Saelens (2014): input/observation quality and thermal models

Extraction date: 2026-10-20. **Scoped ready** for thermal identification, observation design and contribution-boundary synthesis. Methodological cross-domain evidence, not MSR validation. No numerical reproduction.

## Identity, completeness and provenance

G. Reynders, J. Diriken, D. Saelens. *Quality of grey-box models and identified parameters as function of the accuracy of input and observation signals.* Energy and Buildings82,263–274 (2014). DOI https://doi.org/10.1016/j.enbuild.2014.07.025. Uploaded12-page typeset publisher article matches primary publisher metadata independently checked2026-10-20. Printed page = PDF page+262; no cover. Complete article through references [32] on PDF12/274; no appendices in the supplied article. Text and equations readable; selected equation/figure pages rendered, with all pages visually surveyed. External simulation models/data and CTSM source were not supplied or executed. Supplement availability not independently established.

## Problem, prior work and established contribution

Engineering motivation is building demand-side management and model-predictive control. The authors compare prediction usefulness with recovery of physical thermal properties, varying model order, available signals and data periods. Original evidence is virtual measurements from two detailed IDEAS/Modelica dwelling simulations, not physical experiments. The study explicitly allows a low-order model to predict well while poorly estimating physical parameters (PDF5–7/267–269, Figures3–6). It also exposes incomplete-heating-input and boundary-signal problems that are directly relevant as **methodological cautions** for TRIDENT.

Cited foundations: S08 Bacher–Madsen2011; Madsen2007 time-series theory; Andersen–Madsen–Hansen2000 SDE heat dynamics; Kristensen–Madsen2003 CTSM; Xu–Wang2008 simplification. The IDEAS generator and heat-pump models refer to Baetens2012 and Reynders2013. Their reported results are not independent checks of those originals.

## Physical setup, data, observations and uncertainty

PDF2–3/264–265,Table1,§2: two single-zone Belgian detached dwellings, uninsulated pre1945 (SFHD1) and insulated post2005 (SFHD5). Volumes766/741m³; air–water heat-pump/radiator system nominal48/17.5kW; ventilation383/370m³/h with84% constant recovery; room setpoint20°C and setback16°C. Uccle weather; uniform zone air and component surfaces,1D component conduction; constant ventilation/infiltration; furniture represented through fivefold air capacity. This is an assumed synthetic building, not an actual instrumented loop; there are no relevant fluid Re/Pr/Ri ranges or direct-flow measurements. Envelope dimensions, areas, U-values, areal capacities and glazing gains are in Table1. They do not specify TRIDENT materials or uncertainties.

Generator boundary resolution1min and output5min, resampled10min for identification (§§2,4/PDF3). Variable solver time step; no reproduced convergence or generator V&V. Table2/PDF4 gives five overlapping training windows:14–21Feb,14–28Feb,1–28Feb,14Apr–30Jun,15Mar–30Jun. Shorter/low-heating windows change excitation as well as sample count. These are not independent replicated experiments.

Inputs (§4/PDF3–4): outdoor/ground temperatures, solar/internal/radiator gains. Ground represented as constant12°C rather than the detailed ground history. **Radiator heat delivered to the room** is prescribed, so upstream heater dynamics are bypassed; this is explicitly distinguished from measured energy consumption. Identified storage and source allocation can depend on heat-emission system (PDF4/266). TRIDENT electrical power is likewise not automatically net heat deposited into the modeled salt/pipe domain; that last statement is our inference, not their reactor finding.

Observed outputs: room air temperature; optional heat fluxes to component groups. Third-order observation combines envelope/roof/floor fluxes by an area-weighted average; orders4–5 separate additional components (§4/PDF4). No real flux meters were installed. Adding these virtual observations changes identifiability and practical feasibility; available TRIDENT temperature data alone do not supply them.

§5.2/Table3/PDF8–9: A effective solar/effective internal gains; B horizontal solar/effective internal; C oriented vertical solar/effective internal; D effective solar/domestic electricity; E oriented solar/domestic electricity; F effective solar/no internal input. They compare realistic input proxies, not only additive measurement noise.

§5.3/PDF10/272: biased scenario uses temperature noise mean0.25°C, SD0.15°C; flux mean+10% of simulated value, relative SD10%. Other channels use unbiased noise as in the preceding scenario, whose full channel-by-channel amplitudes and realizations are not specified in the inspected article. Confidence bands increase with noise; no repeated-noise coverage study is established. The introduction calls biased noise 'colored'; **nonzero mean does not by itself establish temporal correlation**, so that terminology must not be imported into our covariance model.

## Governing/reduced mathematics and implementation

§3/PDF3/265 reports Eq(1) as dX(t)=A(θ)X(t)+B(θ)U(t)+σ(θ)dω. **The printed drift terms omit dt.** A dimensionally conventional Itô expression is our interpretation, not verbatim reported mathematics:

\[
dX=[A(\theta)X+B(\theta)U]dt+\sigma(\theta)dW,
\qquad Y=C(\theta)X+D(\theta)U+\epsilon .
\]

The output relation is their Eq(2). Do not implement Eq(1) literally without a time convention. For temperature states, A has1/s units, B maps temperature/power inputs to K/s, and σ has K/√s for standard Wiener increments. Units differ by channel; the paper does not specify one universal B unit. Measurement and process noise have different roles; no complete covariance specification appears in these two equations.

Figure1/PDF4/266 and §3: order1 lumps all mass; order2 separates air and mass; order3 separates envelope, internal walls/floors and air; order4 adds ground-floor state/boundary; order5 adds roof state. Heat/source distribution factors are fitted and held constant throughout the year. RC edges are reciprocal conduction; capacities storage. No momentum, buoyancy, axial advection or recirculation closure is present. CTSM/R estimates parameters by maximum likelihood; nonlinear capability is mentioned but nonlinear property effects are outside this study. Full expanded matrices, optimizer bounds/initializations, covariance conventions and numerical integration settings are not given here. Thus Figure1 supports a model-class comparison but not a fully specified reproduction.

Our implementation consequence: declare an observation operator and heat-source boundary before calibration. A flux channel in W/m² cannot be substituted for a power in W without area integration, and an area-weighted combined flux requires a matching observation map. With equal connected temperatures, deterministic conduction vanishes; a constant temperature is not preserved if an external source remains. These are dimensional/limiting-case checks, not extra findings claimed by the authors.

## Results and critical appraisal

- §5.1/PDF5–7/267–269,Figures3–6: air-temperature-only fits may support prediction but yield broad physical-parameter uncertainty; higher-order fits encounter overfitting/convergence problems without flux observations. Increasing order from4 to5 worsens long-horizon performance for the uninsulated case. Order4/5 are subsequently used for uninsulated/insulated cases, respectively. This is not proof that one topology is optimal for every thermal system.
- §5.1/PDF6/268 reports uninsulated order4 envelope UA586–597W/K against expected560W/K. The authors attribute compensation to lumping roof/wall storage. This is a proposed mechanistic explanation, not an isolated experiment proving the cause.
- §5.1/PDF7/269: ventilation and massless-window transmission cannot be separated under their model; the reference 'ventilation' coefficient is adjusted to include window loss. Reference capacity is also adjusted to effective storage inside insulation; Figure7 illustrates frequency/excitation-dependent active depth. Fitted storage is not an automatic material heat capacity measurement.
- §5.2/PDF9–10/271–272: input proxies can retain temperature accuracy while source-allocation parameters differ from physical counterparts. Reported effective solar gA10.3–10.8m² versus30.6m² uses their stated0.75×40.8m² reference. **Table1/PDF2 gives different glazing areas/solar factors for the two buildings**; case attribution of this scalar comparison is insufficiently explicit to treat it as a verified universal benchmark. Retain the authors' comparison with this caveat, not as a TRIDENT percentage.
- §5.3/PDF10/272,Figures8–11: the biased case does not markedly change plotted temperature RMSE relative to unbiased noise but does change fitted coefficients. They report UA+4% and ventilation coefficient−4% relative to the unbiased case, explicitly depending on bias and signal-to-noise ratio. These are not general sensor tolerances. Noise also shifts a problematic order5 fit from a different local minimum, so 'noise never changes estimates' would contradict the detailed results.
- §6/PDF10–11/272–273,Figures12–15: temperature and cumulative/instantaneous demand simulations compare reduced and detailed models; winter agreement is better than some shoulder-season predictions. Source underestimation and heat-transfer overestimation produce systematic errors. Do not turn qualitative 'acceptable' agreement into a numeric validation threshold.

Validation limits: prediction horizons1step/2days/1week and free simulations are useful distinctions. The paper does not unambiguously document a locked, nonoverlapping calibration/model-selection/test partition for every reported comparison. Several training windows overlap; the full-year exercise shares the same synthetic generator and includes training-season periods. Treat results as synthetic assessment and horizon sensitivity, not independent experimental validation. RMSE is not a calibrated predictive interval; parameter95% bands are not posterior predictive coverage. The model's optimizer convergence, discrepancy and input-error likelihood are not fully audited by this paper.

## Relevance to both reviews and feasible work

**Conditional methods transfer:** distinguish (a) fitting observed temperatures, (b) identifying physical or effective coefficients, and (c) predicting a held-out engineering output. Compare errors at the use-relevant horizon with and without assimilation. Test prescribed-power/ambient/cooling and sensor-bias hypotheses before declaring missing physics. Do not infer a need for extra states merely from autocorrelation: input dynamics, synchronization and measurement bias are competing explanations.

**Analogy, not direct MSR motivation:** conductive building networks do not establish similarity of a natural-circulation loop to an MSR. Their application supplies a useful counterexample to overclaiming grey-box physical interpretation; the reactor justification still needs S13/S64/S65 and the historical/loop sources.

**Candidate contribution:** derive and assess which conservative loop model distinctions are supported by the available measurements and which remain input/observation confounded. Show independent predictive consequences using existing protocols if data permit. Merely varying RC order, adding uncertainty, using flux observations or studying excitation is established prior art. No new sensor/CFD availability is assumed.

## Claim-to-evidence ledger

| ID | Claim | Locator (PDF / printed) | Scope/limit |
|---|---|---|---|
| S69-C01 | Comparison uses two synthetic IDEAS dwelling models | 2–4 /264–266;§§2–4,Table1–2 | Not physical experiment |
| S69-C02 | Radiator-emitted heat bypasses heating-system dynamics; fitted storage depends on emission system | 3–4 /265–266;§4 | Analogous boundary-definition issue, not TRIDENT finding |
| S69-C03 | Accurate temperature prediction need not identify physical coefficients; virtual flux observations alter inference | 5–7 /267–269;§5.1,Fig3–6 | No new instrumentation assumed |
| S69-C04 | Effective capacity and combined window/ventilation loss need explicit parameter interpretation | 7 /269;§5.1,Fig6–7 | Model/excitation dependent |
| S69-C05 | Biased observation scenario changes coefficients without a comparable RMSE change | 10 /272;§5.3,Fig8–11 | Particular noise levels and synthetic cases |
| S69-C06 | More states can worsen long-horizon performance and cause problematic estimates | 5–7 /267–269;§5.1,Fig3,5–6 | Case-specific order5 failure |
| S69-C07 | Detailed and reduced simulations show season/source-dependent discrepancies | 10–11 /272–273;§6,Fig12–15 | No locked independent physical validation established |
| S69-C08 | Printed Eq1 lacks dt multiplying drift terms | 3 /265;§3,Eq1 | Visually checked; conventional SDE form is our interpretation |

## Coverage checklist

| Section/material | PDF / printed | Status and reason |
|---|---|---|
| Abstract/introduction | 1–2 /263–264 | Read/extracted; decision and prior work |
| §2 detailed model/Table1 | 2–3 /264–265 | Read/extracted; assumptions and synthetic reference |
| §3 equations/model orders/Fig1 | 3–4 /265–266 | Read/extracted; equation visually checked; expanded matrices absent |
| §4 data/Table2 | 3–4 /265–266 | Read/extracted; inputs,observations,periods |
| §5.1 ideal inputs/Fig2–7 | 5–7 /267–269 | Read/extracted; figures qualitatively inspected,not pointwise digitized |
| §5.2 realistic inputs/Table3 | 8–10 /270–272 | Read/extracted; source-proxy comparisons; scalar reference caveat retained |
| §5.3 noise/Fig8–11 | 8–10 /270–272 | Read/extracted; reported noise case and limitations |
| §6 simulation/Fig12–15 | 10–11 /272–273 | Read/extracted; horizon/season comparison,not reproduced |
| §7 conclusion | 11 /273 | Read/extracted; qualified against detailed results |
| References | 11–12 /273–274 | Inspected for leads; cited originals not thereby read |
| Supplement/code/raw data | Outside supplied PDF | Not supplied/retrieved; exact reproduction not ready |

Next originals worth checking: S08 (deeper model-selection extraction); stochastic likelihood foundation Kristensen2004; effective-storage reduction theory. These do not block the available MSR motivation batch. Current upload request S69 is resolved.
