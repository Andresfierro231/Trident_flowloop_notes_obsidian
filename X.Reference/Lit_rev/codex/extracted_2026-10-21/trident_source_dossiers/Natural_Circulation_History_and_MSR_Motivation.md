> **Historical evidence update:** Original report S47 (Gabbard,ORNL-TM-3002,May1970) is now retrieved and scoped-extracted. It separates power-metrology disagreement, primary-HX property revision and air-radiator performance. See [S47 dossier](dossiers/S47_Gabbard_1970_MSRE.md) and the P0 memo before using the alleged25% heat-balance claim. S43/S46 evidence is also now incorporated there.

# Natural circulation loop history and MSR motivation

Evidence checkpoint, 20 October 2026. This is a scoped motivation synthesis from the supplied dossiers and selected historical primary passages, not a completed history of thermosyphons or a claim to have located the first natural-circulation loop.

## What the history actually supports

Natural circulation is a transport mechanism used for several engineering purposes. A laboratory loop may study that mechanism, validate a closure/code, expose materials to circulating salt, or test part of a passive cooling concept. Those purposes require different forms of representativeness. A loop's motivation does not require it to be a complete reactor analogue.

| Historical evidence | Original purpose and engineering question | What it does not establish |
|---|---|---|
| **S40, Romie and Kinyon, 5 February1958**, *A Molten Salt Natural Convection Reactor System*, ORNL-CF-58-2-46, DOI10.2172/4349103 | A reactor design calculation considers replacing fuel-circulation pumps with natural convection. Its explicit tradeoff is pump reliability/maintenance versus increased fuel-salt inventory in risers and exchanger. | Not an operated60MW reactor or experimental validation of a nitrate/water loop. Not evidence that all MSRs were intended to use pump-free primary flow. |
| **S42, Robertson, January1965**, *MSRE Design and Operations Report Part I Description of Reactor Design*, ORNL-TM-728, DOI10.2172/4654707 | The MSRE design uses a fuel pump, secondary coolant pump and air radiator. The introduction identifies practical long-duration operation, materials and salt behavior as central objectives. | Normal pumped design is not proof natural circulation never occurred or was never tested. A1969 natural-circulation test remains an operational-report lead, not verified here. |
| **S41, Savage, Compere, Baker and Bohlmann, December1967**, *Operation of Molten-Salt Convection Loops in the ORR*, ORNL-TM-1960 | Fueled fluoride-salt convection loops irradiate salt in contact with graphite and Hastelloy N. Natural circulation enables an in-pile exposure experiment; heating/cooling, handling and structural performance also matter. | Not primarily a scaled passive decay-heat-removal demonstrator. In-pile materials/fuel evidence cannot be claimed by an unirradiated surrogate loop. |
| **S36,1994; S09,2002** | Water-loop scaling, friction, startup, steady circulation, hysteresis and stability test how simplified loops and models transfer. | Matching a steady flow law alone does not match transient or stability behavior. These are not automatically MSR-specific experiments. |
| **S37/S38/S16/S21 and S35/S39,2024–2026** | Optical diagnostics, high-Pr development, local heating, heat-loss reconstruction, measurement interpretation and code comparison in the TAMU facility. | Multiple papers may reuse experiments. They do not create independent reactor-scale evidence or automatically establish quantitative local recirculation/heat-transfer causality. |

The1958 report is particularly useful proposal motivation because it connects a physical mechanism to a concrete design tradeoff. The1967 report gives a different, equally valid motivation: maintaining a circulating fuel-salt environment for irradiation and compatibility testing. Modern loop diagnostics and validation studies add a third purpose: finding when economical models and sparse measurements support defensible predictions.

## How a loop can represent an MSR

Representativeness should be stated as **a particular phenomenon and QoI under specified conditions**. The target must distinguish a liquid-fuel MSR primary loop, an unfueled salt coolant loop, a passive decay-heat loop, and a drain-tank heat-removal path. They need not share source distribution, geometry, thermal inertia, operating state or safety decision.

