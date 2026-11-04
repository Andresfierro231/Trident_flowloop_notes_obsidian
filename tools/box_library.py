#!/usr/bin/env python3
"""Offline, read-only Box library intake. Text extraction never renders pages."""
import argparse
import collections
from concurrent.futures import ThreadPoolExecutor
import csv
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET

REPO = Path(__file__).resolve().parents[1]
HOME = REPO / "X.Chat/01_sources/box_library"
DEFAULT_ROOT = Path.home() / "ObsidianVaults/MainVault/Box/books/research"
TOPICS = {
    "natural circulation": r"natural.circulation|thermosiphon|thermosyphon",
    "molten salts": r"molten.salt|hitec|flibe|flinak",
    "heat transfer": r"heat.transfer|convection|thermal.boundary",
    "CFD": r"\bcfd\b|computational.fluid",
    "reduced models": r"reduced.order|reduced.model|compartment|thermal.network|pod.galerkin",
    "digital twins": r"digital.twin|digital.shadow",
    "inverse problems": r"inverse.problem|parameter.estimat|identifiab|calibrat",
    "uncertainty": r"uncertainty|bayesian|stochastic|probabilistic",
    "flow resistance": r"pressure.loss|pressure.drop|friction|hydraulic|fitting.loss",
    "flow development": r"developing.flow|entrance.region|boundary.layer",
    "flow reversal": r"flow.reversal|counter.flow|counter.current|recirculation",
    "stability and transitions": r"stability|instabilit|transient|chaotic|bifurcation",
    "material properties": r"thermophysical|viscosity|specific.heat|thermal.conductivity|density",
    "experimental methods": r"measurement|instrumentation|sensor|experimental",
    "numerical methods": r"finite.volume|finite.element|discretization|numerical.method",
    "system codes": r"\bsam\b|system.code|relap|modelica",
    "reactors": r"reactor|nuclear|neutronic",
    "software": r"python|programming|software|coding",
}
def write_json(path, value):
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")

def atomic_text(path, text):
    temporary = path.with_name(path.name+".tmp")
    temporary.write_text(text)
    temporary.replace(path)

def scan_error(error):
    raise error

