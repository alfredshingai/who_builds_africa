# Changelog

All notable changes - follow Keep a Changelog + SemVer for schema, CalVer for data releases.

## [Unreleased]

## [v0.2.0] - 2026-09-11
### Added
- Data: expand to 15 real projects - added ZWE New Parliament (Shanghai Construction, RMB675.8m grant, 2023), Victoria Falls Airport ($150m Exim, 2016), KEN KAIST at Konza ($94.7m Korea Eximbank, 2019), Lamu Port Berths 1-3 (CCCC $484m, 2021), ETH Hawassa Industrial Park (CCECC $246m, 2016), BWA/ZMB Kazungula Bridge (Daewoo $161m, 2021 cross-border) - 5 countries, 31 orgs, 15 contracts, 23 sources
- App: country filter now dynamic (populated from DATA.projects), banner 15 REAL PROJECTS, Quality header with Last verified + changelog link
- Contributor: structured issue forms (data-submission.yml / correction.yml), scripts/new_project.py helper, data/templates/ CSV headers
- UI: flex layout fix (no blank whitespace, 100dvh, map resize), remove all em dashes (185)
- Releases: v0.2.0 snapshot (15 features) + v0.1.0-synthetic preserved, CITATION v0.2.0

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
