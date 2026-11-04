# Maintaining the Trident skill pack

Read this only to change the pack or set up a checkout. Routine agents use native
metadata or `SKILLS.md`, then load only the relevant skill. The helper requires Python3.9+ and the standard library only. The seven skills add
no model calls, dependencies, hooks, services or automatic reviewers.

## One owner, machine-local discovery

The notes Git repository owns `.agents/skills/` and generated `SKILLS.md`.
Pull/commit/push that repository under its existing Git rules. HPC initiative
and proposal remain separate owners; a skill cannot change their instructions,
research direction, evidence gates or execution authorization.

From the **notes checkout** on either Mac or TACC:

```bash
python3 -B .agents/skills/_support/catalog.py check
python3 -B .agents/skills/_support/catalog.py link --target '/actual/other/project'
python3 -B .agents/skills/_support/catalog.py link --target '/actual/other/project' --apply
```

The first link command is a dry run. The second creates relative links for
`<target>/.agents/skills` and `<target>/SKILLS.md`, without copying skills.
Verify the target using its current machine map; no Mac/TACC path substitution.
Do not run the link command again inside subfolders of an already configured
Git repository. The helper detects inherited aliases and avoids duplicate discovery.

Links are local setup, not Git transport. In another Git owner, ignore exactly
`/.agents/skills` and `/SKILLS.md` rather than committing machine-relative aliases.
Preserve any existing skill directory/catalog: the helper refuses collisions,
including broken links, and has no force option. Repeated correct setup is a no-op.
Moving a checkout may require recreating its known local aliases after inspection.
The short discovery hook in each owner's AGENTS.md is versioned separately.

Codex discovers repository `.agents/skills` metadata; the full `SKILL.md` is
loaded only when selected. Other agents can use the same fallback catalog.
If a running client has cached discovery, reload/restart it; the AGENTS/catalog
route is immediately readable. Do not infer one client's discovery from another.
[Official discovery contract](https://learn.chatgpt.com/docs/build-skills).

## Cheap use and extension

```bash
python3 -B .agents/skills/_support/catalog.py list --match equation
python3 -B .agents/skills/_support/catalog.py check
python3 -B .agents/skills/_support/test_catalog.py
```

`list` prints metadata only; `--match` is a literal filter, not an LLM router.
Keep the active model; do not escalate models or spawn paid reviews to use a skill.
Ordinary tasks may need no skill. Choose one primary skill, adding another only
for a distinct necessary subtask. Do not reload the catalog for every tool call,
read every skill/reference at startup, or call a model to select a skill.

To add a skill, create one descriptive `trident-*/SKILL.md` with `name` and a
single JSON-quoted YAML `description`. Keep the body self-contained and narrow;
link substantial conditional detail only when needed. Reuse existing owner
scripts/documents rather than duplicate them. Update `_support/sources.json`
with a reviewed source or classify the new entry as an original Trident skill.
Then run `render`, `check` and the smoke tests above. The catalog is generated
from skill metadata; no second manual list needs maintenance.

Budgets are enforced by `catalog.py`:160characters per description,
1400combined description characters,2600characters per skill and3200for the
fallback catalog. These are text-growth limits, not exact token measurements.
The check reports a rough characters/4 estimate including this host's paths;
actual tokens, host overhead and billing vary. Expansion should narrow/split
unrelated workflows before raising these limits. Keep expensive/model-based
validation opt-in and justified by the change.

## Provenance and updates

`_support/sources.json` pins reviewed upstream commits, source paths, hashes,
selected concepts and deliberately omitted behavior. All skill bodies are
concise local adaptations/original wording; no upstream SKILL.md, installer or
executable script is vendored or run. Attribution notices for reviewed MIT
sources are retained under `_support/licenses/`.

- Matt Pocock: bounded reproducible debugging and requirement/standards review.
- Kepano: Obsidian syntax adapted to this vault's existing routes and originals.
- K-Dense: evidence binding and explicit unresolved scientific provenance.
- OpenAI: metadata-first skill packaging and discovery; no external plugin bundle.

Upstream changes are not pulled automatically. Review the specific needed
change, preserve local exceptions, update its pin/hash/notice, then run offline
checks and a realistic bounded use case. Existing user authorization governs;
this process adds no new permission or approval ritual.
