# Settler states, territories and claims on and around the plains, 1700–1905, and the reservations (METHODS.md §5).
# Every boundary is built here from modern state outlines (Natural Earth, model/geo/admin1.json), the rivers of the base map,
# and the meridians, parallels and divides that the treaties and organic acts name. The lines are approximate; each feature
# carries the act or treaty that made it and the date it took effect. Sources recalled, not reread: Van Zandt, Boundaries of
# the United States and the Several States (USGS Bulletin 1212, 1966); the Newberry Library's Atlas of Historical County
# Boundaries; Natural Resources Canada, Atlas of Canada, Territorial Evolution; Gerhard, The North Frontier of New Spain (1982).
# Levels: claim (sovereignty asserted), unorg (held but unorganized), terr (organized territory, province or district),
# state (state or province with self-government, and the Republic of Texas), res (reservation or reserve).
import json, os
from shapely.geometry import shape, box, Polygon, Point, LineString
from shapely.ops import unary_union, substring, linemerge

HERE = os.path.dirname(os.path.abspath(__file__))
_A = json.load(open(os.path.join(HERE, '..', 'geo', 'admin1.json')))
_G = json.load(open(os.path.join(HERE, '..', 'build', 'geo.json')))
EXT = box(-126, 22, -79, 61.5)
LAND = shape(_G['land']).buffer(0).intersection(EXT)
def _a(k): return shape(_A[k]).buffer(0)
def US(n): return _a('USA:' + n)
def CA(n): return _a('CAN:' + n)
def MX(n): return _a('MEX:' + n)
US_ALL = unary_union([shape(v).buffer(0) for k, v in _A.items() if k.startswith('USA:')])
CA_ALL = unary_union([shape(v).buffer(0) for k, v in _A.items() if k.startswith('CAN:')])
MX_ALL = unary_union([shape(v).buffer(0) for k, v in _A.items() if k.startswith('MEX:')])

def P(*latlon): return [(lo, la) for la, lo in latlon]          # vertices written (lat, lon)
def poly(*parts):
    pts = [q for part in parts for q in part]
    return Polygon(pts).buffer(0)
def band(s, n): return box(-130, s, -70, n)                      # latitude band
def lon(w, e): return box(w, 15, e, 65)                          # longitude band
def west(x): return box(-130, 15, x, 65)
def east(x): return box(x, 15, -70, 65)
def north(y): return box(-130, y, -70, 65)
def south(y): return box(-130, 15, -70, y)

def _chain(segs):
    """join river segments into one ordered line, nearest end to nearest end"""
    segs = [list(s.coords) for s in segs]
    segs.sort(key=lambda c: -LineString(c).length)
    line = segs.pop(0)
    while segs:
        best = None
        for i, c in enumerate(segs):
            for rev in (False, True):
                cc = c[::-1] if rev else c
                for at_end in (True, False):
                    a = line[-1] if at_end else line[0]
                    b = cc[0] if at_end else cc[-1]
                    d = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
                    if best is None or d < best[0]: best = (d, i, cc, at_end)
        _, i, cc, at_end = best; segs.pop(i)
        line = line + cc if at_end else cc + line
    return LineString(line)
_RC = {}
def river(name, bb):
    k = (name, bb)
    if k not in _RC:
        B = box(*bb)
        segs = []
        for r in _G['rivers']:
            g = shape(r['g'])
            if r['n'] == name and B.intersects(g): segs += list(getattr(g, 'geoms', [g]))
        assert segs, name
        _RC[k] = _chain(segs)
    return _RC[k]
def rseg(name, bb, frm, to):
    """river coordinates from the point nearest frm to the point nearest to, both given (lat, lon)"""
    L = river(name, bb)
    a = L.project(Point(frm[1], frm[0])); b = L.project(Point(to[1], to[0]))
    return list(substring(L, a, b).coords)

# ---- shared lines -------------------------------------------------------------------------------------------------
MISS = ('Mississippi', (-96, 28, -88, 48))
MISSOURI = ('Missouri', (-113, 38, -90, 49))
REDS = ('Red', (-101.5, 30.5, -91, 35))
ARK = ('Arkansas', (-107, 33, -90, 40))
RIOG = ('Rio Grande', (-108, 25, -96, 38))
SABINE = ('Sabine', (-97, 29, -93, 34))
NUECES = ('Nueces', (-101, 27, -97, 31))
CANAD = ('Canadian', (-105, 34.5, -94.5, 37.5))
WASHITA = ('Washita', (-101, 33.5, -96, 36))
NFRED = ('North Fork Red', (-102, 34, -98.5, 36))
YELL = ('Yellowstone', (-111.5, 43.5, -103.5, 48.5))
CHEY = ('Cheyenne', (-105.5, 43, -100.5, 45))
BELLE = ('Belle Fourche', (-106, 43.5, -102, 45))
WHITE_SD = ('White', (-104, 42.5, -99, 44))
MOREAU = ('Moreau', (-103, 45, -100, 45.5))
CANNON = ('Cannonball', (-103.5, 46, -100.5, 46.7))
MILK = ('Milk', (-113.5, 47.9, -106, 49.3))
GILA = ('Gila', (-115, 32.4, -108, 33.7))

# The continental divide, north to south (lat, lon); approximate.
CDIV = P((61.5, -130), (57.5, -125.0), (55.5, -122.0), (54.0, -120.0), (52.5, -117.8), (51.5, -116.3), (50.5, -115.2),
         (49.0, -114.06), (48.57, -113.52), (48.0, -113.05), (47.35, -112.6), (46.75, -112.35), (46.3, -112.45),
         (45.95, -112.9), (45.9, -113.6), (45.69, -113.94), (45.3, -113.7), (44.97, -113.44), (44.6, -112.8),
         (44.55, -112.3), (44.6, -111.5), (44.45, -110.75), (44.2, -110.6), (43.75, -110.07), (43.25, -109.75),
         (42.75, -109.25), (42.36, -108.92), (42.0, -108.0), (41.6, -107.5), (41.0, -106.9), (40.6, -106.7),
         (40.38, -106.6), (40.0, -105.85), (39.8, -105.78), (39.5, -105.95), (39.36, -106.3), (39.0, -106.4),
         (38.5, -106.33), (38.17, -106.6), (37.85, -106.95), (37.48, -106.8), (37.2, -106.6), (37.0, -106.5),
         (36.5, -106.85), (36.0, -107.1), (35.3, -108.0), (34.5, -108.3), (33.5, -108.4), (32.5, -108.2), (31.33, -108.2),
         (28.0, -107.5), (22.0, -105.0))
EAST_OF_DIV = poly(CDIV, P((22.0, -70), (61.5, -70)))
WEST_OF_DIV = poly(CDIV, P((22.0, -130), (61.5, -130))).difference(EAST_OF_DIV)

# The Mississippi–Missouri drainage west of the Mississippi: the extent of French Louisiana. Its north side runs along the
# divide from Hudson Bay waters (the Red of the North, Souris and Saskatchewan), its south-west side along the divide from the
# Rio Grande and the Texas rivers, to the Sabine. Approximate.
LOU_N = P((47.24, -95.21), (46.5, -95.9), (45.75, -96.6), (46.3, -97.9), (47.2, -99.3), (47.8, -100.4), (47.75, -101.4),
          (48.2, -102.3), (48.8, -103.3), (49.2, -105.0), (49.5, -107.0), (49.65, -109.5), (49.6, -110.7), (49.4, -112.0),
          (49.0, -113.2), (48.57, -113.52))
