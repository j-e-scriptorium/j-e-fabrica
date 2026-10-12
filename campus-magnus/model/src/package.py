"""Build the review package: data tables with provenance and judgment flags, coverage and fit diagnostics.
usage: python3 package.py <src dir> <project dir> <out dir>"""
import json, csv, sys, os, re, math, collections, shutil
sys.path.insert(0, sys.argv[1]); S = sys.argv[2]; OUT = sys.argv[3]
import data_src as D, ecology_src as EC, provenance as P
d = json.load(open(f'{S}/build/data.json', encoding='utf-8'))
G = {g['id']: g for g in d['groups']}
os.makedirs(f'{OUT}/data', exist_ok=True)


def W(name, head, rows):
    with open(f'{OUT}/data/{name}', 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f); w.writerow(head); w.writerows(rows)
    return len(rows)


def alive(g, y): return G[g]['start'] <= y <= G[g]['end']
def fitted(gs, y):
    k = int(round(y - 1700)); k = max(0, min(205, k))
    v = [d['tracks'][g]['pa'][k] for g in gs if alive(g, y) and g in d['tracks']]
    return sum(v) if v else None


LOC = re.compile(r'\bpp?\. ?\d|table \d|entry|no\. \d|fig\. \d|ch\. |calendar|chapter|winter count|\bvol\. \d+, p')
# ---------- documented records ----------
val = {(p[0], round(p[1], 2)): p for p in json.load(open(f'{S}/build/validation.json'))['points']}
rec = []; tiers = collections.Counter()
YS = collections.defaultdict(float)
for o in d['obs']:
    if o.get('pop') and len(o['g']) == 1 and o.get('whole', True): YS[(o['g'][0], o['y'])] += o['pop']
for n, o in enumerate(sorted(d['obs'], key=lambda o: (o['y'], o['g'][0])), 1):
    gs = o['g']; t = P.tier(o['src']); tiers[t] += 1
    fl = P.flags(o['raw'], o.get('basis', ''), o.get('loc', ''), o.get('whole', True))
    on_track = o.get('lat') is not None and o.get('loc') == 'stated' and o.get('whole', True) and not o.get('seasonal')
    fit = fitted(gs, o['y']) if o.get('pop') else None
    summed = len(gs) == 1 and o.get('pop') and o.get('whole', True) and YS[(gs[0], o['y'])] != o['pop']
    docv = YS[(gs[0], o['y'])] if summed else o.get('pop')
    v = val.get((gs[0], round(o['y'], 2))) if (o.get('pop') and len(gs) == 1) else None
    rec.append([f'R{n:04d}', round(o['y'], 3), ';'.join(gs), G[gs[0]]['tribe'],
                'several divisions' if len(gs) > 1 else G[gs[0]]['name'],
                o['pop'] if o.get('pop') is not None else '', o.get('basis', ''), o['raw'],
                o.get('loc', ''), o.get('lat', ''), o.get('lon', ''), o.get('r', ''),
                'yes' if o.get('seasonal') else '', 'no' if o.get('whole') is False else 'yes',
                'yes' if on_track else 'no', o['src'], t, 'yes' if LOC.search(o['src']) else 'no',
                o['kind'], o.get('fam', ''), o.get('famf', ''),
                fit if fit is not None else '', round(docv / fit, 2) if (fit and o.get('pop')) else '', 'yes' if summed else '',
                v[3] if v else '', v[4] if v else '', ';'.join(fl)])
W('records.csv', ['record_id', 'year', 'group_ids', 'tribe', 'scope', 'persons', 'persons_basis', 'source_says',
                  'place_status', 'lat', 'lon', 'place_radius_km', 'season_dated', 'counts_whole_group',
                  'steers_track', 'source', 'provenance_tier', 'source_has_locator', 'kind', 'source_family',
                  'source_family_factor', 'fitted_persons_in_sample', 'documented_over_fitted', 'summed_with_same_year_records',
                  'leave_one_out_prediction', 'leave_one_out_z', 'judgment_flags'], rec)

# ---------- sources ----------
def stem(s):
    s = re.sub(r'[,;]? ?(pp?\.|entry|table|no\.|calendar ent|ch\.) .*$', '', s)
    return s.strip()
src = collections.defaultdict(lambda: [0, 0, set(), set()])
for r in rec:
    k = stem(r[15]); src[k][0] += 1; src[k][1] += 1 if r[5] != '' else 0; src[k][2].add(r[16]); src[k][3].add(r[3])
W('sources.csv', ['source', 'records', 'of_which_counts', 'provenance_tier', 'peoples'],
  sorted([[k, v[0], v[1], '/'.join(sorted(v[2])), '; '.join(sorted(v[3]))] for k, v in src.items()], key=lambda x: -x[1]))

# ---------- keyframes (our guesses) ----------
kf = []; n = 0
for gid, L in D.GUESS.items():
    docy = [p[0] for p in d['tracks'][gid]['pos'] if p[3] == 'o'] if gid in d['tracks'] else []
    for (y, pl, pp, note) in L:
        n += 1
        if isinstance(pl, str): pl = D.P.get(pl, pl)
        over = any(abs(y - q) < 1.0 for q in docy) and pl is not None
        kf.append([f'K{n:04d}', gid, G[gid]['tribe'], G[gid]['name'], y,
                   pl[0] if isinstance(pl, (tuple, list)) else '', pl[1] if isinstance(pl, (tuple, list)) else '',
                   pp if pp else '', note or '', 'yes' if not note else '',
                   'place+persons' if (pl is not None and pp) else ('place only' if pl is not None else ('persons only' if pp else 'marker only (defers to records)')),
                   'place overridden by a documented place within a year' if over else ''])
