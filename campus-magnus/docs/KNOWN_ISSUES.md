# Known issues

Issues are ranked by how far they could move the map if resolved against us. Each one ends with what would settle it. The works suggested there are named from general knowledge, not checked for this package.

## 1. The Comanche population, 1800–1875

- **The tension.** The fit puts the Comanche at about 12,000 in 1840 and 10,000 in 1846. Six documented figures for 1843–49 run 14,300–20,000, and Hämäläinen (2008) accepts 20,000. The fit discounts them because accepting them requires a fall of about 90% between 1846 and 1875, when the reservation counts begin. The model's growth prior resists a collapse that no dated shock explains.
- **What the model includes.**
  - smallpox 1816 (40%), 1839 (20%), 1848 (20%, assumed rate) and 1862 (15%, assumed);
  - cholera 1849 (25%, assumed).
- **What it lacks.** Any representation of the 1850s drought, bison failure, starvation and Texas warfare that Hämäläinen calls a "demographic collapse".
- **Why the low reading.** The Kiowa, Cheyenne and Arapaho, under the same pressures, lost 0–45% over the same years.
- **A trial that did not resolve it.** Adding an assumed 35–60% loss for 1855–65 (drought, bison failure, war) raises the 1846 fit only to 11,000–12,600. The fit is held down less by the growth prior than by Hodge’s small division figures for 1869–72 (Yamparika 356 and 200, Nokoni 312 and 250), which lie well below it and probably count only those at the agency. The 1870 estimate of 3,742 (Kavanagh) also lies above the fit, by a factor of 1.4. Treating those figures as partial counts is the likelier repair, but it wants the sources below.
- **Would settle it.**
  - Hämäläinen ch. 7–8 and his notes on the 1840s figures;
  - Kavanagh, *Comanche Political History* (1996), division by division;
  - the Butler and Lewis (1846) and Neighbors (1849) reports themselves, for how their counts were made.
- **Effect if the high reading is right.** The southern-plains total in the 1840s rises by 5,000–8,000, and the Comanche dots by about 40% in area.

## 2. Epidemic mortality rates are mostly assumed

- **Scale.** The single most influential input before 1800 (±25% on every rate moves the 1780 total between 135,000 and 179,000). Most division-level rates are scaled from a regional figure or assumed (JUDGMENTS §7).
- **Would settle it.** Fenn, *Pox Americana* (2001), and Thornton (1987) reread for division-level figures; Trimble's work on the Missouri epidemics; for 1837, the Fort Clark and Fort Union journals.

## 3. The eighteenth century rests on few records

- **Thin coverage.** Of 321 division × period cells, 32 have neither a count nor a place (`coverage_by_division_and_period.csv`, flag `thin`). Fourteen of them are 1700–49, mostly the northern plains (Blackfoot divisions, Gros Ventre, both Crow divisions, Shoshone, Northern Assiniboine, Cree) and the Osage and Ponca.
- **What fills the gap.** The map draws these years from keyframes and smoothing. Their held-out error (×1.46 for population, 1700–99) is the worst of any period.
- **Would settle it.** Russell, *Eighteenth-Century Western Cree and Their Neighbours* (1991); Burpee's editions of Henday (1907), Cocking (1908) and La Vérendrye (1927); A. B. Thomas, *After Coronado* (1935) and *Forgotten Frontiers* (1932) for the Spanish documents; Nasatir, *Before Lewis and Clark* (1952) for Truteau and Mackay.

## 4. Canadian peoples after 1870 and before 1790

- **The gap.** The Plains Cree, Plains Ojibwe and Northern Assiniboine have no Canadian Indian Affairs or treaty paylist counts in the record. Their reserve-era curves rest on Hodge, Denig via Hayden, and keyframes. The Cree and Ojibwe are flagged `thin` for 1875–1905.
- **Would settle it.** Canada, *Annual Reports of the Department of Indian Affairs* (1880 onward) and the Treaty 4 and Treaty 6 paylists.

## 5. Agency counts used as the fixed reference

- **The assumption.** Reservation censuses (1868 on) anchor the source-family factors at 1.0. Agents had reasons to inflate rolls (rations) and sometimes to deflate them. If they ran systematically high, every earlier family's factor inherits the bias.
- **Partial check.** Counts called "census", "roll" or "enrollment" are weighted more tightly than agents' estimates. Where an agent's figure is flagged in the source as high (Arapaho 1872, "probably too high", Fowler), the record says so.
- **Would settle it.** A comparison of agency rolls with the 1890 and 1900 U.S. census Indian schedules.

## 6. The band layer is largely illustrative

- **Recalled places.** 198 band places are recalled from standard histories without entry-by-entry checking.
- **Ours.** Band weights and budding order; the matching of lists from different decades.
- **Status.** Division totals constrain the bands' sum, but nothing else about the bands is tested. Do not cite band-level positions or sizes from this map.

## 7. Uncalibrated village halos

- **The gap.** Village divisions' position uncertainty is a hand-set formula (`METHODS.md` §3), not fitted to held-out places.
- **Measured miss.** The held-out median miss is 46 km.
- **Whether the halo is the right size.** Untested: it may be too wide near well-dated sites and too narrow across long undocumented gaps.

## 8. Second-hand and recalled material in the record

- **Records.** 27 records are tier C: the work was not read here. They include:
  - all three Hämäläinen figures;
  - Brooks and Thornton on 1816;
  - Burnet;
  - Larocque via Wikipedia;
  - Kappler's 1855 Blackfoot treaty;
  - several Texas sites.
- **Other recalled material.** The seasonal literature patterns, the original 129 settlement dates (since checked against references, each naming its check), and the band places.
- The header of `data_src.py` describes the documented records as read for this build. The 27 tier-C records are the exceptions, and each is marked in its source field.

**Would settle it.** The `review_sample.csv` check (`REVIEW_PROTOCOL.md` §1), with all tier-C records added.

## 9. Wikipedia as a coordinate source

- **Scale.** About 110 places use Wikipedia's coordinates for battles, treaties, agencies and archaeological sites, as given.
- **Risk.** Errors there are usually small for named sites (under 10 km) but can be larger for battle sites known only approximately.
- **Would settle it.** Spot-check against the National Register of Historic Places nominations or USGS GNIS.

## 10. Divisions as fixed entities

- **The simplification.** Divisions split, merged and re-formed over two centuries, and the model fixes a single date for each split (JUDGMENTS §1). Before about 1800, names such as "Oglala" or "Hunkpapa" may not denote the later groups. The early tracks of the seven Teton divisions are largely projections of their later identities backward.
- **Would settle it.** DeMallie's discussion in "Teton", Handbook 13, read for the dates by which each division is first attested. A first-attestation date could become each division's start, with an undivided "Teton" before it.

## 11. Things the tests cannot see

- A record that misreports its source.
- A bias shared by every source on a people.
- A keyframe that is wrong where no record lies near enough to contradict it.

`REVIEW_PROTOCOL.md` §1–3 are the only defences against the first two. For the third, the keyframe-removal sensitivity run gives a bound, not a test.