LOU_SW = P((38.5, -106.33), (38.42, -106.08), (38.0, -105.6), (37.58, -105.48), (37.2, -105.2), (36.6, -105.3),
           (36.0, -105.4), (35.3, -104.3), (34.9, -103.6), (34.5, -103.0), (34.3, -102.0), (34.0, -101.3), (33.6, -100.2),
           (33.4, -99.5), (33.5, -98.5), (33.4, -97.5), (33.3, -96.5), (33.25, -95.5), (33.0, -94.8), (32.5, -94.4),
           (32.0, -94.05), (31.5, -93.5), (30.5, -93.7), (29.7, -93.85), (28.5, -93.6), (28.5, -89.2))
_i0 = CDIV.index((-113.52, 48.57)); _i1 = CDIV.index((-106.33, 38.5))
LOU = poly(rseg(*MISS, (28.95, -89.15), (47.24, -95.21)), LOU_N[1:], CDIV[_i0 + 1:_i1 + 1], LOU_SW[1:]).intersection(LAND)
# East of the Mississippi, south of the Lake Superior divide.
EMISS = poly(rseg(*MISS, (47.24, -95.21), (28.95, -89.15)), P((28.5, -80), (47.0, -80), (47.6, -89.0), (47.7, -92.0))).intersection(LAND)
# Hudson Bay drainage, to the continental divide.
HB_S = P((48.57, -113.52), *[(la, lo) for lo, la in LOU_N[::-1][1:]], (47.9, -92.0), (48.2, -90.8), (48.6, -89.6),
         (48.9, -88.0), (49.2, -85.0), (49.0, -80.0))
_j = CDIV.index((-114.06, 49.0))
HBC = poly(HB_S, P((61.5, -80), (61.5, -130)), CDIV[:_j + 1]).intersection(LAND)

# The Adams–Onís line (signed 1819, in force 22 Feb. 1821): the Sabine to 32°, north to the Red, up the Red to 100°W, north
# to the Arkansas, up the Arkansas to its source, north to 42°, west along 42° to the Pacific.
AO = (rseg(*SABINE, (29.7, -93.85), (32.0, -94.05)) + P((33.55, -94.04)) + rseg(*REDS, (33.55, -94.04), (34.56, -100.0))
      + P((37.75, -100.0)) + rseg(*ARK, (37.75, -100.0), (39.25, -106.3)) + P((42.0, -106.3), (42.0, -130.0)))
NE_OF_AO = poly(AO, P((61.5, -130), (61.5, -70), (22, -70), (22, -93.85)))
OREGON = WEST_OF_DIV.intersection(band(42, 49)).intersection(LAND)
US_MASK = US_ALL.union(box(-130, 24, -95.15, 49.0))          # the northern border: 49° west of the Lake of the Woods
TEXAS_CLAIM = poly(rseg(*RIOG, (25.95, -97.15), (37.83, -107.43)), P((42.0, -107.43), (42.0, -106.3)),
                   rseg(*ARK, (39.25, -106.3), (37.75, -100.0)), P((34.56, -100.0)),
                   rseg(*REDS, (34.56, -100.0), (33.55, -94.04)), P((32.0, -94.04)),
                   rseg(*SABINE, (32.0, -94.05), (29.7, -93.85)), P((25.95, -97.0))).intersection(LAND)
# The Gadsden Purchase (in force 30 June 1854): south of the Gila and of the 1848 line along New Mexico's southern boundary.
GADSDEN = poly(P((32.5, -106.6), (32.5, -108.2), (32.95, -108.2)), rseg(*GILA, (32.95, -108.3), (32.72, -114.6)),
               P((32.49, -114.81), (31.33, -111.07), (31.33, -108.21), (31.78, -108.21), (31.78, -106.53))).intersection(LAND)
US_1854 = US_ALL.intersection(EXT)
MX_1854 = MX_ALL.intersection(EXT)

# The country west of the Mississippi and north of Missouri, east of the Missouri and White Earth rivers (Michigan 1834,
# Wisconsin 1836, Iowa 1838 and Minnesota 1849 territories).
EOM_N = poly(rseg(*MISS, (47.24, -95.21), (40.39, -91.42)), P((40.6, -91.73), (40.58, -95.77)),
             rseg(*MISSOURI, (40.58, -95.77), (48.05, -102.75)), P((49.0, -102.75), (49.0, -95.21))).intersection(LAND)
MN_E = US('Minnesota').difference(EOM_N)
NUECES_STRIP = poly(rseg(*RIOG, (25.95, -97.15), (29.8, -101.4)), P((30.0, -100.17)),
                    rseg(*NUECES, (30.0, -100.17), (27.85, -97.5)), P((26.0, -97.0))).intersection(LAND)
TEJAS = poly(rseg(*SABINE, (29.7, -93.85), (32.0, -94.05)), P((33.55, -94.04)),
             rseg(*REDS, (33.55, -94.04), (34.56, -100.0)), P((30.0, -100.17)),
             rseg(*NUECES, (30.0, -100.17), (27.85, -97.5)), P((28.0, -96.0))).intersection(LAND)
NM_PROV = box(-109.5, 31.9, -103.0, 38.0).intersection(LAND)

# ---- the features ---------------------------------------------------------------------------------------------------
F = []
def add(fid, name, level, owner, y0, y1, geom, src, **o):
    F.append(dict(id=fid, name=name, level=level, owner=owner, y0=y0, y1=y1, geom=geom, src=src, **o))

VZ = 'Van Zandt, Boundaries of the United States and the Several States (1966), recalled'
NB = 'Atlas of Historical County Boundaries (Newberry Library), recalled'
AC = 'Atlas of Canada, Territorial Evolution, recalled'
GE = 'Gerhard, The North Frontier of New Spain (1982), recalled'

# Claims
add('fr_lou', 'New France (Louisiana)', 'claim', 'fr', 1700, 1762.84, LOU.union(EMISS), 'French claim to the Mississippi drainage; ceded west of the river to Spain at Fontainebleau, 3 Nov. 1762')
add('fr_east', 'New France (Illinois country)', 'claim', 'fr', 1762.84, 1763.11, EMISS, 'East of the Mississippi to Britain, Treaty of Paris, 10 Feb. 1763')
add('gb_east', 'British America', 'claim', 'gb', 1763.11, 1783.67, EMISS, 'Treaty of Paris 1763; to the United States, Treaty of Paris, 3 Sept. 1783')
add('gb_hbc', 'Rupert’s Land (Hudson’s Bay Company)', 'claim', 'gb', 1700, 1870.54, HBC, 'Charter of 1670; the Hudson Bay drainage; transferred to Canada 15 July 1870', note='South of 49° the Hudson Bay drainage passed to the United States in 1818.')
add('es_lou', 'Spanish Louisiana', 'claim', 'es', 1762.84, 1803.97, LOU, 'Treaty of Fontainebleau 1762; retroceded to France by the secret Treaty of San Ildefonso (1 Oct. 1800) but held by Spain until 1803; transferred to the United States 20 Dec. 1803 (upper Louisiana 10 Mar. 1804)')
_es = LAND.difference(LOU).difference(EMISS).difference(HBC)
_es = _es.difference(box(-130, 42, -70, 62)).difference(east(-89.0))
add('es_ns', 'New Spain', 'claim', 'es', 1700, 1821.15, _es, 'Spanish claim; its line with Louisiana was disputed until the Adams–Onís Treaty (in force 22 Feb. 1821)')
add('es_ao', 'New Spain', 'claim', 'es', 1821.15, 1821.74, LAND.difference(NE_OF_AO).intersection(south(42)), 'Adams–Onís line; Mexican independence 27 Sept. 1821')
add('us_east', 'United States', 'claim', 'us', 1783.67, 1803.97, EMISS.intersection(north(31.0)), 'Treaty of Paris 1783; the 31st parallel with Spain by Pinckney’s Treaty (1795)')
_us1803 = EMISS.intersection(north(31.0)).union(LOU)
add('us_1803', 'United States', 'claim', 'us', 1803.97, 1818.8, _us1803, 'The Louisiana Purchase, transferred 20 Dec. 1803; its western line disputed with Spain')
_us1818 = _us1803.intersection(south(49.0)).union(HBC.intersection(south(49.0)).intersection(EAST_OF_DIV)).intersection(US_MASK)
add('us_1818', 'United States', 'claim', 'us', 1818.8, 1821.15, _us1818, 'Convention of 1818: the 49th parallel from the Lake of the Woods to the Rockies')
_us1821 = NE_OF_AO.intersection(LAND).intersection(US_MASK).difference(OREGON).intersection(east(-125))
add('us_1821', 'United States', 'claim', 'us', 1821.15, 1845.99, _us1821, 'The Adams–Onís line, in force 22 Feb. 1821')
add('us_1845', 'United States', 'claim', 'us', 1845.99, 1846.46, _us1821.union(TEXAS_CLAIM), 'Annexation of Texas, 29 Dec. 1845')
add('us_1846', 'United States', 'claim', 'us', 1846.46, 1848.41, _us1821.union(TEXAS_CLAIM).union(OREGON), 'Oregon Treaty, 15 June 1846')
add('us_1848', 'United States', 'claim', 'us', 1848.41, 1854.5, US_1854.difference(GADSDEN), 'Treaty of Guadalupe Hidalgo, ratified 30 May 1848')
add('us_1854', 'United States', 'claim', 'us', 1854.5, 1906, US_1854, 'Gadsden Purchase, in force 30 June 1854')
add('or_joint', 'Oregon Country (joint British–American occupation)', 'claim', 'gb', 1818.8, 1846.46, OREGON, 'Convention of 1818; divided at 49° by the Oregon Treaty, 1846')
_mx = LAND.difference(NE_OF_AO).intersection(south(42))
add('mx_1821', 'Mexico', 'claim', 'mx', 1821.74, 1836.17, _mx, 'Independence, 27 Sept. 1821')
add('mx_1836', 'Mexico', 'claim', 'mx', 1836.17, 1848.41, _mx.difference(TEXAS_CLAIM), 'Mexico did not recognize Texan independence; the line drawn is the Texan claim', note='Mexico claimed Texas to the Nueces, and all of it, until 1848.')
add('mx_1848', 'Mexico', 'claim', 'mx', 1848.41, 1854.5, MX_1854.union(GADSDEN), 'Treaty of Guadalupe Hidalgo')
add('mx_1854', 'Mexico', 'claim', 'mx', 1854.5, 1906, MX_1854, 'Gadsden Purchase')
add('ca', 'Canada', 'claim', 'ca', 1870.54, 1906, CA_ALL.intersection(EXT), 'Rupert’s Land and the North-Western Territory transferred to Canada, 15 July 1870')

# Spanish provinces and Mexican states
def prov(fid, name, y0, y1, g, src, owner='es', level='terr', **o): add(fid, name, level, owner, y0, y1, g, src, **o)
prov('es_nm', 'Santa Fe de Nuevo México', 1700, 1821.74, NM_PROV, GE + '; bounds approximate')
prov('mx_nm', 'Nuevo México (territory)', 1821.74, 1848.41, NM_PROV, 'Mexican province, a federal territory from 1824; bounds approximate', owner='mx')
prov('es_tx', 'Texas (province)', 1716.5, 1821.74, TEJAS, GE + '; the Nueces and Medina lines with Nuevo Santander and Coahuila, the Sabine and Red with Louisiana; approximate')
prov('mx_tx', 'Texas (province)', 1821.74, 1824.75, TEJAS, 'Mexican province until the constitution of 4 Oct. 1824', owner='mx')
_coah = MX('Coahuila').union(NUECES_STRIP.intersection(west(-99.3)))
_tams = MX('Tamaulipas').union(NUECES_STRIP.intersection(east(-99.3)))
prov('es_coah', 'Coahuila', 1700, 1821.74, _coah, GE + '; approximate')
prov('es_ns_', 'Nuevo Santander', 1748.5, 1821.74, _tams, GE + '; founded 1748; approximate')
prov('es_nl', 'Nuevo León', 1700, 1821.74, MX('Nuevo León'), GE)
prov('es_nv', 'Nueva Vizcaya', 1700, 1821.74, MX('Chihuahua').union(MX('Durango')), GE)
prov('es_son', 'Sonora y Sinaloa', 1700, 1821.74, MX('Sonora').union(MX('Sinaloa')), GE)
prov('mx_coah_p', 'Coahuila', 1821.74, 1824.75, _coah, 'Mexican province', owner='mx')
prov('mx_tams_p', 'Nuevo Santander', 1821.74, 1824.75, _tams, 'Mexican province', owner='mx')
prov('mx_nv_p', 'Nueva Vizcaya', 1821.74, 1824.75, MX('Chihuahua').union(MX('Durango')), 'Mexican province', owner='mx')
prov('mx_son_p', 'Sonora y Sinaloa', 1821.74, 1824.75, MX('Sonora').union(MX('Sinaloa')), 'Mexican province', owner='mx')
def mxs(fid, name, y0, y1, g, src='Mexican state under the constitution of 1824'): add(fid, name, 'state', 'mx', y0, y1, g, src)
mxs('mx_cyt', 'Coahuila y Tejas', 1824.75, 1836.17, _coah.union(TEJAS))
mxs('mx_coah', 'Coahuila', 1836.17, 1848.41, _coah, 'Coahuila after Texan independence; the Nueces strip claimed by Texas')
mxs('mx_coah2', 'Coahuila', 1848.41, 1906, MX('Coahuila'))
mxs('mx_tams', 'Tamaulipas', 1824.75, 1848.41, _tams)
mxs('mx_tams2', 'Tamaulipas', 1848.41, 1906, MX('Tamaulipas'))
mxs('mx_nl', 'Nuevo León', 1824.75, 1906, MX('Nuevo León'))
mxs('mx_chih', 'Chihuahua', 1824.75, 1848.41, MX('Chihuahua'))
mxs('mx_chih2', 'Chihuahua', 1848.41, 1854.5, MX('Chihuahua').union(GADSDEN.intersection(east(-109.05))), 'Chihuahua with the Mesilla strip, sold to the United States in 1854')
mxs('mx_chih3', 'Chihuahua', 1854.5, 1906, MX('Chihuahua'))
mxs('mx_dur', 'Durango', 1824.75, 1906, MX('Durango'))
mxs('mx_sys', 'Estado de Occidente (Sonora y Sinaloa)', 1824.75, 1830.3, MX('Sonora').union(MX('Sinaloa')))
mxs('mx_son', 'Sonora', 1830.3, 1848.41, MX('Sonora'), 'Separated from Sinaloa, 1830')
mxs('mx_son2', 'Sonora', 1848.41, 1854.5, MX('Sonora').union(GADSDEN.intersection(west(-109.05))), 'Sonora with the Gadsden strip, sold to the United States in 1854')
mxs('mx_son3', 'Sonora', 1854.5, 1906, MX('Sonora'))

