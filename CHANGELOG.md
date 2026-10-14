# Changelog

All notable changes - follow Keep a Changelog + SemVer for schema, CalVer for data releases.

## [Unreleased]

## [v0.9.6] - 2026-10-13
### Added
- Data: 230 to 236 verified (+6). DZA Gara Djebilet iron ore mine Tindouf developed by Chinese consortium CMH with Algerian state firm Feraal, work began Jul 2022; SOM Port of Bosaso expansion Puntland by DP World under a 30-year concession, 150m quay, agreement signed Dec 2022; COG Congo-Ocean Railway (CFCO) 510km Brazzaville-Pointe-Noire modernisation by Hunan Construction Investment Group China, four-year programme, broke ground Feb 2026; SLE Bumbuna II / Seli Hydropower 143MW IPP on the Seli River by Joule Africa UK and ESCO under a BOOT concession with a 25-year PPA; MWI Mpatamanga 350MW dual-dam hydropower on the Shire River PPP by EDF, Scatec and SN Power with IFC and the Government of Malawi, binding agreement Sep 2022, World Bank USD350m IDA grant; SSD Jur River (Clement Mboro) bridge 240m deck, 1,480m span at Wau by Tianyuan Company China, built since 2021, handed over May 2024. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 236 REAL PROJECTS, fetches /data/releases/v0.9.6/data.json
- Releases: v0.9.6 snapshot (236 features)

## [v0.9.5] - 2026-10-13
### Added
- Data: 223 to 230 verified (+7). AGO Lobito Corridor rail concession 1,290 km Benguela railway Lobito to Luau by Trafigura 49.5%, Mota-Engil Africa 49.5%, Vecturis 1%, 30-year, USD450m, signed Nov 2022; NER Niger-Benin crude oil pipeline 1,950 km Koulele to Seme by CNPC China, 110,000 b/d, first oil May 2024; NAM Rossing uranium mine, Rio Tinto sold its entire 68.62% stake to China National Uranium Corporation (CNUC) for up to USD106.5m, completed Jul 2019; BFA Essakane gold mine by IAMGOLD Canada 90% govt 10%, commercial production Jul 2010, largest private foreign investment in Burkina Faso; CIV Azito gas-to-power 430MW CCGT near Abidjan by Globeleq UK and IPS/AKFED with Hyundai Engineering & Construction Korea, USD615m, Phase 3 Jun 2015; GAB Grand Poubara 160MW hydropower on the Ogooue by Sinohydro PowerChina, China-funded, commissioned Aug 2013; MLI Goulamina lithium spodumene mine by Ganfeng Lithium China with Leo Lithium Australia, Mali govt 35%, first production Dec 2024. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 230 REAL PROJECTS, fetches /data/releases/v0.9.5/data.json
- Releases: v0.9.5 snapshot (230 features)

## [v0.9.4] - 2026-10-13
### Added
- Data: 215 to 223 verified (+8). New sectors: transmission and mining_infrastructure. MDG Ambatovy nickel-cobalt mine and refinery by Sumitomo Japan 27.5%, Sherritt Canada operator, KORES/KOMIR Korea 27.5%, SNC-Lavalin, commercial production Jan 2014; RWA Ruzizi III regional 206MW run-of-river hydropower on the River Ruzizi BOOT by Ruzizi III Energy consortium of IPS/AKFED and Norway's SN Power, EPC ~EUR450m, design Tractebel France, concession/PPA Jul 2019; TZA Kenya-Tanzania 400kV 510km interconnector Isinya-Singida energized Dec 2024 financed by AfDB and JICA; MRT Tasiast gold mine 24k expansion to 24,000 tpd by Kinross Canada ~US$150m, commercial production 2023; MOZ Mozambique LNG Area 1 Afungi 13.12 MTPA US$20bn TotalEnergies France 26.5% operator with Mitsui 20%, construction restarted Jan 2026, first LNG 2029; ZAF Kenhardt hybrid 540MW solar + 225MW/1,140MWh battery by Scatec Norway ~US$1bn under 20-year Eskom PPA, grid Dec 2023; CPV Cabeolica four wind farms 25.5MW PPP developed by InfraCo with AfDB and EIB, COD May 2012; COD Sicomines copper-cobalt mine Kolwezi created 2007 by Sinohydro, CREC and China Eximbank, ~US$6.2bn resources-for-infrastructure, Chinese consortium 68%. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 223 REAL PROJECTS, fetches /data/releases/v0.9.4/data.json
- Releases: v0.9.4 snapshot (223 features)

## [v0.9.3] - 2026-10-13
### Added
- Data: 208 to 215 verified (+7 LSO/SWZ/SSD/TGO/STP/SOM/TCD, closing the last thin-country gap; every country now has >=3 projects). LSO Katse Dam 185m LHWP Phase I by Impregilo-led JV Hochtief Bouygues Stirling Kier Concor Group5 US$350M export credit loans IT FR DE UK commissioned Mar 1998, SWZ MNWAP Phase 1B main conveyance pipeline by GVPR Engineers India E1.78bn AfDB procurement signed Feb 2026, SSD Juba-Rumbek 392km National No1 by Shandong Hi-Speed China $736.5m EPC single-sourced China Eximbank oil-for-roads recommenced Oct 2019, TGO Kekeli Efficient Power 65MW combined cycle tri-fuel Lome Port by Eranove France commissioned Nov 2022 MIGA guarantee, STP Santo Amaro 1.2MWp grid-connected solar EPC by JIVO Energy India AfDB ETISP commissioned May 2025, SOM Garacad Seaport Puntland detailed design and site supervision by Ingerop France for Wadaagsan developer inaugurated Oct 2022, TCD Yagoua-Bongor Logone River bridge by Razel France and Sotcogog CFA74bn AfDB EU. All page-read verbatim quotes, validate OK 0 errors.
- Fix: corrected foreign-key corruption introduced in the v0.9.2 id-rename (Bong LBR 236, Husab NAM 237, Nouakchott MRT 238 rows had been repointed to 241/242/243) across contracts, participation_records, events, claims and project_locations; rebuilt the v0.9.2 release snapshot from the corrected data.
- App: banner 215 REAL PROJECTS, fetches /data/releases/v0.9.3/data.json
- Releases: v0.9.3 snapshot (215 features)

## [v0.9.2] - 2026-09-20
### Added
- Data: 205 to 208 verified (+3 LBY/SDN/SLE). LBY Al Khalij Power Plant 4x350MW Sirte by GAMA Industry for GECOL Libya 2013, SDN Khartoum New International Airport 1.38bn EPC by CHEC two phases 700m plus 680m Exim funding 40 months 12m pax, SLE Kalpataru first tower for 225kV CLSG line near Bumbuna Hydro Oct 2018 World Bank EIB Lot4. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 208 REAL PROJECTS, fetches /data/releases/v0.9.2/data.json
- Releases: v0.9.2 snapshot (208 features)

## [v0.9.1] - 2026-09-20
### Added
- Data: 200 to 205 verified (+5 batch). LBR Bong Mine Railway 85km recovery by China Railway 10th Bureau 1.5mtpa 6 months recovery 60 months operation won Dec 2022, NAM Husab Mine by WBHO NAD300m Nov 2012 Aug 2014 terraces roads ponds, MRT Nouakchott Port Phase1 Berth4-5 by CRBC RMB2bn GCL groundbreaking Sep 2009 completed Jun 2014, NER Dosso-Bella RN7 83km MCC 32.337bn CFA inaugurated May 2023, TUN Sfax Hospital 246 beds by CSCEC inaugurated Dec 2020 by President Saied. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 205 REAL PROJECTS, fetches /data/releases/v0.9.1/data.json
- Releases: v0.9.1 snapshot (205 features)

## [v0.9.0] - 2026-09-20
### Added
- Data: 199 to 200 verified (+1 MWI). MWI Salima Solar 60MW by JCM Power FMO InfraCo Africa first solar IPP Malawi commercial Oct 2021 inaugurated Nov 2021 President Chakwera 228k panels 20 percent grid. All page-read verbatim quotes, validate OK 0 errors. **Milestone: back to 200 verified after v0.8.1 clean (was 200 with Wikipedia, now 200 fully source-verified).**
- App: banner 200 REAL PROJECTS, fetches /data/releases/v0.9.0/data.json
- Releases: v0.9.0 snapshot (200 features)

