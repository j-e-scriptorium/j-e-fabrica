# Known issues

Issues are ranked by how far they could move the map if resolved against us. Each one ends with what would settle it. The works suggested there are named from general knowledge, not checked for this package.

## 1. The Comanche population, 1819–1875

- **The tension.** The fit puts the Comanche at about 10,800 in 1830 and 11,000 in 1846. Three groups of sources disagree:
  - Burnet (1819) and Berlandier (late 1820s): 10,000–12,000 (Kavanagh, Handbook 13, pp. 900–901);
  - the agents of 1843–49: 14,300–20,000;
  - Hämäläinen (2008): 20,000–30,000 in the 1820s and 1830s (p. 179) and "near the twenty-thousand level" about 1849 (p. 293).
- **Why the fit sits low.** It is not mainly the growth prior. Hodge's small figures for 1869–72 are partial counts and never entered the fit. The 1840s figures are pulled down by the 1819 and 1829 counts of 10,000–12,000 through the growth prior, and every Handbook-cited count is in the catch-all "other sources" family, whose factor (1.19) scales them down. Accepting 20,000 in the 1840s would mean either growth from 1829 that no source describes, or Burnet and Berlandier counting only part of the nation.
- **What the model now includes**, after Hämäläinen was read in full:
  - smallpox 1816 (40%) and 1839–40 (20%);
  - 1848 smallpox and 1849 cholera at 5% each, since Williams and Neighbors reported 300 deaths for both years (Kavanagh, p. 902), against Hämäläinen's description of severe losses (p. 302);
  - drought and famine, 1850–60, at 35% (rate ours, scaled to Hämäläinen's series, ch. 7 and n. 9);
  - smallpox, famine and war in the early 1860s at 40% (Hämäläinen p. 313: "as many as four thousand", leaving 5,000 in 1865);
  - hunger and war, 1871–75, at 30% (rate ours; pp. 339–40).
- **Status.** Open. The fit runs about 3,200 in 1865 and 2,900 in 1870, against Hämäläinen's 5,000 and Tatum's 3,742.
- **Would settle it.** Kavanagh, *Comanche Political History* (1996), for how each figure of 1819–49 was made and what part of the nation it covers; the Butler and Lewis (1846) and Neighbors (1849) reports themselves.
- **Effect if the high reading is right.** The southern-plains total in the 1840s rises by 5,000–9,000, and the Comanche dots by about 50% in area.

## 2. Epidemic mortality rates are mostly assumed

- **Scale.** The single most influential input before 1800 (±25% on every rate moves the 1780 total between 138,000 and 183,000). Most division-level rates are scaled from a regional figure or assumed (JUDGMENTS §7).
- **Would settle it.** Fenn, *Pox Americana* (2001), and Thornton (1987) reread for division-level figures; Trimble's work on the Missouri epidemics; for 1837, the Fort Clark and Fort Union journals.

## 3. The eighteenth century rests on few records

- **Thin coverage.** Of 345 division × period cells, 33 have neither a count nor a place (`coverage_by_division_and_period.csv`, flag `thin`). Fourteen of them are 1700–49, mostly the northern plains (Blackfoot divisions, Gros Ventre, both Crow divisions, Shoshone, Northern Assiniboine, Cree) and the Osage and Ponca.
- **What fills the gap.** The map draws these years from keyframes and smoothing. Their held-out error (×1.41 for population, 1700–99) is the worst of any period.
- **Would settle it.** Russell, *Eighteenth-Century Western Cree and Their Neighbours* (1991); Burpee's editions of Henday (1907), Cocking (1908) and La Vérendrye (1927); A. B. Thomas, *After Coronado* (1935) and *Forgotten Frontiers* (1932) for the Spanish documents; Bolton's *Athanase de Mézières* (1914) for the Wichita, Kitsai and Tonkawa; Nasatir, *Before Lewis and Clark* (1952) for Truteau and Mackay.

## 4. Canadian peoples after 1870 and before 1790

- **The gap.** The Plains Cree, Plains Ojibwe and Northern Assiniboine have no Canadian Indian Affairs or treaty paylist counts in the record. Their reserve-era curves rest on Hodge, Denig via Hayden, and keyframes. The Cree and Ojibwe are flagged `thin` for 1875–1905. The Sarsi and Stoney have the 1877 Treaty 7 rolls and the Department's counts for 1885 and 1895 as the Handbook gives them, and nothing else after 1877. The 1890 census covers the United States only.
- **Would settle it.** Canada, *Annual Reports of the Department of Indian Affairs* (1880 onward) and the Treaty 4, 6 and 7 paylists.

## 5. Agency counts used as the fixed reference

- **The assumption.** Reservation censuses (1868 on) anchor the source-family factors at 1.0. Agents had reasons to inflate rolls (rations) and sometimes to deflate them. If they ran systematically high, every earlier family's factor inherits the bias.
- **Partial check.** Counts called "census", "roll" or "enrollment" are weighted more tightly than agents' estimates. Where an agent's figure is flagged in the source as high (Arapaho 1872, "probably too high", Fowler), the record says so.
- **A check that does not decide it.** The special Indian census of 1890 is now in the record, but it largely reproduced the agency rolls: its figures for the Crow, Kansa, Iowa, Otoe-Missouria and Southern Cheyenne are identical to the Indian Office’s for that year. Where it differs it adds detail (division-level splits at Standing Rock, Rosebud and Fort Berthold), not an independent count.
- **Would settle it.** The 1900 census Indian schedules, which were enumerated household by household, compared with the agency rolls of 1900.

## 6. The band layer is largely illustrative

- **Recalled places.** 198 band places are recalled from standard histories without entry-by-entry checking.
- **Ours.** Band weights and budding order; the matching of lists from different decades.
- **Status.** Division totals constrain the bands' sum, but nothing else about the bands is tested. Do not cite band-level positions or sizes from this map.

## 7. Uncalibrated village halos

- **The gap.** Village divisions' position uncertainty is a hand-set formula (`METHODS.md` §3), not fitted to held-out places.
- **Measured miss.** The held-out median miss is 48 km.
- **Whether the halo is the right size.** Untested: it may be too wide near well-dated sites and too narrow across long undocumented gaps.

## 8. Second-hand and recalled material in the record

- **Records.** 22 records are tier C: the work was not read here. They include:
  - Brooks and Thornton on the Comanche in 1816;
  - Larocque's 1805 Crow figures via Wikipedia;
  - Kappler's 1855 Blackfoot treaty;
  - Prescott's 1850 Mdewakanton count via Schoolcraft;
  - the treaty-council attendance lists for Fort Laramie (1851) and Medicine Lodge (1867), taken from Wikipedia;
  - several Texas and Oklahoma sites recalled (El Cañón mission, Van Dorn's fight, the Wichita refugee camp of 1865).
- Hämäläinen's figures and the San Carlos settlement of 1787, formerly tier C, now cite pages of the book, read in full.
- **Other recalled material.** The seasonal literature patterns, the original 129 settlement dates (since checked against references, each naming its check), and the band places.
- The header of `data_src.py` describes the documented records as read for this build. The tier-C records are the exceptions, and each is marked in its source field.

**Would settle it.** The `review_sample.csv` check (`REVIEW_PROTOCOL.md` §1), with all tier-C records added.

## 9. Wikipedia as a coordinate source

- **Scale.** About 110 places use Wikipedia's coordinates for battles, treaties, agencies and archaeological sites, as given.
- **Risk.** Errors there are usually small for named sites (under 10 km) but can be larger for battle sites known only approximately.
- **Would settle it.** Spot-check against the National Register of Historic Places nominations or USGS GNIS.

## 10. Divisions as fixed entities

- **The simplification.** Divisions split, merged and re-formed over two centuries, and the model fixes a single date for each split (JUDGMENTS §1). The seven Teton divisions are drawn from 1700, though most are not named in any source until much later.
- **First recorded names**, from the synonymy in DeMallie, "Sioux Until 1850", Handbook 13, pp. 755–58:
  - Oglala ("Occononas") and Saone ("Chaony"), 1795–96 (Truteau). Saone was an umbrella for the northern Teton (Miniconjou, Sans Arc, Hunkpapa and others).
  - Brulé, Miniconjou, Hunkpapa and Sans Arc, 1803–04 (Tabeau).
  - Sihasapa and Two Kettle in their Sioux forms, 1833 (Denig). Tabeau's 1803–04 list has a Two Kettle band name.
- **Consequence.** The divisions' tracks before those dates are projections of their later identities backward. Tabeau also reports two Oglala bands trying to farm with the Arikara before the Teton crossed the Missouri ("Sioux Until 1850", p. 731).
- **Would settle it.** Not more reading but a modelling choice: an undivided Teton before 1795, splitting into Oglala, Brulé and Saone, and the Saone into its later divisions by 1804. This is the next structural change to make.

## 11. Things the tests cannot see

- A record that misreports its source.
- A bias shared by every source on a people.
- A keyframe that is wrong where no record lies near enough to contradict it.

`REVIEW_PROTOCOL.md` §1–3 are the only defences against the first two. For the third, the keyframe-removal sensitivity run gives a bound, not a test.
