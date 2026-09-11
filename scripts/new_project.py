#!/usr/bin/env python3
"""
Helper for contributors: interactively create a new project entry
and validate against vocabularies. No auto-publish - outputs CSV rows to paste.

Usage:
  python scripts/new_project.py
  python scripts/new_project.py --check  # just validate curated

FOSS, no proprietary deps. Prompts for required fields, enforces vocabularies.
"""
import csv, pathlib, re, sys, yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
VOC = yaml.safe_load(open(ROOT / "schema" / "vocabularies.yaml"))

def prompt(msg, default=""):
    v = input(f"{msg} [{default}]: ").strip()
    return v or default

def choose(msg, options):
    print(f"{msg} options: {', '.join(options)}")
    v = prompt(msg)
    if v and v not in options:
        print(f"  ! must be one of {options}")
        return choose(msg, options)
    return v

def main():
    if "--check" in sys.argv:
        import subprocess
        subprocess.run([sys.executable, str(ROOT / "scripts" / "validate.py"), "--all"], check=True)
        return
    print("WHO BUILDS AFRICA? - New project helper (outputs CSV rows to copy into data/curated/)")
    print("Read DATA_METHODOLOGY.md + SOURCING_GUIDE.md first. Never invent values.")
    pid = prompt("Project ID (wba_prj_*)", "wba_prj_01HREAL016")
    if not re.match(r"^wba_prj_[A-Z0-9]+$", pid):
        print("  ! ID must match wba_prj_*")
        return
    name = prompt("Canonical name")
    alias = prompt("Aliases (| separated)", "")
    iso = prompt("Country ISO3 (e.g. ZWE)", "ZWE")
    if not re.match(r"^[A-Z]{3}$", iso):
        print("  ! ISO3 must be 3 uppercase letters")
        return
    print(f"Sectors: {VOC['sectors']}")
    sectors = prompt("Sectors (| separated)")
    for s in sectors.split("|"):
        if s and s not in VOC["sectors"]:
            print(f"  ! invalid sector {s}")
            return
    status = choose("Status", VOC["project_status"])
    prec = choose("Location precision", VOC["location_precision"])
    lat = prompt("Lat (empty if corridor/country)", "")
    lon = prompt("Lon (empty if corridor/country)", "")
    wkt = prompt("geom_wkt (LINESTRING(...) or POINT(...) or empty)", "")
    summary = prompt("One-sentence summary")
    print("\n--- CSV row for data/curated/projects.csv ---")
    print(f"{pid},{name},{alias},{iso},{sectors},{status},{prec},{lat},{lon},{wkt},{summary},,2026-09-11,2026-09-11")
    print("\nNext: add dates.csv, sources.csv, claims.csv, contracts.csv, participation_records.csv entries")
    print("Then run: python scripts/validate.py --all")
    print("See samples/synthetic/ for example rows and DATA_DICTIONARY.md for headers.")

if __name__ == "__main__":
    main()