def hash_file(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def bounded_hash(path):
    try:
        result = subprocess.run([sys.executable, str(Path(__file__).resolve()), "_hash", str(path)], capture_output=True, text=True, timeout=5)
        if result.returncode or not re.fullmatch(r"[0-9a-f]{64}", result.stdout.strip()):
            raise ValueError("hash read failed")
        return path, result.stdout.strip(), None
    except (subprocess.TimeoutExpired, ValueError) as e:
        return path, None, str(e)[:300]

def abstract_from(text):
    """Return a candidate only, with a literal heading and page locator."""
    for m in re.finditer(r"\b(?:abstract|a b s t r a c t)\b\s*[:.\n]?", text, re.I):
        chunk = text[m.end():m.end()+10000]
        end = re.search(r"\b(?:key\s*words?|index terms)\s*[:—–]|\n\s*(?:(?:1\s*[.]?\s*|I\.\s*)?introduction|nomenclature)\b|©|copyright", chunk, re.I)
        if end:
            chunk = chunk[:end.start()]
        # No clear end means a capped candidate, explicitly flagged.
        value = re.sub(r"\s+", " ", chunk).strip()
        if len(value) >= 100:
            return {"text": value[:8000], "status": "extracted_candidate",
                    "page": text[:m.start()].count("\f")+1,
                    "boundary": "heading_to_heading" if end else "bounded_text_needs_review"}
    return {"text": "", "status": "not_found_in_first_5_pages", "page": None, "boundary": None}

def extract(path):
    with path.open("rb") as f:
        magic = f.read(8)
    result = {"text_status": "unsupported_format", "abstract": {"text": "", "status": "not_applicable", "page": None},
              "keywords_native": [], "doi_candidates": [], "opening_excerpt": "", "text_pages_examined": 0}
    text = ""
    if magic.startswith(b"%PDF"):
        from pdfminer.high_level import extract_text
        text = extract_text(str(path), maxpages=5)
        result["text_status"] = "pdf_text_extracted" if text.strip() else "no_extractable_text"
        result["text_pages_examined"] = min(5, len(text.rstrip("\f").split("\f"))) if text else 0
        result["abstract"] = abstract_from(text)
        if not text.strip():
            result["abstract"]["status"] = "no_extractable_text"
    elif path.suffix.lower() == ".docx":
        with zipfile.ZipFile(path) as z:
            item = z.getinfo("word/document.xml")
            if item.file_size > 20*1024*1024:
                raise ValueError("Word XML exceeds bounded intake size")
            tree = ET.fromstring(z.read(item))
        ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
        text = "\n".join("".join(p.itertext()) for p in tree.findall(".//w:p", ns))[:50000]
        result["text_status"] = "word_text_excerpt"
        result["abstract"] = abstract_from(text)
        result["excerpt_locator"] = "opening Word body text (up to 50000 characters)"
    elif path.suffix.lower() == ".csv":
        with path.open(errors="replace") as f:
            text = f.read(50000)
        result["text_status"] = "supporting_csv_excerpt"
        result["abstract"]["status"] = "not_applicable_supporting_data"
    elif path.suffix.lower() in (".txt", ".md", ".rst", ".bib"):
        text = path.read_text(errors="replace")[:50000]
        result["text_status"] = "text_file_excerpt"
        result["abstract"] = abstract_from(text)
    elif path.suffix.lower() in (".png", ".jpg", ".jpeg", ".gif", ".tif", ".tiff"):
        result["text_status"] = "image_not_inspected"
    kw = re.search(r"(?:key\s*words?|index terms)\s*[:—–-]\s*([^\n\f]{3,500})", text, re.I)
    if kw:
        result["keywords_native"] = [x.strip(" .;") for x in re.split(r"[;,•]", kw[1]) if x.strip()]
    result["doi_candidates"] = sorted(set(x.rstrip(".,;)") for x in re.findall(r"10\.\d{4,9}/[^\s<>\"{}]+", text[:30000], re.I)))[:12]
    result["opening_excerpt"] = re.sub(r"\s+", " ", text[:1000]).strip()[:600]
    result.setdefault("excerpt_locator", "opening extracted text; PDF pages 1–5" if magic.startswith(b"%PDF") else "file beginning")
    topic_text = path.name+" "+(result["abstract"]["text"][:4000] or text[:2500])
    result["topics"] = [k for k, pat in TOPICS.items() if re.search(pat, topic_text, re.I)]
    return result

def records(home):
    f = home / "catalog.jsonl"
    return [json.loads(x) for x in f.read_text().splitlines()] if f.exists() else []

def annotated(home):
    """Curated fields are separate from machine intake and never overwritten."""
    f = home / "annotations.json"
    annotations = json.loads(f.read_text()) if f.exists() else {}
    result = []
    for record in records(home):
        r = record.copy()
        r["curation"] = annotations.get(r["id"], {})
        note = home / "notes" / (r["id"]+".md")
        if note.is_file():
            r["note_path"] = str(note.relative_to(home))
        result.append(r)
    return result

def refresh(root, home, reextract=False):
    # Refuse a missing mount: never interpret it as removal of the whole library.
    if not root.is_dir() or root.is_symlink():
        raise ValueError("Library root must exist as a real directory; pass the verified per-machine root.")
    home.mkdir(parents=True, exist_ok=True)
    previous = records(home)
    old = {r["id"]: r for r in previous}
    oldpaths = {x["path"]: r["id"] for r in previous for x in r.get("locations", [])}
    grouped = collections.defaultdict(list)
    paths = []
    for here, dirs, names in os.walk(root, followlinks=False, onerror=scan_error):
        dirs[:] = sorted(d for d in dirs if not d.startswith(".") and not (Path(here)/d).is_symlink())
        for name in sorted(names):
            f = Path(here)/name
            if name.startswith(".") or f.is_symlink():
                continue
            paths.append(f)
    with ThreadPoolExecutor(max_workers=6) as pool:
        for f, sha, error in pool.map(bounded_hash, paths):
            rel = f.relative_to(root).as_posix()
            ident = "BL-"+sha[:20] if sha else "PENDING-"+hashlib.sha256(rel.encode()).hexdigest()[:20]
            grouped[ident].append({"path": rel, "bytes": f.stat().st_size, "sha256": sha, "read_error": error})
    if not grouped:
        raise ValueError("Empty library scan refused; check the mount/root.")
    now = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    changes = {"added": [], "removed": [], "changed": [], "moved_or_alias_changed": [], "availability_changed": []}
    output = []
    for ident, locations in sorted(grouped.items()):
        locations.sort(key=lambda x: x["path"])
        sha = locations[0]["sha256"]
        assert all(x["sha256"] == sha for x in locations), "ID prefix collision"
        if ident in old and not reextract:
            assert old[ident]["sha256"] == sha, "ID prefix collision with previous record"
            r = old[ident].copy()
            if {x["path"] for x in r["locations"]} != {x["path"] for x in locations}:
                changes["moved_or_alias_changed"].append({"id": ident, "before": [x["path"] for x in r["locations"]], "after": [x["path"] for x in locations]})
        else:
            path = root / locations[0]["path"]
            try:
                if not sha:
                    raise ValueError("Content hash unavailable: "+str(locations[0]["read_error"]))
                proc = subprocess.run([sys.executable, str(Path(__file__).resolve()), "_extract", str(path)],
                                      capture_output=True, text=True, timeout=30)
                if proc.returncode:
                    raise ValueError(proc.stderr[-600:])
                content = json.loads(proc.stdout)
            except (subprocess.TimeoutExpired, ValueError, json.JSONDecodeError) as e:
                content = {"text_status": "extraction_error", "error": str(e)[:600],
                           "abstract": {"text": "", "status": "extraction_error", "page": None},
                           "topics": [], "keywords_native": [], "doi_candidates": [], "opening_excerpt": ""}
            r = {"id": ident, "sha256": sha, "first_seen": old.get(ident, {}).get("first_seen", now),
                 "title": path.stem, "title_status": "filename_unverified", **content}
            if ident not in old:
                changes["added"].append(ident)
        r["locations"] = locations
        if r["title_status"] == "filename_unverified":
            filename = Path(locations[0]["path"])
            r["title"] = filename.stem if filename.suffix.lower() in (".pdf", ".docx", ".csv", ".txt", ".md", ".bib", ".rst") else filename.name
        r["vault_targets"] = ["MainVault/Box/books/research/"+x["path"] for x in locations]
        r["status"] = "present"
        r["categories"] = sorted({str(Path(x["path"]).parent) for x in locations})
        r["keywords"] = sorted(set(r.get("topics", []) + r.get("keywords_native", []) + ["folder:"+x for x in r["categories"]]))
        r["description"] = "Discovery record: "+r["title"]+"; folders: "+", ".join(r["categories"])
        r["reading_status"] = "machine_text_intake_not_scientific_review"
        output.append(r)
    currentpaths = {x["path"]: r["id"] for r in output for x in r["locations"]}
    for path, ident in oldpaths.items():
        if path in currentpaths and ident != currentpaths[path]:
            kind = "availability_changed" if ident.startswith("PENDING-") or currentpaths[path].startswith("PENDING-") else "changed"
            changes[kind].append({"path": path, "before": ident, "after": currentpaths[path]})
    for ident, r in old.items():
        if ident not in grouped:
            last_paths = r.get("locations") or r.get("previous_locations", [])
            unavailable = any(currentpaths.get(x["path"], "").startswith("PENDING-") for x in last_paths)
            provisional_replaced = ident.startswith("PENDING-") and any(x["path"] in currentpaths for x in last_paths)
            if r.get("status") == "present" and not unavailable and not provisional_replaced:
                changes["removed"].append(ident)
            retired = r.copy()
            retired["status"] = "unverified_current_bytes" if unavailable else ("superseded_provisional" if provisional_replaced else "not_present")
            retired["previous_locations"] = retired.get("locations") or retired.get("previous_locations", [])
            retired["locations"] = []
            output.append(retired)
    output.sort(key=lambda r: r["id"])
    atomic_text(home/"catalog.jsonl", "".join(json.dumps(r, ensure_ascii=False, sort_keys=True)+"\n" for r in output))
    with (home/"search.csv").open("w", newline="") as f:
        fields = ["id", "status", "title", "categories", "keywords", "abstract_status", "paths"]
        writer = csv.DictWriter(f, fields, lineterminator="\n", quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for r in output:
            writer.writerow({"id": r["id"], "status": r["status"], "title": r["title"],
                             "categories": "; ".join(r["categories"]), "keywords": "; ".join(r["keywords"]),
                             "abstract_status": r["abstract"]["status"],
                             "paths": "; ".join(x["path"] for x in r["locations"])})
    active = [r for r in output if r["status"] == "present"]
    with (home/"REVIEW_QUEUE.csv").open("w", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["id", "title", "abstract_status", "text_status", "next_action"])
        for r in active:
            action = "verify abstract/identity on original pages" if r["abstract"]["text"] else "locate abstract or write a clearly labeled reading summary"
            if r["text_status"] == "supporting_csv_excerpt":
                action = "supporting data; verify its cited original sources"
            writer.writerow([r["id"], r["title"], r["abstract"]["status"], r["text_status"],
                             action])
    categories = collections.Counter(c for r in active for c in r["categories"])
    topics = collections.Counter(t for r in active for t in r.get("topics", []))
    category_map = "---\ntitle: Box library category map\nowner: literature writer\nstatus: maintained\nupdated: "+now[:10]+"\ntags: [project/trident, doc/index]\n---\n\n# Category routes\n\n- Generated by refresh; do not edit. Search a folder/topic, then inspect only selected IDs.\n- Counts are unique records per category; duplicates across folders can count twice. Topic tags are heuristic discovery, not scientific review.\n\n| Source folder | Records |\n|---|---:|\n"
    category_map += "\n".join("| "+c.replace("|", "\\|")+" | "+str(n)+" |" for c,n in sorted(categories.items()))
    category_map += "\n\n| Heuristic topic | Records |\n|---|---:|\n"+"\n".join("| "+t+" | "+str(n)+" |" for t,n in sorted(topics.items()))+"\n"
    atomic_text(home/"CATEGORY_MAP.md", category_map)
    report = {"root": str(root), "scan_time": now, "files": sum(len(r["locations"]) for r in active),
              "document_records": len(active), "hashed_unique_documents": sum(bool(r["sha256"]) for r in active),
              "unhashed_files": sum(len(r["locations"]) for r in active if not r["sha256"]), "duplicates_extra_copies": sum(len(r["locations"])-1 for r in active),
              "abstract_status": dict(collections.Counter(r["abstract"]["status"] for r in active)),
              "text_status": dict(collections.Counter(r["text_status"] for r in active)), "changes": changes}
    write_json(home/"LAST_SCAN.json", report)
    if any(changes.values()):
        with (home/"history.jsonl").open("a") as f:
            f.write(json.dumps({"scan_time": now, "changes": changes})+"\n")
    print(json.dumps({k:v for k,v in report.items() if k!="changes"}))
    return report

def search(home, query, limit):
    terms = query.casefold().split()
    hits = []
    for r in annotated(home):
        if r["status"] != "present":
            continue
        hay = json.dumps(r, ensure_ascii=False).casefold()
        if all(t in hay for t in terms):
            hits.append({"_rank": sum(r["title"].casefold().count(t)*5 for t in terms), "id": r["id"], "title": r.get("curation", {}).get("title", r["title"])[:220], "categories": r["categories"],
                         "keywords": r["keywords"][:10], "abstract_status": r["abstract"]["status"],
                         "existing_source_ids": r.get("curation", {}).get("existing_source_ids", []), "note_path": r.get("note_path"),
                         "paths": [x["path"] for x in r["locations"]][:1], "location_count": len(r["locations"])})
    hits.sort(key=lambda r: (-r["_rank"], r["id"]))
    for r in hits:
        r.pop("_rank")
    print(json.dumps({"total_matches": len(hits), "returned": hits[:limit]}, ensure_ascii=False, indent=2))
    return hits

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--home", type=Path, default=HOME)
    sub = p.add_subparsers(dest="cmd", required=True)
    scan = sub.add_parser("refresh"); scan.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    scan.add_argument("--reextract", action="store_true", help="Retry text intake even for unchanged hashes; curated annotations are preserved")
    find = sub.add_parser("search"); find.add_argument("query"); find.add_argument("--limit", type=int, default=8)
    show = sub.add_parser("show"); show.add_argument("id")
    note = sub.add_parser("note"); note.add_argument("id")
    internal = sub.add_parser("_extract"); internal.add_argument("path", type=Path)
    hashing = sub.add_parser("_hash"); hashing.add_argument("path", type=Path)
    a = p.parse_args()
    if a.cmd == "_hash":
        print(hash_file(a.path))
    elif a.cmd == "_extract":
        print(json.dumps(extract(a.path), ensure_ascii=False))
    elif a.cmd == "refresh":
        refresh(a.root.expanduser(), a.home, a.reextract)
    elif a.cmd == "search":
        search(a.home, a.query, max(1,min(a.limit,50)))
    elif a.cmd in ("show", "note"):
        r = next((r for r in annotated(a.home) if r["id"] == a.id), None)
        if r is None:
            p.error("Unknown ID; search first.")
        if a.cmd == "show":
            print(json.dumps(r, ensure_ascii=False, indent=2))
        else:
            folder = a.home / "notes"
            folder.mkdir(exist_ok=True)
            path = folder / (a.id+".md")
            # Exclusive creation protects existing reading notes.
            with path.open("x") as f:
                f.write("---\ntitle: Reading note "+a.id+"\nowner: literature writer\nstatus: working\nupdated: "+dt.date.today().isoformat()+"\ntags: [project/trident, doc/source]\n---\n\n# "+r["title"]+"\n\n- Catalog ID: "+a.id+"\n- Existing S/claim IDs: not yet mapped\n- Reading depth: not yet read\n- Exact source/version and pages: pending\n\n## Verified identity and abstract\n\n- Pending primary-source check.\n\n## Useful claims and exact locators\n\n- Claim; page/equation/table; conditions; limits.\n\n## Relevance to current research questions\n\n- Question/aim ID and possible use; no implied scope change.\n\n## Open questions\n\n- Pending.\n")
            print(path)
if __name__ == "__main__":
    main()
