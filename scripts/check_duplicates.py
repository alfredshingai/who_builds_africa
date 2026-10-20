#!/usr/bin/env python3
"""
Detect duplicate and broken records in the curated dataset.

Pure-stdlib checks, safe for CI with only PyYAML installed:
  * duplicate primary keys
  * broken foreign keys
  * duplicate projects by name/alias within a country
  * near-identical projects in the same sector/locality
  * duplicate organisations after legal-suffix normalisation
  * duplicate source URLs
  * duplicate claims and participation rows
  * repeated aliases

Exit status is 1 when errors are found. Warnings are advisory; --strict
also fails on warnings. Reviewed legitimate pairs belong in
data/curated/duplicate_allowlist.csv.
"""
import argparse
import collections
import csv
import difflib
import itertools
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_DIR = ROOT / "data" / "curated"

LEGAL_WORDS = {
    "the", "of", "and", "for", "company", "corporation", "corp", "limited",
    "ltd", "group", "plc", "inc", "sa", "co", "s", "republic",
}
PROJECT_STOP = {"the", "of", "and", "for", "a", "an", "project", "phase", "lot"}


def load_csv(base, name):
    path = pathlib.Path(base) / f"{name}.csv"
    if not path.exists():
        return [], []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def ascii_lower(value):
    value = unicodedata.normalize("NFKD", value or "")
    return value.encode("ascii", "ignore").decode().lower()


def norm_name(value, drop=()):
    value = ascii_lower(value).replace("&", " and ")
    value = re.sub(r"\([^)]*\)", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(w for w in value.split() if w not in drop)


def norm_url(value):
    value = (value or "").strip().lower()
    value = re.sub(r"^https?://", "", value)
    value = re.sub(r"^www\.", "", value)
    value = value.split("#", 1)[0].split("?", 1)[0].rstrip("/")
    return value


def tokens(value):
    return set(norm_name(value, PROJECT_STOP).split())


def variants(row):
    names = [row.get("canonical_name", "")]
    names.extend((row.get("aliases") or "").split("|"))
    return [n.strip() for n in names if n.strip()]


def pair_key(a, b):
    return tuple(sorted((a, b)))


def load_allowlist(path):
    allowed = {}
    if not path.exists():
        return allowed
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row.get("id_a") or not row.get("id_b"):
                continue
            allowed[(row.get("entity_type", ""), pair_key(row["id_a"], row["id_b"]))] = row.get("reason", "")
    return allowed


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, message):
        self.errors.append(message)

    def warn(self, message):
        self.warnings.append(message)


def check_primary_keys(base, tables, report):
    for table in tables:
        _, rows = load_csv(base, table)
        seen = collections.Counter(r.get("id") for r in rows if r.get("id"))
        for ident, count in seen.items():
            if count > 1:
                report.error(f"{table}.csv duplicate primary key {ident} ({count}x)")


def check_foreign_keys(base, report):
    _, projects = load_csv(base, "projects")
    _, dates = load_csv(base, "dates")
    _, sources = load_csv(base, "sources")
    _, orgs = load_csv(base, "organizations")
    _, claims = load_csv(base, "claims")
    _, contracts = load_csv(base, "contracts")

    project_ids = {r["id"] for r in projects}
    date_ids = {r["id"] for r in dates}
    source_ids = {r["id"] for r in sources}
    org_ids = {r["id"] for r in orgs}
    claim_ids = {r["id"] for r in claims}
    contract_ids = {r["id"] for r in contracts}

    def optional(value, valid, table, row, field):
        value = (value or "").strip()
        if value and value not in valid:
            report.error(f"{table}.csv {row.get('id','?')} broken {field} reference {value}")

    for table in ("project_locations", "claims", "contracts", "participation_records",
                  "financing_records", "events"):
        _, rows = load_csv(base, table)
        for row in rows:
            optional(row.get("project_id"), project_ids, table, row, "project_id")

    _, rows = load_csv(base, "claims")
    for row in rows:
        optional(row.get("source_id"), source_ids, "claims", row, "source_id")
        optional(row.get("organization_id"), org_ids, "claims", row, "organization_id")
        optional(row.get("contract_id"), contract_ids, "claims", row, "contract_id")

    _, rows = load_csv(base, "contracts")
    for row in rows:
        optional(row.get("contracting_authority"), org_ids, "contracts", row, "contracting_authority")
        optional(row.get("contractor"), org_ids, "contracts", row, "contractor")

    _, rows = load_csv(base, "participation_records")
    for row in rows:
        optional(row.get("org_id"), org_ids, "participation_records", row, "org_id")
        optional(row.get("contract_id"), contract_ids, "participation_records", row, "contract_id")

    _, rows = load_csv(base, "financing_records")
    for row in rows:
        value = (row.get("institution") or "").strip()
        if value.startswith("wba_org_"):
            optional(value, org_ids, "financing_records", row, "institution")

    _, rows = load_csv(base, "events")
    for row in rows:
        optional(row.get("date_id"), date_ids, "events", row, "date_id")
        optional(row.get("source_claim"), claim_ids, "events", row, "source_claim")

    for table in ("organization_aliases", "organization_countries"):
        _, rows = load_csv(base, table)
        for row in rows:
            optional(row.get("org_id"), org_ids, table, row, "org_id")

    _, rows = load_csv(base, "organization_relations")
    for row in rows:
        optional(row.get("from_org"), org_ids, "organization_relations", row, "from_org")
        optional(row.get("to_org"), org_ids, "organization_relations", row, "to_org")


