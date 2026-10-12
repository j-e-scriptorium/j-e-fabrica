# Register of judgment calls

A judgment call is any step where the record does not decide the matter and we did. They fall into eleven classes below.

- Each class gives the decision, the reason, how many records it touches, how to find them, and what changes if it is wrong.
- Record-level judgments are flagged in `data/records.csv` (`judgment_flags`). The flags are assigned automatically from each record's text by `provenance.py`, so they are a finding aid, not a verdict; read the `source_says` column.
- The page's own table of choices, with measured effects, is in the “About the data” section of the map page under "Every extrapolation choice".

## 1. What counts as a unit

| Decision | Reason | Where |
|---|---|---|
| Fit 55 divisions, not 31 tribes or ~300 bands | Divisions are the level at which the sources most often count people. | `groups.csv` |
| Splits dated to a year: Cheyenne 1832, Arapaho 1835; Missouria merge into Oto 1830; Cuartelejo and Paloma Apache end 1732 (absorbed by the Jicarilla, after Gunnerson) | A year is needed for the fit. The splits were gradual over a decade or more. | `groups.csv` start/end |
| Arkansas Osage (Claremore's band) a separate division, 1802–39 | Pike and Clark count it separately. | `osa` |
| Two names Clark recorded but which cannot be identified (Castahana, Dotame) kept as evidence only. Two others once kept apart ("Staitan", "Nemousin") folded into the Arapaho. | Parks, "Enigmatic Groups", Handbook 13, pp. 972–73: probable identifications only. | records with group `u_cas`, `u_dot`; Arapaho 1805 |

## 2. Who a record is about (21 records flagged `identification_judged`)

These are the identifications that most affect tracks.

- Henday's "Archithinue" camp of 1754 (placed with the Siksika) and his "Asinepoets" (Assiniboine).
- Bourgmont's 1724 Padouca, and Vermale's 1717 Padouca villages, both taken as Plains Apache. Both are contested; some writers take Padouca as Comanche after about 1750.
- Long's 1820 Kaskaia, as Plains Apache after Parks; kept off the track.
- Peter Pond's 1775 "Yankton" as Yanktonai.
- Ulibarrí's 1706 "probably Jicarilla" bands.
- Cocking's Pegogamaw Cree, filed with the Fort des Prairies division; kept off the track.

**If wrong:** the track of the named division moves by up to several hundred km for the decade around the record.

## 3. Turning counts into persons

| Decision | Records |
|---|---|
| A source's own persons-per-lodge or per-warrior ratio where it states one | 32 (`multiplier_stated_by_source`) |
| Our ratio otherwise: lodges × 5, warriors × 4, earth lodges × 10 (Thompson's ratio is 8–10) | 75 (`multiplier_ours`) |
| Clark 1805: the lower of his two figures | ~40 Clark records |
| Same-year counts of parts of one division are summed to a division total | see `summed_with_same_year_records` |
| A range ("1,000–1,500 families") taken at its midpoint | noted in `source_says` |

**If wrong:** sensitivity runs move totals by about 1% for ±1 person per lodge (the “About the data” section of the map page, Sensitivity).

## 4. Where a record is put

| Decision | Records |
|---|---|
| A count whose source gives no usable place is placed by us (`place_status = inferred`) and **never steers a track** | 419 |
| A stated place is geocoded by us, with a radius `place_radius_km` for its vagueness | all `stated` records |
| A range ("between the Platte and the Arkansas") is placed at its centre; its radius is kept as uncertainty | 34 (`place_centre_ours`) |
| Wikipedia's coordinates for battle, treaty, agency and site articles are used as given | ~110 records, tier B |
| A date derived from context (a narrator's age, "mid-18th century", an archaeological span) | 5 (`date_ours`) |

## 5. Which records steer a division's track

674 records steer a track. Of the rest, 112 are deliberately kept off (`steers_track = no`, `kept_off_track` flag). The reasons follow.

- **A part of the division.** A band, a chief's following, a camp holding part of the people (Crazy Horse's following, 1876–77; Cocking's Pegogamaw, 1772–73).
- **A visit, delegation, council attendance or war party.** San Sabá 1758, the Council House Fight 1840, Shoshone at Horse Creek 1851. These say where some men were for days.
- **A seasonal hunt camp of a village people.** 15 records.
- **A range or tradition that conflicts with a precisely dated place nearby.** These four were removed after a visual and numerical audit of the tracks:
  - Saukamappee's Shoshone camp, about 1730, which put the Shoshone north of every Blackfoot division;
  - the Cheyenne "1760–1850" Black Hills union, pinned to 1780 against Truteau's Missouri location in 1795;
  - the 1851 treaty range for the Northern Arapaho;
  - Hayden's general 1860 Arapaho range, against the dated 1859–60 Powder River winter camp.

**If wrong:** keeping a partial record off the track hides real movement; putting it on drags the whole division to a minority's location. The audit criterion is in `REVIEW_PROTOCOL.md` §4.

## 6. Our keyframes (`keyframes_our_guesses.csv`)

- **What they are.** 489 guesses: 400 give both place and persons, 74 persons only, 10 place only, and 5 only mark an event.
- **What backs them.**
  - 247 carry a note, often naming the event or source behind them: "Treaty 6", "Whetstone agency, 1869–71", "1780–81 smallpox".
  - 242 carry none. Their basis is interpolation between neighbouring documented states, judged by eye against the record.
- **Weight.** Persons at ±30% (σ 0.3 in log); places at ±150 km.
- **When they give way.** A keyframe place within a year of a documented place is dropped. Keyframe persons are excluded when estimating source-family factors.
- **Where they matter most.**
  - Before 1780, where six divisions have no count at all.
  - The northern plains before 1790.
  - The Plains Cree and Plains Ojibwe throughout, where Canadian treaty-era counts were not read.
- **Effect of removing all of them.** The 1780 total falls by about 8%, the 1850 total by 6%, held-out population error worsens from 1.21 to 1.26, and held-out place error for the drawn nomadic track worsens from 115 to 128 km (the smoother that sets the halo barely moves, 113 → 115 km).

## 7. Epidemics and famines (`epidemics_and_shocks.csv`)

- **What is applied.** 22 events, 212 event × division rows.
- **What is sourced.** Dates and the existence of each event are sourced. Rates are sourced for some divisions per event and scaled or assumed for the rest; the `rate_basis` field of each event says which.
- **The assumed rates that matter most.**
  - The 1780–82 smallpox at the edges of its documented range.
  - The 1801–02 smallpox except for the Omaha.
  - The 1839–40 southern smallpox (assumed below Mooney's "third").
  - The 1849 cholera except for the Kiowa and Cheyenne.
  - The 1848 Comanche smallpox: the event comes from Hämäläinen via a reader's highlight (tier C); the 20% rate is ours.
- **Events deliberately not modelled.** Grinnell's 1845 Blackfoot smallpox, which no other source read here gives (probably a misdating of 1837).
- **If wrong.** This is the most influential assumption before 1800: ±25% on every rate moves the 1780 total between 135,000 and 179,000.

## 8. Source-family factors

The factors are estimated by the model, not set by hand, but the grouping of sources into families is ours (`family()` in `build3.py`). Reservation censuses are fixed as the reference; every other family's counts are scaled toward them.

The estimated factors run from 0.60 (Henry 1809, counting men in his trading district) to 1.18 ("other sources"). Morse 1820 comes out about 11% high and Clark about 11% low.

**If wrong:** a family biased in the same direction as the censuses (for example, agents inflating ration rolls before 1880) would go uncorrected. See `KNOWN_ISSUES.md` §5.

## 9. Seasonal round

- **The literature patterns.** 28 rows in `seasonal_patterns.csv`, all with sources **recalled, not reread for this build**. Examples: Ray and Moodie for the Cree and Assiniboine; Ewers for the Blackfoot; West for the Cheyenne and Arapaho at the Big Timbers.
- **What they control.** They set the direction of the summer move wherever a division has no season-dated places of its own.
- **The calendar.** The months of the move were chosen among statistically tied candidates by closeness to the ethnographic year.
- **Two fitted patterns rejected because they worsened held-out error:**
  - a Kiowa and Plains Apache winter ground on the North Fork of the Red;
  - a Teton round along the Missouri.

## 10. Bands and villages

- **Names.** Documented, from one list per division (Dorsey, Grinnell, Denig, Hayden, Wissler, Kroeber, Lowie, Skinner).
- **Ours.**
  - band weights;
  - budding order before the list year;
  - the matching of lists to each other (Hayden's c. 1856 bands to Dorsey's; Denig's Crow chiefs to Lowie's divisions; Skinner's Cree bands to our three divisions);
  - most band positions.
- **Band places.** 198 rows in `band_places_recalled.csv`, **recalled from standard histories, not checked entry by entry**, except where a record in `records.csv` gives the place.
- **Status.** Treat the band layer as illustration constrained by division totals, not as evidence.

## 11. Contested figures and how each was resolved

The full list is in the “About the data” section of the map page, "Where the sources disagree". These are the calls a reviewer is most likely to challenge.

- **Comanche, 1840s.** Six figures of 14,300–20,000 (1843–49) against about 1,500 counted on the reservation from 1875.
  - **Resolution.** The fit gives about 12,000 in 1840 and about 10,000 by 1846.
  - **Reason.** Accepting 17,000–20,000 implies a 90% loss in 30 years, against 0–45% for the Kiowa, Cheyenne and Arapaho, who shared the same epidemics, wars and bison collapse.
  - **Status.** Hämäläinen (2008) accepts the high figure. **Open.**
- **Mandan and Arikara, 1780.** Mooney's reconstructions are far below the village counts; kept as soft constraints.
- **Hidatsa, 1838.** Hayden's "forty lodges" against later rolls; unresolved, fit in between.
- **Arikara, 1871–78.** Hodge's 1,650 against the Fort Berthold roll of 654; irreconcilable, fit splits them.
- **Arapaho, 1820.** Bell's "10,000" excluded as a mixed-camp count.
- **Kiowa, 1854.** Whitfield's 2,800 treated as an overestimate against Mooney's series.
- **Blackfoot, 1809.** Henry's tents give half of Umfreville's 1789 figures; both kept, and Henry's family factor (0.60) absorbs the difference.
