# Data Dictionary - v0.1

All curated CSVs in `data/curated/` - headers are contract. See `schema/wba.schema.json` for machine schema.

## countries.csv
`iso3` (PK, ISO3166 alpha-3), `name_en`, `name_fr`, `name_pt`, `region` (AU region)

## projects.csv
`id` (PK wba_prj_*), `canonical_name`, `aliases` (| separated), `country_iso3` FK, `sectors` (|), `status` enum, `location_precision` enum, `lat`, `lon`, `geom_wkt` (nullable), `summary` (1 sentence), `notes`, `created_at`, `updated_at`

## organizations.csv
`id` (PK wba_org_*), `canonical_name`, `org_type` enum[private,soe,state_agency,dev_bank,consortium,jv,export_credit,other], `notes`

## organization_aliases.csv
`id`, `org_id` FK, `alias`, `lang`, `is_transliteration` bool

## organization_relations.csv
`id`, `from_org` FK, `to_org` FK, `relation` enum[parent,subsidiary,jv_member,consortium_member], `start_date` FK→dates.id, `end_date`

## organization_countries.csv
`org_id` FK, `country_iso3` FK, `relation` enum[incorporation,headquarters,parent,ultimate_owner,financing,soe_origin], `source_claim` FK→claims.id

## dates.csv
`id` (PK wba_date_*), `edtf_string`, `precision` enum[day,month,year,approximate,range,before,after,unknown], `earliest` (ISO date), `latest`, `display_string`

## sources.csv
`id` (PK wba_src_*), `title`, `publisher`, `authors`, `source_type` enum, `pub_date` FK, `access_date` FK, `url`, `archive_url`, `lang`, `page`, `classification` enum[primary,secondary,tertiary], `accessibility`, `paywall` bool, `license`

## claims.csv
`id` (PK wba_clm_*), `source_id` FK, `project_id` FK nullable, `organization_id` FK nullable, `contract_id` FK nullable, `verbatim_quote` (exact), `claim_text` (normalized: "X awarded Y to Z in 2014"), `claim_type` enum[award,role,value,location,status,date,other], `evidence_strength` enum[confirmed,corroborated,officially_reported,credibly_reported,probable,unclear,disputed,unverified,corrected,archived], `corroboration_status`

## contracts.csv
`id` (PK wba_ctr_*), `project_id` FK, `title`, `contract_id_external`, `contracting_authority` FK→org, `contractor` FK→org, `contract_type` enum, `procurement_method`, `status` enum, `award_date` FK, `sign_date` FK, `start_date` FK, `end_date` FK, `currency` (ISO4217), `value_original`, `value_precision` enum[exact,approx,range,undisclosed], `financing_source` FK→org nullable, `amendment_count` int, `notes`

## participation_records.csv
`id` (PK wba_par_*), `project_id` FK, `contract_id` FK nullable, `org_id` FK, `role` enum[financier,developer,contractor,subcontractor,supplier,consultant,designer,operator,maintainer,manager,jv,consortium_member,sponsor], `start_date` FK nullable, `end_date` nullable, `share_percent` nullable, `notes`

## financing_records.csv
`id` PK `wba_fin_*`, `project_id` FK, `institution` FK→org, `instrument` enum[loan,grant,equity,export_credit,guarantee], `amount`, `currency`, `share_percent`, `notes`

## events.csv
`id` PK `wba_evt_*`, `project_id` FK, `event_type` enum[proposed,announced,feasibility,tender_issued,awarded,signed,financial_close,construction_start,delayed,suspended,contractor_replaced,redesigned,completed,commissioned,partially_completed,cancelled,abandoned,revived,extension,renewal], `date_id` FK→dates.id, `source_claim` FK, `notes`

## change_history.csv
`id`, `entity_type`, `entity_id`, `changed_by`, `changed_at`, `field`, `old_value`, `new_value`, `source_claim`, `reason`

## project_locations.csv
`project_id` FK, `admin1`, `admin2`, `city`, `locality`, `precision` enum, `lat`, `lon`

## releases
`data/releases/vX.Y.Z/` → exports + `CITATION.md` + `CHECKSUMS`

## Vocabularies
See `schema/vocabularies.yaml` for full enums.

## IDs

ULID-based, stable, never reused. Example: `wba_prj_01H9...`, `wba_org_01H9...`. Use `slug` for URLs.

## Sample

See `samples/synthetic/` - all rows marked `SYNTHETIC` in notes.
