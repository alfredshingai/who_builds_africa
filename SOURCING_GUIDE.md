# Sourcing Guide

## What counts as a source

Governed sources: government contracts, procurement notices, tender docs, ministry/agency docs, company reports/announcements, development bank / export-credit records, parliamentary/court docs (legally accessible), academic/research reports, reputable journalism, trade publications, public datasets, satellite/geospatial, archived pages. All require `url` or `doc_id` + `publisher`.

## Capture

For each source, record: `title`, `publisher`, `authors`, `source_type`, `pub_date`, `access_date`, `url`, `archive_url` (Wayback where legally allowed), `lang`, `page/section/table`, `verbatim_quote`, `claim_text`, `classification` (primary/secondary/tertiary), `accessibility`, `paywall`, `reliability_notes`, `license`.

## Usability Check

- Legally reusable? Link + quote only if copyrighted; no full PDFs unless open.
- Paywalled/offline? Mark `accessibility`, try archive, note limits.
- Language? Preserve original + translation review (no auto-translate assumed correct).

## Extraction Rules

- Quote exactly- never invent. Record `claim_text` = normalized sentence supported.
- One source can support many claims; one claim can have many sources.
- Mark `evidence_strength` per claim; `uncorroborated` until 2nd independent source.

## Shortcomings to flag

Broken hyperinflation-era conversions, implausible values, duplicate reporting - null with note, don't silently fix.

## Workflow

Discover → capture source → assess usability → extract claims → identify project/contract/org → normalize names → record dates with precision → assess strength → geo-tag → submit for review → validated → publish → schedule re-verification.
