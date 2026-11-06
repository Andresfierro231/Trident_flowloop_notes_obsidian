# Natural-circulation loops, MSR engineering needs and feasible TRIDENT contributions

**Working review v0.6,21October2026.** A connected proposal/dissertation draft grounded in the accumulated dossiers, including newly inspected S13/S64/S65. This is a substantive review draft, not an exhaustive history, a certified novelty finding or a reactor-safety validation. Stable source IDs resolve to the registry; consequential claims below give original locators or point to the detailed dossier. The exact project facts remain governed by Markdown collé.md and the supplied project records.

## 1. Why these experiments matter

A natural-circulation loop is useful because it makes a coupled heat-transport problem accessible: heating changes temperature and density; the density distribution creates buoyant head; hydraulic resistance limits circulation; and circulation redistributes heat. Solids, losses and the heat sink add feedback and time scales. A steady buoyancy–friction balance can therefore coexist with oscillatory or unstable response. The loop can support controlled study of these mechanisms and assessment of models under observable conditions.

For an MSR proposal, this physical interest must connect to an engineering decision. The question is not simply whether a reduced model matches a temperature trace. It is whether the model can predict a specified heat duty, temperature response, circulation measure or thermal margin accurately enough for its intended use, with uncertainty appropriate to the available evidence. Reactor heat transport is the motivation; a carefully delimited facility/model result can be the scientific contribution.

Two distinctions organize the review. First, a useful mechanism experiment need not quantitatively represent a complete reactor. Second, predictive agreement, parameter identifiability and physical interpretation are different achievements. S69/S70 give direct methodological counterexamples to conflating them; S64/S65 explain why the distinction persists when moving from a laboratory configuration toward a reactor application.

## 2. An intersecting history of mechanisms, materials and reactor concepts

The current primary evidence supports several related histories, not a claim to have located the first thermosyphon or an inevitable progression toward MSRs.

**Reactor design tradeoffs.** Romie–Kinyon's1958 natural-convection reactor concept explicitly weighs pump reliability/maintenance against increased salt inventory associated with risers and an exchanger (S40,ORNL-CF-58-2-46,PDF4/printed1; abstractPDF3/ii). Its60MW thermal rating is a design calculation, not demonstrated plant performance. This is useful motivation because it connects buoyant heat transport to a concrete engineering tradeoff.

**Circulating-salt exposure and materials experiments.** The1967 ORR convection-loop report concerns fueled fluoride-salt irradiation in contact with graphite/HastelloyN (S41,PDF9/printed1; discussionPDF37–41/29–33). Natural circulation supports a materials/fuel exposure mission. The operated loops also experienced failures; proposed thermal-stress explanations are qualified in the original. An unirradiated surrogate loop does not reproduce those material environments, but this history shows why loop motivation can extend beyond passive heat removal.

**Normal pumped reactor operation.** The MSRE design report describes fuel and coolant pumps and an air radiator (S42,§2.4,PDF41/printed9;§2.4.2,PDF44/12). It would be inaccurate to present normal MSRE primary flow as identical to a small buoyancy-driven test loop. Reports of a later1969 natural-circulation test remain an original-operating-record acquisition lead in our corpus; no exact date, duration or achieved power is used here.

**Mathematical and experimental model systems.** Keller1966 and Welander1967 (S54/S55) study distinct idealized transport/oscillation mechanisms. Keller acknowledges Welander's earlier1965 report, so journal dates alone cannot establish discovery priority. Later water-loop scaling/stability, conjugate-loop models, high-Pr measurements and stochastic reductions extend this role. The inspected originals support a history of useful simplification and its limits, not a universal reduced equation for every loop.

**Scaled high-temperature experiments.** Bardet–Peterson2008 (S64) develops reduced-temperature/size/power experiments for selected salt/helium convection phenomena. The motivation is economical and observable assessment with explicit distortion, including fluid/structure response. Modern salt/surrogate facilities add local diagnostics, property/loss characterization and code assessment. Several papers can share one apparatus or dataset; their existence does not create independent reactor-scale replications.

## 3. Which reactor questions make our quantities useful?