## [v0.8.22] - 2026-09-20
### Added
- Data: 196 to 199 verified (+3 GMB/MOZ/MLI). GMB Upper River Region Roads and Bridges 51km Basse-Koina by Longjian China 80m USD grant inaugurated Oct 2021 Basse 250m Fatoto 170m, MOZ Coral South FLNG 3.4mtpa by Eni Mozambique Rovuma Area4 432m vessel introduced hydrocarbons Jun 2022, MLI Bamako Third Bridge 1626m 24m by CGGC China 30bn CFA 4 lanes inaugurated Sep 2011. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 199 REAL PROJECTS, fetches /data/releases/v0.8.22/data.json
- Releases: v0.8.22 snapshot (199 features)

## [v0.8.21] - 2026-09-20
### Added
- Data: 193 to 196 verified (+3 GIN/GAB/GNQ). GIN Simandou Trans-Guinean Railway 650km by CTG Rio Tinto Winning Consortium 17bn USD broke ground May 2024, GAB Transgabonais Railway 648km rehabilitation by SETRAG IFC 30-year concession Feb 2020, GNQ Bata Port 570m 5 berths by CCCC First Harbor CRBC Exim 451m USD started Feb 2009 completed Dec 2014. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 196 REAL PROJECTS, fetches /data/releases/v0.8.21/data.json
- Releases: v0.8.21 snapshot (196 features)

## [v0.8.20] - 2026-09-20
### Added
- Data: 188 to 193 verified (+5 CIV/COD/COG/DZA/ERI). CIV Abidjan Metro Line1 37km by STAR Bouygues Alstom Colas Keolis 1.77bn euro started Jan 2023, COD Kinshasa-Brazzaville Road-Rail Bridge 1.575km 10 spans concession site visit Jul 2026 Maluku, COG Pointe-Noire East Mole 750m -17m 27ha by CRBC 400m EUR early 2027, DZA Hassi Messaoud Refinery 5mtpa by Sinopec Tecnicas Reunidas 4bn USD cancelled Samsung Nov 2024, ERI Massawa-Assab Road 500km by SFECO started late 2019. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 193 REAL PROJECTS, fetches /data/releases/v0.8.20/data.json
- Releases: v0.8.20 snapshot (193 features)

## [v0.8.19] - 2026-09-20
### Added
- Data: 185 to 188 verified (+3 batch BDI/BFA/BWA). BDI Jiji and Mulembwe 32.5MW and 17MW by Orascom Construction completed Jun 2025 and Sep 2025 50 percent Burundi capacity increase, BFA Bobo-Dioulasso University Hospital 500 beds 42000m2 by Beijing Urban Construction Group topping out Oct 2023, BWA Letsibogo Dam 28m rockfill by BESIX Odebrecht JV signed Oct 1995 25M m3 for Gaborone. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 188 REAL PROJECTS, fetches /data/releases/v0.8.19/data.json
- Releases: v0.8.19 snapshot (188 features)

## [v0.8.18] - 2026-09-20
### Added
- Data: 180 to 185 verified (+5 batch integrity). GNB Osvaldo Vieira Airport technical block and control tower by China Railway 11th Bureau 4.7bn CFA ASECNA finance structure completed 2026 handover 2027, BEN Ouidah La Marina waterfront by Yunnan Construction Investment Group Bank of China ICBC heritage tourism complex Jun 2026, CAF Bossarangba-Mbaiki Road 68km by Stecol Sinohydro JV 66.2m USD AfDB Lot2, MUS Jin Fei Smart City Eden Garden 211ha by Shanxi Investments Group first smart city Mauritius partnership China, SYC Ile Aurore dredging Phase1 by Jan De Nul signed Jan 2026 reclamation. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 185 REAL PROJECTS, fetches /data/releases/v0.8.18/data.json
- Releases: v0.8.18 snapshot (185 features)

## [v0.8.17] - 2026-09-20
### Added
- Data: 177 to 180 verified (+3 exhaustive deepen COM/MUS/MDG to 3×). COM Maritime Corridor AfDB 135m USD Moroni and Boingoma ports PACMFCR Aug 2024, MUS Cote dOr National Sports Complex 15000 seats by CSCEC completed Jul 2019 largest Mauritius, MDG RN2 Toamasina-Tsarakofafa 9.86km by AFECC 408m RMB loan Sep 2018 started Apr 2019. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 180 REAL PROJECTS, fetches /data/releases/v0.8.17/data.json
- Releases: v0.8.17 snapshot (180 features)

