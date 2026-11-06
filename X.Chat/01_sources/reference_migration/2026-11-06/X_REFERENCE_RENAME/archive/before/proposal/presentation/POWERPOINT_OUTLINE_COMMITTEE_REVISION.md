# PhD proposal — physical reduction, justified closures and assessed SAM implementation

**Active working outline, revised November 6 after Cole/Clarno feedback.** Author: Andrés Nicolás Fierro López. Proposal and this Markdown presentation package are due **November 13 at noon**. The meeting slot is one hour; the script below is deliberately shorter to leave room for figures, derivations and discussion. Rehearsal must measure actual duration. No PowerPoint file is generated.

**Reading rule:** open the case table before a numerical figure. [Full model/BC/equation appendix](SIMULATION_ASSUMPTIONS.md), [actual input/code links](AS_RUN_INPUT_INDEX.md), [figure disposition](FIGURE_READINESS.md), [rehearsal/questions](NOV06_REHEARSAL.md). The compiled proposal contains the same case explanations in Appendix C. Earlier annotated text is preserved in the [pre-revision snapshot](../doc_support/committee/integration/2026-11-06/defensible_results/before/presentation/POWERPOINT_OUTLINE_COMMITTEE_REVISION.md).

## 1 — Predict heat transport with models we can explain

**On slide**

- Predict temperature, circulation and heat removal from specified operating inputs.
- Resolve the physical feature that changes the requested output.
- Generate justified closures; implement and assess them in SAM.
- Build from the master's CFD-to-1D reduction.

**Exact speaker notes**

“My proposed dissertation asks how much spatial and thermal detail a reduced loop model needs for a useful engineering prediction. The outputs are temperature, circulation, heat removal and response to an input change. I will start from the CFD-to-one-dimensional reduction developed in my master's thesis. The doctoral work goes beyond an internal solver: it must justify closures, reproduce the selected physical model in SAM, and establish where the resulting predictions are supported by evidence. I will distinguish completed methods, numerical comparisons and the experimental demonstration still to do.”

## 2 — The master's thesis is the completed foundation

**On slide**

- Reduce CFD fields onto explicit mass, energy and pressure bases.
- Solve a periodic steady loop for temperature and circulation.
- Keep thermal, hydraulic and sensor explanations separate.
- Use local heat budgets to assess a temperature fit.

| Master's method | Definition / source | Doctoral extension |
|---|---|---|
| CFD reduction | Declared sections, surfaces, signs and averaging; Chapters 2–3 | Qualify new fields before generating closures |
| Physical solver | Periodic steady energy solution plus buoyancy–loss root; Chapter 4 | Matched SAM implementation and numerical limits |
| Assessment | Temperature, circulation and regional heat paths; Chapters 5–6 | Independent conditions and physical uncertainty |
| What is shown here | Completed method and research conclusions; no new numerical case grade or figure | Quantitative thesis results need their own complete actual-run case record before being added |