| Provisional engineering decision | QoIs that would inform it | Plausible loop evidence | Transfer conditions or missing physics |
|---|---|---|---|
| Can a selected passive path reject the specified heat load? | Signed circulation, heat rejection, maximum fluid/wall temperature, time to temperature limit | Heat/cooling response; loop momentum and energy behavior | Match heat source/sink placement and time history, hydraulic/elevation ratios, fluid/property regime, losses and wall storage. Measured maximum needs adequate spatial coverage. |
| How much preheating/trace heating is needed? | Minimum salt/wall temperature, margin above liquidus, cooldown rate, time to cold limit | S38 accidental cooldown motivates cold-side limits; prospective thermal models can test sensible-heat behavior | A heater trip is not equivalent to disappearance of reactor decay heat. Actual freezing prediction needs phase change, composition and solidification/flow coupling. |
| What elevation, pipe diameter or exchanger resistance is worthwhile? | Flow versus duty, pressure-loss allocation, temperature rise, fuel/coolant inventory | S40 design tradeoff; S09/S36 scaling | Reactor constraints and component topology; steady similarity is insufficient for stability. |
| Which model and sensors are sufficient for a decision? | Predictive error/intervals for specified probes, duty, flow and extrema; identifiable parameter groups | S16/S35/S39 observation and loss-model comparisons; S26 inference workflow | Point versus bulk operators, shared derived data, independent calibration/validation, input uncertainty and discrepancy must be explicit. |
| Do local developing or reverse-flow regions change heat-transfer risk? | Signed reverse-flow extent/exchange, near-wall gradients, local temperature peaks, change in duty or h | S35 CFD predicts local reversal; S21/S37/S39 provide related but limited local diagnostics | Requires qualified local fields and quantitative independent evidence. Sparse TRIDENT temperatures alone do not identify3D recirculation extent or its causal effect. |

This map is a proposal framing, not evidence that a TRIDENT facility already measures every QoI. No CFD, new instruments, primary flowmeter calibration or approved experimental campaign is assumed. PF01's actual available observations remain the feasibility constraint.

Similarity requires more than choosing a fluid with a similar Prandtl number. Source distribution (wall versus volumetric), signed buoyancy integral, resistance and elevation distribution, heater/cooler arrangement, external losses, wall storage, entrance and bend effects, measurement placement and operating regime can change the result. The dimensionless groups must use consistent definitions and reference scales. Thermally developed is not synonymous with radially uniform. Fuel chemistry, radiation, neutronics, gas/fission products and phase change are separate transfer limits unless represented explicitly.

## Auditable historical source notes

### S40 identity and selected dossier

F.E.Romie and B.W.Kinyon. Date, authors, report number and title visually confirmed on PDF1 of the retrieved28-page scan. Abstract PDF3/printedii; introduction PDF4/printed1; main text PDF4–15 corresponds printed1–12; later plots were not fully audited. Retrieval: https://moltensalt.org/references/static/downloads/pdf/ORNL-CF-58-2-46.pdf . Official record: https://www.osti.gov/biblio/4349103 . Direct official PDF retrieval returned429; the mirror is an identified scan of the original ORNL report.

Read PDF1,3–10; visually checked title/abstract and relied on the introduction for the qualitative tradeoff. The abstract reports a60MW thermal design study, not a constructed plant. Numerical exchanger/riser tables and their old property/heat-transfer assumptions are not implementation-ready; no modern UQ or experimental-validation finding is claimed. Not read/extracted: full later exchanger calculations and plots, detailed nuclear/fuel economics and underlying cited originals. Ready only for the narrow historical design-motivation claim.

### S41 identity and selected dossier

