# App — WHO BUILDS AFRICA? (Phase 3 MVP — scaffold)

Static site: Astro + Svelte + MapLibre GL JS + OpenStreetMap. Reads built artifacts from `data/releases/`.

## Phase plan

- **Phase 3:** interactive Africa map (Natural Earth boundaries) → country click → project markers (sized by `location_precision`) + filters (country/foreign origin/sector/role/status/year) + project page (timeline + sources + evidence labels). No backend — `fetch('/data/projects.geojson')` via GitHub Pages.
- **Later:** optional read-only API (`Datasette`/`FastAPI` + `PostGIS`) consuming same CSVs — no schema break.

## FOSS only

MapLibre BSD-3, OSM tiles ODbL (attribution `© OpenStreetMap contributors` always visible). No Mapbox/paid tiles required; self-host OpenMapTiles if needed.

## Local dev (when implemented)

```bash
cd app
npm install
npm run dev # http://localhost:4321
npm run build # -> dist/ copied to docs/ for GitHub Pages or served separately
```

Current status: scaffold placeholder — Phase 1 data is source of truth.