Brown et al.'s liquid-fuel MSR elicitation identifies temperature distribution, power distribution, bulk/potentially local velocity, liquid composition, gases and solids as thermal-hydraulic figures of merit (S13,§V.A/TableII,PDF17–19). Temperature is linked to material limits, deposition/release and feedback; velocity affects transport and local thermal behavior. These are reasons to care about our outputs, not evidence that TRIDENT already predicts safety margins.

The article is a preliminary expert exercise across design concepts. It does **not** formally rank research priorities, quantify universal model uncertainties or establish a completed list of vacant research topics (S13-C04). Its detailed target is liquid-fuel primary-system modeling; auxiliary/secondary systems are not fully treated (§I.B/PDF6). A passive-rejection or secondary-loop mission therefore needs subsystem-specific support such as S51 and the relevant salt-cooled/CIET literature, not only this primary-system elicitation.

| Engineering decision | Candidate QoI | Mechanism and literature basis | What our evidence could establish / limit |
|---|---|---|---|
| Can a specified path reject the required load? | Net source, cooler duty, ambient loss and storage balance | Source–sink transport; S50/S51/S52; S13 heat-exchange needs | Facility duty/response if metrology is supported; not a reactor decay-heat certification |
| Are temperatures compatible with a stated limit? | Measured fluid/wall temperatures; supported minimum/maximum; uncertainty in margin | Thermal distribution/material consequences; S13 TableII and§V | Probe/local/regional predictions; unmeasured global extrema require additional evidence |
| Is circulation adequate and in the intended direction? | Signed bulk circulation or defensible bounds | Buoyant head versus distributed/form resistance; S13§V.D,S52,S57 | Quantities supported by actual observations; energy-derived flow is not independent flow truth |
| What follows a source/sink change? | Response time, overshoot, settling and time to a specified thermal limit | Advection and fluid/solid storage; S50/S52/S65/S66 | Selected facility transients; heater-off is not automatically reactor scram/decay heating |
| Which geometry/exchanger choice improves performance? | Duty/flow/temperature response versus loss and elevation | Thermal barycenters, resistance and heat exchange; S40/S64/S65 | Conditional design trends; need target circuit and valid comparison range |
| Does local flow change heat transfer? | Qualified local gradient or reverse-flow descriptor and thermal consequence | Developing/mixed convection and local geometry; S37/S46/S60 | Conditional extension; sparse temperatures alone do not establish3D recirculation extent |
| Is additional model or measurement complexity worthwhile? | Held-out prediction error, interval coverage and identifiable quantities | S23/S67–S70 and decision-oriented design | Scientific adequacy/information result for declared evidence; dashboard implementation alone is not novelty |

Required acceptance tolerances, qualified property ranges and independent energy/observation anchors remain project facts to establish. A temperature margin above liquidus can be a useful sensible-heat output; predicting freeze onset, latent heat, evolving blockage or recovery adds mechanisms and evidence. Critical heat flux is not a default QoI for the current single-phase scope.

## 4. Representation depends on the circuit and the prediction

A liquid-fuel primary circuit carries fuel, internally generated heat and delayed-neutron precursors; thermal/flow changes interact with reactivity. A salt-cooled solid-fuel system starts with heat generated in fuel/structures. A secondary loop receives heat through an exchanger, while a passive residual-removal or drain system has its own source history, topology and mission. The same apparatus may illuminate mechanisms relevant to several systems, but it cannot support an unqualified 'MSR representative' designation.

S64 requires geometry, initial/boundary conditions and fluid/solid response in addition to fluid groups (§IV.A,Eq2–10,PDF5–6/348–349). Pr matching helps select a simulant; it does not establish matched buoyancy, inertia, property variation, losses or wall response. Its examples can match major groups while retaining viscosity-variation distortion (TableV,PDF11/354). Low-temperature experiments also do not automatically reproduce high-temperature thermal radiation. The paper's illustrative radiation arithmetic has a flagged inconsistency in the dossier, so the proposal should cite the conditional physical requirement rather than borrow that percentage.

This supports a **QoI-specific transfer assessment**. Steady duty or circulation, wall temperature, local extrema and rapid response need not tolerate the same distortion. S56's fluid/solid/interface scaling and the existing conjugate studies reinforce this distinction. A model can be useful for the actual measured facility even if quantitative reactor scaling is not supported.