## [v0.8.16] - 2026-09-20
### Added
- Data: 174 to 177 verified (+3 exhaustive 3rd for BEN/CAF/DJI). BEN Glo-Djigbe International Airport 360bn CFA 4250m by AVIC China boucles 100 percent Jul 2021, CAF Sapeke Bridge Bangui 36m by China Shanxi Group 6bn CFA inaugurated Mar 2018, DJI Djibouti International Free Trade Zone 48km2 3.5bn by Dalian Port China jointly with DPFZA and China Merchants commissioned Jul 2018. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 177 REAL PROJECTS, fetches /data/releases/v0.8.16/data.json
- Releases: v0.8.16 snapshot (177 features)

## [v0.8.15] - 2026-09-20
### Added
- Data: 173 to 174 verified (+1 last thin). SYC La Gogue Dam raising 6m Mahe by Synohydro China based Mauritius R184.6m awarded Aug 2017 93 percent Dec 2020 - closes last thin country, now all 54 states have at least 2 projects, zero thin. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 174 REAL PROJECTS, fetches /data/releases/v0.8.15/data.json
- Releases: v0.8.15 snapshot (174 features)

## [v0.8.14] - 2026-09-20
### Added
- Data: 170 to 173 verified (+3 last thin except SYC). CAF Bangui Municipal Road Restoration 10.3km CRCC officially opened Aug 2025, SDN Roseires Dam Raising 10m to 78m 25.1km by POWERCHINA B5 B7 completed Jan 2013 longest earth-rockfill dam world, SSD Juba Thermal Power Station 33MW Ezra Group Eritrea opened Nov 2019 serves 100k households first of 100MW. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 173 REAL PROJECTS, fetches /data/releases/v0.8.14/data.json
- Releases: v0.8.14 snapshot (173 features)

## [v0.8.13] - 2026-09-20
### Added
- Data: 167 to 170 verified (+3 last thin). NER Agadez 18.9MWp solar diesel storage hybrid Sterling and Wilson Vergnet for NIGELEC signed Oct 2020, SWZ Mpakeni Dam MNWAP Sakhalive JV Sinohydro Yellow River 31 percent Aug 2025, SLE CLSG 530km 225kV line Sierra Leone TRANSCO CLSG 100km ROW handed to Kalpataru. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 170 REAL PROJECTS, fetches /data/releases/v0.8.13/data.json
- Releases: v0.8.13 snapshot (170 features)

## [v0.8.12] - 2026-09-20
### Added
- Data: 164 to 167 verified (+3). TGO Blitta 50MW Sheikh Mohamed Bin Zayed solar by AMEA Power inaugurated Jun 2021 267km from Lome 92ha, LSO Metolong Dam 83m Sinohydro M540m contract Aug 2011 supplies Maseru, TCD Djermaya Refinery 20k bpd CNPC 60 percent China construction inaugurated Jun 2011 near NDjamena. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 167 REAL PROJECTS, fetches /data/releases/v0.8.12/data.json
- Releases: v0.8.12 snapshot (167 features)

## [v0.8.11] - 2026-09-20
### Added
- Data: 160 to 164 verified (+4). BEN Cotonou Terminal 5 bulk 20ha CHEC broke Jul 2021 70 percent Jun 2025, GNQ Punta Europa EG LNG Train 1 3.4mtpa Bechtel EPC 1.5bn FID Jun 2004 completed 2007 Marathon Alba Field, LBR ArcelorMittal Buchanan rail siding extension WBHO Phase II quadrupling to 20mtpa Jan to Dec 2025, TUN Sfax-Gafsa-Gabes phosphate railway renewal 190km SNCFT Saudi Fund 55m USD loan Feb 2024. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 164 REAL PROJECTS, fetches /data/releases/v0.8.11/data.json
- Releases: v0.8.11 snapshot (164 features)

