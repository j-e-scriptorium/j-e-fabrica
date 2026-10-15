# Seasonal helpers shared by the position model (possgp.py), the bands and the village hunts:
#   the calendar of the year (phi: -1 on the winter ground, +1 on the summer ground, smooth ramps between);
#   which records are dated to a season (season_known);
#   the literature patterns (SEASPRI), each the step from a winter ground to a summer ground, used by possgp.py at half weight
#   as a prior mean for the seasonal component the records then correct.
import math, re
import possmooth as PS

# Calendar: PROF gives, as fractions of the year, when the people leave the winter ground, reach the summer ground, leave it,
# and are back on a winter ground (build/profcal.json: mid-March, early July, early August, late October); between them a
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
# 'pts': a winter ground and a summer ground, (lat, lon). Read in the works named where a page or chapter is given: the Southern
# Cheyenne and Arapaho (West), the Piegan (Ewers), the eighteenth-century Blackfoot, Gros Ventre, Assiniboine and Cree (Henday, Cocking),
# the Sarsi (Jenness), the Comanche after 1840 (Texas Indian Papers), the Kiowa (Levy; Kavanagh), the River Crow after 1849 (Denig),
# the Yankton (DeMallie) and the Blackfoot, Plains Cree and Plains Ojibwe (Handbook 13).
# The rest (Ray and Moodie, Milloy for the Cypress Hills Cree, Ross, Hoxie, Stamm, Pond) are recalled, not checked page by page.
RAY='Ray, Indians in the Fur Trade (1974), ch. 2; Moodie & Ray, “Buffalo Migrations in the Canadian Plains”, Plains Anthropologist 21 (1976)'
WEST='West, The Contested Plains: Indians, Goldseekers, and the Rush to Colorado (1998), ch. 4 (spring by the streams; early summer onto the highlands between the drainages for the hunt and the sun dance; from autumn to March in the timbered river bottoms; 6,000 Indians at the Arkansas big timbers in Nov. 1848) and ch. 11 (1861–64: the reservation bands winter at Point of Rocks on the Arkansas and hunt in summer on the Smoky Hill, Republican and Solomon)'
MILLOY='Milloy, The Plains Cree (1988), pp. 21–22, via Darnell, “Plains Cree”, Handbook of North American Indians 13 (2001), p. 640: in the 1790s the Plains Cree hunted in the woodlands in the plentiful summer season and moved onto the plains for buffalo in winter'
OJB1='Albers, “Plains Ojibwa”, Handbook of North American Indians 13 (2001), p. 653: after 1797 the westernmost Ojibwa joined Cree and Assiniboine on winter buffalo drives at parkland oases on the prairies and returned to the parklands and forests to fish in summer'
OJB2='Albers (2001), p. 654: later, two large annual hunts, in summer and in the fall'
DEMP='Dempsey, “Blackfoot”, Handbook of North American Indians 13 (2001), p. 609 (from Doty 1855 and Crooked Meat Strings): from late October the bands wintered along wooded river bottoms; in spring they scattered onto the prairies; in early summer they gathered in tribal camps on the eastern range, particularly near the Cypress Hills, and held the Medicine Lodge in August.'
EW='Ewers, The Horse in Blackfoot Indian Culture (BAE Bulletin 159, 1955)'
HEN='Henday’s journal, 1754–55, in Burpee, ed., “York Factory to the Blackfeet Country” (1907), pp. 337–51'
COC='Cocking’s journal, 1772–73, in Burpee, ed., “An Adventurer from Hudson Bay” (1908)'
TIPS='Winfrey and Day, eds., The Indian Papers of Texas and the Southwest, 1825–1916 (1966; repr. 1995)'
ARCH=('pts',(51.4,-113.3),(52.0,-106.8))
ARCHSRC=HEN+': in Oct. 1754 the Archithinue camp near Knee Hills Creek moved west for the winter, its leader saying they would come down “in the Spring… after the Buffalo”; in May 1755 they were on the lower South Saskatchewan trading with the Cree canoe brigades; '+COC+', p. 110: the Equestrian Indians “live… to the S.W. Westerly: draw towards the N.E. in March to meet our Natives”. Which Blackfoot division, or the Gros Ventre, Henday met is not certain'
TRADERS=COC+', pp. 101–17: the families wait at the Saskatchewan rendezvous in August, move southwest into the plains to winter, trapping wolves and pounding buffalo, and build canoes in spring to go down to the Bay; '+HEN+' (the same round, wintering farther west)'
NCOM=TIPS+', vol. 5 (Neighbors, July 1855: “All the Northern Comanches bands, are now north near the Arkansas river with their families”; Ford, Feb. 1859: the main camps on the head-waters of the Red and Arkansas, feeding their horses on cottonwood)'
KAV='Kavanagh, Comanche Political History (1996)'
HAMR='Hämäläinen, The Comanche Empire (2008)'
NCOMK=KAV+', pp. 237, 332, 343–44, 348: “The Northern Comanches come into Texas only in the winters” (Stem, 1851); in March 1852 “the mass of the Comanche Nation are journeying from Red River” to reach Fort Atkinson on the Arkansas early in April, “as is their usual practice in the spring”, and by February 1853 they were moving north again; '+HAMR+', pp. 284–85: winter villages in the wooded river valleys from late November to April. Kavanagh doubts any fixed round for the nation as a whole before then (p. 55)'
KIOW='Levy, “Kiowa”, Handbook of North American Indians 13 (2001), p. 908: winter camps along watercourses; by late spring the buffalo moved north out of Texas to the Arkansas River country and the bands followed; the Sun Dance in June and early July; '+NCOMK
SEASPRI={
 'ass':[(1700,1880,('vec',200,90),RAY+': wintered in the parkland and wooded valleys, summered on the open grassland to the south and west')],
 'asn':[(1700,1800,('pts',(52.3,-108.3),(53.2,-104.8)),TRADERS),(1800,1880,('vec',200,90),RAY)],
 'cre':[(1750,1810,('vec',20,90),MILLOY),(1810,1880,('vec',200,90),RAY)],
 'crw':[(1750,1805,('pts',(52.3,-108.3),(53.2,-104.8)),TRADERS+'; '+MILLOY),(1805,1880,('vec',190,90),RAY+'; Milloy, The Plains Cree (1988)')],
 'crs':[(1790,1880,('vec',190,80),'Milloy, The Plains Cree (1988): the Cypress Hills as a wooded winter refuge with summer hunts onto the grassland')],
 'ojb':[(1780,1820,('vec',45,80),OJB1),(1820,1880,('vec',225,90),'Ross, The Red River Settlement (1856): the summer hunts went southwest from Pembina onto the Coteau; winters in the Pembina and Turtle Mountain timber; '+OJB2)],
 'sik':[(1700,1790,ARCH,ARCHSRC),(1800,1880,('pts',(50.73,-112.95),(49.62,-110.0)),DEMP+' The Blackfoot chose their reserve at the Blackfoot Crossing of the Bow, a favorite wintering place.')],
 'kai':[(1700,1790,ARCH,ARCHSRC),],
 'pik':[(1700,1790,ARCH,ARCHSRC),(1800,1847,('pts',(47.6,-111.9),(48.9,-111.5)),EW+', p. 126: about 1833 the Piegan wintered on the Sun and Teton rivers (Culbertson via Bradley); the summer ground is taken from the later period (the Sweetgrass Hills, p. 128), a pairing that is ours'),(1848,1880,('pts',(48.38,-111.75),(48.92,-111.5)),EW+', pp. 41, 125, 128: from about 1848 to 1880 the Piegan bands wintered in the Marias valley from the Cut Bank–Two Medicine junction to the big bend; the Sweetgrass Hills were a favourite Sun Dance ground, in August')],
 'gv':[(1750,1800,('pts',(51.9,-109.0),(53.0,-105.5)),COC+', pp. 109–11: 28 tents of Water-fall Indians at a buffalo pound southwest of the Eagle Hills in December 1772, the Equestrian Indians drawing “towards the N.E. in March” to trade')],
 'sar':[(1800,1880,('vec',135,50),'Jenness, The Sarcee Indians of Alberta (1938), pp. 11–12: in winter family groups camped “along the edge of the woods”; in early spring out onto the prairies; the tribe united in August. No places are named: the direction (summer southeast of the winter ground) and the distance are ours')],
 'cwr':[(1700,1848,('vec',45,100),'Hoxie, Parading through History (1995): River Crow wintered on the Yellowstone and Musselshell, traded at the Missouri villages in summer'),(1849,1870,('pts',(48.0,-104.3),(46.4,-107.3)),'Denig, “Indian Tribes of the Upper Missouri” (BAE 46, 1930), p. 404: after the peace of about 1849 “the Crows winter with the Assiniboin”, near Fort Union, and return to the Yellowstone in summer')],
 'cwm':[(1700,1880,('vec',30,70),'Hoxie (1995): Mountain Crow wintered in the Wind River, Bighorn and upper Yellowstone valleys, hunted out onto the plains in summer')],
 'sho':[(1820,1845,('pts',(43.0,-108.8),(42.9,-110.1)),'Stamm, People of the Wind River (1999): winters in the Wind River valley; summers in the Green River valley, where the rendezvous of 1825–40 were held')],
 'chs':[(1832,1870,('pts',(38.05,-102.6),(39.3,-101.8)),WEST+': winter at the Big Timbers of the Arkansas, summer hunts between the Arkansas and the Smoky Hill; '+'Wedel and Frison, “Environment and Subsistence”, Handbook of North American Indians 13 (2001), p. 56 (after Wedel 1963): the Big Timbers of the Arkansas a regular wintering ground of the Cheyenne, Arapaho and Kiowa')],
 'ars':[(1835,1870,('pts',(38.05,-102.6),(39.3,-101.8)),WEST+'; '+'Wedel and Frison, “Environment and Subsistence”, Handbook of North American Indians 13 (2001), p. 56 (after Wedel 1963): the Big Timbers of the Arkansas a regular wintering ground of the Cheyenne, Arapaho and Kiowa')],
 'cyy':[(1850,1870,('pts',(35.3,-101.0),(37.5,-99.5)),NCOM)],
 'cyk':[(1850,1870,('pts',(35.3,-101.0),(37.5,-99.5)),NCOM)],
 'cyp':[(1840,1859,('pts',(32.9,-99.4),(35.0,-98.9)),TIPS+', vol. 3, doc. 87 (Neighbors, 1849: in winter they “seek shelter… in the upper cross timbers of Texas, between the head waters of the Colorado River and the Wichita Mountains”) and doc. 125 (Marcy and Neighbors, 1854: “their old wintering grounds upon the Clear Fork of the Brazos”); the summer ground from the dated camps toward the Red River and the Salt Plains, 1843–45 (ours)')],
 'cyn':[(1850,1870,('pts',(35.3,-101.0),(37.5,-99.5)),NCOM)],
 'kio':[(1830,1870,('pts',(34.9,-99.2),(37.6,-99.6)),KIOW)],
 'ynk':[(1750,1860,('pts',(42.95,-97.9),(43.3,-99.6)),'DeMallie, “Yankton and Yanktonai”, Handbook of North American Indians 13 (2001), pp. 777, 789: village sites on the Missouri, “where they planted gardens, largely abandoning them during the summer buffalo hunts”; “The Yankton hunted frequently west of the Missouri, on the Niobrara and White rivers, in association with the Brule Teton”')],
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
