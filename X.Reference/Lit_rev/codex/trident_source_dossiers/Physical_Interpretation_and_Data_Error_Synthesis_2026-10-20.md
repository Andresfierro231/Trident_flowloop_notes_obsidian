> Current checkpoint21October2026: reviews v0.6; S13/S64/S65 scoped-read; S24/S29/S11 retrieved.74sources,37purpose-scoped dossiers,328claims. Current requests and next passes: Access_Gaps_and_Requests_2026-10-21.md and Next_Two_Prompts_2026-10-21.md. Earlier statuses below are historical.

# What S69 and S70 change for the TRIDENT literature reviews

2026-10-20. Both requested uploads are received. Main texts and S70 Appendix1 inspected; detailed coverage and qualifications are in their dossiers. Publisher identities independently checked on the web. This is a source-backed working synthesis, not a final direction or certified novelty finding.

## Main consequence

**Fit, identification and physical interpretation are separate achievements.** S69 supplies synthetic examples of useful temperature prediction with weak physical-property inference. S70 supplies a stronger warning: even an identifiable low-order network need not place resistance and storage in the true material layers. Their common implication is not to abandon physical models. It is to specify which physical or predictive claim the data actually support.

| Decision for our reviews | Evidence now available | Consequence for TRIDENT | What is still unestablished |
|---|---|---|---|
| What should calibration target? | S70-C03: a stable aggregate can coexist with non-identifiable internal coefficients | Evaluate target parameter combinations and engineering predictions directly | Which loop combinations are identifiable under actual inputs/observations |
| Can fitted storage mean material heat capacity? | S70-C05;S69-C04: effective allocation depends on reduction and excitation | Label effective storage separately from independently established material inventory | A valid mapping to loop fluid/pipe/insulation properties |
| Does good temperature agreement prove a heat-loss mechanism? | S69-C03/C05: observation/input choices alter coefficients without matching changes in RMSE | Compare source, bias and observation hypotheses before attributing error to closure physics | Whether actual TRIDENT discrepancies are caused by any one mechanism |
| Should every weak parameter be removed? | S70-C06: nuisance coefficients can help estimate total resistance | Assess reductions against target predictions and refitted nuisance terms | Which deletions preserve the loop's predictive task |
| What validation horizon matters? | S70-C04;S69-C06/C07: one-step agreement can hide free-simulation/longer-horizon errors | Declare assimilation versus forward prediction and assessment horizon | Independent prospective/withheld predictive coverage |
| Is a conductive RC precedent reactor motivation? | Both papers concern buildings/walls | Use them as methodological comparators | Reactor circuit, engineering decision and similarity must come from MSR/loop sources |

## A concrete methods-review argument

A conservative model hierarchy should be judged against a common prediction contract: prescribed boundary/source histories, initial state, outputs, observation map, adjustable coefficients and assessment data. Net heat entering that model is not interchangeable with an upstream power reading. S69 explicitly avoids heater-system dynamics by supplying radiator-delivered heat (§4,PDF3–4/265–266). For TRIDENT, electrical power, distributed pipe heating, stored heater energy and salt-side deposited duty require a separate measurement/source model; this is our application of their boundary lesson, not their reactor finding.

Identification should then be reported at three levels: individual coefficients, physically interpretable combinations and future outputs. S70's series resistance is an established example of the second level. Its evidence does not prove that a sum of loop regional losses, a circulation estimate or an unobserved maximum is similarly protected. Derive or test that claim for the actual model class and observation set. This helps turn a generic calibration exercise into a precise scientific question.

Accuracy must also match intended use. A filter repeatedly corrected by measured temperatures and a free-running model answer different questions. S70 rejects first-order models for long-term characterization despite acceptable one-step residual behavior. S69 reports increasing-order failures on longer horizons. Therefore our comparisons need the same forecast horizon, available measurements and permitted refits, plus a genuinely withheld assessment where feasible. Parameter confidence intervals, filter state bands, prediction RMSE and predictive coverage cannot substitute for each other.

These two articles are not complete inference implementation specifications. S70's Table1 capacitance entries conflict with its total; its diffusion-amplitude wording and implicit measurement equation need care. S69's printed Eq1 omits drift dt, and its expanded matrices/covariance/optimizer settings are not fully specified. The dossiers preserve these flags and distinguish our dimensional interpretations from printed mathematics. S73, newly retrieved from an author's repository, is the next foundational implementation source; only identity/abstract inspected so far.

## How this changes the proposal argument

