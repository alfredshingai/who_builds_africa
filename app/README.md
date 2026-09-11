# App - WHO BUILDS AFRICA? (Phase 3 MVP - scaffold)

Static site: Astro + Svelte + MapLibre GL JS + OpenStreetMap. Reads built artifacts from `data/releases/`.

## Phase plan

- **Phase 3:** interactive Africa map → project markers (sized by `location_precision`) + filters (country/foreign origin/sector/role/status/year) + project page (timeline + sources + evidence labels). No backend - `fetch('../data/releases/v0.1.0-synthetic/data.json')` static. Deployed on **Vercel** via `vercel.json:1` (static, `cleanUrls`, rewrites `/` → `/app/index.html`).
- **Later:** optional read-only API (`Datasette`/`FastAPI` + `PostGIS`) consuming same CSVs - no schema break.

## FOSS only

MapLibre BSD-3, OSM tiles ODbL (attribution `© OpenStreetMap contributors` always visible). No Mapbox/paid tiles required; self-host OpenMapTiles if needed.

## Local dev (when implemented)

```bash
# static - no build required (app/index.html is pure HTML + MapLibre CDN)
python3 -m http.server 8000  # then open http://localhost:8000/app/index.html
# or Vercel: vercel --prod (framework: Other, output: ./, install: none)
```

Current status: scaffold placeholder - Phase 1 data is source of truth.
