---
name: trident-manuscript
description: "Revise or build the Trident LaTeX manuscripts while preserving author format, bibliography alignment and existing build checks."
---

# Manuscript revision

Resolve the requested manuscript owner and read its current `AGENTS.md` and build
entry point. An external reference's default manuscript does not change the task.

- Edit the active source, not an archived staged copy. Preserve the author's
  current structure and format; the proposal currently uses concise bullets.
- Preserve citation keys and source evidence. Use the owner's bibliography tool
  for numbering; align its Markdown companion if the compiled order changes.
- Prefer the existing build script and a separate output directory. On TACC,
  load `module load texlive/2023` in the build shell if needed; report the actual
  compiler version rather than inferring it from the module name.
- Check compiler exit status, undefined citations/references and overfull boxes
  in text logs. A PDF build does not authorize viewing its pages.
- Use existing numerical transcription/equation checks only when the changed
  content affects them. Do not rebuild or rerun unrelated studies for an agent
  instruction, link or ordinary Markdown-only edit.

Put detailed source audits and coordination in the owner's existing support
records. Rendered committee text stays brief. No invented results, silent changes
to property laws, new experiments or unrequested journal-submission procedures.
