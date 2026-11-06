# S32 — JCGMGUM-6:2020: scoped measurement-model evidence

Official *Guide to the expression of uncertainty in measurement—Part6:Developing and using measurement models*,firstedition2020. DOI https://doi.org/10.59161/JCGMGUM-6-2020 .103-page official PDF;cover/title/edition,contents andterminalindexpresent. Main numbering=PDF−8. Extracted21October2026. This is scoped guidance extraction,not full-document reading or a laboratory accreditation audit.

Read:§5/PDF11–13/printed3–5;§6/PDF13–15/5–7;§10.5/PDF43–44/35–36;§12.1–2/PDF65/57;§13.2/PDF69/61. Cover/contents/endindexinspected. Otherclauses/statisticalexamples/annexes unread. No relevant conclusion is attributed to those unread passages.

The measurand must be specified according to use,including spatial/temporal/referenceconditions as appropriate (§6). “Temperature” alone does not distinguish a contactwallreading,bulkfluid average or unobservedmaximum. §5.3sets modeldevelopment steps:specifymeasurand/modelprinciple,identifyeffects,extend model andassessadequacy. Omittedknown effects can narrow uncertainty unrealistically (§5.6). Numericalalgorithm formdoesnotmake a measurementmodel independent of assumptions.

§10.5explains sharedsystematic effects. They canbe modeled as commonlatent inputs or carried as covariances;they cannot generally be eliminated wheninformationisinsufficient. Thecalibratedresistor exampledemonstrates erroneousuncertaintyreduction ifcommonreferenceerror istreatedindependently. **Ourapplication:**reusing a calibrationoffset across temperatures/duties should reuse the same uncertainoffset perjointsample,notresampleindependentlyfor each occurrence.

§12assesses adequacy across the intendedrange andencouragesreference/experimentalcomparison;agreement supplies support,not omniscience. §13.2warns against empirical/hybrid extrapolation outside assessedrange andallowscarefultheoreticalextrapolation onlywith a justifiedphenomenologicalmodel. This complements S75's embedded-modelapplicability argument. It doesnot prove a salt-surrogate transferor justify all ROMextrapolation.

| Coverage | Status |
|---|---|
| Identity/contents/numbering/endindex | Inspected |
| Listedmodel/measurand/shared-effect/adequacyclauses | Read/extracted |
| Otherclauses,examples andannexes | Unread;not neededfor currentlimitedclaims |
| Facility model/metrology execution | Not performed |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S32-C01 | Measurand specification depends on use and can require spatial/temporal/reference conditions | §6,PDF13–15/5–7 | Does not supply TRIDENTsensor maps |
| S32-C02 | Known measurement effects belong in the model/uncertaintyassessment | §5.3–5.6,PDF11–12/3–4 | Missing information cannotbe repairednumerically |
| S32-C03 | Shared effects introduce correlation or require commoninputs | §10.5,PDF43–44/35–36 | No invented covariance magnitudes |
| S32-C04 | Adequacy and extrapolation are scoped to model/use/range | §12.1–2/PDF65/57;§13.2/PDF69/61 | Not universalreactor/ROMvalidation |
