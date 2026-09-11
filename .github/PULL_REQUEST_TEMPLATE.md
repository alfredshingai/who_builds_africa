<!-- WHO BUILDS AFRICA — PR Checklist -->
## Summary

## Type
- [ ] Data addition/correction (curated CSVs)
- [ ] Docs/methodology
- [ ] Code/scripts/app

## Data PR Checklist (if applicable)
- [ ] Every new/changed claim has `source_id` + `verbatim_quote` + `claim_text`
- [ ] `evidence_strength` set per claim (not defaulted)
- [ ] Dates use `dates.csv` with correct `precision` (day/month/year/approx/range/before/after/unknown)
- [ ] `location_precision` honest (exact/approx/city/district/province/country/cross_border/corridor/unknown) — no fake coords
- [ ] Contract `value` separated from `estimated cost` / `loan` — currency present if value present
- [ ] `participation_records.role` explicitly set (contractor != financier != supplier …)
- [ ] Checked duplicate org/project candidates
- [ ] Ran `python scripts/validate.py --all` locally — passes
- [ ] Synthetic vs real clearly labelled (SYNTHETIC only in `samples/`)

## Notes for reviewer

Evidence summary, conflicts preserved, links to sources:
