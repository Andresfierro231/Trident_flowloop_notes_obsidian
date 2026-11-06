# S31 — JCGM102:2011: scoped vector covariance evidence

Official *Evaluation of measurement data—Supplement2 to the GUM—Extension to any number of output quantities*,October2011. DOI https://doi.org/10.59161/JCGM102-2011 .80-page official PDF;title/date,contents andterminalindex printed72present. Main numbering=PDF−8. Extracted21October2026;selected-clause dossier,not full80-page or normative implementation review.

Read:§6.2.1/PDF23/15;§6.3.1/PDF25/17;§6.5.1–2/PDF27–28/19–20;Tables1–2/start§7/PDF31/23 and§7.1/PDF32/24. Cover/contents/endindex inspected;examples on those pages are context only,not all entries reproduced. Other clauses,remaining coverage-region details,workedexamples andannexes are unread.

Eq3 gives Uy=Cx Ux Cxᵀ for first-order propagation of an explicit vector modelY=f(X). Entries retain physical productunits,including covariances between differentoutputs. Acommon uncertainthermometer/power/property variable can coupleduty,flowandmargin even if separately reported. Eq8 gives Cy Uy Cyᵀ=Cx Ux Cxᵀ forimplicit measurementmodels;singularCy prevents this localcovariance solution,andthe source discourages direct inversionforstability. **Our derivative convention:**forh(Y,X)=0,dY/dX=−Cy⁻¹Cx wheninvertible;theglobalminus signcancelsin thecovarianceproduct. Do notmistake local linearpropagation for globalidentifiability orvalidity of an ill-conditioned ratio.

§6.5treats a vectoroutput as oneentity with a **joint coverage region**,not merely independent intervals. Gaussianellipse factors depend on dimension andcovariance;the bivariate95%radialfactor2.45is not univariate1.96. These conditionalGaussian constructions do notprove empirical jointcoverage for a physical forecast. §7.1usesjoint samples andvectoroutputs;the same sample must carry through sharedinputs. No uncertaintybudget ortrialcount assigned toTRIDENT.

| Coverage | Status |
|---|---|
| Identity/contents/numbering/endindex | Inspected |
| Selected explicit/implicit covariance andcoverage/MCclauses | Read/extracted |
| Remaining clauses,examples/annexes | Unread;no blanket compliance claim |
| Numerical reproduction | Not performed |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S31-C01 | Vector first-order uncertainty retains covariance via sensitivity matrix | §6.2.1/Eq3,PDF23/15 | Local linear approximation |
| S31-C02 | Implicit-model covariance requires a nonsingular output Jacobian | §6.3.1/Eq8–10,PDF25/17 | Directinverse discouraged;not an identifiabilityproof |
| S31-C03 | Joint coverage regions differ from separate marginal intervals | §6.5.1–2,PDF27–28/19–20 | Distribution/dimensional assumptions matter |
| S31-C04 | Vector Monte Carlo samples jointinputs and retains outputdependence | §7.1,PDF31–32/23–24 | Does not validate inputlaws or physicalmodel |