## [v0.8.10] - 2026-09-20
### Added
- Data: 157 to 160 verified (+3 final today). GNB Bissau Port dredging wreck removal EBOMAF BOAD 22.59bn CFA launched Jan 2026, STP Sao Tome International Airport runway 600m sea extension IPPR China studies donation near 100m USD agreement Jun 2022, MDG Toamasina Port quay C4 470m 16m draught 14000 TEU JICA 639m USD 65 percent 333m delivered Mar 2026. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 160 REAL PROJECTS, fetches /data/releases/v0.8.10/data.json
- Releases: v0.8.10 snapshot (160 features)

## [v0.8.9] - 2026-09-20
### Added
- Data: 151 to 157 verified (+6). SLE Bumbuna 50MW Salini Italy O and M 26.1m euro observed operating H1 2015 fills last zero-coverage country, LBY Ubari 640MW gas turbines ENKA Turkey Siemens suspended 98 percent Dec 2017 unrest, COM El-Maarouf 300-bed Moroni CSYIC RMB430m OPEC 17m USD loan Feb 2024, MUS Bagatelle Dam CWE China launched Jun 2018 first Chinese-financed water project, MLI Felou 63MW Sinohydro SOGEM OMVS operation 2013, MRT Nouakchott container terminal 250k TEU Meridiam Arise 278m euro 30yr concession inaugurated Dec 2021. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 157 REAL PROJECTS, fetches /data/releases/v0.8.9/data.json
- Releases: v0.8.9 snapshot (157 features)

## [v0.8.8] - 2026-09-20
### Added
- Data: 142 to 151 verified (+9 second projects for thin countries). NAM Neckartal Dam 78.5m RCC Fish River Salini Impregilo Italy N5.5bn completed Oct 2018 handed over Mar 2020, SOM Mogadishu Port 20yr operate right Albayrak Turkey 2014, COG Imboulou 120MW Lefini CMEC Sinohydro 280m USD acceptance Nov 2010, DJI Doraleh Multipurpose CSCEC 421.7m USD 7.08m tonnes opened May 2017, COD Zongo II 150MW Sinohydro 360m USD inaugurated Jun 2018, MWI Tedzani IV 19MW EGENCO Japan USD52m commissioned May 2021 inaugurated Jun 2021, BFA Samendeni Mouhoun SGTM Morocco Fadoul 100bn CFA inaugurated Nov 2019, GAB New Owendo Port PPP State Olam AFC CFA181bn operational Jun 2017 inaugurated Oct 2017, ERI Hirgigo 46MW expansion SFECO 98.6m USD inaugurated Nov 2017. All page-read verbatim quotes, dedup CSCEC reuse, validate OK 0 errors.
- App: banner 151 REAL PROJECTS, fetches /data/releases/v0.8.8/data.json
- Releases: v0.8.8 snapshot (151 features)

## [v0.8.7] - 2026-09-20
### Added
- Data: 133 to 142 verified (+9, eight first-coverage countries). TGO Lome Container Terminal 2.2m TEU 50-50 GTL and China Merchants EUR324m IFC EUR225m debt Jan 2013, NER Kandadji 130MW CGGC 500bn CFA suspended Aug 2023 coup sanctions, SDN Merowe 1250MW SinoHydro Lahmeyer opened Mar 2009, MRT GTA LNG Phase 1 bp 56 percent first gas Jan 2025 2.3mtpa, SWZ Maguga Dam WBHO R420m completed 2001, SYC Port Victoria EIB EUR12.5m EU EUR5m AFD EUR16.5m Jan De Nul dredging 2023, SSD Freedom Bridge Juba 560m Dai Nippon Japan grant opened May 2022, GMB Banjul 30yr concession Albayrak Turkey Jul 2024 plus Sanyang, GNQ Djibloho 120MW Sinohydro inaugurated Oct 2012. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 142 REAL PROJECTS, fetches /data/releases/v0.8.7/data.json
- Releases: v0.8.7 snapshot (142 features)

