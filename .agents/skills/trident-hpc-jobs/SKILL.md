---
name: trident-hpc-jobs
description: "Prepare or monitor authorized durable TACC compute or transfer jobs using the existing Slurm scripts and completion receipts."
---

# Durable HPC work

Confirm the actual host/allocation and the already-authorized execution scope.
Read the HPC owner's `docs/workflows/SLURM_BATCH_JOBS.md` only for this task;
follow its current login-node submission route and resource limits.

- Reuse the existing job/receipt template. Save the exact command, inputs,
  resources, output/log paths and an atomic completion receipt in the owning run.
- Durable work uses saved `sbatch` submitted from a login node. An interactive
  allocation may use bounded `srun`; a detached shell is not a batch substitute.
- Size independent work to the allocated CPUs/memory, respecting the owner's
  bounded equivalence checks and task gates. Do not launch a new campaign just
  to test this skill or saturate an allocation.
- Record job ID and expected completion. Keep the conversation available; avoid
  duplicate submissions, long foreground watches and repeated log/queue reads.
  Read the receipt at completion or the next handoff.
- A file cannot wake this conversation. Do not promise push notifications or
  external messages without a configured, authorized channel.

Mac agents can prepare handoffs; they cannot assume local Slurm/TACC execution.
Preserve existing backup immutability and facility-specific data holds. Do not
ask again for authorization already established in the task.
