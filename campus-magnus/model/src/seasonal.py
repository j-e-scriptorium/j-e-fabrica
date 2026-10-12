# Seasonal round of the nomadic divisions.
# A division's place at time t = annual centre c(t) + phi(t) * A(t), where phi = +1 at midsummer (20 July), -1 at midwinter
# (18 January) and A(t) is a slowly varying vector (km east, km north): half the step from the winter ground to the summer ground.
# A is estimated from places dated to a season, shrunk toward a prior taken from the ethnographic literature (SEASPRI);
# where neither exists A is zero and the division has no seasonal swing of its own.
import math, re
import numpy as np
import possmooth as PS

# Seasonal profile: -1 on the winter ground, +1 on the summer ground. PROF gives, as fractions of the year, when the division
# leaves the winter ground, reaches the summer ground, leaves it, and is back on a winter ground; between them it moves on a
# smooth ramp. None means a plain cosine peaking on 20 July.
PROF=None
def _ss(x): return x*x*(3-2*x)
def phi(t,P=None):
    P=P if P is not None else PROF; f=t%1
    if P is None: return math.cos(2*math.pi*(f-0.55))
    a,b,c,d=P
    if f<a or f>=d: return -1.0
    if f<b: return -1+2*_ss((f-a)/(b-a))
    if f<c: return 1.0
    return 1-2*_ss((f-c)/(d-c))

MONTH=re.compile(r'\b(Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z.]*\b|\b(spring|summer|winter|autumn|fall)\b|sun[ -]dance|wintered|winters',re.I)
NOSEASON=re.compile(r'Agency|agency|reserve|reservation (was )?established|treaty council|Treaty',re.I)
def season_known(y,raw,r):
    f=round(y%1,3)
    if f==0 or (r or 0)>200 or NOSEASON.search(raw or ''): return False
    return abs(f-0.5)>0.005 or bool(MONTH.search(raw or ''))

