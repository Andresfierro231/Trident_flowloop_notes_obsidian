# S74 — modern high-Pr surrogate similarity: strong prior art, conditional evidence

21October2026. **Scoped ready** for similarity/motivation and prior-art synthesis; numerical transcription requires the flags below. H.H.Abdellatif,D.Arcilesi,R.Christensen,A.S.Iskhakov, *Similarity analysis of high-Prandtl surrogate fluids for thermal-hydraulic studies of molten salt reactors*, Annals of Nuclear Energy225(2026),111757; online6August2025. DOI https://doi.org/10.1016/j.anucene.2025.111757. User-supplied typeset19PDFpages, printed=PDF; identity matches publisher/institutional metadata. Body through§5/PDF17 and references throughPDF19 complete. Main text read; critical group/scale/Table4.7–4.10 pages visually checked. No separate code/property data or original manufacturer tables inspected.

## Original contribution and prior work

The paper applies an H2TS-inspired global/local similarity framework to Therminol66,DOWTHERMA andDOWTHERMRP and three cited reference designs: KP-FHR,FuSTAR andFUJI-233Um. It extends earlier fluid/scale comparisons, explicitly citing S64,CIET and Seo2018. It is an **analytical/design/correlation study**, not a new physical experiment validating every scaled reactor, local field or transient. Its strong abstract/conclusion language must be read in that light. Related experimental paper cited as a2025 preprint corresponds to the available S29 PartII lineage; do not count these as independent experimental campaigns without tracing data.

## Reference conditions and property treatment

§2/PDF3–5,Tables2.1–2.3 gives source-era reference designs. KP-FHR andFuSTAR use solid fuel with fluoride coolant; FUJI uses a fuel-salt mixture and pumped primary transport. Their neutron, fuel, pool/channel and exchanger distinctions are not reproduced by a generic pipe loop. Current vendor/status claims were not independently verified; design values are those selected for this paper.

§3/PDF5–7,Tables3.1–3.4 collects salt properties and fits manufacturer oil data. **Salt-property T is Kelvin, oil-fit T is Celsius; oil viscosities are mPa·s and cp kJ/(kgK)** in Table3.4. These are regression/input conventions, not universal units. The scaling calculations actually use tabulated manufacturer data with interpolation rather than those fitted oil correlations (§3.2/PDF7). Therefore substituting the regression without assessing its distortion does not exactly reproduce the reported tables. R² is goodness of fit, not a property uncertainty/covariance budget.

Table4.1/PDF10 reference salt Pr values:FLiBe600°C18.55,FLiBe675°C13.20,FLiNaK600°C10.53,fuel-salt637°C10. Surrogate temperatures are selected to match each Pr at that mean state; this does not demonstrate a match over every transient temperature excursion. No metrological covariance, probabilistic property propagation or new physical uncertainty measurements are supplied.

## Governing assumptions and mathematical scope

§4.1/PDF8–9 assumes steady incompressible Boussinesq1D flow, constant properties, no pipe-to-ambient loss and negligible hot/cold-leg wall inertia. Core/IHX nonuniformity is reduced to effectiveness factors. Momentum includes pump head, buoyancy and distributed/minor loss; energy equates reactor heat to IHX rejection (Eq4.1–4.5). These assumptions omit exactly some heat-loss/storage/source/observation questions central to TRIDENT.

Top-down groups include Eu,Ri,flow resistance,modified core/IHX Stanton numbers. Bottom-up discussion links friction/Re and Nu(Re,Pr). §4.2/PDF9–11 then imposes Re/Fr to set U/L, βΔT to match buoyancy, and a time ratio L/U; solid and free-surface conditions are considered separately. S64 contains the earlier liquid/solid scale relations. For arbitrary components, Re matching alone does not establish equal minor losses, roughness, area ratios, heat-source distribution or exchanger effectiveness.

DF=(Πprototype−Πmodel)/Πprototype is a normalized **group distortion**, not a percentage error in an engineering output or a predictive confidence bound (§4.2/PDF11). Tables4.2–4.5 report many zero DFs by construction. 'Acceptable' Biot DF<.10 is not a declared TRIDENT acceptance tolerance or a proof of small temperature error.

## Numerical and convention checks

