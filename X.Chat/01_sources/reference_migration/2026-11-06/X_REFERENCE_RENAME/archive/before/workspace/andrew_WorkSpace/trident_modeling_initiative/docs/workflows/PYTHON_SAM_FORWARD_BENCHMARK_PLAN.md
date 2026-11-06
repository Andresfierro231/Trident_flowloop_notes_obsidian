---
title: Planned declared Python and SAM forward-model benchmark
status: active
last_updated: 2026-09-16
tags: [project/trident, doc/specification, domain/thermal_network, domain/flow, facility/acu, status/provisional]
---

# Planned Python/SAM forward-model benchmark

Tags: #project/trident #doc/specification #domain/thermal_network #domain/flow #facility/acu #status/provisional

The user identified **comparison against SAM as the next research phase**
after cooler implementation and the [M3 root study](M3_ROOT_DISCRIMINATION_STUDY_PLAN.md).
Future agents should route through [SAM-001](../../coordination/tasks/SAM-001.md).
SAM is established and useful as an independent software benchmark, but
agreement with SAM is not equivalent to conservation verification or facility
validation. Preserve discrepancies, do not tune the Python model to a
non-equivalent SAM case, and do not infer a SAM result from an input file.

## Current source-form discrepancy to resolve first

The read-only [detailed SAM input](../../reference/trident_acu_loop_detailed.i)
uses a 90 W-labelled positive-valued `cooler_volumetric_power` as
`heat_source` in the primary-fluid `CoolingJacket` component near lines
35, 140 and 276. The [simple input](../../reference/trident_acu_loop_simple.i)
uses the whole top-leg footprint instead. The comment calls it heat
*removal*, but the input expression is positive. The bounded probe below
checks the source's temperature effect; steady duty and full exported
energy/flow behavior still need a matched run before calling it a cooler.
The SAM geometries also differ from provisional
ACU Rev B physical arc lengths and jacket limits. The predictive Python
[jacket model](../theory/STEADY_COOLER_MODEL_FORMS.md) removes heat at
pipe wall and predicts secondary outlet; it is not form-equivalent to the
current SAM fluid source. The Python diagnostic supports both `+90 W`
removed and `-90 W` removed (i.e. 90 W added) on the fluid layer solely
to investigate sign/placement. Neither has a reviewed SAM alignment ID.

The [bounded SAM-001 source-sign probe](../../reports/benchmarks/SAM_SOURCE_SIGN_DIAGNOSTIC.md)
now supplies actual `+90/-90 W` one-step exports: the positive case has
a warmer primary cooler outlet than the negative case, consistent with
positive `heat_source` **heating**, not the comment's “removal.” The
installed executable identifies SAM commit `c2afbe17f`; both runs use
copies of the same SHA-pinned input and record exact CSV hashes. Seven
unused input declarations include `T_amb` and `h_amb`, so those named
ambient settings are not applied by the detailed case. This resolves a
bounded sign question but does not supply a steady duty ledger or common
Python–SAM case; no alignment ID is assigned.

A separate [synthetic one-pipe pilot](../../reports/benchmarks/SAM_ONE_PIPE_ENERGY_BALANCE_PHASE1.md)
now compares an actual stationary SAM fluid-source run against the
implemented Python M2 specific-enthalpy law at declared constant `c_p`,
mass flow, source volume, and inlet temperature. The guarded crosswalk
checks exact fixture/export hashes and yields a component integrated-energy
residual; it is **not** a periodic M2 or natural-circulation M3 code-to-code
match. This staged gate is recorded in [ADR-0019](../decisions/ADR-0019-stage-sam-benchmark-by-shared-physics.md).

The [full-loop source-pinned crosswalk](../../config/examples/sam/acu_full_loop_form_crosswalk_v1.yaml)
now inventories fourteen required fields in the current Python M3 and
read-only detailed SAM cases. Twelve differ and two remain unresolved;
the [gate report](../../reports/benchmarks/SAM_FULL_LOOP_FORM_GATE_V1.md)
explains why **no full-loop alignment ID or numerical delta** is issued.
The comparison interface now requires an assessed crosswalk in addition to
matching ID text, exact resolved Python/SAM input hashes, and a verified
native SAM export hash before it permits diagnostic full-loop deltas. A new
matched SAM fixture and actual export are still required.

## Benchmark sequence and guardrails

1. Inventory exact SAM executable/source revision, input SHA-256,
   component heat-source sign convention, runtime settings and export
   channels. Require a run/export ID and unit map; never use source input
   values as reference output. Use read-only copies and no repo runtime
   dependency on machine-specific SAM paths.
2. Construct a case-form crosswalk: facility/geometry representation,
   pipe ID/length/elevation, mesh, source/sink axial footprint and radial
   layer, fluid/solid properties, ambient/cooler/loss closures, pressure/
   exit topology, heater duty/efficiency, and solver tolerances. Name the
   differences first. Declare an alignment ID only after the form and sign
   are independently reviewed; preserve non-equivalent forms as separate
   rows rather than comparing residuals as validation.
3. The first constant-property fluid-source *component* pilot is complete
   but awaits outside review; next build analytic/no-flow and prescribed
   signed-flow **full-loop** cases with an exact source/geometry/topology
   crosswalk. Then compare predictive wall-jacket
   forms only after SAM is configured to an actually equivalent boundary.
   Each stage compares conservation ledger, flow candidates, temperature
   stations, imposed/predicted cooler duty and, if modeled in SAM, secondary
   outlet. Treat root branches individually; no closest-root selection.
4. The [cooler matrix](../../config/examples/m3/cooler_matrix.yaml) and
   [case runner/guarded wrapper](../../src/trident_thermal/reporting/sam_compare.py)
   retain resolved Python variants, source hashes and every M3 candidate.
   A SAM normalized JSON wrapper must declare run/revision, source/export
   SHA-256, units, model-form alignment evidence and source placement.
   Until an actual export and crosswalk exist, all SAM IDs in examples
   remain null and the comparison reports no agreement.
5. Publish a versioned side-by-side discrepancy report with exact cases,
   raw export lineage, per-term differences, unit/sign conversions,
   numerical sensitivity, and unresolved physics/form mismatches. If a
   difference is caused by non-equivalence, report that before interpreting
   magnitude. Outside review is required before a scientific conclusion.

This plan supports a high-value benchmark phase without restarting the
paused inverse-modeling/data-comparison work.