# Prior seasonal patterns. 'vec': bearing (degrees from north) of the summer ground from the winter ground, and half the distance;
# 'pts': a winter ground and a summer ground, (lat, lon). All recalled from the works named, not checked page by page for this build.
RAY='Ray, Indians in the Fur Trade (1974), ch. 2; Moodie & Ray, “Buffalo Migrations in the Canadian Plains”, Plains Anthropologist 21 (1976)'
EWERS='Ewers, The Horse in Blackfoot Indian Culture (1955), pp. 123–29; The Blackfeet (1958)'
HAM='Hämäläinen, The Comanche Empire (2008), ch. 7; “The Rise and Fall of Plains Indian Horse Cultures”, JAH 90 (2003)'
WEST='West, The Contested Plains (1998), chs. 3–4; Moore, The Cheyenne Nation (1987)'
MILLOY='Milloy, The Plains Cree (1988), pp. 21–22, via Darnell, “Plains Cree”, Handbook of North American Indians 13 (2001), p. 640: in the 1790s the Plains Cree hunted in the woodlands in the plentiful summer season and moved onto the plains for buffalo in winter'
OJB1='Albers, “Plains Ojibwa”, Handbook of North American Indians 13 (2001), p. 653: after 1797 the westernmost Ojibwa joined Cree and Assiniboine on winter buffalo drives at parkland oases on the prairies and returned to the parklands and forests to fish in summer'
OJB2='Albers (2001), p. 654: later, two large annual hunts, in summer and in the fall'
DEMP='Dempsey, “Blackfoot”, Handbook of North American Indians 13 (2001), p. 609 (from Doty 1855 and Crooked Meat Strings): from late October the bands wintered along wooded river bottoms; in spring they scattered onto the prairies; in early summer they gathered in tribal camps on the eastern range, particularly near the Cypress Hills, and held the Medicine Lodge in August.'
SEASPRI={
 'ass':[(1700,1880,('vec',200,90),RAY+': wintered in the parkland and wooded valleys, summered on the open grassland to the south and west')],
 'asn':[(1700,1880,('vec',200,90),RAY)],
 'cre':[(1750,1810,('vec',20,90),MILLOY),(1810,1880,('vec',200,90),RAY)],
 'crw':[(1750,1810,('vec',20,90),MILLOY),(1810,1880,('vec',190,90),RAY+'; Milloy, The Plains Cree (1988)')],
 'crs':[(1790,1880,('vec',190,80),'Milloy, The Plains Cree (1988): the Cypress Hills as a wooded winter refuge with summer hunts onto the grassland')],
 'ojb':[(1780,1820,('vec',45,80),OJB1),(1820,1880,('vec',225,90),'Ross, The Red River Settlement (1856): the summer hunts went southwest from Pembina onto the Coteau; winters in the Pembina and Turtle Mountain timber; '+OJB2)],
 'sik':[(1700,1800,('vec',90,70),EWERS),(1800,1880,('pts',(50.73,-112.95),(49.62,-110.0)),DEMP+' The Blackfoot chose their reserve at the Blackfoot Crossing of the Bow, a favorite wintering place.')],
 'kai':[(1700,1880,('vec',90,70),EWERS+'. Dempsey (Handbook 13, p. 609) names the Belly–St. Mary confluence as a wintering ground and the Cypress Hills as the summer range, but a pattern built on those two places predicts the Blood’s dated places worse than this one.')],
 'pik':[(1700,1880,('vec',90,70),EWERS+'. A pattern built on Dempsey’s wintering grounds (Marias and Milk valleys) and the Cypress Hills predicts the Piegan’s dated places worse than this one; their dated summer camps lie on the Missouri and the Marias.')],
 'cwr':[(1700,1880,('vec',45,100),'Hoxie, Parading through History (1995): River Crow wintered on the Yellowstone and Musselshell, traded at the Missouri villages in summer')],
 'cwm':[(1700,1880,('vec',30,70),'Hoxie (1995): Mountain Crow wintered in the Wind River, Bighorn and upper Yellowstone valleys, hunted out onto the plains in summer')],
 'sho':[(1820,1845,('pts',(43.0,-108.8),(42.9,-110.1)),'Stamm, People of the Wind River (1999): winters in the Wind River valley; summers in the Green River valley, where the rendezvous of 1825–40 were held')],
 'chs':[(1832,1870,('pts',(38.05,-102.6),(39.3,-101.8)),WEST+': winter at the Big Timbers of the Arkansas, summer hunts between the Arkansas and the Smoky Hill; '+'Wedel and Frison, “Environment and Subsistence”, Handbook of North American Indians 13 (2001), p. 56 (after Wedel 1963): the Big Timbers of the Arkansas a regular wintering ground of the Cheyenne, Arapaho and Kiowa')],
 'ars':[(1835,1870,('pts',(38.05,-102.6),(39.3,-101.8)),WEST+'; '+'Wedel and Frison, “Environment and Subsistence”, Handbook of North American Indians 13 (2001), p. 56 (after Wedel 1963): the Big Timbers of the Arkansas a regular wintering ground of the Cheyenne, Arapaho and Kiowa')],
 'cyy':[(1750,1875,('vec',340,70),HAM+': winter in sheltered, wooded river valleys; summer hunting and trading out on the high plains')],
 'cyk':[(1750,1875,('vec',340,70),HAM)],
 'cyp':[(1750,1875,('vec',340,70),HAM)],
 'cyn':[(1830,1875,('vec',340,70),HAM)],
 'cyq':[(1835,1875,('vec',340,70),HAM)],
 'ynk':[(1750,1860,('vec',90,80),'Tabeau’s Narrative (ed. Abel, 1939); Lewis & Clark: summer trade fair on the James River (the “Dakota rendezvous”), winters in the Missouri timber')],
 'yku':[(1750,1870,('vec',90,80),'as for the Yankton (Tabeau)')],
 'ykl':[(1750,1870,('vec',90,80),'as for the Yankton (Tabeau)')],
 'sis':[(1750,1862,('vec',270,80),'Pond (1908): winters in the timber of the Minnesota and Lake Traverse, summer hunts west onto the Coteau des Prairies')],
 'wpt':[(1750,1862,('vec',270,70),'as for the Sisseton (Pond)')],
}
def _prior_raw(gid,t,lat0,lon0):
    for (a,b,spec,src) in SEASPRI.get(gid,[]):
        if a<=t<=b:
            L=SEASPRI.get(gid,[]); cont_in=a<=1700 or any(x[1]==a for x in L); cont_out=any(x[0]==b for x in L)
            ramp=max(0.0,min(1.0,1.0 if cont_in else (t-a)/3,1.0 if cont_out else (b-t)/3))   # fade in and out over three years at the ends of a pattern
            if spec[0]=='vec':
                th=math.radians(spec[1]); return (spec[2]*math.sin(th)*ramp, spec[2]*math.cos(th)*ramp), True
            W=PS.local(lat0,lon0,*spec[1]); S=PS.local(lat0,lon0,*spec[2])
            return ((S[0]-W[0])/2*ramp,(S[1]-W[1])/2*ramp), True
    return (0.0,0.0), False

