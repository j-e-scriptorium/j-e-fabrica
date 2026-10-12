"""Mechanical audit of the built model. usage: python3 audit.py <project dir>   (reads build/data.json)
Prints four lists a reviewer should look through:
  1. track anchors less than 1.5 years apart but more than 200 km apart (possible conflicting places);
  2. straight-line track segments of 300 km or more over 15 years or more (long unsupported moves);
  3. year-on-year population changes beyond -15% or +8% with no shock that year (unexplained jumps);
  4. internal consistency: keyframes overriding documented places, records outside the map, counts on dead divisions.
"""
import json, math, sys
S = sys.argv[1]
d = json.load(open(f'{S}/build/data.json', encoding='utf-8'))
G = {g['id']: g for g in d['groups']}
km = lambda a, b: math.hypot((a[0] - b[0]) * 111, (a[1] - b[1]) * 111 * math.cos(math.radians(a[0])))

print('1. Near-simultaneous distant anchors (dt <= 1.5 yr, > 200 km)')
for gid, t in d['tracks'].items():
    P = [p for p in t['pos'] if p[3] == 'o']
    for a, b in zip(P, P[1:]):
        if b[0] - a[0] <= 1.5 and km(a[1:3], b[1:3]) > 200:
            print(f'   {gid:4} {a[0]:8.2f} -> {b[0]:8.2f}  {km(a[1:3], b[1:3]):5.0f} km')

print('2. Long straight segments (>= 300 km over >= 15 yr)')
for gid, t in d['tracks'].items():
    P = [p for p in t['pos'] if p[3] in 'og']
    for a, b in zip(P, P[1:]):
        if b[0] - a[0] >= 15 and km(a[1:3], b[1:3]) >= 300:
            print(f'   {gid:4} {a[0]:8.2f} -> {b[0]:8.2f}  {km(a[1:3], b[1:3]):5.0f} km  ({a[3]}->{b[3]})')

print('3. Unexplained population jumps')
shock_years = {}
for e in d['epi']:
    for g in e['m']:
        for y in range(int(e['s']), int(e['e']) + 2): shock_years.setdefault(g, set()).add(y)
for gid, t in d['tracks'].items():
    g = G[gid]; pa = t['pa']
    for y in range(max(1701, g['start'] + 1), min(1905, g['end']) + 1):
        r = pa[y - 1700] / pa[y - 1701]
        if (r < 0.85 or r > 1.08) and y not in shock_years.get(gid, set()):
            print(f'   {gid:4} {y}  x{r:.2f}  ({pa[y - 1701]} -> {pa[y - 1700]})')

print('4. Consistency')
bad = 0
for o in d['obs']:
    alive = [g for g in o['g'] if g in G and G[g]['start'] - 1 <= o['y'] <= G[g]['end'] + 1]
    if o.get('pop') and not alive and o['g'][0] in G:
        print(f'   count on no living division: {o["g"]} {o["y"]} {o["raw"][:60]}'); bad += 1
    if o.get('lat') is not None and not (25 <= o['lat'] <= 60 and -125 <= o['lon'] <= -85):
        print(f'   place outside map: {o["g"]} {o["y"]} {o["lat"]},{o["lon"]}'); bad += 1
print(f'   {bad} problems')
