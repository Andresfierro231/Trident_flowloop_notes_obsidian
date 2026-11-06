---
title: "Moser proposal throughline: choices, parameters and validation"
status: maintained
owner: notes interpretation / proposal coordinator
updated: 2026-11-06
tags: [project/trident, doc/index]
---

# Moser proposal throughline: choices, parameters and validation

Tags: #project/trident #doc/index

**Sources read:** the unchanged [November 4 part2 feedback](../../X.Reference/phD_goals/Feedback_historic/'26_nov_04_moser_feedback_proposal_pt2) and the [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/M. Meeting Notes/'26 Oct 14 - Moser meeting feedback on abstract.md|October 14 Moser meeting note]]. Received in the November6 session; the filename is not an inferred new meeting date. This document interprets the advice; it is not new committee approval or a scientific result.

## Tell one connected story

1. **Motivation:** what MSR heat-transport decision needs a temperature, circulation, cooling-duty or response prediction, and why these testbeds help answer it.
2. **State of the field and completed work:** relevant literature plus the master's CFD-to-1D reduction, showing the physical and numerical experience already acquired.
3. **Proposal:** choose models, identify the parameters that must be set, and define how their predictions will be assessed. Keep these three decisions connected throughout methods and literature discussion.
4. **Execution:** end methods with a sequence of activities leading to measurable objectives, required evidence/resources, a parallel plan and a fallback.

## Aims before methods, without another competing manuscript

Moser's note says “Perhaps research aims should go before research methods.” The current four-chapter proposal order remains the author-approved structure. Implemented in proposal main on November6: a short aims overview immediately after completed evidence, before methods, with the formal hypotheses, milestones and delivery plan retained at the end. Presentation slide3 states the three aims before the balance equations; the methods include the connected modeling/parameter/validation table. This is a concrete, limited way to make the purpose of each method visible early.

## Connect each choice to parameters and a decisive comparison

| Modeling choice / question | Quantities to set or estimate | Assessment and fallback |
|---|---|---|
| Scalar temperature versus retained spatial information | Same geometry, property/source/closure definitions; explicitly matched parameter freedom | Compare transported enthalpy, local temperature and circulation against qualified common references. If a simpler boundary repair meets the target, added states are not justified. |
| Steady radial loss versus participating storage | Regional conductances, capacities, input scale and initial solid state, each with a source/bound | Heated anchor plus compatible transition, then a separate condition. If only a ratio/time constant is constrained, report that combination. |
| Bulk model output versus installed sensor response | Location/surface/footprint; contact or response assumptions where supported | Fixed-physics comparison of observer alternatives on qualified channels. Do not repair a location error by silently tuning a film. |
| Source-model reproduction versus SAM implementation | Exact physical case and native input/CLI; source placement and represented solid paths fixed | First convergence and mass/energy/numerical checks; then independent physical comparison. A failed root remains a numerical checkpoint, not a prediction. |

These are study contracts, not newly completed comparisons. The active proposal's case tables and actual-input index govern S1/S2/R1; do not replace those explanations with this planning table.

**Model/BC/IC/numerical tables and actual inputs before discussing results:** [case explanations](https://github.com/Andresfierro231/Andres_Fierro_Dissertation_Proposal/blob/0c3a27478fdd5278005c97b6c415ae0dd314156c/presentation/SIMULATION_ASSUMPTIONS.md), [executed inputs/code/receipts](https://github.com/Andresfierro231/Andres_Fierro_Dissertation_Proposal/blob/0c3a27478fdd5278005c97b6c415ae0dd314156c/presentation/AS_RUN_INPUT_INDEX.md). These are engineering provenance links, not literature citations.

## What the draft can already demonstrate

- **Master's thesis:** conservation-based CFD reduction, an executable periodic steady solver and physical-budget assessment. This is the main completed-work foundation. A numerical thesis plot must still carry its own complete setup and input record before it is added.
- **S1:** a specified synthetic thermal implementation comparison, with its full model/BC/IC/numerical/source appendix. It supports one implementation step, not physical-loop or natural-circulation validation.
- **S2:** the original scalar TAMU implementation has no accepted full-loop root. Its failure explains a next numerical task; it cannot be presented as a physical operating limit.
- **R1:** original conditional resistance code and same-data inverse/forward algebra are recovered. The two-code whole-network replay and independent experimental test are still deliverables.

Use these results along the proposed progression to show why the first approach is plausible, what experience already exists and what failure changes the next step. See the active proposal repository for the full assumptions and actual inputs; this is not a second editable proposal.

## Gaps to close, in order

| Priority | Missing material | Reviewable deliverable / success |
|---|---|---|
|1|Application motivation and testbed relevance|One–two opening slides/pages connecting decision → output → phenomenon → testbed measurement/model. Do not simply label a loop an MSRE primary/secondary surrogate.|
|2|Specific reactor relevance|A source-backed MSRE primary/secondary heat-path diagram and an explicit applicability/difference table; current commercial example only after primary-source checking. The feedback itself does not establish this mapping.|
|3|Master's quantitative demonstration|One exact original case with model/closure/tuning/BC/IC/observer/numerical/input tables; explain how its local-budget finding motivates the next model choice.|
|4|Full-circle heated demonstration|Qualified case → supported boundary inference → matched Trident/SAM forward replay → frozen independent condition. Reconstruction and prediction stay separate.|
|5|Effort/resources and fallback|For each objective: inputs needed, case/parameter dimensions, measured accepted-run cost and refinement/UQ budget, responsible track and feedback gate. Do not infer campaign cost from failed-root runtime.|

Check existing Brown/MSR-phenomena, Reis/TAMU and Gabbard/MSRE material and their dossiers before requesting a new literature review. This pass has not rechecked those primary sources, drawn an MSRE schematic or selected a commercial design; no reactor mapping or new literature gap is claimed established. No external contact or scientific execution is authorized by this note.

**Active authoring owner:** separate `Andres_Fierro_Dissertation_Proposal` Git repository, `main.tex`, `presentation/POWERPOINT_OUTLINE_COMMITTEE_REVISION.md`, and `doc_support/committee/EXPLANATION_GUIDE.md`. Local aliases must be configured on the local computer; their existence is not inferred here. [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/03_proposal/README.md|Proposal route]] provides the maintained owner map.
