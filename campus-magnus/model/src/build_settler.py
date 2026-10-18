"""usage: python3 build_settler.py <model dir>   (writes build/settler.json: the settler states, territories, claims and
reservations of settler_src.py, simplified and clipped to the map, with a label point for each)"""
import sys, json, os
from shapely.geometry import mapping, box, MultiPolygon, Polygon
from shapely.geometry.polygon import orient
import settler_src as S
M = sys.argv[1] if len(sys.argv) > 1 else '..'
CLIP = box(-127, 22, -85.5, 61.5); VIEW = box(-115.5, 27.6, -88.5, 55.2)
def rnd(o):
    if isinstance(o, (list, tuple)):
        if o and isinstance(o[0], (int, float)): return [round(o[0], 2), round(o[1], 2)]
        return [rnd(x) for x in o]
    return o
out = []
for f in S.F:
    g = f['geom'].intersection(CLIP)
    if g.geom_type == 'GeometryCollection':
        ps = [p for p in g.geoms if p.geom_type in ('Polygon', 'MultiPolygon')]
        g = MultiPolygon([q for p in ps for q in getattr(p, 'geoms', [p])]) if ps else Polygon()
    if g.is_empty or not g.intersects(VIEW): continue
    tol = 0.006 if f['level'] == 'res' else 0.02
    g = g.simplify(tol, preserve_topology=True)
    if g.is_empty: continue
    v = g.intersection(VIEW)
    lp = v.representative_point() if not v.is_empty else g.representative_point()
    # round, drop slivers that rounding collapses (d3 reads a degenerate ring as a hemisphere), and orient clockwise for d3-geo
    from shapely import set_precision
    g = set_precision(g, 0.01).buffer(0)
    minA = 0.003 if f['level'] == 'res' else 0.02
    ps = [p for p in getattr(g, 'geoms', [g]) if p.geom_type == 'Polygon' and p.area >= minA]
    if not ps: continue
    g = MultiPolygon([orient(Polygon(p.exterior, [i for i in p.interiors if Polygon(i).area >= minA]), sign=-1.0) for p in ps])
    m = mapping(g)
    rec = dict(id=f['id'], n=f['name'], lv=f['level'], ow=f['owner'], y0=f['y0'], y1=f['y1'], src=f['src'],
               lab=[round(lp.x, 2), round(lp.y, 2)], a=round(v.area, 2), g=dict(type=m['type'], coordinates=rnd(m['coordinates'])))
    if f['id'].startswith('unorg'): rec['nd'] = 1
    for k in ('csa', 'note', 'tribes', 'sub'):
        if f.get(k): rec[k] = f[k]
    out.append(rec)
json.dump(out, open(os.path.join(M, 'build', 'settler.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(out), 'features', os.path.getsize(os.path.join(M, 'build', 'settler.json')) // 1024, 'kB')
