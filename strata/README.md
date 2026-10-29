# Strata — ancient-history corpus v1.0

**363 rounds from all forty-two chapters of Susan Wise Bauer's _The Story of the World, Volume 1: Ancient Times_,**
plus 17 further "enrichment" items outside the book itself (`tier: "C"`, held out of play
by default — `SETTINGS.includeTierC` in `index.html`): 380 items in all.

## Files

- `index.html` — the game. Self-contained: the corpus is compiled into a `const ITEMS = [...]`
  array in the page itself, not fetched at runtime. On load it first asks which chapters
  (1–42) to draw rounds from, via a two-handle drag range over the book's table of contents
  (chapter titles are hardcoded display copy, not part of the corpus); rounds are then dealt
  only from that range, and the round count quietly caps at however many questions the chosen
  range actually has if that's fewer than `SETTINGS.roundsPerGame`. The browser remembers
  which items have been played (`localStorage`, key `strata.seen`) and deals unseen ones
  first; when a chapter range runs out of unseen items, its slate is wiped and the cycle
  starts again.
- `sotw1_corpus.json` — the source corpus, and the only place to edit items. Carries a
  few extra documentation fields (`sotwTime`, `scholarlyTime`, `timeShare`, `precisionLabel`,
  and some editorial notes) that `index.html` doesn't need at runtime because they're
  already baked into each item's `time`, `timeMax`, and `placeMax`.
- `build.py` — checks the corpus against the rules below and compiles it into the
  `ITEMS` line of `index.html`. After any corpus edit, run `python3 strata/build.py`; it
  refuses to write, and names the offending items, if a window misses the book's or the
  scholarly date, a label disagrees with its window's width, a split doesn't total 5,000,
  and so on.
- `vendor/` — Leaflet 1.9.4 (self-hosted, no CDN) and `land.js`, which just turns the
  shared map data in `../../assets/worldmap.js` into GeoJSON (`landGeoJSON()`,
  `riversGeoJSON()`, `lakesGeoJSON()`) for Leaflet to render as a vector layer, so a
  round never depends on a live tile server. The actual data — coastlines, rivers,
  and lakes, all public-domain Natural Earth 1:50m (`ne_50m_land`,
  `ne_50m_rivers_lake_centerlines`, `ne_50m_lakes`), pulled from the project's own
  GitHub mirror rather than hand-traced, so a river or lake is the same source and
  point density as the coast it meets — lives in that one shared file rather than a
  copy here, so it stays in sync with `../voyages/` automatically instead of by
  hand. The rivers and lakes exist so the interior of a continent has some legible
  structure — deliberately not modern political borders.
  `countries.js` holds modern country names at Natural Earth 1:50m admin-0 label points
  (`COUNTRY_LABELS`, each with the lowest zoom at which it shows), overlaid on the map only
  after a guess is submitted, so the answer can be read against today's map without the
  borders prompting the guess itself.

## Schema

Each item: `{id, chapter, tier, category, difficulty, prompt, subtitle, place, time,
lambdaYears, lambdaKm, dateBasis, confidence, reveal, timeMax, placeMax}`.

`place` is `{shape: "circle", lat, lon, radiusKm, label}`, `{shape: "polygon", points, label}`,
or `{shape: "multipoint", points, radiusKm, label}` (nearest point wins). `time` is
`{start, end, timeBasis, label}`, in historians' years: negative = BC, and there is no year
0 (−44 is 44 BC; 1 BC is followed by AD 1). The slider steps straight across the gap, and
a miss that straddles it is counted one year shorter.

## Scoring

A round is worth `timeMax + placeMax`, always 5,000. Score decays exponentially outside the
true window or shape: `max * exp(-distanceOutside / lambda)`, `lambda` set per item
(`lambdaYears`, `lambdaKm`) to roughly how forgiving that item's dating or geography should be.

**The 5,000-point split is not fixed.** It follows `timeShare` in the source corpus — how
precisely the item can be dated, narrowest window first (year → decade → reign/lifetime →
century → few centuries → "known only as a long era"). An item securely dated to the year
puts most of its weight on time; an item known only as a long era puts almost all of it on
place, since no guess will narrow a millennia-wide window. The in-game precision bar shows
this split before you answer.

## Chronology quirks

- **Where the book's traditional dating and current scholarship disagree, the scored
  window is the union of both** (`sotwTime` and `scholarlyTime` record each separately in
  the source corpus) — so knowing either gets full credit, rather than marking a
  scholarship-only date wrong against the book or vice versa. One deliberate exception: the
  standard Babylonian _Epic of Gilgamesh_ is scored on that version's composition
  (1300–1100 BC), not on the book's 3000–1200 BC, which spans the whole Gilgamesh
  tradition rather than this text; `build.py` lists it in `UNION_EXCEPTIONS`.
- **Patriarchal narratives** (Abraham, Isaac, and similar Genesis-era items) are scored on
  the later end of the proposed range, following Kenneth Kitchen's chronology
  (`config.patriarchalChronology: "kitchen-late"`), rather than the earlier dates some
  older reference works give.
- **Two Chapter 1 items reach back past 7000 BC** — Jericho's walls and the first nomads —
  the latter all the way to the slider's 9000 BC floor.
- **Eleven items are capped at AD 500** even though their real subject runs later — an
  institution, practice, or figure's influence that continues past the ancient period this
  corpus covers. The true end date is preserved in the source corpus as `time.trueEnd`;
  the scored `time.end` stops at AD 500, where the slider ends.

## Provenance

Built for the Fabrica by an earlier Claude session, from the 1994 Susan Wise Bauer text,
cross-checked against current archaeological and historical scholarship per item
(`dateBasis`: `secure`, `conventional`, `traditional`, or `archaeological`; `confidence`:
`high`, `medium`, or `low`).
