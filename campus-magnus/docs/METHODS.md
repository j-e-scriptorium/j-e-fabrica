# Methods: formal specification

This file states the model as the code implements it, with every setting and how it was chosen. Line references are to `model/src/build3.py` unless stated. the “About the data” section of the map page gives the same choices in prose with their rationale and measured effects.

## 1. Units and inputs

- **Unit.** A *division* $g$ (59 in all) with a lifespan $[s_g, e_g]$ and a lifeway (`nomadic` or `village`). A people (tribe) is the sum of its divisions. A division that splits ends in the year its successors begin; for example the Cheyenne end in 1832 and the Northern and Southern Cheyenne begin then.
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
$S_g(t) = \prod_j \left(1 - \min(0.97, f_{gj})\cdot \mathrm{smooth}\!\left(\frac{t - a_j}{b_j - a_j}\right)\right)$, with smooth a 0→1 ramp. The fit estimates the *underlying* curve $u_g(t) = x_g(t) - \log S_g(t)$, and observations are compared after subtracting $\log S_g$ at their date (lines 26–31, 103–109).

**Objective.** For each division, minimise
$$\sum_i \frac{(\ell_i - u_g(t_i))^2}{\sigma_i^2} + \frac{\lVert D_2 u_g\rVert^2}{\sigma_{s}^2} + \frac{\lVert D_1 u_g - r_0\rVert^2}{\sigma_r^2}$$
where:
- $\ell_i$ is the log of a documented count (same-year counts for parts of one division are summed first), a keyframe's persons, or a whole-tribe allocation (below);
- $D_1$ and $D_2$ are first- and second-difference operators;
- the penalties are a smoothness prior on the change in growth rate and a weak prior pulling growth toward $r_0$.

The objective is a linear least-squares solve; the posterior SD comes from the inverse normal matrix (lines 103–117).

**Whole-tribe counts.** A count covering several divisions is allocated to its members in proportion to the current fit and enters each member at $1.6\,\sigma$. Fitting and allocation alternate for four iterations (lines 118–132).

**Source-family factors.** Each source family is assigned by substring of the source (`family()`, lines 43–52). For each family $f$ other than reservation censuses:
1. Refit without $f$'s counts and without any keyframes.
2. Compare $f$'s counts with that fit where the fit's SD is ≤ 0.35.
3. Take the precision-weighted mean log ratio shrunk toward 0 with prior SD $\tau$.

Every count is then divided by its family's factor and the model refitted (lines 136–172). Reservation censuses are the fixed reference.

**Reported uncertainty.** The posterior SD × 1.25 (`SD_INFL`), from the leave-one-out calibration (§5).

| Setting | Value | Meaning | How set |
|---|---|---|---|
| σ census | 0.15 (0.10 if the text says census/roll/enrollment/“numbered”) | any count dated 1868 or later, and any record whose basis is “census” | judgment; checked by hold-out |
| σ primary | 0.30 | contemporary estimate | judgment; checked by hold-out |
| σ Clark 1805 | 0.35 | Clark's table | judgment; sensitivity ±0.25/0.50 |
| σ secondary | 0.45 | later reconstruction | judgment; sensitivity ±0.30/0.70 |
| σ keyframe | 0.30 | our persons guess | judgment; sensitivity 0.2/0.5/none |
| aggregate inflation | 1.6 | whole-tribe count shared across divisions | judgment |
| $\sigma_s$ (SS) | 0.02 | change in growth rate per year | set so median \|z\| of documented counts ≈ 0.6 |
| $\sigma_r$ (SR) | 0.06 | spread of growth around $r_0$ | judgment; ±0.03/0.12 tested |
| $r_0$ (R0) | 0.005 | background growth, +0.5% a year | judgment; 0 and 1% tested |
| τ (BT) | 0.25 | shrinkage of family factors | judgment; 0.15/0.40 tested |
| SD_INFL | 1.25 | widening of reported SD | leave-one-out coverage |
| persons per lodge | source's own; else lodges × 5, warriors × 4, earth lodges × 10 | conversion | flagged on each record (`persons_basis`) |

**Known structural property.** The growth prior ($\sigma_r = 0.06$/yr) makes a sustained decline of more than about 4% a year costly unless a dated shock explains it. Where the record has high early counts and low later censuses with no documented catastrophe in between, the fit discounts the early counts rather than inventing a collapse. The 1840s Comanche are the main case (`KNOWN_ISSUES.md` §1).

## 3. Position

**Anchors.**
- Documented places with `loc = stated`, `whole = true`, not `seasonal`. A same-year group is averaged, weighted by persons.
- Keyframe places, dropped if a documented place lies within one year (lines 63–76).
- Ranges ("roam from the Big Shyenne up to the Yellowstone") are placed at the range's centre.

**Nomadic divisions.**
- *The drawn centre* is a monotone cubic (Hermite) curve through every anchor in order, which never overshoots.
- *Its uncertainty* comes from a random-walk Kalman filter and RTS smoother run through the same anchors in local km coordinates (`possmooth.py`). The settings are as follows; the first three were fitted by holding out documented places (`calib_pos.py`, `build/poscal.json`):
  - process variance $q$ = 2,000 km² a year per axis;
  - a documented place has variance $(0.25 r)^2 + 90^2$;
  - a keyframe has variance $150^2$;
  - the halo radius is $1.46\sqrt{P_t + 90^2}$, capped at 450 km, where 1.46 makes the halo contain 68% of withheld places (`calib_halo.py`).
