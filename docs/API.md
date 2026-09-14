# API & Data Access - Africa Contract Footprints

All data is static, versioned, and FOSS. No auth, no paid gate. Fetch directly from `https://who-builds-africa.vercel.app` or GitHub raw.

## Releases

- **Current:** `data/releases/v0.8.0/` - 200 projects (55 countries), 237 orgs, 198 contracts, 249 participations, 370 sources, 355 claims
- **Previous:** `data/releases/v0.7.1/` (150), `v0.7.0/` (150), `v0.6.0/` (100 - all 54 countries), `v0.5.0/` (75) - all preserved
- **Demo synthetic:** `data/releases/v0.1.0-synthetic/` - 5 synthetic projects (schema demo)
- **Source of truth:** `data/curated/*.csv` - PR-reviewed, `validate.py` enforced

## Files per release

```
data/releases/v0.8.0/
  data.json              # all tables in one JSON (for app)
  projects.json, organizations.json, contracts.json, participation_records.json,
  financing_records.json, sources.json, claims.json, events.json, dates.json, project_locations.json
  projects.geojson       # Point + LineString (corridor), precision in properties
  projects.csv, organizations.csv, ... (CSV mirrors)
  footprints.sqlite      # SQLite with projects table + all CSVs as tables
  CITATION.md
```

## Stable IDs

`wba_prj_*`, `wba_org_*`, `wba_ctr_*`, `wba_par_*`, `wba_src_*`, `wba_clm_*`, `wba_evt_*`, `wba_date_*` - never reused, ULID-based. Use for citations.

## Examples

```bash
# All projects
curl https://who-builds-africa.vercel.app/data/releases/v0.8.0/projects.json

# GeoJSON for map
curl https://who-builds-africa.vercel.app/data/releases/v0.8.0/projects.geojson

# One project + its participations
curl https://who-builds-africa.vercel.app/data/releases/v0.8.0/data.json | jq '.projects[] | select(.id=="wba_prj_01HREAL001")'

# Organizations active in >1 country
curl https://who-builds-africa.vercel.app/data/releases/v0.8.0/participation_records.json | jq

# CSV download
curl -O https://who-builds-africa.vercel.app/data/releases/v0.8.0/claims.csv
```

## Pagination, rate limit, caching

No server - CDN cached (`Cache-Control: public, max-age=3600, stale-while-revalidate=86400` via `vercel.json`). Client loads all 200 rows at once (894KB data.json). For future >1k rows, add `?limit=&offset=` in API layer (planned `Datasette`/`PostgREST`).

## Licenses

- Data: ODbL-1.0 (`LICENSE-DATA`) - attribution + share-alike
- Code: MIT (`LICENSE`)
- Docs: CC BY 4.0 (`LICENSE-DOCS`)

Cite: `Africa Contract Footprints / WHO BUILDS AFRICA? v0.8.0, ODbL-1.0, https://github.com/alfredshingai/who_builds_africa`
