---
title: Box literature catalog intake
owner: LIB-001 Mac writer
status: review
updated: 2026-11-04
tags: [project/trident, doc/handoff]
---

# Extended Box literature discovery
- Local Darwin/Mac; notes base 32394f5 pulled on isolated edit/box-library-catalog-2026-11-04. Canonical notes checkout's unrelated material-note whitespace remains untouched.
- Source owner: /Users/andres/ObsidianVaults/MainVault/Box/books/research. All 175 files indexed; 173 SHA-256 identities, two additional byte-identical copies, zero unavailable hashes after the initial Box access delay resolved.
- Text intake only: PDF first five pages (including unusual filename extensions), bounded Word body text and text/CSV excerpts. No image rendering/OCR/CAD, external metadata requests or model calls. No Box originals written/moved/renamed.
- Abstract coverage:102 extracted candidates;60 not found in bounded intake;2 PDFs with no extractable text;9 CSV support records with abstract not applicable. All candidates need primary-page verification, not scientific-review status.
- New source owner X.Chat/01_sources/box_library/: JSONL catalog, compact CSV, last-scan report, history, category map, review queue; separate curated annotations and opt-in reading notes. Original box_literature_inventory.csv and existing S/claim/question identities preserved.
- Tool: tools/box_library.py refresh/search/show/note. Content IDs survive rename and identify identical copies; changed bytes create a new version; removed records remain. Unavailable bytes have provisional IDs and separate availability events, not assertions of changed/deleted content.
- Three integration/regression tests pass (identity/rename/change/duplicate/removal; curation/symlink/missing-root preservation; no fabricated abstracts; transient read failures). Repeated actual-library refresh produced byte-identical catalog and empty change set. Catalog approximately606KB; search returns eight compact hits by default.
- Maintained navigation check passes in isolated worktree. Full Obsidian links to new files must be rechecked after integration, because the real vault alias targets the canonical main checkout.
- Proposal independently checked/pulled: already current; no manuscript/scientific changes. Notes publication is actual Git HEAD/origin; Git visibility is not remote researcher acknowledgment.
- Next: agents search narrowly, open one ID, verify original pages/identity/abstract, create a note only when reading, map existing source IDs and record useful keywords in annotations. Missing abstract is an explicit review queue, not invented text.
