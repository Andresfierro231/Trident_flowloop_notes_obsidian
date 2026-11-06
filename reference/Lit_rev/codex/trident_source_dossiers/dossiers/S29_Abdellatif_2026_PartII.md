# S29 — Therminol-66 surrogate natural-circulation loop,Part II

Extraction21October2026. Hossam H.Abdellatif,Joshua Young,David Arcilesi,Richard Christensen,*Preliminary Experimental Validation of Single-Phase Natural Circulation Loop Using Surrogate Fluid for Molten Salt Based on CFD Model to Support R&D of MSRs: Part II*. *Journal of Nuclear Engineering*7(3),45,published6July2026. DOI https://doi.org/10.3390/jne7030045 . Published36-page article;PDF=printed1–36. Stable S29 retained for this exact PartII DOI; not PartI,not the2025thesis,and not S74 similarity paper.

## Identity/completeness/version and scope

First-page title/authors,DOI,received13April2026/revised22June/accepted28June/publication6July2026 and complete Sections1–7 agree. **Internal metadata inconsistency:** footer says “J.Nucl.Eng.2025,7,45” throughout although first-page publication is2026. Do not silently use the footer year or claim it is a2025published article. Publisher web recheck returned429 this pass; local publisher typeset PDF is the technical original read. Earlier repository metadata remains a separate provenance record. Main text1–31 read;abbreviations/nomenclature31–33 inspected;references33–36 inspected for lineage/discovery. Selected pages7,9,11,14–15,18,21,23,26,28–30 rendered;7/28/30 visually inspected,and critical figures/properties checked below. No separate appendix/supplement appears. Underlying time series,CFD files,calibration raw records and manufacturer source tables not supplied/read. Ready for scoped loop-motivation,observation/validation and closest-prior-art synthesis,not reproduced CFD or a full reactor-transfer claim.

## Problem and what is actually established

Authors claim the first experimental/numerical Th-66 investigation **in this facility**,and compare measured temperatures/indirect flow with a3D Fluent model,with/without distributed external losses. This establishes a close laboratory precedent for oil-loop experiments,CFD comparison,loss effects and practical limitations. It does not establish the first surrogate loop in the field or independently validate local flow structures. Prior water/RELAP5work is PartI[17];facility/thesis[18];similarity assessment[30] is **S74**,so that is a linked prior methodology,not an independent corroborating experiment.

Historical/MSR claims in the introduction are cited background. Its early-1960s “first MSR” description must not replace original ARE/MSRE chronology already treated in the motivation review. Current ARIS design counts and toxicity statements are not adopted as verified current facts. The experiment’s plausible mission is selected thermal-hydraulic mechanism/model assessment and passive heat-removal response,conditional on similarity,not a complete nuclear-reactor demonstration.

## Facility,conditions,instruments and data

§2/Table1/Fig4,PDF5–9: VHVC loop,SS316Schedule80nominal2.5-inch pipe,ID59mm,OD73.03mm,600lb flange connections;ceramic-glass insulation14–20mm. Immersion heater rated4kW plus2kWguard heater;electrical supply limits actual maximum~5kW. Table1 “maximum heater power4000W” describes immersion component,not total installed6kW. Cooler has eight copper tubes,ID7.75mm/OD9.53mm,nominal19-inch length;primary Th-66inside tubes,secondary countercurrent water on shell. Prose mixes “1/4-inch tubing” and.38-inch OD;use explicitTable1dimensions and flag unresolved nominal wording. Fig4contains component dimensions;no single fully reconciled total hydraulic-length/resistance model extracted. L-shaped accumulator permits filling/expansion;design2MPa is distinct from test5–50psig. Four CFD cases use22psig(Table5/PDF17).

SixRTDs,two five-pointKTCprobes,three pressure transducers/two gauges;cooling-water flowmeter,power instrumentation.10s acquisition;steady-state mean window30–60min,reported dT/dt~1e−4°C/s sustained30min;typically one/two repeats with boundary-related retests. No independent primary flowmeter—§6/PDF30 proposes installing one later. A five-point temperature probe is not direct velocity metrology.

Table5/PDF17CFD cases:500/800W with secondary.063kg/s,CW inlet18/20°C;1000/1500W with.126kg/s,CW inlet16/15°C. Power and cooling conditions change together,so cross-case power trends are not one-factor causal tests. Experimental transients described onPDF9–10include loss/recovery of heat sink,power reduction1500→108W,and multistep power/passive cooling;their presence in protocol is not complete CFD transient validation.

## Governing relations and uncertainty