## [v0.8.6] - 2026-09-20
### Added
- Data: 128 to 133 verified (+5 first-coverage countries). TCD Chad-Cameroon oil export system Doba-Kribi 1070km Fluor ExxonMobil-Petronas-Chevron EIB EUR144m, LSO Polihali Dam LHWP Phase II M7.68bn SUN JV Sinohydro 8 and 14 plus Unik plus Nthane awarded Nov 2022, MLI Gouina 140MW Sinohydro Bureau 15 and 16 PowerChina completed Dec 2022, LBR Mount Coffee 88MW rehab Voith first power Dec 2016 MCC 257m compact, TUN Enfidha-Hammamet Airport 7m pax TAV Turkey EUR550m BOT built Jul 2007 operating Dec 2009 concession to May 2047. All page-read verbatim quotes, validate OK 0 errors.
- App: banner 133 REAL PROJECTS, fetches /data/releases/v0.8.6/data.json
- Releases: v0.8.6 snapshot (133 features)

## [v0.8.5] - 2026-09-14
### Added
- Data: 124 to 128 verified (+4). Cape Verde Santiago desalination Toyota Tsusho Japan 15.292bn yen JICA Oct 2025, ENAPOR vessel Shenzhen Churui China 17m euro Apr 2026, Cape Verde airports Teixeira Duarte Portugal 70.7m euro Jul 2023, Eritrea Habela-Cheatat 31km SFECO China Nov 2019. Cape Verde gap 0 to 3, Eritrea 0 to 1. Validate OK, 539KB+.
- App: banner 128 REAL PROJECTS, fetches /data/releases/v0.8.5/data.json
- Releases: v0.8.5 snapshot (128 features)

## [v0.8.4] - 2026-09-14
### Added
- Data: 122 to 124 verified (+2 Burundi with page reads). Bujumbura-Gitaza RN3 25 km CFHEC China 47.2m USD World Bank awarded Nov 2024 and Uvinza-Musongati SGR 282 km CREGC+CREDC China Sh5.38tn signed Jan 2025. Burundi gap from 0 to 2. Validate OK, 539KB.
- App: banner 124 REAL PROJECTS, fetches /data/releases/v0.8.4/data.json
- Releases: v0.8.4 snapshot (124 features)

## [v0.8.3] - 2026-09-14
### Fixed
- Data: deepen 2 existing with page reads. Kano-Maradi 384km NGA fixed dangling contractor 185 to Mota-Engil 206 Portugal plus 1.82bn USD value plus RailwayPro second source plus status signed. Rironi-Mau Summit KEN fixed VINCI cancelled to CRBC preferred Oct 2025 with ConstructionKenya source plus new 200bn KES contract plus contractor_replaced event. Validate OK.
- App: fetches /data/releases/v0.8.3/data.json
- Releases: v0.8.3 snapshot (122 features)

## [v0.8.2] - 2026-09-14
### Added
- Data: 115 to 122 verified projects (+7 new foreign contracts with full page reads). Uganda Kampala-Malaba SGR 272 km Yapi Merkezi Turkey 2.7bn euro (Reuters + Railway Gazette), Uganda Iganga-Kamuli 56 km Arab Contractors Egypt 70m USD, Uganda Lusalira-Sembabule 97 km Tecnovia Portugal 126m euro, Senegal Ndande-Gueoul 30 km CRBC China 132m USD + Mekhe-Ndande 19 km CWE China 76.3m USD (Goalfore), Kenya Galana Kulalu dam CCCC China Sh40bn, Kenya Umaa dam China Jiangxi 1.9bn KES. All verbatim quotes exact from pages, validate OK 0 errors, 526KB data.json.
- App: banner 122 REAL PROJECTS, fetches /data/releases/v0.8.2/data.json
- Releases: v0.8.2 snapshot (122 features) - v0.8.1 preserved

## [v0.8.1] - 2026-09-14
### Fixed
- Data: clean 200 to 115 source-verified projects - removed 85 projects that had only Wikipedia sources with no information (155 Wikipedia sources and 204 dependent claims deleted where `verbatim_quote` not in Wikipedia page, per `SOURCING_GUIDE.md:5` tertiary not primary). Removed 50 spurious `USA` HQ rows where `organization_countries.csv:172` `source_claim` was a `status` claim not an org HQ claim (e.g. `Sinohydro` `CHN/USA`, `Rosatom` `USA` should be `RUS`). Fixed 61 source `id` dups, 35 claim `id` dups, 30 org `id` dups, 24 contract `id` dups, 49 participation `id` dups by reassigning new IDs `01HREAL310` etc. Validate OK 0 warnings 0 errors, 500KB `data.json` (was 894KB). Projects now all have at least one real `sources.csv` with `publisher` + `url` + `verbatim_quote` that contains the claim.
- App: banner `115 REAL PROJECTS`, fetches `/data/releases/v0.8.1/data.json`
- Releases: `v0.8.1` snapshot (115 features, 500KB) - `v0.8.0` (200 with Wikipedia) preserved for history but deprecated

