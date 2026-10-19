# Methods: formal specification

This file states the model as the code implements it, with every setting and how it was chosen. Code references are to `model/src/build3.py` unless stated. The “About the data” section of the map page gives the same choices in prose with their rationale and measured effects.

## 1. Units and inputs

- **Unit.** A *division* $g$ (66 in all) with a lifespan $[s_g, e_g]$ and a lifeway (`nomadic` or `village`). A people (tribe) is the sum of its divisions. A division that splits ends in the year its successors begin; for example the Cheyenne end in 1832 and the Northern and Southern Cheyenne begin then, and the Teton end in 1785 and the Brulé, Oglala, Miniconjou and Saone begin then. The parent's last keyframe and the successors' first are set so that the fitted totals meet.
- **Documented records** (`OBS` in `data_src.py`) carry the following fields:
  - group(s): one division, or several for a whole-tribe count;
  - year (decimal; a season gives the fraction);
  - persons (optional) with a `basis` (souls, lodges × k, warriors × 4…);
  - place (optional) with radius $r$ km and status `stated` (the source describes it; we geocode) or `inferred` (the source gives a count but no usable place; we place it);
  - source and `kind` (`primary` = contemporary observer, `secondary` = later reconstruction);
  - `whole` (false = counts or locates only part of the division);
  - `seasonal` (a hunt camp etc.).
- **Keyframes** (`GUESS`): (year, place or none, persons or none, note) per division. Ours.
- **Shocks** (`EPI`): (start, end, label, {division: mortality fraction}, source, basis).

## 2. Population

The fit works on log population $x_g(t)$ on an annual grid $t = 1700 \ldots 1905$.

**Shock survival.** For each event $j$ with fraction $f_{gj}$, spread smoothly over $[a_j, b_j]$:
$S_g(t) = \prod_j \left(1 - \min(0.97, f_{gj})\cdot \mathrm{smooth}\!\left(\frac{t - a_j}{b_j - a_j}\right)\right)$, with smooth a 0→1 ramp. The fit estimates the *underlying* curve $u_g(t) = x_g(t) - \log S_g(t)$, and observations are compared after subtracting $\log S_g$ at their date (`surv()`).

**Objective.** For each division, minimise
$$\sum_i \frac{(\ell_i - u_g(t_i))^2}{\sigma_i^2} + \frac{\lVert D_2 u_g\rVert^2}{\sigma_{s}^2} + \frac{\lVert D_1 u_g - r_0\rVert^2}{\sigma_r^2}$$
where:
- $\ell_i$ is the log of a documented count (same-year counts for parts of one division are summed first), a keyframe's persons, or a whole-tribe allocation (below);
- $D_1$ and $D_2$ are first- and second-difference operators;
- the penalties are a smoothness prior on the change in growth rate and a weak prior pulling growth toward $r_0$.

The objective is a linear least-squares solve; the posterior SD comes from the inverse normal matrix (`fit()`).

**Splits and mergers.** Where a division splits from another that goes on, the parent loses the new division's share in the year of the split; where a division ends by merging into another, the survivor gains its people (`data_src.SHIFTS`, `data/division_transfers.csv`). Each fraction is the new division's population in its first year over the parent's in the year before, or the ending division's last-year population over the survivor's, iterated against the fit until each people's total is continuous across the change. The transfers enter $S_g(t)$ as steps completed by the year of the change; they are not scaled in the sensitivity runs. The one remaining step is the Cheyenne in 1832: the counts after the division (about 3,500 for the two halves) run above those before it (about 3,100), a tension in the evidence that a transfer cannot remove.

**Whole-tribe counts.** A count covering several divisions is allocated to its members in proportion to the current fit and enters each member at $1.6\,\sigma$. Fitting and allocation alternate for four iterations.

**Source-family factors.** Each source family is assigned by substring of the source (`family()`). For each family $f$ other than reservation censuses:
1. Refit without $f$'s counts and without any keyframes.
2. Compare $f$'s counts with that fit where the fit's SD is ≤ 0.35.
3. Take the precision-weighted mean log ratio shrunk toward 0 with prior SD $\tau$.

Every count is then divided by its family's factor and the model refitted. Reservation censuses are the fixed reference.

**Reported uncertainty.** The posterior SD × 1.25 (`SD_INFL`), from the leave-one-out calibration (§6). Unwidened, the 1-sd range holds 75% of withheld counts and the 2-sd range 92%; widened, 80% and 96%. The misses are heavier-tailed than normal, so the widening is set by the 2-sd range and leaves the 1-sd range conservative.

