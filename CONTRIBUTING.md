# Contributing to WHO BUILDS AFRICA?

Thank you for contributing - accuracy and traceability matter more than speed.

## Ways to contribute

- Add/correct a project, contract, organization, participation, source
- Improve validation/scripts/docs/map
- Translate methodology (human-reviewed only)

## Workflow (must read before PR)

1. Read `DATA_METHODOLOGY.md`, `SOURCING_GUIDE.md`, `DATA_DICTIONARY.md`
2. Open an Issue describing the record + sources
3. Fork → branch `data/<country>-<slug>` or `fix/<id>` → edit CSVs in `data/curated/` or `samples/` for synthetic
4. Run `python scripts/validate.py --all` locally - must pass
5. PR template checklist + link every new claim to a source row with `verbatim_quote`
6. Reviewer ≠ author required; `scripts/validate.py` must pass in CI
7. On merge, `change_history` auto-appended; release notes in `CHANGELOG.md`

## Data submission rules (non-negotiable)

- Never invent dates/values/coords/roles - use `unknown` / `undisclosed` / `country` precision
- One project ≠ one contract - create separate `contracts.csv` + `participation_records.csv` rows
- Record exact claim supported per source in `claims.csv.claim_text`
- Preserve conflicts - add both claims with `evidence_strength` + `corroboration_status`, don't silently pick one
- Label synthetic data `SYNTHETIC` - never present fabricated records as real

## Templates

- CSV templates: `data/curated/*.csv` headers + `samples/synthetic/`
- Issue templates: `.github/ISSUE_TEMPLATE/`

## Local setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/validate.py --all
python scripts/build.py --out data/releases/v0.1.0 --check
```

## Questions

Open a Discussion - tag `question` or `data-help`.