H.C.Savage,E.L.Compere,J.M.Baker,E.G.Bohlmann. ORNL-TM-1960, **December1967**,43-page scan; do not use the separate1966 catalog lead as this report's publication date. Title PDF3; contents PDF5; body PDF9/printed1 through PDF41/printed33, so body printed=PDF−8. Retrieval: https://media.githubusercontent.com/media/openmsr/msr-archive/master/docs/ORNL-TM-1960.pdf ; alternate https://moltensalt.org/references/static/downloads/pdf/ORNL-TM-1960.pdf . Scan OCR is imperfect; no isotope exponents or numerical burnup values were adopted from OCR.

Read title/index, abstract/introduction PDF9/printed1 and discussion/conclusions PDF37–41/printed29–33. It reports two operated fueled fluoride-salt convection loops, an irradiation/contact-material purpose, and termination following primary-system breaks. The conclusions distinguish observed damage from proposed thermal-stress causes and explicitly call part of that causal interpretation speculative (printed32/PDF40). This is valuable evidence that thermal transients and materials limits matter alongside circulation. Detailedgeometry, operating tables, stress-code equations, full failure chronology and referenced material tests remain unextracted. Ready for the narrow historical-purpose/limitation synthesis, not quantitative thermal-stress or irradiation-life prediction.

### S42 identity and selected dossier

R.C.Robertson. ORNL-TM-728, January1965; supplied-by-web575-page scan covering a large design report. Title PDF1 confirms report identity. Retrieval: https://moltensalt.org/references/static/downloads/pdf/ORNL-TM-0728.pdf . Official identifier: https://doi.org/10.2172/4654707 . The normal fuel/coolant circulation structure is also described by INL's official Virtual Test Bed documentation: https://virtualtestbed.inl.gov/msr/msre/msre_description.html .

Read selected front/index pages, introduction printed3–6/PDF35–38, general description printed7–12/PDF39–44 and its pump subsection§2.4.2 at printed12/PDF44. The scan's selected Arabic pages use printed=PDF−32; do not extrapolate this offset blindly across all volumes/inserts. Original§2.4 describes fuel and coolant pumps, and§2.4.2 specifies a centrifugal fuel pump. These are design statements. Detailed core/HX thermal design, pump curves, safety/operating procedures, later volumes and any subsequent operating reports remain unread. Ready to correct a blanket normal-primary-natural-circulation narrative, not to summarize actual1969 natural-circulation tests or all MSRE safety performance.

## Historical claim ledger and next questions

| Claim ID | Supported claim | Original locator | Scope |
|---|---|---|---|
| S40-C01 | Pump reliability/maintenance versus increased salt inventory explicitly motivated a natural-convection reactor concept. | PDF4/printed1, Introduction |1958 calculated concept |
| S40-C02 | Report considers a60MW thermal system. | PDF3/printedii, Abstract; PDF4/printed1 |Design rating, not demonstrated power |
| S41-C01 | ORR salt convection loops were intended for irradiation of representative fuel with graphite/Hastelloy N. | PDF9/printed1, Abstract/§1 |Different purpose from passive decay-heat testing |
| S41-C02 | Operated loops experienced primary-system failures; thermal-stress causes remain qualified. | PDF9/printed1; PDF37–40/printed29–32,§7 |Observed failures versus proposed mechanism |
| S42-C01 | MSRE normal circulation design included fuel and coolant pumps. | PDF41/printed9,§2.4; PDF44/printed12,§2.4.2 |Does not rule out later natural-circulation tests |
| S42-C02 | MSRE aimed to demonstrate practical operation and long-duration salt/material performance. | PDF35–38/printed3–6,§1 |Original design purpose |

Historical acquisition leads: primary reports for early heated-loop stability experiments (including the1950s ANL/ORNL leads cited in S36), and the original operating record of the reported January1969 MSRE natural-circulation test. The exact date/duration/power must be verified in that original record before appearing in the proposal. The search is not exhaustive before1958, across nonnuclear thermosyphons, or across all MSR concepts. These limits prevent a “first ever” or universal historical conclusion.
