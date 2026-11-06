---
title: Reviewed Box reference imports
status: maintained
last_updated: 2026-09-07
tags: [project/trident, doc/index, domain/data, facility/shared]
---

# Reviewed Box reference imports

Tags: #project/trident #doc/index #domain/data #facility/shared

## Purpose

This folder holds selected, immutable source documents copied from Box after
review. It is not a Box mirror, credential store, or bulk-data landing area.

## Package contract

Each import uses a dated subfolder containing:

- the exact retrieved document;
- `SOURCE_MANIFEST.yaml` based on `SOURCE_MANIFEST.example.yaml`;
- no derived analysis or modified replacement of the source.

Unreviewed and bulk downloads belong under ignored `data/staging/box/`. Follow
the [Box document workflow](../../docs/workflows/BOX_DOCUMENT_ACCESS.md).

## Authority and retention

Imported documents are source evidence, not automatically verified facility
truth. Preserve them in Git only when licensing, sensitivity, and size permit;
otherwise record a durable external-storage identifier and checksum in the
manifest. Update this index when the package contract changes.