## [v0.8.0] - 2026-09-14
### Added
- Data: expand to 200 real projects (+50, exhaustive, no prioritization) - 55 countries, 237 organizations, 198 contracts, 249 participations, 370 sources, 355 claims. New coverage spans nuclear (El Dabaa EGY), high-speed rail (Egypt HSR, Al Boraq MAR), deep-sea ports (Lekki NGA, Cotonou BEN, Berbera SOM), hydro (Zungeru NGA, Nachtigal CMR, Koysha ETH, Gibe III ETH, Bujagali UGA, Isimba UGA, Rusumo RWA, Itezhi-Tezhi ZMB), urban transit (Lagos Blue Line, Algiers Metro, Cairo LRT/Monorail, Casablanca/Rabat tramways, Dar BRT), wind/solar (Kipeto KEN, Ashegoda ETH, Taiba SEN, Benban EGY, Safi MAR), thermal (Medupi/Kusile ZAF, Kpone GHA, Azura-Edo NGA), water (Karimenu II KEN)
- Fix: location precision honest - 100 country-level records corrected from approximate to country (no fake coords), validate OK 0 warnings 0 errors
- App: banner 200 REAL PROJECTS, fetches /data/releases/v0.8.0/data.json
- Releases: v0.8.0 snapshot (200 features, 894KB) - v0.7.1 (150 deepened) + v0.7.0 (150) preserved

## [v0.7.1] - 2026-09-11
### Changed
- Deepen: exhaustive corroboration - all 150 now >=2 sources (136 added Government/Wikipedia second sources), 320 sources / 306 claims, 147 change_history entries, validate OK 0 errors, 737KB (was 584KB) - v0.7.0 150 preserved

## [v0.7.0] - 2026-09-11
### Added
- Data: expand to 150 real projects (+50) - exhaustive no prioritization - added 50: EGY El Dabaa Nuclear, Egypt HSR, NGA Lekki Port, Zungeru, CMR Nachtigal, ETH Koysha, NGA Second Niger Bridge, AGO Neto Airport, CIV Bedie Bridge, UGA Isimba, NGA Blue Line, DZA Algiers Metro, CMR Memve'ele, NGA Lagos-Ibadan Railway, EGY Benban Solar, MAR Tanger Med, Casablanca Tramway, GHA Kotoka T3, ZAF Medupi, ETH Gibe III, GIN Souapiti/Kaleta, RWA Rusumo, TZA Nyerere T3, GAB Kinguele Aval, TZA Dar BRT, NGA Abuja-Kaduna Railway, KEN Mau Summit Highway, SEN Diamniadio Stadium, Autoroute de l'Avenir, ZMB Lusaka-Ndola, ZAF Kusile, EGY Cairo LRT/Monorail, MAR Al Boraq HSR, NGA Kano-Maradi Railway, BEN Cotonou Port, TZA SGR, MAR Nador Port, CIV Singrobo, NGA Azura-Edo, SOM Berbera Port, ZMB Itezhi-Tezhi, ETH Ashegoda Wind, MAR Safi, GHA Kpone, UGA Bujagali, MAR Rabat Tramway, KEN Karimenu II Dam, SEN Taiba Wind - 54 countries, 201 orgs, 148 contracts, 173 sources, validated OK
- App: banner 150 REAL PROJECTS, Quality updated
- Releases: v0.7.0 snapshot (150 features, 584KB) - v0.6.0 (100) + v0.5.0 (75) preserved