# The Republic and State of Texas
add('tx_rep', 'Republic of Texas', 'state', 'tx', 1836.17, 1845.99, TEXAS_CLAIM, 'Declaration of independence, 2 Mar. 1836; the boundary act of 19 Dec. 1836: the Rio Grande to its source, north to 42°, and the Adams–Onís line', note='The claim, not the country Texas held: west of the Nueces and north of the Red the Comanche and others held it.')
add('tx_st', 'Texas', 'state', 'us', 1845.99, 1850.9, TEXAS_CLAIM, 'Admitted 29 Dec. 1845 with the Republic’s claim', csa=None)
add('tx_st2', 'Texas', 'state', 'us', 1850.9, 1906, US('Texas'), 'Compromise of 1850, accepted by Texas 25 Nov. 1850', csa=(1861.09, 1865.45))

# United States: territories and states
def ter(fid, name, y0, y1, g, src, **o): add(fid, name, 'terr', 'us', y0, y1, g, src, **o)
def sta(fid, name, y0, g, src, csa=None, y1=1906): add(fid, name, 'state', 'us', y0, y1, g, src, csa=csa)
_nw = unary_union([US('Ohio'), US('Indiana'), US('Illinois'), US('Michigan'), US('Wisconsin'), MN_E])
add('gb_quebec', 'Province of Quebec', 'terr', 'gb', 1775.33, 1783.67, _nw, 'Quebec Act 1774, in force 1 May 1775: the country north of the Ohio to the Mississippi')
ter('nwt', 'Northwest Territory', 1787.55, 1800.5, _nw, 'Northwest Ordinance, 13 July 1787')
ter('ind_t', 'Indiana Territory', 1800.5, 1809.17, unary_union([US('Indiana'), US('Illinois'), US('Wisconsin'), MN_E]), 'Act of 7 May 1800, in force 4 July')
ter('ind_t2', 'Indiana Territory', 1809.17, 1816.92, US('Indiana'), 'Illinois Territory set off, 1809')
sta('in', 'Indiana', 1816.92, US('Indiana'), 'Admitted 11 Dec. 1816')
ter('ill_t', 'Illinois Territory', 1809.17, 1818.92, unary_union([US('Illinois'), US('Wisconsin'), MN_E]), 'Act of 3 Feb. 1809, in force 1 Mar.')
ter('mich_t', 'Michigan Territory', 1805.5, 1818.92, US('Michigan'), 'Act of 11 Jan. 1805, in force 30 June')
ter('mich_t2', 'Michigan Territory', 1818.92, 1834.5, unary_union([US('Michigan'), US('Wisconsin'), MN_E]), 'The country north of Illinois attached, 1818')
ter('mich_t3', 'Michigan Territory', 1834.5, 1836.5, unary_union([US('Michigan'), US('Wisconsin'), MN_E, EOM_N]), 'Act of 28 June 1834: the country west of the Mississippi to the Missouri and White Earth rivers attached')
ter('wis_t', 'Wisconsin Territory', 1836.5, 1838.5, unary_union([US('Wisconsin'), MN_E, EOM_N]), 'Act of 20 Apr. 1836, in force 4 July')
ter('wis_t2', 'Wisconsin Territory', 1838.5, 1848.41, US('Wisconsin').union(MN_E), 'Iowa Territory set off, 1838')
ter('iowa_t', 'Iowa Territory', 1838.5, 1846.99, EOM_N, 'Act of 12 June 1838, in force 4 July: to the Missouri and White Earth rivers')
ter('minn_t', 'Minnesota Territory', 1849.17, 1858.36, EOM_N.union(MN_E).difference(US('Iowa')), 'Act of 3 Mar. 1849')
ter('sw_t', 'Territory South of the River Ohio', 1790.4, 1796.42, US('Tennessee'), 'Act of 26 May 1790')
ter('miss_t', 'Mississippi Territory', 1798.27, 1817.95, US('Mississippi').union(US('Alabama')), 'Act of 7 Apr. 1798; enlarged to Tennessee 1804')
ter('orl_t', 'Territory of Orleans', 1804.75, 1812.33, US('Louisiana').intersection(poly(rseg(*MISS, (28.95, -89.15), (35.0, -90.1)), P((35, -100), (28, -100)))), 'Act of 26 Mar. 1804, in force 1 Oct.')
_purch = lambda: LOU.difference(US('Louisiana'))
ter('lou_d', 'District of Louisiana', 1804.75, 1805.5, _purch(), 'Act of 26 Mar. 1804: governed from Indiana Territory', note='Its western line with New Spain was disputed until 1821.')
ter('lou_t', 'Louisiana Territory', 1805.5, 1812.43, _purch(), 'Act of 3 Mar. 1805, in force 4 July', note='Its western line with New Spain was disputed until 1821.')
_ark1819 = US('Arkansas').union(US('Oklahoma').intersection(south(36.5)).intersection(east(-100.0)))
ter('mo_t', 'Missouri Territory', 1812.43, 1819.5, _purch().intersection(US_MASK), 'Act of 4 June 1812')
ter('mo_t2', 'Missouri Territory', 1819.5, 1821.61, _us1818.intersection(_purch().union(HBC.intersection(south(49)))).difference(_ark1819).difference(US('Louisiana')), 'Arkansas Territory set off, 1819')
ter('ark_t', 'Arkansas Territory', 1819.5, 1828.4, _ark1819, 'Act of 2 Mar. 1819, in force 4 July; the western line moved east in 1824 and 1828 (approximate)')
ter('ark_t2', 'Arkansas Territory', 1828.4, 1836.45, US('Arkansas'), 'Western boundary of the Cherokee treaty of 6 May 1828')
ter('ks_t', 'Kansas Territory', 1854.41, 1861.08, band(37, 40).intersection(EAST_OF_DIV).intersection(west(-94.6)).intersection(US_1854), 'Kansas–Nebraska Act, 30 May 1854: 37° to 40°, to the summit of the Rockies')
_ne1854 = band(40, 49).intersection(EAST_OF_DIV).intersection(US_1854).difference(EOM_N).difference(US('Iowa')).difference(US('Missouri')).difference(US('Minnesota'))
ter('ne_t', 'Nebraska Territory', 1854.41, 1861.17, _ne1854, 'Kansas–Nebraska Act: 40° to 49°, from the Missouri and White Earth rivers to the summit of the Rockies')
_wy = US('Wyoming'); _wy_w = _wy.intersection(west(-110.05)); _wy_sw = _wy_w.intersection(south(42.0)); _wy_nw = _wy_w.difference(_wy_sw)
ter('ne_t2', 'Nebraska Territory', 1861.17, 1863.17, US('Nebraska').union(_wy.intersection(band(41, 43)).difference(_wy_w)), 'Dakota and Colorado set off, 1861')
ter('dak_t', 'Dakota Territory', 1861.17, 1863.17, unary_union([US('North Dakota'), US('South Dakota'), band(43, 49).intersection(EAST_OF_DIV).intersection(west(-104.05)).intersection(US_1854)]), 'Act of 2 Mar. 1861: north of 43°, to the summit of the Rockies')
ter('dak_t2', 'Dakota Territory', 1863.17, 1864.4, US('North Dakota').union(US('South Dakota')), 'Idaho Territory set off, 1863')
ter('dak_t3', 'Dakota Territory', 1864.4, 1868.56, unary_union([US('North Dakota'), US('South Dakota'), _wy.difference(_wy_w)]), 'Wyoming east of 110°W returned to Dakota with the Montana act, 1864')
ter('dak_t4', 'Dakota Territory', 1868.56, 1889.84, US('North Dakota').union(US('South Dakota')), 'Wyoming Territory set off, 1868; statehood 2 Nov. 1889')
ter('ne_t3', 'Nebraska Territory', 1863.17, 1867.16, US('Nebraska'), 'Idaho Territory took the land west of 104°W, 1863')
ter('co_t', 'Colorado Territory', 1861.16, 1876.59, US('Colorado'), 'Act of 28 Feb. 1861')
_ut1850 = band(37, 42).intersection(WEST_OF_DIV).intersection(east(-120)).intersection(US_1854)
ter('ut_t', 'Utah Territory', 1850.7, 1861.16, _ut1850, 'Act of 9 Sept. 1850: 37° to 42°, from California to the summit of the Rockies')
ter('ut_t2', 'Utah Territory', 1861.16, 1868.56, US('Utah').union(_wy_sw), 'Colorado and Nevada set off, 1861')
ter('ut_t3', 'Utah Territory', 1868.56, 1896.01, US('Utah'), 'Wyoming Territory set off, 1868; statehood 4 Jan. 1896')
_nm1850 = (lon(-103.05, -100).intersection(south(38)).union(box(-130, 15, -103.04, 38).intersection(EAST_OF_DIV)).union(WEST_OF_DIV.intersection(south(37)).intersection(east(-114.6)))
           ).intersection(US_1854).difference(GADSDEN).difference(US('Texas')).intersection(west(-103.04))