Eq3/PDF9 infers primary mass flow from cooler heat balance: mdotp=mdotCW(hCW,out−hCW,in)/(hp,in−hp,out),kg/s with h J/kg. It assumes appropriately matched bulk enthalpies and no unaccounted cooler/storage/ambient duty. Using local RTD temperatures as bulk values requires an observation model;during transients,wall/fluid storage invalidates the steady equation unless included. Eqs4–13/PDF10–12 report mdot=ρvA;Q=mdotΔh;buoyancy head≈(ρc−ρh)gH balanced against (fL/D+K)mdot²/(2ρA²). f is Darcy64/Re or.316Re^−.25;feff=f0(1+αDen),De=Re√(D/(2Rc)). α,n are from correlations or calibration,but a unique numerical set/full loop application is not supplied. For different-area branches/components,one velocity/area cannot be applied indiscriminately. Head-loss formula uses positive flow magnitude;reversal requires a signed convention. Qelec−Qloss=mdotcpΔT is a steady heater control-volume approximation,not a whole-loop transient conservation equation.

Table2/PDF9 lists±.101/.225°C RTD,±.123/.344°C coolingTC,±5%secondaryflow,±1%pressure,±3.2%ammeter. Coverage factors,systematic covariance,enthalpy/property uncertainty and run-specific propagated budgets are not completely specified. Fig21/PDF28labels energy-flow±5.22%;the paper does not show a sufficiently reproducible full covariance propagation deriving this value for every operating case. **Our propagation reminder:** mdot=Q/Δh implies u²(mdot)/mdot²≈u²(Q)/Q²+u²(Δh)/Δh²−2cov(Q,Δh)/(QΔh);this is a local linearization,not the source’s demonstrated calculation. Missing heat-balance terms and point-to-bulk bias are outside a sensor-only RSS budget.

**Instrumentation convention flag:** Eqs1–2/PDF8give current-to-pressure slopes54,389.15and31,343.9and offsets−217.557/−125.072 while prose calls x current in mA. Substitution x=.004/.020A gives plausible4–20mAinstrument endpoints;substitution4/20mAwithoutconversion does not. Do not implement the labeled unit literally without calibration records.

§4.4/Eqs19–22/PDF18–19 property fits use **T°C**:ρ=1020.166430−.613T−3.254e−4T²kg/m³;cp=1496.195426+3.2983T+9.52745e−4T²J/(kgK);k=.11829−3.27434e−5T W/(mK);μ=54.94979/T^2.077 Pa s,stated30–360°C. Source manufacturer recommended bulk limit345°C narrows a practical range;no TRIDENT operation recommendation made. ActualCFD uses piecewise linearρ/k/cpandpower-lawμ,not all printed fits directly. Regression R²/95%fitbands do not establish property accuracy or total prediction coverage. Small absolute μ does not imply negligible relative Re/Pr uncertainty.

## CFD and validation independence

§4/PDF12–20:Fluent2023R2,SSTkω,curvature correction,viscous heating,coupled pressure/velocity,second-order spatial schemes;meshes2.62/4.44/6.83millioncells,heat-transferwallsy+<1,plate up to~1–1.5onfinest. Full governing/closure equations and all gravity/density/initial-condition choices are not documented as a reproducible case file;the analytical balances are not the complete CFD equations. No validated universal turbulence-closure ranking follows.

§4.1/PDF14–16 compares meshes using experimental temperature/error metrics and selects the mesh with smallest disagreement. Time steps1/2/3s;2s chosen partly for closest experimental value at3000s. Eq18half-mesh-spread is a sensitivity proxy,not Richardson/GCI asymptotic uncertainty or a rigorous bound. Nonmonotone agreement with experiment does not establish numerical convergence. Numerical verification and model-selection evidence are intertwined;no locked independent selection/validation partition demonstrated.

§4.5/PDF20uses Churchill–Chu external-convection correlations at fixed20°Cambient,Ra based on verticalL/horizontalD,Qloss=hA(Ts−T∞),implemented as wall flux. §5/PDF21also says h4–6.5W/(m²K)based on priorRELAP5. Conclusion calls losses “measured” (PDF30),but an independently measured heat-loss distribution/calibration budget is not demonstrated here. Insulation/interface/radiation treatment and the two h descriptions need clarification before reuse. Cited originals establish correlation pedigree;they were not read in this pass. No claim that model-development agreement is independent loss identification.

## Results and strongest limitations

At800W,source reports heater-outlet RMS7.60°C(loss)vs15.93°C(adiabatic),PDF21–22. Approximate settling time CFD10000s vs experiment25000s(PDF22)shows a material dynamic mismatch despite qualitative trend agreement. CFD flow~.039kg/s(loss)or.058(adiabatic)vs inferred~.01(PDF23/Fig15). These quoted values are source approximate readings,not digitized new measurements. Local fieldsFigs16–18/PDF24–26are modeled distributions;temperature/velocity causality and recirculation extent are not independently measured.

Across cases,the source quotes maximum relative temperature deviations35.5%heaterinlet,16.7%heateroutlet,11.9%cooler(PDF26–27). Temperature-relative percentages depend on origin/unit choice if absolute°Cdenominators are used;without a declared engineering scale these are not universal accuracy bounds. Figure19/PDF26 explicitly labels some experimental error bars as |CFD−EXP|. These bars represent model–data differences,not independent thermometer uncertainty; they must not be copied into a metrology budget. Table6/PDF29quantifies ΔT directly:at800Wheater30.66°Cexperimentvs10.412CFD;cooler17.75vs8.108°C. These are consequential transport discrepancies,even when selected absolute temperatures agree.