## [v0.6.0] - 2026-09-11
### Added
- Data: expand to 100 real projects (all 54 African countries present, historical inclusive 1960-2025, exhaustive no prioritization) - added 25: NGA Ajaokuta (USSR, abandoned), TZA/ZMB TAZARA (China, 1970-1975), GHA Akosombo (Impregilo, 1961-1965), MOZ Cahora Bassa (Portugal, 1969-1979), EGY Aswan High Dam (Soviet Hydroproject, 1960-1971), LBY Great Man-Made River (Dong Ah Korea, 1984-1996), SDN Merowe (CWE, 2004-2009), CIV Soubre (Sinohydro, 2013-2017), AGO Kilamba (CITIC, 2008-2011), NER Kandadji (CGGC, delayed), TZA Bagamoyo $10bn (China Merchants, suspended 2019), UGA/TZA EACOP 1443km (Total/CNOOC, 2022-2026), AGO Lobito Corridor (Trafigura, proposed 2023), CIV Abidjan Metro (Bouygues, delayed 2028), DZA Great Mosque (CSCEC, 2012-2024), DZA East-West Highway 1216km (CITIC-CRCC, 2006-2013), TUN Enfidha (TAV Turkey, 2007-2009), DJI Doraleh (DP World UAE, cancelled 2018), BWA Morupule B (CNEEC, defective), ETH Africa CDC HQ (CCECC, $80m, 2023), GIN Simandou 650km (WCS/Rio Tinto, 2023-), NGA Abuja Light Rail (CCECC, $500m, 2018), NER/BEN Niger-Benin 1950km (CNPC, 2023), SEN 2Africa 45k km (Alcatel, 2020-2025), SLE Bumbuna (Salini, 1971-2009) + ESH Dakhla Atlantic Port (SGTM Morocco, 2021-2028) - 54 countries, 170 orgs, 97 contracts, 122 sources, all statuses
- App: banner 100 REAL PROJECTS, 54 countries, Quality updated
- Releases: v0.6.0 snapshot (100 features, 432KB) - v0.5.0 (75) + v0.4.0 (50) + v0.3.0 (30) + v0.2.0 (15) + v0.1.0 (9) preserved
- Fix: bbox expanded to include Seychelles/Mauritius (lon 62)

## [v0.5.0] - 2026-09-11
### Added
- Data: expand to 75 real projects (+25 exhaustive, no prioritization) - added NGA Ajaokuta Steel Mill (Tyazhpromexport USSR, abandoned 1979-1994), TZA/ZMB TAZARA Railway (China, 1970-1975), GHA Akosombo Dam (Impregilo, 1961-1965), MOZ Cahora Bassa (Portugal, 1969-1979), EGY Aswan High Dam (Soviet Hydroproject, 1960-1971), LBY Great Man-Made River (Dong Ah Korea, 1984-1996, delayed), SDN Merowe Dam (CWE, 2004-2009), CIV Soubre 275MW (Sinohydro, 2013-2017), AGO Kilamba Kiaxi (CITIC, 2008-2011), NER Kandadji Dam (CGGC, delayed 2008-), TZA Bagamoyo Port $10bn (China Merchants/Oman, suspended 2019), UGA/TZA EACOP 1443km (TotalEnergies/CNOOC, 2022-2026), AGO/ZMB/COD Lobito Corridor (Trafigura/Mota-Engil, proposed 2023), CIV Abidjan Metro (Bouygues/Alstom, delayed 2017-2028), DZA Great Mosque (CSCEC, 2012-2024), DZA East-West Highway 1216km (CITIC-CRCC, 2006-2013), TUN Enfidha Airport (TAV Turkey, 2007-2009), DJI Doraleh Terminal (DP World UAE, cancelled 2018), BWA Morupule B 600MW (CNEEC, defective 2012-2014), ETH Africa CDC HQ (CCECC, $80m grant, 2023), GIN Simandou 650km (WCS/Rio Tinto, 2023-), NGA Abuja Light Rail (CCECC, $500m, 2018), NER/BEN Niger-Benin Pipeline 1950km (CNPC, 2023), SEN 2Africa Cable 45,000km (Alcatel, 2020-2025), SLE Bumbuna 50MW (Salini, 1971-2009) - 30 countries, 139 orgs, 73 contracts, 98 sources, historical inclusive pre-2000 to present, all statuses commissioned/delayed/suspended/cancelled/abandoned/proposed
- App: banner 75 REAL PROJECTS, 30 countries, Quality updated
- Releases: v0.5.0 snapshot (75 features, 334KB) - v0.4.0 (50) + v0.3.0 (30) + v0.2.0 (15) + v0.1.0 (9) preserved

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
