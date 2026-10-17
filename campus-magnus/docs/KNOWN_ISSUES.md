# Known issues

Issues are ranked by how far they could move the map if resolved against us. Each one ends with what would settle it. The works suggested there are named from general knowledge, not checked for this package.

## 1. The Comanche population, 1819–1875

- **The figures, and how Kavanagh's *Comanche Political History* (1996) shows them to have been made.**
  - Burnet's 10,000–12,000 "in 1819" was written in 1847 "from the recollection of near thirty years" (p. 354), and is weighted as a reconstruction.
  - Bonnell's 20,000 (1838) is hearsay from one village, in a polemical letter (p. 228).
  - Butler and Lewis's 1846 report gives every division in lodges at seven to a lodge, 15,600 in all. Butler's own letter four months earlier had 12,500 at five to a lodge. Kavanagh calls the list confused and its figures unreliable (pp. 297–300, 332).
  - Neighbors's 20,000 of 1849 (4,000 warriors, "made from the best information that could be obtained from the Indians by frequent inquiry") and the "19,200" of 1841–45 are round figures from Texas, which Kavanagh notes describe only the Comanches known to Anglo-Texans (p. 354). Schoolcraft's table of Texas estimates gives Butler and Davis's 1846 figure as 14,300 and a "consolidated" 15,000 for 1850; Parker's census of 1854 gives 10,000 "men, women, and children" (Winfrey and Day, *Indian Papers of Texas*, vol. 3, docs. 87, 100, 131). The consolidated figure is a compilation of the others and is not entered.
  - After 1850 the counts are concrete: the Penateka at 2,800 (1846, unreliable), 1,200 (1854) and 384 (1859); the Arkansas River Comanches at 3,200 (Whitfield 1856); the New Mexico Kotsoteka and Kwahada at about 2,000 (Norton 1866); 4,445 in 1869 (including an estimated 1,960 never reported); 3,742 in 1870 (including 1,000 estimated); 2,643 at the census of March 1874; 1,721 in 1875.
- **Verdict.** The best contemporary whole-nation figure for the 1840s is Butler and Lewis's 12,500–15,600, itself unreliable; the 20,000 figures are round hearsay. The fit, about 10,600 in 1846, sits under the Butler and Lewis range; Parker's 10,000 of 1854, the first figure after the epidemic of 1849, is above the fit's 8,000. The Texas counts of 1851–52 that Kavanagh quotes (Stem: 600 for the southern bands; Hardee: 700 for the lower bands and 1,500, by hearsay, for the bands of Pahayuko and Sanaco; pp. 332) and Bogy and Irwin's band list of 1866 (Yamparika 1,800, Kotsoteka 700, Nokoni 600, Penateka 600, Kwahada 1,000; p. 404) are in the record. Hämäläinen's 20,000–30,000 for the 1820s–40s is not supported by any count Kavanagh reports and is weighted as a reconstruction.
- **What remains uncertain.** Whether the decline from the 1840s to the 1860s came mainly in 1848–49 (Hämäläinen: severe; the only contemporary count, 300 deaths) or in the drought of the 1850s. The model puts most of it in the 1850s and early 1860s, with rates of its own scaled to the counts.
- **An unentered report.** In May 1843 Eldredge heard that smallpox had broken out among Comanches back from Matamoros, "carrying them off by the hundreds", and gave it "but little credence" (Winfrey and Day, *Indian Papers of Texas*, vol. 1, p. 256). No epidemic is applied for 1843.
- **Would settle it.** The Stem (1851) and Hardee (1852) reports in full, for their division detail, and the Brazos and Clear Fork reservation rolls of 1855–59, none of which Winfrey and Day print.

## 2. Epidemic mortality rates are mostly assumed

