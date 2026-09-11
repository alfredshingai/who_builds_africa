# WHO BUILDS AFRICA?

**Powered by the Africa Contract Footprints database**

> An open-source, source-tracked map and database documenting foreign participation in African infrastructure and development across time.

[![License: MIT](https://img.shields.io/badge/Code-MIT-green.svg)](LICENSE)
[![License: ODbL](https://img.shields.io/badge/Data-ODbL--1.0-blue.svg)](LICENSE-DATA)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](LICENSE-DOCS)

**Initial focus:** Zimbabwe, Kenya, Ethiopia (expands to all African countries)

---

### What "builds" means

Neutral and evidence-led. A participation record may be:

financing · designing · constructing · engineering · supplying equipment · consulting · developing · operating · maintaining · managing · joint venture / consortium

We never imply a company built an entire project if evidence only shows financing, supply, or subcontracting. Every role is explicitly labelled.

### The product is the database

The map is the exploration interface; the real product is the structured, historically inclusive, source-tracked, versioned, auditable database behind it.

- **Historically inclusive:** any accessible period, including pre-2000, archived/scanned/non-English sources
- **Uncertainty preserved:** missing/unknown/approx dates, conflicting claims, and location precision are explicit — never invented
- **Evidence > narrative:** every material claim links to source + verbatim passage + evidence strength

### Explore (MVP)

- Interactive map of Africa → country → project markers (sized/shaped by precision)
- Filters: country, foreign origin, sector, role, status, year/range
- Project pages: timeline, organizations & roles, contract values, sources with evidence labels
- Downloads: CSV / JSON / GeoJSON / GeoPackage / SQLite — versioned releases

Live site: *Vercel* — `https://who-builds-africa.vercel.app` (or your Vercel URL) serves `app/index.html` as `/` via `vercel.json:1` rewrites; `data/releases/` is static. See `app/` for local dev.

### Repository Structure

```
schema/          JSON Schema + vocabularies + ER diagram
data/curated/    validated CSVs (source of truth, PR-reviewed)
data/releases/   versioned exports (GeoJSON, GPKG, SQLite)
samples/         synthetic sample records (clearly labelled SYNTHETIC)
scripts/         validate.py, build.py (pydantic + Frictionless)
app/             static site (Astro + Svelte + MapLibre GL JS + OSM)
docs/            methodology, dictionary, sourcing guide (MkDocs)
```

### Quick Start (local)

```bash
git clone https://github.com/alfredshingai/who_builds_africa.git
cd who_builds_africa
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt  # pydantic, frictionless, etc.

# validate curated data
python scripts/validate.py --all

# build release artifacts from curated CSVs
python scripts/build.py --out data/releases/v0.1.0

# run static site (after Phase 3)
cd app && npm install && npm run dev
```

### Licenses

- **Code** → MIT (`LICENSE`)
- **Database** → ODbL-1.0 (`LICENSE-DATA`) — attribution + share-alike
- **Docs** → CC BY 4.0 (`LICENSE-DOCS`)
- **Source quotes** → remain © publishers (short quotations for evidence)
- **Map** → © OpenStreetMap contributors, ODbL — see `NOTICE.md`

### Attribution

When you use the data, cite: `Africa Contract Footprints / WHO BUILDS AFRICA? (https://github.com/alfredshingai/who_builds_africa), ODbL-1.0, Release vX.Y.Z`

See `CITATION.cff` and `data/releases/*/CITATION.md`.

### Contributing

Read `CONTRIBUTING.md`, `DATA_METHODOLOGY.md`, `SOURCING_GUIDE.md`, `REVIEW_POLICY.md`. All public submissions are PR-reviewed before publication. Corrections: see `CORRECTIONS.md`.

### Governance

See `GOVERNANCE.md` — maintainer: @alfredshingai, open to co-maintainers, transparent review, no paid gate.

---

Built with free and open-source tools only. No proprietary map/API required.