- Table4.2/PDF12:KP-FHR/Th66 length.3825,velocity.618465,ΔT.29273,thermal-power.0108 andtime.61846 ratios. Our checks L/U≈.6185 and(.3825)²/.61846≈.23656 support the listed time/diffusivity scaling. The conclusion says less than1% power, but .0108 is1.08%; retain the table rather than the rounded rhetoric.
- **Power-normalization flag:** the displayed heat/pump-source matching onPDF11 sets dimensional power-scaling products equal to1, whereas tables give nonunit power ratios. Our dimensionally consistent interpretation would normalize by the actual source-power ratio; that factor is not displayed. Do not implement the displayed equality literally or silently repair it.
- **Solid-time flag:** PDF11 lists both Fourier matching with a scaled transient time and equality of dimensional solid diffusion times. Generally those conditions cannot both hold when the flow transit-time scale differs from1. Also its Biot conductivity/thickness rearrangement must be checked against the defined fluid/solid symbols and S64. Use a freshly derived dimensionless interface/storage model rather than copying these identities unchecked.
- **Geometry flag:**Tables2.1–2.3 report overall core diameters2.4,3,6m, which Tables4.7–4.9/PDF16 label core hydraulic diameter. No sufficiently detailed pore/channel wetted geometry is supplied to establish those as hydraulic diameters for packed/rod/graphite-channel cores. A true fluid hydraulic diameter and relative roughness/heat-transfer geometry are necessary before applying pipe correlations quantitatively.

These are implementation/transfer ambiguities, not evidence that every illustrative scaling ratio is wrong. We did not reconstruct all table entries or the authors' code.

## Correlation results and their limits

§4.4/PDF13–16 compares friction/Nu correlations and reports their validity ranges. Its printed forms must be distinguished from each original; the originals were not newly audited here. Figure4.6 shows differences between chosen heat-transfer correlations that can be much larger than the surrogate matching discrepancies. Internally heated-fluid correction Eq4.8–4.9 is **cited** prior work, not a new correlation established by S74; it depends on signed volumetric/wall heating and has finite Re/Pr ranges. No direct local recirculation inference is supplied.

Table4.10/PDF17 compares Dittus–Boelter Nu values for prototype and scaled conditions, with the stated maximum relative difference below.11%. **This is not independent validation:** applying the same deterministic Nu(Re,Pr) function to deliberately matched Re/Pr mathematically yields matching Nu, up to rounding. It does not measure local salt/oil HTC, validate a transient, quantify correlation bias or independently confirm a reactor-scale field. Near equality of a group/correlation is useful consistency evidence with a much narrower interpretation than physical equivalence.

No calibration/held-out experimental split, probabilistic output coverage, independently observed fields or newly executed reactor/surrogate experiments appears in this study. Its references to property uncertainties up to±20% are background statements; they are not a propagated uncertainty result for each table.

## TRIDENT implications and coverage

S74 is strong prior art against claiming novelty for comparing high-Pr oils, matching multiple groups, H2TS application or reference-reactor scaling. A useful increment could quantify **QoI error under unavoidable source,loss,storage,observation and regime distortions**, with independent assessment. That is a hypothesis, not a verified gap. A pipe loop can offer mechanism evidence even when it cannot represent a solid-fuel core/pool or internal nuclear heating. No oil recommendation or new operating envelope is selected here.

| Coverage | PDF | Status |
|---|---|---|
| Intro/design backgrounds | 1–5 | Read; cited designs/background not independently verified |
| Property sources/fits | 5–7 | Read; key unit conventions extracted; raw tables not acquired |
| H2TS balances/groups | 8–11 | Read; key pages checked; source/solid normalization flags retained |
| Scale/distortion tables | 10–14 | Read/mapped; selected scale arithmetic checked,not all entries reproduced |
| Correlation comparisons/design outputs | 13–17 | Read/extracted; not independent validation; original correlations not thereby read |
| Conclusion/references | 17–19 | Read/discovery inspection; no historical/status endorsement |
| External data/code/supplement | External | Not supplied/read; exact numerical reproduction incomplete |

## Stable claims

| ID | Claim | Locator | Limit |
|---|---|---|---|
| S74-C01 | Modern multi-fluid/reference-design H2TS similarity is established prior art | §1–4,PDF3,8–17 | Analytical design study |
| S74-C02 | Scaling assumes no external loss/negligible leg-wall inertia,constant-property1D flow | §4.1,PDF8 | Not the full TRIDENT model |
| S74-C03 | Oil fits and calculations use distinct data representations and unit conventions | §3.2,Table3.4,PDF7 | Interpolation used in actual scaling |
| S74-C04 | Zero group distortion is a construction result,not output-error coverage | §4.2–4.3,PDF11–13 | Uncertain inputs/omitted physics remain |
| S74-C05 | Nu matching uses the same Dittus–Boelter correlation at matched Re/Pr | §4.5/Table4.10,PDF16–17 | Consistency,not independent physical validation |
| S74-C06 | Source-power and solid-time identities need normalization clarification | §4.2,PDF11 | Our mathematical checks; no silent correction |
| S74-C07 | Core diameters become hydraulic diameters without sufficient wetted-geometry justification | Tables2.1–2.3,4.7–4.9,PDF3–5,16 | Quantitative pipe-correlation transfer conditional |
| S74-C08 | Table4.2 provides nonunit scale ratios and mean-state matching | PDF10–12,Tables4.1–4.2 | Not an envelope-wide uncertainty analysis |
