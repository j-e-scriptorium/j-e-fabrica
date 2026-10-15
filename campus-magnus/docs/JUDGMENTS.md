# Register of judgment calls

A judgment call is any step where the record does not decide the matter and we did. They fall into eleven classes below.

- Each class gives the decision, the reason, how many records it touches, how to find them, and what changes if it is wrong.
- Record-level judgments are flagged in `data/records.csv` (`judgment_flags`). The flags are assigned automatically from each record's text by `provenance.py`, so they are a finding aid, not a verdict; read the `source_says` column.
- The page's own table of choices, with measured effects, is in the “About the data” section of the map page under "Every extrapolation choice".

## 1. What counts as a unit

| Decision | Reason | Where |
|---|---|---|
| Fit 59 divisions, not 34 peoples or ~300 bands | Divisions are the level at which the sources most often count people. | `groups.csv` |
| Splits dated to a year: Cheyenne 1832, Arapaho 1835; Missouria merge into Oto 1830; Cuartelejo and Paloma Apache end 1732 (absorbed by the Jicarilla, after Gunnerson, and by the Lipan, after Hämäläinen, p. 48); Kitsai end 1894 (merged into the Wichita, after Parks); the Stoney drawn as the Mountain Stoney only | A year is needed for the fit. The splits were gradual over a decade or more. | `groups.csv` start/end |
| Splits and mergers carry people across: the new division's share leaves its parent, and an ending division's people join the survivor (`division_transfers.csv`). The eastern Comanche from the Kotsoteka 1745, the Tenewa from the Yamparika 1830, the Kwahadi from the Kotsoteka 1858; the Jupe into the Yamparika 1795; the Cypress Hills Cree from the other Plains Cree 1790; the Arkansas Osage out in 1802 and back in 1839; the Missouria into the Oto 1830; the Cuartelejo and Paloma Apache half to the Jicarilla, half to the Lipan 1732; the Kitsai into the Wichita 1894; the Two Kettle from the Miniconjou 1833; the River and Mountain Crow counted together from 1885 | Without them a people's total jumps when a division appears or vanishes | `data_src.SHIFTS` |
| Arkansas Osage (Claremore's band) a separate division, 1802–39 | Pike and Clark count it separately. | `osa` |
| Two names Clark recorded but which cannot be identified (Castahana, Dotame) kept as evidence only. Two others once kept apart ("Staitan", "Nemousin") folded into the Arapaho. | Parks, "Enigmatic Groups", Handbook 13, pp. 972–73: probable identifications only. | records with group `u_cas`, `u_dot`; Arapaho 1805 |

## 2. Who a record is about (24 records flagged `identification_judged`)

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
| A source's own persons-per-lodge or per-warrior ratio where it states one | 33 (`multiplier_stated_by_source`) |
| Our ratio otherwise: lodges × 5, warriors × 4, earth lodges × 10 (Thompson's ratio is 8–10) | 84 (`multiplier_ours`) |
| Clark 1805: the lower of his two figures | ~40 Clark records |
| Same-year counts of parts of one division are summed to a division total | see `summed_with_same_year_records` |
| A range ("1,000–1,500 families") taken at its midpoint | noted in `source_says` |

**If wrong:** sensitivity runs move totals by about 1% for ±1 person per lodge (the “About the data” section of the map page, Sensitivity).

## 4. Where a record is put

| Decision | Records |
|---|---|
| A count whose source gives no usable place is placed by us (`place_status = inferred`) and **never steers a track** | 467 |
| A stated place is geocoded by us, with a radius `place_radius_km` for its vagueness | all `stated` records |
| A range ("between the Platte and the Arkansas") is placed at its centre; its radius is kept as uncertainty | 42 (`place_centre_ours`) |
| Wikipedia's coordinates for battle, treaty, agency and site articles are used as given | ~110 records, tier B |
| A date derived from context (a narrator's age, "mid-18th century", an archaeological span) | 5 (`date_ours`) |

## 5. Which records steer a division's track

795 records inform a track, each as a noisy sighting of the division's centre rather than a point it must pass through (`METHODS.md` §3). Another 282 places are drawn but kept off (`steers_track = no`): camps, councils and visits of part of a division. The reasons follow.

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

- **What they are.** 519 guesses: 425 give both place and persons, 79 persons only, 10 place only, and 5 only mark an event.
- **What backs them.**
  - 269 carry a note, often naming the event or source behind them: "Treaty 6", "Whetstone agency, 1869–71", "1780–81 smallpox".
  - 250 carry none. Their basis is interpolation between neighbouring documented states, judged by eye against the record.
- **Weight.** Persons at ±30% (σ 0.3 in log); places at ±150 km.
- **When they give way.** A keyframe place within a year of a documented place is dropped. Keyframe persons are excluded when estimating source-family factors.
- **Where they matter most.**
  - Before 1780, where six divisions have no count at all.
  - The northern plains before 1790.
  - The Plains Cree and Plains Ojibwe throughout, where Canadian treaty-era counts were not read.
- **Effect of removing all of them.** The 1780 total falls by about 2%, the 1850 total by 3%, held-out population error barely moves (1.112 to 1.111, sensitivity runs), and held-out place error for the nomadic centre worsens from 109 to 111 km.

## 7. Epidemics and famines (`epidemics_and_shocks.csv`)

- **What is applied.** 31 events, 235 event × division rows.
- **What is sourced.** Dates and the existence of each event are sourced. Rates are sourced for some divisions per event and scaled or assumed for the rest; the `rate_basis` field of each event says which.
- **The assumed rates that matter most.**
  - The 1780–82 smallpox for the Sioux, Cheyenne, Arapaho, Kiowa and western Comanche (20–30%, set just above Fenn's minimum for the Sioux) and at the edges of its range. The north, the Missouri villages, the Lipan and the eastern Comanche are sourced from Fenn (2001), read in full.
  - The 1801–02 smallpox except for the Omaha.
  - The 1839–40 southern smallpox (assumed below Mooney's "third").
  - The 1849 cholera except for the Kiowa and Cheyenne.
  - The Comanche losses of 1848–49 (5% a year, against a contemporary report of 300 deaths), 1850–60 (drought and famine, 35%), the early 1860s (40%), 1871–73 (15%) and 1874–75 (30%): the events are from Hämäläinen and Kavanagh, read in full; the rates are ours, scaled to the counts.
  - The Sarsi and Stoney in 1780–82 and the Stoney in 1837–38, at their neighbours' rates.
- **Events deliberately not modelled.** Grinnell's 1845 Blackfoot smallpox, which no other source read here gives (probably a misdating of 1837).
- **If wrong.** This is the most influential assumption before 1800: ±25% on every rate moves the 1780 total between 136,000 and 185,000.

## 8. Source-family factors

The factors are estimated by the model, not set by hand, but the grouping of sources into families is ours (`family()` in `build3.py`). Reservation censuses are fixed as the reference; every other family's counts are scaled toward them.

The estimated factors run from 0.60 (Henry 1809, counting men in his trading district) to 1.19 ("other sources"). The catch-all family holds most counts cited from the Handbook chapters, so it scales down every people whose figures come mainly from there, including the four peoples added from Handbook 13. Morse 1820 comes out about 11% high and Clark about 11% low.

**If wrong:** a family biased in the same direction as the censuses (for example, agents inflating ration rolls before 1880) would go uncorrected. See `KNOWN_ISSUES.md` §5.

## 9. Seasonal round

- **The literature patterns.** Rows in `seasonal_patterns.csv`, each with its source and page.
  - The Southern Cheyenne and Arapaho: West, *The Contested Plains*, chs. 4 and 11, and Wedel and Frison in Handbook 13. Winter at the Big Timbers of the Arkansas; summer hunts between the Arkansas and the Smoky Hill.
  - The Piegan: Ewers, *The Horse in Blackfoot Indian Culture*, pp. 41, 125–28. Winters on the Sun and Teton about 1833 and on the Marias from about 1848; summer gatherings at the Sweetgrass Hills.
  - The eighteenth-century Archithinue (Blackfoot or Gros Ventre), Saskatchewan Assiniboine and Fort des Prairies Cree: Henday 1754–55 and Cocking 1772–73.
  - The Sarsi: Jenness, pp. 11–12; the direction and distance are ours.
  - The Comanche after 1840: the Texas Indian Papers. The Penateka wintered on the Clear Fork and in the upper Cross Timbers; the northern bands summered by the Arkansas, which Kavanagh's sources of 1851–53 confirm (*Comanche Political History*, pp. 332, 343–44, 348).
  - The Kiowa, 1830–70: Levy, Handbook 13, p. 908, and Kavanagh's sources of 1851–53. Winter camps on the Red River and Washita; spring and summer on the Arkansas, following the herds north.
  - The River Crow after about 1849: Denig, BAE 46, p. 404, "the Crows winter with the Assiniboin", near Fort Union.
  - The Yankton: DeMallie, Handbook 13, pp. 777, 789. Gardens at village sites on the Missouri, "largely abandon[ed] … during the summer buffalo hunts" west of the Missouri on the Niobrara and White.
  - The Siksika, the Plains Cree of the 1790s and the Plains Ojibwe: Handbook 13.
  - **Recalled, not reread for this build:** Ray and Moodie for the nineteenth-century Cree and Assiniboine; Hoxie for the Crow before 1849; Stamm for the Shoshone; Pond for the Sisseton and Wahpeton.
- **Where the sources disagree, no pattern.**
  - The western Comanche divisions before 1830. Hämäläinen has the upper Arkansas as their winter ground and trade-fair site (pp. 164, 284–85). Trimble in 1818 and the sources of 1851–53 that Kavanagh quotes put them on the Arkansas in spring and summer and on the Red River in winter. Kavanagh himself finds that the eighteenth-century documents "do not indicate that the Comanche pattern followed seasonal changes" (p. 55).
  - The Kotsoteka before 1850 and the eastern Comanche before 1840, for the same reason.
  - The Yanktonai. Their villages and hunts ran in different directions in different bands.
- **Weight.** Each pattern enters at half its stated distance, as a starting point the division's season-dated places correct; the whole distance did worse out of sample.
- **What they control.** They set the direction of the summer move wherever a division has no season-dated places of its own.
- **The calendar.** The months of the move were chosen among statistically tied candidates by closeness to the ethnographic year. It times the literature patterns and the bands' scatter, not the pattern learned from the records.
- **Undated camps.** A camp with no month is weighted by the seasons of the dated records, not assigned a season.
- **Not adopted.** Pooling the seasonal move across the divisions of a people: the Lakota divisions' moves ran in different directions.
- **Patterns rejected because they worsened held-out error:**
  - a Kiowa and Plains Apache winter ground on the North Fork of the Red;
  - a Teton round along the Missouri;
  - for the Blood after 1800, Dempsey's Blackfoot round (Handbook 13, p. 609: winters at the Porcupine Hills and the Belly–Saint Mary confluence, early summer near the Cypress Hills), which raised the mean miss on three withheld Blood places from 58 to 89 km;
  - for the Yamparika and the Tenewa and Nokoni, 1830–49, the winter-south, summer-north swing of the 1850s carried back two decades;
  - for the eastern Comanche, 1750–1839, Hämäläinen's winter villages on the Brazos, Colorado and Concho with summer assemblies by the Wichita Mountains (pp. 276, 284–86).

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

- **Comanche, 1819–54.** Burnet's 10,000–12,000 (written from memory in 1847), Butler and Lewis's 12,500–15,600 and Butler and Davis's 14,300 (1846), round figures of 19,200–20,000 (1838–49) from Texas, and Parker's 10,000 (1854).
  - **Resolution.** The fit gives about 10,600 in 1846 and 8,000 in 1854. Burnet is weighted as a reconstruction, Butler and Lewis and the round figures as contemporary estimates.
  - **Reason.** Kavanagh's *Comanche Political History* shows how each figure was made: Butler and Lewis divide the nation into six divisions in lodges, but Kavanagh calls the list unreliable; the 20,000 figures are hearsay or describe only the Comanches known to Texans.
  - **Status.** Hämäläinen (2008) accepts 20,000; nothing in the counts supports it. Closed unless new counts appear.
- **Mandan and Arikara, 1780.** Mooney's reconstructions are far below the village counts; kept as soft constraints.
- **Hidatsa, 1838.** Hayden's "forty lodges" against later rolls; unresolved, fit in between.
- **Arikara, 1871–78.** Hodge's 1,650 against the Fort Berthold roll of 654; irreconcilable, fit splits them.
- **Arapaho, 1820.** Bell's "10,000" excluded as a mixed-camp count.
- **Kiowa, 1854.** Whitfield's 2,800 treated as an overestimate against Mooney's series.
- **Blackfoot, 1809.** Henry's tents give half of Umfreville's 1789 figures; both kept, and Henry's family factor (0.60) absorbs the difference.

## 12. Checks against the narrative histories

The tracks and populations were read against the developments described in Hämäläinen, *The Comanche Empire* (2008), Kavanagh, *Comanche Political History* (1996), West, *The Contested Plains* (1998), Bray, "Teton Sioux Population History" (1994), Ewers (1955), Denig (BAE 46) and the Handbook 13 chapters. Each development below is followed by how the map shows it.

- **Jupe and Yamparika north of the Arkansas, to about 1805.** Anza in 1786: "the Jupes and Yamparicas extending from the Rio Napestle to the north a little beyond the Sierra de Almagre" (Kavanagh, pp. 123–25, 190, 482). Both centres now stay north of the Arkansas through the 1790s; the Yamparika cross it in the 1820s, as the Cheyenne and Arapaho take the upper Arkansas.
- **The Jupe merge into the Yamparika.** The leadership of the two reversed by 1794; the name lingers to the 1820s (Kavanagh, pp. 190, 482–83; Hämäläinen, p. 282). The Jupe division ends in 1795 and its people pass to the Yamparika (`division_transfers.csv`): the merger, not a loss.
- **The western Kotsoteka faced New Mexico.** Ortiz in 1786 counted eight Kotsoteka rancherías between the Canadian and the Pecos; their chiefs met on the Canadian in 1793 and camped there in 1808–10 (Kavanagh, pp. 113–14, 139, 143, 154–55). The Kotsoteka centre now lies on the upper Canadian, not in western Oklahoma. Vial's camps of 1785–87 near Wichita Falls are now the eastern Comanche's.
- **The eastern Comanche, from the 1750s.** Kotsoteka bands took the Texas plains in the early 1750s (Hämäläinen, pp. 55, 105). Their rancherías in the 1780s "commonly stay above" the Red and pass to the head of the Brazos (Cabello, in Kavanagh, p. 108); the 1780 keyframe follows that.
- **The smallpox of 1780–81 struck the eastern Comanche only.** "It failed to spread among the nearby western Comanches" (Hämäläinen, p. 111). The western divisions now lose 5%, the eastern 60%.
- **The Tenewa, from about 1810.** A splinter of Yamparikas under El Sordo formed the Tenewa on the middle Red (Kavanagh, p. 483; Hämäläinen, pp. 151, 282). The model carries them, with the Nokoni who emerged among them by 1846, as one division from 1830, labelled Tenewa and Nokoni. Pahayuko's camps are now theirs, not the Penateka's. Between 1810 and 1830 they are within the Yamparika.
- **The Kwahadi, from the late 1850s.** A faction drawing followers across divisional lines, first named in 1862 (Hämäläinen, pp. 311, 315; Kavanagh, pp. 372, 481). The division now begins in 1858, not 1835.
- **The Kiowa move south.** The Kiowa–Comanche peace was made about 1790 or in 1806. The Kiowa then "established residence on the upper Canadian and Red rivers" (Hämäläinen, p. 172) and camped "along and south of the Arkansas River" (Levy, Handbook 13, p. 908). A combined Comanche–Kiowa ranchería was on the Huerfano in 1810, and Fowler's camp of 1821 near Pueblo held Kiowas (Kavanagh, pp. 171, 211). The Kiowa centre is now at 39.8° N in 1810 and 38.0° N in 1825, against 41.3° and 38.7° before. A Dakota winter count still puts a Kiowa village by Scott's Bluff in the winter of 1814–15, so part of the people stayed north.
- **1859: the Comanche and Kiowa on the Arkansas–Canadian strip.** "Nearly all Comanches and Kiowas, some ten thousand people" (Hämäläinen, p. 311). The Yamparika, Kotsoteka and Kiowa centres lie there; the reserve Penateka stay on the Clear Fork until their removal in August.
- **The Comanche totals.** Hämäläinen's 30,000–40,000 about 1800 and 20,000 in the 1840s are his reconstruction from round contemporary figures. Kavanagh shows how those figures were made, and the fit follows the counts (§11; `KNOWN_ISSUES.md` §1).
- **The Teton, 1805–81.** Bray reconstructs 8,500 in 1805 and 16,110 in 1881 (Table 3). His reconstruction is entered at secondary weight. The fit stays at about 6,250 in 1805: Clark's figures, which Bray calls "a gross underestimate", and the keyframes outweigh it. The fit is about 18,100 in 1881, between Bray and the agency counts he calls inflated. The fit's Sans Arc stay about a third below Bray's through 1870. Following Bray, the Tetons lose 2% in 1837–38 (5% for the Sihasapa and Hunkpapa), and the Brulé lose 15% in 1849–50.
- **The Cheyenne and Arapaho after 1840.** They wintered at the Front Range, the South Platte and the Big Timbers and hunted more than 100 miles east in summer. The gold rush of 1858–59 took the Front Range winter grounds and pushed them into the Smoky Hill–Republican country (West, pp. 192–93, 204, 234–35). The tracks show the centre of that range, not the displacement within it.
- **The Wichita after 1811.** Hämäläinen has them abandoning the Red River villages: some joined the Comanche, and the rest gathered in villages on the Brazos, Navasota and Trinity (p. 149). The Wichita division moves west up the Red from 1813 and to the Wichita Mountains by 1828. The Waco and Tawakoni villages on the Brazos are records, not the division centre.
- **The Cuartelejo and Paloma Apache after 1730.** Hämäläinen has them at Pecos and in the Pecos valley until 1752 (pp. 36, 48). The model ends them in 1732, half absorbed by the Jicarilla and half by the Lipan.
- **Henday's "Archithinue", 1754.** Cocking used the term for the Gros Ventre and the three Blackfoot tribes. "Wissler … was reasonably certain that they also were Gros Ventres" (Ewers, pp. 17–18). The camp of October 1754 is now shared between the Gros Ventre and Siksika tracks. Henday's Alberta "Assiniboine" were "doubtless Stoneys" (Handbook 13, p. 596).
