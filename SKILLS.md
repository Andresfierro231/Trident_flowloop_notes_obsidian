---
title: Trident on-demand skills
status: maintained
owner: notes skill pack
updated: 2026-11-04
tags: [project/trident, doc/index, domain/agent_coordination]
---

# Skill catalog

Use native skill names/descriptions first. This is the fallback index when they
are unavailable. At task start or a scope change, select only the relevant skill;
routine work can need none. Read its `SKILL.md`, not the whole pack. Load another
only for a distinct required subtask. Existing owner instructions and user scope apply.

| Skill | When useful |
|---|---|
| [trident-code-review](.agents/skills/trident-code-review/SKILL.md) | Review a scoped diff for requirement fidelity and correctness when asked for a code review or a substantial implementation check. |
| [trident-debug](.agents/skills/trident-debug/SKILL.md) | Diagnose reproducible solver, script or build failures; use a small feedback loop before changing the implementation. |
| [trident-equation-audit](.agents/skills/trident-equation-audit/SKILL.md) | Check model equations against implementation, units, signs and conservation when reviewing or changing mathematical balances. |
| [trident-hpc-jobs](.agents/skills/trident-hpc-jobs/SKILL.md) | Prepare or monitor authorized durable TACC compute or transfer jobs using the existing Slurm scripts and completion receipts. |
| [trident-manuscript](.agents/skills/trident-manuscript/SKILL.md) | Revise or build the Trident LaTeX manuscripts while preserving author format, bibliography alignment and existing build checks. |
| [trident-obsidian](.agents/skills/trident-obsidian/SKILL.md) | Maintain Obsidian wikilinks, embeds, properties and note organization when editing the Trident notes vault. |
| [trident-source-check](.agents/skills/trident-source-check/SKILL.md) | Verify citations and original property correlations when adding references, tracing coefficients or checking scientific claims. |

Optional offline lookup: `python3 .agents/skills/_support/catalog.py list --match equation`.
[Maintenance, setup and source provenance](.agents/skills/_support/README.md)
are needed only when adding/updating skills or setting up another checkout.