ter('nm_t', 'New Mexico Territory', 1850.9, 1854.5, _nm1850, 'Act of 9 Sept. 1850 (Compromise of 1850): north to 38° east of the Rockies and 37° west of them')
ter('nm_t2', 'New Mexico Territory', 1854.5, 1861.16, _nm1850.union(GADSDEN), 'With the Gadsden Purchase, 1854')
ter('nm_t3', 'New Mexico Territory', 1861.16, 1863.15, US('New Mexico').union(US('Arizona')), 'Colorado Territory set off, 1861')
ter('nm_t4', 'New Mexico Territory', 1863.15, 1906, US('New Mexico'), 'Arizona Territory set off, 24 Feb. 1863')
ter('az_t', 'Arizona Territory', 1863.15, 1906, US('Arizona'), 'Act of 24 Feb. 1863')
ter('csa_az', 'Confederate Territory of Arizona', 1862.05, 1865.45, US('New Mexico').union(US('Arizona')).intersection(south(34.0)), 'Proclaimed 1 Aug. 1861; organized by the Confederate Congress, 18 Jan. 1862; Union troops held it from mid-1862', csa=(1862.05, 1865.45))
ter('nv_t', 'Nevada Territory', 1861.16, 1864.83, US('Nevada'), 'Act of 2 Mar. 1861')
ter('or_t', 'Oregon Territory', 1848.62, 1853.17, OREGON, 'Act of 14 Aug. 1848')
ter('wa_t', 'Washington Territory', 1853.17, 1859.12, OREGON.intersection(north(46)), 'Act of 2 Mar. 1853')
ter('or_t2', 'Oregon Territory', 1853.17, 1859.12, OREGON.difference(north(46)), 'Washington Territory set off, 1853')
ter('wa_t2', 'Washington Territory', 1859.12, 1863.17, OREGON.difference(US('Oregon')), 'Oregon’s statehood, 14 Feb. 1859, left the rest of its territory to Washington')
ter('wa_t3', 'Washington Territory', 1863.17, 1889.87, US('Washington'), 'Idaho Territory set off, 1863')
ter('id_t', 'Idaho Territory', 1863.17, 1864.4, unary_union([US('Idaho'), US('Montana'), _wy.difference(_wy_sw)]), 'Act of 3 Mar. 1863')
ter('id_t2', 'Idaho Territory', 1864.4, 1868.56, US('Idaho').union(_wy_nw), 'Montana set off, 1864; Idaho kept Wyoming west of 110°W and north of 42°')
ter('id_t3', 'Idaho Territory', 1868.56, 1890.5, US('Idaho'), 'Wyoming set off, 1868; statehood 3 July 1890')
ter('mt_t', 'Montana Territory', 1864.4, 1889.86, US('Montana'), 'Act of 26 May 1864; statehood 8 Nov. 1889')
ter('wy_t', 'Wyoming Territory', 1868.56, 1890.52, _wy, 'Act of 25 July 1868; statehood 10 July 1890')
# Indian Territory and Oklahoma
_ok = US('Oklahoma'); _pan = _ok.intersection(west(-100.0)); _okm = _ok.difference(_pan)
_canad_s = poly(rseg(*CANAD, (35.45, -94.6), (35.6, -100.0)), P((33, -100.0), (33, -94.4)))
_it1890 = _okm.intersection(east(-96.5).difference(_canad_s).union(_canad_s.intersection(east(-98.0)))).union(_okm.intersection(band(36.5, 37.1)).intersection(lon(-100, -96.5)))
_outlet = _okm.intersection(band(36.5, 37.1)).intersection(lon(-100, -96.5))
add('ind_t', 'Indian Territory', 'unorg', 'us', 1834.5, 1890.34, _okm, 'Indian Intercourse Act, 30 June 1834, and the removal treaties; the country of the Five Tribes and others', note='Not an organized territory; the nations governed themselves under their treaties. Most allied with the Confederacy in 1861.')
add('ind_t2', 'Indian Territory', 'unorg', 'us', 1890.34, 1893.71, _it1890, 'Oklahoma Organic Act, 2 May 1890: the Five Tribes and the Cherokee Outlet (approximate)')
add('ind_t3', 'Indian Territory', 'unorg', 'us', 1893.71, 1906, _it1890.difference(_outlet), 'The Cherokee Outlet opened, 16 Sept. 1893 (approximate)')
ter('ok_t', 'Oklahoma Territory', 1890.34, 1893.71, _ok.difference(_it1890), 'Oklahoma Organic Act, 2 May 1890 (approximate)')
ter('ok_t2', 'Oklahoma Territory', 1893.71, 1906, _ok.difference(_it1890.difference(_outlet)), 'With the Cherokee Outlet, 1893 (approximate)')
add('pls', 'Public Land Strip (No Man’s Land)', 'unorg', 'us', 1850.9, 1890.34, _pan, 'Left outside every state and territory by the Compromise of 1850; joined to Oklahoma Territory, 1890')
# States, with their dates of admission; the Confederate states are marked from secession to the surrender in the West.
sta('ky', 'Kentucky', 1792.42, US('Kentucky'), 'Admitted 1 June 1792')
sta('tn', 'Tennessee', 1796.42, US('Tennessee'), 'Admitted 1 June 1796', csa=(1861.44, 1865.45))
sta('la', 'Louisiana', 1812.33, US('Louisiana'), 'Admitted 30 Apr. 1812', csa=(1861.07, 1865.45))
sta('ms', 'Mississippi', 1817.95, US('Mississippi'), 'Admitted 10 Dec. 1817', csa=(1861.03, 1865.45))
sta('il', 'Illinois', 1818.92, US('Illinois'), 'Admitted 3 Dec. 1818')
sta('al', 'Alabama', 1819.95, US('Alabama'), 'Admitted 14 Dec. 1819', csa=(1861.03, 1865.45))
add('mo', 'Missouri', 'state', 'us', 1821.61, 1837.24, US('Missouri').intersection(east(-94.62)), 'Admitted 10 Aug. 1821; the Platte Purchase added 1837')
sta('mo2', 'Missouri', 1837.24, US('Missouri'), 'With the Platte Purchase, 1837', csa=None)
sta('ar', 'Arkansas', 1836.45, US('Arkansas'), 'Admitted 15 June 1836', csa=(1861.35, 1865.45))
sta('mi', 'Michigan', 1837.07, US('Michigan'), 'Admitted 26 Jan. 1837')
sta('ia', 'Iowa', 1846.99, US('Iowa'), 'Admitted 28 Dec. 1846')
sta('wi', 'Wisconsin', 1848.41, US('Wisconsin'), 'Admitted 29 May 1848')
sta('mn', 'Minnesota', 1858.36, US('Minnesota'), 'Admitted 11 May 1858')
sta('ks', 'Kansas', 1861.08, US('Kansas'), 'Admitted 29 Jan. 1861')
sta('nv', 'Nevada', 1864.83, US('Nevada'), 'Admitted 31 Oct. 1864')
sta('ne', 'Nebraska', 1867.16, US('Nebraska'), 'Admitted 1 Mar. 1867')
sta('co', 'Colorado', 1876.59, US('Colorado'), 'Admitted 1 Aug. 1876')
sta('nd', 'North Dakota', 1889.84, US('North Dakota'), 'Admitted 2 Nov. 1889')
sta('sd', 'South Dakota', 1889.84, US('South Dakota'), 'Admitted 2 Nov. 1889')
sta('mt', 'Montana', 1889.86, US('Montana'), 'Admitted 8 Nov. 1889')
sta('wa', 'Washington', 1889.87, US('Washington'), 'Admitted 11 Nov. 1889')
sta('id', 'Idaho', 1890.5, US('Idaho'), 'Admitted 3 July 1890')
sta('wy', 'Wyoming', 1890.52, US('Wyoming'), 'Admitted 10 July 1890')
sta('ut', 'Utah', 1896.01, US('Utah'), 'Admitted 4 Jan. 1896')
sta('or', 'Oregon', 1859.12, US('Oregon'), 'Admitted 14 Feb. 1859')
sta('ca_st', 'California', 1850.69, US('California'), 'Admitted 9 Sept. 1850')