def check_projects(base, allowed, report):
    _, projects = load_csv(base, "projects")
    _, locations = load_csv(base, "project_locations")
    loc = {r["project_id"]: r for r in locations}
    _, contracts = load_csv(base, "contracts")
    _, participation = load_csv(base, "participation_records")
    project_orgs = collections.defaultdict(set)
    for row in contracts:
        for field in ("contracting_authority", "contractor"):
            if row.get(field):
                project_orgs[row["project_id"]].add(row[field])
    for row in participation:
        if row.get("org_id"):
            project_orgs[row["project_id"]].add(row["org_id"])

    # Exact names or aliases shared by different projects in one country.
    names = collections.defaultdict(set)
    for row in projects:
        for name in variants(row):
            names[(norm_name(name), row.get("country_iso3"))].add(row["id"])
    for (name, country), ids in names.items():
        if name and len(ids) > 1:
            report.error(f"projects.csv duplicate name/alias '{name}' in {country}: {', '.join(sorted(ids))}")

    for a, b in itertools.combinations(projects, 2):
        if a.get("country_iso3") != b.get("country_iso3"):
            continue
        key = ("project", pair_key(a["id"], b["id"]))
        if key in allowed:
            continue
        sectors_a = set(filter(None, (a.get("sectors") or "").split("|")))
        sectors_b = set(filter(None, (b.get("sectors") or "").split("|")))
        ratio = difflib.SequenceMatcher(
            None, norm_name(a.get("canonical_name")), norm_name(b.get("canonical_name"))
        ).ratio()
        same_sector = bool(sectors_a & sectors_b)

        la, lb = loc.get(a["id"], {}), loc.get(b["id"], {})
        same_locality = bool(la.get("city")) and la.get("city") == lb.get("city")
        if not same_locality:
            same_locality = bool(la.get("admin1")) and la.get("admin1") == lb.get("admin1")

        subset = False
        for va in variants(a):
            ta = tokens(va)
            if len(ta) < 2:
                continue
            for vb in variants(b):
                tb = tokens(vb)
                if len(tb) < 2:
                    continue
                if ta < tb or tb < ta:
                    subset = True
                    break
            if subset:
                break

        shared_org = bool(project_orgs[a["id"]] & project_orgs[b["id"]])
        reason = f"{a['id']} '{a.get('canonical_name')}' / {b['id']} '{b.get('canonical_name')}'"
        if same_sector and ratio >= 0.77:
            report.error(f"near-duplicate projects ({ratio:.2f}, same sector): {reason}")
        elif same_locality and subset and shared_org:
            report.error(f"near-duplicate projects (same locality, shared org): {reason}")
        elif same_sector and ratio >= 0.65:
            report.warn(f"review similar projects ({ratio:.2f}): {reason}")
        elif same_locality and subset:
            report.warn(f"review similar projects (same locality): {reason}")