Source distribution is especially consequential. S65's1D stability comparison combines localized wall heating and uniform fluid heating, and finds source-share- and geometry-dependent dimensionless stability boundaries (§4,Figures10–13,PDF8–10). Actual fluid-specific operating trajectories were not mapped onto those boundaries (§4.2,PDF9); cross-method numerical agreement was not experimental validation. S66 subsequently examines wall inertia/source alternatives. Consequently, matching total power alone does not establish equivalent transient or stability behavior, and testing source placement is already prior art.

S13 also limits representation beyond heat transport: isotope/chemical composition, gas/solid transport, direct nuclear deposition and precursor effects are separate requirements. The paper's heat-removal/reactivity wording in§IV.C contains an unresolved sign/sequence ambiguity, recorded in the dossier; it is not used to define a transient direction here. Old design/regulatory/data-availability statements are treated as historical, not automatically current2026 facts.

For every proposed use, classify the claim as: direct facility prediction; conditional quantitative scaling with explicit distortion; mechanism analogy; or incompatibility. Record the target circuit, source/sink, regime, fluid/solid time scales and observation operator. Similarity is a scoped argument with evidence, not a label attached to a fluid.

## 5. What the strongest prior work already covers

Physical1D loop models already include conjugate storage, heat losses, nonuniform geometry and transient assessment (S52); related molten-salt studies compare experiments,1D and CFD descriptions (S10/S50). Model/source/tank assumptions and fitted boundary coefficients limit independence. Thermal-loop models with wall states or ambient-loss calibration are therefore not themselves a new theoretical contribution.

Closure and numerics can change dynamic conclusions. S57 examines friction-transition/numerical effects; S65's frozen versus varying transition factors change a comparison near Re≈2500; S66 treats wall/source effects. Keller/Welander, S59 and Fourier studies establish substantial reduction/dynamics theory. S30/S62 and S63 add stochastic/event and finite-disturbance analyses. Their existence rules out generic claims that low order, nonlinear response, noise or wall inertia have been ignored.

Local high-Pr behavior is likewise studied. S37/S46/S60 provide spatial evidence and CFD interpretations with their own measurement and representativeness limits. The question is which local descriptor and thermal consequence our evidence can resolve, not whether local flow exists as a research topic. Newly retrieved S29 and requested S19/S74 are close modern comparators that must be extracted before narrowing novelty further. No technical findings are attributed to their unread sections.

Inference methods also have established foundations. S23 links profile likelihood to identification, experiment planning and reduction; S67/S68 apply thermal likelihood/profile and observation/structure comparisons. S70 shows stable total resistance despite internal non-identifiability and warns that identifiable RC coefficients need not map to physical layers. S69 shows that temperature accuracy can coexist with input/bias-dependent parameter estimates. S26 already learns thermal structure in a Bayesian framework. A thesis must build beyond combining these established ingredients.

Uncertainty propagation alone is also insufficient novelty: S51 already propagates model/parameter choices toward thermal reliability criteria. Stochastic dynamics and epistemic uncertainty answer different questions. A fuller TRIDENT contribution would need justified input/observation uncertainty, discrepancy awareness, applicability and independent predictive consequences. Exact total uncertainty coverage cannot be inferred merely from chosen Monte Carlo distributions, a parameter posterior or filtered calibration bands.

## 6. Feasible scientific contributions and what would falsify them

The evidence supports candidate questions, not certified gaps. Literature need and local feasibility must both be established.

| Candidate aim | Established ingredients | Additional result worth pursuing | Feasibility/falsification |
|---|---|---|---|
| Identify supported loop quantities under sparse observations | Profiles, aggregate parameters, thermal networks, effective storage | A loop/model-class identifiability or invariance result with uncertain sources/observations, plus consequences for predictions | No-CFD core plausible if inputs/inventory and holdouts are supported; fails as novelty if it repeats known grouping with no additional result |
| Determine when added physical states/transport are justified | Wall/source sensitivity, conjugate models, order selection and reduction | A criterion predicting when omitted physics changes a declared QoI beyond tolerance across new conditions | Begin with measured thermal/duty/response QoIs; fails if complexity only improves calibration |
| Design and assess useful evidence for prediction | Bayesian design, profile-guided excitation and sensitivity ranking | Show which feasible protocol resolves a consequential ambiguity and improves independently assessed prediction | Must compare established design objectives; S71/S72 remain decisive prior-art checks |
| Bound local thermal consequences without overinterpreting sparse data | Local-flow studies and observation-dependent inference | A supported bound/reconstruction or a precise non-identifiability result for a defined descriptor | Requires independent local evidence for validation; otherwise retain as conditional extension |