The proposal can motivate research through the difficulty of **reliable inference from limited thermal evidence**, while anchoring its engineering purpose in a particular reactor heat-transport decision. Building examples establish that apparently physical network models may identify effective behavior rather than component properties. They do not establish that the STNCL is dynamically similar to an MSR or that a reactor safety margin has been measured.

The existing natural-circulation, high-Pr, internal-heating and MSR sources must supply that link. The next useful available reading is S64 (scaled salt/helium experiments), S65 (internal heat generation and dynamic stability), and deeper S13 (liquid-fuel MSR phenomena). They address three different transfer questions: fluid/geometric similarity; source-distribution similarity; and reactor engineering relevance. No new upload is needed for them. Existing scoped historical sources S40–S42/S47 and loop sources provide the historical foundation; this pass does not upgrade their prior reading depth.

## Candidate contributions after the prior-art challenge

| Hypothesis | Already established ingredients | A defensible additional result would require | Feasibility boundary/falsifier |
|---|---|---|---|
| H01: identifiable loop quantities under sparse thermometry | Profiles, aggregate parameters, excitation effects and thermal networks | Loop-specific invariance/identifiability or carefully scoped numerical evidence, including uncertain source and observation maps | Unknown duty/inventory may prevent separate identification; fail if no advantage over established grouping methods |
| H02: QoI-driven retained physics | Order selection and differences between fit and physical interpretation | A criterion predicting when retained fluid/wall/insulation/transport physics changes an independently assessed output beyond tolerance | Must use declared QoIs and regimes; fail if extra complexity only improves calibration |
| H03: supported local thermal consequences | Sparse thermal observations do not directly observe local flow | An evidence-limited bound or independently tested reconstruction with explicit observation consistency | Without local reference, avoid claiming recirculation extent or unobserved extrema are validated |
| H04: informative feasible evidence | Input proxies, bias studies, profile-guided excitation and Bayesian design already exist | Demonstrate what a feasible existing protocol resolves for a stated prediction, compared with established designs | Extra sensors/CFD are optional scenarios; no claim that maximizing parameter information guarantees predictive value |

These are questions to investigate, not established gaps. S71/S72 remain important challenges to any claim of new goal-oriented design/calibration. They should be extracted before committing to such a novelty statement.

## Proposed Codex implementation gates

This is a review-derived plan, not authorization to process held data or implement a model now.

1. Specify each candidate's inputs/states/outputs and observation/source operators. Preserve units, sensor averaging and area/volume definitions.
2. Check energy balance, equilibrium, positivity and relevant limits. These verify mathematics/code; they do not validate physical adequacy.
3. Separate source/bias/calibration uncertainties from model coefficients. Avoid interpreting process noise as a complete discrepancy model.
4. Evaluate profile likelihood for consequential coefficients or aggregates, with nuisance reoptimization and consistent objective normalization. Record bounds, multiple optima and incomplete scans.
5. Compare model structures using declared free-prediction horizons and withheld conditions, alongside physical-parameter questions. If there is no independent truth for a quantity, label the conclusion accordingly.

No empirical performance gain, particular model recommendation or thesis novelty is asserted by these gates.

## Reading and acquisition state

- **Resolved:** S69 and S70, publisher-looking full articles supplied, with purpose-scoped dossiers and16 new stable claims in the ledger.
- **Retrieved without user help:** S73 Kristensen, Madsen & Jørgensen (2004), *Parameter estimation in stochastic grey-box models*, Automatica40(2),225–237; DOI10.1016/j.automatica.2003.10.001. Author-hosted13-page typeset copy; identity/abstract only, full methods still unread.
- **Next available batch:** S64/S65/S13 for engineering motivation and transfer, then S71/S72:THESIS1 for predictive-design/calibration prior art; S73 for likelihood implementation.
- **Immediate upload requests:** none. S23 algorithm supplement and S72 final journal article remain optional later version/completeness checks, not blockers.
- **Additional cited lead:** Ramallo-González, Eames & Coley(2013), analytic lumping of multilayer constructions, DOI10.1016/j.enbuild.2013.01.014. Primary publisher author page and secondary discovery metadata found; original full paper not acquired or read. Lower priority than finishing the available motivation batch; not assigned a new canonical source ID until registry intake.

Search date2026-10-20. Targeted queries: exact S69/S70 DOIs; “Lumped parameter models for building thermal modelling” PDF; “Parameter estimation in stochastic grey-box models”2004 PDF. Primary evidence: uploaded articles, SAGE/Elsevier metadata and Henrik Madsen's author repository. Search is not exhaustive and does not establish novelty. No subscriptions, new instruments, TRIDENT CFD, experimental execution or bulk data processing assumed.
