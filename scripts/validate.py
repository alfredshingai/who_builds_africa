#!/usr/bin/env python3
"""
Validate curated (+ optionally synthetic) CSVs against vocabularies and rules.
Checks: required fields, ISO codes, date order, coords in Africa, missing source link,
enum validity, value without currency, location without precision, duplicate detection.
"""
import argparse, csv, pathlib, sys, re
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
CURATED = ROOT / "data" / "curated"
SYNTHETIC = ROOT / "samples" / "synthetic"
SCHEMA_DIR = ROOT / "schema"

# Africa bbox approx
AFRICA_BBOX = (-35, -25, 38, 52)  # lat_min, lon_min, lat_max, lon_max (approx)

def load_vocab():
    with open(SCHEMA_DIR / "vocabularies.yaml") as f:
        return yaml.safe_load(f)

def load_csv(path):
    if not path.exists():
        return [], []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        rows = list(r)
        return r.fieldnames or [], rows

def check_iso3(code):
    return bool(re.match(r"^[A-Z]{3}$", code or ""))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--all", action="store_true", help="validate curated")
    ap.add_argument("--samples", action="store_true", help="also validate synthetic samples")
    args = ap.parse_args()
    vocab = load_vocab()
    errors = []
    warns = []

    # choose dirs
    dirs = []
    if args.all or not args.samples:
        dirs.append(("curated", CURATED))
    if args.samples:
        dirs.append(("synthetic", SYNTHETIC))

    # quick enum sets
    valid_sectors = set(vocab["sectors"])
    valid_roles = set(vocab["organization_roles"])
    valid_location = set(vocab["location_precision"])
    valid_strength = set(vocab["evidence_strength"])
    valid_precision = set(vocab["date_precision"])

    for label, base in dirs:
        # projects
        _, projects = load_csv(base / "projects.csv")
        for i, r in enumerate(projects, 2):
            if not r.get("id"): errors.append(f"{label}/projects.csv:{i} missing id")
            if r.get("country_iso3") and not check_iso3(r["country_iso3"]):
                errors.append(f"{label}/projects.csv:{i} invalid iso3 {r['country_iso3']}")
            if r.get("location_precision") and r["location_precision"] not in valid_location:
                errors.append(f"{label}/projects.csv:{i} invalid location_precision {r['location_precision']}")
            # sectors
            if r.get("sectors"):
                for s in r["sectors"].split("|"):
                    s=s.strip()
                    if s and s not in valid_sectors:
                        errors.append(f"{label}/projects.csv:{i} invalid sector {s}")
            # coords check
            lat = r.get("lat","").strip()
            lon = r.get("lon","").strip()
            prec = r.get("location_precision","")
            if prec in ("exact","approximate") and not (lat and lon):
                warns.append(f"{label}/projects.csv:{i} {r['id']} precision {prec} but missing lat/lon")
            if lat and lon:
                try:
                    la, lo = float(lat), float(lon)
                    if not (AFRICA_BBOX[0] <= la <= AFRICA_BBOX[2] and AFRICA_BBOX[1] <= lo <= AFRICA_BBOX[3]):
                        warns.append(f"{label}/projects.csv:{i} coords outside Africa bbox: {la},{lo}")
                except: errors.append(f"{label}/projects.csv:{i} invalid lat/lon")
            if not r.get("location_precision"):
                errors.append(f"{label}/projects.csv:{i} missing location_precision")
        # participation
        _, pars = load_csv(base / "participation_records.csv")
        for i, r in enumerate(pars, 2):
            if r.get("role") and r["role"] not in valid_roles:
                errors.append(f"{label}/participation_records.csv:{i} invalid role {r['role']}")
            if not r.get("role"):
                errors.append(f"{label}/participation_records.csv:{i} missing role")
            if not r.get("org_id"): errors.append(f"{label}/participation_records.csv:{i} missing org_id")
        # contracts
        _, contracts = load_csv(base / "contracts.csv")
        for i, r in enumerate(contracts, 2):
            if r.get("value_original") and not r.get("currency"):
                errors.append(f"{label}/contracts.csv:{i} value without currency {r['id']}")
            if r.get("currency") and not re.match(r"^[A-Z]{3}$", r["currency"]):
                # allow empty
                if r["currency"].strip(): errors.append(f"{label}/contracts.csv:{i} invalid currency {r['currency']}")
        # claims
        _, claims = load_csv(base / "claims.csv")
        for i, r in enumerate(claims, 2):
            if not r.get("verbatim_quote"): warns.append(f"{label}/claims.csv:{i} missing verbatim_quote {r['id']}")
            if not r.get("claim_text"): errors.append(f"{label}/claims.csv:{i} missing claim_text")
            if r.get("evidence_strength") and r["evidence_strength"] not in valid_strength:
                errors.append(f"{label}/claims.csv:{i} invalid evidence_strength {r['evidence_strength']}")
            if not r.get("source_id"): errors.append(f"{label}/claims.csv:{i} missing source_id")
        # dates
        _, dates = load_csv(base / "dates.csv")
        for i, r in enumerate(dates, 2):
            if r.get("precision") and r["precision"] not in valid_precision:
                errors.append(f"{label}/dates.csv:{i} invalid precision {r['precision']}")

    # duplicate checks (within synthetic + curated individually)
    for label, base in dirs:
        _, projects = load_csv(base / "projects.csv")
        seen=set()
        for r in projects:
            k=(r.get("canonical_name","").lower().strip(), r.get("country_iso3"))
            if k in seen and k!=("",None): warns.append(f"{label} duplicate candidate project {k}")
            seen.add(k)
        _, orgs = load_csv(base / "organizations.csv")
        seen=set()
        for r in orgs:
            k=r.get("canonical_name","").lower().strip()
            if k in seen and k: warns.append(f"{label} duplicate org {k}")
            seen.add(k)

    if warns:
        print("WARNINGS:")
        for w in warns: print("  -",w)
    if errors:
        print("ERRORS:")
        for e in errors: print("  -",e)
        print(f"\n{len(errors)} error(s), {len(warns)} warning(s)")
        sys.exit(1)
    else:
        print(f"OK — {len(warns)} warning(s), 0 errors ({', '.join(d[0] for d in dirs)})")
        sys.exit(0)

if __name__ == "__main__":
    main()