# Canada
_on_w = CA('Ontario')
add('uc', 'Upper Canada', 'terr', 'gb', 1791.9, 1841.11, _on_w.intersection(east(-89.15)).intersection(south(49.5)), 'Constitutional Act 1791 (in force 26 Dec. 1791); its north-west limit undefined (approximate)')
add('cw', 'Canada West (Province of Canada)', 'terr', 'gb', 1841.11, 1867.5, _on_w.intersection(east(-89.15)).intersection(south(49.5)), 'Act of Union, in force 10 Feb. 1841 (approximate)')
add('on', 'Ontario', 'state', 'ca', 1867.5, 1889.6, _on_w.intersection(east(-89.15)).intersection(south(49.5)), 'Confederation, 1 July 1867; the western boundary in dispute with Canada and Manitoba (approximate)')
add('on2', 'Ontario', 'state', 'ca', 1889.6, 1906, _on_w.intersection(south(51.6)), 'Privy Council award 1884; Canada (Ontario Boundary) Act 1889: west to the Lake of the Woods, north to the Albany River')
add('mb', 'Manitoba', 'state', 'ca', 1870.54, 1881.25, box(-99.0, 49.0, -96.0, 50.5).intersection(LAND), 'Manitoba Act, in force 15 July 1870: the “postage stamp” province')
add('mb2', 'Manitoba', 'state', 'ca', 1881.25, 1906, box(-101.5, 49.0, -95.15, 52.83).intersection(LAND), 'Extended west and north, 1881 (approximate)')
_bc = CA('British Columbia')
add('bc_c', 'British Columbia (colony)', 'terr', 'gb', 1858.59, 1871.55, _bc, 'Colony from 2 Aug. 1858')
add('bc', 'British Columbia', 'state', 'ca', 1871.55, 1906, _bc, 'Joined Canada, 20 July 1871')
_nwt = CA_ALL.intersection(EXT).difference(_on_w).difference(_bc).difference(CA('Québec'))
add('nwt_c', 'North-West Territories', 'terr', 'ca', 1870.54, 1881.25, _nwt.difference(box(-99.0, 49.0, -96.0, 50.5)), 'Rupert’s Land Act; Temporary Government Act, 1869–70')
add('nwt_c2', 'North-West Territories', 'terr', 'ca', 1881.25, 1905.67, _nwt.difference(box(-101.5, 49.0, -95.15, 52.83)), 'After the enlargement of Manitoba, 1881')
add('d_assa', 'District of Assiniboia', 'terr', 'ca', 1882.35, 1905.67, box(-111.35, 49.0, -101.5, 52.0).intersection(LAND), 'Order in council, 8 May 1882 (approximate)', sub=True)
add('d_sask', 'District of Saskatchewan', 'terr', 'ca', 1882.35, 1905.67, box(-111.35, 52.0, -100.5, 55.0).intersection(LAND).difference(box(-101.5, 49.0, -95.15, 52.83)), 'Order in council, 8 May 1882 (approximate)', sub=True)
add('d_alta', 'District of Alberta', 'terr', 'ca', 1882.35, 1905.67, box(-125, 49.0, -111.35, 55.0).intersection(CA_ALL).difference(_bc), 'Order in council, 8 May 1882 (approximate)', sub=True)
add('sk', 'Saskatchewan', 'state', 'ca', 1905.67, 1906, CA('Saskatchewan'), 'Saskatchewan Act, in force 1 Sept. 1905')
add('ab', 'Alberta', 'state', 'ca', 1905.67, 1906, CA('Alberta'), 'Alberta Act, in force 1 Sept. 1905')

# Unorganized American land: what the United States claimed and had not put in a state or territory.
WEST_MISS = poly(rseg(*MISS, (28.95, -89.15), (47.24, -95.21)), P((49.0, -95.21), (49.0, -126), (24, -126), (24, -89.15)))
def unorganized():
    ys = sorted({f['y0'] for f in F if f['owner'] == 'us'} | {f['y1'] for f in F if f['owner'] == 'us'} | {1906})
    us = [f for f in F if f['owner'] == 'us' and f['level'] == 'claim']
    held = [f for f in F if f['owner'] == 'us' and f['level'] in ('terr', 'state', 'unorg')]
    out = []
    for a, b in zip(ys, ys[1:]):
        m = (a + b) / 2
        if m < 1803.97: continue
        c = [f for f in us if f['y0'] <= m < f['y1']]
        if not c: continue
        rest = c[0]['geom'].intersection(WEST_MISS).difference(unary_union([f['geom'] for f in held if f['y0'] <= m < f['y1']] or [Polygon()]))
        rest = rest.buffer(-0.02).buffer(0.02)
        if rest.area < 0.5: continue
        if out and out[-1][3].equals(rest): out[-1][1] = b; continue
        out.append([a, b, 'Unorganized territory' + (' (Indian Country)' if a < 1854.41 else ''), rest])
    for i, (a, b, n, g) in enumerate(out):
        add(f'unorg{i}', n, 'unorg', 'us', a, b, g, 'Land the United States claimed outside any state or territory (residual of the features above)')
unorganized()

