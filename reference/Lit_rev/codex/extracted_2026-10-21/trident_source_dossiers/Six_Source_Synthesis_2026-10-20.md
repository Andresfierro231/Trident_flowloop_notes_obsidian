> Later checkpoint: reviews v0.3; S07/S18 scoped-extracted; current acquisition requests S23/S67. See Research_Execution_Plan_2026-10-20.md and Upload_Requests_Current.md. The earlier reading/access statuses below are historical.

# Six-source extraction checkpoint — 20 October 2026

The six outstanding requested papers have all been received. Each now has a purpose-scoped evidence dossier, coverage checklist and permanent claim IDs. Both literature reviews have been revised to v0.2. There is no immediate document-acquisition blocker.

## What changed

| Source | Decision informed | Result and limitation |
|---|---|---|
| S54 Keller1966 | Why loops became useful scientific models; what simplified dynamics can establish | Exact positive-flow oscillation for a special discontinuous exchange law with zero momentum inertia; not a constant-power or validated reactor loop |
| S55 Welander1967 | Why equilibrium buoyancy–friction intuition can miss instability | Advected thermal pockets and exchanger exposure can amplify oscillations; cross-sectional mixing and source laws restrict transfer |
| S59 Rodríguez-Bernal/VanVleck1998 | What rigorous low-dimensional reduction already exists | Exact restricted asymptotic subsystem from heating/geometry mode overlap; finite-time sensor/extrema reconstruction is a separate task |
| S63 Goyal2020 | Whether local stability is enough for transition predictions | Selected finite perturbations can leave a linearly stable state's neighborhood; full basin/chaos interpretation needs qualification/reproduction |
| S62 Matulis/Bindra2025 | What uncertainty/QoI a stochastic closure represents | First-reversal time and long-run dwell times respond differently; channel-DNS forcing is not loop-specific total UQ |
| S66 Cammi/Luzzi/Pini2016 | Wall-state prior art and external/internal-source analogy | Two-shell wall and source-distribution stability are established; distributed external heating approximates selected internal-heating stability under restrictions |

## History and MSR motivation

Loops have intersecting motivations: isolating convection feedback, testing heat-transport models, supporting materials/instrumentation development, and investigating passive thermal systems. The 1960s originals establish particular idealized mechanisms; they do not establish that all loops originated as MSR replicas.

Connect TRIDENT to a specific circuit and engineering decision. Candidate measured/assessable QoIs include heat rejection, losses, supported fluid/wall temperatures, circulation bounds and thermal response. A loop can provide mechanism or method evidence even where complete reactor similarity is unavailable. Quantitative transfer requires source, sink, geometry, property, regime and solid/fluid time-scale justification.

S66 is particularly useful: distributed wall heating outside the cooler is compared with fluid internal generation. A localized heater is a different source, and similar stability behavior does not establish equal local temperatures or every transient. The study's code comparisons are not new experimental validation; the authors explicitly leave that to future work.

## Implications for prospective contributions

Generic RC models, separate wall states, Fourier reduction, chaos, stochastic forcing and Monte Carlo cannot serve as novelty claims by themselves. Stronger provisional questions are:

1. Which physically meaningful parameter combinations and thermal states can sparse observations identify?
2. Can a criterion tied to a chosen QoI predict when added wall/transport physics changes predictions materially?
3. Can a feasible experiment/model-selection procedure improve independently assessed uncertainty across held-out conditions?
4. When can local thermal consequences be bounded despite unidentifiable local flow?

Each remains a hypothesis. The no-CFD minimum should focus on supported thermal/duty/response predictions. Reversal probabilities, unobserved extrema and local-recirculation extent require additional regime/observation evidence.

## Numerical and interpretive cautions to retain

- S54 prints a density/expansion sign convention needing reconciliation.
- S63's printed fractional flow powers and one-direction differences do not fully specify reversal implementation.
- S66 Table1 bore .00269m conflicts with Lt/Df269.1 and Lt7.24m; resolve the intended geometry before reproduction.
- S62 Eq13 does not differentiate Eq12 for general a2. The dossier separates printed mathematics from our derivative.
- Nonexponential dwell times do not alone exclude a higher-dimensional Markov process.

These are source/implementation questions, not accusations about unaudited executed code.

## Next reading batch — no uploads needed

| Order | Available source | Exact decision |
|---|---|---|
| 1 | S18 conjugate Fourier manuscript | How much of the proposed wall/transport reduction already exists; verify manuscript/journal correspondence |
| 2 | S23 practical identifiability | How to distinguish identified parameter groups from merely good fits; select defensible diagnostics |
| 3 | S07 Bayesian experiment design | Which feasible inputs/observations discriminate candidate models or reduce QoI uncertainty |
| 4 | S64 Bardet–Peterson2008 and S65 Ruiz–Cammi–Luzzi2015 | Sharpen surrogate-fluid and internally heated-loop transfer limits |
| 5 | Remaining S13 engineering elicitation | Complete the circuit/decision/QoI map while respecting its non-ranked elicitation scope |

S15/S61 and S58 author full text remain accessible backlog. Reading them is different from acquiring them. No request is made for FlowTests5/6, bulk data processing or Ethan-thesis discrepancy reconciliation.

## Coverage and unresolved work

All six main texts were inspected in this batch. S59 proof algebra was not independently verified. S66's long appendix expressions were mapped/selected-inspected rather than completely extracted. Selected critical pages were rendered; figures were not exhaustively digitized. No calculation, experiment or operating-data analysis was reproduced.

The two reviews are connected working drafts, not final comprehensive reviews. Finishing the available inference/design/similarity core, adjudicating claims across sources and specifying the actual facility/input/observation contract are the principal remaining steps. Additional papers will be requested only after a consequential evidence need and access check.
