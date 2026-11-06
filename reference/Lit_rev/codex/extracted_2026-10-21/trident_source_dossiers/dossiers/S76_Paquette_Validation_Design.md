# S76 — Prediction-oriented validation-experiment design

Antonin Paquette-Rufiange,Serge Prudhomme,Marc Laforest. Journal:CMAME414(2023),116182,DOI https://doi.org/10.1016/j.cma.2023.116182 . **Inspected:**arXiv2303.06114v1,10March2023,first-page compilation13March2023,31pages. PDF=manuscript printed numbering;finaljournal correspondence not established. Extracted21October2026.

## Integrity and relevance

Title/authors/relatedjournalDOI match primary arXiv record. MainSections1–5,Algorithms1–3,Figures1–10,Tables1–3,AppendicesA–C andTablesC.4–5present. Maintext1–25 andappendices28–31read;references25–28 discovery-inspected,not each cited original read. PDF14/15/29rendered;Eq17/PDF15visually checked. No code,supplement or physical data acquired. Ready for scoped validation-design/theory/novelty synthesis;not a certified design or error-bound implementation.

## Problem and method

The paper asks how to choose a realizable validation scenario and observable that challenge a model for a specified target,especially when the target scenario/quantity cannot be directly measured. This differs from calibrating parameters (S72),maximizing parameter/target information (S07/S71),or propagating embedded discrepancy (S75).

Eq1/PDF4defines residualr(p,u)=0;controlsx,modelparametersθ,sensorsz;predictionh_qoi(x,θ)and observationh_obs(x,θ,z). The model must be wellposed and functionals sufficiently regular. It assumes identical modelparameterdistribution across scenarios and **certain controls/sensorparameters** (§2.3–2.5,PDF5–8). The paper's specialized “aleatory” terminology means assigned probability laws;do not adopt it as a universal epistemic/aleatory taxonomy.

Eq14/PDF13: M_h(x,z)=EΘ[∇_(x,θ)h∇_(x,θ)hᵀ]. This gradient second moment is not Fisherinformation,posteriorcovariance or a model-errorbound. Eq15/PDF14uses spectralnormdistance. Eq16selects realizable x_val minimizingdistance between target influence matrices atvalidation andprediction. Eq17/PDF15selects available h_obs,zbydistance between **trace-normalized** matrices forobservation andtarget atx_val. Algorithm3performs these stages sequentially. Trace normalization accommodates overall outputscale/units;zero trace needs handling.

**Our coordinate check:**if p=Dξ,then ∇ξh=Dᵀ∇ph andMξ=DᵀMpD. Spectral distances and trace-normalized shape generally depend on parameter units/scaling. Output normalization alone does not remove that dependence. Use explicit nondimensional/reference scales before implementation;the paper's conclusion notes parameter-space dimensional transformations as future work (PDF25).

**Our counterexample:**two outputs differing by a parameter-independent additivebias have identical parameter gradients andinfluence matrices but unequal values. Hence matrixagreement alone cannotboundpredictionerror. Authors explicitly disclaim guaranteed correct validation decisions (§4.1/PDF20),consistent with this observation. This is our logicalcheck,not a new empiricalfinding or a proof that the approach fails universally.

## Demonstrations,units and independence

Projectile:1DlinearStokes-type drag model,Eq2/PDF4;mass,length,initialposition/velocity andgravityviscosity variables. A manufactured quadraticdragODEprovides “observations,”with5%multiplicativeGaussian noise (Eq20–22/PDF18). A validation case matching initialRe can falsely fail to challenge thebad drag approximation;the influence-matched caseexposesit(Fig5/PDF19–20). This is a syntheticcounterexampletoonescalarsimilaritycriterion,not proof dimensional analysisisuseless or an always-correctdesign.

Transport:steady2Dlinearadvection–diffusion,Eq23/PDF20;prescribedvelocity,controlledinletprofile,region-averageQoIs and0.1×0.1regionalobservations(Eq25/PDF23). Diffusivityparameter is certainDiracdistributed here;thereforeinfluencematrixrankone isexpected,not evidence of generalhighdimensionalperformance. ChangingQoIchanges preferred validationinlet/sensorpatterns. No physicalmodelvalidation or buoyancy/conjugatecoupling.