# ---- reservations and reserves ---------------------------------------------------------------------------------------
# Drawn from the treaty, statute and executive-order descriptions (recalled: Royce, Indian Land Cessions in the United
# States, BAE 18th Annual Report, 1899; Kappler, Indian Affairs: Laws and Treaties; for Canada, the Treaty 7 reserve surveys
# as summarized in Dempsey and Getty, Handbook 13). Small reservations are drawn as boxes on their location; the large ones
# from their river and meridian lines. All approximate. Coloured by the people the reservation was made for.
MARIAS = ('Marias', (-111.6, 47.8, -110.4, 48.5))
WMO = poly(rseg(*MISSOURI, (38.82, -90.12), (47.98, -104.05)), P((47.98, -116), (30, -116), (30, -90.12)))   # south/west of the Missouri
EMO = box(-116, 30, -85, 50).difference(WMO)
def res(fid, name, tribes, y0, y1, g, src, **o):
    add(fid, name, 'res', 'res', y0, y1, g.intersection(LAND), src, tribes=tribes, **o)
_gsr = poly(rseg(*MISSOURI, (43.0, -98.46), (46.0, -100.6)), P((46.0, -104.05), (43.0, -104.05)))
_bh = poly(rseg(*BELLE, (44.75, -103.0), (44.43, -102.2)), rseg(*CHEY, (44.43, -102.2), (43.95, -103.0))).union(west(-103.0))
res('gsr', 'Great Sioux Reservation', ['Lakota'], 1868.33, 1877.16, _gsr, 'Fort Laramie treaty, 29 Apr. 1868: South Dakota west of the Missouri to 46°N')
res('gsr2', 'Great Sioux Reservation', ['Lakota'], 1877.16, 1890.11, _gsr.difference(_bh), 'Act of 28 Feb. 1877: the Black Hills taken, west of 103°W and between the forks of the Cheyenne')
res('pr', 'Pine Ridge Reservation (Oglala)', ['Lakota'], 1890.11, 1906, box(-103.0, 43.0, -101.23, 43.75), 'Sioux Act, 2 Mar. 1889, in force 10 Feb. 1890')
res('rb', 'Rosebud Reservation (Brulé)', ['Lakota'], 1890.11, 1904.6, box(-101.23, 43.0, -98.5, 43.7).intersection(WMO), 'Sioux Act, 1889')
res('rb2', 'Rosebud Reservation (Brulé)', ['Lakota'], 1904.6, 1906, box(-101.23, 43.0, -99.53, 43.7), 'Gregory County opened, 1904')
res('lb', 'Lower Brulé Reservation', ['Lakota'], 1890.11, 1906, box(-100.4, 43.8, -99.3, 44.2).intersection(WMO), 'Sioux Act, 1889')
res('cr', 'Cheyenne River Reservation (Miniconjou, Sans Arc, Two Kettle, Sihasapa)', ['Lakota'], 1890.11, 1906, box(-102.05, 44.5, -100.3, 45.45).intersection(WMO), 'Sioux Act, 1889')
res('sr', 'Standing Rock Reservation (Hunkpapa, Sihasapa, Yanktonai)', ['Lakota', 'Yanktonai'], 1890.11, 1906, box(-102.05, 45.45, -100.4, 46.4).intersection(WMO), 'Sioux Act, 1889; the agency at Fort Yates from 1873')
res('cc', 'Crow Creek Reservation', ['Yanktonai'], 1866.5, 1906, box(-99.65, 43.9, -99.0, 44.3).intersection(EMO), 'Lower Yanktonai settled there from 1866; reservation confirmed 1889')
res('ynk', 'Yankton Reservation', ['Yankton'], 1859.15, 1906, box(-98.95, 42.95, -98.3, 43.3).intersection(EMO), 'Treaty of 19 Apr. 1858, ratified 1859')
res('pon1', 'Ponca Reservation', ['Ponca'], 1859.2, 1877.4, box(-98.4, 42.75, -97.95, 42.95), 'Treaty of 12 Mar. 1858; the Ponca removed to the Indian Territory, 1877')
res('pon2', 'Ponca Reservation', ['Ponca'], 1878.5, 1906, box(-97.15, 36.6, -96.8, 36.9), 'In the Indian Territory from 1878')
res('santee', 'Santee Reservation', ['Dakota'], 1866.5, 1906, box(-98.05, 42.6, -97.65, 42.85), 'Executive orders of 1866 and 1869')
_mnr = LineString(P((45.32, -96.55), (45.0, -96.0), (44.75, -95.6), (44.55, -95.1), (44.4, -94.65))).buffer(0.15)
res('mnr', 'Upper and Lower Sioux reservations (Minnesota River)', ['Dakota'], 1852.5, 1863.2, _mnr, 'Treaties of Traverse des Sioux and Mendota, 1851 (ratified 1852); halved 1858; forfeited after the war of 1862')
res('lt', 'Lake Traverse Reservation (Sisseton–Wahpeton)', ['Dakota'], 1867.13, 1892.3, Polygon(P((46.0, -96.58), (46.0, -97.9), (45.27, -97.02), (45.3, -96.46))), 'Treaty of 19 Feb. 1867; opened 1892')
res('dl', 'Devil’s Lake Reservation', ['Dakota', 'Yanktonai'], 1867.13, 1906, box(-99.2, 47.75, -98.6, 48.05), 'Treaty of 19 Feb. 1867')
res('fb', 'Fort Berthold Reservation', ['Hidatsa', 'Mandan', 'Arikara'], 1870.28, 1880.53, box(-104.0, 46.9, -101.3, 48.3), 'Executive order of 12 Apr. 1870 (bounds approximate)')
res('fb2', 'Fort Berthold Reservation', ['Hidatsa', 'Mandan', 'Arikara'], 1880.53, 1906, box(-103.2, 47.4, -101.4, 48.2), 'Executive order of 13 July 1880 (bounds approximate)')
_nmt = poly(rseg(*MISSOURI, (47.98, -104.05), (47.9, -110.5)), rseg(*MARIAS, (47.9, -110.6), (48.4, -111.4)),
            P((48.3, -112.5), (48.3, -113.3), (49.0, -114.0), (49.0, -104.05))).intersection(EAST_OF_DIV)
