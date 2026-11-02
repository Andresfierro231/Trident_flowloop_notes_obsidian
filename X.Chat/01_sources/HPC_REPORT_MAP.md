# HPC modeling report map

- Saved source: [October 23 checkpoint](</Users/andres/Box-Box/VCU ACU Shared Research/TRIDENT_Modeling_Archives/2026-10-23_OPS-002_results_backup_20261023T192726Z>); `completion.json` records `complete_verified`, finished October 26. This task read the receipt, not a fresh full-backup validation.
- Extracted 1,560 Markdown working/report records to scratch and matched each to the saved inventory hash; cataloged the 791 report records. Cataloged does not mean fully read.
- [Report catalog](hpc_report_catalog.csv) carries exact archive/member, heading, frontmatter status and hash. [Selected-source manifest](hpc_source_manifest.json) carries reading depth for the routes below.
- Original documents stay inside the immutable archives; exact member paths below are relative to `trident_modeling_initiative/`. The working/report archive column is the retrieval locator.
- Source status and any reported results describe the saved checkpoint, not verified current HPC behavior. External-symlink gaps are recorded in the checkpoint; do not invent missing external CFD results.

| Route | Question answered | Archive | Exact source member | Use / boundary |
|---|---|---|---|---|
| HC01 | Start here for derivations/major decisions; use study homes and dated continuations | `reports.tar.zst` | `reports/IMPORTANT_REPORTS.md` | Maintained report/derivation/decision entry; selected route rows read |
| HC02 | Scope and stage ownership; scope approval is not completion | `working.tar.zst` | `docs/project/RESEARCH_ROADMAP.md` | Approved three-stage scope; full text read |
| HC03 | Data provenance/quality/window/uncertainty roles; contract is broader than implemented features | `working.tar.zst` | `docs/data/DATA_CONTRACT.md` | Raw-to-observation fields, window/role/provenance contract; full text read |
| HC04 | ACU adapter and observation ledger; synthetic/provisional, installed mappings not qualified in this note | `working.tar.zst` | `docs/data/OBSERVATION_COMPARISON_PIPELINE.md` | Implemented ACU adapter/observation bridge and unresolved qualification; full text read |
| HC05 | M0/M1/M2/M3, shell and benchmark families; preserve their distinct assumptions | `working.tar.zst` | `docs/theory/README.md` | Theory family index; entry read |
| HC06 | TAMU reconstruction manual route; fixed-cooler/inherited-law and resolution limits | `working.tar.zst` | `docs/theory/TAMU_ROM_RECONSTRUCTION.md` | Manual/continuation/source boundaries; full text read |
| HC07 | Cross-sectional temperature/buoyancy, heat paths, hydraulics and Trident transfer candidates | `reports.tar.zst` | `reports/research/2026/10/2026-10-20_TAMU-BUOY-009_buoyancy_studies/2026-10-21/TAMU-TRIDENT-015_trident_applicability/REPORT.md` | Transfer table and first mechanism sections read; later sections remain pointers |
| HC08 | October 26 bounded campaign authorized; need later completion/result receipt | `working.tar.zst` | `docs/decisions/2026-10-26_TAMU-TRIDENT-016_batch-studies.md` | Bounded historical TAMU campaign authorization; full text read, completion not inferred |
| HC09 | Prescribed-primary conditional radial model; not a full circulating prediction | `working.tar.zst` | `docs/theory/VCU_NONLINEAR_CONDITIONAL_BOUNDARY.md` | Nonlinear conditional shell model, initialization and evidence limits; full text read |
| HC10 | Accepted nominal electrical estimate; no metered or net-fluid power claim | `working.tar.zst` | `docs/decisions/2026-10-22_CAL-019_nominal_heater_power.md` | Accepted nominal heater assumptions and net-fluid boundary distinction; full text read |
| HC11 | VCU run/history/steady-rule inventory; temperature steadiness is not full energy equilibrium | `reports.tar.zst` | `reports/data/VCU_EXPERIMENT_INDEX.md` | Run-index header and selected rows read; per-run files not fully audited |
| HC12 | Prepared experiment amendments and role/anchor requirements; not agreed or executed new tests | `working.tar.zst` | `docs/experiments/RESEARCH_DATA_REQUIREMENTS.md` | Existing data-request sequence and nominal-power amendment; relevant sections read |
| HC13 | Ben Booth/NeutronOS requirements/interface development; not deployed controls | `working.tar.zst` | `docs/dashboard/README.md` | Collaborative interface requirements/status; full text read |
| HC14 | Required total-UQ budget; no claim end-to-end propagation is already implemented | `working.tar.zst` | `docs/uncertainty/README.md` | Core uncertainty contract/status; full text read |
| HC15 | Clarno Vision/ModSim program context; expands understanding without replacing thesis scope | `reports.tar.zst` | `reports/proposal/2026/10/phd_research_framework/2026-10-21/DOC-035_clarno_program_context/README.md` | Program-reference entry and role/scope context; selected sections read |
| HC16 | Continuing solver write-up, boundary/regional/downcomer comparisons and linked derivations | `reports.tar.zst` | `reports/solver/2026/10/clarno_solver_guide/2026-10-21/RPT-001_friday_writeup/README.md` | Continuing solver-report entry and later-study routes; selected updates read |

## Report families

- `IMPORTANT_REPORTS.md`: 1 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `README.md`: 1 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `benchmarks`: 7 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `checkpoints`: 6 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `data`: 472 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `geometry`: 38 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `operations`: 16 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `proposal`: 51 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `research`: 44 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `solver`: 131 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.
- `verification`: 24 Markdown records, including indexes/continuations/case notes; not a count of distinct scientific studies.

## Reading path by task

- Proposal/scope: HC02 → HC15 → existing DOC-026/028/029/034 routes in HC01 → current local literature synthesis.
- Temperature reproduction: HC03 → HC11 → HC16 → HC09, with source/initial/boundary information explicit.
- Full-loop model: HC05 → exact M1/M2/M3/cooler theory → verification checkpoints; distinguish synthetic numerics from facility evidence.
- Developing-profile/recirculation research: HC06 → HC07 → HC08; retain TAMU owner and transfer gates.
- UQ/data needs: HC14 → literature A §§8–9/15 → HC12; do not ask for provisions already present in Nick’s protocols.
- Operational use: HC13 → current plan result/provenance needs; offline/online/decision/control stages are separate.
- Once an HPC reply supplies newer evidence, append its commit/report identity and supersession rather than rewriting what this checkpoint contained.
