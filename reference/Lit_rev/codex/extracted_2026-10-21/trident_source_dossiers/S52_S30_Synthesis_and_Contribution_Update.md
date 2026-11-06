> Current deliverables: Methods_and_Theory_Review_Working_Draft.md, Motivation_and_Contribution_Review_Working_Draft.md and Upload_Requests_Current.md supersede prior reading/access statuses.

# S52/S30: implications for the two literature reviews

2026-10-20. Governing goals remain those in supplied Markdown collé.md. This is an evidence-backed synthesis checkpoint, not the final comprehensive reviews or a selected thesis direction. Source dossiers contain detailed locators, mathematical caveats and coverage checklists.

## What the new sources add

| Question | S52: LeBENC/LBE experiment | S30: Fourier/stochastic water loop | TRIDENT consequence |
|---|---|---|---|
| Why build a loop? | Reactor-related thermal hydraulics, material compatibility and instrument development, §§1–3 | Study performance/stability/dynamic fluctuation effects, §§1–2 | Mechanism studies and engineering test facilities have multiple purposes; MSR representativeness needs a separate argument |
| What model is retained? | Variable-area circulation, separate fluid/wall energy and axial conduction, §§4.1–4.4 | Eight real circulation/Fourier thermal states, fixed heater flux and prescribed cooler-wall temperature, §2 | RC, finite-volume and Fourier models are credible competing families; none is automatically the final model |
| What is fitted or inferred? | Cooler and regional loss coefficients inferred using thermal balances, §§4.5–4.6 | Effective diffusivity selected against stability; stochastic coefficients learned from channel DNS, §§2.1/2.4 | Record the calibration inputs, target and evidence independence for every model |
| What uncertainty is represented? | No complete propagated measurement/model budget | Dynamic stochastic forcing from a particular training signal | Neither is a complete template for measurement, inputs, epistemic discrepancy and prediction-to-decision uncertainty |
| What does assessment demonstrate? | Agreement with calibrated thermal/flow estimates and selected transients | Prior steady/stability comparisons and numerical deterministic/stochastic scenarios | Baselines must be compared using the same input/observation/holdout contract |
| What does it not establish? | Independent flow truth or transferable high-Pr closure | TRIDENT noise amplitude, full margin probability, solid storage or measured local recirculation | Restrict claims to measured QoIs unless additional qualified evidence exists |

## Motivation review: an evidence-supported paragraph

Natural-circulation loops support both basic transport/dynamics research and practical reactor development. In the HANS facility, Borgohain and colleagues combined LBE thermal-hydraulic experiments with high-temperature instrumentation and chemistry/materials concerns (S52, §§1–3, PDF1–4). Its liquid-metal reactor context differs from the molten-nitrate reactor/solar applications of S50 and the DRACS-inspired coupled salt/air system of S51. These examples motivate studying heat removal, transient thermal response and operating margins, but they do not make every heated loop a scaled representation of every MSR. A defensible TRIDENT argument must name the reactor subsystem and decision, identify the relevant transport/source/storage scales, and state which differences prevent quantitative transfer. The historical Keller/Welander papers and single-phase scaling literature are queued to establish that argument from their original assumptions.

## Methods review: an evidence-supported paragraph

Established physical reductions already span conjugate one-dimensional conservation models and Fourier systems with only a few thermal modes. LeBENC retains fluid and wall energy, variable-area momentum and ambient exchanges, while using experimental thermal balances to determine important exchange coefficients (S52, §§4.1–4.6). Matulis and colleagues instead retain circulation and Fourier temperature modes, including a mean mode allowing unequal heating and cooling, then add a data-driven fluctuating minor-loss term (S30, §§2.1–2.5). These alternatives differ in state meaning, boundary inputs, calibration and uncertainty representation. Consequently, a useful comparison must hold the prediction task fixed: independently available heater/cooler/ambient inputs, the observation operator, permitted calibration data, withheld operating cases and declared QoIs. Training agreement alone cannot establish that fitted coefficients represent unique physical properties or that unobserved extrema/local flow are predicted.

## Provisional contribution hypotheses, narrowed by prior art

**H01 — Identifiable physical reduction.** Establish supported groups of storage, loss and transport parameters when input uncertainty and sensor mapping are explicit. A feasible no-CFD core is a conservative model-class analysis and independently assessed temperature/duty/response predictions at actual observation locations. The elementary capacity/conductance scaling ambiguity is established background, not sufficient novelty.

**H02 — QoI-dependent retained physics.** Develop and test a criterion for retaining fluid/wall/insulation/tank storage or transport enrichment against an error/uncertainty target. Existing papers already include these mechanisms or discuss their omission. A contribution must predict *when and for which QoI* a simpler model fails, and demonstrate transfer across withheld conditions beyond fitting each case.

**Uncertainty and decisions.** Separate measurement/input uncertainty, uncertain physical parameters, structural discrepancy and time-varying fluctuation forcing. S51 already uses model alternatives for margin calculations; S30 already studies stochastic closure. A useful advance could be inference/discrimination with empirically assessed predictive coverage for achievable QoIs. Sparse temperature data may support only bounds or parameter groups, not loop-specific stochastic friction; report that outcome if it is the evidence.

**Local recirculation.** Extent and causal heat-transfer consequences remain conditional targets. Current temperature agreement alone does not validate local velocity structure. Read S60 and retain S37/S46 as strong prior work before defining a local-flow contribution.

These are hypotheses and feasibility gates, not established gaps or promises of a novel theorem.

## Immediate implementation lessons for Codex

1. Treat the published equations as reported evidence, not trusted software specifications. Both dossiers identify sign, coefficient, area or stochastic convention ambiguities. Derive any corrected implementation separately and preserve attribution.
2. Compare a conservative regional network, a conjugate finite-volume loop and a Fourier alternative under one input/observation/assessment contract. Choose complexity through the declared QoIs and information content.
3. Check energy/exchange conservation, constant-temperature equilibrium, source units/areas, signed circulation near zero, nonnegative dissipation and appropriate property/enthalpy conventions before fitting.
4. Distinguish thermal-balance flow estimates from independent primary-flow observations; include shared-input covariance. Different agreement plots need not be independent evidence.
5. Keep fixed-parameter uncertainty, process fluctuations and measurement noise distinct. A stochastic trajectory does not by itself provide a calibrated decision probability.

No code changed, experiments executed, operating-data processed or CFD availability assumed in this pass.

## What is ready and what remains

The new dossiers are ready for qualified prior-art, model-assumption and motivation synthesis; their literal equations are not certified implementation recipes. The **Fifteen_Paper_Reading_Plan.md** specifies the next portfolio and three high-value acquisition requests. The two final reviews remain to be assembled after focused extraction of the available S18/S23 and relevant similarity/engineering sources. S30/S52 requests are resolved and must not be repeated.