**Scholarly source:** [Fierro López, master's thesis, current source and structure](../../Master_support/csem-Masters_thesis/README.md); [model definition](../../Master_support/csem-Masters_thesis/chapters/04_reduced_model_methodology.tex); [conclusions](../../Master_support/csem-Masters_thesis/chapters/06_conclusions.tex). The thesis remains the source owner. Conference contributions are optional supporting history, not the proposal's completed-work argument.

**Exact speaker notes**

“The strongest completed-work argument is my master's thesis. Its first contribution is a reproducible way to reduce spatial CFD fields to comparable one-dimensional mass, energy and pressure quantities. Its second is an executable steady loop model: the energy solution is periodic and the mass flow is adjusted until buoyancy balances pressure loss. The assessment then examines temperature, circulation and the locations where heat leaves the system. That last distinction matters: a temperature fit alone does not establish the correct heat path. Those methods and conclusions motivate the doctoral work. The next step is a justified model that survives implementation in another code and assessment on supported conditions.”

## 3 — The novelty must be a tested physical result

**On slide**

- Conservation, grey-box learning and identifiability tools already exist.
- Test when an added profile or storage state changes an engineering output.
- Test what sparse observations can constrain about that change.
- Deliver a justified closure or applicability limit, with a matched SAM case.

| Established method | Additional result we must demonstrate |
|---|---|
| Conjugate loop dynamics | Which thermal/flow detail is required in the selected loop regime |
| Output-oriented reduction | A loop-specific retention criterion with defensible closure/error bounds |
| Parameter / prediction profiling | A physically consequential supported-target limit under declared input and sensor information |

**Literature:** Cammi et al. (2016), `cammi2016wallinertia`; Kristensen et al. (2004), `kristensen2004greybox`; Raue et al. (2009), `raue2009identifiability`; Kreutz et al. (2012), `kreutz2012prediction`; Bui-Thanh et al. (2007), `buithanh2007goal`; Carlberg et al. (2018), `carlberg2018conservative`. Exact entries are in [main.bib](../main.bib); the literature review remains the closest-prior comparison, not proof of novelty.

**Research aims before the methods**

- **Justify and implement:** select the physical representation/closures and reproduce the chosen model in SAM.
- **Set and learn:** identify supported parameter combinations, boundaries and sensor maps.
- **Assess and bound:** test separate conditions, heat budgets, uncertainty, cost and applicability.

**Exact speaker notes**

“The three aims are to justify and implement the model choices, determine the parameters and observations needed, and assess the resulting predictions and limits. Those choices, parameters and validation tests must be explained together. The tools alone are not the novelty. Conservation, conjugate thermal models, parameter profiles and output-oriented reduction all have established literature. My proposed contribution is to connect a loop-specific physical feature to a supported prediction. One candidate is a criterion for when a scalar temperature description needs a profile or storage extension. A second is a limit on which engineering targets sparse observations can support. Either candidate must beat a simpler boundary correction or established profiling method. A useful negative result must identify a reproducible ambiguity, show its consequence for the target and say what evidence would resolve it.”

## 4 — Show the balances before the results

**On slide**

- States: fluid, pipe and optional insulation temperatures.
- Transport: signed upstream enthalpy plus selected conduction.
- Exchange: each internal heat transfer enters two balances with opposite signs.
- Circulation: buoyancy equals pressure loss in a steady natural-circulation solve.

For cell index $i$, let $F_i,P_i,S_i$ be fluid, pipe and insulation temperatures [K]; $H_i$ face enthalpy rate [W]; $c_i,a_i,g_i,w_i$ conductances [W/K]; and $q_h,q_c,q_a$ heater, cooler removal and signed room heat input [W]. The canonical **steady** balances are

$$
\begin{aligned}
0&=H_{i-1}-H_i+c_{i-1}(F_{i-1}-F_i)+c_i(F_{i+1}-F_i)+g_i(P_i-F_i),\\
0&=a_{i-1}(P_{i-1}-P_i)+a_i(P_{i+1}-P_i)+g_i(F_i-P_i)+w_i(S_i-P_i)+q_{h,i}-q_{c,i},\\
0&=w_i(P_i-S_i)+q_{a,i}.
\end{aligned}
$$

With mass flow $\dot m$ [kg/s], specific enthalpy $h$ [J/kg] and pressure differences [Pa],

$$
H_i=\max(\dot m,0)h(F_i)+\min(\dot m,0)h(F_{i+1}),\qquad
\Delta p_b(\mathbf T(\dot m))=\Delta p_{loss}(\dot m,\mathbf T(\dot m)).
$$

**Backup:** proposal Chapter 3 and Appendix B provide the continuum reduction, all retained/omitted terms, units and equation-to-implementation ledger. The transient S1 extension is specified separately on slide 6 and Appendix C.

**Exact speaker notes**

“This is the steady model I mean when I describe the canonical thermal network. Each cell has a fluid temperature and a pipe temperature, with an insulation state when represented. The fluid receives upstream enthalpy, axial conduction and heat from the pipe. The pipe receives the heater source and exchanges heat with adjacent pipe cells, fluid, insulation and cooler. The insulation connects the pipe to the environment. Internal transfers cancel when the balances are summed. At specified flow this is a thermal solve. In steady natural-circulation mode I also solve the signed pressure balance. These equations do not claim a transient solution; storage is an explicit addition in the separate benchmark I will show.”

## 5 — State what is fixed, uncertain and fitted

**On slide**

- A fixed value is not automatically an accurately known physical value.
- Start from a named correlation with its applicable regime.
- Separate boundary, hydraulic and sensor corrections.
- Fit a small named parameter set; assess it on another condition.

| Quantity | Initial treatment | Needed before physical interpretation |
|---|---|---|
| Geometry / inventory | Revision-qualified nominal configuration | Installation and dimensional uncertainty |
| Material laws | Named original source and temperature/composition range | Product/composition match; extrapolation and dependence |
| Heat input / cooler / ambient | Recorded histories and accepted nominal heater definition | Source placement, allocation, initial state and uncertainty |
| Friction / film | Named law, convention, geometry and development range | Evidence of applicability; no blanket confidence label |
| Regional loss parameters | Small proposed effective set | Bounds, heat budget and separate-condition assessment |
| Probe map | Location, surface, footprint and response defined first | Installation and observer uncertainty |

For hydraulic diameter $D$ [m], area $A$ [m²], viscosity $\mu$ [Pa s] and fluid conductivity $k_f$ [W/(m K)],

$$
Re=\frac{|\dot m|D}{A\mu},\qquad h_i=\frac{Nu\,k_f}{D}.
$$

A circular-tube laminar Darcy reference is $f_D=64/Re$; zero/reversed flow requires the finite signed pressure-product form, not division by zero. The selected Nusselt/development law must be stated for each physical case. **Source:** [master's model, thermal and pressure closure sections](../../Master_support/csem-Masters_thesis/chapters/04_reduced_model_methodology.tex).

**Exact speaker notes**

“Before tuning I need to separate four roles. Some quantities are specified inputs. Some have independent measurements with an uncertainty basis. Others are uncertain working assumptions. A small subset may be estimated from data. Those roles are not interchangeable. I will identify the original source and regime of each property and correlation. Reynolds number organizes the friction regime; Nusselt number relates the selected thermal closure to the film coefficient. A developing or recirculating region may require more than the fully developed reference. I will not repair a sensor-location or boundary-input error by silently tuning a film coefficient.”

## 6 — S1 setup: a transient thermal implementation test

**On slide**

- Synthetic primary loop; no experimental temperatures or fitted parameters.
- Same frozen thermal inputs; initialized circulation persists.
- Compare two thermal discretizations and axial refinement.

| Case S1 item | Actual specification |
|---|---|
| Model | Transient Trident finite-volume benchmark extension and SAM PBPipe/solid heat structures; canonical M1/M2/M3 remain steady |
| Unknowns | Fluid-cell and solid-shell temperatures; no resolved fluid radial/angular profile |
| Geometry | Working Rev9 primary path; 38 components, 5.50314 m length, 26.64 mm bore; nominal selected sensor positions |
| Solids / paths | Steel + fiberglass/ceramic as selected; perfect contact; within-component solid axial conduction; no solid conduction across component ends; fluid axial conduction off |
| Source / initial state | 100 W **in steel**; all temperatures initially 300 K |
| Boundaries | Ambient 295 K, bath 290 K; inner/bath films 100 W/(m² K); exterior 9.77808 W/(m² K), including frozen radiation |
| Flow / pressure | Initial velocity 0.01 m/s; gravity, drag and bend losses zero; periodic primary with one 101000 Pa gauge datum; no natural-circulation test |
| Properties / fitting | All constants frozen; full fluid/solid table in appendix; nothing fitted |
| Mesh | 88 / 176 axial elements; steel 3 / insulation 4 radial subdivisions where present |
| Time | Backward Euler, requested 1 s; baseline 851 accepted steps, 0.5–1 s; refined 850 steps of 1 s; horizon 850 simulated seconds |
| Outputs | PTC1–4 nominal primary-fluid and STC1–12 outside-steel model outputs; not experimental readings |

Let $\mathbf T$ be thermal states [K], $\mathbf C$ capacities [J/K], $\mathbf A$ conductances/transport [W/K] and $\mathbf b$ sources/boundaries [W]. The transient extension solves

$$
\mathbf C\dot{\mathbf T}=\mathbf A(\dot m)\mathbf T+\mathbf b,\qquad
(\mathbf C/\Delta t_n-\mathbf A)\mathbf T^{n+1}=\mathbf C\mathbf T^n/\Delta t_n+\mathbf b.
$$

**Before showing the result:** [full S1 model and numerical table](SIMULATION_ASSUMPTIONS.md#s1--what-exactly-was-compared-in-sam006), [archived actual deck](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/SAM006/baseline_as_run.i), [baseline exact overrides](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/SAM006/heated_forward/resolved_case.json), [refined exact overrides](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/SAM006/heated_axial2/resolved_case.json), [all inputs/code/output records](AS_RUN_INPUT_INDEX.md).

**Exact speaker notes**

“This case asks a narrow question: do two thermal implementations agree when their selected inputs are the same? It uses synthetic conditions. The heater deposits one hundred watts in steel. All thermal states begin at three hundred kelvin, with a two-hundred-ninety-five-kelvin room and a two-hundred-ninety-kelvin cooler bath. The fluid and solid properties are frozen. Gravity and drag are disabled, so the initialized flow persists; this does not test natural circulation. The Trident benchmark includes thermal storage and advances a backward-Euler system on the actual accepted SAM time grid. It is separate from the canonical steady hierarchy. I compare the baseline and a doubled axial mesh with other inputs unchanged. The full table and executed inputs are available before interpreting the plot.”

## 7 — S1 result: compare the same final outputs

**On slide**

- At 850 simulated seconds, compare all sixteen declared model outputs.
- Largest endpoint difference: **0.13143 K → 0.05840 K** with axial refinement.
- This supports the specified thermal implementation comparison.

**Case definition:** slide 6; [full assumptions](SIMULATION_ASSUMPTIONS.md), [saved comparison data](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/SAM006/comparison.json). No fit, measured observation or natural-circulation claim is added here.

![S1 synthetic thermal comparison at 850 simulated seconds. Top: SAM and Trident baseline temperatures in kelvin at four nominal fluid and twelve outside-steel outputs. Bottom: Trident minus SAM in kelvin, baseline and axial-refined. Station order is categorical, not distance. Model and boundaries are specified on slide 6; source is the pinned SAM006 comparison.json.](assets/defensible_results_2026-11-06/S1_endpoint_comparison.svg)

**Exact speaker notes**

“The top panel shows the baseline final temperatures from SAM and the Trident thermal extension at the same declared locations. The lower panel shows their difference, so the small discrepancy remains visible. PTC labels are primary-fluid model outputs; STC labels sample outside steel. These are categorical stations, not evenly spaced axial coordinates or experimental measurements. The largest absolute final-output difference falls from about thirteen hundredths of a kelvin to about six hundredths with the declared axial refinement. That is an implementation result for this fixture. Eight hundred fifty seconds is simulated time, not runtime. The old PTC4 curve mixed sparse reporting snapshots with a maximum over all accepted steps; I removed that confusing comparison from the main story. Its exact definition remains in the appendix.”

## 8 — R1: show the backward calculation honestly

**On slide**

- Recover the historical heated-window resistance calculation and its code.
- An outer material/exterior assumption anchors the absolute heat scale.
- Reconstructing the same temperatures checks algebra; prediction needs another test.

| R1 input / assumption | Value / meaning |
|---|---|
| Record and geometry | September 17 nominal 248–258 min; historical Rev8, material-v3, provisional sensor join |
| Fluid proxy / outside steel / air | 50.0734 / 48.1763 / 20.9099 °C; fluid is a height-interpolated proxy, not local measured bulk |
| Outer resistance | $R'_o=6.52424$ m K/W from material/exterior assumptions |
| Fixed exterior / contact | Convection 5 W/(m² K), emissivity 0.8, radiant temperature=air; perfect contact; reference 323.15 K |
| Omitted mean terms | Storage, axial redistribution and additional environmental heat assumed negligible, not proven negligible |
| Unknowns and status | Effective inner resistance and outward line heat conditional on the anchor; not a new fit or native network simulation |

For temperatures $T_f,T_w,T_a$ and per-length resistances $R'_i,R'_o$ [m K/W],

$$
q'=\frac{T_w-T_a}{R'_o}=4.17924\;\mathrm{W/m},\qquad
R'_i=R'_o\frac{T_f-T_w}{T_w-T_a}=0.45394\;\mathrm{m\,K/W}.
$$

The same-data forward algebra is

$$
T_w=T_a+q'R'_o,\qquad T_f=T_w+q'R'_i.
$$

**Sources:** [full R1 explanation](SIMULATION_ASSUMPTIONS.md#r1--conditional-resistance-inference-and-the-missing-full-circle-test), [issued original method](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/RESISTANCE/METHODS.md), [actual calculate script](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/RESISTANCE/as_used_sources/runs/2026-10-21_CAL-014_sep17_conditional_resistances/calculate.py), [cached means and roundtrip](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/RESISTANCE/roundtrip.json), [all inputs](AS_RUN_INPUT_INDEX.md).

**Exact speaker notes**

“This is the resistance calculation I can recover from the existing heated-record work. It uses a fluid-temperature proxy, an outside-steel temperature and ambient temperature. The outer resistance comes from a chosen material and exterior model. Given that anchor, the wall-to-air difference determines a line heat rate, and the fluid-to-wall difference determines an effective inner resistance. That inner path includes steel and the fluid-proxy relation; it is not a separately measured bulk film. Substituting those values back reconstructs the same temperatures by construction. It checks the algebra and units, but it does not independently validate the resistance. Storage and unmodeled environmental heat have not been established negligible. Those qualifications determine what can be used in the next forward study.”

## 9 — Close the loop: infer boundaries, then solve forward

**On slide**

- Qualify one heated experimental case and its initial state.
- Infer only the supported boundary quantities.
- Run Trident and SAM with the **same surface-specific boundary**.
- Freeze the model; assess another complete condition without retuning.

![Proposed full-circle demonstration. Experimental record feeds backward inference, then two matched forward implementations, then an independent-condition assessment. Historical local inversion/algebra is documented; Trident/SAM whole-network replay and the independent test remain pending. This is a study plan, not simulation output.](assets/defensible_results_2026-11-06/R1_full_circle_plan.svg)

| Stage | Required output | Completion criterion |
|---|---|---|
| Case preparation | Date/channel/geometry/input/initial-state table | Every displayed observation and boundary has a source and role |
| Inverse boundary | Named resistance/conductance group, anchor and uncertainty/dependence | Supported parameter combination; no unsupported absolute identification |
| Matched forward replay | Two input decks, balance tables and sensor-output plots | Both converge; heat/mass/numerical gates pass; same boundaries and observation definitions |
| Independent assessment | Frozen model, separate full condition, prediction errors and uncertainty | Tolerance and reference resolution fixed before assessment; failures retained |

**Critical surface rule:** a fluid-only CFD wall coefficient includes unmeshed steel/insulation/exterior resistance. If SAM represents those solids explicitly, impose only the remaining exterior boundary. Overall conductance at that exterior would count the solids twice. [R1 surface conversion and pending-case specification](SIMULATION_ASSUMPTIONS.md).

**Exact speaker notes**

“This is the full-circle demonstration requested in the feedback. First I must assemble one supported heated case, including input histories, channel identity and initial state. The inverse step produces only the boundary quantities the data and anchor can support. I then encode the same physical boundary in Trident and SAM and run both forward. The surface matters: a coefficient for a fluid-only CFD wall includes solid paths that an explicit-solid SAM model already solves. I must remove those represented paths before setting the SAM exterior film. After the reconstruction case works, I freeze the choices and assess a separate condition. The two-code network replay and independent test are deliverables still to complete; I am not presenting the local algebra as though they were done.”

## 10 — S2: diagnose the TAMU SAM implementation before claiming a prediction

**Case table — read before the outcome**

| Item | Actual S2 choice |
|---|---|
| Model | Original 46-component scalar Salt2 source, not later profile ROM; fluid pressure/velocity/temperature plus explicit solids, 4268 unknowns |
| Input / source | Source geometry, property tables and frozen friction/films; 265.7 + 37 = 302.7 W **in fluid** |
| Exterior / initial state | Source-derived Robin drive and source-model initialization; pressure datum; not measured secondary/room state |
| Method | Steady FD, PJFNK and assembled NEWTON; no time step; follow-ups use 20 nonlinear iterations, relative/absolute tolerances $10^{-9}/10^{-7}$ |
| Fit and acceptance | No experimental fitting; positive convergence marker and full outputs plus energy 0.006 W, mass spread $10^{-5}$, reference temperature 1 K and reference flow 5% gates |
| Interpretation | Numerical/source reproduction only; property table interval is not phase qualification |

**Actual inputs:** [FD deck](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/TAMU/original_FD/baseline/input.i), [PJFNK deck](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/TAMU/2026-11-06_SPR-004_tamu_baseline_diagnosis/pjfnk_baseline/input.i), [NEWTON deck](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/TAMU/2026-11-06_SPR-004_tamu_newton_discriminator/newton_baseline/input.i), [resolved invocations](../doc_support/committee/integration/2026-11-06/defensible_results/inputs/TAMU/recorded_invocations.json), [full model/limits](SIMULATION_ASSUMPTIONS.md), [source/code index](AS_RUN_INPUT_INDEX.md).

**On slide**

- **No accepted full-loop root.** FD timed out; follow-ups reached their nonlinear iteration cap.
- Process exit zero is insufficient; saved candidates are excluded from prediction figures.
- Next: accepted scalar reproduction, then closure comparison, then experimental assessment.

**Exact speaker notes**

“The TAMU implementation is a different case. It reproduces the original scalar Salt2 source, with forty-six components and explicit solids. The specified three hundred two point seven watts goes into fluid in this source model, unlike the steel source in S1. The exterior drive is a source-model equivalent, not a measured cooling-air temperature. These were steady root attempts, so there is no time step to report. The original finite-difference attempt timed out. PJFNK and assembled Newton follow-ups reached their nonlinear cap even though the program returned zero. None passed the required convergence and engineering gates. I therefore have no accepted full-loop prediction to plot. The immediate milestone is a converged, balanced scalar reproduction under unchanged inputs, followed by a physically justified comparison.”

## 11 — Distinguish available data from expected data

**On slide**

- Start with the master's evidence, heated VCU records and working CAD.
- Reconstruct one complete input/observation case before a large fit.
- Use Luciano's phases to request the missing evidence.
- External CFD and experiment delivery dates remain unconfirmed.

| Evidence | Available now | Needed next |
|---|---|---|
| Master's / TAMU | Model, reduction and issued assessment; WGL archive setup/inventory located | Qualify matching fields/planes/windows and numerical accuracy before a new spatial result |
| Heated VCU | Historical temperatures, cached conditional results, nominal heater specification, working geometry | Join dates, installation, channels, heater/cooler/ambient history and initial state |
| Luciano phases | Phase 0 checkout, 1 baseline, 2 relaxation, 3 thermal anchors, 4 transitions/repeats are a proposed route | Lead-confirmed settings and acquisition; compatible heated anchor/shutdown and independent restart |
| Extra observations | Outer-insulation instruments reported ordered | Installation, mapping and received records; not yet measured inputs |
| VCU / ACU CFD | No qualified spatial reference available | Actual case, boundaries and resolution/conservation evidence |

**Internal preparation sources, not scholarly citations:** [phase-source index](/scratch/09748/andresfierro231/projects_scratch/Trident/andrew_WorkSpace/trident_modeling_initiative/box/Trident_FlowLoop_Notes/reference/Nick_luciano_exp_plan/2026-09-14/README.md), [requirements and current phase/nominal-power amendments](/scratch/09748/andresfierro231/projects_scratch/Trident/andrew_WorkSpace/trident_modeling_initiative/docs/experiments/RESEARCH_DATA_REQUIREMENTS.md). No experiment or CFD campaign is launched by this outline.

**Exact speaker notes**

“I can begin with existing material, but a file inventory is not yet a complete assessment case. The first physical target is a heated VCU record with a useful thermal signal. Near-ambient records are deferred because window heating can dominate their small temperature differences. The heated case still needs its date, installation, channels, operating histories and initial state joined. Luciano's phase plan provides a route from checkout and baseline quality to relaxation, thermal anchors and transitions or repeats. I need a compatible heated anchor and shutdown, plus a separately initialized assessment condition. Extra instruments and facility CFD are expected inputs, not received data or promised dates. The schedule must continue useful work while those dependencies are resolved.”

## 12 — CFD is a reference only after its physics is qualified

**On slide**

- Read the actual equations, turbulence/wall model and boundaries.
- Match surfaces, averaging and conservation quantities to the ROM target.
- Check spatial/time resolution before learning a closure.
- Exclude poor CFD; continue bounded thermal work if no CFD arrives.

**Two-sentence explanation to be able to give:** OpenFOAM can run laminar, Reynolds-averaged or large-eddy formulations; its name does not tell us which model was used. NekRS uses a high-order spectral-element formulation and supports filtered LES, so a RANS–LES comparison may change modeled/resolved scales and wall fluxes; neither code name alone establishes a superior reference.

**Primary sources:** [OpenFOAM turbulence-model selection](https://doc.openfoam.com/2306/tools/processing/models/turbulence/), [Argonne Cardinal/NekRS LES filtering](https://cardinal.cels.anl.gov/theory/les_filter.html). These describe methods, not the installed TAMU case configuration.

| Dependency | Required check | If unavailable / unsuitable |
|---|---|---|
| Facility CFD | Geometry, properties, actual input/BC/IC files and source placement | No facility-profile or recirculation conclusion |
| Reduced quantities | Same planes, signs, areas and time windows | Do not interpret different integrations as closure error |
| Numerical quality | Convergence, regional/global conservation, mesh/time sensitivity of target | Repair or exclude; do not fit its error |
| No qualified CFD | Supported thermal records and conventional correlations | Assess SAM implementation, loss/storage and sensor maps; keep spatial superiority unresolved |

**Exact speaker notes**

“The difference between OpenFOAM and NekRS can matter, but I need to identify the actual formulation. OpenFOAM supports laminar, Reynolds-averaged and large-eddy cases. NekRS uses spectral elements and can apply LES filtering. If one case uses RANS and another LES, they represent unresolved motion differently; that can affect the profiles and wall fluxes I want to reduce. A code name is not a quality ranking. I will first match physical boundaries, properties, surfaces and averaging, then check conservation and numerical resolution for the requested quantity. If facility CFD is absent or unsuitable, I continue the thermal and SAM studies but do not claim a facility-profile or recirculation result.”

## 13 — A model temperature is not automatically a sensor temperature

**On slide**

- Define the surface, position, footprint and response.
- Distinguish area temperature, transported enthalpy and local probe output.
- Change the observer before adding free physical coefficients.

Let $\mathbf x$ be physical states, $\theta$ physical parameters, $\eta_j$ sensor location/contact/response quantities and $\epsilon_j$ measurement/model error [K]. A declared observation is

$$
y_j(t)=\mathcal H_j[\mathbf x(t),\theta,\eta_j]+\epsilon_j(t).
$$

For section area $A$ [m²], velocity $u$ [m/s] and density $\rho$ [kg/m³],

$$
T_A=\frac1A\int_A T\,dA,\qquad
T_H=\frac{\int_A\rho uT\,dA}{\dot m}.
$$

$T_H$ is a temperature-equivalent enthalpy average only for constant $c_p$; otherwise integrate enthalpy. Near zero net flow compare signed fluxes rather than divide by $\dot m$.

**Source:** JCGM GUM-6 measurement-model guidance, `jcgm2020measurementmodels`; [master's reduction](../../Master_support/csem-Masters_thesis/chapters/02_thermal_fluids_and_reduction.tex). No manufactured profile or installed-probe qualification is presented as a physical result here.

**Exact speaker notes**

“A local probe, an area average and a transport average answer different questions. The area average weights geometric area. The transport average weights signed mass flow and, with variable properties, must use enthalpy directly. A probe instead samples its installation and may have contact or response effects. I will make that observation map explicit before fitting a regional loss or film parameter. Otherwise a coefficient may compensate for a measurement interpretation error. The detector work must also identify the actual plane, footprint and units. Numerical interpolation checks do not qualify an installation. The assessment will compare observation maps with the physical model and allowed inputs held fixed.”

## 14 — Assess predictions, heat budgets and uncertainty together

**On slide**

- Fix the target and tolerance before assessment.
- Withhold a complete condition or transition.
- Report local/global heat budgets with temperature and circulation.
- Carry input, observer, parameter and numerical uncertainty; retain failures.

| Measure | Required report |
|---|---|
| Temperature | Bias/RMSE by mapped channel and condition; trajectory and extrema definitions |
| Duty / circulation | Error only against a qualified reference, with source/input uncertainty |
| Physical consistency | Regional and whole-loop energy balance; mass balance; source/surface ownership |
| Numerical error / cost | Spatial/time refinement, convergence and paired runtime/problem size |
| Usefulness | Tolerance tied to decision/reference resolution; bounded applicability and rejected cases |

**Literature:** Oliver et al. (2014), `oliver2014unobserved`; JCGM covariance and measurement models, `jcgm2011vectorcovariance`, `jcgm2020measurementmodels`; parameter/prediction profiling, `raue2009identifiability`, `kreutz2012prediction`.

**Exact speaker notes**

“The assessment must answer whether the output is useful, not just whether a curve looks close. I will set a target, a tolerance and a separate complete assessment condition. Temperature residuals will be reported by channel, together with circulation or duty only where the reference supports them. Regional heat budgets test whether a good temperature result came from the right heat path. Numerical error is bounded before attributing a difference to model form. Uncertain input scales, initial states, properties and sensor maps may be correlated, so I will not vary them independently by default. Unsupported uncertainty is reported as missing, not zero. Failed solves and phase or range violations remain part of the result.”

## 15 — Run the research tracks in parallel

**On slide**

- Start model/SAM, heated-case preparation and detector maps together.
- Use evidence gates for spatial claims and independent prediction.
- Write and preserve reproducible case records throughout.

![Proposed twelve-month research schedule with overlapping equation/case audit, closures and SAM, heated-experiment replay, CFD/profile assessment, detector/uncertainty, independent assessment/transfer and writing. Bars indicate work periods, not external data commitments. Source: proposal research plan; no simulation data.](assets/defensible_results_2026-11-06/parallel_research_plan.svg)

| Review gate | Concrete packet | If evidence is delayed |
|---|---|---|
| Months 1–2 | Complete model/case appendix, accepted scalar reproduction, heated-case input table | Keep root/ledger diagnosis and conditional preparation explicit |
| Months 3–5 | Closure-source dossier, two-code replay, spatial/observer comparison where qualified | Continue conventional-correlation thermal work; no unsupported profile claim |
| Months 6–8 | Frozen model, independent condition, uncertainty and limits | Report bounded methods result if independent data are missing |
| Months 9–10 | Paired accuracy/cost, facility transfer matrix and operator-reviewed scenario | Offline replay with explicit facility applicability |
| Months 11–12 | Dissertation, figures and reproducible evidence package | Narrow unsupported claims; finish the tested result |

**Exact speaker notes**

“This is a parallel research plan. Equations and case documentation begin with closures and SAM implementation, while heated-case reconstruction and detector definitions proceed alongside them. Spatial comparisons depend on qualified CFD; independent prediction depends on a separate supported condition and a frozen model. Those dependencies control the claims, not whether every other task stops. If CFD is late or poor, I continue conservative thermal implementation, resistance boundaries, loss and storage information, and sensor mapping. If independent experiments are missing, I do not substitute a reconstruction for prediction. Writing and input preservation run throughout, so each review packet contains a teachable result, the full case and the next evidence decision.”

## 16 — Next review: one explained case and one concrete decision

**On slide**

- **Done:** master's reduction; documented S1 implementation comparison; recovered R1 algebra/code; diagnosed S2 failure status.
- **Next:** qualify one heated input/observer case and complete matched forward replay.
- **Research test:** justify a closure/state choice and assess its consequence independently.
- **Review request:** agree the first output, evidence route and criterion for success.

**Exact speaker notes**

“The next review should be built around one fully explained case. I can now show the master's method as the foundation, a specified synthetic thermal comparison, the actual resistance inversion and the unresolved TAMU numerical result. The next physical demonstration is the heated-case reconstruction followed by matched forward Trident and SAM calculations. Beyond that, the doctoral result must justify a closure or retained state and show its consequence on an independently assessed output. I would like the committee's guidance on the first output that matters most, whether this evidence route addresses it, and the criterion that would make the result convincing.”

## Technical backup and material to add only after qualification

- **Complete equations and model forms:** proposal Chapter 3, Appendix B continuum reduction and Appendix C case records; [Markdown assumptions](SIMULATION_ASSUMPTIONS.md).
- **PTC4/reporting/dt:** S1 appendix explains accepted integration steps versus five reporting snapshots and maximum over the full accepted grid. The active figure uses only final outputs.
- **Actual source files:** [input index](AS_RUN_INPUT_INDEX.md). Original as-run SAM deck is different from the later diagnostic template.
- **R1 resistance-to-boundary surface:** use wetted-wall overall resistance only when those solids are not meshed; do not double count explicit solids.
- **Master's numerical result figure:** add only with the exact selected model/CFD case, all BC/IC/closure/tuning/observer/numerical tables and original inputs. The completed-method slide is usable now; unpublished case reconstruction is not implied.
- **Withheld numerical families:** [disposition ledger](FIGURE_READINESS.md). Original plots remain historical sources outside the active talk/PDF. They are not unexplained backup slides.
- **Explanation placeholder:** expand the chosen full-circle case into the final experimental result slide when both forward implementations and case-specific physical gates are complete. Do not fill this with another generic count of passed checks.
