# S02 — JCGM101:2008: scoped Monte Carlo propagation evidence

Official *Evaluation of measurement data—Supplement1 to the GUM—Propagation of distributions using a Monte Carlo method*,firstedition2008. DOI https://doi.org/10.59161/JCGM101-2008 .90-page official PDF,title/edition and terminal index printed82present. Main Arabic numbering=PDF−8. Extracted21October2026. This is **selected-clause reading**,not a full90-page review or implemented metrology procedure.

Read:contents,§5.1–5.3 onPDF16/printed8,§5.8–5.9 onPDF21–22/13–14,Fig4/PDF23/15,§6.5/start§7/PDF35/27 and§7.9.4/PDF40/32. Cover and endindex inspected. The preceding/following clauses,examples,full distribution assignment,conditions§5.10continuation and annexes remain unread except discovery snippets;none is represented as fully extracted.

The guidance separates **formulation**,distribution propagation and summarizing. Numerical precision of propagation cannot repair a deficient measurement model or invented input distribution. Figure4 explicitly samples the **joint** inputPDF,which preserves dependence. §5.8 discusses differentiability/higher-order conditions for Taylor-based propagation;Monte Carlo is an alternative for the specified model/distributions,not a proof of their validity. §5.9 provides sampled outputdistribution,expectation,standarduncertainty andcoverageinterval. Dependenceamonginputquantities does not mean independent draws of each instrument occurrence.

§7.9.4 supplies an adaptive repeated-batch stabilization procedure for estimate,standarduncertainty andintervalendpoints;the notes say stochastic stopping does not guarantee the desired numerical tolerance. Tails/interval endpoints may require more trials than means. Therefore a universal sample count is not justified. No TRIDENT simulations or measurements processed;no claimed calibrated coverage or rare-event resolution. Model discrepancy and independently assessed future prediction remain distinct from propagating metrologyinputs.

| Coverage | Status |
|---|---|
| Identity/numbering/endindex | Inspected |
| Listed clauses/figure above | Read and purpose-scoped extracted |
| Other clauses,worked examples,annexes | Unread;not needed for current limited claims |
| Numerical implementation | Not executed |

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S02-C01 | Formulation,propagation andsummarizing are separate uncertainty-evaluation activities | §5.1–5.3,PDF16/printed8 | Numerical propagation cannot fix bad model/input information |
| S02-C02 | Monte Carlo propagates samples of the specified joint inputdistribution | §5.9/Fig4,PDF22–23/14–15 | Not a complete model-formvalidation procedure |
| S02-C03 | Adaptive stabilization checks outputestimate,uncertainty andinterval endpoints | §7.9.4,PDF40/32 | Stochastic tolerance is not guaranteed;no universal trialcount |
