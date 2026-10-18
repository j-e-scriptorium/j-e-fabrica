# Review protocol

These checks are ordered from most to least decisive. A reviewer with library access should do §1 first; a reviewer without it, human or LLM, can still do §§2–6 from this package alone. Each check says what a pass and a fail look like and how to report.

## 1. Do the records say what their sources say?

This is the check the package cannot do for itself.

**Sample.** `data/review_sample.csv` holds 80 records drawn at random with a fixed seed, stratified by tier: 25 A1, 30 A2, 15 B, 10 C, about half counts and half places. Add all 22 tier-C records from `records.csv` (`provenance_tier = C`), since those were never read here.

For each record, find the cited page or entry and fill `reviewer_verdict`:
- `confirmed`: the source says what `source_says` reports, for the people, year and place given;
- `wrong number`, `wrong place`, `wrong date`;
- `not in source`;
- `source not available`.

Check four things in each record:
- the persons figure and its basis (souls, lodges, warriors), including whether the multiplier is the source's;
- the people and division;
- the year (a season sets the decimal: winter ≈ .9–.1, summer ≈ .5);
- whether the geocoded point (`lat`, `lon`) lies within `place_radius_km` of what the source describes.

**Pass.**
- At most 2 of the 55 A-tier records wrong in any respect, and none wrong by more than a factor of 1.5 in persons or 100 km in place.
- Tier B: the coordinates match the article.
- Tier C: no expectation; report what you find.

**Fail.** Three or more A-tier errors, or any fabricated record (`not in source` where the source is available). Either one means the whole record set needs re-verification, not just the sample.

**Report.** The filled CSV and a count by tier and verdict.

**For an LLM reviewer without the sources.** Do not guess verdicts. You can still check:
- internal consistency of each sampled record: the quote supports the persons figure and basis, and the place described matches the coordinates;
- consistency with what you reliably know, marked as such;
- duplicate records (one observation entered twice under different sources).

## 2. Do the judgment calls hold up?

Read `JUDGMENTS.md`. For each class, decide whether the decision is defensible, and whether a specialist would choose differently.

Specific questions a Plains ethnohistorian is best placed to answer:

1. Is the 66-division scheme right for the 18th century? The Teton are undivided to 1785 and the Saone to 1806; should the Yanktonai and Blackfoot be undivided too before their divisions are first attested, and are the Teton dates right (`KNOWN_ISSUES.md` §10)?
2. Are the Padouca of 1717 and 1724 Plains Apache, as assumed here?
3. Is the low Comanche reading of the 1840s (≈10,000–12,000) more defensible than Hämäläinen's 20,000 (`KNOWN_ISSUES.md` §1)?
4. Which assumed epidemic rates (`epidemics_and_shocks.csv`, basis "assumed" or "scaled") are most out of line with the literature?
5. Are the seasonal-round directions in `seasonal_patterns.csv` correct for each people? Most are page-cited; those without a page (Milloy for the Qu'Appelle Cree after 1830 and the Cypress Hills Cree, Ross, Pond) were recalled, not reread.
6. Are any of the 508 keyframes (`keyframes_our_guesses.csv`) clearly wrong? Look especially at the 227 with no note, and at places before 1790.
7. Is any people or division missing that should be on a map of this scope? Candidates include the Plains Ojibwe before 1780, the Caddo, the Quapaw and the Plains Métis. The Sarsi, Stoney, Tonkawa and Kitsai are on the map.

## 3. Does the model reproduce, and do its tests hold?

From `model/src`:

```
python3 build3.py . ..        # must reproduce data/fitted_population_by_division.csv exactly
python3 validate.py . ..      # leave-one-out: expect median factor ≈ 1.11, 2-sd coverage ≈ 0.92
python3 calib_gp.py . ..      # expect out of sample a median ≈ 119 km, mean ≈ 147 on 660 places; halo coverage ≈ 0.68 per season
python3 audit.py ..           # expect the list in docs/audit.txt
```

**Pass.** The numbers match the Reliability section of `README.md` to the stated precision.

**Fail.** Any mismatch: report the command and output.

Then probe the model with your own changes. Useful probes:
- set `NOGUESS=1` to drop all keyframes;
- set `EPS=0.75` or `EPS=1.25` to scale every epidemic rate;
- set `SR=0.12` to loosen the growth prior, which is what lets the 1840s Comanche counts be honoured;
- remove a source family by editing `family()` in `build3.py`.

Read `model/build/sensitivity.json` for the probes already run.

## 4. Does the map make sense when you watch it?

Open `index.html` (served over http). With "Best guess" and "Divisions" selected, step through every decade, then look for the following.

- **Zigzags.** A division jumping hundreds of km and back within a few years. `docs/audit.txt` §1 lists every pair of anchors less than 1.5 years and more than 200 km apart. Most are real (Kiowa sun dances, battles, removals to Indian Territory); judge the rest.
- **Long straight runs.** These are moves across 300 km or more with no anchor in between. `audit.txt` §2 lists them, and each is interpolation.
- **Wrong neighbours.** One people placed on the wrong side of another. Examples fixed during building:
  - the Shoshone north of the Blackfoot around 1730;
  - the Cheyenne in the Black Hills in 1780.
- **Populations that move without cause.** `audit.txt` §3 lists any year-on-year change beyond −15% or +8% that no shock, split or merger explains. The one run it lists is the Sarsi rise of 1874–80, between the Treaty 7 roll of 1877 and the pay-sheets of 1880–81 (`KNOWN_ISSUES.md` §12).
- **Off the herds.** `audit.txt` §5 lists the years a nomadic division's centre lies outside the bison range before its reservation. Most are within about 160 km of the range's edge as it shrank; judge whether any is a track error.
- **Evidence-only view.** Do the records cluster where the best guess puts each people?


## 5. Are the reported uncertainties honest?

**Population.**
- `data/validation.csv` gives, for each count, the leave-one-out prediction and standardized miss.
- After the 25% widening, 95% of |z| should be ≤ 2.5; the package gives 96%, and 80% ≤ 1.25, because the misses are heavier-tailed than normal.
- Check this by period and by people. If one people's misses all run one way, its fit is biased, not merely noisy.

**Place.** The nomadic halo is calibrated to contain 68% of withheld places in each season. The village halo is fitted to hold 68% of withheld village places, unevenly across strata (`KNOWN_ISSUES.md` §7).

**Coverage.** Cross `coverage_by_division_and_period.csv` with the halo and SD columns. Uncertainty should be largest where the flag is `thin`. If it is not, the model is overconfident there.

## 6. Verdict

Report one line per layer, each with the evidence for it.

| Layer | Verdict scale |
|---|---|
| Documented records (evidence view) | reliable / reliable with listed errors / unreliable |
| Population, 1700–1799 | usable as order of magnitude / usable with stated ranges / not usable |
| Population, 1800–1905 | same |
| Positions, nomadic | same |
| Positions, villages | same |
| Seasonal round | same |
| Bands and villages | illustrative only / better than illustrative |

Also list the three findings that would most change the map if acted on.
