# S38 Reis Seo Hassan 2024 heater failure and solidification

## Identity and readiness

Jadyn Reis, Joseph Seo and Yassin Hassan (2024), *Consequences of molten salt solidification in a natural circulation flow visualization loop due to heater failure*, Nuclear Engineering and Design 424, 113278. DOI https://doi.org/10.1016/j.nucengdes.2024.113278. Available online 8 May 2024. Complete nine-page journal article; PDF page = printed article page. Both uploaded copies have identical extracted page text despite different byte hashes, and are treated as one evidence item, not independent replication. All sections, Tables 1–2, figures/captions and references read; PDF pp. 3 and 5 rendered for equation/table verification. No raw time history/supplement supplied; data on request.

**Ready:** motivation about cold margins, spatial heating and instrumentation limits, with causal qualifications. **Not ready:** pressure/structural-failure validation, transient-flow validation or a transferable freezing closure. This is an observed off-normal event with retrospective reconstruction, not a controlled repeated accident campaign or numerical model-validation exercise.

## Problem and actual contribution

Authors report the thermal history and aftermath of heater failure during extended molten-salt-loop operation. Original evidence: initial steady PIV, continuously logged temperatures, heater-status reconstruction, post-event inspection and a later water leak test. Seven phases organize the event. Hypothesized changes in flow resistance and local pressure are interpretations; the work had no continuous transient-flow or pressure measurements (§2.2, p. 3).

The introduction cites ARE/MSRE experiences, modern facilities and accident analysis. Broad statements about fuel processing, reactivity or nonproliferation are not established by this non-nuclear nitrate experiment. Some historical metadata are internally problematic: a 2019 risk-study reference is listed with year 1965. The cited Robertson 1965 report cannot establish a later operational event merely because cited nearby. Use official originals for history, not these summaries as proof of chronology or performance. A heater-loss event in a non-fueled test is not equivalent to reactor shutdown: actual fuel continues generating decay heat.

## Geometry, operating procedure and measurements

§2/Fig. 1, pp. 2–3: 316 stainless four-leg loop, nominal legs 0.9144 m and pipe diameter about 0.025 m; lower/upper legs inclined 20 degrees. Transparent quartz test section 0.186 m, in rising leg downstream of heater; transparent DC heater. Upper air jacket 0.305 m long, nominal 0.051 m diameter, flow meter range 0–300 L/min. Expansion/melting pot nominal 0.076 m. Six centerline K-type probes, distributed wall thermocouples, insulation and separate tape heaters/controllers. Table 1 uses D=0.0236 m for the steel pipe; do not replace this with nominal quartz diameter.

HITEC composition reported NaNO₃/NaNO₂/KNO₃ =7/49/44 mol%, 5 kg prepared from ≥99% assay components (§2.5 p. 4). This is a prepared nitrate surrogate, not fuel salt; chemistry, composition drift and freezing properties do not transfer by matching Pr. Initial preparation: melting pot 220 °C, legs 200 °C for filling. Operation then uses main 375 W, combined vertical-leg heating 54.3 W and transparent-section 20 W. Text also gives regulated total 429.3 W (§2.3 p. 3); 375+54.3 equals that total, with transparent DC power apparently additional. A full gross-to-net deposition ledger is not supplied; do not declare one power total without clarifying meter boundaries. Secondary airflow 33 L/min (5.5e−4 m³/s), backup heater setpoint TP2=180 °C, reported salt freezing about 148 °C. Twenty-four hours between adjustments was the authors' steady-state procedure, not a universal settling-time requirement.

Temperature DAQ 50 Hz. Initial PIV: 6000 frames, 1000 fps, 512×1024 camera, 50-μm silver-coated hollow spheres, 1-mm laser sheet; 2.84% vectors interpolated by outlier procedure (§3 phase I, p. 4). Only the initial steady velocity is measured during this event; later velocities/blockage times are not continuous PIV observations.

## Equations and numerical checks