def prior_A(gid,t,lat0,lon0):
    """the literature pattern, eased over five years where one pattern gives way to the next"""
    vals=[_prior_raw(gid,t+d,lat0,lon0) for d in (-2,-1,0,1,2)]
    has=_prior_raw(gid,t,lat0,lon0)[1] or any(v[1] for v in vals[1:4])
    return (sum(v[0][0] for v in vals)/5,sum(v[0][1] for v in vals)/5),has
def herm(arr,y):
    """monotone cubic Hermite through (t, x, y) points, as on the page"""
    n=len(arr)
    if y<=arr[0][0]: return arr[0][1],arr[0][2]
    if y>=arr[-1][0]: return arr[-1][1],arr[-1][2]
    i=1
    while arr[i][0]<y: i+=1
    a,b=arr[i-1],arr[i]; h=b[0]-a[0]; t=(y-a[0])/h
    def tan(k,c):
        s1=(arr[k][c]-arr[k-1][c])/(arr[k][0]-arr[k-1][0]) if k>0 else None
        s2=(arr[k+1][c]-arr[k][c])/(arr[k+1][0]-arr[k][0]) if k<n-1 else None
        if s1 is None: return s2
        if s2 is None: return s1
        if s1*s2<=0: return 0
        m=(s1+s2)/2; return math.copysign(min(abs(m),3*min(abs(s1),abs(s2))),m)
    t2=t*t;t3=t2*t;h00=2*t3-3*t2+1;h10=t3-2*t2+t;h01=-2*t3+3*t2;h11=t3-t2
    f=lambda c: h00*a[c]+h10*h*tan(i-1,c)+h01*b[c]+h11*h*tan(i,c)
    return f(1),f(2)

def residuals(docs,gs,y0,y1,P,Afun=None,skip=None):
    """Leave-one-out residuals of the season-dated places from the smoothed track of everything else (deseasonalized by Afun)."""
    R=[]
    for j,d in enumerate(docs):
        if not d[4] or j==skip: continue
        ob=[]
        for i,(t,x,y,r,s) in enumerate(docs):
            if i==j or i==skip: continue
            if s and Afun is not None: a=Afun(t); p=phi(t); x,y=x-p*a[0],y-p*a[1]
            ob.append((t,x,y,(P['k']*r)**2+P['s0']**2))
        ob+=[(t,x,y,P['sg']**2) for (t,x,y) in gs]
        if not ob: continue
        T,ms,Ps=PS.smooth(y0,y1,ob,P['q']); m,v=PS.predict_at(T,ms,Ps,d[0])
        t,x,y,r,_=d; R.append((t,phi(t),x-m[0],y-m[1],v+(P['k']*r)**2+P['s0']**2))
    return R
def estimate(R,years,tau,sigA,sigN,gid,lat0,lon0,Rs=(),lam=0.0):
    """Rs: residuals from sibling divisions of the same people, counted at weight lam (partial pooling)."""
    R=list(R)+[(t,p,rx,ry,v/lam) for (t,p,rx,ry,v) in Rs] if lam>0 else R
    A=np.zeros((len(years),2)); W=np.zeros(len(years)); V=np.zeros(len(years))
    for k,ty in enumerate(years):
        a0,has=prior_A(gid,ty,lat0,lon0); s2=(sigA if has else sigN)**2
        num=np.array(a0)/s2; den=1/s2
        for (t,_p,rx,ry,v) in R:
            p=phi(t); w=math.exp(-abs(ty-t)/tau)/v; num=num+w*p*np.array([rx,ry]); den+=w*p*p; W[k]+=w*p*p
        a=num/den; V[k]=1/den; nrm=math.hypot(*a)
        if nrm>200: a=a*200/nrm
        A[k]=a
    estimate.var=V
    return A,W
def Afun_of(years,A):
    def f(t):   # linear between whole years, as on the page
        u=min(len(years)-1.0,max(0.0,t-years[0])); i=int(u); j=min(len(years)-1,i+1); w=u-i; return A[i]*(1-w)+A[j]*w
    return f
def fit_A(docs,gs,y0,y1,P,tau,sigA,sigN,gid,lat0,lon0,iters=2,skip=None):
    years=np.arange(int(math.floor(y0)),int(math.ceil(y1))+1); Af=None
    for it in range(iters):
        R=residuals(docs,gs,y0,y1,P,Af,skip); A,W=estimate(R,years,tau,sigA,sigN,gid,lat0,lon0); Af=Afun_of(years,A)
    return years,A,W
