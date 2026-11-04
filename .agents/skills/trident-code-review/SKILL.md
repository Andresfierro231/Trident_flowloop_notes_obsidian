---
name: trident-code-review
description: "Review a scoped diff for requirement fidelity and correctness when asked for a code review or a substantial implementation check."
---

# Scoped review

Identify the owner, requested change and exact diff or files. Use the supplied
baseline; if none is given, inspect the current task diff without attributing
pre-existing dirty work to this task.

Review two distinct questions:
- Does the change implement the user-approved requirement and selected physical
  model? Trace important equations or numerical behavior to actual code/tests.
- Does it respect the owner's documented conventions and interfaces? Prioritize
  correctness, conservation, regressions and maintainability over style preferences.

Read only affected contracts and dependencies. Use existing deterministic tooling
for checks it already enforces; do not invent a new issue tracker or mandatory
specification document. Do not launch parallel reviewers by default.

Report actionable findings with file/line, concrete failure or risk, and severity.
Separate demonstrated defects from questions and optional improvements. If there
are no findings, state the checks and remaining test limits rather than making
an unqualified correctness claim. Review does not authorize editing or committing
another owner's files.
