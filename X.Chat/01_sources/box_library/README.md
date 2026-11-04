---
title: Box literature discovery catalog
owner: literature writer
status: maintained
updated: 2026-11-04
tags: [project/trident, doc/source]
---

# Find a source without loading the library

From the notes Git root (Mac uses /Users/andres/miniforge3/bin/python3):

    python3 tools/box_library.py search 'natural circulation' --limit 8
    python3 tools/box_library.py show BL-<search-result-ID>
    python3 tools/box_library.py note BL-<search-result-ID>
    python3 tools/box_library.py refresh --root /verified/local/library/root

- Start with search, one show record, then the original pages needed for the question. AND terms search folder/category, abstract candidates, keywords, DOI candidates, title and curated metadata. Eight results by default; placeholders above are not literal source IDs.
- catalog.jsonl: one record per unique readable document (or provisional unreadable file); paths, full SHA-256, categories, automatic topics, native keywords, abstract candidate and extraction status.
- search.csv: compact spreadsheet/rg index including every current document's paths. Avoid loading the full catalog into chat.
- LAST_SCAN.json: coverage/errors and latest added/changed/removed/moved IDs. history.jsonl preserves earlier changes.
- annotations.json: human-curated fields keyed by BL ID; never overwritten by refresh. Add verified title/authors/year/DOI, tags, existing_source_ids, abstract/summary with exact locator/provenance. Show exposes curation separately; search includes it.
- notes/: opt-in reading notes; note command creates once and refuses overwrite. Search notes with rg in that small folder, and add curated searchable tags to annotations.
- REVIEW_QUEUE.csv: abstract/identity extraction status, regenerated on refresh.
- Legacy ../box_literature_inventory.csv keeps its filename-only role; existing paths/script preserved.

## Identity and repeatability
- BL ID uses the first 20 hex characters of full SHA-256, with full-hash collision checks. Hashing is retried every refresh with six bounded local I/O workers and a five-second per-file timeout. Byte-identical duplicates share one record and multiple locations; different exports/editions have different IDs.
- Rename retains ID; changed bytes create a new version ID. History records path-based old/new IDs and old/new alias lists. Missing documents remain not_present records, preserving note references.
- Categories preserve actual folders. Topics are regex discovery tags, not scientific classification. Native keywords remain separate.
- Pass the verified root per machine. Mac default is the user's Box books/research directory. Missing/empty roots and filesystem errors stop intake; do not interpret an unavailable library as mass removal.
- No originals renamed/moved/written; no symlink recursion, network metadata, model calls, image/OCR/CAD processing or full-document ingestion. Unavailable bytes receive a clearly provisional PENDING-path-hash ID, not a content identity; a successful later read replaces it with a BL content ID and records the transition. Provisional IDs cannot establish duplicates or survive renames. No source is omitted merely because its bytes are unavailable.
- Initial PDF text intake examines at most five pages, with a 30-second timeout per file. Word documents use bounded body XML text; CSV support tables are cataloged as supporting data, not papers with abstracts. Unchanged hashes reuse extraction.
- PDF extraction needs pdfminer.six. Other operations use the standard library. Missing dependency/parse/timeout failures become explicit extraction_error entries. Remote agents can search the Git catalog without Box access.
- One writer owns refresh; commit catalog/index/history together after checking LAST_SCAN.json.

## Abstract and evidence limits
- extracted_candidate means a literal Abstract heading was found, with page and boundary method. A reader must check columns, headers and text extraction.
- not_found_in_first_5_pages does not mean the source lacks an abstract. Books may have none or place it elsewhere.
- no_extractable_text, unsupported_format and extraction_error stay visible; no abstract is fabricated.
- Opening excerpts are short literal locators, not abstracts or generated scientific summaries. Descriptions are filename/folder metadata.
- DOI candidates can belong to cited references; verify the document's own DOI. Filename titles remain unverified.
- Read exact pages/equations/tables before citing a claim. Catalog intake is not scientific review.
- Existing S/claim/question IDs retain their owners. BL IDs identify library files and do not replace bibliographic identities or organize research scope.

## Long-term growth
One catalog, one optional note per document version, one maintained synthesis per question. Curate promising sources rather than creating empty notes for every file. Cross-link old/new versions and existing source IDs. Freeze review milestones in Git; keep PDFs in Box.

- To retry cached failed extraction or deliberately improve the parser intake, run refresh --reextract; this reopens text sources while retaining IDs and separate annotations/notes. Run normal refresh twice to confirm empty changes after intake.

- Category map: [[MainVault/Box/Andres_Obsidian_Notes_Box/Trident_FlowLoop_Notes/X.Chat/01_sources/box_library/CATEGORY_MAP.md|folder and topic counts]]. Regenerated by refresh, alongside the review queue. Catalog vault_targets are exact Obsidian source routes; source paths are resolved under the verified machine root.

- If a known path temporarily cannot be read, the old content record becomes unverified_current_bytes, not a claim of deletion or changed bytes. Availability events are separate from content changes. Provisional records become superseded_provisional after successful hashing.
