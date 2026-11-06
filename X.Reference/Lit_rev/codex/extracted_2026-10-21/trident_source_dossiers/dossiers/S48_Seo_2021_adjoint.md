# S48 — Seo et al. (2021): adjoint sensitivities in a high-Pr loop

20 October2026. **Ready for closest-method, QoI/sensitivity and qualified motivation synthesis. Reported equations require resolution before literal implementation.**

## Identity, version and completeness

Seok Bin Seo, In Cheol Bang, Hisashi Ninokata, Antonio Cammi, “Application of adjoint-based sensitivity analysis to natural circulation of high-Pr fluid inside heat transport system,” *Nuclear Engineering and Design*381(2021),111349, [DOI10.1016/j.nucengdes.2021.111349](https://doi.org/10.1016/j.nucengdes.2021.111349). Supplied20-page publisher-formatted PDF; title, authors, DOI and publication identity agree with the verified registry. Online2 July2021; accepted17 June2021. Printed page=PDF page. Main text, AppendixA, AppendixB and references are present/readable. Relevant text, equations, tables and plot overviews across all pages were inspected, with high-resolution checks of consequential formula/unit and error tables. Plots were not digitized; original MATLAB code, raw facility data and any external supplement were not supplied.

## Contribution and what is established

The authors formulate a1D loop and continuous Lagrangian adjoints for time/space-integrated mass-flux, temperature and cooler-Nusselt functionals. They compare adjoint derivatives with finite-difference recalculation and direct sensitivities, then explore property functions, exchanger orientations, reference temperatures and fluids (§§2–5). This already establishes an application of adjoint QoI sensitivity to molten-salt-related natural circulation: a generic sensitivity-driven loop method cannot be claimed as a first.

The geometry is based on UNIST experiments, chiefly **DOWTHERM RP oil**, not a new salt experiment in this paper. Shin2016/2018 are cited prior experimental/analogy evidence; they were not independently read here. §3.3's “validation” is principally agreement of derivative methods for the same forward model. No new independent measured-temperature/flow validation campaign or uncertainty-calibrated failure probability is demonstrated.

## Geometry, physical model and conditions

One closed constant-diameter rectangular loop, externally heated vertical section and horizontal/vertical coolers with constant prescribed wall temperature; atmospheric pressure in the described facility. Table1/PDF5: D=0.023 m; heater length0.19 m; cooler lengths0.30 and0.74 m; wall temperature293.15 K; reference temperature423.15 K; heat flux72.84 kW/m². The remaining named lengths and their interpretation are in Fig1/PDF4 and Table1; no complete CAD model is reconstructed here. Referenceρ=1004.52 kg/m³,μ=0.0013 Pa s,cp=1974.7 J/(kg K),k=0.12 W/(m K),β=0.0006987 K⁻¹; Darcy a=64,b=1 and reported local factor0.001. These are source-specific inputs, not TRIDENT constants.

Assumptions (§3.1/PDF4):1D incompressibility, Boussinesq density, uniform heater flux, fixed cooler-wall temperature, no conduction/dissipation in the fluid energy equation and laminar distributed friction. No independently evolving conjugate wall/insulation or explicit ambient-loss state is represented in these equations. Only cp and μ are temperature-dependent in the later fluid comparison. Reference-temperature analyses use333.15,423.15,523.15 K (§4.3/PDF16); do not confuse those values with an experimentally established validity interval for every material/property fit.

G is mass flux kg/(m² s), uniform in s under Eq9; s follows nominal clockwise flow from cooler entry. Eq15 is the loop-integrated momentum balance with inertia, temperature-driven buoyancy and distributed/local resistance. Eq11 advances cpT with source/cooler exchange. Eq13 is Darcy \(f=a/Re^b\). These equations have no general signed-flow/reversal treatment: \(G^2\) and \(G^{2-b}\) require a declared positive branch or a signed reformulation. The local factor is introduced in a distributed \(f_{\rm local}/D\) form; do not silently replace it with a sum of minor-loss K values without matching the length normalization.

## Reported mathematics versus analyst checks

The generic adjoint identity is a useful transferable starting point. For \(F(x,\alpha)=0\), solve \(F_x^\mathsf T\lambda=r_x^\mathsf T\), then \(dr/d\alpha=r_\alpha-\lambda^\mathsf T F_\alpha\) (source Eqs6–8/PDF3). For the transient PDE, initial/boundary/terminal terms appear explicitly in Eq28/PDF5; their cancellation requires appropriate conditions, not a generic “drop boundaries” rule. Source Eq29 normalizes with \(\alpha/R\). AppendixB defines \(R_1=\int\int G\,ds\,dt\), \(R_2=\int\int T\,ds\,dt\), and \(R_3=\int\int_{\rm cooler}Nu\,ds\,dt\). These are integrals, not instantaneous extrema or failure events; the prose's “space average” omits a normalization shown nowhere in B1. With fixed domain/time, constant normalization cancels in a normalized sensitivity but matters for dimensional values and geometry/time-dependent functionals.

Consequential ambiguities, visually checked rather than repaired silently:

1. **Cooler coefficient, Eq14/PDF4.** It prints \(h=h_{\rm ref}\,q''(L_h/L_c)/(T-T_w)\). With declared dimensional h_ref and q'', the right side has units of h squared. A missing normalization or different coefficient definition is necessary. If an intended closure is simply \(h\propto1/(T-T_w)\), its product with driving temperature becomes constant and its temperature derivative changes materially. Obtain code/clarification before adopting this closure or its adjoint.
2. **Energy variable, Eq11/PDF4 and Eqs33/B2/B5/B9.** For differential specific heat cp(T), enthalpy is \(\int cp\,dT\); \(d(cpT)/dT=cp+T\,cp'\). Those are different thermal-storage/transport laws unless cp has a nonstandard mean definition, not established here. An adjoint consistent with the printed forward model does not validate the thermodynamics of that model.
3. **Units, Eq16/PDF5.** The cp fit0.0029T+0.748 matches Fig2's **kJ/(kg K)** scale, whereas Table1/nomenclature use J/(kg K). Eq17 is Pa s while Fig2 shows mPa s. Later sodium Eq41 explicitly uses kJ/(kg K), while water/HITEC expressions use J/(kg K). Code must normalize units once, consistently, and differentiate the same normalized functions.
4. **Boundary problem, Eqs20–21/PDF5.** The source specifies cooler-entry temperature equal to T_ref as well as periodic temperature. The precise role of that internal temperature constraint—controlled operating condition versus merely a reference—is not sufficiently documented for a fully autonomous forward prediction. §4.3/PDF16 calls it a controlled operating temperature and maximum. Preserve the conditional task; do not prescribe the temperature later claimed as independently predicted.
5. **Functional conventions.** Eq30/PDF7 adds dimensional G and T without explicit nondimensional weights. Define a dimensionally meaningful objective before reuse. Temperature integral normalized sensitivities depend on the declared absolute-temperature reference; smaller sensitivity is not automatically better engineering performance.
6. **Integration endpoint.** The evaluation horizon is described as startup until mass flux reaches steady state (PDF7–9). If recomputed as a parameter-dependent stopping time, derivative evaluation needs the moving-endpoint term; the exact fixed/adaptive convention is not given. Terminal values, time/space grids and recalculation perturbation sizes are not documented sufficiently for exact replication.

These are implementation blockers and qualifications, not a conclusion that the paper's entire method is invalid.

## Results, verification and uncertainty limits

MATLAB custom scripts and implicit Euler are reported; iterative relative tolerance10⁻⁹ is stated (§3.3/PDF7). That tolerance is not a time/space discretization error estimate. No complete grid/time convergence study or derivative perturbation-sweep evidence is reported.

Table2/PDF7 checks a general functional: maximum listed adjoint/recalculation difference5.08% (diameter). AppendixB tables are more specific: mass-flux adjoint differences up to4.98%; temperature up to15.22% (density) and13.70% (local resistance); Nu up to13.87% (β) and12.97% (density), PDF16. Thus “within5%” is not a general accuracy guarantee. Direct/adjoint agreement tests derivative consistency, not experimental validity. Continuous-adjoint/discretized-forward mismatch, conditioning and perturbation choice need independent investigation rather than assuming an error cause.

Figure4/PDF8 illustrates the expected scaling advantage for many parameters and few objectives: a separate adjoint per objective, with forward trajectory/storage and inner-product costs still present. No machine-independent TRIDENT speedup is claimed.

The property-function comparisons (Eqs17,38–39; Figs8–12/PDF9–11) show sensitivity to viscosity **derivatives** even for similar fitted values; the authors report large changes, including up to200% for selected temperature sensitivities. Those are source-specific results, not universal amplification factors. Comparing rounded high-order polynomial derivatives warrants conditioning checks.

Their conclusion that high-Pr fluids are “more stable/reliable” follows smaller local normalized sensitivities under this model and selected operating points (§5/PDF16–17; Fig21/PDF14). It is **not** a demonstrated dynamic stability boundary, global uncertainty analysis, matched-similarity experiment or probabilistic functional-reliability calculation. Fluid, temperature, properties and other scales change together; Pr alone is not isolated as a causal parameter.

## TRIDENT relevance, next reading and implementation

Direct methodology: compute sensitivities of declared QoIs using the actual conservative forward/observation model; verify with tangent/direct or finite-difference checks across perturbation sizes. Conditional transfer: property gradients and source/sink arrangement can change parameter importance. Analogy: oil-to-salt scaling requires the cited original evidence and mechanism-specific similarity. Not justified: importing printed h/energy equations, declaring high-Pr inherently safe, or using this derivative comparison as independent TRIDENT validation.

For a four-to-six-state model with few fit groups, direct sensitivities or automatic differentiation may be simpler than a hand-derived continuous adjoint; benchmark actual cost. Sensitivity magnitude alone is not identifiability or experiment value: use observation rank/covariance and parameter uncertainty as well. Full UQ additionally requires justified joint inputs, discrepancy, numerical error and withheld predictive assessment.

Next original sources: S50 Srivastava2016 for the comparable1D loop; S51 Jiao2018 functional reliability for probability-of-limit questions; Shin2016/2018 and2017 thesis for the actual oil-simulant evidence; Cao et al.2003 adjoint-DAE theory if using parameter-dependent initial/boundary conditions. These cited originals are leads until separately acquired/read. Author MATLAB code would resolve important equations but was not found via targeted title/code searches; do not block the entire literature programme on it.

## Coverage checklist and claims

| Component | Inspected/extracted | Limit |
|---|---|---|
| §§1–2/PDF1–3 | Motivation, prior art and generic adjoint | Cited experiments/theory not implicitly read |
| §§3.1–3.2/PDF3–5 | Forward assumptions, units, BCs and adjoint formulation | Exact implementation not reconstructed |
| §3.3/PDF6–8/Table2 | Cross-method checks and reported numerical setup | Not independent physical validation |
| §4/PDF8–16/Figs5–19 | Property, geometry and reference-condition comparisons | No figure digitization or derivative replication |
| §§5–6/PDF16–17/Figs20–21 | Fluid comparison, conclusions and claim limits | Local sensitivity is not probabilistic reliability |
| AppendixA/AppendixB/PDF15–19 | Derivation checks, functionals and TablesB1–B3 | No independent line-by-line proof/execution of every adjoint term |
| References/PDF19–20 | Traced selectively | New full-text requests recorded |
| Raw data/code/external supplement | Not supplied | Not reviewed or executed |

| Claim ID | Claim | Locator | Qualification |
|---|---|---|---|
| S48-C01 | Adjoint natural-circulation QoI sensitivity is established application prior art | §§2–3,PDF3–8 | Few objectives/many parameters; oil-based forward model |
| S48-C02 | Published validation compares derivative methods for the same model | §3.3/Table2,PDF7–8 | Not a new independent experimental validation campaign |
| S48-C03 | h, energy, cp units and reference/periodic BCs require clarification for implementation | Eqs11,14,16,20–21; PDF4–5 | Analyst audit of visually checked mathematics |
| S48-C04 | Some functional derivative discrepancies exceed5% | TablesB1–B3,PDF16 | Temperature15.22%,Nu13.87%; source table values |
| S48-C05 | Viscosity-function gradients change reported sensitivities | §4.1/Eqs17,38–39/Figs8–12,PDF9–11,14 | Source-specific; no universal multiplier |
| S48-C06 | High-Pr reliability/stability interpretation is limited to local normalized sensitivity | §5/§6/Figs20–21,PDF14,16–17 | Not a probability-of-failure or dynamic stability proof |
| S48-C07 | Source functionals are integrated mass flux, temperature and cooler Nu | AppendixB/EqsB1,B4,B8,PDF18–19 | Not extrema; endpoint/normalization conventions matter |