| Equation ID | Reported relation/locator | Check/implementation restriction |
|---|---|---|
| S38-E01 | U_i=α Δx_i/Δt; Eq. (1), p. 3 | α m/pixel, displacement pixels, Δt seconds gives m/s. Calibration and synchronization shared across vectors can create covariance. |
| S38-E02 | First-order independent-term propagation of α,Δx_i,Δt; Eq. (2), p. 3 | Dimensions m²/s² inside variance. No cross terms shown; uncorrelated-input assumption must be justified for reuse. |
| S38-E03 | Printed magnitude-uncertainty Eq. (3), p. 3 uses factors U_bar/(U_bar²+V_bar²) and V_bar/(U_bar²+V_bar²) inside the square-root variance sum. | Visually confirmed: denominator lacks sqrt(U_bar²+V_bar²). As printed the result is dimensionless, not velocity. Analyst delta-method expression for M=sqrt(U²+V²) uses (U/M)²Var(U)+(V/M)²Var(V)+2UV Cov(U,V)/M². This is a separately derived replacement to verify, not the reported equation or an authorized code change. Reported 3.58% uncertainty cannot be reconstructed solely from the printed formula. |
| S38-E04–07 | HITEC μ,ρ,c_p,k polynomials matching S16 Eqs. (5)–(8); here Eqs. (4)–(7), p. 4 explicitly state **T in K**. | Resolves a temperature-unit lead for the same printed coefficients; validity ranges still require original property sources. A cross-paper agreement is not independent property validation. |
| S38-E08–11 | Pr=μc_p/k; Re=ρU_mean D/μ; Gr=gβΔT D³/ν²; Ri=Gr/Re². Eqs. (8)–(11), pp. 4–5 | Dimensionless; properties at heated-leg film temperature and ΔT for wall–bulk driving are discussed. Table 1's displayed loop ΔT should not automatically be substituted for local wall–bulk ΔT. Re and Ri characterize this state, not universality thresholds for loop flow. |

Table 1, p. 5: steel-pipe mean velocity 0.0373 m/s, displayed ΔT 7.8 °C, D=0.0236 m, Pr=27.2, Re=260.0, Gr=8.14e4 and reported Ri=1.25. Initial test-section PIV average 0.0471 m/s is rescaled to 0.0373 m/s for diameter change (p. 4). Arithmetic check: displayed Gr/Re²≈1.204, not 1.25; preserve this discrepancy rather than manufacturing an explanation. No uncertainty for that consistency check is available. Magnitude versus signed axial cross-sectional velocity and axisymmetry assumptions must be audited before using this value for a conservation benchmark.

Thermocouple manufacturer ±1.1 °C below 293 °C, stated ΔT uncertainty ±1.56 °C; power-meter ±1% or ±0.93% by range. These are not a joint covariance model or independent spatial-gradient accuracy. Temporal samples at 50 Hz are not 50 independent observations per second.

## Results and what was established

§3 phases II–VII/Figs. 2–6, pp. 4–7: main 375-W heater failed; first 7 min cooling accelerated to 1.70 °C/min, subsequent 11 min mean 1.43 °C/min, Phase II drop 24.4 °C. Backup heating triggered at 180 °C; one cold-leg heater was already unavailable. Approximately 24 min later leakage/additional heater failures were reconstructed; authors infer a salt plug/flow halt 52 min after initial failure. That time is a temperature/phase interpretation, not a metered zero-flow threshold. No pressure trace demonstrates their proposed pressure-buildup pathway.

Inspection and water leak test locate damage at welded/instrumented fittings and quartz seals (Figs. 7–9; §4 pp. 6–8). Salt contamination, heater damage, subsequent leakage and repair are original facility evidence. This does not isolate whether solidification strain, pre-existing weld/seal weakness, local expansion or thermal stress caused each breach. The near-freezing temperature plateau is consistent with phase change but does not resolve plug geometry or phase fraction. Backup heater location plausibly changes buoyancy, but the paper does not quantitatively identify that mechanism against alternatives.