- Held-out median miss: 107 km for the smoother (110 km without keyframes) and 108 km for the drawn curve (123 km without keyframes), over 518 places, each withheld with any other place within half a year (`calib_pos.py`, `calib_track.py`, `build/trackcal.json`). The smoother parameters were fitted on an earlier, smaller record set (380 places) and not refitted.

**Village divisions.** The track holds at each place.
- Where `ecology_src.VMOVE` dates a relocation, the move happens over about five months around that date.
- Otherwise it moves over two years centred on the midpoint between the two places.
- The halo is a hand-set formula: 20 km + (distance to next site × fraction of the gap elapsed) + 3 km per year from the nearest anchor, capped at 300 km. **This formula is not calibrated.**
- The held-out median miss for village places is 45 km over 245 places (52 km without keyframes).

**Seasonal offset (optional layer).**
- The annual offset $A_g(t)$ (summer ground minus annual centre, km east and north) is estimated from season-dated places within about 5 years (exponential weights, τ = 5 yr). It is shrunk toward a literature pattern (`seasonal_patterns.csv`) or toward zero, with prior SD 60 km per axis.
- Within the year, position = centre + φ(month)·A, with a plateau-and-ramp calendar fitted by hold-out (`calib_prof.py`): winter ground to mid-March, summer ground by early July until early August, back by late October.
- Season-dated places are reproduced exactly.
- Hold-out: on 297 withheld season-dated places the median miss is 120 km with the offset and 120 km without it (mean 139 against 141). Withholding every place within half a year of the test place, 117 against 122 km (mean 149 against 151; `recheck_seas_block.py`). Sourced literature patterns account for most of that gain; season-dated camps of single bands, pooling across a people's divisions and retuning the kernel and shrinkage gained at most 1% and were not adopted.

**Seasonal round: an alternative tested** (`seas_gp.py`).
- The model: a quasi-periodic Gaussian process for each nomadic division, a smooth long-term track plus a seasonal component (first two annual harmonics) whose shape and strength are learned from the records and drift over about eight years. Places dated to a month carry their phase. Camps with no month (35) carry the season-of-record distribution of the dated places, which peaks in late July, so they are neither credited to nor scored against a season they cannot be shown to belong to. Range and agency statements (183) and our keyframes observe only the annual mean.
- The test: the 297 season-dated places, each withheld with every place within half a year; settings tuned on half the divisions and scored on the other half, then the reverse. Misses are also measured beyond each record's own stated radius (a median of 25 km), so that a place given only as "on the Arkansas" is not counted as missed when the prediction falls within it.

| | median miss | mean miss | beyond the stated radius, median |
|---|---|---|---|
| Drawn track, no seasonal move | 122 km | 151 km | |
| Drawn track with the seasonal offset above | 117 km | 149 km | |
| Gaussian process, long-term track only | 115 km | 148 km | 78 km |
| Gaussian process, track and seasonal component | 112 km | 145 km | 75 km |

- The seasonal component itself is worth about 3%. Most of the process's advantage comes from its smoother long-term track, which averages several years of records instead of passing through each one.
- Why the seasonal gain is small: the Kiowa calendar, the densest record, puts a summer sun-dance ground a median 155 km from the next winter camp, but winter camps a median 129 km from the winter before and summer grounds 140 km from the summer before, in no fixed direction. Each season's ground moved from year to year almost as far as the seasons were apart, so a seasonal pattern can explain only a small part of where a division was.
- Not adopted on the map: the process's track does not pass through every documented place, which the map's tracks do by design (`JUDGMENTS.md`). The seasonal offset of the map is kept.

## 4. Bands and villages (derived layer)

- One ethnographic band list per division, dated to the year it describes (`bands_src.py`). Band names are documented; the weights, budding order and positions are not.
- Division population is divided among the bands alive in a year. The bands' number follows population at a median band size of about 210.
- Band positions are the division centre plus a shared annual shift and band scatter, drawn from a fixed random seed with scales from the Kiowa calendar camps.
- Documented band places (`band_places_recalled.csv`; most recalled from standard histories, see `JUDGMENTS.md` §6) override the draw.

## 5. Tests

| Test | Script | Output | Result |
|---|---|---|---|
| Leave-one-out population | `validate.py` | `model/build/validation.json`, `data/validation.csv` | 1,071 counts; median miss ×1.11 (interpolation ×1.08; before 1840 the model is better, after it interpolation); 2-sd coverage 0.92 before widening |
| Held-out places | `calib_pos.py`, `calib_halo.py` | `model/build/poscal.json` | median 107 km nomadic (smoother), 108 km (drawn curve), 45 km village |
| Withheld season-dated places | `recheck_seas.py` | console | 297 places; median 120 against 120 km, mean 139 against 141; block hold-out (`recheck_seas_block.py`) 117 against 122 |
| Whole-model sensitivity | `sens.py` | `model/build/sensitivity.json` | table under “Sensitivity of the population totals” on the map page |
| Rebuild from package | — | — | bit-identical populations and tracks |

What none of these tests can catch:
- a record that misreports its source;
- a systematic bias shared by every source for a people (all early observers counting from one trading post);
- a keyframe that is wrong where nothing documented lies nearby to contradict it.

`REVIEW_PROTOCOL.md` addresses the first two directly.
