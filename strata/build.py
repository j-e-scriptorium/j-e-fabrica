#!/usr/bin/env python3
"""Check sotw1_corpus.json and compile it into the ITEMS array in index.html.

Run from anywhere:  python3 strata/build.py
Edit the corpus, never the ITEMS line by hand. The script refuses to write
if any item breaks one of the corpus's own rules, and says which.
"""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CORPUS, PAGE = HERE / "sotw1_corpus.json", HERE / "index.html"

# Fields index.html reads at runtime; everything else in the corpus is
# documentation (sotwTime, scholarlyTime, timeShare, editorial notes, ...).
RUNTIME = ["id", "chapter", "tier", "category", "difficulty", "prompt", "subtitle",
           "place", "time", "lambdaYears", "lambdaKm", "dateBasis", "confidence",
           "reveal", "timeMax", "placeMax"]

# Must match COPY.precisionLabels in index.html: the in-game label is computed
# from the width of the time window, so the corpus label has to agree with it.
PRECISION = [(5, "dated to the year"), (30, "dated to the decade"),
             (90, "dated to a reign or lifetime"), (250, "dated to about a century"),
             (600, "dated to a few centuries"), (None, "known only as a long era")]

# Deliberate exceptions to the union-of-book-and-scholarship rule.
UNION_EXCEPTIONS = {"c08-standard-epic"}

MIN_YEAR, MAX_YEAR, ROUND = -9000, 500, 5000


def precision(span):
    return next(t for u, t in PRECISION if u is None or span <= u)


def check(items):
    errs, seen = [], set()
    for it in items:
        i, t, p = it["id"], it["time"], it["place"]
        def bad(msg): errs.append(f"{i}: {msg}")
        if i in seen: bad("duplicate id")
        seen.add(i)
        for k in RUNTIME:
            if k not in it: bad(f"missing {k}")
        if it["timeMax"] + it["placeMax"] != ROUND: bad(f"timeMax + placeMax != {ROUND}")
        if t["start"] > t["end"]: bad("time.start after time.end")
        if t["start"] < MIN_YEAR or t["end"] > MAX_YEAR: bad("time window off the slider")
        if 0 in (t["start"], t["end"]): bad("year 0 does not exist (1 BC is -1, AD 1 is 1)")
        want = precision(t["end"] - t["start"])
        if it.get("precisionLabel") != want: bad(f"precisionLabel should be '{want}'")
        if i not in UNION_EXCEPTIONS:
            for k in ("sotwTime", "scholarlyTime"):
                s = it.get(k)
                if s and (s["start"] < t["start"] or min(s["end"], MAX_YEAR) > t["end"]):
                    bad(f"time window does not contain {k}")
        if p["shape"] == "circle":
            if not (-90 <= p["lat"] <= 90 and -180 <= p["lon"] <= 180): bad("circle centre off the globe")
        elif p["shape"] in ("polygon", "multipoint"):
            if len(p["points"]) < (3 if p["shape"] == "polygon" else 1): bad(f"too few {p['shape']} points")
        else:
            bad(f"unknown place shape {p['shape']}")
    return errs


def main():
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    items = corpus["items"]
    errs = check(items)
    if corpus.get("count") != len(items):
        errs.append(f"corpus count says {corpus.get('count')}, has {len(items)}")
    if errs:
        sys.exit("Not built:\n  " + "\n  ".join(errs))
    compiled = json.dumps([{k: it[k] for k in RUNTIME} for it in items],
                          separators=(",", ":"), ensure_ascii=False)
    page = PAGE.read_text(encoding="utf-8")
    page, n = re.subn(r"^const ITEMS = \[.*\];$", lambda _: f"const ITEMS = {compiled};",
                      page, count=1, flags=re.M)
    if n != 1:
        sys.exit("Not built: no 'const ITEMS = [...];' line in index.html")
    PAGE.write_text(page, encoding="utf-8")
    playable = sum(it["tier"] != "C" for it in items)
    print(f"Built {len(items)} items ({playable} in play, {len(items) - playable} tier C).")


if __name__ == "__main__":
    main()