Figure21/PDF28separately labels “Experiment” and “Energy Balance”,but the same article says primary flow is obtained indirectly and no primary meter exists. The additional curve’s distinct provenance/independence is not fully explained. Their agreement cannot validate flow twice. Identified explanations—flanges/minor losses omitted,guard/rod power assigned differently,losses—are plausible confounded contributors,not independently isolated effects. A deterministic CFDmodel can exhibit physical oscillations;determinism alone is not a sufficient explanation for missing experimental oscillations.

**Similarity is not achieved merely by choosing the oil.** Fig22/PDF30has testedPr largelytens–hundreds;§7/PDF31explicitly says comparable molten-saltPr would require more than1500W. No actual prototype-to-testRe/Fr/source/wall/radiation similarity table for these runs is established. A proposed oil can be a candidate fluid while current operating cases remain distorted. MSR engineering relevance is therefore conditional mechanism/model learning,not demonstrated reactor-equivalent performance.

## TRIDENT use,next sources and coverage

This source invalidates broad novelty claims for oil-loopCFDcomparison,loss-inclusive modeling,indirect cooler-flow inference or presenting localCFDfields. A feasible increment must specify identifiable thermal/duty/response QoIs,shared-observation uncertainties,model inadequacy and held-out predictive consequences. Without independent flow evidence,focus on assessable thermal outputs and disclose flow conditionality. Do not adopt itsCFD,sensors or higher-power upgrades as TRIDENT resources.

S74 is the direct similarity lineage already read. S20(Podila etal.,2023,DOI10.1016/j.pnucene.2023.104880,Ref22)remains useful only if retaining local-field extension. Existing PartI/thesis and facility-design sources must be matched to registry before new IDs. No reference original is treated as read through S29. External raw time series are unnecessary for this literature pass.

| Coverage | PDF | Status/reason |
|---|---|---|
| Intro/background/lineage | 1–5 | Read;historical/design claims kept as cited background |
| Facility/calibration/protocol | 5–10 | Read/extracted;Fig4selected dimensions mapped |
| Analytical balances | 10–12 | Read/extracted;units/control-volume limits |
| CFD/numerics/properties/losses | 12–20 | Read/extracted;no case-file reproduction |
| Thermal/flow/local results | 21–30 | Read/extracted;selected critical figures visually checked;no full digitization |
| Future/conclusion/nomenclature | 30–33 | Read/inspected;upgrade proposals not resources |
| References | 33–36 | Discovery-inspected;originals not thereby read |
| Raw data,CFD/calibration/supplement | External | Unavailable/unread;not needed for scoped synthesis |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S29-C01 | Therminol-loop experiments plus3Dloss-inclusive CFD are close existing prior art | §2–5,PDF5–30 | Specific facility/operating cases |
| S29-C02 | Primary circulation is inferred from cooler enthalpy balance,not directly metered | Eq3/PDF9;§6/PDF30 | Shared temperature/flow/property ingredients |
| S29-C03 | Case power and cooling conditions change together | Table5/PDF17 | Cross-case trends not isolated power causality |
| S29-C04 | Mesh/time choices partly optimize experimental agreement | §4.1/PDF14–16 | No locked independent validation split |
| S29-C05 | Half-mesh-spread is used as a discretization sensitivity estimate | Eq18/PDF16 | Not demonstrated asymptotic/GCI uncertainty |
| S29-C06 | Loss-inclusive results improve selected temperature metrics but retain strong flow/dynamic mismatch | PDF21–23,Fig13–15 | Flow reference indirect |
| S29-C07 | Local temperature/velocity maps are CFDoutputs | Fig16–18/PDF24–26 | Not measured recirculation extent/causal HTC effect |
| S29-C08 | Tested Pr range is not established as molten-salt-matched | Fig22/PDF30;§7/PDF31 | Candidate oil selection differs from achieved similarity |
| S29-C09 | Quoted±5.22%flow uncertainty lacks a fully reproducible run-specific covariance budget | Fig21/PDF28;Table2/PDF9 | Not adopted as total uncertainty bound |
| S29-C10 | Separate experimental/energy-balance flow curves lack demonstrated independent provenance | Eq3/PDF9;Fig21/PDF28;§6/PDF30 | Curve agreement not two independent validations |
| S29-C11 | Current-pressure calibration prose/equations need ampere-versus-mA clarification | Eq1–2/PDF8 | Our endpoint/unit check,not a corrected calibration |
| S29-C12 | Loss descriptions and omitted geometry/power split confound mechanism attribution | §4.5/PDF20;§5/PDF21,25–28 | Plausible explanations,not isolated identified effects |
| S29-C13 | Some temperature-plot bars are explicitly model–experiment differences | Fig19/PDF26 | Not independent experimental uncertainty bars |