| Setting | Value | Meaning | How set |
|---|---|---|---|
| σ census | 0.15 (0.10 if the text says census/roll/enrollment/“numbered”) | any count dated 1868 or later, and any record whose basis is “census” | judgment; checked by hold-out |
| σ Teton agency | 0.30, in a family of its own | Teton agency figures from 1868 until the division settled | Hämäläinen, *Lakota America*, chs. 8–9: inflated for rations, nonagency bands uncounted |
| σ primary | 0.30 | contemporary estimate | judgment; checked by hold-out |
| σ Clark 1805 | 0.35 | Clark's table | judgment; sensitivity ±0.25/0.50 |
| σ secondary | 0.45 | later reconstruction | judgment; sensitivity ±0.30/0.70 |
| σ keyframe | 0.30 | our persons guess | judgment; sensitivity 0.2/0.5/none |
| aggregate inflation | 1.6 | whole-tribe count shared across divisions | judgment |
| $\sigma_s$ (SS) | 0.02 | change in growth rate per year | judgment; median \|z\| of documented counts in sample 0.4; ×½ and ×2 tested |
| $\sigma_r$ (SR) | 0.06 | spread of growth around $r_0$ | judgment; ±0.03/0.12 tested |
| $r_0$ (R0) | 0.005 | background growth, +0.5% a year | judgment; 0 and 1% tested |
| τ (BT) | 0.25 | shrinkage of family factors | judgment; 0.15/0.40 tested |
| SD_INFL | 1.25 | widening of reported SD | leave-one-out coverage of the 2-sd range |
| persons per lodge | source's own; else lodges × 5, warriors × 4, earth lodges × 10 | conversion | flagged on each record (`persons_basis`) |

**Known structural property.** The growth prior ($\sigma_r = 0.06$/yr) makes a sustained decline of more than about 4% a year costly unless a dated shock explains it. Where the record has high early counts and low later censuses with no documented catastrophe in between, the fit discounts the early counts rather than inventing a collapse. The 1840s Comanche are the main case (`KNOWN_ISSUES.md` §1).

## 3. Position

**Records used.**
- Documented places with `loc = stated`, `whole = true`, not `seasonal`.
- Keyframe places, dropped if a documented place lies within one year.
- Ranges ("roam from the Big Shyenne up to the Yellowstone") are placed at the range's centre with the range's radius.

**Nomadic divisions** (`possgp.py`, settings in `build/gpcal.json` from `calib_gp.py`). Position is a quasi-periodic Gaussian process in local km coordinates, per axis:

$$x(t) = T(t) + S(t) + \lambda\,\phi(t)\,A_{\text{lit}}(t), \qquad x_i = x(t_i) + \varepsilon_i .$$

- *The centre* $T$ is the sum of a smooth squared-exponential component (scale 200 km, length 45 years) and a short one (75 km, 4 years) that follows records a few years apart where they agree.
- *The seasonal component* $S$ is the first two annual harmonics, $\cos/\sin 2\pi t$ and $\cos/\sin 4\pi t$ with weights 1 and 0.5, whose amplitudes drift with a squared-exponential kernel (45 km, 8 years).
- *The literature pattern* $A_{\text{lit}}$ (`seasonal_patterns.csv`) enters as a prior mean, timed by the calendar φ and weighted λ = 0.5; half the stated distance did better than the whole.
- *Each record* is a noisy sighting: $\varepsilon_i$ has variance $(0.5\,r_i)^2 + (90\,\rho_g(t_i))^2$ km², where $r_i$ is the stated radius and $\rho_g$ falls from 1 to 0.25 over three years after the division settles on a reservation (`possgp.RES`). A keyframe has variance $150^2$.
- *Which part of the process a record sees.* A place dated to a season sees $T + S$ at its date. A camp with no month sees $T$ plus $S$ averaged over the season-of-record distribution of the dated places (its circular moments, which peak in late July), so it is neither credited to nor scored against a season it cannot be shown to belong to. Ranges, agencies, statements of where a people lived, places dated only to a year, radii over 150 km and keyframes see $T$ alone.
- *The halo* is $1.51\sqrt{\sigma_T^2(t) + R(t)^2}$ per axis, capped at 450 km, where $\sigma_T^2$ is the posterior variance of the centre and $R$ is the spread of camps round it: 114 km in winter, 84 km between, 83 km in summer (interpolated by season), each set so that the halo holds 68% of withheld places of that season (68%, 69% and 68%). With the seasonal round off, $R$ also includes the year's seasonal swing. After a reservation $R$ is scaled by $\rho_g$.
- *The map* receives the yearly centre and, for each year, the eight harmonic coefficients of $S$ plus the literature term, evaluated at the fraction of the year.

