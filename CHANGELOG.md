# Changelog

All notable changes - follow Keep a Changelog + SemVer for schema, CalVer for data releases.

## [Unreleased]

## [v0.4.0] - 2026-09-11
### Added
- Data: expand to 50 real projects (+20) - added ZWE Tokwe-Mukosi (Webuild, 2016), NetOne Broadband ($71m Huawei, 2019), KEN Olkaria Geothermal (JICA, 2015), Outer Ring Road (China Wu Yi, AfDB, 2015), ETH Genale Dawa III 254MW (CGGC, $326m, 2020), ZMB KKIA $360m (CJIC, 2021), TZA SGR Lots 3-4 $1.9bn (Yapi Merkezi, 2021), MOZ Nacala Corridor 912km (Vale/Mitsui, 2017), GHA Tema Port T3 3M TEU (AECOM/CHEC/IFC, 2019), AGO Caculo Cabaca 2172MW (CGGC, $4.5bn, 2026), MAR Noor 580MW (ACWA/MASEN, 2016), NAM Walvis Bay 750k TEU (CHEC, $260m, 2019), CMR Kribi 615+715m (CHEC, 2018/2025), ZAF Gautrain 80km (Bouygues/Bombardier, 2012), COD Busanga 240MW (PowerChina, 2023), EGY New Capital CBD $3bn (CSCEC, 2022), SEN AIBD Dakar (Limak/Summa, 2017), RWA BK Arena $104m (Summa, 2019), UGA Karuma 600MW (Sinohydro, $1.7bn, 2024), BFA Zagtouli 33MW (Cegelec, 2017) - 20 countries, 91 orgs, 48 contracts, 69 sources
- App: banner 50 REAL PROJECTS, dynamic country 20, Quality updated
- Releases: v0.4.0 snapshot (50 features, 230KB) - v0.3.0 (30) + v0.2.0 (15) + v0.1.0 (9) preserved

## [v0.3.0] - 2026-09-11
### Added
- Data: expand to 30 real projects - added ZWE Beitbridge Border ($300m Raubex, 2022), TelOne Broadband ($98.6m Huawei, 2017), KEN Thwake Dam (CGGC, AfDB $370m, 2017), Mombasa Port Berths 20-21 (Toyo/JICA, 2016/2022), ETH Adama Wind 204MW (CGCOC/HydroChina, $392m, 2015), Bole Airport (CCCC, 2015), ZMB Kafue Gorge Lower 750MW (Sinohydro, $2bn, 2021), TZA Nyerere 2115MW (Arab Contractors/Elsewedy, $2.9bn, 2024), MOZ Maputo Bridge 3,041m (CRBC, $785m, 2018), RWA Bugesera Airport ($818m Mota-Engil PPP), SEN Dakar TER 55km (Eiffage 370m euros, 2021), GHA Bui 400MW (Sinohydro, $790m, 2013), AGO Lauca 2070MW (Odebrecht, $4.3bn, 2017), UGA Kampala-Entebbe 51km (CCCC $476m, 2018), MWI Fibre Backbone 4000km (Huawei $121.8m, 2018) - 13 countries, 57 orgs, 30 contracts, 43 sources
- App: banner 30 REAL PROJECTS, dynamic country filter now 13, Quality view updated
- Releases: v0.3.0 snapshot (30 features) - v0.2.0 (15) and v0.1.0 (9) preserved

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
