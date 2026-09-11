# Data Methodology - Africa Contract Footprints

## Mission

Living, source-tracked historical database of foreign participation in African infrastructure. Neutral, evidence-led - `The source reports...` not `X built Y`.

## Definitions

- **Foreign:** explicit per-organization: `incorporation`, `headquarters`, `parent`, `ultimate_owner`, `financing`, `soe_origin` - never collapsed to one field. A record is foreign if any of those countries ≠ project country, with source.
- **Builds:** financing, designing, constructing, engineering, supplying, consulting, developing, operating, maintaining, managing, JV/consortium - role enum in `participation_records.role`.
- **Project ≠ Contract ≠ Participation ≠ Financing:** one project has many contracts/participants/funders/phases/locations/events.

## Scope

- Countries: initially Zimbabwe, Kenya, Ethiopia - expands to all Africa. Uses ISO 3166-1 alpha-3.
- Sectors: controlled vocab in `schema/vocabularies.yaml` (roads, rail, ports, airports, dams, water, hydropower, solar, wind, transmission, mining infra, telecoms, housing, hospitals, schools, etc.) - propose new via Issue.
- Time: any period inclusive, with `edtf` + `precision` (day/month/year/approx/range/before/after/unknown). Historical events stored, not overwritten.

## Inclusion Rule

Accessible contract or documented participation with ≥1 source supporting a specific claim. No invented values.

## Date Model

Uses `dates` table with `edtf_string`, `precision`, `earliest`, `latest`, `display_string`. Supports: `2018-03-12`, `2018-03`, `2018`, `~2018`, `2017/2019`, `before 2005`, `unknown`. Never coerce `unknown` to a year. Separate fields for announcement, tender, award, sign, financial-close, start, expected-complete, actual-complete, suspension, cancellation, etc. as `events`.

## Geographic Model

`location_precision` enum: `exact`, `approximate`, `city`, `district`, `province`, `country`, `cross_border`, `corridor`, `unknown`. Map symbology reflects this - hollow centroid for country-only, clustered markers, lines for corridors (rail/road/pipeline), polygons for sites. No fake coordinates.

## Evidence

Claim-centric: each `claims` row links `source` → `verbatim_quote` + `claim_text` (e.g., "Ministry of Transport awarded Company X construction contract for Project Y in 2014"). Strength: `confirmed`, `corroborated`, `officially_reported`, `credibly_reported`, `probable`, `unclear`, `disputed`, `unverified`, `corrected`, `archived`. Corroboration status explicit.

## Roles & Values

`participation_records.role` enum enforced. Contract `value` separated from `estimated project cost` / `loan` / `grant` / `equity` - never conflate. `value_precision`: `exact`, `approx`, `range`, `undisclosed`.

## Versioning & Provenance

Stable IDs `wba_prj_*`, `wba_org_*`, etc. (ULID). Changes tracked in `change_history.csv` + git. Releases: `data/releases/vYYYY.MM.DD/` + tag + Zenodo DOI (planned). Stable IDs never reused; merges preserve `old→new` in `project_merges.csv`.

## Limitations (must display on site)

Reporting bias, language bias, survivorship, missing disclosures - warn against causal claims from counts alone.

## MVP Focus (v0.1)

30-50 source-tracked records across 3 countries, multiple sectors/foreign origins/historical periods, all validated via `scripts/validate.py`.