Table 2 p. 8 reports final cooldown slopes: TP1 0.0483, TP2 0.0012, TP3 0.1154, TP4 0.1188, TP5 0.0202, TP6 0.0659 °C/min. These are fitted/reported event slopes with differing phases and boundary conditions, not intrinsic regional conductances or heat capacities. Final <25 °C at all measured sites after 17 h 46 min is an event observation, not the time a different loop needs to become thermally uniform. Recommendations for Inconel heaters are author recommendations, not a comparative qualified material test.

## TRIDENT applicability and next action

Direct motivation: local cold margins, protection-heater placement, dependable boundary histories and distinguishing measured from inferred flows. Conditional transfer: ACU salt solidification requires actual salt properties, operating envelope and heater/cooling configuration. Analogy only: glycol VCU cannot validate salt phase change or nitrate seal/material compatibility. No instruction here to conduct a damaging heater-failure experiment, add a freezing model to the core single-phase thesis, or claim a licensed safety function.

Current models should expose when they leave their single-phase regime; their scope cannot silently span the phase-change event. Model contracts need heater switching, net deposition, ambient/secondary conditions and initial stored energy. Hypothesized flow reversal, local recirculation and breach pressure need independent evidence before becoming assessment targets. H03 remains gated by unavailable local observations/qualified CFD; H02 can study measured thermal consequences without promising structural accident prediction.

Next originals: official MSRE design/safety reports (ORNL-TM-728 and reactor safety report DOI 10.2172/4034157), ARE operating report DOI 10.2172/4237975, S10 molten-salt transient study, and actual heater/DAQ event ledger if reproducing this case. They are leads; the cited originals have not been read simply by reading this article.

## Coverage checklist

| Material | Status | Reason/limit |
|---|---|---|
| §1, pp. 1–2 | Read/extracted critically | Historical and design claims treated as cited background; no adoption of generic reactor-benefit claims. |
| §§2.1–2.5, pp. 2–4 | Read/extracted | Apparatus, PIV, protocol, UQ and properties; Eq. 3 dimensional issue flagged. |
| §3 phases I–VII, pp. 4–7 | Read/extracted | Measured initial flow/temperature event separated from inferred later flow/pressure. |
| §4 and §5, pp. 7–8 | Read/extracted | Damage observations and limits of causal interpretation. |
| Tables 1–2 | Read/extracted; Table 1 visually checked | No raw-data recalculation of phase boundaries or slopes. |
| Figs. 1–9 | Present and inspected qualitatively | No independent stress, pressure or plug-size reconstruction. |
| Data statement/references, pp. 8–9 | Read; leads extracted | Underlying data not supplied. |
| Second uploaded copy | Text equality checked | One evidence item; no duplicate claim weight. |

## Claim ledger

| Claim ID | Claim | Locator | Type/limit |
|---|---|---|---|
| S38-C01 | Continuous temperatures, but only pre-failure PIV and no pressure data, support the event reconstruction. | §2.2 p. 3 | Direct measurement contract; later mechanism claims remain inferred. |
| S38-C02 | Local heat-source changes and backup availability preceded leakage, further heater failures and freezing. | §3 pp. 4–7; §4 pp. 7–8 | Original event account; not isolated causal validation. |
| S38-C03 | Claimed blockage at 52 min is inferred from the thermal history rather than a continuous flow meter. | Phase V p. 7; §2.2 p. 3 | Author event interpretation plus evidence restriction. |
| S38-C04 | Printed magnitude-uncertainty Eq. 3 is dimensionally inconsistent as written. | Eq. 3 p. 3, rendered verification | Analyst audit; reported uncertainty not independently reconstructed. |
| S38-C05 | HITEC property-polynomial T is explicitly Kelvin here. | §2.5/Eqs. 4–7 p. 4 | Author convention; does not establish fit validity range. |
