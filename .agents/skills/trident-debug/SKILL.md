---
name: trident-debug
description: "Diagnose reproducible solver, script or build failures; use a small feedback loop before changing the implementation."
---

# Focused diagnosis

Use the owning task and current code; preserve unrelated dirty files and issued
results. Start with the smallest relevant error and exact invocation.

- Build or reuse a bounded pass/fail reproduction that exercises the reported
  symptom. A successful process exit alone may not test numerical correctness.
- Pin inputs and random seeds when relevant. Compare an independent calculation,
  prior revision or alternate configuration only when it isolates a hypothesis.
- State a hypothesis, run one discriminating check and inspect the result.
  Minimize the reproducer before broadening tests or instrumentation.
- If execution is unavailable, perform a qualified static diagnosis and identify
  the exact missing evidence. Do not block useful work behind a mandatory
  questionnaire or demand instrumentation that the task does not need.
- Fix the cause, verify the original symptom and run the owner's affected checks.
  Stop broadening once the issue and material regressions are covered.

No automatic stress campaign, dependency installation, reviewer agents or
external-service calls. Expensive runs use the existing HPC execution workflow;
this skill does not authorize them. Keep full logs with the task and show a short
result with the remaining uncertainty.