def check_organizations(base, allowed, report):
    _, orgs = load_csv(base, "organizations")
    _, aliases = load_csv(base, "organization_aliases")

    by_name = collections.defaultdict(list)
    for row in orgs:
        by_name[norm_name(row.get("canonical_name"), LEGAL_WORDS)].append(row)
    for name, rows in by_name.items():
        if name and len(rows) > 1:
            report.error(f"organizations.csv duplicate normalized name '{name}': {', '.join(r['id'] for r in rows)}")

    alias_names = collections.defaultdict(set)
    for row in aliases:
        name = norm_name(row.get("alias"), LEGAL_WORDS)
        if name:
            alias_names[(name, row.get("org_id"))].add(row.get("id"))
    for (name, org_id), ids in alias_names.items():
        if len(ids) > 1:
            report.warn(f"organization_aliases.csv repeated alias '{name}' for {org_id}: {', '.join(sorted(ids))}")

    for a, b in itertools.combinations(orgs, 2):
        ratio = difflib.SequenceMatcher(
            None, norm_name(a.get("canonical_name"), LEGAL_WORDS),
            norm_name(b.get("canonical_name"), LEGAL_WORDS),
        ).ratio()
        if ratio >= 0.97:
            if ("organization", pair_key(a["id"], b["id"])) in allowed:
                continue
            report.warn(
                f"review similar organizations ({ratio:.2f}): "
                f"{a['id']} '{a.get('canonical_name')}' / {b['id']} '{b.get('canonical_name')}'"
            )


def check_sources(base, report):
    _, sources = load_csv(base, "sources")
    urls = collections.defaultdict(list)
    for row in sources:
        key = norm_url(row.get("url"))
        if key:
            urls[key].append(row["id"])
    for url, ids in urls.items():
        if len(ids) > 1:
            report.error(f"sources.csv duplicate URL {url}: {', '.join(ids)}")


def check_claims_and_participation(base, report):
    _, claims = load_csv(base, "claims")
    seen = collections.defaultdict(list)
    for row in claims:
        key = (
            row.get("project_id"), row.get("source_id"),
            norm_name(row.get("verbatim_quote")), row.get("claim_type"),
            row.get("organization_id"), row.get("contract_id"),
        )
        seen[key].append(row["id"])
    for ids in seen.values():
        if len(ids) > 1:
            report.error(f"claims.csv duplicate claim: {', '.join(ids)}")

    _, rows = load_csv(base, "participation_records")
    seen = collections.defaultdict(list)
    for row in rows:
        key = (row.get("project_id"), row.get("org_id"), row.get("role"), row.get("contract_id"))
        seen[key].append(row["id"])
    for key, ids in seen.items():
        if len(ids) > 1:
            report.error(f"participation_records.csv duplicate role {key}: {', '.join(ids)}")


def main():
    parser = argparse.ArgumentParser(description="Check curated data for duplicates and broken links")
    parser.add_argument("--in", dest="inp", default=str(DEFAULT_DIR), help="dataset directory")
    parser.add_argument("--allowlist", default=None, help="reviewed duplicate pairs CSV")
    parser.add_argument("--strict", action="store_true", help="fail on warnings too")
    args = parser.parse_args()

    base = pathlib.Path(args.inp)
    allowlist_path = pathlib.Path(args.allowlist) if args.allowlist else base / "duplicate_allowlist.csv"
    allowed = load_allowlist(allowlist_path)
    report = Report()

    tables = [
        "projects", "organizations", "organization_aliases", "organization_countries",
        "organization_relations", "sources", "claims", "contracts", "participation_records",
        "financing_records", "events", "dates", "project_locations", "change_history",
    ]
    check_primary_keys(base, tables, report)
    check_foreign_keys(base, report)
    check_projects(base, allowed, report)
    check_organizations(base, allowed, report)
    check_sources(base, report)
    check_claims_and_participation(base, report)

    for message in report.errors:
        print("ERROR:", message)
    for message in report.warnings:
        print("WARN: ", message)
    print(f"{len(report.errors)} error(s), {len(report.warnings)} warning(s) in {base}")
    if report.errors or (args.strict and report.warnings):
        sys.exit(1)


if __name__ == "__main__":
    main()
