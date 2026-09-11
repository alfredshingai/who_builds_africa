#!/usr/bin/env python3
"""
Build release artifacts: CSVs -> GeoJSON + SQLite (MVP).
Usage: python scripts/build.py --in data/curated --out data/releases/v0.1.0
       python scripts/build.py --samples --out /tmp/test_build
"""
import argparse, pathlib, csv, json, sqlite3, shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]

def build(src: pathlib.Path, out: pathlib.Path, use_samples=False):
    in_dir = ROOT / "samples" / "synthetic" if use_samples else src
    out.mkdir(parents=True, exist_ok=True)
    # copy curated/synthetic CSVs to release as snapshot
    for p in in_dir.glob("*.csv"):
        shutil.copy(p, out / p.name)
    # GeoJSON from projects
    projects_path = in_dir / "projects.csv"
    features=[]
    if projects_path.exists():
        with open(projects_path, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                lat=r.get("lat","").strip(); lon=r.get("lon","").strip()
                prec=r.get("location_precision","")
                geom=None
                props={"id":r["id"],"name":r["canonical_name"],"country":r["country_iso3"],"sectors":r["sectors"],"status":r["status"],"location_precision":prec}
                if lat and lon:
                    try: geom={"type":"Point","coordinates":[float(lon), float(lat)]}
                    except: geom=None
                elif r.get("geom_wkt","").strip().startswith("LINESTRING"):
                    # placeholder - real parser would use shapely
                    geom=None
                    props["geom_wkt"]=r["geom_wkt"]
                features.append({"type":"Feature","geometry":geom,"properties":props})
    gj={"type":"FeatureCollection","features":features, "_note":"SYNTHETIC if from samples; real data requires source-backed coords"}
    (out / "projects.geojson").write_text(json.dumps(gj, indent=2), encoding="utf-8")

    # JSON extracts for frontend (projects + related records denormalized where useful)
    def csv_to_json(name):
        p = in_dir / f"{name}.csv"
        if not p.exists(): return []
        with open(p, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    extracts = {
        "projects": csv_to_json("projects"),
        "organizations": csv_to_json("organizations"),
        "organization_aliases": csv_to_json("organization_aliases"),
        "organization_countries": csv_to_json("organization_countries"),
        "contracts": csv_to_json("contracts"),
        "participation_records": csv_to_json("participation_records"),
        "financing_records": csv_to_json("financing_records"),
        "sources": csv_to_json("sources"),
        "claims": csv_to_json("claims"),
        "events": csv_to_json("events"),
        "dates": csv_to_json("dates"),
        "project_locations": csv_to_json("project_locations"),
    }
    (out / "data.json").write_text(json.dumps(extracts, indent=2), encoding="utf-8")
    # also individual JSON files for smaller fetches
    for k,v in extracts.items():
        (out / f"{k}.json").write_text(json.dumps(v, indent=2), encoding="utf-8")

    # SQLite
    db_path = out / "footprints.sqlite"
    if db_path.exists(): db_path.unlink()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("CREATE TABLE projects (id TEXT PRIMARY KEY, name TEXT, country TEXT, sectors TEXT, status TEXT, location_precision TEXT, lat REAL, lon REAL)")
    for feat in features:
        p=feat["properties"]; g=feat["geometry"]
        lat = g["coordinates"][1] if g else None
        lon = g["coordinates"][0] if g else None
        cur.execute("INSERT INTO projects VALUES (?,?,?,?,?,?,?,?)", (p["id"], p["name"], p["country"], p["sectors"], p["status"], p["location_precision"], lat, lon))
    con.commit(); con.close()

    # CITATION
    (out / "CITATION.md").write_text(f"# Release {out.name}\n\nCite: Africa Contract Footprints / WHO BUILDS AFRICA? ({out.name}), ODbL-1.0\nSource: https://github.com/alfredshingai/who_builds_africa\nCounts: {len(features)} project features\n", encoding="utf-8")
    print(f"Built {len(features)} features -> {out}")

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", default=str(ROOT/"data/curated"))
    ap.add_argument("--out", required=True)
    ap.add_argument("--samples", action="store_true", help="build from synthetic samples")
    ap.add_argument("--check", action="store_true", help="validate before build (runs validate.py)")
    args=ap.parse_args()
    if args.check:
        import subprocess, sys
        r=subprocess.run([sys.executable, str(ROOT/"scripts/validate.py"), "--all"],)
        if r.returncode!=0: raise SystemExit(r.returncode)
    build(pathlib.Path(args.inp), pathlib.Path(args.out), args.samples)
