# The Expansion of America — data

`states.json`: all 50 states, sorted by year of statehood. Each entry:

```
{postal, name, rank, year, blurb, illustration, map, flag}
```

- `rank` — 1 (most interesting) to 50 (least), as ranked in the source doc; not otherwise used.
- `blurb` — one paragraph on the state's path to statehood.
- `illustration` / `map` / `flag` — paths into `images/`: a historical illustration or portrait, a period map, and the state flag, respectively.

## Provenance

Sourced from a user-supplied doc ("State Origins Illustrated"), which paired each state with four images: a highlight map stamped with its admission year, a historical illustration, a period map, and its flag. The admission-year highlight map is **not** carried over here — the exhibit has its own interactive map for that — so each state keeps only the other three.

## Not yet built

This is data prep only. The actual visualization (`index.html`: a map you scroll through time, states/territory changing as the US grew, hover for a state's story) hasn't been built yet.
