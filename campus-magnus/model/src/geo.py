import json,sys
from shapely.geometry import shape,box,mapping
from shapely.ops import unary_union
G=sys.argv[1]; OUT=sys.argv[2]
B=box(-126,20,-76,62)
def load(f): return json.load(open(f"{G}/{f}.geojson"))['features']
def rnd(geom):
    if geom.geom_type=='GeometryCollection':
        ls=[g for g in geom.geoms if 'Line' in g.geom_type]; ps=[g for g in geom.geoms if 'Polygon' in g.geom_type]
        from shapely.ops import unary_union as U
        geom=U(ls) if ls else U(ps)
    def r(c):
        if isinstance(c[0],(int,float)): return [round(c[0],2),round(c[1],2)]
        return [r(x) for x in c]
    m=mapping(geom); return {'type':m['type'],'coordinates':r(m['coordinates'])}
out={}
land=unary_union([shape(f['geometry']) for f in load('ne_50m_land')]).intersection(B).simplify(0.04)
out['land']=rnd(land)
lakes=[shape(f['geometry']).intersection(B) for f in load('ne_50m_lakes')]
out['lakes']=rnd(unary_union([l for l in lakes if not l.is_empty]).simplify(0.03))
st=[shape(f['geometry']).intersection(B) for f in load('ne_50m_admin_1_states_provinces_lines') if f['properties'].get('ADM0_A3') in ('USA','CAN','MEX')]
out['states']=rnd(unary_union([s for s in st if not s.is_empty]).simplify(0.04))
# rivers: 10m north america, keep scalerank<=? 
rv=[]
for f in load('ne_10m_rivers_lake_centerlines'):
    p=f['properties']; g=shape(f['geometry']).intersection(B)
    if g.is_empty: continue
    sr=p.get('scalerank',9)
    if sr<=9: rv.append({'n':p.get('name') or '', 'r':sr, 'g':rnd(g.simplify(0.02))})
P=box(-116,26,-88,55)
X={'Big Sioux','Elk Horn','Marias','Arikaree','Bad','North Canadian','Grand','Cannonball','Moreau','Heart','Washita','Neosho','Verdigris','Big Horn','Bighorn','Wind','Tongue','Rosebud','Judith','Musselshell','Cheyenne','White','James','Kansas','Republican','Smoky Hill','Pecos','Assiniboine','Qu\'Appelle','Bow','Vermilion','Little Sioux','Des Moines','Big Dry','Poplar','Frenchman','Medicine Lodge','North Fork Red','Pembina','Lodgepole','Clarks Fk.  Yellowstone','Greybull','Floyd','Middle Loup','Lance'}
for f in load('ne_10m_rivers_north_america'):
    if not f['geometry']: continue
    p=f['properties']; g=shape(f['geometry']).intersection(P)
    if g.is_empty: continue
    sr=p.get('scalerank',12); n=p.get('name') or ''
    if sr<=10 or n in X: rv.append({'n':n,'r':sr,'g':rnd(g.simplify(0.02))})
out['rivers']=rv
json.dump(out,open(OUT,'w'),separators=(',',':'))
print(len(rv), sum(1 for r in rv if r['r']<=5))