W('keyframes_our_guesses.csv', ['keyframe_id', 'group_id', 'tribe', 'division', 'year', 'lat', 'lon', 'persons_guess',
                                'note', 'no_stated_basis', 'role', 'status'], kf)

# ---------- epidemics ----------
ep = []
for i, (s_, e, lab, M, srcs, basis) in enumerate(D.EPI, 1):
    for g, f in M.items():
        ep.append([f'E{i:03d}', s_, e, lab, g, G[g]['name'], f, basis, P.tier(srcs), srcs])
W('epidemics_and_shocks.csv', ['event_id', 'start', 'end', 'event', 'group_id', 'division', 'mortality_fraction',
                               'rate_basis', 'provenance_tier', 'source'], ep)

# ---------- groups ----------
W('groups.csv', ['group_id', 'tribe', 'division', 'language_family', 'start', 'end', 'lifeway'],
  [[g['id'], g['tribe'], g['name'], g['fam'], g['start'], g['end'], g.get('life', '')] for g in d['groups']])

# ---------- coverage ----------
PER = [(1700, 1749), (1750, 1799), (1800, 1824), (1825, 1849), (1850, 1874), (1875, 1905)]
cov = []
for g in d['groups']:
    gid = g['id']
    if g['fam'] == 'unident' or gid not in d['tracks']: continue
    pos = d['tracks'][gid]['pos']
    for a, b in PER:
        lo, hi = max(a, g['start']), min(b, g['end'])
        if lo > hi: continue
        cnt = [r for r in rec if gid in r[2].split(';') and r[5] != '' and r[13] == 'yes' and lo <= r[1] <= hi + .999]
        cnt1 = [r for r in cnt if r[2] == gid]
        pl = [p for p in pos if p[3] == 'o' and lo <= p[0] <= hi + .999]
        kfp = [p for p in pos if p[3] == 'g' and lo <= p[0] <= hi + .999]
        ys = sorted([lo] + [p[0] for p in pl] + [hi + 1])
        gap = max(b_ - a_ for a_, b_ in zip(ys, ys[1:]))
        sd = d['tracks'][gid]['sd'][lo - 1700:hi - 1700 + 1]
        hal = d['tracks'][gid]['sp'][lo - 1700:hi - 1700 + 1]
        cov.append([gid, g['tribe'], g['name'], f'{lo}–{hi}', len(cnt1), len(cnt) - len(cnt1), len(pl), len(kfp),
                    round(gap, 1), round(sum(sd) / len(sd)) if sd else '', round(sum(hal) / len(hal)) if hal else '',
                    'thin' if (len(pl) == 0 and len(cnt) == 0) else ('sparse' if gap > 25 else '')])
W('coverage_by_division_and_period.csv', ['group_id', 'tribe', 'division', 'period', 'counts_for_division',
                                          'counts_shared_with_other_divisions', 'documented_places_on_track',
                                          'keyframe_places_on_track', 'longest_gap_without_documented_place_years',
                                          'mean_population_sd_percent', 'mean_halo_km', 'flag'], cov)

# ---------- fitted series ----------
gids = [g['id'] for g in d['groups'] if g['fam'] != 'unident']
W('fitted_population_by_division.csv', ['year'] + gids,
  [[1700 + k] + [(d['tracks'][g]['pa'][k] if alive(g, 1700 + k) else '') for g in gids] for k in range(206)])
W('fitted_population_sd_percent.csv', ['year'] + gids,
  [[1700 + k] + [(d['tracks'][g]['sd'][k] if alive(g, 1700 + k) else '') for g in gids] for k in range(206)])
tribes = sorted({G[g]['tribe'] for g in gids})
W('fitted_population_by_people.csv', ['year'] + tribes,
  [[y] + [sum(d['tracks'][g]['pa'][y - 1700] for g in gids if G[g]['tribe'] == t and alive(g, y) and not (G[g]['end'] == y and y < 1905 and any(G[h]['tribe'] == t and G[h]['start'] == y for h in gids)))
          for t in tribes] for y in range(1700, 1906)])

# ---------- copies of existing exports ----------
for f in ['plains_positions.csv', 'plains_seasonal_patterns.csv', 'plains_village_moves.csv', 'plains_settlements.csv',
          'plains_bands.csv', 'plains_band_population.csv', 'plains_band_places_recalled.csv', 'plains_band_events.csv',
          'plains_bison_range.csv', 'plains_validation.csv']:
    shutil.copy(f'{S}/out/{f}', f'{OUT}/data/{f.replace("plains_", "")}')

json.dump(dict(tiers=tiers, records=len(rec), keyframes=len(kf), epidemic_rows=len(ep),
               keyframes_without_note=sum(1 for k in kf if k[9]), keyframe_roles=collections.Counter(k[10] for k in kf), counts=sum(1 for r in rec if r[5] != ''),
               places_only=sum(1 for r in rec if r[5] == ''), steer=sum(1 for r in rec if r[14] == 'yes'),
               with_locator=sum(1 for r in rec if r[17] == 'yes'),
               flags=collections.Counter(f for r in rec for f in r[26].split(';') if f),
               coverage_thin=sum(1 for c in cov if c[11] == 'thin'), coverage_rows=len(cov),
               epi_basis=collections.Counter(e[7].split(';')[0][:40] for e in ep)),
          open(f'{OUT}/data/_summary.json', 'w'), ensure_ascii=False, indent=1)
print('ok', tiers, len(rec), len(kf), len(ep), len(cov))
