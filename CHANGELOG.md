# Changelog

All notable changes - follow Keep a Changelog + SemVer for schema, CalVer for data releases.

## [Unreleased]

## [v0.1.0] - 2026-09-11
### Added
- Phase 0+1 foundation: MIT/ODbL-1.0/CC BY 4.0 split, GOVERNANCE.md, CONTRIBUTING.md, DATA_METHODOLOGY.md, DATA_DICTIONARY.md, SOURCING_GUIDE.md, vocabularies.yaml, JSON Schema, 14-table normalized model with EDTF dates, location_precision, evidence_strength, stable wba_* IDs
- Validation: scripts/validate.py (ISO codes, EDTF, Africa bbox, enums, value without currency, duplicate detection) + scripts/build.py (CSV → GeoJSON/SQLite/JSON extracts)
- Samples: 5 synthetic projects (ZWE/KEN/ETH) demonstrating corridor/exact/country precision, disputed claims, undisclosed values
- App MVP: MapLibre GL JS 4.7 + OSM raster (ODbL), static pure HTML (no build), Vercel deploy (vercel.json), filters (country/sector/role/status/origin/precision/search), table view, project detail (timeline/contracts/roles/evidence cards with verbatim_quote+archive_url), data downloads (CSV/JSON/GeoJSON/SQLite)
- Fixes: window.status/origin collision, root 404 → index.html, Vercel framework null static, absolute /data paths
### Data
- 9 real source-tracked projects: ZWE Hwange 7&8 + Kariba South + RGM Airport; KEN Nairobi Expressway + SGR + Lake Turkana Wind; ETH Addis LRT + Ethio-Djibouti Railway + GERD
- 21 organizations (Sinohydro/PowerChina/Exim/CJI/CRBC/CCCC/Vestas/CREC/CCECC/Webuild + state agencies), 9 contracts, 20 participations, 7 financing_records, 15 sources (Xinhua/Chronicle/Airport Technology/CRBC/Reuters/Vestas/ERC/Railway Gazette/Webuild/ENR), 14 claims, 12 events, 14 dates
- Releases: data/releases/v0.1.0 (9 features, SQLite, GeoJSON, data.json) + v0.1.0-synthetic (5 features)
### Changed
- Deploy: GitHub Pages → Vercel (static, no Python entrypoint), docs/index.html mirrored
- Governance: initial focus ZWE/KEN/ETH, neutral language, uncertainty preserved

## [0.1.0] - 2026-09-11 (placeholder)
- Initial empty repository