**Test** (`calib_gp.py`). Each documented place is withheld with every place of its division within half a year and predicted from the rest. Settings are chosen on a grid by hold-out over half the divisions and scored on the other half, then the reverse; the table gives those out-of-sample figures. The production settings are then tuned on all divisions together. Each division is fitted once, and each withheld block is removed from that fit exactly, through the inverse covariance, rather than refitted; a refit for every place (`CALIB_SLOW=1`) gives the same results to 10⁻¹¹ km, and the whole grid runs in about a minute, so it is rerun whenever records are added. Season-dated places are scored at their date, the others against the year's centre. Misses are also measured beyond each record's stated radius, so that a place given only as "on the Arkansas" is not counted as missed when the prediction falls within it.

| | places | median miss | mean miss | beyond the stated radius, median |
|---|---|---|---|---|
| Track through every record (monotone cubic) | 660 | 125 km | 155 km | |
| Centre only | 660 | 121 km | 147 km | 66 km |
| Centre and seasonal component | 660 | 119 km | 147 km | 64 km |
| Season-dated places: track through every record | 406 | 132 km | 165 km | |
| Season-dated places: centre only | 406 | 124 km | 154 km | 84 km |
| Season-dated places: centre and seasonal component | 406 | 122 km | 153 km | 82 km |
| Ranges and agencies: track through every record | 212 | 96 km | 131 km | |
| Ranges and agencies: centre and seasonal component | 212 | 106 km | 129 km | 17 km |

- With the production settings, tuned on all divisions, the miss is 113 km (mean 143) over the 660 places, 117 km (mean 149) on the season-dated places, and 118 km (mean 149) without our keyframes. These are a little better than the out-of-sample figures because the settings have seen every division.
- The seasonal component is worth little on season-dated places out of sample (124 to 122 km); the rest of the gain over a track through every record comes from averaging several years of records. The Kiowa calendar, the densest record, shows why: a summer sun-dance ground lies a median 155 km from the next winter camp, but winter camps a median 129 km from the winter before and summer grounds 140 km from the summer before, in no fixed direction.
- Range and agency statements are served about as well by a track through every record (median 96 km against 106, mean 131 against 129).
- The cost falls on precise events in years of mixed records: in 1876 the Miniconjou annual centre lies between the Cheyenne River agency and the summer camps, about 385 km from the Little Bighorn (about 245 km in late June with the seasonal component).

**Village divisions.** The track holds at each place. With the seasonal round on, the division's dot and its bands go out on the tribal hunts in the hunt table (`index.html`, `HUNT`: grounds and calendars by people) and return; the track itself stays at the village.
- Where `ecology_src.VMOVE` dates a relocation, the move happens over about five months around that date.
- Otherwise it moves over two years centred on the midpoint between the two places.
- The halo is 24 km + 1.25 × (distance to the next place × the share of the gap elapsed, up to half), capped at 300 km; where the move is dated, the distance term applies only within a year of it. The two terms are fitted to 243 withheld village places (`calib_vhalo.py`) as the halo that holds 68% of them with coverage most even across strata of time and distance from the nearest place. A term in the years from the nearest place was tried and not chosen. Coverage is 59% within three years of another record and 76% three to ten years from one (`KNOWN_ISSUES.md` §7).
- Held out (`calib_vmove.py`), the 222 village places of the peoples with dated moves are missed by a median 8 km and a mean 43 km (the midpoint rule alone: 17 and 70).

**Seasonal round (on by default).** The map adds $S$ and the literature term to the centre at the month shown. With the seasonal round off, each division is drawn twice at half its population, at its winter ground (the middle of the winter-ground period of the calendar φ, the turn of the year) and at its summer ground (mid-July) for the year, so that the default picture of a year shows its range rather than the annual centre alone; at the bands level each band is placed on one ground or the other. Where a division has neither season-dated places within about eight years nor a literature pattern, $S$ is zero and only the bands' scatter moves with the seasons. The calendar φ (winter ground to mid-March, summer ground by early July until early August, back by late October; `build/profcal.json`) times the literature patterns and the bands; the learned component keeps its own timing.

## 4. Bands and villages (derived layer)

