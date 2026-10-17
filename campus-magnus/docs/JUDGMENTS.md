# Register of judgment calls

A judgment call is any step where the record does not decide the matter and we did. They fall into eleven classes below.

- Each class gives the decision, the reason, how many records it touches, how to find them, and what changes if it is wrong.
- Record-level judgments are flagged in `data/records.csv` (`judgment_flags`). The flags are assigned automatically from each record's text by `provenance.py`, so they are a finding aid, not a verdict; read the `source_says` column.
- The page's own table of choices, with measured effects, is in the “About the data” section of the map page under "Every extrapolation choice".

## 1. What counts as a unit

| Decision | Reason | Where |
|---|---|---|
| Fit 66 divisions, not 34 peoples or ~300 bands | Divisions are the level at which the sources most often count people. | `groups.csv` |
| Splits dated to a year: the Teton 1785 (into the Brulé, Oglala, Miniconjou and the northern Teton or Saone) and the Saone 1806 (into the Hunkpapa, Sihasapa and Sans Arc), after Bray, "Teton Sioux Population History", pp. 173, 177–78, and Tabeau's names of 1803–04; Cheyenne 1832, Arapaho 1835; Missouria merge into Oto 1830; Cuartelejo and Paloma Apache end 1732 (absorbed by the Jicarilla, after Gunnerson, and by the Lipan, after Hämäläinen, p. 48); Kitsai end 1894 (merged into the Wichita, after Parks); the Stoney drawn as the Mountain Stoney only | A year is needed for the fit. The splits were gradual over a decade or more. | `groups.csv` start/end |
| Splits and mergers carry people across: the new division's share leaves its parent, and an ending division's people join the survivor (`division_transfers.csv`). The eastern Comanche from the Kotsoteka 1745, the Tenewa from the Yamparika 1830, the Kwahadi from the Kotsoteka 1858; the Jupe into the Yamparika 1795; the Cypress Hills Cree from the other Plains Cree 1790; the Arkansas Osage out in 1802 and back in 1839; the Missouria into the Oto 1830; the Cuartelejo and Paloma Apache half to the Jicarilla, half to the Lipan 1732; the Kitsai into the Wichita 1894; the Two Kettle from the Miniconjou 1833; the River and Mountain Crow counted together from 1885. Where a division ends and its successors begin, the parent's last keyframe and the successors' first are set so that the fitted totals meet: within 2% for the Teton (1785) and the Saone (1806). The Cheyenne step of 1832 is left, as a conflict in the counts (`METHODS.md` §2) | Without them a people's total jumps when a division appears or vanishes | `data_src.SHIFTS`; keyframes noted "Continuity" |
| Arkansas Osage (Claremore's band) a separate division, 1802–39 | Pike and Clark count it separately. | `osa` |
| Two names Clark recorded but which cannot be identified (Castahana, Dotame) kept as evidence only. Two others once kept apart ("Staitan", "Nemousin") folded into the Arapaho. | Parks, "Enigmatic Groups", Handbook 13, pp. 972–73: probable identifications only. | records with group `u_cas`, `u_dot`; Arapaho 1805 |

## 2. Who a record is about (32 records flagged `identification_judged`)

These are the identifications that most affect tracks.

- Henday's "Archithinue" camp of 1754, shown for the Siksika, Blood and Gros Ventre and steering none of their tracks (§12), and his "Asinepoets": Assiniboine on the way west, Stoney in Alberta (Handbook 13, p. 596).
- Bourgmont's 1724 Padouca, and Vermale's 1717 Padouca villages, both taken as Plains Apache. Both are contested; some writers take Padouca as Comanche after about 1750.
- Long's 1820 Kaskaia, as Plains Apache after Parks; kept off the track.
- Peter Pond's 1775 "Yankton" as Yanktonai.
- Ulibarrí's 1706 "probably Jicarilla" bands.
- Cocking's Pegogamaw Cree, filed with the Fort des Prairies division; kept off the track.

**If wrong:** the track of the named division moves by up to several hundred km for the decade around the record.

## 3. Turning counts into persons

| Decision | Records |
|---|---|
| A source's own persons-per-lodge or per-warrior ratio where it states one | 42 (`multiplier_stated_by_source`) |
| Our ratio otherwise: lodges × 5, warriors × 4, earth lodges × 10 (Thompson's ratio is 8–10) | 140 (`multiplier_ours`) |
| Clark 1805: the lower of his two figures | ~40 Clark records |
| Same-year counts of parts of one division are summed to a division total | see `summed_with_same_year_records` |
| A range ("1,000–1,500 families") taken at its midpoint | noted in `source_says` |

**If wrong:** sensitivity runs move totals by about 1% for ±1 person per lodge (the “About the data” section of the map page, Sensitivity).

## 4. Where a record is put

| Decision | Records |
|---|---|
| A count whose source gives no usable place is placed by us (`place_status = inferred`) and **never steers a track** | 1,428 |
| A stated place is geocoded by us, with a radius `place_radius_km` for its vagueness | all `stated` records |
| A range ("between the Platte and the Arkansas") is placed at its centre; its radius is kept as uncertainty | 54 (`place_centre_ours`) |
| Wikipedia's coordinates for battle, treaty, agency and site articles are used as given | about 130 records from 72 articles, tier B |
| A date derived from context (a narrator's age, "mid-18th century", an archaeological span) | 6 (`date_ours`) |

## 5. Which records steer a division's track

826 records inform a track, each as a noisy sighting of the division's centre rather than a point it must pass through (`METHODS.md` §3). Another 302 stated places are drawn but kept off (`steers_track = no`): camps, councils and visits of part of a division. The reasons follow.

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

- **What they are.** 508 guesses: 417 give both place and persons, 73 persons only, 12 place only, and 6 only mark an event.
- **What backs them.**
  - 281 carry a note, often naming the event or source behind them: "Treaty 6", "Whetstone agency, 1869–71", "1780–81 smallpox".
  - 227 carry none. Their basis is interpolation between neighbouring documented states, judged by eye against the record.
- **Weight.** Persons at ±30% (σ 0.3 in log); places at ±150 km.
- **When they give way.** A keyframe place within a year of a documented place is dropped. Keyframe persons are excluded when estimating source-family factors.
- **Where they matter most.**
  - Before 1780, where sixteen divisions have no count, not even as part of a tribal total, and the Cuartelejo and Paloma Apache, who have none at any date.
  - The northern plains before 1790.
  - The Plains Ojibwe throughout, and the Plains Cree before the Canadian returns of 1883.
- **Effect of removing all of them.** The 1780 total falls by about 6%, nearly all of it the undivided Teton, who have no count of their own and drop out with the Cuartelejo and Paloma Apache; the 1850 total falls by 2%; held-out population error barely moves (1.106 to 1.110, sensitivity runs), and held-out place error for the nomadic centre worsens from 107 to 114 km.

## 7. Epidemics and famines (`epidemics_and_shocks.csv`)

- **What is applied.** 37 events, 228 event × division rows, each applied only to divisions alive while it ran.
- **What is sourced.** Dates and the existence of each event are sourced. Rates are sourced for some divisions per event and scaled or assumed for the rest; the `rate_basis` field of each event says which.
- **The assumed rates that matter most.**
  - The 1780–82 smallpox for the Sioux, Cheyenne, Arapaho, Kiowa and Plains Apache (20%, just above Fenn's minimum for the Sioux) and at the edges of its range. The north, the Missouri villages, the Lipan and the eastern Comanche are sourced from Fenn (2001), read in full; the western Comanche (5%) from Hämäläinen, p. 111; the Assiniboine (40%) from Handbook 13, p. 574, and Denig. The northern rate (60%) sits between the traders' "at least one half" and Binnema's "about two-thirds" (*Common and Contested Ground*, p. 122), at Oman's three-fifths. The Gros Ventre losses of 1801 (smallpox and Cree–Assiniboine attacks, about 175 of 2,400) are from Binnema, p. 189.
  - The 1801–02 smallpox except for the Omaha.
  - The 1839–40 southern smallpox (assumed below Mooney's "third").
  - The 1849 cholera except for the Kiowa, the Cheyenne and the Brulé (Bray).
  - The Comanche losses of 1848–49 (5% a year, against a contemporary report of 300 deaths), 1850–60 (drought and famine, 35%), the early 1860s (40%), 1871–73 (15%) and 1874–75 (30%): the events are from Hämäläinen and Kavanagh, read in full; the rates are ours, scaled to the counts.
  - The Sarsi and Stoney in 1780–82 and the Stoney in 1837–38, at their neighbours' rates.
- **The Crow in 1837.** Calloway's third is set aside for Ewers's reading of Chardon, that "the Crows suffered little loss" (Denig, *Five Indian Tribes*, p. 170 n. 29); the rate is 10%. The Crow influenza of 1850–51 (Kurz's 150 dead, Denig's 600) is applied at 8%, and Vaughan's smallpox of 1851–52 among the Mountain Crow ("some four hundred") at 12%.
- **Events deliberately not modelled.** Grinnell's 1845 Blackfoot smallpox, which no other source read here gives (probably a misdating of 1837).
- **If wrong.** This is the most influential assumption before 1800: ±25% on every rate moves the 1780 total between 135,000 and 188,000.

## 8. Source-family factors

The factors are estimated by the model, not set by hand, but the grouping of sources into families is ours (`family()` in `build3.py`). Reservation censuses are fixed as the reference; every other family's counts are scaled toward them.

The estimated factors run from 0.64 (Henry 1809, counting men in his trading district) to 1.14 ("other sources" and modern reconstructions). The catch-all family holds most counts cited from the Handbook chapters, so it scales down every people whose figures come mainly from there, including the four peoples added from Handbook 13. Morse 1820 comes out about 8% high and Clark about 12% low.

**If wrong:** a family biased in the same direction as the censuses (for example, agents inflating ration rolls before 1880) would go uncorrected. See `KNOWN_ISSUES.md` §5.

## 9. Seasonal round

- **The literature patterns.** Rows in `seasonal_patterns.csv`, each with its source and page.
  - The Southern Cheyenne and Arapaho: West, *The Contested Plains*, chs. 4 and 11, and Wedel and Frison in Handbook 13. Winter at the Big Timbers of the Arkansas; summer hunts between the Arkansas and the Smoky Hill.
  - The Piegan: Ewers, *The Horse in Blackfoot Indian Culture*, pp. 41, 125–28. Winters on the Sun and Teton about 1833 and on the Marias from about 1848; summer gatherings at the Sweetgrass Hills.
  - The eighteenth-century Archithinue (Blackfoot or Gros Ventre), Saskatchewan Assiniboine and Fort des Prairies Cree: Henday 1754–55 and Cocking 1772–73.
  - The Sarsi: Jenness, pp. 11–12; the direction and distance are ours.
  - The Comanche after 1840: the Texas Indian Papers. The Penateka wintered on the Clear Fork and in the upper Cross Timbers; the northern bands summered by the Arkansas, which Kavanagh's sources of 1851–53 confirm (*Comanche Political History*, pp. 332, 343–44, 348).
  - The Kiowa, 1830–70: Levy, Handbook 13, p. 908, and Kavanagh's sources of 1851–53. Winter camps on the Red River and Washita; spring and summer on the Arkansas, following the herds north.
  - The Mountain Crow: Larocque in 1805, as Binnema quotes him (*Common and Contested Ground*, p. 37): in winter "at a Park by the foot of the Mountain", in spring and fall on the Yellowstone, in summer on the Tongue and "Horses River". The places are ours. It lowered the miss on withheld Mountain Crow season-dated places (median 71 to 65 km), and replaces Hoxie's recalled pattern.
  - The River Crow after about 1849: Denig, BAE 46, p. 404, "the Crows winter with the Assiniboin", near Fort Union. *Five Indian Tribes* confirms it ("A portion of the nation now passes the winter with the Assiniboines", p. 195), and Ewers dates Bear's Head's band at Fort Union in the winter of 1851–52 and in March 1856 (p. 143 n. 9).
  - The Eastern Shoshone, 1863–70: Stamm, *People of the Wind River*, pp. 43–46. After the fall hunt east of South Pass the bands wintered east of the mountains: Washakie's near the headwaters of the Greybull, the others on the upper North Platte and the Powder (Shimkin, as Stamm quotes him). In spring they gathered in the Wind River valley, and as summer came went to Fort Bridger for the Sun Dance and the annuities. The winter point is the middle of the four winter grounds, which is ours. For 1871–80, Stamm pp. 73, 79 and 101–12: winter in the Wind River valley and the Big Horn Basin, spring and summer toward Fort Bridger, the Green River and Utah; the summer point is ours. Tested on the withheld season-dated Shoshone places, the pattern neither helps nor hurts (mean miss 168 km, against 169 for the unsourced pattern it replaces).
  - The Yankton: DeMallie, Handbook 13, pp. 777, 789. Gardens at village sites on the Missouri, "largely abandon[ed] … during the summer buffalo hunts" west of the Missouri on the Niobrara and White.
  - The Siksika after 1800: Dempsey, Handbook 13, p. 609. The Plains Cree of the 1790s: Milloy via Darnell, Handbook 13, p. 640. The Plains Ojibwe: Albers, Handbook 13, pp. 653–54.
  - The Assiniboine and Fort des Prairies Cree from about 1780: Ray, *Indians in the Fur Trade*, pp. 170–74 and fig. 31. From the late 1770s the plains bands followed the herds into the parkland in winter and went south onto the open grassland in summer; the Brandon report of 1822 has the Missouri Assiniboine wintering on the lower Souris and the Qu'Appelle and "usually travelling southward to the Missouri River" in summer. Taken literally, that is a half-distance of about 130 km; on the few withheld Assiniboine places 90 km does better (a mean miss of 106 km against 113), and 90 is kept. The traders' round of the eighteenth century (summer at the Saskatchewan rendezvous for the Bay) ends in 1779, not 1800.
  - The Qu'Appelle–Touchwood Cree to 1825: Ray, pp. 173–74 and p. 180 n. 27. They wintered on the plains edge in the Touchwood, Beaver and Nut Hills and went back to the forest in summer, "changed very little" into the early 1820s. Ray gives no summer-on-the-grassland pattern for them, so the reverse pattern from 1830 rests on Milloy, recalled.
  - Tested on withheld season-dated places, the sourced northern and Crow patterns are slightly worse than the unsourced ones they replace (River Crow 182 km against 175 on 11 places; Missouri Assiniboine 106 against 103 on 5). The sourced patterns are kept.
  - The River Crow, 1805–48: Hoxie, *Parading through History*, p. 72: "River Crow leaders operated along the Yellowstone for part of the year, but moved north along the Judith and Musselshell Rivers during the winter." Summer is south of winter, the opposite of the recalled pattern it replaces, which had them summering at the Missouri villages; Hoxie does not say that. For 1871–79, p. 100: summers north of the Yellowstone, winters at the Mission Creek and then the Stillwater agency for rations. Nothing before 1805.
  - **Recalled, not reread for this build:** Milloy for the Qu'Appelle Cree after 1830 and for the Cypress Hills Cree (Ray, through Cowie, has the Cypress Hills as a regular winter refuge only after about 1870); Ross (1856) for the Pembina hunts of the Plains Ojibwe after 1820; Pond for the Sisseton and Wahpeton.
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
- **Band places.** 197 rows in `band_places_recalled.csv`, **recalled from standard histories, not checked entry by entry**, except where a record in `records.csv` gives the place.
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
- **Blackfoot, 1809.** Henry's tents give half of Umfreville's 1789 figures; both kept, and Henry's family factor (0.64) absorbs the difference.

## 12. Checks against the narrative histories

The tracks and populations were read against the developments described in Hämäläinen, *The Comanche Empire* (2008), Kavanagh, *Comanche Political History* (1996), West, *The Contested Plains* (1998), Bray, "Teton Sioux Population History" (1994), Ewers (1955), Denig (BAE 46) and the Handbook 13 chapters. Each development below is followed by how the map shows it.

- **Jupe and Yamparika north of the Arkansas, to about 1805.** Anza in 1786: "the Jupes and Yamparicas extending from the Rio Napestle to the north a little beyond the Sierra de Almagre" (Kavanagh, pp. 123–25, 190, 482). Both centres stay north of the Arkansas through the 1790s; the Yamparika cross it in the 1820s, as the Cheyenne and Arapaho take the upper Arkansas.
- **The Jupe merge into the Yamparika.** The leadership of the two reversed by 1794; the name lingers to the 1820s (Kavanagh, pp. 190, 482–83; Hämäläinen, p. 282). The Jupe division ends in 1795 and its people pass to the Yamparika (`division_transfers.csv`): the merger, not a loss.
- **The western Kotsoteka faced New Mexico.** Ortiz in 1786 counted eight Kotsoteka rancherías between the Canadian and the Pecos; their chiefs met on the Canadian in 1793 and camped there in 1808–10 (Kavanagh, pp. 113–14, 139, 143, 154–55). The Kotsoteka centre lies on the upper Canadian. Vial's camps of 1785–87 near Wichita Falls are assigned to the eastern Comanche.
- **The eastern Comanche, from the 1750s.** Kotsoteka bands took the Texas plains in the early 1750s (Hämäläinen, pp. 55, 105). Their rancherías in the 1780s "commonly stay above" the Red and pass to the head of the Brazos (Cabello, in Kavanagh, p. 108); the 1780 keyframe follows that.
- **The smallpox of 1780–81 struck the eastern Comanche only.** "It failed to spread among the nearby western Comanches" (Hämäläinen, p. 111). The western divisions lose 5%, the eastern 60%.
- **The Tenewa, from about 1810.** A splinter of Yamparikas under El Sordo formed the Tenewa on the middle Red (Kavanagh, p. 483; Hämäläinen, pp. 151, 282). The model carries them, with the Nokoni who emerged among them by 1846, as one division from 1830, labelled Tenewa and Nokoni. Pahayuko's camps are theirs. Between 1810 and 1830 they are within the Yamparika.
- **The Kwahadi, from the late 1850s.** A faction drawing followers across divisional lines, first named in 1862 (Hämäläinen, pp. 311, 315; Kavanagh, pp. 372, 481). The division begins in 1858.
- **The Kiowa move south.** The Kiowa–Comanche peace was made about 1790 or in 1806. The Kiowa then "established residence on the upper Canadian and Red rivers" (Hämäläinen, p. 172) and camped "along and south of the Arkansas River" (Levy, Handbook 13, p. 908). A combined Comanche–Kiowa ranchería was on the Huerfano in 1810, and Fowler's camp of 1821 near Pueblo held Kiowas (Kavanagh, pp. 171, 211). The Kiowa centre is at 39.8° N in 1810 and 37.9° N in 1825. A Dakota winter count still puts a Kiowa village by Scott's Bluff in the winter of 1814–15, so part of the people stayed north.
- **1859: the Comanche and Kiowa on the Arkansas–Canadian strip.** "Nearly all Comanches and Kiowas, some ten thousand people" (Hämäläinen, p. 311). The Yamparika, Kotsoteka and Kiowa centres lie there; the reserve Penateka stay on the Clear Fork until their removal in August.
- **The Comanche totals.** Hämäläinen's 30,000–40,000 about 1800 and 20,000 in the 1840s are his reconstruction from round contemporary figures. Kavanagh shows how those figures were made, and the fit follows the counts (§11; `KNOWN_ISSUES.md` §1).
- **The northwestern plains, 1700–1806.** Binnema, *Common and Contested Ground* (2001), read in full, reconstructs the region from the Hudson's Bay Company journals.
  - The Shoshone were "probably already established in the Missouri Basin" by 1690–1700 (p. 84), held the northwestern plains from the 1720s, and after the smallpox of 1781 and the Blackfoot advance lived "along the mountainous margins" (p. 182); Le Raye puts them on the headwaters of the Bighorn in 1802. The Shoshone keyframe for 1700 is on the Missouri, and the centre moves south from the 1780s.
  - The Blackfoot were pushed north toward the Eagle Hills by the 1730s, were secure in the Red Deer basin by 1770, and held the Oldman basin by the 1790s (pp. 90, 106, 137). Large Piegan camps on the Highwood in December 1792 and Sakatow's band at High River in November 1800 are in the record.
  - The Gros Ventre held the country near the Saskatchewan forks in the 1770s (p. 75), wintered near Chesterfield House at the Red Deer forks about 1800 (about 180 tents and 600 warriors, Fidler), and after the attacks of 1801 "pitched away" for the Missouri in April 1802 (pp. 189–92); a southern band with Arapaho kin was in the Bighorn Basin by 1802–05.
  - The Sarsi were pounding bison as far south as the Battle River by 1793 (p. 175).
  - The Gros Ventre map of 1801 (fig. 7.5) gives tents for a dozen peoples to the south; they are in the record as counts of the groups the cartographer knew, not as totals.
- **Denig, *Five Indian Tribes of the Upper Missouri* (written 1855–56; ed. Ewers, 1961), read in full.**
  - Denig's 1833 table of the Sioux by band (pp. 14–15) is his own count; he traded with the Teton from Fort Pierre in 1833–36. The Hayden figures are this table. Each 1833 record is now placed at the range Denig gives for the division (pp. 16–36). The table adds the Gens des Pins (100 lodges), taken as Upper Yanktonai, and two bands kept out of the totals: the Gens des Perches (50 lodges), which may be Upper or Lower Yanktonai, and the Esantees (30 lodges), a small Wahpekute band.
  - Denig gives five to a lodge for 1833 and "not … more than four" for 1855 (p. 15), eight for the Crow in 1833 (p. 169) and four for the Assiniboine and Cree in 1855. Each of his counts uses his own ratio. Warren, two years later, gives eight. The gap is large, and the source-family factor (§8) absorbs whatever runs through all of Denig's figures alike.
  - Denig's 1855 Brulé (150 lodges) and Oglala (180 lodges) are kept out of the fit. Ewers judges that Denig "grossly exaggerated" the Oglala decline (p. 22 n. 26), and the Brulé figure is Vaughan's of 1853. Vaughan's 1853, Twiss's 1856 and Culbertson's 1850 lodge counts, which Ewers prints in his notes, are entered at eight to a lodge: Culbertson's own ratio, and Warren's.
  - The Plains Cree total of 1855 ("ten or eleven hundred lodges") includes about 200 lodges of Woodland Cree at Île-à-la-Crosse (p. 111). The record takes the Plains Cree as 850 lodges; the subtraction is ours.
  - Denig's 800 Crow lodges and 6,400 souls for 1833 are about twice the figures of Maximilian and Larpenteur. His smallpox of the winter of 1833–34, which left 360 lodges, has no other witness (Ewers, p. 170 n. 29). Both are recorded and kept out of the fit. Two Face's 200 lodges are one band, the largest, not the Mountain Crow total.
- **Stamm, *People of the Wind River* (1999), read in full.** Stamm's counts are the agents'. Mann's 1,800 of 1863 includes "deserters" from other Shoshone groups, and Irwin's 1,200 hungry Indians of 1871 were Shoshone and Bannock together; that one is not entered. Irwin's winter of 1872–73 ("nearly eight hundred" on the reservation and four hundred more expected) is entered as 1,200. For 1880 the written report has 1,050 Shoshone and the statistical table 1,150 (Stamm, p. 279 n. 35); the table is used. In 1855–56 Washakie's band wintered near Dillon and summered at Henry's Lake and Fort Bridger (Wilson's memoir, as Stamm reads it). That puts the Shoshone track in southwestern Montana for one year, which is where the sources put it.
- **Hyde, *Red Cloud's Folk* (1937), read in full from the page images.** Hyde is used for the observers he relays: Parker's 2,000 Oglala of 1835, the Grattan-day camp of 1854, the first Red Cloud Agency on the North Platte near Henry, Nebraska (1871–73), and the agency and surrender counts of 1874–77. His table of Oglala estimates (Appendix A) supplies Riggs's 2,500 of 1840, Red Cloud's 600 lodges at seven of 1870, and the Oglala's own 1,000 lodges of 1874. The agency counts of 1874 and 1876 mix divisions and seasons; Hyde notes that the summer ration count was "about half the winter number". These counts are recorded and kept out of the fit. Hyde's own chronology before 1800 (the Teton on the Blue Earth about 1700; the Hunkpapa east of the Missouri until about 1825) is older than DeMallie's and Bray's, which the model follows.
- **Nasatir, ed., *Before Lewis and Clark*, vol. 1 (1952), read in full.** The French and Spanish documents give warrior counts by tribe for 1719, 1758 (Kerlerec), 1785 (Miró), 1791 (Concha) and 1793–95 (Trudeau, Truteau and Mackay), each entered at four persons to a warrior, which is ours. Truteau puts the Arikara of 1794–96 in two villages just below the mouth of the Cheyenne, reduced to about 500 fighting men after two of their four parts left for the Skiri and the Mandan; the 1795 keyframe is moved there from the Grand River. His 150 Cheyenne tents of 1795 and the Teton band "Ta Coropa" of eighty huts are single camps, kept out of the totals. Volume 2 (Mackay and Evans in full) is not read.
- **Robertson, *Rotting Face* (2001), read in full.** Robertson's tolls come from Chardon, Pilcher, Meyer and the older literature, and are used where he gives a figure: the Arapaho and Gros Ventre in 1831–32 ("better than a quarter of both tribes"), the Pawnee in the spring of 1838 ("nearly one-fourth … an estimated 2,500", a separate event from the 1837 Missouri epidemic, which reached them through Lakota captives), the upper Missouri cholera of 1851 (7% of the Hidatsa), the Osage in 1806–07 (200) and the Marias Massacre of 1870 (173). The Arikara arrived at the Mandan village on 28 April 1837, a year before the date the record had.
- **Hoxie, *Parading through History* (1995), read in full.** Rotten Belly's seventy tents at Fort Clark in 1833 are River Crow, after Hoxie and Ewers. The 1873 agency table counts the River Crow twice, at the Crow agency and at Fort Belknap (1,200 and 1,240), because they wintered at one and summered near the other; it is kept out of the fit. The Gros Ventre fell from 2,000 to 1,300 in the smallpox of 1869 (35%, from the agent's report). The 1884–86 Crow figures of about 3,200 are estimates; Hoxie calls the 1887 census the first reliable one.
- **Ray, *Indians in the Fur Trade* (1974), read in full.** Ray's district counts depend on his persons-per-lodge ratio, which he takes as eleven in 1815 and seven in 1822. His Assiniboine losses in the measles and whooping cough of 1819–20 (about half at Brandon, 42% at Carlton) are partly that change of ratio, so the epidemic is applied at 30% to the Assiniboine and 25% to the Cree. His Cree 1870 note, that vaccination kept the smallpox out of the Qu'Appelle and Touchwood Hills bands entirely, takes the Qu'Appelle Cree rate for 1869–70 from 15% to 3%.
- **The Teton, 1785–1881.** The model follows Bray's chronology of the divisions: one Teton division to 1785, then the Brulé, Oglala, Miniconjou and Saone, the Saone dividing in 1806 (§1; `KNOWN_ISSUES.md` §10).
- **The Teton, 1805–81.** Bray reconstructs 8,500 in 1805 and 16,110 in 1881 (Table 3). His reconstruction is entered at secondary weight. The fit stays at about 5,900 in 1805: Clark's figures, which Bray calls "a gross underestimate", and the keyframes outweigh it. The fit is about 18,100 in 1881, between Bray and the agency counts he calls inflated. The fit's Sans Arc stay about a third below Bray's through 1870. Following Bray, the Tetons lose 2% in 1837–38 (5% for the Sihasapa and Hunkpapa), and the Brulé lose 15% in 1849–50.
- **The Cheyenne and Arapaho after 1840.** They wintered at the Front Range, the South Platte and the Big Timbers and hunted more than 100 miles east in summer. The gold rush of 1858–59 took the Front Range winter grounds and pushed them into the Smoky Hill–Republican country (West, pp. 192–93, 204, 234–35). The tracks show the centre of that range, not the displacement within it.
- **The Wichita after 1811.** Hämäläinen has them abandoning the Red River villages: some joined the Comanche, and the rest gathered in villages on the Brazos, Navasota and Trinity (p. 149). The Wichita division moves west up the Red from 1813 and to the Wichita Mountains by 1828. The Waco and Tawakoni villages on the Brazos are records, not the division centre.
- **The Cuartelejo and Paloma Apache after 1730.** Hämäläinen has them at Pecos and in the Pecos valley until 1752 (pp. 36, 48). The model ends them in 1732, half absorbed by the Jicarilla and half by the Lipan.
- **Henday's "Archithinue", 1754.** Cocking used the term for the Gros Ventre and the three Blackfoot tribes. "Wissler … was reasonably certain that they also were Gros Ventres" (Ewers, pp. 17–18); Morton reads them as Blood (p. 247). The camp of October 1754 is shown for all three and steers none of their tracks. Henday's Alberta "Assiniboine" were "doubtless Stoneys" (Handbook 13, p. 596).
