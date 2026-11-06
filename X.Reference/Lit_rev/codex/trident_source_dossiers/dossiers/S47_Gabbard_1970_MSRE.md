# S47 — Gabbard (1970): the original MSRE heat-balance evidence

2026-10-20. **Ready for the scoped A5 historical correction and metrology motivation. Heat-exchanger equation implementation is not cleared.**

C. H. Gabbard, *Reactor Power Measurement and Heat Transfer Performance in the Molten Salt Reactor Experiment*, ORNL-TM-3002, May 1970. Persistent official record: [OSTI 4157686](https://www.osti.gov/biblio/4157686). The cover and author/title were visually verified in a 36-page scanned copy retrieved from the [historical mirror](https://moltensalt.org/references/static/downloads/pdf/ORNL-TM-3002.pdf). Official retrieval returned HTTP429/timeouts; the mirror supplies a primary ORNL report, not an independent secondary account. No page-by-page byte identity with the inaccessible OSTI PDF is claimed. Cover, legal notice, contents, printed1–29, blank pages and distribution list are present. Printed page = PDF page−4 for the numbered body. OCR is poor; consequential values in Table I and conclusions were checked visually. Cover describes the report as preliminary and subject to revision.

## Evidence and engineering significance

The report distinguishes three issues:

1. Revised coolant specific heat changed the routine heat-balance full-power estimate from about7.2 to8.0 MW. Isotopic estimates were lower; the abstract describes about7–10%, while the body also reports further calibration corrections. Do not merge those different calculations into a single universal discrepancy (PDF5–10/printed1–6).
2. The primary salt-to-salt exchanger's initial performance overestimate was resolved, according to the author, by revised physical-property data rather than a new salt-specific heat-transfer law (conclusions, PDF31/27).
3. The air radiator retained a design-versus-observation discrepancy. Air-side transfer and flow-distribution explanations were not definitively resolved (same page). These are separate from power metrology.

Thus the original report does **not** substantiate a “25% MSRE heat-balance discrepancy.” The defensible motivation is that uncertain properties, installed instrumentation and boundary-side performance can materially affect inferred power and design margins.

## Measurement model and limitations

The dominant calorimetric term is coolant mass flow × specific heat × radiator temperature drop. Table I (PDF9/5) reports radiator removal7.853 MW and total inferred nuclear power7.971 MW after other losses and inputs; heater and pump inputs have negative signs in this inference balance. This is not a statement that electrical power is a loss. Transferring this accounting to TRIDENT requires declaring the control volume and signs.

The author checked installed thermocouples under isothermal conditions and examined venturi pressure readout/calibration; two readout channels shared the same flow element and therefore were not fully independent flow measurements (PDF9–10/5–6). Salt activation-decay, pressure-drop recalculation and air calorimetry were attempted as cross-checks. The report concludes they were not accurate enough to settle the disagreement; a later differential-pressure-cell calibration was planned (PDF32/28). No later outcome is asserted here.

## Transfer, skeptical appraisal and implementation implications

This is original evidence from an operating pumped MSRE system, not from a natural-circulation surrogate. It strongly supports auditing absolute energy scale and shared metrology before fitting missing heat-transfer physics. It cannot establish TRIDENT error magnitudes or make a particular closure valid. Agreement after property revision is evidence against using the earlier primary-exchanger mismatch as proof that conventional correlations fundamentally failed. The unresolved radiator result does not isolate local recirculation.

A TRIDENT duty/flow estimate reusing the same thermometers as its validation outputs needs a joint covariance model. Independent sensor channels sharing a calibration chain should retain shared bias. Known-power tests should distinguish commanded power, electrical measurement, heat deposited into the chosen control volume and stored energy.

## Coverage and claims

| Component | Status | Limit |
|---|---|---|
| Cover, contents, abstract and introduction | Inspected; cover visual | Identity and report scope |
| Power measurement, PDF8–13/4–9 | Text inspected; Table I visual | Detailed spectral counts not reproduced |
| Air-balance/HX discussions, PDF15–29/11–25 | Selected passages inspected | Full equation/figure extraction deferred; no coefficients cleared for code |
| Conclusions PDF31–32/27–28 | Inspected; PDF31 visual | Main A5 evidence |
| References | Inspected selectively | Later calibration outcome not traced |
| Distribution list | Skipped | No relevant scientific evidence |

| Stable claim | Evidence | Locator | Qualification |
|---|---|---|---|
| S47-C01 | Reported power-metrology disagreement is not the alleged25% claim | Abstract; power measurement | PDF5–10/1–6; calibration versions differ |
| S47-C02 | Property revision resolved the primary-HX design overestimate in this report | Conclusions | PDF31/27; author's historical conclusion |
| S47-C03 | Air-radiator discrepancy and power-metrology discrepancy remained distinct unresolved issues | Conclusions | PDF31–32/27–28 |
| S47-C04 | Installed metrology and independent energy-scale checks matter | Table I; calibration discussion | PDF9–13/5–9; direct mechanism, not TRIDENT numerical error |

Next historical sources, if a complete chronology is required: later MSRE systems/component reports and the post-operation venturi calibration. These are follow-up leads; this pass does not claim the discrepancy remained unresolved forever.
