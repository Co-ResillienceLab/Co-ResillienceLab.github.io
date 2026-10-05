import json, re, pathlib, requests, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "_data" / "publications.json"
HEADERS = {"Accept": "application/json",
           "User-Agent": "CoRe-Lab-website (mailto:lauren8.scott@northumbria.ac.uk)"}


def load_people():
    people = []
    for f in (ROOT / "_people").glob("*.md"):
        m = re.match(r"^---\s*\n(.*?)\n---", f.read_text(encoding="utf-8"), re.S)
        if not m:
            continue
        fm = yaml.safe_load(m.group(1)) or {}
        if fm.get("orcid"):
            people.append((fm["title"], str(fm["orcid"]).strip()))
    return people


def orcid_works(orcid):
    r = requests.get(f"https://pub.orcid.org/v3.0/{orcid}/works",
                     headers=HEADERS, timeout=30)
    r.raise_for_status()
    works = []
    for g in r.json().get("group", []):
        summaries = g.get("work-summary", [])
        if not summaries:
            continue
        w = summaries[0]
        doi = None
        for e in g.get("external-ids", {}).get("external-id", []):
            if e.get("external-id-type") == "doi":
                doi = e["external-id-value"].lower().strip()
                break
        year = ((w.get("publication-date") or {}).get("year") or {}).get("value") or ""
        works.append({
            "title": w["title"]["title"]["value"],
            "journal": (w.get("journal-title") or {}).get("value") or "",
            "year": str(year),
            "type": w.get("type") or "",
            "doi": doi,
        })
    return works


def crossref(doi):
    try:
        r = requests.get(f"https://api.crossref.org/works/{doi}",
                         headers=HEADERS, timeout=30)
        if r.status_code != 200:
            return {}
        m = r.json()["message"]
        authors = []
        for a in m.get("author", []):
            name = " ".join(x for x in [a.get("given"), a.get("family")] if x)
            authors.append(name or a.get("name", ""))
        return {"authors": authors,
                "journal": (m.get("container-title") or [""])[0]}
    except requests.RequestException:
        return {}


def main():
    cache = {}
    if OUT.exists():
        for p in json.loads(OUT.read_text(encoding="utf-8")):
            if p.get("doi"):
                cache[p["doi"]] = p

    merged = {}
    for name, orcid in load_people():
        try:
            works = orcid_works(orcid)
        except requests.RequestException as e:
            print(f"Skipping {name} ({orcid}): {e}")
            continue
        for w in works:
            key = w["doi"] or f"{w['title'].lower()}|{w['year']}"
            if key not in merged:
                merged[key] = {**w, "authors": [], "members": []}
            merged[key]["members"].append(name)

    for key, p in merged.items():
        if p["doi"]:
            extra = cache.get(p["doi"]) or crossref(p["doi"])
            p["authors"] = extra.get("authors", [])
            p["journal"] = p["journal"] or extra.get("journal", "")

    pubs = sorted(merged.values(), key=lambda p: (p["year"], p["title"]), reverse=True)
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(pubs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(pubs)} publications")


if __name__ == "__main__":
    main()
