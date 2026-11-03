# Working understanding — literature, plans and HPC evidence

- Status: maintained synthesis, November 2; [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/00_navigation/LITERATURE_RESOURCES.md|literature sources and answers]], [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/HPC_REPORT_MAP.md|HPC routes HC01–HC16]], [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/02_synthesis/PLANNING_COVERAGE.md|planning coverage]].
- Organizing authority: the author’s proposal goals, scientific questions and research tasks. The review supplies evidence/answers alongside modeling reports, experiment records and notes.
- Current source evidence is richer than the first organization pass. Treat this note as the interpretation owner and follow exact records before changing theory or implementation.

## Research purpose and contribution

- Develop and assess a CFD–experiment order-reduction framework yielding a fast, interpretable physical ROM.
  - Conservation, development-informed closures and observation-consistent temperature maps describe the proposed method. [Review A §§1–7/11/14; B §§10–11]
  - Completed CSEM and CAL work establish groundwork and limits; another fit or an extra state is not itself a new finding. [B §7; HC01]
- Approved scope: steady performance/margins → transitions → operational assistance; UQ throughout. [HC02]
  - Immediate author emphasis: understand experimental data and reproduce temperatures, leaning on the master's work.
  - Minimum later-stage demonstration and numerical acceptance criteria remain design choices, not reasons to postpone organizing the outline.

## Distinct model families

- TRIDENT M0/M1/M2/M3: diagnostic radial/no-flow/known-flow/coupled steady circulation hierarchy. [HC05; A §§2–3]
  - M1 is a segmented no-flow energy model with configured axial conduction; it is not necessarily a set of uncoupled radial rings.
  - M2 retains signed conservative enthalpy transport; M3 solves candidate steady buoyancy/resistance roots and does not supply transient circulation inertia.
- Conditional VCU shell studies: measured primary-temperature/ambient histories drive radial solid response. [HC09; HC16]
  - Useful for wall/boundary/initial-state comparisons, but do not independently predict supplied primary temperatures or circulation.
  - The nonlinear exterior operator freezes material properties at a declared reference, uses supplied boundaries and fixed initial-profile policies, and is not a resolved bare-patch sensor model.
- Isolated historical TAMU polar/developing benchmark: separate research/manual/continuation family. [HC06–HC08]
  - Distinguishes area temperature, enthalpy-transport temperature and probe temperature; those meanings affect buoyancy, heat transport and observations differently.
  - Candidate lesson for TRIDENT: test the smallest profile/covariance addition that matters to a target; no automatic coefficient/solver port or facility validation.

## Data and boundary understanding

- Every record needs raw identity, source rows, clock/units, channel/geometry revision, quality flags, transformations and development/assessment history. [HC03–HC04; A §§5/10/15]
  - Preserve raw data and rejected/flagged samples; the old plan's four-standard-deviation rule is a historical idea, not an adopted universal exclusion policy.
  - State grouping should retain actual source/sink/environment histories and within-group variation; nearby settings are not automatically interchangeable physics.
- VCU has later run-index and steady-window work beyond CAL-008–010. [HC11]
  - CAL-012 selected-channel/averaging rules and CAL-016 all-recorded-channel raw-range rules differ. Do not merge their passing windows.
  - Recorded temperatures passing a ten-minute screen do not prove heater/cooler constancy, no hidden storage or qualified power delivery.
- CAL-019 accepts nominal 20-ohm mats/48-ohm bands and dial=loaded-RMS as declared assumptions. [HC10]
  - This supports nominal calculations now; additional electrical characterization is optional for improving confidence, not a prerequisite to using the accepted nominal specification.
  - Nominal generation is not metered deposited power or net heat into fluid; source-to-solid/fluid ownership, storage/contact/losses and run exceptions remain explicit.
- ACU source adapters/observation ledgers exist as provisional/synthetically checked interfaces; the read archived note does not establish qualified installed channel/units/run mappings. [HC04]
  - Do not interpret this as a current live status report; request changed evidence from HPC. Existing ACU processing restrictions remain.

## Learning, mapping and uncertainty

- Separate physical-parameter/closure learning, bulk-to-sensor observation mapping and residual discrepancy correction. [A §§4–8; G01]
  - Compare ordinary interpolation/physics against modest learned alternatives before committing to GNN/LSTM/neural operators.
  - Temperature/pressure ratios depend on reference conventions and can be ill-conditioned; use a justified difference/scale or physical observation map instead of adopting a universal raw ratio.
  - Reduced bias after correction is not proof that the physical closure improved. Score raw and corrected predictions with the same held-out conditions.
- Shared calibration, power, properties and boundary/initial information propagate jointly; temporal variability alone is not total uncertainty. [A §8; HC14]
  - Sensor-loss/drift diagnostics are useful planning branches. They need observation coverage and matched tests before being described as deployed anomaly detection.

## Program integration and communication

- The plan includes model/data identifiers, provenance chains, historical/replay/live displays and collaborator roles. [G01; HC13/HC15]
  - Program context expands the thesis explanation; historical software names and collaborator assignments do not select the current stack or imply completed integration.
  - Dashboard/interface work remains with Ben Booth/NeutronOS. A display prototype, prediction service, operator advice and equipment control have different evidence requirements.
- The user requested a Box-mediated Q&A route: [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/06_hpc_exchange/README.md|HPC exchange]].
  - Prepared files and an export package do not imply delivery, acknowledgment, current HPC status or authorization to run new scientific work.
  - Use replies to update exact source/status pointers and integrate evidence; keep original responses and dated decisions intact.