- **Scale.** Still the single most influential input before 1800: ±25% on every rate moves the 1780 total between 135,000 and 188,000.
- **1780–82, after reading Fenn, *Pox Americana* (2001).**
  - Sourced: the northern plains (60%: Oman's count of the tents left gives three-fifths dead; Binnema, *Common and Contested Ground*, p. 122, judges "about two-thirds of all northwestern plains Indians", and finds no group that escaped), the Missouri villages (68%, Lehmer), the Lipan (more than 400 dead, about 15%) and the eastern Comanche (two-thirds reported, 60% used). The western Comanche lose 5%: the epidemic "failed to spread among the nearby western Comanches" (Hämäläinen, p. 111). The Assiniboine lose 40%: "between one-third and one-half" (Handbook 13, p. 574), with Denig's tradition of about 300 lodges lost from some 1,500 (BAE 46, p. 399).
  - Fenn's 43% is a case-fatality rate (deaths among the infected, from Madras in the 1960s), not a mortality rate. Her own minimum for the nomadic Sioux, a third infected, is about 14%. The Sioux, Cheyenne, Arapaho, Kiowa and Plains Apache lose 20%: assumed, just above that minimum. Bray's reconstruction has the Sioux as a whole losing 16% ("Teton Sioux Population History", p. 170).
  - The Crow stay at 43%, above Fenn's 21.5% minimum, because Larocque's lodge count implies far heavier losses.
- **Other epidemics.** Most division-level rates for 1801–02 and 1849 remain scaled or assumed (JUDGMENTS §7). The Teton rates for 1837–38 (2%, 5% for the Sihasapa and Hunkpapa) and the Brulé rate for 1849–50 (15%) follow Bray (pp. 178–80); Bray mentions no Teton losses in 1801–02, which the model still applies at 25%.
- **Would settle it.** Thornton (1987); Trimble's work and the Fort Clark journal for 1837; Hackett for the Canadian epidemics.

## 3. The eighteenth century rests on few records

- **Thin coverage.** Of 336 division × period cells, 30 have neither a count nor a place (`coverage_by_division_and_period.csv`, flag `thin`). Four are the Teton divisions of 1785–99, which no source counts or places before Lewis and Clark. Fifteen are 1700–49: the northern plains (the Siksika and Blood, Gros Ventre, Sarsi, Stoney, both Crow divisions, Northern Assiniboine and Cree), the Arapaho, the Osage, the Ponca and the Tonkawa.
- **What fills the gap.** The map draws these years from keyframes and smoothing. Their held-out error (×1.37 for population, 1700–99) is the worst of any period.
- **Would settle it.** Russell, *Eighteenth-Century Western Cree and Their Neighbours* (1991); the Hudson's Bay Company post journals of the Saskatchewan, 1770–1800; A. B. Thomas, *After Coronado* (1935), *Forgotten Frontiers* (1932) and *The Plains Indians and New Mexico* (1940) for the Spanish documents; John, *Storms Brewed in Other Men's Worlds* (1975); Nasatir, *Before Lewis and Clark* (1952) for Truteau and Mackay.

## 4. Canadian peoples after 1870 and before 1790

- **The counts.** The Department of Indian Affairs returns give the Blackfoot, Blood, Canadian Piegan, Sarsi, Morley Stoney, Northern Assiniboine and Plains Cree band by band for 1883, 1884, 1886–88, 1890, 1892, 1893, about 1898, 1899 and 1900, some years for Treaty 7 or Treaties 4 and 6 only. The returns read for 1881–82, 1885, 1889 and 1891 give one figure per treaty, which cannot be divided among the peoples; 1894–97 were not available. Two series run side by side: the census returns, and the tables of the number and whereabouts of each band, which count absentees and run higher.
- **What the counts need.** The Plains Cree total includes bands the Department called mixed Cree, Saulteaux and Stony; the Woods Cree bands are left out. The Treaty 4 Saulteaux are not part of the Pembina–Turtle Mountain division and are not modelled. The Canadian Dakota refugees (about 730 on reserves in 1890) are not modelled either.
- **Would settle it.** The band-level returns for 1881–82, 1885, 1889, 1891 and 1894–97, and the Treaty 4, 6 and 7 paylists.

## 5. Agency counts used as the fixed reference

- **The assumption.** Reservation censuses (1868 on) anchor the source-family factors at 1.0. Agents had reasons to inflate rolls (rations) and sometimes to deflate them. If they ran systematically high, every earlier family's factor inherits the bias.
- **Partial check.** Counts called "census", "roll" or "enrollment" are weighted more tightly than agents' estimates. Where an agent's figure is flagged in the source as high (Arapaho 1872, "probably too high", Fowler), the record says so.
- **A check that does not decide it.** The special Indian census of 1890, in the record, largely reproduced the agency rolls: its figures for the Crow, Kansa, Iowa, Otoe-Missouria and Southern Cheyenne are identical to the Indian Office’s for that year. Where it differs it adds detail (division-level splits at Standing Rock, Rosebud and Fort Berthold), not an independent count.
- **Would settle it.** The 1900 census Indian schedules, which were enumerated household by household, compared with the agency rolls of 1900.

## 6. The band layer is largely illustrative

- **Recalled places.** 197 band places are recalled from standard histories without entry-by-entry checking.
- **Ours.** Band weights and budding order; the matching of lists from different decades.
- **Status.** Division totals constrain the bands' sum, but nothing else about the bands is tested. Do not cite band-level positions or sizes from this map.

## 7. Village halos: uneven coverage

- **The fit.** The village halo is fitted to 243 withheld village places (`calib_vhalo.py`, `METHODS.md` §3) and holds 68% of them; the median miss is 11 km.
- **Where it is too narrow.** Places within three years of another record fall inside only 59% of the time. Most of these misses are a division's several villages standing apart in the same years, which one track cannot represent; the halo is a statement about the track, not about the spread of a division's villages.
- **Where it is too wide.** Places three to ten years from the nearest record fall inside 76% of the time.
- **No time term.** A term growing with the years since the nearest record was tested and not chosen: the widest misses are those nearest in time to another record, and places more than ten years from one already fall inside 72% of the time.

## 8. Second-hand and recalled material in the record

- **Records.** 22 records are tier C: the work was not read here. They include:
  - Brooks and Thornton on the Comanche in 1816;
  - Larocque's 1805 Crow figures via Wikipedia;
  - Kappler's 1855 Blackfoot treaty;
  - Prescott's 1850 Mdewakanton count via Schoolcraft;
  - the treaty-council attendance lists for Fort Laramie (1851) and Medicine Lodge (1867), taken from Wikipedia;
  - several Texas and Oklahoma sites recalled (El Cañón mission, Van Dorn's fight, the Wichita refugee camp of 1865).
- **Other recalled material.** The seasonal literature patterns not read here (Milloy for the Qu'Appelle Cree after 1830 and the Cypress Hills Cree, Ross for the Plains Ojibwe after 1820, Pond for the Sisseton and Wahpeton), the village moves cited from Smith's *Like-a-Fishhook Village* (1972), and the band places. The 129 settlement dates were checked against references, each named in `settlements.csv`.
- The header of `data_src.py` describes the documented records as read for this build. The tier-C records are the exceptions, and each is marked in its source field.

**Would settle it.** The `review_sample.csv` check (`REVIEW_PROTOCOL.md` §1), with all tier-C records added.

## 9. Wikipedia as a coordinate source

- **Scale.** About 130 places, from 72 articles, use Wikipedia's coordinates for battles, treaties, agencies and archaeological sites, as given.
- **Risk.** Errors there are usually small for named sites (under 10 km) but can be larger for battle sites known only approximately.
- **Would settle it.** Spot-check against the National Register of Historic Places nominations or USGS GNIS.

## 10. Divisions as fixed entities

- **The simplification.** Divisions split, merged and re-formed over two centuries, and the model fixes a single date for each split (JUDGMENTS §1). The Teton are one division to 1785, when the Brulé, Oglala, Miniconjou and the Saone begin; the Saone divide into the Hunkpapa, Sihasapa and Sans Arc in 1806; the Two Kettle bud from the Miniconjou in 1833. The Yanktonai and Blackfoot divisions are still drawn from 1700.
- **First recorded names**, from the synonymy in DeMallie, "Sioux Until 1850", Handbook 13, pp. 755–58:
  - Oglala ("Occononas") and Saone ("Chaony"), 1795–96 (Truteau). Saone was an umbrella for the northern Teton (Miniconjou, Sans Arc, Hunkpapa and others).
  - Brulé, Miniconjou, Hunkpapa and Sans Arc, 1803–04 (Tabeau).
  - Sihasapa and Two Kettle in their Sioux forms, 1833 (Denig). Tabeau's 1803–04 list has a Two Kettle band name.
- **The Two Kettle** begin in 1833, budded from the Miniconjou (Bray, "Teton Sioux Population History", pp. 178, 182); Denig is the first to count them as a division, and Nicollet in 1839 still lists them as a camp of a Miniconjou band.
- **What remains ours.** The dates 1785 and 1806 are round: Bray dates the Brulé and Oglala as distinct, and the Miniconjou and Saone as emerging, by 1785 (pp. 173, 177–78); Tabeau names the Hunkpapa and Sans Arc in 1803–04. Bray counts the Sihasapa as a band with the Yankton in 1805; the model keeps them with the Saone. The successors' shares at each split are ours, set from their later counts. Tabeau also reports two Oglala bands trying to farm with the Arikara before the Teton crossed the Missouri ("Sioux Until 1850", p. 731).
- **The Comanche divisions.** Kavanagh treats them as processual: the eastern Kotsoteka became the Hois and then the Penateka; a splinter of Yamparikas became the Tenewa about 1810; the Jupe merged into the Yamparika between 1794 and the 1820s; the Kwahadi drew on several divisions in the 1860s (*Comanche Political History*, pp. 479–86). The model's dates follow him where it can: the Kwahadi from 1858, the Jupe to 1795, the Tenewa and Nokoni as one division from 1830. The Tenewa of 1810–30 are carried within the Yamparika. The Texas habit of calling any distant Comanche "Yamparika" (p. 124) makes the Texas Yamparika records of 1780–1812 uncertain, and they are not entered.
- **Would settle it.** For the Teton, a band-level source for 1785–1805 (Truteau's and Tabeau's narratives in full; Nasatir, *Before Lewis and Clark*). For the Yanktonai and Blackfoot, the same modelling choice made for the Teton: undivided until their divisions are first attested.

## 11. Things the tests cannot see

- A record that misreports its source.
- A bias shared by every source on a people.
- A keyframe that is wrong where no record lies near enough to contradict it.

`REVIEW_PROTOCOL.md` §1–3 are the only defences against the first two. For the third, the keyframe-removal sensitivity run gives a bound, not a test.

## 12. Conflicts the primary texts raise

Reading the primary sources behind figures the record had cited second-hand turned up disagreements that are not resolved here.

- **Blood and North Blackfoot, 1858–60.** Hayden gives the Blood 300 lodges and 2,400 people and the North Blackfoot 150 and 1,200 in 1858; Agent Vaughan's 1860 table, as Ewers prints it (p. 21), has them the other way round. Both are kept; one is a transposition. ARCIA 1858 (p. 432) and 1860 (p. 308) would settle it.
- **Henday's route and the 1754 camp.** Burpee takes Henday down the Red Deer and the South Saskatchewan and builds his canoes on the Red Deer above Tail Creek. Morton sends him down the North Saskatchewan, building the canoes at the mouth of the Sturgeon, because the plains peoples "were not trappers and were unfamiliar with the use of the canoe" (*A History of the Canadian West*, pp. 246–49). Morton puts the Archithinue camp about 55 km north of Burpee's, west of Nevis on the Red Deer. Burpee reads the Archithinue as Blackfoot, Morton as Blood (p. 247), Ewers after Wissler as probably Gros Ventre (pp. 17–18). The record places the camp after Burpee and keeps it off every division track. Henday's own route points follow Burpee.
- **Kelsey's "Naywatame Poets", 1691.** Morton reads them as Gros Ventre, and the record follows him; Russell, whom Binnema follows (*Common and Contested Ground*, p. 77), reads them as Hidatsa. The record is kept off the tracks either way.
- **Le Raye's "Paunched Indians", 1802.** Binnema takes them as "certainly Gros Ventre-Arapahos" (p. 192), a band of the southern Gros Ventre on the upper Yellowstone and Bighorn; the record follows him. Clark's "Paunch Indians" of 1805 are a different people, counted with the Crow.
- **Henday's "Archithinue".** Binnema glosses the word as the Cree for "stranger", used for the Blackfoot and Gros Ventre together (p. 212, n. 45), which supports keeping the 1754 camp off any one division. Another version of Henday's journal (B.239/a/40) names "bloody Indians" on 16 May 1755 (n. 52); that record is assigned to the Blood.
- **Chesterfield House.** Binnema has it standing empty from 1802 to 1804; `settlements.csv` runs it from 1800 to 1805, after North American Forts.
- **The Forks rendezvous.** The record dates the Chevalier de La Vérendrye's visit to the Forks of the Saskatchewan, "the rendezvous every spring of the Crees", to 1739, as the La Vérendrye journals do; Morton dates it 1749 (pp. 230–31).
- **Saukamappee's smallpox.** Morton ties the epidemic Saukamappee describes, caught from the Snakes, to the 1730s (smallpox at Montreal in 1732 and on the Winnipeg River in 1737), not to 1781 (p. 18). The model applies no 1730s epidemic on the northern plains.
- **Denig's two manuscripts.** BAE 46 gives the Missouri Assiniboine bands at four and a half to a lodge; *Five Indian Tribes* gives the same bands at four (p. 79). The two texts also swap band names. The *Five Indian Tribes* "Gens du Lac" are the BAE 46 "Gens du Nord", and its "Gens du Nord" are the BAE 46 Red Root band (Ewers, pp. 82–83 n. 17, p. 88 n. 26). Ewers has the Red Root band splitting from the Canoe band about 1844, where `bands_src` has it from the Gauche band.
- **Denig's dates.** Denig dates the 1837 smallpox to 1838, the siege of Fort McKenzie to 1835 (it was June 1834) and the Crow influenza to 1849 (Kurz has the winter of 1850–51). He dates the Crow–Assiniboine peace to 1844 or "since 1850", where BAE 46 has about 1849. The record follows Ewers's corrections.
- **The Red Cloud Agency counts of 1872.** Hyde gives 1,342 Northern Cheyenne and 1,515 Northern Arapaho (p. 199). Fowler, in Handbook 13, gives the 1,342 to the Arapaho, and the record follows her. The 1872 report would settle it (`SOURCES_WANTED.md`).
- **Hyde's errors.** Hyde (1937) is often superseded. He has the Arikara on the Platte until about 1835, and he calls Le Raye's journal a forgery, which Binnema does not. He puts the Bates fight of 1874 on the head of the Powder; it was on the Nowood. He makes the Reynolds camp of March 1876 Crazy Horse's, which later work (recalled) makes mainly Cheyenne. He also undercounts the Cheyenne at the Little Bighorn. Hyde's 60 Oglala lodges for Lewis and Clark's count of 1804 stand against Clark's 50 in the record.
- **Ray's own figures.** Ray gives 800 Cree lodges for Hayden where Hayden prints 880, 200 lodges for Mackenzie's Assiniboine where Mackenzie's two groups sum to 190, and puts the Carlton losses of 1819–20 at "roughly 900" where his own figures give 1,900. The record uses the primary figures where Ray quotes them.
- **The Cypress Hills Cree.** Ray, through Cowie, has the Cypress Hills as a regular winter refuge only from about 1870; the record's seasonal pattern for this division (Milloy, recalled) starts in 1790, and Denig's 350 lodges of La Lance "in the Cypress and Prickly Pear mountains" in 1855 stand between them.
- **The Kansa in 1752.** The Handbook has the Kansa moving to the mouth of the Kansas River in 1752; Macarty, in Nasatir, has them returning that year "to their old homes" near Fort Cavagnolle, some 30 km up the Missouri. Both records stand.
- **Shoshone counts that mix peoples.** Mann's 1,800 of 1863 and Irwin's 1,200 of 1871 include Bannock or other Shoshone. Irwin's spring 1872 ratio of five Bannocks to sixteen Shoshones (Stamm, p. 83) is the only figure that splits them.
- **The Indian Office tables.** The Upper Platte agency's Cheyenne and Arapaho swap labels between 1862 and 1863 (the 1863 reading, Cheyenne 1,800 and Arapaho 720, agrees with every other source and is the one used; the 1862 and 1864 tables, which print the other, are left out); the Kiowa and Comanche are 2,800 in the 1867 table and 4,000 in the 1868 table, both marked as from the report of 1867; the Wind River Shoshone are 1,041 in the 1874 table the record uses and 1,800 in the 1874 figure Ewers prints. Figures carried forward unchanged from year to year are common and were left out.
- **Sarsi, 1877–81.** The Treaty 7 roll of 1877 has 255; the pay-sheets Jenness quotes have 672 (1879, swollen by people of other tribes, he says), 396 (1880) and 470 (1881), and his own estimate for 1880 is 400–450. The 1880 and 1881 pay-sheets are used; the fit runs between them and the 1877 roll.
- **The Wichita confederacy.** De Mézières calls both of the Red River villages of 1778 Taovaya; the Handbook calls the north-bank town Wichita proper. The "Panis-mahas" who joined the Taovaya in the 1770s may have been Skiri Pawnee; they are left out of the Wichita counts.
- **La Vérendrye's peoples of 1742–43.** The Gens des Chevaux, Gens de l'Arc, Beaux Hommes, Petits Renards, Pioya and Gens de la Belle Rivière cannot be securely identified; they are not in the record.