A defensible minimum program can cover the approved stages of steady performance, transitions and operational assistance by progressively increasing predictive scope. It starts with a common input/state/output/observation contract and a small conservative hierarchy; then tests identification/uncertainty and selected withheld responses; finally communicates applicability and uncertain what-if predictions. Ben Booth/NeutronOS collaboration can deliver the last stage, but the interface is not the scientific advance.

This minimum does not assume new instruments or qualified TRIDENT CFD. If measurement support is weaker than hoped, a rigorous characterization of indistinguishable models or unsupported quantities can be useful, provided it is nontrivial and connected to an engineering consequence. If qualified CFD/local measurements arrive, use a few discriminating cases to test mechanism/observation hypotheses rather than automatically treating an entire field as ground truth. Resources and dissertation timing should determine how many QoIs and regimes can be assessed credibly.

## 7. Evidence still needed before a proposal-ready novelty claim

The next work is targeted technical closure, not another unrestricted search. S71/S72 must challenge prediction-oriented design/calibration; S73 must ground likelihood/noise implementation; S29 and, if obtained, S19/S74 must challenge the most similar contemporary loop/transfer claims. S24 and S03 support modern learned-model alternatives only if the available state data and constraints justify them.

Project evidence must establish fluid/properties/envelope, net deposited power and cooling duty, sensor calibration/coordinates/averaging, executed protocols, independent repeats/holdouts, and intended decision tolerances. Current draft experiment requests are not executed experiments. Bulk FlowTests5/6 stay excluded; this review pass does not process operating data or reconcile Ethan's thesis discrepancies.

The historical account remains scoped: no universal first-loop claim, no unverified numerical1969 MSRE test story, no alleged25% MSRE discrepancy as a generic motivation. The maintained dossiers/claim ledger preserve exact evidence and limitations. The next two prompts close the highest-value theory/comparator gaps, then consolidate the two comprehensive review drafts with a skeptical novelty and coverage audit.

## Decisive evidence update — batch A,21October2026

S19 and S74 now have purpose-scoped original-source dossiers. S19 compares external surface thermometry with steady CFD using measured thermal boundaries. Its velocities and wall-to-bulk profiles remain inferred; the reported5.5% concerns a difference between comparison discrepancies, not independently measured flow accuracy (S19-C01–C06,Table7/PDF8). S74 establishes modern multi-fluid H2TS comparison as prior art. Its matched-correlation Nu agreement is a construction/consistency result, not independent experimental validation (S74-C01–C08,Table4.10/PDF17). A proposed TRIDENT contribution must exceed these established calculations and define what independent evidence could assess its QoI under loss,storage,source and observation distortion.

S72 final article has been received; theory extraction of S71/S72/S73 and close-loop S29 continues in the next checkpoint. Earlier requests for S19/S74 are resolved.

## Decisive theory update — batch B

S71(arXivv2) establishes nonlinear target-information design with separate observation/target maps; EIG ranking is conditional on prior,noise,forward/prediction model and numerical estimation. S72(final) establishes goal-weighted calibration with a discrepancy fit nested within each physical-parameter choice; it explicitly leaves propagation to unobserved QoIs unresolved. Ordinary MLE wins its reported validation metric,although the article's Eq46 normalization needs clarification. S73 establishes continuous-time stochastic grey-box likelihood and sparse-observation filtering,including a two-state thermal-wall example; fitted diffusion and local curvature uncertainty do not identify missing mechanisms or ensure predictive coverage.

Thus goal-oriented design,goal-oriented calibration and stochastic thermal grey-box fitting are prior methods. The proposed contribution needs a narrower loop-specific result about identifiable QoIs,robust adequacy or uncertainty separation,assessed against these baselines. These theories support an experiment-request rationale using feasible existing inputs/times;they do not assume new sensors or CFD. See S71-C01–C09,S72-C01–C10,S73-C01–C08 and their dossiers.