AppendixA/PDF28obtains thefixedvelocityfield fromStokesequations and no-slipbanks/docks,parabolicinlet,tractionoutlet. Itsroughlywater viscositylabel ν uses a dynamicviscositydescription;unit/densityconvention must be resolved before physicaluse. Theauthors explicitly say theflowmodel is a coarse illustrative approximation. AppendixB/PDF28–30derivesadjointgradients includingDirichletlifting. EqB.3–B.4negative-adjoint convention must remainconsistent;theweakformannotationB.1 has variable/labelnotationalissues. Verify derivatives independently before reproduction. AppendixC/PDF30–31uses NOMAD derivativefree multistart because outerobjective derivatives requiresecondderivatives. Multiplelocalminima and nonuniqueness are explicitly illustrated;10starts do not prove globaloptimality.

§2.7/Eq13/PDF11uses probabilityofdiscrepancywithin tolerance as an optionalvalidationmetric;distributional independence assumed between experimentalobservations andmodelparameters. This must not be silentlyusedwhenparameters werecalibratedusing the same observations. §2.7.2/PDF12explicitly **does not propagate modelerror to the target or decide modelvalidity**. Sensitivitymatch guides a test;it does not replace executing thetest or estimating targeterror.

## TRIDENT application and skeptical appraisal

A feasible adaptation could rank existing controllablehistories or sensorobservationtimes for a thermal/duty/response target. Control and sensoruncertainty are often central forTRIDENT and excluded here;accountingforthem is additionalmodelingwork,not automaticallya novelresult. No newinstruments or arbitraryexperimentalsetpoints follow from this source. It invalidates novelty basedsolelyon matchingtarget/observation sensitivities or choosingQoI-specificvalidationcases. Together S75/S76narrow the proposed advance to a specific conservative loopclass,evidenceconstraint,adequacy result and independent predictiveconsequence.

| Coverage | PDF | Status |
|---|---|---|
| Motivation/definitions | 1–8 | Read/extracted |
| Calibration/validation context | 9–12 | Read;independence/targeterrorlimits retained |
| Proposeddesign | 13–15 | Read/extracted;Eq17checked |
| Numericalexamples | 15–24 | Read/mapped;not reproduced |
| Conclusion | 24–25 | Read;limits retained |
| AppendicesA–C | 28–31 | Read/extracted selectively;no adjoint/code reproduction |
| References | 25–28 | Discovery inspection,not originalsource reading |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S76-C01 | Target-specific validation scenario/observable design is established priorart | Eq14–17/Algorithm3,PDF13–15 | Distinct from informationdesign/calibration |
| S76-C02 | Designmatches gradientsecondmoments,not modelerror | Eq14–17/PDF13–15;PDF20 | No guaranteed correctvalidationdecision |
| S76-C03 | Controls/sensors are certain and parameterlaw shared acrossscenarios | §2.3–2.5,PDF5–8;§5/PDF25 | ImportantTRIDENTuncertainties excluded |
| S76-C04 | Trace normalization handles outputscale but parametercoordinates still matter | Eq17/PDF15;§5/PDF25 | OurDᵀMDcoordinatecheck |
| S76-C05 | InitialRe-matched syntheticexample fails tochallenge wrongdragmodel | Fig5,PDF19–20 | Not a universalrejection ofsimilarityanalysis |
| S76-C06 | Transportexample usesfixedStokesvelocity and certaindiffusivity | §4.2/PDF20–24;AppendixA/PDF28 | Not naturalcirculation orexperimentalvalidation |
| S76-C07 | Appendicesprovideadjointgradients and demonstratenonunique/localdesignsolutions | AppendixB–C,PDF28–31 | Gradient/numericalverification stillneeded |
| S76-C08 | Targetmodelerrorpropagation and validitydecision are outside article scope | §2.7.2/PDF12;§5/PDF25 | Validationdesign doesnot certifyQoIaccuracy |
