# Strata — ancient-history corpus v1.0

**380 rounds, all forty-two chapters of Susan Wise Bauer's _The Story of the World, Volume 1: Ancient Times_,**
plus 17 further "enrichment" items outside the book itself (`tier: "C"`, held out of play
by default — `SETTINGS.includeTierC` in `index.html`).

## Files

- `index.html` — the game. Self-contained: the corpus is compiled into a `const ITEMS = [...]`
  array in the page itself, not fetched at runtime. On load it first asks which chapters
  (1–42) to draw rounds from, via a two-handle drag range over the book's table of contents
  (chapter titles are hardcoded display copy, not part of the corpus); rounds are then dealt
  only from that range, and the round count quietly caps at however many questions the chosen
  range actually has if that's fewer than `SETTINGS.roundsPerGame`.
- `sotw1_corpus.json` — the source corpus this file to edit or regenerate from. Carries a
  few extra documentation fields (`sotwTime`, `scholarlyTime`, `timeShare`, `precisionLabel`)
  that `index.html` doesn't need at runtime because they're already baked into each item's
  `time`, `timeMax`, and `placeMax`.
- `vendor/` — Leaflet 1.9.4 (self-hosted, no CDN) and `land.js`, world coastlines decoded
  from the same public-domain Natural Earth 1:50m data used by `../voyages/basemap.js`,
  rendered as a vector layer rather than raster map tiles so a round never depends on a
  live tile server. `land.js` also carries a hand-traced `RIVERS` set (Nile, Tigris,
  Euphrates, Indus, Ganges, and other major rivers) so the interior of a continent has
  some legible structure — deliberately not modern political borders.

## Schema

Each item: `{id, chapter, tier, category, difficulty, prompt, subtitle, place, time,
lambdaYears, lambdaKm, dateBasis, confidence, reveal, timeMax, placeMax}`.

`place` is `{shape: "circle", lat, lon, radiusKm, label}`, `{shape: "polygon", points, label}`,
or `{shape: "multipoint", points, radiusKm, label}` (nearest point wins). `time` is
`{start, end, timeBasis, label}`, in astronomical years (negative = BC).

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
  scholarship-only date wrong against the book or vice versa.
- **Patriarchal narratives** (Abraham, Isaac, and similar Genesis-era items) are scored on
  the later end of the proposed range, following Kenneth Kitchen's chronology
  (`config.patriarchalChronology: "kitchen-late"`), rather than the earlier dates some
  older reference works give.
- **Two Chapter 1 items reach past 7000 BC**, beyond the slider's nominal start at 9000 BC
  but still within its range.
- **Eleven items are capped at AD 500** even though their real subject runs later — an
  institution, practice, or figure's influence that continues past the ancient period this
  corpus covers. The true end date is preserved in the source corpus as `time.trueEnd`;
  the scored `time.end` stops at AD 500, where the slider ends.

## Provenance

Built for the Fabrica by an earlier Claude session, from the 1994 Susan Wise Bauer text,
cross-checked against current archaeological and historical scholarship per item
(`dateBasis`: `secure`, `conventional`, `traditional`, or `archaeological`; `confidence`:
`high`, `medium`, or `low`).