- One ethnographic band list per division, dated to the year it describes (`bands_src.py`). Band names are documented; the weights, budding order and positions are not.
- Division population is divided among the bands alive in a year. The bands' number follows population at a median band size of about 210.
- Band positions are the division centre plus a shared annual shift and band scatter, drawn from a fixed random seed with scales from the Kiowa calendar camps.
- Documented band places (`band_places_recalled.csv`; most recalled from standard histories, see `JUDGMENTS.md` §10) override the draw.

## 5. Settler states, territories and reservations (reference layer)

A switchable layer shows, for the year on the timeline, the claims of the European and American powers, the organized territories, provinces and districts, the states and provinces (with the Republic of Texas), the Confederate states during the war, and the reservations and reserves. It is reference only: nothing in the population or position model reads it.

- *Construction* (`settler_src.py`, `build_settler.py` → `build/settler.json`, `settler.js`, `data/settler_boundaries.geojson`). Each feature is built from modern state and province outlines (Natural Earth admin-1, kept in `model/geo/admin1.json`), the rivers of the base map, and the meridians, parallels and divides the treaties and organic acts name: the Adams–Onís line, the 49th parallel, the summit of the Rockies, the Missouri and White Earth rivers, the Rio Grande to its source and north to 42° for the Texan claim, and so on. A feature lasts from the day its act or treaty took effect to the day the next one changed it.
- *Levels.* Claims (sovereignty asserted: New France, New Spain, Rupert's Land, the United States, Mexico, Canada) are drawn faint and dotted; land the United States held outside any state or territory is the residual of the others, dashed; territories, provinces and districts in a mid tone; states and provinces in full ink. The Confederate states, and the Confederate Territory of Arizona, are drawn in red from secession to the surrender in the West (June 1865).
- *The nations of the Indian Territory.* The Cherokee, Creek, Seminole, Choctaw and Chickasaw held their land by patent under the removal treaties, governed themselves, and were promised never to be put in a state or territory without consent. That is neither a reservation (land the United States set apart and could reduce at will) nor a territory, so they are a level of their own: a faint wash with a dash-dot line, changing with the treaties of 1828–38, 1855–56 and 1866 (the Cherokee Outlet, the Leased District, the Creek–Seminole partitions). The Indian Territory itself is drawn as unorganized American land around them.
- *Provinces held and claimed.* The Spanish and Mexican provinces are drawn as provinces only along their settled corridors (the Rio Grande from Taos to El Paso; San Antonio to La Bahía and Nacogdoches to Los Adaes; the mission coast of Alta California) and as claims beyond them, after Hämäläinen's point that such maps "confuse outlandish imperial claims for actual holdings" (*Indigenous Continent*, introduction). The corridors are ours.
- *Treaty land outside the reservations.* The unceded Indian territory of article 16 of the 1868 Fort Laramie treaty, 1868–77, is drawn with the Indian Territory nations; its northern edge is ours.
- *Reservations* take the ink of the people they were made for and appear on the date of the treaty or order that made them; each reduction is a new feature. Small reservations are boxes on their location.
- *Sources.* The dates and the defining lines are recalled from Van Zandt, *Boundaries of the United States and the Several States* (1976), the Newberry Library's *Atlas of Historical County Boundaries*, the *Atlas of Canada*'s territorial evolution maps, Gerhard, *The North Frontier of New Spain* (1982), and Royce, *Indian Land Cessions* (1899); they have not been checked against those works page by page. The lines are approximate throughout (`KNOWN_ISSUES.md` §13).

## 6. Tests

| Test | Script | Output | Result |
|---|---|---|---|
| Leave-one-out population | `validate.py` | `model/build/validation.json`, `data/validation.csv` | 1,242 counts; median miss ×1.11 (interpolation ×1.08; before 1840 the model is better, after it interpolation); 2-sd coverage 0.92 before widening, 0.96 after |
| Held-out nomadic places | `calib_gp.py` | `model/build/gpcal.json` | 660 places out of sample; median 119 km, mean 147 (track through every record 125, 155); season-dated 122 against 124 without the seasonal component; halo 68% in each season |
| Held-out village places | `calib_vmove.py` | console | 222 places; median 8 km, mean 43 |
| Village halo coverage | `calib_vhalo.py` | console | 243 places; median miss 11 km; 68% inside |
| Whole-model sensitivity | `sens.py` | `model/build/sensitivity.json` | table under “Sensitivity of the population totals” on the map page |
| Rebuild from package | — | — | bit-identical populations and tracks |

What none of these tests can catch:
- a record that misreports its source;
- a systematic bias shared by every source for a people (all early observers counting from one trading post);
- a keyframe that is wrong where nothing documented lies nearby to contradict it.

`REVIEW_PROTOCOL.md` addresses the first two directly.