res('blk', 'Blackfeet, Gros Ventre and Assiniboine reservation', ['Blackfoot', 'Gros Ventre', 'Assiniboine'], 1874.29, 1888.37, _nmt, 'Act of 15 Apr. 1874: Montana north of the Missouri and Marias (bounds approximate)')
res('blk2', 'Blackfeet Reservation', ['Blackfoot'], 1888.37, 1906, box(-113.6, 48.3, -111.9, 49.0).intersection(EAST_OF_DIV), 'Act of 1 May 1888')
res('fbk', 'Fort Belknap Reservation', ['Gros Ventre', 'Assiniboine'], 1888.37, 1906, box(-109.0, 47.95, -108.25, 48.55), 'Act of 1 May 1888')
res('fp', 'Fort Peck Reservation', ['Assiniboine', 'Yanktonai'], 1888.37, 1906, box(-106.55, 47.95, -104.05, 48.9).difference(WMO), 'Act of 1 May 1888')
_crow = poly(rseg(*YELL, (46.15, -107.95), (45.03, -110.7)), P((45.0, -110.7), (45.0, -107.95)))
res('crow', 'Crow Reservation', ['Crow'], 1868.35, 1882.27, _crow, 'Fort Laramie treaty, 7 May 1868: south of the Yellowstone, east of 107°57′ to the boundary at 45°N')
res('crow2', 'Crow Reservation', ['Crow'], 1882.27, 1891.9, _crow.intersection(east(-110.1)), 'Act of 11 Apr. 1882: the western end ceded')
res('crow3', 'Crow Reservation', ['Crow'], 1891.9, 1906, _crow.intersection(east(-108.8)), 'Agreement of 1890, ratified 1891: the western part ceded (approximate)')
res('nch', 'Northern Cheyenne (Tongue River) Reservation', ['Cheyenne'], 1884.9, 1900.2, box(-106.95, 45.25, -106.35, 45.62), 'Executive order of 26 Nov. 1884')
res('nch2', 'Northern Cheyenne (Tongue River) Reservation', ['Cheyenne'], 1900.2, 1906, box(-106.95, 45.25, -106.2, 45.62), 'Extended to the Tongue River, 19 Mar. 1900')
res('wr', 'Wind River Reservation (Shoshone)', ['Shoshone'], 1868.5, 1874.95, box(-109.6, 42.55, -108.0, 43.8), 'Fort Bridger treaty, 3 July 1868 (bounds approximate)')
res('wr2', 'Wind River Reservation (Shoshone)', ['Shoshone'], 1874.95, 1878.2, box(-109.6, 42.85, -108.0, 43.8), 'The Brunot cession of the Popo Agie valley, 1872, ratified 1874')
res('wr3', 'Wind River Reservation (Shoshone and Northern Arapaho)', ['Shoshone', 'Arapaho'], 1878.2, 1906, box(-109.6, 42.85, -108.0, 43.8), 'The Northern Arapaho placed there, March 1878')
_kca = poly(rseg(*WASHITA, (35.05, -98.0), (35.15, -98.8)), P((35.15, -99.55)), rseg(*NFRED, (35.15, -99.55), (34.4, -99.2)),
            rseg(*REDS, (34.4, -99.2), (34.1, -98.0)))
res('kca', 'Kiowa, Comanche and Apache Reservation', ['Kiowa', 'Comanche', 'Plains Apache'], 1867.81, 1901.6, _kca, 'Medicine Lodge treaty, 21 Oct. 1867; opened 6 Aug. 1901')
_wich = box(-98.65, 35.05, -98.0, 35.45)
res('wich', 'Wichita and Caddo Reservation', ['Wichita', 'Kitsai'], 1859.6, 1901.6, _wich, 'Settled on the Washita in 1859; agreement of 1872 (bounds approximate)')
_ca = poly(P((36.5, -98.0), (36.5, -100.0), (35.15, -100.0), (35.15, -98.8)), rseg(*WASHITA, (35.15, -98.8), (35.05, -98.0))).difference(_wich)
res('cha', 'Cheyenne and Arapaho Reservation', ['Cheyenne', 'Arapaho'], 1869.6, 1892.3, _ca, 'Executive order of 10 Aug. 1869; opened 19 Apr. 1892')
res('osg1', 'Osage Reservation', ['Osage'], 1825.42, 1865.72, box(-100.0, 37.0, -95.0, 37.72), 'Treaty of 2 June 1825: a strip fifty miles wide along the southern line of Kansas (approximate)')
res('osg2', 'Osage Diminished Reserve', ['Osage'], 1865.72, 1872.43, box(-98.3, 37.0, -95.6, 37.45), 'Canville treaty, 29 Sept. 1865 (approximate)')
_kaw = box(-97.0, 36.8, -96.75, 37.0)
res('osg3', 'Osage Reservation', ['Osage'], 1872.43, 1906, poly(P((37.0, -96.0)), rseg(*ARK, (37.0, -97.0), (36.13, -96.0))).difference(_kaw), 'Act of 5 June 1872: in the Indian Territory, bounded by the Arkansas')
res('kaw1', 'Kansa Reservation', ['Kansa'], 1825.42, 1846.4, box(-96.7, 38.95, -95.65, 39.4), 'Treaty of 3 June 1825 (approximate)')
res('kaw2', 'Kansa Reservation (Council Grove)', ['Kansa'], 1846.4, 1873.4, box(-96.55, 38.55, -96.25, 38.8), 'Treaty of 14 Jan. 1846 (approximate)')
res('kaw3', 'Kaw Reservation', ['Kansa'], 1873.4, 1906, _kaw, 'Act of 5 June 1872; removed 1873')
res('paw1', 'Pawnee Reservation', ['Pawnee'], 1857.73, 1876.2, box(-98.1, 41.3, -97.6, 41.55), 'Table Creek treaty, 24 Sept. 1857 (on the Loup at Genoa)')
res('paw2', 'Pawnee Reservation', ['Pawnee'], 1876.2, 1906, box(-97.0, 36.1, -96.5, 36.45), 'Act of 10 Apr. 1876: in the Indian Territory')
res('oma', 'Omaha Reservation', ['Omaha'], 1854.21, 1906, box(-96.6, 41.9, -96.1, 42.3).intersection(WMO), 'Treaty of 16 Mar. 1854')
res('oto1', 'Oto and Missouria Reservation', ['Oto', 'Missouria'], 1854.3, 1881.4, box(-97.05, 39.95, -96.6, 40.2), 'Treaty of 15 Mar. 1854 (on the Big Blue)')
res('oto2', 'Oto and Missouria Reservation', ['Oto', 'Missouria'], 1881.4, 1906, box(-97.2, 36.35, -96.85, 36.6), 'In the Indian Territory from 1881')
res('iowa', 'Iowa Reservation (Great Nemaha)', ['Iowa'], 1836.75, 1906, box(-95.75, 39.85, -95.3, 40.05), 'Treaty of 17 Sept. 1836')
res('tonk', 'Tonkawa Reservation', ['Tonkawa'], 1885.4, 1906, box(-97.4, 36.6, -97.2, 36.75), 'At Fort Oakland, Indian Territory, from 1884–85')
res('jic', 'Jicarilla Reservation', ['Jicarilla'], 1887.15, 1906, box(-107.3, 36.0, -106.85, 37.0), 'Executive order of 11 Feb. 1887')
res('tm', 'Turtle Mountain Reservation', ['Plains Ojibwe'], 1882.97, 1884.24, box(-100.5, 48.6, -99.3, 49.0), 'Executive order of 21 Dec. 1882')
res('tm2', 'Turtle Mountain Reservation', ['Plains Ojibwe'], 1884.24, 1906, box(-99.95, 48.75, -99.75, 48.95), 'Reduced to two townships, 29 Mar. 1884')
res('sik_r', 'Blackfoot (Siksika) Reserve', ['Blackfoot'], 1880.5, 1906, box(-113.2, 50.68, -112.35, 50.92), 'Treaty 7 (1877); surveyed at the Blackfoot Crossing')
res('kai_r', 'Blood (Kainai) Reserve', ['Blackfoot'], 1883.0, 1906, box(-113.6, 49.2, -112.85, 49.62), 'Treaty 7; between the Belly and St. Mary rivers from 1883')
res('pik_r', 'Peigan Reserve', ['Blackfoot'], 1880.5, 1906, box(-113.95, 49.5, -113.55, 49.65), 'Treaty 7; on the Oldman River')
res('sar_r', 'Sarcee Reserve', ['Sarsi'], 1883.0, 1906, box(-114.35, 50.88, -114.05, 51.0), 'Treaty 7; near Calgary from 1883')
res('sto_r', 'Stoney (Morley) Reserve', ['Stoney'], 1879.0, 1906, box(-115.05, 51.12, -114.55, 51.25), 'Treaty 7; at Morley on the Bow')
