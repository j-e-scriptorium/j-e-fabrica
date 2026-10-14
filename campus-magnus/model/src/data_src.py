# Plains bands 1700-1905: source data.
# Three provenance tiers, kept physically separate in this file:
#   OBS    - documented: a count and/or place stated in a source fetched and read for this build.
#            kind 'primary' = contemporary observer; 'secondary' = later scholarly reconstruction.
#            basis says how persons were obtained (stated souls, or lodges/warriors x multiplier).
#            loc 'stated' = place described in the source (geocoded by us, radius r km);
#                'inferred' = source gives count but place is our placement.
#   GUESS  - our best-guess keyframes (never presented as data).
#   SETTLE - non-Native settlements/posts; field 7 names the reference each was checked against ('' = recalled, unchecked).
# Census towns come separately from Steiner & Heppler (Stanford) US Historical City Populations.

# Sources read in PDFs supplied by the project's owner (tier A1). Pages as printed, with the PDF page where it helps.
BOLTON=lambda pp: f'Bolton, ed., Athanase de Mézières and the Louisiana–Texas Frontier, 1768–1780 (1914), {pp}'
HENDAY=lambda pp: f'Henday’s journal, 1754–55, in Burpee, ed., “York Factory to the Blackfeet Country” (1907), {pp}'
COCKING=lambda pp: f'Cocking’s journal, 1772–73, in Burpee, ed., “An Adventurer from Hudson Bay” (1908), {pp}'
VEREND=lambda pp: f'Burpee, ed., Journals and Letters of Pierre Gaultier de Varennes de la Vérendrye and His Sons (1927), {pp}'
EWERS2=lambda pp: f'Ewers, The Horse in Blackfoot Indian Culture (BAE Bulletin 159, 1955), {pp}'
DENIG46=lambda pp: f'Denig, “Indian Tribes of the Upper Missouri” (BAE 46th Annual Report, 1930), {pp}'
JENNESS=lambda pp: f'Jenness, The Sarcee Indians of Alberta (1938), {pp}'
_TIP=lambda v: (lambda pp: f'Winfrey and Day, eds., The Indian Papers of Texas and the Southwest, 1825–1916, vol. {v} (1966; repr. 1995), {pp}')
TIPV1,TIPV2,TIPV3,TIPV4,TIPV5=(_TIP(v) for v in (1,2,3,4,5))

FAM = {  # language family -> categorical slot (fixed order)
 'dakotan':1, 'algonquian':2, 'numic':3, 'caddoan':4, 'msiouan':5, 'dhegiha':6, 'athabaskan':7, 'kiowa':8}
FAMNAME = {'dakotan':'Dakotan Siouan','algonquian':'Algonquian','numic':'Numic (Uto-Aztecan)','caddoan':'Caddoan',
 'msiouan':'Missouri River Siouan','dhegiha':'Dhegiha & Chiwere Siouan','athabaskan':'Athabaskan','kiowa':'Kiowa-Tanoan'}

# id, tribe label, division label, family, start, end, lifeway ('nomadic'|'village')
GROUPS = [
 ('bru','Lakota','Brulé (Sičháŋǧu)','dakotan',1700,1905,'nomadic'),
 ('ogl','Lakota','Oglala','dakotan',1700,1905,'nomadic'),
 ('min','Lakota','Miniconjou','dakotan',1700,1905,'nomadic'),
 ('hnk','Lakota','Hunkpapa','dakotan',1700,1905,'nomadic'),
 ('sih','Lakota','Sihasapa (Blackfeet Lakota)','dakotan',1700,1905,'nomadic'),
 ('sna','Lakota','Itazipčho (Sans Arc)','dakotan',1700,1905,'nomadic'),
 ('twk','Lakota','Oohenunpa (Two Kettle)','dakotan',1700,1905,'nomadic'),
 ('ynk','Yankton','Yankton','dakotan',1700,1905,'nomadic'),
 ('yku','Yanktonai','Upper Yanktonai & Cuthead','dakotan',1700,1905,'nomadic'),
 ('ykl','Yanktonai','Hunkpatina (Lower Yanktonai)','dakotan',1700,1905,'nomadic'),
 ('mde','Dakota','Mdewakanton','dakotan',1700,1905,'village'),
 ('wpk','Dakota','Wahpekute','dakotan',1700,1905,'nomadic'),
 ('wpt','Dakota','Wahpeton','dakotan',1700,1905,'nomadic'),
 ('sis','Dakota','Sisseton','dakotan',1700,1905,'nomadic'),
 ('ass','Assiniboine','Southern (Missouri) Assiniboine','dakotan',1700,1905,'nomadic'),
 ('asn','Assiniboine','Northern (Saskatchewan) Assiniboine','dakotan',1700,1905,'nomadic'),
 ('cre','Plains Cree','Qu’Appelle–Touchwood Cree','algonquian',1700,1905,'nomadic'),
 ('crw','Plains Cree','Fort des Prairies Cree','algonquian',1700,1905,'nomadic'),
 ('crs','Plains Cree','Cypress Hills–Wood Mountain Cree','algonquian',1790,1905,'nomadic'),
 ('ojb','Plains Ojibwe','Pembina–Turtle Mountain','algonquian',1780,1905,'nomadic'),
 ('sik','Blackfoot','Siksika','algonquian',1700,1905,'nomadic'),
 ('kai','Blackfoot','Kainai (Blood)','algonquian',1700,1905,'nomadic'),
 ('pik','Blackfoot','Piikani (Piegan)','algonquian',1700,1905,'nomadic'),
 ('gv','Gros Ventre','A’aninin (Gros Ventre, Fall Indians)','algonquian',1700,1905,'nomadic'),
 ('chy','Cheyenne','Cheyenne (before division)','algonquian',1700,1832,'village→nomadic'),
 ('chn','Cheyenne','Northern Cheyenne','algonquian',1832,1905,'nomadic'),
 ('chs','Cheyenne','Southern Cheyenne','algonquian',1832,1905,'nomadic'),
 ('ara','Arapaho','Arapaho (before division)','algonquian',1700,1835,'nomadic'),
 ('arn','Arapaho','Northern Arapaho','algonquian',1835,1905,'nomadic'),
 ('ars','Arapaho','Southern Arapaho','algonquian',1835,1905,'nomadic'),
 ('cwm','Crow','Mountain Crow','msiouan',1700,1905,'nomadic'),
 ('cwr','Crow','River Crow','msiouan',1700,1884,'nomadic'),
 ('man','Mandan','Mandan','msiouan',1700,1905,'village'),
 ('hid','Hidatsa','Hidatsa','msiouan',1700,1905,'village'),
 ('kio','Kiowa','Kiowa','kiowa',1700,1905,'nomadic'),
 ('kap','Plains Apache','Plains (Kiowa) Apache','athabaskan',1700,1905,'nomadic'),
 ('apc','Plains Apache','Cuartelejo & Paloma Apache','athabaskan',1700,1732,'village'),
 ('jic','Jicarilla','Jicarilla Apache','athabaskan',1700,1905,'nomadic'),
 ('lip','Lipan','Lipan Apache','athabaskan',1700,1905,'nomadic'),
 ('cyj','Comanche','Jupe','numic',1700,1795,'nomadic'),
 ('cyy','Comanche','Yamparika','numic',1700,1905,'nomadic'),
 ('cyk','Comanche','Kotsoteka','numic',1700,1905,'nomadic'),
 ('cyp','Comanche','Penateka (Eastern Comanche)','numic',1745,1905,'nomadic'),
 ('cyn','Comanche','Nokoni','numic',1830,1905,'nomadic'),
 ('cyq','Comanche','Kwahadi','numic',1835,1905,'nomadic'),
 ('sho','Shoshone','Eastern (Plains) Shoshone','numic',1700,1905,'nomadic'),
 ('wic','Wichita','Wichita (Taovaya & allies)','caddoan',1700,1905,'village'),
 ('pwc','Pawnee','Chawi & Pitahawirata (Grand Pawnee)','caddoan',1700,1905,'village'),
 ('pwk','Pawnee','Kitkahahki (Republican Pawnee)','caddoan',1700,1905,'village'),
 ('pws','Pawnee','Skiri (Loup Pawnee)','caddoan',1700,1905,'village'),
 ('ari','Arikara','Arikara','caddoan',1700,1905,'village'),
 ('oma','Omaha','Omaha','dhegiha',1700,1905,'village'),
 ('pon','Ponca','Ponca','dhegiha',1700,1905,'village'),
 ('oto','Oto','Oto','dhegiha',1700,1905,'village'),
 ('mis','Missouria','Missouria','dhegiha',1700,1830,'village'),
 ('kaw','Kansa','Kansa (Kaw)','dhegiha',1700,1905,'village'),
 ('osg','Osage','Great Osage','dhegiha',1700,1905,'village'),
 ('osl','Osage','Little Osage','dhegiha',1700,1905,'village'),
 ('osa','Osage','Arkansas Osage (Claremore’s band)','dhegiha',1802,1839,'village'),
 ('iow','Iowa','Iowa (Báxoje)','dhegiha',1700,1905,'village'),
]
# groups that appear only as documented names we could not identify; no guess track
UNIDENT = [
 ('u_cas','Unidentified','Castahana (Clark 1805; probably an Arapahoan group, Parks 2001)'),
 ('u_dot','Unidentified','Dotame (Clark 1805; probably a Plains Apachean group, Parks 2001)'),
]

P = {  # reference places (lat, lon) — our geocoding
 'blackhills':(44.0,-103.75),'whiteR':(43.7,-100.6),'badR_mouth':(44.37,-100.37),'chyR_mid':(44.5,-102.2),
 'moreau':(45.3,-101.5),'grandR':(45.75,-101.4),'cannonball':(46.35,-101.1),'powderR':(44.9,-106.0),
 'lbh':(45.57,-107.43),'bighorn_mouth':(46.15,-107.47),'bighorn_basin':(44.4,-108.2),'windR':(43.2,-108.9),
 'musselshell':(46.8,-108.2),'milk_low':(48.1,-106.3),'milk_mid':(48.45,-108.4),'marias':(48.25,-111.2),
 'belly':(49.55,-112.8),'bow':(50.9,-113.2),'fort_union':(48.0,-104.0),'white_earth':(48.4,-102.8),
 'souris':(48.9,-101.4),'quappelle':(50.75,-103.8),'wood_mt':(49.4,-106.4),'cypress':(49.6,-109.9),
 'sask_forks':(53.2,-105.0),'edmonton':(53.54,-113.5),'eagle_hills':(52.4,-108.6),'battleford':(52.75,-108.3),
 'pembina':(48.97,-97.25),'turtle_mt':(48.88,-99.8),'devils_lake':(47.95,-98.85),'lake_traverse':(45.65,-96.85),
 'minn_mouth':(44.88,-93.2),'mille_lacs':(46.2,-93.65),'laramie':(42.2,-104.55),'s_platte':(40.4,-104.3),
 'bents':(38.04,-103.43),'sand_creek':(38.54,-102.51),'medicine_lodge':(37.28,-98.58),'washita':(35.62,-99.67),
 'darlington':(35.55,-98.0),'ft_sill':(34.66,-98.4),'anadarko':(35.07,-98.24),'palo_duro':(34.95,-101.67),
 'pine_ridge':(43.03,-102.55),'rosebud':(43.23,-100.85),'standing_rock':(46.09,-100.63),'chyR_agency':(44.6,-100.75),
 'crow_creek':(44.1,-99.33),'yankton_ag':(42.98,-98.42),'santee':(42.83,-97.85),'sisseton':(45.6,-97.05),
 'ft_peck':(48.1,-105.2),'ft_belknap':(48.48,-108.77),'like_fishhook':(47.58,-101.85),'ft_clark':(47.25,-101.27),
 'knifeR':(47.33,-101.39),'heartR':(46.83,-100.85),'lame_deer':(45.62,-106.67),'wind_res':(43.0,-108.6),
 'crow_ag':(45.6,-107.46),'blackfeet_ag':(48.45,-112.55),'blood_res':(49.3,-113.1),'siksika_res':(50.85,-112.95),
 'pawnee_ok':(36.34,-96.8),'genoa':(41.45,-97.73),'ponca_ok':(36.68,-97.05),'omaha_res':(42.12,-96.36),
 'oto_ok':(36.47,-97.18),'big_blue':(40.05,-96.95),'kaw_ok':(36.75,-96.85),'council_grove':(38.66,-96.49),
 'pawhuska':(36.67,-96.33),'neosho':(37.5,-95.3),'nemaha':(40.0,-95.45),'grand_pawnee':(41.25,-97.35),
 'loup_vil':(41.45,-97.95),'rep_vil':(39.95,-97.92),'osage_vil':(37.95,-94.3),'three_forks':(35.85,-95.35),
 'kaw_vil':(39.2,-96.6),'oto_vil':(41.0,-96.3),'omaha_vil':(42.32,-96.49),'ponca_ck':(42.8,-98.1),
 'arikara_1804':(45.55,-100.45),'skidi_loup':(41.6,-98.3),'llano':(34.2,-101.8),'edwards':(30.6,-99.4),
 'spanish_fort':(33.95,-97.65),'cuartelejo':(38.48,-100.92),'taos':(36.4,-105.57),'pecos_pueblo':(35.55,-105.68),
}

# ---------------------------------------------------------------------------------------------
# OBS: documented observations. g = group id, or list of ids for an aggregate (whole-tribe) count.
# pop = persons (None = place-only record). raw = what the source says. r = location radius km.
CLARK = 'Clark, “Estimate of the Eastern Indians,” Fort Mandan, winter 1804–05 (Moulton ed., Journals of the Lewis & Clark Expedition, vol. 3; UNL online edition)'
CLARK06 = 'Clark/Lewis, printed “Statistical View of the Indian Nations,” 1806 (remarks paragraphs in the UNL edition of the Estimate)'
DENIG = 'Denig, “Indian Tribes of the Upper Missouri” (ms. c. 1854; BAE 46th Annual Report, 1930)'
HAYDEN = 'Hayden, Contributions to the Ethnography and Philology of the Indian Tribes of the Missouri Valley (1862)'
HODGE = 'Hodge ed., Handbook of American Indians North of Mexico (BAE Bulletin 30, 1907–10)'
OBS = [
 # ---- Clark 1805 (souls: the lower of Clark's two figures; raw keeps both) ----
 dict(g=['osg','osa'],y=1805,pop=5000,raw='1,200 warriors; souls 7,000 [or] 5,000; 2 villages (Osage R. & Three Forks of Arkansas)',basis='souls',loc='stated',at=P['osage_vil'],r=150,src=CLARK,kind='primary'),
 dict(g='osl',y=1805,pop=1300,raw='300 warriors; souls 2,000 [or] 1,300; Osage R., near the Great Osage',basis='souls',loc='stated',at=(38.05,-94.2),r=40,src=CLARK,kind='primary'),
 dict(g='osa',y=1805,pop=None,raw='“About three years since, nearly one half of this nation… emigrated to the three forks of the Arkansas”',basis='',loc='stated',at=P['three_forks'],r=40,src=CLARK06,kind='primary'),
 dict(g='kaw',y=1805,pop=1300,raw='300 warriors; souls 2,000 [or] 1,300; village 80 leagues up the Kansas R., north side',basis='souls',loc='stated',at=P['kaw_vil'],r=40,src=CLARK,kind='primary'),
 dict(g='oto',y=1805,pop=500,raw='120 warriors; 500 souls; village 18 leagues up the Platte, SE side',basis='souls',loc='stated',at=P['oto_vil'],r=30,src=CLARK,kind='primary'),
 dict(g='mis',y=1805,pop=300,raw='80 warriors; souls 500 [or] 300; live with the Otoes',basis='souls',loc='stated',at=(41.0,-96.25),r=30,src=CLARK,kind='primary'),
 dict(g='pwc',y=1805,pop=1600,raw='400 warriors; souls 2,000 [or] 1,600; village 30 leagues up the Platte, S. side',basis='souls',loc='stated',at=P['grand_pawnee'],r=30,src=CLARK,kind='primary'),
 dict(g='pws',y=1805,pop=1000,raw='280 warriors; souls 1,600 [or] 1,000; on the Loup R., 36 leagues from its mouth',basis='souls',loc='stated',at=P['loup_vil'],r=30,src=CLARK,kind='primary'),
 dict(g='pwk',y=1805,pop=1400,raw='300 warriors; souls 2,000 [or] 1,400; living in the Grand Pawnee village, rejoined “last spring”',basis='souls',loc='stated',at=(41.27,-97.32),r=30,src=CLARK,kind='primary'),
 dict(g='pwk',y=1795,pop=None,raw='“About ten years since they withdrew… and established a village on a large northwardly branch of the Kanzas” (Republican R.)',basis='',loc='stated',at=P['rep_vil'],r=60,src=CLARK06,kind='primary'),
 dict(g='oma',y=1805,pop=600,raw='60–80 lodges; 150–200 warriors; souls 1,200 [or] 600; rove on the Niobrara and head of the Loup since the 1802 smallpox',basis='souls',loc='stated',at=(42.5,-98.8),r=120,src=CLARK,kind='primary'),
 dict(g='oma',y=1795,pop=2800,raw='“About ten years since, they boasted 700 warriors” (village 236 mi above the Platte)',basis='warriors × 4',loc='stated',at=P['omaha_vil'],r=20,src=CLARK06,kind='primary'),
 dict(g='pon',y=1805,pop=200,raw='20 lodges; 50 warriors; souls 300 [or] 200; rove with the Omaha',basis='souls',loc='stated',at=(42.55,-98.65),r=120,src=CLARK,kind='primary'),
 dict(g='ari',y=1805,pop=2000,raw='500 warriors; souls 3,000 [or] 2,000; 3 villages near the Grand R. (“remains of eight different tribes”)',basis='souls',loc='stated',at=P['arikara_1804'],r=15,src=CLARK,kind='primary'),
 dict(g='man',y=1805,pop=1250,raw='2 villages; 350 warriors; 1,250 souls (1,500 struck out); Knife R. mouth area',basis='souls',loc='stated',at=(47.28,-101.2),r=10,src=CLARK,kind='primary'),
 dict(g='man',y=1780,pop=None,raw='“About 25 years since they lived in six villages, about forty miles below their present villages”',basis='',loc='stated',at=(46.95,-100.95),r=30,src=CLARK06,kind='primary'),
 dict(g='hid',y=1805,pop=2500,raw='Minitari: 2 villages on the Knife R.; 500–600 warriors; 2,500 souls',basis='souls',loc='stated',at=P['knifeR'],r=10,src=CLARK,kind='primary',part=True),
 dict(g='hid',y=1805,pop=200,raw='Awaxawi (“Shoe Men”): 1 village at Knife R. mouth; 50 warriors; 200 souls (300 struck out)',basis='souls',loc='stated',at=(47.32,-101.36),r=10,src=CLARK,kind='primary',part=True),
 dict(g='iow',y=1805,pop=800,raw='200–250 warriors; 800 souls (1,600 struck out); 40 leagues up the Des Moines R.',basis='souls',loc='stated',at=(40.8,-92.1),r=40,src=CLARK,kind='primary'),
 dict(g='wpt',y=1805,pop=700,raw='Wahpeton: 80 lodges; 200 warriors; 700 souls; north side of the Minnesota R., 18 leagues up',basis='souls',loc='stated',at=(44.75,-93.6),r=40,src=CLARK,kind='primary'),
 dict(g='mde',y=1805,pop=1200,raw='Mdewakanton: 120 lodges; 300 warriors; 1,200 souls; mouth of the Minnesota R.',basis='souls',loc='stated',at=P['minn_mouth'],r=30,src=CLARK,kind='primary'),
 dict(g='wpk',y=1805,pop=400,raw='Wahpekute: 60 lodges; 150 warriors; souls 700 [or] 400; 30 leagues up the Minnesota R.',basis='souls',loc='stated',at=(44.3,-93.95),r=50,src=CLARK,kind='primary'),
 dict(g='sis',y=1805,pop=800,raw='Sisseton: 80 lodges; 200 warriors; 800 souls; head of the Minnesota R. & Red R.',basis='souls',loc='stated',at=(45.6,-96.7),r=80,src=CLARK,kind='primary'),
 dict(g=['yku','ykl'],y=1805,pop=1600,raw='“Yanktons of the North”: 200 lodges; 500 warriors; 1,600 souls; heads of the James R., to the Missouri',basis='souls',loc='stated',at=(46.4,-98.6),r=150,src=CLARK,kind='primary'),
 dict(g='ynk',y=1805,pop=700,raw='Yankton “on River Demoin”: 80 lodges; 200 warriors; 700 souls; lower Big Sioux, Floyd’s & Little Sioux rivers',basis='souls',loc='stated',at=(43.0,-96.4),r=100,src=CLARK,kind='primary'),
 dict(g='bru',y=1805,pop=900,raw='Teton Bois Brulé: 120 lodges; 300 warriors; souls 1,400 → 900; E. side of the Missouri, White R. to Teton (Bad) R.',basis='souls',loc='stated',at=(44.0,-99.7),r=80,src=CLARK,kind='primary'),
 dict(g='ogl',y=1805,pop=360,raw='Teton Okandandas: 50 lodges; 120 warriors; souls 600 [or] 360; Missouri from Teton R. to Cheyenne R.',basis='souls',loc='stated',at=(44.6,-100.6),r=60,src=CLARK,kind='primary'),
 dict(g='min',y=1805,pop=750,raw='Teton Minnakenozzo: 100 lodges; 250 warriors; souls 1,200 [or] 750; Cheyenne R. up to the Arikara',basis='souls',loc='stated',at=(45.2,-100.7),r=60,src=CLARK,kind='primary'),
 dict(g=['hnk','sih','sna','twk'],y=1805,pop=900,raw='Teton Saone: 120 lodges; 300 warriors; souls 1,400 [or] 900; Missouri from the Arikara to Beaver Cr. (Hodge: probably includes the Hunkpapa)',basis='souls',loc='stated',at=(45.95,-100.6),r=70,src=CLARK,kind='primary'),
 dict(g='chy',y=1805,pop=1200,raw='Shar-ha (Cheyenne): 110 lodges; 300 warriors; souls 1,700 [or] 1,200; heads of the Cheyenne R. in the Black Hills',basis='souls',loc='stated',at=(44.2,-103.9),r=100,src=CLARK,kind='primary'),
 dict(g='kio',y=1805,pop=700,raw='Kiowa with Wetapahato: 70 lodges; 200 warriors; souls 1,000 [or] 700; Paduca (N.) fork of the Platte & Loup, SW of the Black Hills',basis='souls',loc='stated',at=(42.4,-103.2),r=150,src=CLARK,kind='primary'),
 dict(g='ara',y=1805,pop=2000,raw='Clark’s three Arapaho groups: Kanenavich, 150 lodges, 400 warriors, 1,500 souls (heads of the N. Platte & S. fork of the Cheyenne); Staetan (“Kites”), 25 lodges, 75 warriors, 300 souls (head of the Cheyenne, often with the Kanenavich); Nemousin (“Allebome”), 15 lodges, 50 warriors, 200 souls (head of the N. fork of the Cheyenne). The Staetan are Tabeau’s Squihitanes, of the same language as the Arapaho, and the Nemousin his Nimoussines, the Nawathinehena (Fowler, “Arapaho”, Handbook 13 (2001), pp. 860–61)',basis='souls',loc='stated',at=(43.3,-104.4),r=150,src=CLARK,kind='primary'),
 dict(g='ara',y=1805.0,pop=None,basis='',loc='stated',kind='primary',raw='Clark: the Staetan (“Kites”), an Arapaho group, at the head of the Cheyenne, often with the Kanenavich (part; kept off the division track)',at=(43.6,-104.2),r=120,src=CLARK+'; identification Fowler, “Arapaho”, Handbook 13 (2001), p. 860',whole=False),
 dict(g='ara',y=1805.0,pop=None,basis='',loc='stated',kind='primary',raw='Clark: the Nemousin (“Allebome”), the Nawathinehena division of the Arapaho, at the head of the north fork of the Cheyenne (part; kept off the division track)',at=(44.6,-104.6),r=80,src=CLARK+'; identification Fowler, “Arapaho”, Handbook 13 (2001), p. 861',whole=False),
 dict(g='kap',y=1805,pop=300,raw='Cataka: 25 lodges; 75 warriors; souls 400 [or] 300; between the heads of the N. and S. forks of the Cheyenne',basis='souls',loc='stated',at=(44.3,-104.5),r=80,src=CLARK,kind='primary'),
 dict(g='u_dot',y=1805,pop=120,raw='Dotame: 10 lodges; 30 warriors; souls 200 [or] 120; heads of the Cheyenne',basis='souls',loc='stated',at=(44.3,-104.2),r=80,src=CLARK,kind='primary'),
 dict(g='u_cas',y=1805,pop=5000,raw='Castahana (“Gens des Vache”): 500 lodges; 1,300 warriors; souls 7,000 [or] 5,000; Bighorn R. and heads of the Loup',basis='souls',loc='stated',at=(43.8,-107.0),r=200,src=CLARK,kind='primary'),
 dict(g='cwr',y=1805,pop=3500,raw='Kee-hât-sâ, Crow (“Ravin nation”): 350 lodges; 900 warriors; souls 5,000 [or] 3,500; Yellowstone about the mouth of the Bighorn',basis='souls',loc='stated',at=P['bighorn_mouth'],r=100,src=CLARK,kind='primary'),
 dict(g='cwm',y=1805,pop=2300,raw='Paunch Indians (Allakaweah): 300 lodges; 800 warriors; souls 4,000 [or] 2,300; near the Rockies, heads of the Bighorn',basis='souls',loc='stated',at=(44.8,-108.2),r=150,src=CLARK,kind='primary'),
 dict(g='asn',y=1805,pop=1600,raw='Assiniboine band: 200 lodges; 450 warriors; souls 2,000 [or] 1,600; plains between the Missouri and the Saskatchewan',basis='souls',loc='stated',at=(50.6,-106.0),r=250,src=CLARK,kind='primary'),
 dict(g='ass',y=1805,pop=750,raw='Assiniboine band: 100 lodges; 200 warriors; souls 1,200 [or] 750; Mouse (Souris) R.',basis='souls',loc='stated',at=(48.7,-101.0),r=80,src=CLARK,kind='primary',part=True),
 dict(g='ass',y=1805,pop=850,raw='Assiniboine band: 100 lodges; 250 warriors; souls 1,200 [or] 850; heads of the Mouse & Qu’Appelle, Little Muddy (White Earth) R.',basis='souls',loc='stated',at=(49.3,-102.8),r=120,src=CLARK,kind='primary',part=True),
 dict(g='cre',y=1805,pop=1000,raw='Knistanoes (Cree): 150 lodges; 300 warriors; 1,000 souls; head of the Assiniboine & toward the Saskatchewan',basis='souls',loc='stated',at=(51.0,-102.5),r=150,src=CLARK,kind='primary'),
 dict(g='gv',y=1805,pop=2500,raw='Fall Indians: 260 lodges; 660 warriors; 2,500 souls; head of the S. fork of the Saskatchewan',basis='souls',loc='stated',at=(50.5,-110.5),r=200,src=CLARK,kind='primary'),
 dict(g='ojb',y=1805,pop=350,raw='Chippewa on the Red R. (Pembina): 100 warriors; souls 800 [or] 350',basis='souls',loc='stated',at=P['pembina'],r=40,src=CLARK,kind='primary'),
 dict(g='wic',y=1805,pop=2000,raw='Pania Pickey: 500 warriors; 2,000 souls; head of the Red R.',basis='souls',loc='stated',at=P['spanish_fort'],r=150,src=CLARK,kind='primary'),
 # ---- Mackenzie, c. 1789 (as quoted by Hayden) ----
 dict(g='pik',y=1789,pop=5400,raw='“On the head waters of the South Branch [Saskatchewan] are the Picaneux, to the number of twelve to fifteen hundred men”',basis='warriors × 4',loc='stated',at=(50.8,-113.6),r=150,src='Mackenzie, General History of the Fur Trade (1801), quoted in '+HAYDEN,kind='primary'),
 dict(g='kai',y=1789,pop=1000,raw='“Next to them, on the same water, are the Blood Indians… fifty tents, or two hundred and fifty men”',basis='warriors × 4',loc='stated',at=(50.3,-112.3),r=150,src='Mackenzie (1801), quoted in '+HAYDEN,kind='primary'),
 dict(g='sik',y=1789,pop=3200,raw='“From them downwards extend the Blackfeet Indians… their number may be eight hundred men”',basis='warriors × 4',loc='stated',at=(50.9,-111.0),r=150,src='Mackenzie (1801), quoted in '+HAYDEN,kind='primary'),
 dict(g='gv',y=1789,pop=2400,raw='“Next to them, and who extend to the confluence of the South and North Branch, are the Fall or Big-bellied Indians… about six hundred warriors”',basis='warriors × 4',loc='stated',at=(52.4,-107.5),r=200,src='Mackenzie (1801), quoted in '+HAYDEN,kind='primary'),
 # ---- Denig (via Hayden) on the Teton etc., 1833: lodges × 5 (multiplier stated) ----
 dict(g='bru',y=1833,pop=2500,raw='Brulés, 500 lodges (avg. five souls per lodge)',basis='lodges × 5 (stated)',loc='inferred',at=P['whiteR'],r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='ogl',y=1833,pop=1500,raw='Oglalas, 300 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(44.2,-101.8),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='min',y=1833,pop=1300,raw='Minneconjou, 260 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(44.7,-101.6),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='sih',y=1833,pop=1100,raw='Sihasapa (Blackfeet Dakota), 220 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(45.5,-101.3),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='twk',y=1833,pop=500,raw='Two Kettles, 100 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(44.5,-100.6),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='hnk',y=1833,pop=750,raw='Hunkpapas, 150 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(45.9,-101.0),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='sna',y=1833,pop=500,raw='Sans Arcs, 100 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(45.1,-102.2),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='ynk',y=1833,pop=1500,raw='Lower Yanktons, 300 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(43.4,-97.5),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 dict(g='yku',y=1833,pop=1250,raw='Pabaksa (Cut-Heads), 250 lodges',basis='lodges × 5 (stated)',loc='inferred',at=(46.6,-98.7),r=150,src=HAYDEN+' (Denig’s count)',kind='primary'),
 # ---- Hodge on Teton divisions ----
 dict(g='min',y=1850,pop=2150,raw='Culbertson: 270 lodges, “between 2,100 and 2,200 people”; roamed the Black Hills & headwaters of the Cheyenne, Cherry Cr. to Grand R.',basis='souls',loc='stated',at=(44.8,-102.5),r=150,src=HODGE+', “Miniconjou”',kind='primary'),
 dict(g='min',y=1856,pop=1600,raw='Warren: 200 lodges and 1,600 souls',basis='souls',loc='inferred',at=(44.8,-102.5),r=150,src=HODGE+', “Miniconjou”',kind='primary'),
 dict(g='min',y=1863,pop=1280,raw='Indian Affairs Report for 1863 gives 1,280',basis='souls',loc='inferred',at=(44.8,-102.0),r=200,src=HODGE+', “Miniconjou”',kind='primary'),
 dict(g='hnk',y=1850,pop=2560,raw='Culbertson: range on the Cheyenne, Moreau, Grand, and Cannonball rivers; 320 tipis',basis='tipis × 8 (Warren’s implied ratio)',loc='stated',at=(45.7,-101.2),r=150,src=HODGE+', “Hunkpapa”',kind='primary'),
 dict(g='hnk',y=1855,pop=2920,raw='Warren: on the Missouri near the mouth of the Moreau, roaming from the Big Cheyenne to the Yellowstone; 2,920 souls',basis='souls',loc='stated',at=(45.6,-102.3),r=250,src=HODGE+', “Hunkpapa”',kind='primary'),
 dict(g=['bru','ogl','min','hnk','sih','sna','twk'],y=1890,pop=16426,raw='“in 1890 the total Teton population was 16,426”',basis='souls',loc='inferred',at=(44.2,-101.5),r=250,src=HODGE+', “Teton”',kind='primary'),
 dict(g='ykl',y=1866,pop=2100,raw='Hunkpatina “estimated at 2,100” in 1866',basis='souls',loc='inferred',at=(44.6,-99.6),r=200,src=HODGE,kind='primary'),
 dict(g='ykl',y=1905,pop=1009,raw='“chiefly on Crow Creek res., S. Dak., where they numbered 1,009 in 1905”',basis='souls',loc='stated',at=P['crow_creek'],r=20,src=HODGE,kind='primary'),
 # ---- Denig on the Assiniboine ----
 dict(g=['ass','asn'],y=1760,pop=9000,raw='At separation from the Sioux (traditional date c. 1760) “at least 1,500 lodges, averaging six souls to a lodge”; then about the head of the Minnesota & Des Moines, Devils Lake, Lac qui Parle',basis='lodges × 6 (stated)',loc='stated',at=(46.5,-97.5),r=250,src=DENIG+'; Hodge’s editor notes the date is far too late',kind='secondary'),
 dict(g='ass',y=1837,pop=6600,raw='“Still numbered 1,000 to 1,200 lodges, trading on the Missouri until the year 1838”',basis='lodges × 6',loc='stated',at=(48.4,-104.5),r=200,src=DENIG,kind='primary'),
 dict(g='ass',y=1839,pop=2400,raw='Smallpox of 1838 “reduced their numbers to less than 400 lodges”',basis='lodges × 6',loc='stated',at=(48.4,-104.5),r=200,src=DENIG,kind='primary'),
 dict(g='ass',y=1854,pop=450,raw='Gens du Gauche, 100 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.3,-104.6),r=100,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=270,raw='Gens du Nord, 60 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.9,-105.6),r=100,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=990,raw='Gens des Canots, 220 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.5,-103.3),r=100,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=135,raw='Gens des Canots, 30 more lodges trading near the mouth of the Pembina',basis='lodges × 4.5 (stated)',loc='stated',at=P['pembina'],r=40,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=270,raw='Gens des Filles, 60 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.7,-106.7),r=100,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=225,raw='Gens des Roches, 50 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.5,-107.6),r=100,src=DENIG,kind='primary',part=True),
 dict(g='ass',y=1854,pop=135,raw='Bas Rouge, 30 lodges',basis='lodges × 4.5 (stated)',loc='inferred',at=(48.2,-105.2),r=100,src=DENIG,kind='primary',part=True),
 dict(g='asn',y=1854,pop=1240,raw='Northern Assiniboine, “250 or 300 lodges,” from the W. banks of the Saskatchewan, Assiniboine & Red rivers west to the Woody Mountains',basis='lodges × 4.5',loc='stated',at=(50.5,-105.5),r=250,src=DENIG,kind='primary'),
 dict(g=['ass','asn'],y=1890,pop=3008,raw='“In 1890 they numbered 3,008”',basis='souls',loc='inferred',at=(49.0,-105.5),r=300,src=HODGE+', “Assiniboin”',kind='primary'),
 dict(g=['ass','asn'],y=1904,pop=2600,raw='“in 1904, 2,600” (US: 699 at Ft Belknap, 535 at Ft Peck)',basis='souls',loc='inferred',at=(49.0,-105.5),r=300,src=HODGE+', “Assiniboin”',kind='primary'),
 # ---- Cree, 1856 (Denig via Hayden): lodges × 4 (stated) ----
 dict(g=['cre','crw','crs'],y=1856,pop=4200,raw='“About ten or eleven hundred lodges, averaging four souls to a lodge”',basis='lodges × 4 (stated)',loc='inferred',at=(51.0,-106.0),r=350,src=HAYDEN+' (Denig)',kind='primary'),
 dict(g='cre',y=1856,pop=400,raw='Co-kah (“Eyes Open”) band, 100 lodges and upwards, near Lac Qu’Appelle',basis='lodges × 4 (stated)',loc='stated',at=P['quappelle'],r=50,src=HAYDEN+' (Denig)',kind='primary',part=True,whole=False),
 dict(g='crw',y=1856,pop=540,raw='Four small bands, 130–140 lodges, about Fort de Prairie',basis='lodges × 4 (stated)',loc='stated',at=(53.4,-113.0),r=100,src=HAYDEN+' (Denig)',kind='primary'),
 dict(g='crs',y=1856,pop=1200,raw='Le Sonnant’s band, about 300 lodges, along the Montagnes des Bois (Wood Mountain)',basis='lodges × 4 (stated)',loc='stated',at=P['wood_mt'],r=80,src=HAYDEN+' (Denig)',kind='primary',part=True),
 dict(g='crs',y=1856,pop=1400,raw='La Lance’s band, 350 lodges, in the Cypress and Prickly Pear mountains',basis='lodges × 4 (stated)',loc='stated',at=P['cypress'],r=100,src=HAYDEN+' (Denig)',kind='primary',part=True),
 # ---- Blackfoot ----
 dict(g='kai',y=1853,pop=2450,raw='Bloods, 350 lodges, 2,450 persons, 875 warriors',basis='souls',loc='inferred',at=(49.6,-112.8),r=150,src='Doty in Stevens, Pacific Railroad Reports vol. 1, as given by '+HAYDEN,kind='primary'),
 dict(g='sik',y=1853,pop=1750,raw='Blackfeet, 250 lodges, 1,750 persons',basis='souls',loc='inferred',at=(50.8,-112.5),r=150,src='Doty in Stevens, Pacific Railroad Reports vol. 1, as given by '+HAYDEN,kind='primary'),
 dict(g='pik',y=1853,pop=2520,raw='Piegans, 360 lodges, 2,520 persons, 900 warriors',basis='souls',loc='inferred',at=(48.3,-111.6),r=150,src='Doty in Stevens, Pacific Railroad Reports vol. 1, as given by '+HAYDEN,kind='primary'),
 dict(g='sik',y=1858,pop=1200,raw='Blackfeet: 150 lodges; 1,200 total',basis='souls',loc='inferred',at=(50.8,-112.5),r=150,src='Report of the Commissioner of Indian Affairs, 1858, as given by '+HAYDEN,kind='primary'),
 dict(g='kai',y=1858,pop=2400,raw='Bloods: 300 lodges; 2,400 total',basis='souls',loc='inferred',at=(49.6,-112.8),r=150,src='Report of the Commissioner of Indian Affairs, 1858, as given by '+HAYDEN,kind='primary'),
 dict(g='pik',y=1858,pop=3700,raw='Piegans: 460 lodges; 3,700 total',basis='souls',loc='inferred',at=(48.3,-111.6),r=150,src='Report of the Commissioner of Indian Affairs, 1858, as given by '+HAYDEN,kind='primary'),
 # ---- Gros Ventre (Atsina) ----
 dict(g='gv',y=1833,pop=1000,raw='Prince Maximilian (1832–33): about 200 lodges, 400 to 500 warriors',basis='lodges × 5 (Hayden’s census ratio)',loc='inferred',at=(47.9,-110.4),r=150,src=HAYDEN,kind='primary'),
 dict(g='gv',y=1853,pop=2520,raw='Gov. Stevens: 360 lodges, 900 warriors, total population 2,520',basis='souls',loc='inferred',at=P['milk_mid'],r=150,src=HAYDEN,kind='primary'),
 dict(g='gv',y=1904,pop=535,raw='Atsina at Ft Belknap res., Mont., “in 1904 they numbered 535”',basis='souls',loc='stated',at=P['ft_belknap'],r=20,src=HODGE+', “Atsina”',kind='primary'),
 # ---- Arapaho & Cheyenne ----
 dict(g='arn',y=1860,pop=900,raw='Na-ka-si’-nin (“People of the Sage”), 180 lodges; sources of the S. Platte & Pike’s Peak north to the Red Buttes; wintered 1859–60 on Powder R. (the range is a general one; the place of the count is taken as unstated, since the dated winter camp on Powder River is in the record)',basis='lodges × 5 (assumed)',loc='inferred',at=(42.0,-105.3),r=250,src=HAYDEN,kind='primary'),
 dict(g='ars',y=1860,pop=1000,raw='Na-wuth’-i-ni-han, 200 lodges, range along the Arkansas and its tributaries',basis='lodges × 5 (assumed)',loc='stated',at=(38.2,-101.5),r=250,src=HAYDEN,kind='primary'),
 dict(g='ars',y=1904,pop=889,raw='Southern Arapaho (Oklahoma), 889 in 1904',basis='souls',loc='inferred',at=P['darlington'],r=60,src=HODGE+', “Arapaho”',kind='primary'),
 dict(g='arn',y=1904,pop=859,raw='Northern Arapaho (Wind River res., Wyo.), 859 in 1904',basis='souls',loc='stated',at=P['wind_res'],r=30,src=HODGE+', “Arapaho”',kind='primary'),
 dict(g='chy',y=1822,pop=3250,raw='Morse (1822): “this tribe, of 3250 souls, dwell and hunt on the river of this name… a little above the Great Bend”',basis='souls',loc='stated',at=(44.5,-101.8),r=200,src='Morse, Report to the Secretary of War (1822), quoted in '+HAYDEN,kind='primary'),
 dict(g='chs',y=1904,pop=1903,raw='Southern Cheyenne, 1,903 in 1904',basis='souls',loc='inferred',at=P['darlington'],r=60,src=HODGE+', “Cheyenne”',kind='primary'),
 dict(g='chn',y=1904,pop=1409,raw='Northern Cheyenne, 1,409 in 1904',basis='souls',loc='inferred',at=P['lame_deer'],r=40,src=HODGE+', “Cheyenne”',kind='primary'),
 # ---- Crow ----
 dict(g=['cwm','cwr'],y=1855,pop=3220,raw='“Formerly numbered about eight hundred lodges… now reduced to four hundred and sixty lodges”',basis='lodges × 7 (assumed)',loc='inferred',at=(45.3,-107.8),r=250,src=HAYDEN+' (Denig)',kind='primary'),
 dict(g='cwm',y=1855,pop=1400,raw='Two-face’s band, “about two hundred lodges,” range through the Wind River mountain region',basis='lodges × 7 (assumed)',loc='stated',at=(43.3,-108.9),r=120,src=HAYDEN+' (Denig)',kind='primary',part=True),
 dict(g='cwr',y=1855,pop=None,raw='Bear’s Head’s band wanders the Yellowstone valley, sometimes wintering with the Assiniboine near Fort Union',basis='',loc='stated',at=(47.0,-106.0),r=200,src=HAYDEN+' (Denig)',kind='primary'),
 dict(g='cwm',y=1871,pop=2700,raw='“The Mountain Crows numbered 2,700 in 1871” (Pease)',basis='souls',loc='inferred',at=(45.68,-110.37),r=60,src=HODGE+', “Crows”',kind='primary'),
 dict(g='cwr',y=1871,pop=1400,raw='“…and the River Crows 1,400” (Pease)',basis='souls',loc='inferred',at=(48.3,-108.0),r=120,src=HODGE+', “Crows”',kind='primary'),
 # ---- Village tribes ----
 dict(g='man',y=1837,pop=1600,raw='“in 1837 1,600 souls”, before the smallpox',basis='souls',loc='inferred',at=P['ft_clark'],r=15,src=HODGE+', “Mandan”',kind='primary'),
 dict(g='hid',y=1837,pop=600,raw='“When living with the Mandans at Fort Clarke they numbered about one hundred and twenty lodges, averaging five souls”',basis='lodges × 5 (stated)',loc='stated',at=(47.3,-101.35),r=15,src=HAYDEN,kind='primary'),
 dict(g='hid',y=1838,pop=200,raw='After the smallpox “reduced to forty lodges”; then moved “sixty miles above on the opposite side of the river”',basis='lodges × 5 (stated)',loc='stated',at=(47.3,-101.35),r=15,src=HAYDEN,kind='primary'),
 dict(g='ari',y=1871,pop=1650,raw='“In 1871 the tribe numbered 1,650”',basis='souls',loc='inferred',at=P['like_fishhook'],r=15,src=HODGE+', “Arikara”',kind='primary'),
 dict(g='ari',y=1888,pop=500,raw='“by 1888 they were reduced to 500”',basis='souls',loc='inferred',at=P['like_fishhook'],r=30,src=HODGE+', “Arikara”',kind='primary'),
 dict(g='ari',y=1904,pop=380,raw='“the census of 1904 gives the population as 380”',basis='souls',loc='inferred',at=(47.6,-102.0),r=30,src=HODGE+', “Arikara”',kind='primary'),
 dict(g=['pwc','pwk','pws'],y=1820,pop=10000,raw='Long’s expedition, 1820: Grand Pawnees, Republicans, and Loups, all on the Platte and its branches, “numbered about ten thousand souls”',basis='souls',loc='stated',at=(41.35,-97.6),r=60,src='Long expedition (1823), as given by '+HAYDEN,kind='primary'),
 # ---- Comanche ----
 dict(g=['cyj','cyy','cyk'],y=1700,pop=7000,raw='Mooney estimated “there must have been 7,000 Comanche about 1690”',basis='souls',loc='inferred',at=(39.5,-104.5),r=300,src='Mooney (1928), as given in Swanton, Indian Tribes of North America',kind='secondary'),
 dict(g=['cyj','cyy','cyk','cyp'],y=1750,pop=12500,raw='“by 1750 their population seems to have exceeded ten thousand and was probably approaching fifteen thousand”; “numbering between ten and fifteen thousand at midcentury”',basis='souls',loc='inferred',at=(36.5,-101.5),r=400,src='Hämäläinen, The Comanche Empire (2008), pp. 66, 102',kind='secondary'),
 dict(g=['cyj','cyy','cyk','cyp'],y=1774.51,pop=16000,raw='3 July 1774: “The Naytane chief… came with the whole nation”, four bands assembled at the Taovaya village, one of them the Yamparika; Gaignard was told they “comprise fully four thousand warriors” (Hämäläinen dates it 1773 and derives about 16,000; the figure is for the four eastern bands, here applied to the whole nation)',basis='warriors × 4',loc='inferred',at=(35.0,-100.5),r=400,src=BOLTON('vol. 2, pp. 93–94 (pdf 99–100), Gaignard’s journal')+'; Hämäläinen, The Comanche Empire (2008), p. 102',kind='primary'),
 dict(g=['cyj','cyy','cyk','cyp'],y=1780,pop=20000,raw='Estimates of Comanche numbers in 1780, when most numerous, “are usually around 20,000”',basis='souls',loc='inferred',at=(34.8,-100.5),r=400,src='Wikipedia, “Comanche history” (summary of the literature)',kind='secondary'),
 dict(g=['cyj','cyy','cyk','cyp'],y=1781,pop=40000,raw='Hämäläinen’s high reckoning: a 1785 account gives the eastern Comanches 2,000 fighting men after losing two-thirds to smallpox, so “the total Comanche population in the early 1780s reached or exceeded forty thousand”',basis='souls',loc='inferred',at=(34.8,-100.5),r=400,src='Hämäläinen, The Comanche Empire (2008), pp. 102–3',kind='secondary'),
 dict(g=['cyy','cyk','cyp'],y=1819,pop=11000,raw='Written in 1847 “from the recollection of near thirty years”, his information “entirely too limited and imperfect” (Kavanagh, Comanche Political History, p. 354): “In 1819 the three bands consisted of 10,000 to 12,000 souls… 2000 to 2500 warriors” (Comanche, Yamparack, Tenawa)',basis='souls',loc='inferred',at=(33.0,-99.5),r=400,src=TIPV3('doc. No. 78 (Burnet to Schoolcraft, 1847)')+'; also Kavanagh, “Comanche”, Handbook of North American Indians 13 (2001), p. 901',kind='primary'),
 dict(g='cyn',y=1847,pop=1750,raw='Nokoni “said to number 1,750, in 250 lodges, evidently a gross exaggeration”',basis='souls',loc='inferred',at=(34.3,-99.9),r=200,src=HODGE+', “Detsanayuka”',kind='primary'),
 dict(g='cyn',y=1869,pop=312,raw='“in 1869 their number was 312”',basis='souls',loc='inferred',at=P['ft_sill'],r=60,src=HODGE+', “Detsanayuka”',kind='primary',whole=False),
 dict(g='cyn',y=1872,pop=250,raw='“in 1872 they were reported at 250”',basis='souls',loc='inferred',at=P['ft_sill'],r=60,src=HODGE+', “Detsanayuka”',kind='primary',whole=False),
 dict(g='cyy',y=1869,pop=356,raw='Ditsakana (Yamparika) “estimated to number 356 in 1869”',basis='souls',loc='inferred',at=P['ft_sill'],r=60,src=HODGE+', “Ditsakana”',kind='primary',whole=False),
 dict(g='cyy',y=1872,pop=200,raw='“and 200 in 1872”',basis='souls',loc='inferred',at=P['ft_sill'],r=60,src=HODGE+', “Ditsakana”',kind='primary',whole=False),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1904,pop=1400,raw='“They numbered 1,400 in 1904, attached to the Kiowa agency, Okla.”',basis='souls',loc='inferred',at=(34.7,-98.5),r=60,src=HODGE+', “Comanche”',kind='primary'),
 dict(g='lip',y=1805,pop=3000,raw='“In 1805 the Lipan were reported to be divided into 3 bands, numbering 300, 350, and 100 men”',basis='warriors × 4',loc='inferred',at=(29.3,-100.2),r=250,src=HODGE+', “Lipan”',kind='primary'),
]

# ---------------------------------------------------------------------------------------------
# GUESS keyframes: (year, place-or-(lat,lon)-or-None, pop-or-None, note)
# None place/pop = defer to documented observation / interpolation at that year.
def g(*a): return a
GUESS = {
 # ---------------- Lakota ----------------
 'bru':[g(1700,(44.7,-96.9),1200,'Prairie Coteau east of the Missouri'),g(1740,(44.3,-98.5),1500,''),g(1765,(44.0,-99.4),1800,'Reaching the Missouri'),
        g(1780,None,2000,''),g(1782,None,1500,'1780–81 smallpox'),g(1805,None,1400,'Clark’s undeducted figure (1,400) used'),g(1820,(43.6,-100.4),2300,''),
        g(1845,(42.2,-101.2),3500,'Part of the Brulé shifting toward the Platte'),g(1855.7,(41.9,-101.6),3200,'Ash Hollow (Blue Water), Sept. 1855: Little Thunder’s band (see bands)'),
        g(1865,(42.2,-100.5),3800,''),g(1870.0,(43.1,-99.6),4000,'Whetstone agency on the Missouri, 1869–71 (after the August 1868 hunt south of the Platte)'),g(1874,(42.8,-102.8),4500,'Spotted Tail agency'),
        g(1878.9,P['rosebud'],5000,'Rosebud agency'),g(1890,P['rosebud'],5400,''),g(1905,P['rosebud'],5200,'')],
 'ogl':[g(1700,(45.0,-97.7),800,''),g(1740,(44.6,-98.9),1000,''),g(1765,(44.5,-100.2),1200,''),g(1776,(44.1,-102.6),1300,'Winter counts date the Lakota discovery of the Black Hills to about 1775–76'),
        g(1780,None,1400,''),g(1782,None,1000,'1780–81 smallpox'),g(1805,None,1200,'Clark’s 360–600 judged an undercount'),g(1825.5,P['badR_mouth'],1500,'Treaty at the Bad River, 1825'),
        g(1835,P['laramie'],1700,'Move to the Platte with Fort William trade'),g(1850,(41.8,-102.7),2500,''),g(1860,(42.4,-104.0),3000,''),
        g(1866.5,(44.3,-106.4),3500,'Powder River country (Red Cloud’s war)'),g(1871.5,(42.2,-104.4),4000,'Red Cloud agency on the Platte'),
        g(1873.6,(42.68,-103.45),5000,'Red Cloud agency on the White River'),g(1878.9,P['pine_ridge'],6000,'Pine Ridge agency'),g(1890.98,(43.14,-102.36),5000,'Wounded Knee, Dec. 1890'),g(1905,P['pine_ridge'],6600,'')],
 'min':[g(1700,(45.6,-97.8),700,''),g(1760,(45.3,-99.8),900,''),g(1782,None,800,'1780–81 smallpox'),g(1805,None,1200,'Clark’s undeducted figure'),
        g(1820,(44.9,-101.6),1500,''),g(1870,P['chyR_agency'],1700,'Cheyenne River agency'),g(1876.47,P['lbh'],1500,'Little Bighorn camp, June 1876'),
        g(1877.5,P['chyR_agency'],1600,''),g(1890.95,(44.95,-101.9),1500,'Cherry Creek / Big Foot’s band'),g(1905,P['chyR_agency'],1400,'')],
 'hnk':[g(1700,(46.1,-98.2),500,''),g(1760,(45.9,-99.6),700,''),g(1790,(45.9,-100.4),800,''),g(1805,(45.95,-100.6),900,'Share of Clark’s “Saone” (our split)'),g(1833,None,1500,'Denig’s 150 lodges looks low beside the 1850s counts'),
        g(1866,(46.6,-104.4),3000,'Yellowstone & Powder country'),g(1876.47,P['lbh'],2000,'Little Bighorn camp, June 1876'),
        g(1877.5,(46.0,-101.3),1800,'Most Hunkpapa at the Grand River agency; Sitting Bull’s following in Canada (see bands)'),
        g(1882,P['standing_rock'],1700,'Standing Rock'),g(1905,P['standing_rock'],1600,'')],
 'sih':[g(1700,(46.0,-98.4),400,''),g(1760,(45.8,-99.7),600,''),g(1805,(45.9,-100.5),700,'Share of Clark’s “Saone”'),g(1855,(45.5,-101.5),1500,''),
        g(1876,(45.5,-101.0),1200,''),g(1880,(45.6,-100.8),1100,'Standing Rock & Cheyenne River'),g(1905,(45.6,-100.8),1000,'')],
 'sna':[g(1700,(45.8,-98.5),400,''),g(1760,(45.6,-99.9),500,''),g(1805,(45.9,-100.7),500,'Share of Clark’s “Saone”'),g(1855,(45.0,-102.4),1000,''),
        g(1876.47,P['lbh'],800,'Little Bighorn camp, June 1876'),g(1878,P['chyR_agency'],800,''),g(1905,P['chyR_agency'],700,'')],
 'twk':[g(1700,(45.4,-98.0),300,''),g(1760,(45.0,-99.6),400,''),g(1805,(45.8,-100.4),400,'Share of Clark’s “Saone”'),g(1855,(44.6,-100.6),900,''),
        g(1870,P['chyR_agency'],800,''),g(1905,P['chyR_agency'],700,'')],
 # ---------------- Yankton, Yanktonai, Dakota ----------------
 'ynk':[g(1700,(44.4,-95.9),1500,'Pipestone quarry country'),g(1760,(43.6,-96.6),2000,''),g(1782,None,1600,''),g(1805,None,1800,'Clark’s band is a partial count'),
        g(1859.5,P['yankton_ag'],2200,'Yankton agency (1858 treaty)'),g(1880,P['yankton_ag'],2000,''),g(1905,P['yankton_ag'],1700,'')],
 'yku':[g(1700,(46.6,-95.6),1500,''),g(1760,(47.0,-97.9),2000,''),g(1805,(46.6,-98.8),1700,'Share of Clark’s “Yanktons of the North”'),
        g(1850,(47.2,-99.2),2500,''),g(1863.7,(46.17,-98.86),2300,'Whitestone Hill, Sept. 1863'),g(1866,(47.4,-101.2),2200,''),
        g(1873,P['standing_rock'],1800,'Standing Rock (some to Fort Peck & Devils Lake)'),g(1905,P['standing_rock'],1600,'')],
 'ykl':[g(1700,(46.0,-96.1),1000,''),g(1760,(46.1,-97.6),1200,''),g(1805,(46.2,-98.3),1200,'Share of Clark’s “Yanktons of the North”'),
        g(1840,(45.8,-99.4),1800,''),g(1863,P['crow_creek'],2000,'Crow Creek agency')],
 'mde':[g(1700,P['mille_lacs'],2500,'Mille Lacs villages'),g(1740,(45.3,-93.4),2200,'Moving south after wars with the Ojibwe'),g(1760,P['minn_mouth'],2000,''),
        g(1853.5,(44.53,-94.98),2300,'Lower Sioux agency'),g(1862.7,(44.53,-94.98),2200,'U.S.–Dakota War, 1862'),g(1863.4,P['crow_creek'],1300,'Exile to Crow Creek'),
        g(1866.5,P['santee'],1000,'Santee reservation, Neb.'),g(1905,P['santee'],1000,'')],
 'wpk':[g(1700,(45.4,-93.5),600,''),g(1760,(44.3,-94.0),600,''),g(1853.5,(44.4,-94.6),600,''),g(1863.4,P['crow_creek'],300,''),g(1866.5,(42.85,-97.9),300,'With the Mdewakanton at Santee'),g(1905,(42.85,-97.9),250,'')],
 'wpt':[g(1700,(45.8,-94.2),1000,''),g(1760,(45.0,-94.3),1000,''),g(1850,(44.9,-95.9),1200,'Lac qui Parle'),g(1863,P['devils_lake'],1000,'Flight to Devils Lake & Lake Traverse'),
        g(1867.5,P['sisseton'],1000,'Lake Traverse reservation'),g(1905,P['sisseton'],1000,'')],
 'sis':[g(1700,(46.6,-95.4),1500,''),g(1760,(45.6,-96.7),1800,''),g(1805,None,1500,'Clark’s 800 judged low'),g(1850,(45.9,-97.3),2500,''),
        g(1863,(47.6,-98.4),2000,''),g(1867.5,(45.75,-97.2),1700,'Lake Traverse & Devils Lake reservations'),g(1905,(45.75,-97.2),1600,'')],
 'ass':[g(1700,(50.0,-98.6),5000,'Lower Assiniboine & Red rivers'),g(1740,(49.8,-100.5),6000,''),g(1780,(49.5,-101.0),6000,''),g(1782,None,4000,'1780–81 smallpox'),
        g(1805,(48.9,-101.8),3500,'Migration toward the Missouri under way (Denig)'),g(1830,(48.5,-103.8),6000,''),
        g(1871.5,P['ft_peck'],1800,'Fort Peck agency'),g(1890,(48.3,-106.5),1700,'Fort Peck & Fort Belknap'),g(1905,(48.3,-106.5),1250,'')],
 'asn':[g(1700,(52.6,-104.5),4000,'Saskatchewan parkland'),g(1740,(52.6,-106.5),4500,''),g(1780,None,4500,''),g(1782,None,3000,'1780–81 smallpox'),
        g(1805,None,2500,''),g(1838,(50.8,-106.5),2500,''),g(1877,(50.5,-104.5),1400,'Treaty 4 reserves'),g(1905,(50.6,-103.9),1200,'')],
 # ---------------- Cree, Ojibwe ----------------
 'cre':[g(1700,(52.5,-100.5),2000,'Swan River / Lake Winnipegosis edge'),g(1760,(51.5,-102.0),2500,''),g(1782,None,1500,'1780–81 smallpox'),
        g(1805,None,1800,''),g(1856,P['quappelle'],1700,'Our share of Denig’s 1,000–1,100 lodges'),g(1874.7,P['quappelle'],1700,'Treaty 4 at Fort Qu’Appelle'),g(1905,(50.9,-103.6),1500,'')],
 'crw':[g(1700,(54.0,-110.0),1000,'Woodland–parkland edge'),g(1800,(53.3,-111.5),1200,''),g(1876.6,(53.6,-112.5),1100,'Treaty 6'),g(1905,(53.4,-112.8),1000,'')],
 'crs':[g(1790,(51.0,-104.5),800,'Cree moving onto the open plains'),g(1830,(50.4,-107.0),1500,''),g(1870,(49.6,-108.5),2800,''),
        g(1880,P['cypress'],2500,'The last herds draw the Cree to the Cypress Hills'),g(1881.0,(48.6,-108.4),None,'Following the last herds onto the Milk River in Montana, 1879–81 (Dempsey, Big Bear, 1984; recalled)'),g(1882.9,(49.57,-109.88),None,'Big Bear signs his adhesion to Treaty 6 at Fort Walsh, Dec. 1882 (Dempsey; recalled)'),g(1883.6,(52.6,-108.6),2000,'Fort Walsh closed and rations cut; most bands sent north to reserves, 1883'),
        g(1885.3,(52.9,-108.9),1800,'1885 resistance (see Big Bear’s and Poundmaker’s bands)'),g(1890,P['battleford'],1800,''),g(1905,P['battleford'],1700,'')],
 'ojb':[g(1780,(49.6,-97.3),300,'Red River'),g(1820,(48.95,-99.0),800,''),g(1850,P['turtle_mt'],1500,''),g(1882,P['turtle_mt'],1600,'Turtle Mountain reservation'),g(1905,P['turtle_mt'],1600,'')],
 # ---------------- Blackfoot, Gros Ventre ----------------
 'sik':[g(1700,(52.6,-110.0),2500,'Eagle Hills / Battle River'),g(1740,(52.0,-111.5),3000,'Horses arriving'),g(1780,(51.2,-112.0),3500,''),g(1782,None,2400,'1781 smallpox'),
        g(1805,(51.0,-112.0),3000,''),g(1830,(50.8,-112.5),3500,''),g(1837.5,None,2000,'1837 smallpox'),g(1870,None,1800,'1869–70 smallpox'),
        g(1877.7,(50.73,-112.95),2100,'Treaty 7 at Blackfoot Crossing'),g(1880.0,(47.9,-108.7),None,'Crowfoot follows the last herds south into Montana, 1879–81 (Dempsey, Crowfoot, 1972; recalled)'),g(1881.6,(50.73,-112.95),None,'Back at Blackfoot Crossing, summer 1881 (Dempsey; recalled)'),g(1883,P['siksika_res'],2000,''),g(1905,P['siksika_res'],1100,'')],
 'kai':[g(1700,(52.0,-111.0),1000,''),g(1805,(50.0,-112.5),1800,''),g(1830,(49.6,-112.8),2500,''),g(1837.5,None,1700,'1837 smallpox'),
        g(1870,None,2000,''),g(1880,P['blood_res'],2400,'Blood reserve'),g(1905,P['blood_res'],1300,'')],
 'pik':[g(1700,(51.5,-112.5),3000,''),g(1805,(50.3,-113.5),5000,''),g(1830,(48.8,-112.6),6000,''),g(1837.5,None,3500,'1837 smallpox'),
        g(1870.05,(48.3,-111.9),2800,'Marias Massacre, Jan. 1870'),g(1880,(48.4,-112.5),2000,'Blackfeet agency, Badger Creek'),g(1885,None,1800,'Starvation winter 1883–84'),g(1905,P['blackfeet_ag'],2000,'')],
 'gv':[g(1700,(52.6,-106.8),3000,'Saskatchewan forks'),g(1782,None,2000,'1781 smallpox'),g(1795,(51.5,-109.0),2300,'After the 1793 attacks on the Saskatchewan posts'),
        g(1870,(48.4,-108.5),1500,'1869–70 smallpox'),g(1888.5,P['ft_belknap'],900,'Fort Belknap reservation')],
 # ---------------- Cheyenne, Arapaho ----------------
 'chy':[g(1700,(46.6,-97.6),2500,'Sheyenne River village (Biesterfeldt site)'),g(1765,(46.4,-97.8),2800,''),g(1785,(45.4,-100.5),3000,'Missouri River villages'),
        g(1795,(44.4,-103.3),3000,'Black Hills; becoming fully nomadic'),g(1805,None,2800,'Clark’s figure judged low (cf. Morse 1822)'),g(1828,(42.6,-104.4),3300,''),g(1832,(41.6,-104.2),3300,'Division into northern and southern bands')],
 'chs':[g(1832,(41.6,-104.2),1800,''),g(1834,P['bents'],2000,'Bent’s Fort trade'),g(1840.6,(38.1,-103.2),2600,'Great Peace with Kiowa & Comanche, 1840'),
        g(1849.5,None,2200,'1849 cholera'),g(1864.9,(38.6,-101.3),2000,'Sand Creek, Nov. 1864: Black Kettle’s Wutapiu (see bands)'),g(1867.8,P['medicine_lodge'],2000,'Medicine Lodge treaty'),
        g(1868.9,(36.1,-99.3),1900,'Washita, Nov. 1868: Black Kettle’s camp (see bands)'),g(1869.5,P['darlington'],1900,'Darlington agency'),g(1890,P['darlington'],2100,'')],
 'chn':[g(1832,(41.6,-104.2),1300,''),g(1845,(42.6,-105.2),1500,''),g(1860,(44.0,-105.8),1600,''),g(1866,(44.5,-106.3),1700,''),
        g(1876.47,P['lbh'],1300,'Little Bighorn camp, June 1876'),g(1876.9,(43.9,-106.8),1200,'Dull Knife fight, Nov. 1876'),
        g(1877.4,(42.67,-103.47),1100,'Surrender at Camp Robinson'),g(1877.7,P['darlington'],950,'Exiled to Indian Territory'),
        g(1878.7,P['darlington'],900,'Dull Knife’s and Little Wolf’s breakout north (see bands)'),
        g(1883.4,P['darlington'],1000,''),g(1883.8,P['pine_ridge'],1050,'The exiles still in the south move north'),g(1884.9,P['lame_deer'],1200,'Tongue River reservation')],
 'ara':[g(1700,(46.6,-101.0),3000,'Placement uncertain'),g(1750,(44.6,-103.2),3000,''),g(1782,None,2400,''),g(1820,(40.6,-104.5),2600,''),g(1835,(40.0,-104.0),2700,'Division into northern and southern bands')],
 'ars':[g(1835,(39.0,-103.5),1500,''),g(1850,(38.3,-102.0),1600,''),g(1864.9,(38.6,-102.4),1300,'Sand Creek'),g(1867.8,P['medicine_lodge'],1300,''),
        g(1870,(35.6,-98.1),1600,'Cheyenne & Arapaho agency'),g(1890,(35.6,-98.1),1100,'')],
 'arn':[g(1835,(41.4,-104.9),1200,''),g(1866,(44.3,-106.0),1000,'Powder River country'),g(1876,(42.67,-103.47),1000,'Red Cloud agency'),g(1878.3,P['wind_res'],950,'Wind River reservation')],
 # ---------------- Crow, Mandan, Hidatsa ----------------
 'cwm':[g(1700,(45.3,-108.8),3000,''),g(1780,(45.0,-108.5),4000,''),g(1782,None,2500,'1781 smallpox'),g(1805,None,3500,'Clark’s upper figure is nearer later counts'),
        g(1830,(44.6,-108.3),4000,''),g(1855,(44.4,-108.6),2700,'Our share of Denig’s 460 lodges'),g(1869.5,(45.68,-110.37),2700,'Mission Creek agency'),
        g(1875,(45.45,-109.5),2600,'Stillwater (Absaroka) agency'),g(1884.5,P['crow_ag'],3200,'Crow Agency; River Crow rejoin'),g(1905,P['crow_ag'],1800,'')],
 'cwr':[g(1700,(46.5,-106.5),1500,''),g(1782,None,1200,''),g(1805,None,2500,''),g(1830,(46.4,-107.8),2500,''),g(1850,(47.0,-107.0),1600,''),
        g(1859,(47.8,-107.5),1500,'River Crow move to the Missouri & Milk'),g(1880,(47.0,-107.8),1100,''),g(1884,P['crow_ag'],1000,'Rejoin at Crow Agency')],
 'man':[g(1700,P['heartR'],9000,'Heart River villages; numbers before 1780 highly uncertain'),g(1738.9,(46.9,-100.6),9000,'La Vérendrye’s visit, Dec. 1738'),
        g(1780,None,7000,''),g(1782,None,2500,'1780–81 smallpox'),g(1795,(47.27,-101.2),1800,'Removal up to the Knife River'),
        g(1837.5,None,1600,''),g(1838,P['ft_clark'],150,'1837 smallpox'),g(1845.6,P['like_fishhook'],200,'Like-a-Fishhook village'),g(1905,(47.45,-102.1),250,'Charging Eagle and Red Butte')],
 'hid':[g(1700,P['knifeR'],4000,''),g(1780,None,4000,''),g(1782,None,2200,'1781 smallpox'),g(1837,None,2000,'Hayden’s 120 lodges × 5 undercounts earth-lodge households'),
        g(1838.6,None,1000,'Hayden’s 40 lodges after the smallpox judged an undercount'),g(1845.6,P['like_fishhook'],900,'Like-a-Fishhook village'),g(1905,(47.6,-102.25),470,'Independence')],
 # ---------------- Kiowa, Apache ----------------
 'kio':[g(1700,(45.9,-111.0),1500,'Upper Yellowstone–Missouri headwaters (Kiowa tradition)'),g(1740,(45.2,-107.0),1700,'Allied with the Crow'),
        g(1765,(44.0,-103.9),1800,'Black Hills'),g(1782,None,1200,'1781 smallpox'),g(1790,(42.6,-103.4),1300,'Pushed south by Lakota & Cheyenne'),
        g(1805,None,1500,'Clark’s 700 judged low'),g(1810,None,1600,'Alliance with the Comanche, c. 1806'),g(1820,(38.0,-101.5),None,'South of the Arkansas with the Comanche; still on the North Platte in winter 1814–15 (Corbusier count)'),
        g(1833.3,(34.9,-98.9),1700,'Cut-Throat Massacre by the Osage, 1833'),g(1840.6,(38.1,-103.0),1700,'Great Peace, 1840'),g(1849.5,None,1500,'1849 cholera'),
        g(1860,(37.0,-100.0),1700,''),g(1867.8,P['medicine_lodge'],1600,''),g(1869.5,P['ft_sill'],1500,'Kiowa-Comanche agency'),
        g(1874.75,P['palo_duro'],1300,'Red River War'),g(1875.3,P['ft_sill'],1100,''),g(1905,(35.0,-98.4),1150,'')],
 'kap':[g(1700,(43.8,-102.8),400,''),g(1805,None,350,''),g(1810,(38.3,-101.2),350,'Following the Kiowa'),g(1840,(37.8,-102.6),350,''),
        g(1869.5,(34.75,-98.3),300,''),g(1905,(35.1,-98.3),160,'')],
 'apc':[g(1700,P['cuartelejo'],3000,'El Cuartelejo'),g(1719.7,P['cuartelejo'],2500,'Valverde expedition'),g(1727,(37.4,-103.6),1500,'Pressed by Comanche'),g(1732,(36.8,-105.0),1000,'Absorbed into the Jicarilla')],
 'jic':[g(1700,(36.8,-104.7),2500,''),g(1733,(36.5,-105.5),2000,'Mission near Taos'),g(1780,(36.6,-105.4),1500,''),g(1850,(36.4,-105.5),1000,''),g(1887,(36.75,-107.0),800,'Jicarilla reservation'),g(1905,(36.75,-107.0),780,'')],
 'lip':[g(1700,(34.8,-102.2),3000,'Southern High Plains'),g(1740,(31.6,-100.6),3000,'Pushed south by the Comanche'),g(1757.3,(30.9,-99.8),2800,'San Sabá mission'),
        g(1762,(29.6,-99.9),2800,'Missions on the upper Nueces'),g(1780,(29.4,-100.6),2500,''),g(1830,(28.9,-100.1),1500,''),g(1850,(29.0,-101.0),800,''),
        g(1880,(29.2,-102.4),200,''),g(1903.5,(28.8,-101.2),40,'Band in Coahuila (centre ours)'),g(1905,(33.15,-105.7),30,'With the Mescalero')],
 # ---------------- Comanche, Shoshone ----------------
 'cyj':[g(1700,(39.6,-103.8),1500,''),g(1740,(38.5,-104.2),2000,''),g(1780,(37.9,-103.4),3000,''),g(1782,None,1800,''),
        g(1786.15,None,1800,'Anza’s peace, signed at Pecos 1786 by a delegation (not a place for the division)'),g(1795,(37.6,-101.0),1600,'Merging with the Yamparika')],
 'cyy':[g(1700,(40.6,-106.6),2000,'Yampa & North Park'),g(1730,(39.3,-104.8),3000,''),g(1760,(38.3,-102.0),4000,''),g(1780,(37.8,-101.5),6000,''),
        g(1782,None,4000,'1780–81 smallpox'),g(1800,(37.5,-100.8),5000,''),g(1840,(36.6,-100.1),None,''),g(1849.5,None,None,'1849 cholera'),g(1860,(36.4,-99.6),2000,''),g(1867.8,P['medicine_lodge'],1800,''),
        g(1869,None,1200,'Agency count covers only part of the division'),g(1875.4,(34.7,-98.5),400,''),g(1905,(34.7,-98.55),350,'')],
 'cyk':[g(1700,(38.7,-104.8),1500,''),g(1730,(37.5,-103.0),2500,''),g(1750,(36.0,-102.4),4000,''),g(1780,(35.3,-101.8),6000,''),g(1782,None,4000,''),
        g(1800,(35.2,-101.0),4500,''),g(1840,(35.4,-100.5),None,''),g(1849.5,None,None,''),
        g(1860,(35.3,-100.5),1500,''),g(1869.5,(34.7,-98.45),600,''),g(1905,(34.75,-98.4),300,'')],
 'cyp':[g(1745,(35.4,-101.4),1500,'Eastern Comanche separating'),g(1758.2,None,3000,'Destruction of the San Sabá mission, 1758, by a war party (not a place for the division)'),g(1760,(33.0,-99.0),3000,''),
        g(1780,(32.0,-99.5),8000,'Eastern Comanche at their height (Hämäläinen’s high reckoning)'),g(1782,None,4000,'Eastern Comanche reported losing two-thirds to smallpox'),
        g(1785.6,None,4200,'Peace with Spanish Texas, 1785, made by a delegation at San Antonio (not a place for the division)'),g(1800,(31.5,-99.0),5000,''),g(1838,P['edwards'],None,''),g(1840.2,None,None,'Council House Fight, San Antonio: a delegation (not a place for the division)'),g(1840.6,None,None,'Great Raid to Linnville, Aug. 1840: a war party (not a place for the division)'),
        g(1841,(31.5,-99.0),None,''),g(1849.5,None,None,'1849 cholera'),g(1855,(33.0,-99.0),500,'Clear Fork (Brazos) reserve'),
        g(1859.6,P['anadarko'],400,'Removed to the Wichita agency'),g(1869,(34.68,-98.45),350,''),g(1905,(34.68,-98.45),250,'')],
 'cyn':[g(1830,(34.5,-99.8),2000,''),g(1847,None,1500,'1847 report called exaggerated'),g(1860,(34.3,-100.2),1000,''),g(1869,P['ft_sill'],None,''),g(1905,(34.62,-98.5),300,'')],
 'cyq':[g(1835,(34.4,-101.8),1500,'Llano Estacado'),g(1860,(34.3,-101.6),1500,''),g(1874.75,P['palo_duro'],1000,'Palo Duro Canyon, Sept. 1874'),
        g(1875.4,P['ft_sill'],400,'Surrender at Fort Sill, June 1875'),g(1905,(34.62,-98.35),300,'')],
 'sho':[g(1700,(49.6,-111.0),6000,'Northwestern Plains; placement uncertain'),g(1730,(48.6,-110.4),7000,''),g(1780,(47.2,-110.5),6000,''),
        g(1782,None,3000,'1781 smallpox; Blackfoot guns push them south'),g(1800,(44.8,-110.0),3000,''),g(1830,(42.6,-109.5),2500,'Wind River & Green River'),
        g(1868.5,P['wind_res'],1800,'Wind River reservation'),g(1905,(43.05,-108.95),900,'')],
 # ---------------- Caddoan ----------------
 'wic':[g(1700,(37.6,-97.8),6000,'Great Bend villages (Quivira)'),g(1719.6,(35.9,-95.65),6000,'La Harpe’s visit'),g(1745,(36.8,-97.18),5000,'Deer Creek (Ferdinandina) village'),
        g(1757,P['spanish_fort'],4500,'Twin villages on the Red River'),g(1759.8,P['spanish_fort'],4500,'Defeat of Parrilla, 1759'),g(1778,None,3000,'1777–78 epidemics'),
        g(1820,(34.2,-98.4),2000,''),g(1834.5,(34.84,-99.15),1800,'Dodge–Leavenworth visit, 1834'),g(1850,(34.85,-98.0),1300,'Rush Springs'),
        g(1859.6,P['anadarko'],1200,'Wichita agency'),g(1863.0,(37.7,-97.3),1000,'Civil War refugees in Kansas from the winter of 1862–63 (Newcomb, Handbook 13, p. 559)'),g(1867.5,P['anadarko'],900,''),g(1905,P['anadarko'],450,'')],
 'pwc':[g(1700,P['grand_pawnee'],4000,''),g(1780,None,4500,''),g(1782,None,3500,''),g(1805,None,2000,'Clark’s undeducted figure'),
        g(1838,None,3000,'1838 smallpox'),g(1849.5,None,2500,'1849 cholera'),g(1859.5,P['genoa'],1500,'Genoa reservation'),g(1875.5,P['pawnee_ok'],900,'Removal to Indian Territory'),g(1905,P['pawnee_ok'],300,'')],
 'pwk':[g(1700,(40.0,-98.0),2000,''),g(1780,P['rep_vil'],2500,''),g(1804.4,(41.27,-97.32),2000,''),g(1806.75,P['rep_vil'],2000,'Pike’s visit to the Republican village, 1806'),
        g(1820,(41.3,-97.5),1500,'Morse: 40 lodges, young men gone to the Grand village'),g(1850,(41.35,-97.6),1500,''),g(1859.5,P['genoa'],1100,''),g(1875.5,P['pawnee_ok'],700,''),g(1905,P['pawnee_ok'],200,'')],
 'pws':[g(1700,P['skidi_loup'],4000,''),g(1780,P['loup_vil'],4000,''),g(1782,None,3000,''),g(1805,None,1600,''),g(1838,None,2500,''),
        g(1849.5,None,1800,''),g(1859.5,P['genoa'],1200,''),g(1875.5,P['pawnee_ok'],800,''),g(1905,P['pawnee_ok'],250,'')],
 'ari':[g(1700,(44.6,-100.4),12000,'Many villages near the Bad River; numbers highly uncertain'),g(1760,(44.9,-100.4),10000,''),g(1781,None,4000,'1780–81 smallpox'),
        g(1795,P['arikara_1804'],3000,''),g(1823.6,P['arikara_1804'],2500,'Leavenworth’s attack, Aug. 1823'),g(1830,P['arikara_1804'],2200,'Back at the Grand River villages, spring 1824 to 1833 (Parks, Handbook 13, pp. 366–67)'),
        g(1834,P['skidi_loup'],2000,'Living with the Skiri on the Loup'),g(1838,P['ft_clark'],1500,'Reoccupy the Mandan village'),g(1849.5,None,1300,''),
        g(1862.5,P['like_fishhook'],1500,'Like-a-Fishhook village')],
 # ---------------- Dhegiha & Chiwere ----------------
 'oma':[g(1700,(43.5,-96.6),3000,'Big Sioux River'),g(1740,(42.9,-97.3),3000,''),g(1775,P['omaha_vil'],3000,'Big Village (Tonwontonga)'),g(1802,None,900,'1800–01 smallpox'),
        g(1810,P['omaha_vil'],1300,''),g(1845,(41.3,-95.95),1300,''),g(1856,P['omaha_res'],1000,'Omaha reservation'),g(1905,P['omaha_res'],1200,'')],
 'pon':[g(1700,(43.4,-96.9),800,''),g(1750,P['ponca_ck'],800,'Ponca Creek'),g(1802,None,250,'1800–01 smallpox'),g(1830,P['ponca_ck'],700,''),
        g(1877.4,P['ponca_ck'],700,''),g(1877.8,(36.95,-94.85),600,'Forced removal, Quapaw agency'),g(1878.6,P['ponca_ok'],550,''),g(1905,P['ponca_ok'],750,'')],
 'oto':[g(1700,(43.5,-94.9),1500,'Blue Earth & Okoboji country'),g(1720,(41.0,-95.9),1400,''),g(1780,P['oto_vil'],1200,''),g(1830,P['oto_vil'],1100,'Missouria merged'),
        g(1840,(41.05,-95.95),900,''),g(1855,P['big_blue'],450,'Big Blue reservation'),g(1881.6,P['oto_ok'],350,'Red Rock, Indian Territory'),g(1905,P['oto_ok'],390,'')],
 'mis':[g(1700,(39.42,-93.13),2000,'Village on the Missouri below the Grand R.'),g(1760,(39.4,-93.1),1500,''),g(1790,(39.5,-93.6),800,''),g(1798,(41.0,-96.25),300,'Join the Oto'),g(1830,(41.0,-96.3),250,'')],
 'kaw':[g(1700,(39.6,-95.1),2000,'Grand Village des Canzes'),g(1724.8,(39.6,-95.1),2000,'Bourgmont’s visit, 1724'),g(1780,P['kaw_vil'],1800,'Blue Earth village'),g(1805,None,1500,''),
        g(1827,(39.07,-95.9),1600,''),g(1847,P['council_grove'],1400,'Council Grove reservation'),g(1873.4,P['kaw_ok'],500,'Removal to Indian Territory'),g(1905,P['kaw_ok'],220,'')],
 'osg':[g(1700,P['osage_vil'],6000,''),g(1780,None,6500,''),g(1802,None,3500,'Half the nation leaves for the Arkansas'),g(1805,None,2200,'Pike counted 1,695 in the Grand village in 1806'),
        g(1825,(37.6,-95.2),3200,'Neosho villages'),g(1839,(37.4,-95.3),4000,'Arkansas band returns'),g(1872,P['pawhuska'],2000,'Osage reservation, Pawhuska'),g(1905,P['pawhuska'],1100,'')],
 'osl':[g(1700,(39.4,-93.3),1500,'Missouri River near the Grand R.'),g(1777,(38.05,-94.2),1300,'Moved beside the Great Osage'),g(1825,(37.6,-95.45),1200,''),
        g(1872,(36.7,-96.4),1000,''),g(1905,(36.7,-96.4),500,'')],
 'osa':[g(1802,P['three_forks'],1500,''),g(1805,None,2000,'Our share of Clark’s 5,000'),g(1817.8,(36.3,-95.6),2000,'Claremore Mound battle, 1817'),g(1833.3,(36.0,-95.4),2000,''),g(1839,(37.4,-95.3),2000,'Rejoin the Great Osage')],
 'iow':[g(1700,(43.4,-95.1),1500,'Okoboji'),g(1765,(40.8,-92.1),1200,'Des Moines River'),g(1824,(39.65,-94.74),1000,''),g(1837,P['nemaha'],800,'Great Nemaha reservation'),g(1905,P['nemaha'],250,'')],
}

# ---------------------------------------------------------------------------------------------
# SETTLE: posts, forts, missions, towns. Dates & places recalled from standard references
# (Frazer, Forts of the West; HBC Archives post lists; Hannings) — not checked entry by entry.
# kind: 'spanish' | 'french' | 'trade' | 'army' | 'town'
SETTLE = [
 ('Fort Edmonton (first, at Sturgeon Creek)', 'trade', 53.71, -113.22, 1795, 1807, 'North American Forts (northamericanforts.com)'),
 ('Santa Fe', 'spanish', 35.69, -105.94, 1610, 1905, 'Wikipedia (capital 1610; Peralta’s town 1607)'),
 ('Pecos pueblo & mission', 'spanish', 35.55, -105.68, 1619, 1838, 'Wikipedia (mission 1619; pueblo abandoned 1838)'),
 ('El Paso del Norte', 'spanish', 31.74, -106.49, 1659, 1905, 'Wikipedia (town 1659)'),
 ('Santa Cruz de la Cañada', 'spanish', 36.0, -106.03, 1695, 1905, 'Wikipedia'),
 ('Albuquerque', 'spanish', 35.08, -106.65, 1706, 1905, 'Wikipedia'),
 ('Nacogdoches', 'spanish', 31.6, -94.65, 1716, 1905, 'Wikipedia (mission 1716; town refounded 1779)'),
 ('San Antonio de Béxar', 'spanish', 29.42, -98.49, 1718, 1905, 'Wikipedia'),
 ('Los Adaes', 'spanish', 31.65, -93.2, 1721, 1773, 'Wikipedia'),
 ('La Bahía (Goliad)', 'spanish', 28.66, -97.38, 1749, 1905, 'Wikipedia (moved to Goliad 1747–49)'),
 ('Abiquiú', 'spanish', 36.2, -106.32, 1754, 1905, 'Wikipedia'),
 ('Laredo', 'spanish', 27.53, -99.48, 1755, 1905, 'Wikipedia'),
 ('San Sabá presidio', 'spanish', 30.92, -99.83, 1757, 1772, 'Wikipedia (abandoned 1768, reoccupied 1770–72)'),
 ('San Miguel del Vado', 'spanish', 35.37, -105.45, 1794, 1905, 'Wikipedia (settlement petition 1794)'),
 ('Taos (Don Fernando de Taos)', 'spanish', 36.4, -105.57, 1795, 1905, 'Wikipedia (intermittent from c. 1615; permanent from 1795)'),
 ('Arkansas Post', 'french', 34.02, -91.35, 1686, 1905, 'Wikipedia'),
 ('Cahokia', 'french', 38.57, -90.19, 1699, 1905, 'Wikipedia (gives 1696, 1689 and 1699; 1699 kept)'),
 ('Kaskaskia', 'french', 37.92, -89.92, 1703, 1905, 'Wikipedia'),
 ('Natchitoches', 'french', 31.76, -93.09, 1714, 1905, 'Wikipedia'),
 ('Fort de Chartres', 'french', 38.08, -90.16, 1720, 1772, 'Wikipedia (wooden fort 1718–20; stone fort abandoned 1772)'),
 ('Fort Orleans', 'french', 39.29, -93.24, 1723, 1726, 'Wikipedia (site not found; between the two candidate sites)'),
 ('Fort La Reine', 'french', 49.97, -98.3, 1738, 1752, 'Wikipedia; North American Forts (northamericanforts.com) gives 1754'),
 ('Fort Rouge', 'french', 49.88, -97.13, 1738, 1749, 'North American Forts (northamericanforts.com) (intermittent)'),
 ('Fort Dauphin (Lake Winnipegosis)', 'french', 51.65, -99.92, 1741, 1760, 'Wikipedia'),
 ('Fort de Cavagnial', 'french', 39.35, -94.92, 1744, 1760, 'North American Forts (northamericanforts.com)'),
 ('Ste. Genevieve', 'french', 37.98, -90.04, 1750, 1905, 'Wikipedia (about 1750, per Ekberg; traditional dates 1735–40)'),
 ('Fort à la Corne', 'french', 53.2, -104.8, 1753, 1759, 'Wikipedia, “Fort de la Corne”'),
 ('St. Louis', 'french', 38.63, -90.2, 1764, 1905, 'Wikipedia'),
 ('Cumberland House', 'trade', 53.94, -102.31, 1774, 1905, 'Wikipedia'),
 ('Hudson House (Upper 1778–79, Lower 1779–87)', 'trade', 53.15, -106.27, 1778, 1787, 'North American Forts (northamericanforts.com)'),
 ('Manchester House', 'trade', 52.92, -108.6, 1786, 1793, 'Wikipedia'),
 ('South Branch House', 'trade', 52.85, -105.95, 1786, 1794, 'North American Forts (northamericanforts.com); Wikipedia'),
 ('Fort Espérance', 'trade', 50.49, -101.58, 1787, 1819, 'Wikipedia'),
 ('Fort George / Buckingham House', 'trade', 53.85, -111.03, 1792, 1800, 'Wikipedia'),
 ('Brandon House', 'trade', 49.7, -99.67, 1793, 1832, 'Wikipedia (1793–1824; re-established 1828–32)'),
 ('Fort Ellice (Qu’Appelle River post)', 'trade', 50.41, -101.29, 1794, 1892, 'Wikipedia'),
 ('Fort Edmonton', 'trade', 53.54, -113.5, 1808, 1905, 'North American Forts (northamericanforts.com) (present site from 1808; final site 1831)'),
 ('Fort Carlton (first, at the Forks)', 'trade', 53.15, -105.1, 1795, 1804, 'North American Forts (northamericanforts.com)'),
 ('Pembina post', 'trade', 48.97, -97.25, 1797, 1905, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Rocky Mountain House', 'trade', 52.37, -114.93, 1799, 1876, 'Wikipedia'),
 ('Chesterfield House', 'trade', 50.93, -110.0, 1800, 1805, 'North American Forts (northamericanforts.com)'),
 ('Fort Mandan (Lewis & Clark)', 'trade', 47.3, -101.1, 1804, 1805, 'Wikipedia'),
 ('South Branch House (rebuilt)', 'trade', 52.85, -105.95, 1805, 1870, 'Wikipedia'),
 ('Fort Gibraltar / Fort Garry', 'trade', 49.89, -97.13, 1807, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Carlton', 'trade', 52.87, -106.53, 1810, 1885, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Lisa', 'trade', 41.38, -95.95, 1812, 1823, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Chouteau’s post (La Saline)', 'trade', 36.29, -95.15, 1817, 1837, 'North American Forts (northamericanforts.com)'),
 ('Chouteau’s post (Three Forks)', 'trade', 35.8, -95.4, 1820, 1833, 'North American Forts (northamericanforts.com)'),
 ('Fort Tecumseh / Fort Pierre', 'trade', 44.389, -100.391, 1822, 1857, 'Wikipedia (gives 1817 for Fort Tecumseh; 1822 kept)'),
 ('Fort Union', 'trade', 48.0, -104.04, 1829, 1867, 'Wikipedia'),
 ('Fort Pitt', 'trade', 53.57, -109.8, 1829, 1890, 'North American Forts (northamericanforts.com) (burned 1885, rebuilt)'),
 ('Fort Clark', 'trade', 47.25, -101.27, 1831, 1861, 'Wikipedia'),
 ('Fort McKenzie', 'trade', 47.88, -110.5, 1832, 1844, 'North American Forts (northamericanforts.com); FortWiki (1833)'),
 ('Fort Cass', 'trade', 46.16, -107.5, 1832, 1835, 'North American Forts (northamericanforts.com)'),
 ('Bent’s Fort', 'trade', 38.04, -103.43, 1833, 1849, 'Wikipedia (1833; some accounts begin construction in 1828)'),
 ('Fort William / Fort Laramie (post)', 'trade', 42.2, -104.55, 1834, 1849, 'North American Forts (northamericanforts.com)'),
 ('Fort Hall', 'trade', 43.02, -112.6, 1834, 1856, 'Wikipedia says abandoned by 1863; 1856 (end of HBC trade) kept'),
 ('Fort Vasquez', 'trade', 40.2, -104.8, 1835, 1842, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Bridger', 'trade', 41.32, -110.39, 1843, 1858, 'North American Forts (northamericanforts.com)'),
 ('Fort Benton (post)', 'trade', 47.82, -110.67, 1847, 1869, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Qu’Appelle', 'trade', 50.76, -103.79, 1852, 1905, 'Wikipedia'),
 ('Fort Whoop-Up', 'trade', 49.69, -112.86, 1869, 1874, 'Wikipedia'),
 ('Fort Osage', 'army', 39.19, -94.19, 1808, 1822, 'Wikipedia (empty 1813–15)'),
 ('Fort Smith', 'army', 35.39, -94.43, 1817, 1824, 'Wikipedia (first fort 1817–24)'),
 ('Fort Smith (second)', 'army', 35.39, -94.43, 1838, 1871, 'Wikipedia'),
 ('Fort Atkinson (Neb.)', 'army', 41.455, -96.014, 1819, 1827, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Snelling', 'army', 44.89, -93.18, 1819, 1905, 'Wikipedia'),
 ('Fort Gibson', 'army', 35.8, -95.25, 1824, 1890, 'North American Forts (northamericanforts.com)'),
 ('Fort Towson', 'army', 34.02, -95.27, 1824, 1854, 'North American Forts (northamericanforts.com) (gap 1829–31)'),
 ('Fort Leavenworth', 'army', 39.35, -94.92, 1827, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Scott', 'army', 37.84, -94.7, 1842, 1853, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Kearny', 'army', 40.64, -99.0, 1848, 1871, 'Wikipedia'),
 ('Fort Laramie', 'army', 42.2, -104.55, 1849, 1890, 'North American Forts (northamericanforts.com)'),
 ('Fort Union (N.M.)', 'army', 35.9, -105.0, 1851, 1891, 'North American Forts (northamericanforts.com)'),
 ('Fort Belknap (Tex.)', 'army', 33.15, -98.74, 1851, 1859, 'Wikipedia (briefly reoccupied 1867)'),
 ('Fort Riley', 'army', 39.06, -96.8, 1853, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Randall', 'army', 43.06, -98.55, 1856, 1892, 'North American Forts (northamericanforts.com)'),
 ('Fort Bridger (army)', 'army', 41.32, -110.39, 1858, 1890, 'North American Forts (northamericanforts.com)'),
 ('Fort Larned', 'army', 38.18, -99.22, 1859, 1878, 'Wikipedia'),
 ('Fort Wise / Fort Lyon (old site)', 'army', 38.07, -102.95, 1860, 1867, 'Wikipedia'),
 ('Fort Sumner', 'army', 34.4, -104.2, 1862, 1869, 'North American Forts (northamericanforts.com)'),
 ('Fort Sedgwick', 'army', 40.97, -102.2, 1864, 1871, 'North American Forts (northamericanforts.com)'),
 ('Fort Dodge', 'army', 37.73, -99.94, 1865, 1882, 'Wikipedia'),
 ('Fort Wallace', 'army', 38.91, -101.59, 1865, 1882, 'Wikipedia'),
 ('Fort Hays', 'army', 38.86, -99.34, 1865, 1889, 'Wikipedia'),
 ('Fort Reno (Wyo.)', 'army', 43.83, -106.24, 1865, 1868, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Fort Phil Kearny', 'army', 44.53, -106.83, 1866, 1868, 'North American Forts (northamericanforts.com)'),
 ('Fort C. F. Smith', 'army', 45.31, -107.92, 1866, 1868, 'North American Forts (northamericanforts.com)'),
 ('Fort Buford', 'army', 47.99, -104.0, 1866, 1895, 'Wikipedia'),
 ('Fort Fetterman', 'army', 42.84, -105.48, 1867, 1882, 'North American Forts (northamericanforts.com)'),
 ('Fort D. A. Russell', 'army', 41.16, -104.86, 1867, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Ellis', 'army', 45.67, -111.0, 1867, 1886, 'Wikipedia'),
 ('Fort Concho', 'army', 31.45, -100.43, 1867, 1889, 'Wikipedia'),
 ('Fort Griffin', 'army', 32.93, -99.23, 1867, 1879, 'Wikipedia'),
 ('Fort Richardson', 'army', 33.2, -98.17, 1867, 1878, 'Wikipedia'),
 ('Fort Lyon (new site)', 'army', 38.074, -103.133, 1867, 1889, 'Wikipedia (army post to 1889; Wikipedia gives 1897)'),
 ('Fort Supply', 'army', 36.57, -99.57, 1868, 1895, 'Wikipedia'),
 ('Fort Sill', 'army', 34.66, -98.4, 1869, 1905, 'Wikipedia'),
 ('Fort Benton (army)', 'army', 47.83, -110.66, 1869, 1881, 'North American Forts (northamericanforts.com)'),
 ('Fort Abraham Lincoln', 'army', 46.76, -100.85, 1872, 1891, 'Wikipedia'),
 ('Fort Robinson', 'army', 42.67, -103.47, 1874, 1905, 'Wikipedia'),
 ('Fort Reno (Okla.)', 'army', 35.562, -98.035, 1874, 1905, 'Wikipedia'),
 ('Fort Macleod (NWMP)', 'army', 49.72, -113.4, 1874, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Elliott', 'army', 35.518, -100.456, 1875, 1890, 'Wikipedia'),
 ('Fort Walsh (NWMP)', 'army', 49.57, -109.88, 1875, 1883, 'Wikipedia'),
 ('Fort Calgary (NWMP)', 'army', 51.05, -114.05, 1875, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Keogh', 'army', 46.38, -105.85, 1876, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Custer', 'army', 45.7, -107.55, 1877, 1898, 'North American Forts (northamericanforts.com)'),
 ('Fort Assinniboine', 'army', 48.5, -109.8, 1879, 1905, 'North American Forts (northamericanforts.com)'),
 ('Fort Maginnis', 'army', 47.186, -109.139, 1880, 1890, 'Wikipedia; North American Forts (northamericanforts.com)'),
 ('Red River Settlement', 'town', 50.0, -97.0, 1812, 1905, 'Wikipedia'),
 ('Independence', 'town', 39.09, -94.42, 1827, 1905, 'Wikipedia'),
 ('Westport / Kansas City', 'town', 39.06, -94.59, 1833, 1905, 'Wikipedia (area first settled about 1823; town laid out 1833, recalled)'),
 ('Omaha', 'town', 41.26, -95.94, 1854, 1905, 'Wikipedia'),
 ('Sioux City', 'town', 42.5, -96.4, 1854, 1905, 'Wikipedia'),
 ('Denver', 'town', 39.74, -104.99, 1858, 1905, 'Wikipedia'),
 ('Yankton', 'town', 42.87, -97.4, 1858, 1905, 'Wikipedia'),
 ('Virginia City (Mont.)', 'town', 45.29, -111.94, 1863, 1905, 'Wikipedia'),
 ('Helena', 'town', 46.6, -112.03, 1864, 1905, 'Wikipedia'),
 ('Cheyenne', 'town', 41.14, -104.82, 1867, 1905, 'Wikipedia'),
 ('Abilene', 'town', 38.92, -97.21, 1867, 1905, 'Wikipedia (founded 1857; cattle railhead 1867)'),
 ('Wichita', 'town', 37.69, -97.34, 1868, 1905, 'Wikipedia'),
 ('Dodge City', 'town', 37.75, -100.02, 1872, 1905, 'Wikipedia'),
 ('Bismarck', 'town', 46.81, -100.78, 1872, 1905, 'Wikipedia'),
 ('Deadwood', 'town', 44.38, -103.73, 1876, 1905, 'Wikipedia'),
 ('Miles City', 'town', 46.41, -105.84, 1877, 1905, 'Wikipedia'),
 ('Billings', 'town', 45.78, -108.5, 1882, 1905, 'Wikipedia (railroad town 1882; Coulson 1877)'),
 ('Regina', 'town', 50.45, -104.6, 1882, 1905, 'Wikipedia'),
 ('Calgary', 'town', 51.05, -114.07, 1883, 1905, 'Wikipedia (Fort Calgary 1875; railway 1883)'),
]

# =============================================================================================
# ADDITIONS (round 2)
MOONEY = 'Mooney, Calendar History of the Kiowa Indians (BAE 17th Annual Report, 1898)'
CIA = lambda y: f'Annual Report of the Commissioner of Indian Affairs for {y}'
def kc(y,lat,lon,raw,r=25):  # Kiowa calendar camp: place only
    return dict(g='kio',y=y,pop=None,raw=raw,basis='',loc='stated',at=(lat,lon),r=r,src=MOONEY+', calendar entry',kind='primary')
OBS += [
 # ---- Mooney: Kiowa calendar camps, 1833–1891 (place only; season from the calendar) ----
 kc(1833.25,35.0,-98.95,'Spring 1833: camped at the mouth of Rainy-mountain creek on the Washita when the Osage struck (Cut-Throat Massacre)'),
 kc(1833.9,34.9,-99.6,'Winter 1833–34 (“the stars fell”): camped on a small tributary of Elm fork of Red river, Greer county'),
 kc(1834.9,35.25,-99.1,'Winter 1834–35: winter camp on the Washita',60),
 kc(1835.5,35.75,-98.45,'Summer 1835: Cat-tail rush sun dance, south bank of the North Canadian at the Red hills, ~30 mi above Fort Reno'),
 kc(1836.5,36.4,-99.8,'Summer 1836: Wolf-river sun dance, on Wolf creek fork of the North Canadian',40),
 kc(1836.9,34.5,-100.3,'Winter 1836–37: camped on upper Red river',80),
 kc(1837.5,35.35,-100.4,'Summer 1837: Kiowa, Comanche and Apache camped on a tributary of Scott creek, upper North fork of Red river'),
 kc(1838.5,36.4,-99.5,'Summer 1838: confederated camps on Wolf creek above its junction with Beaver creek, attacked by Cheyenne & Arapaho'),
 kc(1839.5,35.05,-98.6,'Summer 1839: Peninsula sun dance, south side of the Washita below Walnut creek'),
 kc(1842.5,36.2,-99.9,'Summer 1842: Repeated sun dance on Kiowa Medicine-lodge creek, entering the North Canadian near 100°',40),
 kc(1843.5,36.2,-99.9,'Summer 1843: sun dance again on Kiowa Medicine-lodge creek',40),
 kc(1845.5,36.2,-99.9,'Summer 1845: sun dance on Kiowa Medicine-lodge creek',40),
 kc(1846.5,36.3,-100.0,'Summer 1846: sun dance on a small tributary of the North Canadian above Medicine-lodge creek',40),
 kc(1846.9,34.95,-99.25,'Winter 1846–47: winter camp on Elk creek, tributary of the North fork of Red river'),
 kc(1847.9,35.5,-103.4,'Winter 1847–48: camped all winter on “White river,” an extreme upper branch of the South Canadian',120),
 kc(1848.5,38.04,-103.4,'Summer 1848: sun dance on the Arkansas near Bent’s fort'),
 kc(1848.9,38.04,-103.4,'Winter 1848–49: camped on the Arkansas near Bent’s fort'),
 kc(1849.9,36.9,-98.6,'Winter 1849–50: camped in two divisions near the Salt fork of the Arkansas',50),
 kc(1851.5,36.57,-99.57,'Summer 1851: Dusty sun dance, north bank of the North Canadian below the junction of Wolf creek'),
 kc(1852.5,38.4,-99.6,'Summer 1852: Kiowa and Apache camped on “Black-hill river,” Kansas, north of the Arkansas',150),
 kc(1853.5,36.57,-99.57,'Summer 1853: sun dance near the present Fort Supply'),
 kc(1854.5,37.28,-98.58,'Summer 1854: Timber-mountain creek (Medicine Lodge creek) sun dance'),
 kc(1856.8,38.03,-103.25,'Fall 1856: Prickly-pear sun dance on the Arkansas ~10 mi below Bent’s fort'),
 kc(1856.95,38.04,-103.4,'Winter 1856–57: Kiowa, Cheyenne and Arapaho camped near Bent’s fort'),
 kc(1857.5,36.85,-98.9,'Summer 1857: sun dance on the north side of the Salt fork of the Arkansas'),
 kc(1857.9,38.05,-102.4,'Winter 1857–58: camped on Two-butte creek, south tributary of the Arkansas below Bent’s fort'),
 kc(1858.5,36.95,-98.35,'Summer 1858: Timber-circle sun dance on lower Mule creek near the mouth of Medicine-lodge creek'),
 kc(1859.5,38.85,-99.4,'Summer 1859: Cedar-bluff sun dance on the Smoky Hill opposite Timber creek, near Fort Hays'),
 kc(1860.9,37.95,-101.9,'Winter 1860–61: camped on the south side of the Arkansas near the western line of Kansas'),
 kc(1861.5,38.45,-99.3,'Summer 1861: sun dance on upper Walnut creek, which enters the Arkansas at the Great Bend'),
 kc(1861.95,37.8,-100.5,'Winter 1861–62: camped on the Arkansas in southwestern Kansas; smallpox brought from New Mexico',100),
 kc(1862.5,36.95,-98.4,'Summer 1862: Smallpox sun dance on Mule creek near the Salt fork'),
 kc(1862.9,38.45,-99.3,'Winter 1862–63: camped on upper Walnut creek (deep snow)'),
 kc(1863.5,38.33,-98.75,'Summer 1863: sun dance on the south side of the Arkansas at the Great Bend'),
 kc(1863.9,36.57,-99.57,'Winter 1863–64: winter camp on the North Canadian below the junction of Wolf creek'),
 kc(1864.5,36.92,-98.3,'Summer 1864: Ragweed sun dance at the junction of Medicine-lodge creek and the Salt fork'),
 kc(1865.5,35.05,-98.6,'Summer 1865: Peninsula sun dance in the bend of the Washita'),
 kc(1866.5,36.95,-98.3,'Summer 1866: German-silver sun dance on Medicine-lodge creek near its mouth'),
 kc(1867.5,35.6,-99.9,'Summer 1867: sun dance on the north bank of the Washita near the western line of Oklahoma'),
 kc(1867.8,37.28,-98.58,'Fall 1867: Medicine Lodge treaty'),
 kc(1868.5,37.25,-98.6,'Summer 1868: sun dance on Medicine-lodge creek near the treaty ground'),
 kc(1869.5,35.25,-99.95,'Summer 1869: sun dance on the North fork of Red river below Sweetwater creek'),
 kc(1869.9,36.57,-99.6,'Winter 1869–70: two camps on Beaver creek near Wolf creek, near Fort Supply'),
 kc(1870.5,35.0,-99.6,'Summer 1870: Plant-growing sun dance, south side of the North fork of Red river, Greer county'),
 kc(1871.9,35.05,-98.95,'Winter 1871–72: part on Long-tree creek, the rest on the Washita near Rainy mountain',50),
 kc(1872.9,35.05,-98.95,'Winter 1872–73: most of the Kiowa on the Washita near Rainy mountain'),
 kc(1873.5,35.4,-100.1,'Summer 1873: Maggot-creek (Sweetwater creek) sun dance'),
 kc(1874.45,34.97,-99.55,'Summer 1874: sun dance on the North fork of Red river at Last mountain (Mount Walsh)'),
 kc(1874.8,34.9,-101.3,'Fall 1874: after the Anadarko fight the Kiowa fled to the head of Red river',100),
 kc(1875.5,34.98,-99.5,'Summer 1875: Love-making spring sun dance near Last mountain, under troop escort'),
 kc(1876.5,35.25,-99.95,'Summer 1876: sun dance at the junction of Sweetwater creek and the North fork'),
 kc(1876.9,34.6,-98.4,'Winter 1876–77: camp a short distance below Fort Sill'),
 kc(1877.5,34.75,-99.7,'Summer 1877: Measles sun dance on the Salt fork of Red river, Greer county'),
 kc(1877.9,34.74,-98.53,'Winter 1877–78: camps near Mount Scott and Signal mountain'),
 kc(1878.5,34.95,-99.4,'Summer 1878: two sun dances on the North fork of Red river',50),
 kc(1879.5,34.9,-99.75,'Summer 1879: Horse-eating sun dance on Elm fork of Red river; buffalo nearly gone'),
 kc(1881.6,34.95,-99.4,'Summer 1881: Hot sun dance on the North fork of Red river',50),
 kc(1881.9,35.1,-98.55,'Winter 1881–82: winter camp on the Washita near the mouth of Hog creek'),
 kc(1884.9,35.1,-98.3,'Winter 1884–85: camped all winter on the Washita just above the agency'),
 kc(1885.5,35.05,-98.6,'Summer 1885: Little Peninsula sun dance in a bend of the Washita ~20 mi above the agency'),
 kc(1885.9,34.8,-98.6,'Winter 1885–86: camps northwest of Mount Scott'),
 kc(1888.9,35.05,-98.6,'Winter 1888–89: encamped on the Washita',40),
 kc(1890.5,35.05,-98.6,'Summer 1890: last attempted sun dance, at the bend of the Washita, stopped by troops'),
 kc(1890.9,35.0,-98.95,'Winter 1890–91: first Kiowa ghost dance, on the Washita at the mouth of Rainy-mountain creek'),
 # ---- Mooney: Kiowa & Plains Apache population series (his compilation of the reports) ----
 *[dict(g='kio',y=y,pop=p,raw=r,basis=b,loc='inferred',at=(36.0,-99.5) if y<1869 else (34.9,-98.5),r=300 if y<1869 else 60,src=MOONEY+', “Population”',kind='primary') for y,p,r,b in [
   (1814,900,'Wate-pana-toe and Ryuwa, 200 warriors, 900 souls (Brackenridge)','souls'),
   (1820,1000,'Wettaphato, 1,000 souls (Morse)','souls'),
   (1828,950,'140 families (i.e., about 950 souls?) (Spanish document of 1828)','families × 6.8 (Mooney)'),
   (1829,1000,'Keawas, 1,000 souls (Porter)','souls'),
   (1836,1800,'Kioways, 1,800 (estimate in Schoolcraft)','souls'),
   (1846,2000,'400 tipis, 2,000 souls (Bent)','souls'),
   (1849,1500,'300 warriors, 1,500 souls, a “careful estimate” (Neighbors)','souls'),
   (1851,1500,'1,500 souls, probably not more than','souls'),
   (1854,2800,'2,800 souls (Agent Whitfield)','souls'),
   (1865,1600,'1,500 to 1,700 souls, about 280 tipis, without Apache (Agent Leavenworth)','souls'),
   (1867,1680,'280 tipis, 1,680 souls, without Apache (Medicine Lodge treaty estimate)','souls'),
   (1869,1896,'1,896 (Reports for 1869 and 1870)','souls'),
   (1871,1776,'1,776 (Report)','souls'),
   (1874,1700,'1,700 (Report)','souls'),
   (1875,1070,'1,070; the first count after final subjugation','souls'),
   (1880,1139,'1,139','souls'),
   (1885,1169,'1,169','souls'),
   (1889,1142,'1,142, “a very careful census”','souls'),
   (1892,1014,'1,014 (decrease from the measles epidemic)','souls'),
   (1896,1065,'November 1896: Kiowa 1,065','souls')]],
 dict(g=['kio','kap'],y=1810,pop=3000,raw='“1,000 warriors, i.e., about 3,000 souls” (Pike); Mooney thinks this includes the Apache and is exaggerated',basis='souls',loc='inferred',at=(38.3,-101.5),r=300,src=MOONEY+', “Population”',kind='primary'),
 dict(g=['kio','kap'],y=1843,pop=1800,raw='1841–45: 1,800 souls (Indian Reports; probably including the Apache)',basis='souls',loc='inferred',at=(36.5,-100.0),r=300,src=MOONEY+', “Population”',kind='primary'),
 dict(g=['kio','kap'],y=1873,pop=1625,raw='1,600 to 1,650 at 6 to a tipi (Battey), probably including the Apache',basis='tipis × 6 (stated)',loc='inferred',at=(35.0,-98.9),r=80,src=MOONEY+', “Population”',kind='primary'),
 *[dict(g='kap',y=y,pop=p,raw=r,basis=b,loc='inferred',at=(36.0,-99.3) if y<1869 else (35.0,-98.3),r=300 if y<1869 else 60,src=MOONEY+', “Population” (Apache)',kind='primary') for y,p,r,b in [
   (1850,325,'50 lodges (=325 souls?)','lodges × 6.5 (Mooney)'),(1854,320,'40 lodges (Fitzpatrick); 320 (Whitfield)','souls'),
   (1865,180,'40 lodges, with 4 or 5 to a lodge (Leavenworth)','lodges × 4.5 (stated)'),(1867,420,'70 tipis, 420 souls (Medicine Lodge treaty estimate)','souls'),
   (1869,300,'300 (Report of 1870)','souls'),(1871,378,'378','souls'),(1875,344,'344','souls'),(1879,315,'315','souls'),
   (1892,241,'Apache 241','souls'),(1896,208,'November 1896: Apache 208','souls')]],
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1843,pop=19200,raw='1841–45: the Comanche “estimated at 19,200” (Indian Reports, as noted by Mooney)',basis='souls',loc='inferred',at=(34.5,-100.5),r=400,src=MOONEY+', “Population”',kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1849,pop=20000,raw='“Texas Indians in 1849”: Comanche or Na-u-ni, 20,000 souls, 4,000 warriors; “This estimate is made from the best information that could be obtained from the Indians by frequent inquiry on the subject”',basis='souls',loc='inferred',at=(33.5,-99.8),r=400,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['kio'],y=1849,pop=1500,raw='“Texas Indians in 1849”: Kiowa, 1,500 souls, 300 warriors; intercourse with the Kiowa “extremely limited”',basis='souls',loc='inferred',at=(36.0,-99.5),r=300,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['lip'],y=1849,pop=500,raw='“Texas Indians in 1849”: Lipan (Apache stock), 500 souls, 100 warriors',basis='souls',loc='inferred',at=(29.8,-100.0),r=250,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['wic'],y=1849,pop=1000,raw='“Texas Indians in 1849”: Waco, Wichita and Tawakoni (associates), 1,000 souls, 200 warriors',basis='souls',loc='inferred',at=(33.3,-98.3),r=200,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['kit'],y=1849,pop=300,raw='“Texas Indians in 1849”: Keechi, 300 souls, 60 warriors',basis='souls',loc='inferred',at=(32.8,-97.8),r=150,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['tkw'],y=1849,pop=650,raw='“Texas Indians in 1849”: Tonkawa, 650 souls, 130 warriors',basis='souls',loc='inferred',at=(31.5,-98.0),r=150,src=TIPV3('doc. No. 87, table (Neighbors, from Schoolcraft vol. 6, p. 708)'),kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1846.4,pop=14300,raw='Butler and Davis, 1846: Comanche or Na-u-ni, 14,300 (as tabulated by Schoolcraft beside Burnet 1847 and Neighbors 1849)',basis='souls',loc='inferred',at=(33.5,-99.8),r=400,src=TIPV3('doc. No. 100, table (Schoolcraft vol. 1, p. 518)'),kind='primary'),
 dict(g=['wic'],y=1846.4,pop=300,raw='Butler and Davis, 1846: Waco, Wichita and Tawakoni (associates), 300 (as tabulated by Schoolcraft)',basis='souls',loc='inferred',at=(33.3,-98.3),r=200,src=TIPV3('doc. No. 100, table (Schoolcraft vol. 1, p. 518)'),kind='primary'),
 dict(g=['lip'],y=1847.6,pop=800,raw='“They can now raise about 200 warriors of their own band” (the Lipan, apart from the Mescalero and “Seratick”)',basis='warriors × 4 (ours)',loc='inferred',at=(29.8,-100.0),r=250,src=TIPV3('doc. No. 78 (Burnet to Schoolcraft, 1847)'),kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1854.5,pop=10000,raw='Parker, “Census of the tribes of southwestern Texas in 1854”: Comanche, men, women, and children, 10,000',basis='souls',loc='inferred',at=(33.5,-99.8),r=400,src=TIPV3('doc. No. 131, table (Parker, from Schoolcraft vol. 5, p. 702)'),kind='primary'),
 dict(g=['wic'],y=1854.5,pop=708,raw='Parker, 1854: Waco—men 65, women 88, children 72, 205; Tawakoni—men 51, women 63, children 55, 189; Wichita—men 80, women 112, children 122, 314 (the Waco and Tawakoni items sum to 225 and 169; either way the three come to 708)',basis='souls',loc='inferred',at=(33.6,-98.4),r=150,src=TIPV3('doc. No. 131, table (Parker, from Schoolcraft vol. 5, p. 702)'),kind='primary'),
 dict(g=['kit'],y=1854.5,pop=360,raw='Parker, 1854: Keechi—men (no count of women and children), 100',basis='men × 3.6 (ours: Parker’s own ratio of persons to men for the Waco, Tawakoni and Wichita)',loc='inferred',at=(33.0,-98.5),r=150,src=TIPV3('doc. No. 131, table (Parker, from Schoolcraft vol. 5, p. 702)'),kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1870,pop=3742,raw='“In 1870, Agent Lawrie Tatum estimated 3,742 Comanches, including some 1,000 off-reservation Kwahadas (Tatum 1870); the Kwahada figure is probably an exageration”',basis='souls',loc='inferred',at=(34.7,-98.8),r=200,src='DeMallie, ed., Handbook of North American Indians, vol. 13: Plains (2001), Kavanagh, “Comanche”, p. 901',kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1875,pop=1721,raw='“In 1875, 1,556 Comanches were reported on the reservation south of the Washita, and another 165 Penatikas north of the river with the Wichitas”',basis='souls',loc='inferred',at=(34.7,-98.5),r=60,src='DeMallie, ed., Handbook of North American Indians, vol. 13: Plains (2001), Kavanagh, “Comanche”, p. 901',kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1878,pop=1475,raw='KCA agency census: Comanches, 1,475; Kiowas, 1,120; Apaches, 344',basis='souls',loc='stated',at=(34.7,-98.45),r=50,src=CIA(1878),kind='primary'),
 dict(g='kio',y=1878,pop=1120,raw='KCA agency census: Kiowas, 1,120',basis='souls',loc='inferred',at=(34.85,-98.6),r=50,src=CIA(1878),kind='primary'),
 dict(g='kap',y=1878,pop=344,raw='KCA agency census: Apaches, 344',basis='souls',loc='inferred',at=(35.0,-98.3),r=50,src=CIA(1878),kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1896,pop=1545,raw='November 1896: “the associated Comanche at the same time numbered 1,545”',basis='souls',loc='inferred',at=(34.7,-98.5),r=50,src=MOONEY,kind='primary'),
 dict(g=['cyy','cyk','cyp','cyn','cyq'],y=1900,pop=1499,raw='1900: 1,499',basis='souls',loc='inferred',at=(34.7,-98.5),r=50,src='Encyclopedia of the Great Plains, “Comanche” (Kavanagh)',kind='secondary'),
 dict(g=['cyy','cyk','cyp'],y=1816,pop=10000,raw='Smallpox, winter 1815–16: about 4,000 Comanche deaths (chief Chihuahua via Jameson, 1817); Thornton puts this against a population of about 10,000',basis='souls',loc='inferred',at=(34.0,-100.0),r=400,src='Brooks, Captives & Cousins; Thornton, American Indian Holocaust and Survival',kind='secondary'),
 # ---- Larocque, 1805: summer travel with the Crow ----
 dict(g=['cwm','cwr'],y=1805.5,pop=2580,raw='Crow camp of “more than 300 tipis” with 645 warriors, joined by 20 Shoshone tipis (Larocque, June–July 1805)',basis='warriors × 4',loc='stated',at=(47.4,-101.5),r=30,src='Larocque, journal of the expedition to the Yellowstone (1805), as summarized in Wikipedia',kind='primary'),
 dict(g='cwm',y=1805.49,pop=None,raw='June 29, 1805: the Crow camp leaves the Knife River with Larocque',basis='',loc='stated',at=(47.4,-101.6),r=20,src='Larocque (1805)',kind='primary'),
 dict(g='cwm',y=1805.57,pop=None,raw='July 27, 1805: tipis pitched on the Powder River',basis='',loc='stated',at=(45.6,-105.6),r=60,src='Larocque (1805)',kind='primary'),
 dict(g='cwm',y=1805.6,pop=None,raw='August 8, 1805: the longest stage, 24 miles, to the foot of the Bighorn Mountains',basis='',loc='stated',at=(44.9,-107.3),r=50,src='Larocque (1805)',kind='primary'),
 dict(g='cwm',y=1805.65,pop=None,raw='Late August 1805: camp near the mouth of the Bighorn Canyon',basis='',loc='stated',at=(45.3,-107.95),r=20,src='Larocque (1805)',kind='primary'),
 dict(g='cwm',y=1805.69,pop=None,raw='September 10, 1805: camp on a large island in the Yellowstone (47 camp moves since June 29)',basis='',loc='stated',at=(45.85,-108.3),r=40,src='Larocque (1805)',kind='primary'),
 # ---- Commissioner of Indian Affairs, agent reports ----
 dict(g=['sis','wpt'],y=1874,pop=1047,raw='“The Sissiton and Wahpeton Sioux, at Devil’s Lake… number 1,047, of whom 750 are permanent residents at the agency”',basis='souls',loc='stated',at=P['devils_lake'],r=30,src=CIA(1874),kind='primary',whole=False),
 dict(g='bru',y=1874,pop=7000,raw='“The Brule Sioux number 7,000”',basis='souls',loc='inferred',at=(42.8,-102.8),r=60,src=CIA(1874),kind='primary'),
 dict(g='cwm',y=1874,pop=3000,raw='“The Mountain and River Crows number respectively 3,000 and 1,200”',basis='souls',loc='inferred',at=(45.45,-109.5),r=60,src=CIA(1874),kind='primary'),
 dict(g='cwr',y=1874,pop=1200,raw='“…River Crows… 1,200”',basis='souls',loc='inferred',at=(48.0,-108.0),r=120,src=CIA(1874),kind='primary'),
 dict(g=['osg','osl'],y=1874,pop=2872,raw='“The population of the Osages, according to last enrollment, is 2,872; the actual number I believe to be over 3,000”',basis='souls',loc='stated',at=P['pawhuska'],r=40,src=CIA(1874),kind='primary'),
 dict(g='pon',y=1874,pop=730,raw='“aggregate a population of 730 persons, of whom 372 are males and 358 females”',basis='souls',loc='stated',at=P['ponca_ck'],r=20,src=CIA(1874),kind='primary'),
 dict(g='ass',y=1874,pop=1998,raw='Fort Peck agency estimate: Assinaboines 1,998',basis='souls',loc='stated',at=P['ft_peck'],r=60,src=CIA(1874),kind='primary'),
 dict(g='yku',y=1874,pop=2266,raw='Fort Peck agency estimate: Yanctonnai Sioux 2,266',basis='souls',loc='stated',at=(48.1,-105.0),r=60,src=CIA(1874),kind='primary',whole=False),
 dict(g='hnk',y=1874,pop=1420,raw='Fort Peck agency estimate: Uncpapa Sioux 1,420',basis='souls',loc='stated',at=(48.1,-105.4),r=60,src=CIA(1874),kind='primary',whole=False),
 dict(g='ykl',y=1874,pop=460,raw='Fort Peck agency estimate: Uncpatina Sioux 460',basis='souls',loc='stated',at=(48.1,-105.3),r=60,src=CIA(1874),kind='primary',whole=False),
 dict(g='sho',y=1874,pop=1041,raw='“The Shoshones numbered at the agency during the past year about 1,041 souls”',basis='souls',loc='stated',at=(43.0,-108.9),r=40,src=CIA(1874),kind='primary'),
 dict(g='hid',y=1878,pop=365,raw='Fort Berthold roll, 1,293: Gros Ventres [Hidatsa] 365, Mandans 273, Arickarees 654',basis='souls',loc='stated',at=P['like_fishhook'],r=15,src=CIA(1878),kind='primary'),
 dict(g='man',y=1878,pop=273,raw='Fort Berthold roll: Mandans 273',basis='souls',loc='stated',at=(47.58,-101.83),r=15,src=CIA(1878),kind='primary'),
 dict(g='ari',y=1878,pop=654,raw='Fort Berthold roll: Arickarees 654',basis='souls',loc='stated',at=(47.58,-101.87),r=15,src=CIA(1878),kind='primary'),
 dict(g='chn',y=1878,pop=970,raw='“Northern Cheyennes: this portion of the Cheyenne tribe numbers 970 people” (at the Cheyenne & Arapaho agency)',basis='souls',loc='stated',at=P['darlington'],r=30,src=CIA(1878),kind='primary',whole=False),
 dict(g='pon',y=1878,pop=631,raw='“The Poncas now number 631 people… a decrease of 45” (OCR reads “63J”)',basis='souls',loc='stated',at=P['ponca_ok'],r=40,src=CIA(1878),kind='primary'),
 dict(g='yku',y=1878,pop=3780,raw='Fort Peck: “3,780 Yanktonais and 1,615 Assinaboines”',basis='souls',loc='stated',at=(48.1,-105.0),r=80,src=CIA(1878),kind='primary',whole=False),
 dict(g='ass',y=1878,pop=1615,raw='Fort Peck: “…1,615 Assinaboines”',basis='souls',loc='stated',at=P['ft_peck'],r=80,src=CIA(1878),kind='primary'),
 dict(g='sho',y=1878,pop=1250,raw='“The Shoshones, Eastern band, number 1,250 souls”',basis='souls',loc='stated',at=(43.0,-108.9),r=40,src=CIA(1878),kind='primary'),
 dict(g='arn',y=1878,pop=938,raw='“The largest number… of the Arapahoes, 938” at the Shoshone agency',basis='souls',loc='stated',at=P['wind_res'],r=30,src=CIA(1878),kind='primary'),
 dict(g='ari',y=1882,pop=672,raw='Fort Berthold: “1,352, composed of Arickarees 672, Gros Ventres 454, Mandans 226”',basis='souls',loc='stated',at=(47.58,-101.87),r=15,src=CIA(1882),kind='primary'),
 dict(g='hid',y=1882,pop=454,raw='Fort Berthold: Gros Ventres [Hidatsa] 454',basis='souls',loc='stated',at=P['like_fishhook'],r=15,src=CIA(1882),kind='primary'),
 dict(g='man',y=1882,pop=226,raw='Fort Berthold: Mandans 226',basis='souls',loc='stated',at=(47.58,-101.83),r=15,src=CIA(1882),kind='primary'),
 dict(g=['osg','osl'],y=1882,pop=1950,raw='“The Osages number 1,950”',basis='souls',loc='stated',at=P['pawhuska'],r=40,src=CIA(1882),kind='primary'),
 dict(g=['cwm','cwr'],y=1882,pop=3500,raw='“The Crows are supposed to number about 3,500”',basis='souls',loc='inferred',at=(45.5,-108.5),r=100,src=CIA(1882),kind='primary'),
 dict(g='gv',y=1882,pop=950,raw='Fort Belknap census, spring 1882: Gros Ventres, 950',basis='souls',loc='stated',at=P['ft_belknap'],r=30,src=CIA(1882),kind='primary'),
 dict(g=['bru','ogl','min','hnk','sih','sna','twk','yku','ykl','mde','wpk'],y=1882,pop=23081,raw='“The total Indian population of the Great Sioux and Santee Reservations (including Crow Creek) is estimated at 23,081”',basis='souls',loc='inferred',at=(44.0,-100.8),r=250,src=CIA(1882),kind='primary'),
 dict(g='ykl',y=1886,pop=939,raw='Crow Creek census, June 30: 1,039 drawing rations, “of whom about 100 are Santees, Lower Brules, Yanktons, and half-breeds, the balance being Lower Yanktonnais”',basis='souls',loc='stated',at=P['crow_creek'],r=15,src=CIA(1886),kind='primary'),
 dict(g='bru',y=1886,pop=1235,raw='“At the census taken June 30 last these Lower Brulé Sioux numbered 1,235”',basis='souls',loc='stated',at=(44.07,-99.58),r=15,src=CIA(1886),kind='primary',whole=False),
 dict(g='kaw',y=1886,pop=203,raw='“The Kaws number 203, of which 152 are full and 51 are mixed bloods”',basis='souls',loc='stated',at=P['kaw_ok'],r=20,src=CIA(1886),kind='primary'),
 dict(g=['mde','wpk'],y=1886,pop=871,raw='“The population of Santee Agency is 871”',basis='souls',loc='stated',at=P['santee'],r=15,src=CIA(1886),kind='primary'),
 dict(g=['mde','wpk'],y=1867,pop=1350,raw='“When the Santees first came to this agency in 1867 they numbered 1,350”',basis='souls',loc='stated',at=P['santee'],r=15,src=CIA(1886)+' (agent’s retrospect)',kind='primary'),
 dict(g='kaw',y=1868,pop=620,raw='“In 1847 the Kansas or Kaw Indians numbered 1,500; their present number is 620”',basis='souls',loc='stated',at=P['council_grove'],r=30,src=CIA(1868),kind='primary'),
 dict(g='kaw',y=1847,pop=1500,raw='“In 1847 the Kansas or Kaw Indians numbered 1,500”',basis='souls',loc='inferred',at=P['council_grove'],r=50,src=CIA(1868)+' (retrospect)',kind='primary'),
 dict(g='sho',y=1868,pop=1800,raw='“This tribe numbers — Shoshones 1,800, Bannocks 600”',basis='souls',loc='inferred',at=(42.5,-109.5),r=150,src=CIA(1868),kind='primary'),
 dict(g='sho',y=1889,pop=930,raw='Shoshone agency census: males 495, females 435',basis='souls',loc='stated',at=(43.0,-108.9),r=30,src=CIA(1889),kind='primary'),
]

# Epidemics and famines: (start, end, label, {group: mortality fraction}, source, basis)
# basis: 'sourced' = fraction given by a cited source; 'scaled' = from a regional figure; 'assumed' = our judgment.
_ALL=lambda *gs: {g:None for g in gs}
LAKOTA=['bru','ogl','min','hnk','sih','sna','twk']
COM=['cyj','cyy','cyk','cyp','cyn','cyq']
EPI = [
 (1780.6,1782.0,'Smallpox, 1780–82',
   {**{g:.55 for g in ['ass','asn','cre','crw','sik','kai','pik','gv','sho']},
    **{g:.68 for g in ['man','hid','ari']}, 'cwm':.43,'cwr':.43,
    **{g:.2 for g in LAKOTA+['ynk','yku','ykl','chy','ara','kio','kap']}, 'cyp':.6, **{g:.3 for g in ['cyj','cyy','cyk']},
    **{g:.3 for g in ['pwc','pwk','pws','wic','jic']}, 'lip':.15, **{g:.15 for g in ['sis','wpt']},
    **{g:.2 for g in ['oma','pon','oto','mis','kaw','osg','osl','iow']}, **{g:.1 for g in ['mde','wpk']}},
   'Fenn, Pox Americana (2001), ch. 6 and epilogue, read in full. North: the traders put losses at 50–98%; Oman, counting the tents left, “about three fifths had perished”; Umfreville, “at least one half” of the plains Indians. Missouri villages: Lehmer’s overall 68% for the Mandan, Hidatsa and Arikara. Crow: Larocque’s 2,000 lodges before the smallpox against 2,400 people in 1805 (after 1801–02 as well); Fenn’s minimum is 21.5%. Sioux: Fenn’s minimum assumes a third infected at the 43% case-fatality rate (about 14%), lower than among the villages because nomads were less exposed and some were immune from 1734–35. Eastern Comanche: Vial and Chaves (1785) report two-thirds dead, which Fenn thinks may be too high. Lipan: “more than four hundred” dead (Cabello, Dec. 1780)','sourced for the north (55%), the Missouri villages (68%), the Lipan (15%, of about 2,900) and the eastern Comanche (60%); Crow at 43% (above Fenn’s minimum, as Larocque implies); the Sioux, Cheyenne, Arapaho, Kiowa and Plains Apache at 20%, just above Fenn’s minimum for the Sioux; the western Comanche at 30% (still 16,000–18,000 in the mid-1780s, Hämäläinen p. 102); the rest assumed'),
 (1801.3,1802.3,'Smallpox, 1801–02',
   {'oma':.6,'pon':.6,**{g:.45 for g in ['oto','mis','pwc','pwk','pws','ari','wic']},'kaw':.3,
    **{g:.25 for g in LAKOTA+['ynk','yku','ykl','man','hid']}, **{g:.2 for g in ['cyy','cyk','cyp','kio','kap','lip','osg','osl','osa','chy','ara','cwm','cwr']}},
   'Clark 1806 (Omaha from 700 warriors to “something less than 300”); Morse via Mooney (“prairie tribes… lost more than half,” Wichita and Caddo almost as severely)','sourced for the Omaha; scaled for the rest'),
 (1815.9,1816.7,'Smallpox, 1815–16',
   {'cyy':.4,'cyk':.4,'cyp':.4,'kio':.4,'kap':.4,'wic':.2,'lip':.2,'jic':.1},
   'Chihuahua via Jameson (about 4,000 Comanche dead; Thornton: of about 10,000); Mooney (the Kiowa suffered “in proportion”)','sourced for the Comanche; scaled for the Kiowa'),
 (1837.45,1838.0,'Smallpox, 1837–38 (Missouri)',
   {'man':.93,'hid':.5,'ari':.5,'ass':.6,'asn':.25,'sik':.67,'kai':.67,'pik':.67,'gv':.05,'cwm':.33,'cwr':.33,'pwc':.25,'pwk':.25,'pws':.25,
    **{g:.1 for g in LAKOTA+['ynk','yku','ykl','cre','crw','crs','ojb']},'hnk':.2},
   'Chardon & Pilcher (Mandan 7/8 or more); Denig (Assiniboine 1,000→400 lodges; HBC-vaccinated bands spared); Bradley (Blackfoot ≥6,000, two-thirds); Calloway (Arikara ½, Crow ⅓, Pawnee ¼); Fowler and Flannery, “Gros Ventre”, Handbook 13 (2001), p. 678 (the Gros Ventre “escaped the smallpox epidemic of 1837 with only 200 deaths”); DeMallie, “Sioux Until 1850”, Handbook 13 (2001), p. 734, after Denig (“a heavy toll on the population of the Hunkpapa and other Sioux along the Missouri”)','sourced, except the lighter Lakota, Cree and Gros Ventre figures (assumed)'),
 (1839.8,1840.4,'Smallpox, 1839–40 (southern plains)',
   {'kio':.25,'kap':.25,**{g:.2 for g in COM},'chs':.15,'ars':.15,'wic':.15,'osg':.1,'osl':.1},
   'Mooney (Kiowa calendar, winter 1839–40; “destroying probably a third”)','assumed below Mooney’s plains-wide third'),
 (1849.4,1849.8,'Cholera, 1849',
   {'kio':.2,'kap':.2,'chs':.45,'chn':.15,'ars':.3,**{g:.05 for g in COM},'pwc':.25,'pwk':.25,'pws':.25,'ogl':.08,'bru':.08,'wic':.15,'osg':.1,'osl':.1,'kaw':.1,'iow':.1},
   'Levy, “Kiowa”, Handbook 13 (2001), p. 921 (after Mooney’s “hundreds died”, and a Kiowa total never much above 1,200–1,350: “if as many as 200 or 300 died, the losses would have been between 13 and 20 percent”; the Kiowa tradition of losing half is set aside); Grinnell, The Cheyenne Indians (“perhaps half of the whole tribe died”); other tribes on the overland trails assumed; Swagerty, “History of the United States Plains Until 1850”, Handbook 13 (2001), p. 258 (“one-fourth of the remaining Pawnee”, after Powers and Leiker); West, The Contested Plains: Indians, Goldseekers, and the Rush to Colorado (1998), ch. 4 (the Southern Cheyenne “devastated”, the Flexed Leg band absorbed by others; soldiers on the Platte report “terrible losses” among the Northern Cheyenne and Lakota; the Pawnee agent reports 1,200 dead, “nearly one-fourth of the tribe”) and ch. 8 (cholera killed more than half of the Flexed Leg band, the Dog Soldiers losing only a few)','sourced for the Kiowa and Cheyenne (the north/south split is ours); assumed elsewhere'),
 (1861.9,1862.4,'Smallpox, 1861–62',
   {'kio':.15,'kap':.15,**{g:.4 for g in COM},'ari':.15,'man':.1,'hid':.1},
   'Mooney (Kiowa calendar; the Arikara abandoned their village because of it); for the Comanche, Hämäläinen, The Comanche Empire (2008), pp. 302, 313: smallpox “struck again” in 1862, “the seventeenth year of famine”, and with war on the New Mexico border “as many as four thousand Comanches may have perished during the early 1860s, leaving a total population of only five thousand in 1865”','assumed, except the Comanche (40%: Hämäläinen’s “as many as” four thousand of about nine thousand, smallpox, famine and war together)'),
 (1857.9,1858.3,'Smallpox, 1857–58 (Blackfoot)',
   {'sik':.1,'kai':.1,'pik':.1,'gv':.08},
   'Grinnell, Blackfoot Lodge Tales (1892), “The Blackfeet of To-day”: “small-pox again carried off great numbers, but the mortality was not to be compared with” the earlier epidemic','event sourced; fractions assumed'),
 (1864.5,1864.9,'Measles, 1864 (Blackfoot)',
   {'sik':.05,'kai':.05,'pik':.05},
   'Grinnell, Blackfoot Lodge Tales (1892), “The Blackfeet of To-day”: “measles ran through all the Blackfoot camps, and was very fatal”','event sourced; fractions assumed'),
 (1869.7,1870.3,'Smallpox, 1869–70',
   {'sik':.3,'kai':.3,'pik':.3,'gv':.25,'asn':.1,'cre':.15,'crw':.15,'crs':.15},
   'Grinnell, Blackfoot Lodge Tales (1892), “The Blackfeet of To-day” (“again in 1869 they had the small-pox”); fractions recalled from general histories of the northern plains','event sourced; fractions assumed'),
 (1883.8,1884.4,'Starvation winter, 1883–84',
   {'pik':.27},'Grinnell, Blackfoot Lodge Tales (1892), “The Blackfeet of To-day”: “more than a quarter of the Piegan tribe… which then numbered about twenty-five or twenty-six hundred, died from starvation”; 400–500 recorded burials at the agency alone','sourced'),
]

# =============================================================================================
# ADDITIONS (round 3): population series compiled by Swanton (1952) from the reports he cites.
SW = 'Swanton, The Indian Tribes of North America (BAE Bulletin 145, 1952)'
MOO28 = 'Mooney, “The Aboriginal Population of America North of Mexico” (1928), as given by '+SW
def sw(g,y,pop,raw,at,r=80,basis='souls',kind='primary',src=None,**o):
    return dict(g=g,y=y,pop=pop,raw=raw,basis=basis,loc='inferred',at=at,r=r,src=src or SW,kind=kind,**o)
LAK=['bru','ogl','min','hnk','sih','sna','twk']; SIOUX=LAK+['ynk','yku','ykl','mde','wpk','wpt','sis']
OBS += [
 # Mooney's 1780 reconstructions (secondary)
 sw(SIOUX,1780,25000,'“25,000 Dakota of all divisions, exclusive of the Assiniboin” in 1780',(45.0,-98.5),400,kind='secondary',src=MOO28),
 sw('ari',1780,3000,'About 3,000 Arikara in 1780',(44.9,-100.4),60,kind='secondary',src=MOO28),
 sw('hid',1780,2500,'Hidatsa and Amahami together 2,500 in 1780',P['knifeR'],30,kind='secondary',src=MOO28),
 sw('man',1780,3600,'3,600 Mandan in 1780',P['heartR'],30,kind='secondary',src=MOO28),
 sw('chy',1780,3500,'Cheyenne and Sutaio 3,500 in 1780',(45.6,-100.4),200,kind='secondary',src=MOO28),
 sw('oma',1780,2800,'About 2,800 Omaha in 1780',P['omaha_vil'],30,kind='secondary',src=MOO28),
 sw('oto',1780,900,'About 900 Oto in 1780',P['oto_vil'],40,kind='secondary',src=MOO28),
 sw('mis',1780,1000,'1,000 Missouri in 1780',(39.45,-93.4),60,kind='secondary',src=MOO28),
 sw(['pwc','pwk','pws'],1780,10000,'10,000 Pawnee in 1780',(41.3,-97.8),80,kind='secondary',src=MOO28),
 sw('pon',1780,800,'800 Ponca in 1780',P['ponca_ck'],40,kind='secondary',src=MOO28),
 sw('kaw',1780,3000,'3,000 Kansa in 1780',P['kaw_vil'],40,kind='secondary',src=MOO28),
 sw(['osg','osl'],1780,6200,'6,200 Osage in 1780',P['osage_vil'],60,kind='secondary',src=MOO28),
 sw('wic',1780,3200,'The confederated Wichita tribes about 3,200 in 1780',(34.2,-98.0),150,kind='secondary',src=MOO28),
 sw('ara',1780,3000,'3,000 Arapaho in 1780',(43.5,-104.0),250,kind='secondary',src=MOO28),
 sw('gv',1780,3000,'3,000 Atsina in 1780',(51.5,-108.5),250,kind='secondary',src=MOO28),
 sw(['ass','asn'],1780,10000,'10,000 Assiniboin in 1780',(50.0,-102.0),300,kind='secondary',src=MOO28),
 sw(['cwm','cwr'],1780,4000,'4,000 Crow in 1780',(45.5,-108.0),200,kind='secondary',src=MOO28),
 # Pawnee
 sw(['pwc','pwk','pws'],1838.5,10000,'1838: “about 10,000 according to an estimate of Dunbar and Allis… one authority places the figure as high as 12,500”',(41.35,-97.8),60),
 sw(['pwc','pwk','pws'],1849.9,4500,'1849: “after the cholera epidemic, they were reported at 4,500”',(41.35,-97.8),60),
 sw(['pwc','pwk','pws'],1856,4686,'1856: 4,686 returned',(41.35,-97.8),60),
 sw(['pwc','pwk','pws'],1861,3416,'1861: 3,416',P['genoa'],20),
 sw(['pwc','pwk','pws'],1879,1440,'1879: “after suffering severely in consequence of the removal to Indian Territory… 1,440”',P['pawnee_ok'],20),
 # Omaha
 sw('oma',1829,1900,'1829: 1,900',P['omaha_vil'],40),
 sw('oma',1848,1600,'1848: 1,600',(41.3,-95.95),40),
 sw('oma',1851,1349,'Schoolcraft: 1,349 in 1851',(41.3,-95.95),40),
 sw('oma',1857,1200,'Burrows: 1,200 in 1857',P['omaha_res'],20),
 sw('oma',1880,1200,'1,200 in the census returns for 1880',P['omaha_res'],20),
 # Iowa
 sw('iow',1760,1100,'An estimate of 1760: 1,100 souls',(41.5,-92.5),150,src=SW),
 sw('iow',1777,1000,'Cruzat, 1777: 250 warriors',(41.0,-92.5),150,basis='warriors × 4'),
 sw('iow',1829,1000,'1829: an estimate of 1,000',(40.4,-94.8),80),
 sw('iow',1832,1400,'Catlin, 1832: “one of the highest, 1,400”',(40.4,-94.8),80),
 sw('iow',1836,992,'1836: “an attempted census returned 992”',P['nemaha'],40),
 sw('iow',1843,470,'United States Indian Office, 1843: 470',P['nemaha'],30),
 sw('iow',1885,226,'1885: 138 in Kansas and 88 in Oklahoma',P['nemaha'],60),
 # Kansa
 sw('kaw',1815,1500,'1815: “supposed to be about 1,500 in all”',P['kaw_vil'],60),
 sw('kaw',1822,1850,'1822: 1,850',(39.1,-96.0),60),
 sw('kaw',1829,1200,'Porter, 1829: 1,200',(39.07,-95.9),40),
 sw('kaw',1843,1588,'United States Indian Office, 1843: 1,588',(39.07,-95.85),30),
 # Oto (with Missouria from 1829)
 sw('mis',1829,80,'1829, with the Oto: “they counted but 80”',P['oto_vil'],20),
 sw(['oto','mis'],1833,1300,'Catlin, 1833: 1,300, “a figure which includes the Missouri”',P['oto_vil'],30),
 sw('oto',1843,931,'United States Indian Office, 1843: 931 (Oto and Missouri)',(41.05,-95.95),30),
 sw('oto',1849,900,'Burrows, 1849: 900',(41.05,-95.95),30),
 sw('oto',1862,708,'1862: 708',P['big_blue'],20),
 sw('oto',1867,511,'1867: 511',P['big_blue'],20),
 sw('oto',1877,457,'1877: 457',P['big_blue'],20),
 sw('oto',1886,334,'1886: 334',P['oto_ok'],20),
 # Ponca
 sw('pon',1829,600,'1829: increased to 600',P['ponca_ck'],30),
 sw('pon',1842,800,'1842: about 800',P['ponca_ck'],30),
 sw('pon',1871,747,'1871: 747',P['ponca_ck'],20),
 # Osage
 sw(['osg','osl','osa'],1822,5200,'Morse (1822): an Osage population of 5,200',(37.5,-95.3),120),
 sw(['osg','osl','osa'],1829,5000,'Porter, 1829: 5,000',(37.5,-95.3),120),
 sw(['osg','osl'],1843,4102,'United States Indian Office, 1843: 4,102',(37.5,-95.3),100),
 # Mandan, Hidatsa
 sw('man',1850,150,'1850: “the total number was said to be 150”',P['like_fishhook'],10),
 sw('man',1852,385,'1852: “had apparently increased to 385”',P['like_fishhook'],10),
 sw('man',1871,450,'1871: 450',P['like_fishhook'],10),
 sw('man',1885,410,'1885: 410',P['like_fishhook'],10),
 sw('man',1905,249,'1905: 249',(47.6,-101.9),20),
 sw('hid',1905,471,'1905: 471',(47.6,-101.9),20),
 # Wichita confederacy
 # The 1772 Wichita count is De Mézières’s report itself, entered with the Bolton records (Wichita, Taovaya, Tawakoni and Iscani together).
 sw('wic',1868,572,'1868: 572 in the confederated tribes',P['anadarko'],30),
 # Crow, Assiniboine
 sw(['cwm','cwr'],1833,3400,'1833: “1,200 warriors and a population of from 3,250 to 3,560”',(45.8,-107.8),200),
 sw(['cwm','cwr'],1890,2287,'1890: 2,287',P['crow_ag'],30),
 sw(['cwm','cwr'],1904,1826,'1904: 1,826',P['crow_ag'],30),
 sw(['ass','asn'],1829,8000,'Porter, 1829: 8,000',(49.3,-104.0),300),
 sw(['ass','asn'],1836,10000,'Drake: “10,000 before the smallpox epidemic of 1836, when 4,000 died”',(49.3,-104.0),300,kind='secondary'),
 sw(['ass','asn'],1843,7000,'United States Indian Office, 1843: 7,000',(49.3,-104.0),300),
 # Sioux agencies, 1904
 sw('ogl',1904,6690,'Pine Ridge (Oglala), 6,690',P['pine_ridge'],30),
 sw('bru',1904,5447,'Rosebud (Brulé, Waglukhe, Lower Brulé, Northern, Two Kettle and Wazhazha), 4,977; Lower Brulé, 470',P['rosebud'],60),
 sw(['min','sna','twk'],1904,2477,'Cheyenne River (Miniconjou, Sans Arcs, and Oohenonpa), 2,477',P['chyR_agency'],30),
 sw(['hnk','sih','yku'],1904,3514,'Standing Rock (Sihasapa, Hunkpapa, and Yanktonai), 3,514',P['standing_rock'],30,whole=False),
 sw('ynk',1904,1702,'Yankton agency, 1,702',P['yankton_ag'],20),
 sw(['mde','wpk'],1904,2004,'Santee agency 1,075; Mdewakanton in Minnesota under no agency, 929',P['santee'],60),
 sw(['sis','wpt'],1904,1908,'Sisseton agency (Sisseton and Wahpeton), 1,908; others at Fort Totten',P['sisseton'],20,whole=False),
 sw('ykl',1904,1025,'Crow Creek (Lower Yanktonai), 1,025',P['crow_creek'],15),
 sw('jic',1905,795,'Jicarilla: 795 in 1905',(36.75,-107.0),30),
 dict(g='pik',y=1883.7,pop=2550,raw='The Piegan “then numbered about twenty-five or twenty-six hundred” (before the starvation winter)',basis='souls',loc='inferred',at=P['blackfeet_ag'],r=40,src='Grinnell, Blackfoot Lodge Tales (1892), “The Blackfeet of To-day”',kind='primary'),
 sw('jic',1845,800,'About 800 Jicarilla in 1845',(36.5,-105.5),100,kind='secondary',src=MOO28),
]

# =============================================================================================
# ADDITIONS (round 4): village moves and hunting places from Fletcher & La Flesche, Grinnell, Tixier, Maximilian.
FL = 'Fletcher & La Flesche, “The Omaha Tribe” (BAE 27th Annual Report, 1911)'
GRP = 'Grinnell, Pawnee Hero Stories and Folk-Tales (1889), “A Summer Hunt”'
def pl(g,y,raw,at,r,src,kind='primary',**o): return dict(g=g,y=y,pop=None,raw=raw,basis='',loc='stated',at=at,r=r,src=src,kind=kind,**o)
OBS += [
 pl('oma',1841.3,'Ton’wonzhinga, the Little Village, built on the Elkhorn near Clark Creek, Dodge County, in the spring of 1841 “on account of attacks by the Sioux”; occupied two years',(41.6,-96.55),8,FL+', p. 100'),
 pl('oma',1843.5,'After two years on the Elkhorn “the people went back to their old village on Omaha creek”',P['omaha_vil'],5,FL+', p. 100'),
 pl('oma',1847.3,'Village on Papillion Creek “about 8 miles west of the present town of Bellevue … built in 1847”; lived there until the 1854 sale',(41.15,-96.07),5,FL+', p. 100'),
 pl('oma',1856.5,'“Two years later they moved to their present reservation some 80 miles northward”',P['omaha_res'],10,FL+', p. 100'),
 pl('oma',1840.6,'Camp of Tenu’ganonpewathe attacked on Cedar Creek (T. 19 N., R. 8 W., 6th P.M.) in 1840 (summer hunt)',(41.61,-98.22),8,FL+', p. 99',seasonal=True),
 pl('oma',1846.95,'Camp “composed mostly of old men, women, and children” attacked by Yankton and Santee on 12 Dec. 1846 on the Missouri (Burt County); “all the other chiefs were on a buffalo hunt”; more than 80 killed',(41.78,-96.19),8,FL+', p. 100',seasonal=True),
 pl('oma',1852.55,'U’hontonga killed in a fight with the Oglala, T. 24 N., R. 17 W. (Loup County), 1852',(42.04,-99.24),8,FL+', p. 100',seasonal=True),
 pl('oma',1855.55,'Logan Fontenelle killed by Oglala while the tribe was moving on the summer hunt, Beaver Creek (T. 21 N., R. 7 W., Boone County), summer 1855',(41.78,-98.11),8,FL+', pp. 100–101',seasonal=True),
 dict(g=['pwc','pwk','pws'],y=1872.55,pop=4000,raw='July 1872: the summer hunt left the Loup village south, crossing the Platte and the Republican “about due south of … Kearney”, and camped on the Beaver; with a few Poncas, Omahas and Otoes “about four thousand Indians in the camp”',basis='souls (whole camp, includes visitors)',loc='stated',at=(40.05,-99.75),r=40,src=GRP+', pp. 270–76',kind='primary',whole=False,seasonal=True),
 pl(['pwc','pwk','pws'],1873.6,'Massacre Canyon, 5 Aug. 1873: a Pawnee summer-hunt camp of about 400 (Agent Williamson: about 700 left Genoa) attacked by Oglala, Brulé and Sihasapa; 156–171 killed',(40.206,-100.965),5,'Wikipedia, “Massacre Canyon”',kind='secondary',seasonal=True),
 pl(['osg','osl'],1840.55,'Tixier with the Osage summer hunt: beyond the Arkansas toward the Great Saline; “we arrived at our last camp toward July 20”; the summer hunt “begins during the early part of June and ends toward the middle of August”',(37.0,-97.9),120,'Tixier, Travels on the Osage Prairies (1840; ed. McDermott, 1940)',seasonal=True),
 pl('man',1833.9,'Winter 1833–34: the people of Mih-Tutta-Hang-Kush built “their winter village of sixty or seventy huts” in the forest “about a league below Fort Clarke”',(47.22,-101.25),4,'Maximilian, Travels in the Interior of North America, 1832–1834 (Thwaites ed., Early Western Travels 23–24)'),
]
EPI += [
 (1846.9,1847.0,'Attack on the Omaha winter camp, Dec. 1846',{'oma':.05},FL+', p. 100: “more than 80 persons were slain”','sourced (fraction of about 1,600)'),
 (1873.55,1873.65,'Massacre Canyon, Aug. 1873',{'pwc':.065,'pwk':.065,'pws':.065},'Wikipedia, “Massacre Canyon”: 156–171 Pawnee killed','sourced (fraction of about 2,400)'),
]

# =============================================================================================
# ADDITIONS (round 5): Thompson 1797–98, Pike 1806, Henry 1809, Long/Say 1819, Morse 1820, Catlin 1832–34 — read in the originals.
THOMPSON = 'David Thompson’s Narrative of His Explorations in Western America, 1784–1812, ed. Tyrrell (Champlain Society, 1916)'
PIKE = 'Pike, Expeditions, ed. Coues (1895), vol. 2'
HENRY2 = 'Alexander Henry the younger, journal 1809–10, in Coues ed., New Light on the Early History of the Greater Northwest (1897), vol. 2'
JAMES = 'James, Account of an Expedition from Pittsburgh to the Rocky Mountains… under Major S. H. Long (1823), vol. 1'
MORSE = 'Morse, Report to the Secretary of War… on Indian Affairs (1822), Appendix (figures from Maj. O’Fallon and Capt. Crooks, and Capt. Bell of Long’s party)'
CATLIN = 'Catlin, Letters and Notes on the Manners, Customs, and Condition of the North American Indians (1841), vol. 2'
def st(g,y,pop,raw,at,r,src,basis='souls',kind='primary',**o):
    return dict(g=g,y=y,pop=pop,raw=raw,basis=basis,loc='stated',at=at,r=r,src=src,kind=kind,**o)
OBS += [
 # Thompson at the Mandan and Hidatsa villages, Dec. 1797 – Jan. 1798: houses counted village by village
 st('man',1798.0,1520,'“This will give to the Mandanes for 190 houses, a population of 1520 souls; of which they may muster about 220 warriors” (eight to a house)',(47.15,-101.2),25,THOMPSON+', pp. 226–28','earth lodges × 8 (Thompson’s)'),
 st('hid',1798.0,1330,'“The Fall Indians of 128 houses, and seven tents have a population of 1330 souls, of which 190 are warriors” (ten to a house); upper village 31 houses and 7 tents, Great Village 82 houses on the Knife River',P['knifeR'],10,THOMPSON+', pp. 226–28','earth lodges × 10 (Thompson’s)'),
 pl('pik',1787.9,'Thompson winters with the Piegan: “Arrive at the Bow River. Cross it. Meet Peeagans… Lodge with an old man” (Saukamappee), winter 1787–88',(50.9,-114.0),80,THOMPSON+', p. 54 and ch. XXIII (pp. 345 ff.)'),
 # Pike, 1806
 st('osg',1806.65,1695,'Pike’s census of the Grand Osage village, Aug. 1806: “men, 502; boys, 341; women and girls, 852; total, 1695; lodges, 214”',P['osage_vil'],5,PIKE+', letter to Wilkinson, pp. 581–82','census'),
 sw('osl',1806.65,824,'Pike’s Statistical Abstract: Little Osage village 824 (250 warriors) — table read against its own totals (Osage 4,019; grand total 20,007)',(38.0,-94.25),20,src=PIKE+', pp. 590–91'),
 sw('osa',1806.65,1500,'Pike’s Statistical Abstract: Arkansas Osage village 1,500 (500 warriors)',(36.2,-95.4),60,src=PIKE+', pp. 590–91'),
 sw('kaw',1806.7,1565,'Pike’s Statistical Abstract: Kans 1,565 (465 warriors)',P['kaw_vil'],40,src=PIKE+', pp. 590–91'),
 sw(['pwc','pwk','pws'],1806.75,6223,'“The population of the three Pawnee villages was estimated by Capt. Pike, in 1806, at 6,223… 1,993 warriors”',P['grand_pawnee'],60,src=JAMES+', p. 445 (quoting Pike)'),
 sw(['cyy','cyk','cyp'],1806.5,8200,'Pike’s Statistical Abstract: Tetaus (Comanche) 8,200 souls, 2,700 warriors — hearsay at the Pawnee and Osage villages',(35.5,-101.0),400,kind='secondary',src=PIKE+', pp. 590–91'),
 # Henry the younger, Saskatchewan, 1809–10 (souls = his men-bearing-arms × 4, as for Umfreville)
 sw(['crw','crs'],1809.5,3600,'Plains Cree of the Saskatchewan, as seen from Fort Vermilion and Fort Augustus: “about 300 tents, which may furnish 900 men capable of bearing arms” (not including the Crees north of the Beaver River)',(52.8,-110.0),300,basis='warriors × 4',src=HENRY2+', p. 515'),
 sw(['ass','asn'],1809.5,8000,'Assiniboine census by bands: 850 tents, plus about 30 of the Swampy Ground Assiniboine; “these 880 tents might produce about 2,000 men capable of bearing arms”; 1,100 guns counted at a war rendezvous on the Missouri, summer 1809',(50.5,-104.5),400,basis='warriors × 4',src=HENRY2+', pp. 522–23'),
 sw('sik',1809.5,2080,'“120 Tents, Painted Feather’s band… 360 warriors; 80 [tents] Cold band… 160”',(51.5,-112.5),200,basis='warriors × 4',src=HENRY2+', p. 530'),
 sw('kai',1809.5,800,'“100 [tents] Bloods… 200 [warriors]”',(51.0,-112.8),200,basis='warriors × 4',src=HENRY2+', p. 530'),
 sw('pik',1809.5,2800,'“350 [tents] Piegans or Picaneaux… 700 [warriors]”; “the most numerous”',(50.5,-113.5),200,basis='warriors × 4',src=HENRY2+', p. 530'),
 sw('gv',1809.5,960,'Big Bellies (Atsina), between the South Branch and the Missouri: “about 80 tents, containing 240 men bearing arms”',(50.0,-110.0),250,basis='warriors × 4',src=HENRY2+', p. 531'),
 # Long's expedition, 1819–20, and Morse's figures for 1820
 pl('kaw',1819.6,'Say at the Kansa village: “about 120 lodges”, on a terrace about a quarter-mile from the Kansas River',P['kaw_vil'],8,JAMES+', p. 120 (Say’s notes)'),
 st(['oto','mis'],1820.5,1500,'Otoes and Missouris, “about 1,500 souls”, in one village on the Platte',P['oto_vil'],15,MORSE+', pp. 251–52'),
 st('oma',1820.5,2250,'O’Mahas 2,250; having “abandoned their old village”, now on the Elkhorn, about 80 miles WNW of Council Bluffs',(41.7,-97.0),40,MORSE+', pp. 251–52'),
 st('pon',1820.5,750,'Pancas 750, at the mouth of the Quicourre (Niobrara)',P['ponca_ck'],20,MORSE+', p. 252'),
 st('ari',1820.5,3500,'Arricaras 3,500; “lately removed some distance west, toward Cannon Ball river”',P['grandR'],80,MORSE+', p. 252'),
 sw('man',1820.5,1250,'Mandans 1,250',(47.3,-101.3),20,src=MORSE+', p. 252'),
 sw('hid',1820.5,3250,'Minetaries 3,250',P['knifeR'],20,src=MORSE+', p. 252'),
 sw(['cwm','cwr'],1820.5,3250,'Absorokas (Crows) 3,250',(45.6,-107.5),250,src=MORSE+', p. 253'),
 st('pwc',1820.5,5000,'Grand Pawnee village “about one hundred and sixty lodges” on the Loup fork (chief Long Hair); souls our share of the 10,000 by lodges; placed seven miles below the Skiri village at the Palmer site',(41.28,-98.10),10,MORSE+', pp. 237–38','earth lodges × 31 (Morse’s total ÷ lodges)',kind='secondary'),
 st('pwk',1820.5,1250,'Republican village, four miles above, “about forty lodges” (chief Fool Robe); “many of the young men of this band have joined the Grand Pawnees”; placed three miles below the Palmer site',(41.25,-98.18),10,MORSE+', pp. 237–38','earth lodges × 31 (Morse’s total ÷ lodges)',kind='secondary'),
 st('pws',1820.5,3750,'Pawnee Loups, three miles farther, 120 lodges (chief Old Knife); the Palmer site (Skiri village, “may have been documented by… Long in 1820”)',(41.22,-98.25),8,MORSE+', pp. 237–38','earth lodges × 31 (Morse’s total ÷ lodges)',kind='secondary'),
 # Catlin
 sw('chy',1832.5,3000,'“The Shiennes are a small tribe of about 3000 in numbers… between the Black Hills and the Rocky Mountains”',(44.0,-104.5),250,src=CATLIN+', Letter 32, p. 2'),
 sw('kaw',1832.5,1560,'“The Konzas, of 1560 souls… on the Konzas River, fifty miles above its union with the Missouri”',(39.1,-95.75),30,src=CATLIN+', Letter 34, p. 22'),
 sw(['osg','osl','osa'],1834.4,5200,'“The Osage… a tribe of about 5200 in numbers… in three villages”',(37.3,-95.3),80,src=CATLIN+', Letter 38, p. 40'),
 pl(['cyk','cyp'],1834.55,'The dragoons camp by “the great Camanchee village… of six or eight hundred skin-covered lodges”, July 1834',(34.75,-98.75),40,CATLIN+', Letter 42, p. 63'),
]

# =============================================================================================
# ADDITIONS (round 6): dated places. Sources read: Lewis & Clark journals (UNL), Grinnell's Fighting Cheyennes,
# Warren 1855–57, Stevens/Stanley 1853, Hayden, Catlin, Mooney; event sites geocoded from Wikipedia (coordinates as given there).
WARREN = 'Warren, Preliminary Report of Explorations in Nebraska and Dakota, in the Years 1855–’56–’57 (1875 reprint)'
GRF = 'Grinnell, The Fighting Cheyennes (1915)'
STEV = 'Stevens, Report of Explorations for a Route for the Pacific Railroad… from St. Paul to Puget Sound (Pacific Railroad Reports, vol. 1, 1855)'
LCJ = 'Lewis & Clark journals, ed. Moulton (UNL online edition)'
def WP(t): return f'Wikipedia, “{t}” (site coordinates and participants)'
REC = ''
RECS = ' (recalled; not checked against the text this round)'
def pls(gs,y,raw,at,r,src,**o): return [pl(g,y,raw,at,r,src,**o) for g in (gs if isinstance(gs,list) else [gs])]
OBS += [
 # ---- Lewis & Clark, 1804
 pl('ynk',1804.66,'Council with the Yankton “at the lower point of Calumet Bluff”, 30 Aug. 1804',(42.86,-97.48),15,LCJ+', entry for 30 Aug. 1804'),
 pl('bru',1804.73,'Council with the Teton band of Black Buffalo at the mouth of the Teton (Bad) River, 25 Sept. 1804; the people “came flocking in from both sides of the river”',P['badR_mouth'],15,LCJ+', entry for 25 Sept. 1804'),
 # ---- Warren's ranges, 1855–57 (pp. 47–50)
 pl('hnk',1856.5,'Unkpapas, 365 lodges: “roam from the Big Shyenne up to the Yellowstone, and west to the Black Hills”',(45.7,-102.6),250,WARREN+', p. 48'),
 pl('sih',1856.5,'Sihasapas, 165 lodges: “haunts and homes same as the Unkpapas”',(45.7,-102.6),250,WARREN+', p. 48'),
 pl('sna',1856.5,'Itazipchos (Sans Arc), about 170 lodges: “roam over nearly the same territory as the Unkpapas”',(45.4,-102.4),250,WARREN+', p. 48'),
 pl('min',1856.5,'Minikanyes, about 200 lodges: “roam principally from the Black Hills south to the Platte”',(43.2,-103.4),200,WARREN+', p. 48'),
 pl('ogl',1856.5,'Ogalalas, about 460 lodges: “generally to be found on or near the Platte near Fort Laramie”',(42.15,-104.2),100,WARREN+', p. 48'),
 pl('bru',1856.5,'Sichangus (Brulés), about 380 lodges: “live on the Niobrara and White Rivers, and range from the Platte to the Shyenne”',(43.1,-101.2),200,WARREN+', p. 48'),
 pl('twk',1856.5,'Oohenonpas (Two Kettles), about 100 lodges, “very much scattered among other bands… generally to be found in the neighborhood of Fort Pierre”',(44.4,-100.4),120,WARREN+', p. 48'),
 pl('ynk',1856.5,'Yanktons, 360 lodges: “at the mouth of the Big Sioux and between it and the Missouri River, as high up as Fort Lookout”',(43.2,-97.9),130,WARREN+', p. 47'),
 pl('yku',1856.5,'Yanktonais, about 800 lodges: “range between James River and the Missouri, as high north as Devil’s Lake”',(46.8,-99.2),200,WARREN+', p. 47'),
 pl('ass',1856.5,'Assiniboins, about 450 lodges: “their country extends from the Red River west along the Missouri as far as the mouth of the Milk River”',(48.3,-104.5),250,WARREN+', pp. 49–50'),
 pl('hid',1856.5,'Minnetarees: “a village of dirt lodges, surrounded by a rude stockade, near Fort Berthold… about 800 souls”',P['like_fishhook'],5,WARREN+', p. 50'),
 pl('ari',1856.5,'Arikaras: “live in a village near Fort Clark… about 840 souls”',P['ft_clark'],5,WARREN+', p. 50'),
 pl('man',1856.5,'Mandans: “live in a village, six miles above Fort Clark… about 250 souls” (July 1856)',(47.3,-101.35),5,WARREN+', p. 50'),
 pl('ari',1823.6,'Leavenworth’s attack on the two Arikara villages near the mouth of the Grand River, Aug. 1823',(45.55,-100.47),10,WP('Arikara War')+'; '+WARREN+', p. 50'),
 # ---- Hayden on the Blackfoot divisions (c. 1855–58)
 pl('kai',1856.5,'“The Blood Indians range through the district along Maria, Teton, and Belly Rivers”',(48.9,-112.4),150,HAYDEN+', p. 249'),
 pl('sik',1856.5,'“The Blackfeet inhabit a portion of country farther north than the Bloods, extending to the banks of the Saskatchewan”',(51.0,-112.2),200,HAYDEN+', p. 249'),
 pl('pik',1856.5,'“The Piegans roam… on the south side of Maria River, on both banks of the Missouri… as far down the Missouri as the Mussel-shell”',(47.8,-111.5),150,HAYDEN+', p. 249'),
 pl('pik',1853.7,'Stanley finds Low Horn’s Piegan camp of 90 lodges, “163 miles north, 20° west, of Fort Benton”, 14 Sept. 1853; Lame Bull’s 100 lodges had gone down the Milk River a week before',(49.9,-111.7),80,STEV+', pp. 447–48 (Stanley’s report)'),
 pl('pik',1855.79,'Lame Bull Treaty council at the mouth of the Judith, Oct. 1855: Piegan, Blood, Blackfoot and Gros Ventre camps',(47.73,-109.64),30,'Kappler, Indian Affairs: Laws and Treaties, vol. 2 (Treaty with the Blackfeet, 17 Oct. 1855)'+RECS),
 pl('gv',1855.79,'Lame Bull Treaty council at the mouth of the Judith, Oct. 1855',(47.73,-109.64),30,'Kappler, Indian Affairs: Laws and Treaties, vol. 2 (Treaty with the Blackfeet, 17 Oct. 1855)'+RECS),
 *pls(['kai','pik'],1870.82,'Battle of the Belly River: Cree and Assiniboine attack the Blood and Piegan camps on the Belly River, 25 Oct. 1870',(49.69,-112.86),20,WP('Battle of the Belly River')),
 pl('kai',1877.73,'Treaty 7 at Blackfoot Crossing, Sept. 1877; the Bloods under Red Crow present',(50.73,-112.95),15,WP('Treaty 7')),
 # ---- Fort Laramie (Horse Creek) council, Sept. 1851
 *pls(['ogl','bru','arn','chn'],1851.71,'Horse Creek (Fort Laramie) treaty council, Sept. 1851: about 10,000 people camped at the mouth of Horse Creek; Washakie’s Shoshone attended without signing'+'',(41.93,-104.0),25,WP('Treaty of Fort Laramie (1851)')+' (Shoshone attendance recalled)'),
 pl('bru',1854.63,'Grattan fight: the Brulé camp of Conquering Bear (with some Oglala and Miniconjou) east of Fort Laramie, 19 Aug. 1854',(42.13,-104.41),10,WP('Grattan massacre')),
 # ---- Cheyenne and Arapaho, from Grinnell
 pl('chs',1837.5,'“In 1837… the Cheyennes were camped on the South Platte River”',(40.5,-104.0),120,GRF+', p. 10'),
 *pls(['chs','ars'],1838.4,'The Cheyenne and Arapaho village moves south against the Kiowa and Comanche camp on Wolf Creek, 1838; “the Cheyennes and Arapahoes were camped together in one big circle”',(36.45,-99.55),50,GRF+', ch. V, pp. 42–56'),
 *pls(['chs','ars'],1840.6,'Great peace with the Kiowa and Comanche “at the mouth of the Two Butte Creek… about fifty miles below Bent’s Fort”, 1840',(38.03,-102.2),15,GRF+', pp. 62–66'),
 pl('chs',1857.575,'Sumner’s fight with the Cheyenne on the Solomon Fork, 29 July 1857 (date: West, The Contested Plains, ch. 1)',(39.35,-99.97),25,WP('Battle of Solomon’s Fork')),
 pl('chs',1864.0,'“A number of Cheyenne villages were camped on Ash Creek near Fort Larned all the winter” of 1863–64',(38.2,-99.25),25,GRF+', p. 120'),
 pl('chs',1864.4,'Summer 1864: the Cheyennes “now come together in one large camp on the Smoky Hill, while the Sioux were camped east of them on the Solomon”',(38.9,-100.2),80,GRF+', p. 138'),
 pl('chs',1865.08,'After Sand Creek: the combined village at the crossing of Lodgepole Creek; raids on the South Platte road around Julesburg, Jan.–Feb. 1865',(41.05,-102.55),40,GRF+', pp. 181–85'),
 *pls(['chn','ogl'],1865.2,'March 1865: the Southern Cheyennes join “the Northern Cheyennes, and the Ogallala Sioux under Old Man Afraid of His Horses, who were encamped on Powder River”',(44.4,-106.0),100,GRF+', pp. 193, 206'),
 pl('arn',1865.2,'Spring 1865: “the Northern Arapahoes near Tongue River, farther west”',(44.9,-107.0),100,GRF+', p. 193'),
 *pls(['ogl','min','chn','arn'],1866.97,'Dec. 1866: the Sioux, Cheyenne and Arapaho camps on Tongue River before the Fetterman fight',(44.85,-107.1),40,GRF+', p. 229'),
 pl('chs',1867.3,'Hancock’s march on the Cheyenne (and Sioux) village on Pawnee Fork, about 45 miles west of Fort Larned, April 1867',(38.25,-99.95),15,GRF+', p. 240'),
 pl('ars',1867.75,'Oct. 1867: “the Arapahoes, all of whom were camped on the Cimarron”',(36.9,-99.4),60,GRF+', p. 262'),
 pl('chs',1867.75,'Oct. 1867: “the Cheyenne camp was on Beaver Creek, a little below where Wolf Creek runs into it”, all the Dog Soldiers with it',(36.43,-99.5),20,GRF+', p. 262'),
 *pls(['chs','ars'],1868.9,'Nov. 1868: “a large number of Indians… camped on the Washita River, not very far from old Fort Cobb”; Black Kettle’s 75 lodges farthest west, then a large Cheyenne and Arapaho village, then Kiowa and Comanche',(35.55,-99.45),40,GRF+', p. 286'),
 pl('chn',1876.48,'The Northern Cheyenne in the great village on the Little Bighorn, 25 June 1876',(45.565,-107.429),10,WP('Battle of the Little Bighorn')),
 pl('chn',1876.9,'Dull Knife’s village on the Red Fork of Powder River, 25 Nov. 1876',(43.754,-106.950),10,WP('Dull Knife Fight')),
 pl('chn',1877.02,'Two Moon’s Cheyenne with Crazy Horse’s Oglala in winter camp on the Tongue River (Wolf Mountain), 8 Jan. 1877',(45.286,-106.581),15,WP('Battle of Wolf Mountain')),
 pl('ogl',1877.02,'Crazy Horse’s following in winter camp on the Tongue River (Wolf Mountain), 8 Jan. 1877; most Oglala were then at the Red Cloud agency',(45.286,-106.581),15,WP('Battle of Wolf Mountain'),whole=False),
 pl('ogl',1876.88,'Nov. 1876: “Crazy Horse, the Sioux, was camped on the Rosebud River, near the big bend”',(45.2,-106.9),40,GRF+', p. 348',whole=False),
 pl('arn',1874.5,'Bates fight: Black Coal’s Arapaho camp on the Nowood, July 1874',(43.542,-107.605),10,WP('Bates Battlefield')),
 # ---- Lakota and Dakota, 1862–76
 *pls(['hnk','min','sna','sih'],1876.48,'The great village on the Little Bighorn, 25 June 1876 (Hunkpapa, Miniconjou, Sans Arc, Sihasapa circles, with Oglala, Brulé and Cheyenne)',(45.565,-107.429),10,WP('Battle of the Little Bighorn')),
 pl('hnk',1876.8,'Sitting Bull’s Hunkpapa at Cedar Creek, 21 Oct. 1876',(47.515,-106.278),15,WP('Battle of Cedar Creek (1876)')),
 *pls(['hnk','sih','yku'],1864.57,'Killdeer Mountain: Lakota (Sitting Bull, Gall), Yanktonai and Santee village of about 1,600 lodges, 28 July 1864',(47.425,-102.918),15,WP('Battle of Killdeer Mountain')),
 pl('yku',1863.67,'Whitestone Hill: the Yanktonai (with some Santee, Hunkpapa and Sihasapa) village, 3 Sept. 1863',(46.17,-98.856),10,WP('Battle of Whitestone Hill')),
 *pls(['sis','wpt'],1863.56,'Big Mound: Standing Buffalo’s Sisseton and the Wahpeton camps on the Coteau, 24 July 1863',(47.024,-99.629),15,WP('Battle of Big Mound')),
 *pls(['mde','wpk'],1862.72,'Wood Lake, 23 Sept. 1862: Little Crow’s Mdewakanton and Wahpekute',(44.701,-95.436),10,WP('Battle of Wood Lake')),
 *pls(['sis','wpt'],1862.73,'Camp Release: the Wahpeton and Sisseton camp that held the captives, Sept. 1862',(44.933,-95.748),10,WP('Camp Release State Monument')),
 *pls(['mde','wpk'],1855.5,'Lower Sioux (Redwood) Agency for the Mdewakanton and Wahpekute, 1854–62',(44.526,-94.958),15,WP('Lower Sioux Agency')),
 *pls(['mde','wpk'],1861.5,'Lower Sioux (Redwood) Agency, 1854–62',(44.526,-94.958),15,WP('Lower Sioux Agency')),
 *pls(['sis','wpt'],1855.5,'Upper Sioux (Yellow Medicine) Agency for the Sisseton and Wahpeton, 1854–62',(44.735,-95.457),25,WP('Upper Sioux Agency')),
 *pls(['sis','wpt'],1861.5,'Upper Sioux (Yellow Medicine) Agency, 1854–62',(44.735,-95.457),25,WP('Upper Sioux Agency')),
 pl('wpt',1840.0,'Lac qui Parle: Wahpeton village and mission, 1835–54',(45.024,-95.868),15,WP('Lac qui Parle Mission')),
 # ---- Southern Plains
 *pls(['cyy','cyk','kap'],1853.55,'Treaty council at Fort Atkinson on the Arkansas with the Comanche, Kiowa and Apache, July 1853',(37.753,-100.083),20,WP('Fort Atkinson (Kansas)')+' (treaty of 27 July 1853 with the Apache, Comanche and Kiowa)'),
 *pls(['cyy','cyk','kap'],1854.55,'Whitfield: the Indians “encamped on Pawnee Fork, at the crossing of the Santa Fe Road… twelve to fifteen hundred lodges… The entire Kiowa and Prairie Comanche were there… the Prairie Apache”',(38.18,-99.2),20,GRF+', p. 98 (quoting Agent Whitfield)'),
 *pls(['ars','kap','cyp','cyy','cyn'],1867.8,'Medicine Lodge treaty council, Oct. 1867: Arapaho, Apache and Comanche (Ten Bears’ Yamparika, Silver Brooch’s Penateka, Horse Back’s Nokoni) camped on Medicine Lodge Creek',P['medicine_lodge'],15,WP('Medicine Lodge Treaty')+' (Comanche divisions recalled)'),
 pl('cyq',1858.36,'Little Robe Creek: Iron Jacket’s Comanche camp on the South Canadian, 12 May 1858',(35.973,-99.908),10,WP('Battle of Little Robe Creek')+'; '+WP('Iron Jacket')),
 *pls(['cyp','wic'],1858.75,'Van Dorn attacks Buffalo Hump’s Comanche camp at the Wichita village near Rush Springs, 1 Oct. 1858',(34.78,-97.96),10,'Van Dorn’s Wichita Village fight, 1 Oct. 1858'+RECS),
 pl('cyn',1860.96,'Pease River: a Nokoni camp, 19 Dec. 1860',(34.070,-99.595),10,WP('Battle of Pease River')),
 pl('cyq',1871.78,'Blanco Canyon: Quanah’s Kwahadi and Kotsoteka camp, Oct. 1871',(33.664,-101.176),15,WP('Battle of Blanco Canyon')),
 pl('cyk',1872.74,'North Fork of the Red River: Mow-way’s Kotsoteka village near McClellan Creek, 28 Sept. 1872',(35.412,-100.672),10,WP('Battle of the North Fork of the Red River')),
 *pls(['cyq','chs'],1874.74,'Palo Duro Canyon: Comanche, Kiowa and Cheyenne winter camps, 28 Sept. 1874',(34.878,-101.606),15,WP('Battle of Palo Duro Canyon')),
 pl('cyk',1779.67,'Anza defeats Cuerno Verde (“likely of the Kotsoteka”) near the Greenhorn Mountains, 3 Sept. 1779',(37.9,-105.0),40,WP('Cuerno Verde')),
 pl('wic',1759.8,'Parrilla’s attack on the Taovaya twin villages on the Red River, Oct. 1759',(33.952,-97.627),5,WP('Battle of the Twin Villages')),
 pl('wic',1834.55,'The Wichita (“Pawnee Pict”) village of “five or six hundred wigwams” of grass on the Red River among the granite mountains, July 1834',(34.89,-99.32),15,CATLIN+', Letter 43, pp. 68–69'),
 pl('wic',1865.0,'Wichita refugees at the mouth of the Little Arkansas, 1864–67',(37.69,-97.34),10,'Wichita refugee camp on the Little Arkansas'+RECS),
 pl('lip',1757.3,'Lipan gather at Mission Santa Cruz de San Sabá, 1757',(30.916,-99.735),20,WP('Mission Santa Cruz de San Sabá')),
 pl('lip',1763.0,'Lipan at the El Cañón missions on the upper Nueces, 1762–71',(29.67,-100.01),30,'Mission San Lorenzo de la Santa Cruz (El Cañón)'+RECS),
 pl('jic',1854.25,'Cieneguilla: Jicarilla camp near present Pilar, 30 March 1854',(36.27,-105.79),15,WP('Battle of Cieneguilla')),
 pl('jic',1887.5,'Jicarilla reservation established near Dulce, 1887',(36.93,-107.0),30,'Jicarilla reservation, executive order of 1887'+RECS),
 # ---- Village tribes and the northeast
 pl('mis',1750.0,'Utz site: “occupied by the Missouri tribe from c. 15th to the late 18th centuries… probably their principal village area during their first contact with Europeans”',(39.274,-93.25),5,WP('Utz Site')),
 pl('pon',1790.0,'Nanza (Ponca Fort): “a fortified village built by the Ponca… circa 1700 and occupied until about 1865”',(42.808,-98.164),5,WP('Ponca Fort')),
 pl('osl',1806.65,'Pike lodges in the Little Osage village, Aug. 1806, a few miles from the Grand village',(38.0,-94.25),8,PIKE+', pp. 391–92'),
 pl('iow',1810.0,'Ioway village on the lower Des Moines River (Iowaville), visitors to Fort Madison 1808–13',(40.88,-92.18),10,WP('Iowaville, Iowa')),
 st('kaw',1724.52,1500,'Bourgmont reaches “the main Kaw village on the Missouri near Doniphan” on 8 July 1724: “a large settlement, with at least 1,500 persons”',(39.64,-95.08),10,WP('Étienne de Veniard, Sieur de Bourgmont'),kind='secondary'),
]
# Kiowa Apache: “an integral part of the Kiowa tribal circle” at all tribal gatherings (Mooney, p. 228), so every sun dance place is theirs too
_kap=[]
for _o in list(OBS):
    if _o['g']=='kio' and _o['loc']=='stated' and not _o['pop'] and 'sun dance' in _o['raw'].lower():
        _kap.append(pl('kap',_o['y'],'At the Kiowa sun dance — '+_o['raw'],_o['at'],_o['r'],MOONEY+', p. 228 (the Apache “have formed an integral part of the Kiowa tribal circle”) and calendar entry'))
OBS += _kap

# ---- round 6b: eighteenth-century and other places from Wikipedia articles read in full
OBS += [
 pl('apc',1706.6,'Ulibarrí at El Cuartelejo, “the main village… on Ladder Creek”, 1706; at least five Cuartelejo rancherías',(38.678,-100.914),15,WP('El Cuartelejo')),
 pl('apc',1720.55,'The Villasur expedition passes through El Cuartelejo, 1720',(38.678,-100.914),30,WP('El Cuartelejo')),
 pl('apc',1724.8,'Bourgmont reaches the Padouca (Apache) village on the upper Little Arkansas, probably near Lyons, 18 Oct. 1724: 140 dwellings, “about 800 men, more than 1,500 women, and about 2,000 children”; the chief claimed twelve villages',(38.35,-98.2),25,WP('Étienne de Veniard, Sieur de Bourgmont')),
 pl('oto',1720.62,'Pawnee and Otoe attack Villasur’s camp just south of the Loup–Platte confluence near Columbus, 14 Aug. 1720',(41.42,-97.36),20,WP('Villasur expedition')),
 pl('pws',1720.62,'Pawnee and Otoe attack Villasur’s camp at the Loup–Platte confluence, 14 Aug. 1720 (the Loup villages were the Skiri’s; division ours)',(41.42,-97.36),30,WP('Villasur expedition')),
 pl('oto',1700.5,'“In 1700 they were, according to Le Sueur, on Blue Earth River near the Iowa”',(44.1,-94.1),50,SW),
 pl('iow',1760.0,'“About 1760 they moved east and came to live along the Mississippi between the Iowa and Des Moines Rivers”',(41.0,-91.4),70,SW),
 pl('mis',1714.0,'Bourgmont lives at “the Missouria village at the mouth of the Grand River”, from 1712',(39.33,-93.22),10,WP('Étienne de Veniard, Sieur de Bourgmont')+'; '+WP('Fort Orleans')),
 pl('mis',1723.9,'Fort Orleans built beside the Missouria village near the mouth of the Grand River, Nov. 1723',(39.33,-93.22),10,WP('Fort Orleans')),
 pl('mis',1790.0,'“Here, or in the immediate neighborhood, they remained until 1798, when they suffered a terrible defeat at the hands of the Sauk and Fox”',(39.33,-93.22),30,SW),
 pl('kaw',1750.0,'Fort de Cavagnial (1744–64), on the bluffs above Salt Creek north of Fort Leavenworth, “roughly in the same location as a major Kansa village”',(39.40,-94.93),15,WP('Fort de Cavagnial')+'; '+WP('Kaw people')),
 pl('kaw',1792.75,'Pedro Vial taken by the Kaw to “their village on the Kansas River”, 1792',P['kaw_vil'],30,WP('Pedro Vial')),
 *pls('kaw',1810.0,'“The primary village of the Kanza between about 1790 and 1828 was along the Kansas River near the confluence with the Big Blue”',P['kaw_vil'],10,WP('Kaw people')),
 pl('wic',1719.75,'Du Tisné finds “two likely Taovaya villages… near the present-day Neodesha, Kansas”, 1719',(37.42,-95.68),20,WP('Taovaya')),
 st('wic',1719.7,6000,'Lasley Vore site on the Arkansas in Tulsa County: “a Wichita village of about 6,000 people, as described by… La Harpe” in 1719',(35.97,-95.97),15,WP('Lasley Vore Site'),kind='secondary'),
 pl('wic',1750.0,'Deer Creek and Bryson-Paddock: “18th century fortified villages of the Wichita… along the Arkansas River in Kay County”',(36.84,-97.10),15,WP('Deer Creek/Bryson Paddock Sites')),
 pl('wic',1778.0,'“In 1778, the Taovaya village at Spanish Fort had 123 houses and across the Red River a Wichita town had another 37 houses”',(33.952,-97.627),5,WP('Taovaya')),
 pl('wic',1785.6,'Vial and Chaves reach the twin Taovaya villages near Spanish Fort, 6 Aug. 1785',(33.952,-97.627),5,WP('Pedro Vial')),
 pl('cyk',1785.65,'The Taovaya take Vial to “the various bands of the Eastern Comanche (Cuchanees or Kotsoteka) on the Little Wichita River near… Wichita Falls”, Aug. 1785',(33.85,-98.55),40,WP('Pedro Vial')),
 pl('cyk',1787.1,'Vial winters “among the Comanche near Wichita Falls”, 1786–87',(33.9,-98.5),50,WP('Pedro Vial')),
 pl('pwk',1806.75,'Pike-Pawnee (Hill) site near Guide Rock: the Kitkehahki village visited by Melgares and then Pike in 1806',(40.07,-98.33),5,WP('Pike-Pawnee Village Site')),
 pl('pwk',1790.0,'Hill site: “a village of the Kitkehahki band… in a region of the Republican River valley that they occupied intermittently from the 1770s to the 1820s”',(40.07,-98.33),20,WP('Pike-Pawnee Village Site')),
 pl('oma',1734.0,'“Around 1734 the Omaha established their first village west of the Missouri River on Bow Creek in present-day Cedar County, Nebraska”',(42.72,-97.2),15,WP('Omaha people')),
 pl('oma',1775.0,'“Around 1775 the Omaha developed a new village, probably located near present-day Homer, Nebraska” (Big Village)',P['omaha_vil'],8,WP('Omaha people')),
 pl('ari',1743.25,'“An Arikara village, near where present-day Pierre, South Dakota developed, was visited in 1743 by two sons of… La Vérendrye”',(44.37,-100.35),15,WP('Arikara')),
 pl('osa',1804.5,'Lewis and Clark: “the Arkansas band on the Verdigris River”',(36.3,-95.6),40,WP('Osage Nation')),
 pl('pon',1789.0,'Munier licensed “to trade with the Ponca at the mouth of the Niobrara River”, 1789',(42.77,-98.05),10,WP('Ponca')),
 *pls('sho',1863.5,'Fort Bridger treaty negotiations with Washakie’s Eastern Shoshone, 1863',(41.32,-110.39),20,WP('Eastern Shoshone')),
 *pls('sho',1868.5,'Fort Bridger treaty, 1868; Washakie’s Eastern Shoshone assigned the Wind River reservation',(41.32,-110.39),20,WP('Eastern Shoshone')),
 pl('cyq',1875.4,'“In May 1875, the last free band of Comanches, led by… Quanah Parker, surrendered and moved to the Fort Sill reservation”',P['ft_sill'],10,WP('Comanche')),
]

# ---- round 6c
H1 = 'Alexander Henry the younger, journal of the Pembina River post, in Coues ed., New Light… (1897), vol. 1'
OBS += [
 pl('ass',1809.5,'Henry’s southern Assiniboine bands: Little Girl (Souris, Moose Hills, Tête à la Biche), Paddling and Foot (Qu’Appelle lakes to the Missouri), Canoe, Red River and Rabbit — 614 tents; centre of their stated ranges',(50.1,-103.3),250,HENRY2+', pp. 522–23'),
 pl('asn',1809.5,'Henry’s Saskatchewan Assiniboine bands: Rocky (Thunder Hill), Water-for-Themselves (Skunk Hills), Eagle Hills, Saskatchewan (South Branch), Foot (west of Eagle Hills), Strong Wood (Battle River) — 236 tents; centre of their stated ranges',(52.3,-108.4),200,HENRY2+', pp. 522–23'),
 pl('gv',1809.5,'Henry: the Big Bellies (Atsina) “are now stationed S. of the Slaves, between the South Branch and the Missouri”',(49.6,-110.0),250,HENRY2+', p. 530'),
 pl('gv',1869.0,'Fort Browning, the trading post and agency for the Gros Ventre (and Assiniboine) near the mouth of Peoples Creek on the Milk River, 1868–71',P['milk_mid'],20,WP('Gros Ventre')),
 pl('ojb',1802.7,'Henry returns to his Pembina River post, Sept. 1802: “60 Saulteurs camped at my fort”',P['pembina'],15,H1+', p. 203'),
 pl('ojb',1806.4,'The Saulteur camp of “nine large cabins” at the forks of the Scratching River, 1806',(49.35,-97.4),15,H1+', p. 286'),
 pl('ojb',1808.6,'Aug. 1808: “I arrived at Panbian river, where I found a number of Saulteurs camped at the fort”',P['pembina'],15,H1+', p. 420'),
 pl('oto',1820.5,'Otoes and Missouris “in one village on the Platte”, 1820',P['oto_vil'],15,MORSE+', pp. 251–52'),
 pl('mis',1820.5,'The Missouris living with the Otoes in their village on the Platte, 1820',P['oto_vil'],15,MORSE+', pp. 251–52'),
 pl('cyj',1787.6,'July 1787: at Paruanarimuca’s request Anza sends a master builder and thirty laborers to build adobe houses and corrals for the Jupes “on the upper Arkansas River near the Rocky Mountains” (San Carlos de los Jupes, near present Pueblo; site after Thomas 1929)',(38.27,-104.6),20,'Hämäläinen, The Comanche Empire (2008), pp. 126–27'),
]
CROWWP = WP('Crow people')+' (chronology)'
OBS += [
 pl('cwr',1825.6,'“The Crows put up 300 tipis near a Mandan village on the Missouri in 1825” (a trading visit, kept off the division track)',(47.3,-101.3),20,CROWWP,seasonal=True),
 pl('cwm',1840.5,'“In the summer of 1840, a Crow camp in the Bighorn valley greeted the Jesuit missionary Pierre-Jean De Smet”',(45.3,-107.9),80,CROWWP),
 pl('cwr',1845.5,'“The River Crows charged a moving Blackfeet camp near Judith Gap in 1845”',(46.68,-109.75),60,CROWWP),
 pl('cwr',1858.5,'“From 1857 to 1860, many Crow traded their surplus robes… at Fort Sarpy (II) near the mouth of the Bighorn River”',P['bighorn_mouth'],40,CROWWP),
 pl('cwm',1870.5,'Summer 1870: Sioux attack “a Crow reservation camp in the Bighorn/Little Bighorn area”',(45.4,-107.6),50,CROWWP),
 pl('cwm',1873.6,'Aug. 1873: a Crow reservation camp at Pryor Creek, with visiting Nez Perce, faces a Sioux war party',(45.6,-108.3),25,CROWWP),
 *pls(['cwm','cwr'],1878.4,'“In the spring of 1878, 700 Crow tipis were pitched at the confluence of Bighorn River and Yellowstone River”',P['bighorn_mouth'],15,CROWWP),
]
OBS += [
 pl('arn',1869.0,'“In 1868–69, the Arapaho briefly sought to locate with… the Gros Ventres at the agency on the Milk River in Montana, but left after a smallpox epidemic”',P['milk_mid'],80,WP('Northern Arapaho')),
 pl('arn',1870.4,'“The Arapaho briefly stayed in the Wind River valley in 1870, but left after miners and Shoshones attacked… as they moved lodges”',(43.0,-108.6),50,WP('Northern Arapaho')),
 pl('arn',1878.9,'“In the winter of 1878–79, the United States Army escorted the Northern Arapaho to the Sweetwater Valley near Independence Rock”',(42.49,-107.13),25,WP('Northern Arapaho')),
]

# =============================================================================================
# ADDITIONS (round 7): agency-era places from the Indian Office reports, plus Maximilian, Thompson and site articles.
def CIAL(y,doc): return f'Annual Report of the Commissioner of Indian Affairs, {y}, agent’s report{doc}'
C74 = 'Annual Report of the Commissioner of Indian Affairs, 1874, Commissioner’s summary of agencies'
MAX = 'Maximilian, Travels in the Interior of North America, 1832–1834, in Thwaites ed., Early Western Travels'
LT = (45.61,-97.14); SPT74=(42.85,-102.85); RC74=(42.68,-103.45); PECK74=(48.0,-106.45)
def agl(gs,y,raw,at,r,src): return pls(gs,y,raw,at,r,src)
OBS += [
 # ---- 1868 agents' reports (document numbers as printed)
 *agl('ynk',1868.68,'Yancton Agency, Dakota Territory, 7 Sept. 1868',P['yankton_ag'],25,CIAL(1868,', no. 40')),
 *agl('pon',1868.71,'Ponca Agency, Dakota Territory, 16 Sept. 1868',P['ponca_ck'],15,CIAL(1868,', no. 41')),
 *agl('ykl',1868.71,'Crow Creek Agency (Upper Missouri Sioux agency), 16 Sept. 1868',P['crow_creek'],25,CIAL(1868,', no. 42')),
 *agl(['ari','hid','man'],1868.75,'Fort Berthold Agency, 30 Sept. 1868',P['like_fishhook'],10,CIAL(1868,', no. 43')),
 *agl(['sis','wpt'],1868.83,'Lake Traverse Agency, 31 Oct. 1868: the Sisseton and Wahpeton “located on reservations designated at Lake Traverse and at Devil’s lake”, with others about Forts Wadsworth, Ransom, Totten and Abercrombie',LT,120,CIAL(1868,', no. 44')),
 *agl('iow',1868.65,'Great Nemaha Agency, Nohart, Nebraska, 24 Aug. 1868',P['nemaha'],15,CIAL(1868,', no. 55')),
 *agl(['pwc','pwk','pws'],1868.63,'Pawnee Indian Agency, Genoa, Nebraska, 20 Aug. 1868',P['genoa'],15,CIAL(1868,', no. 57')),
 *agl('oma',1868.5,'Omaha Indian Agency, Nebraska, 1 July 1868',P['omaha_res'],15,CIAL(1868,', no. 61')),
 *agl('oto',1868.62,'Otoe Missouri Agency, 15 Aug. 1868',P['big_blue'],15,CIAL(1868,', no. 63')),
 *agl(['mde','wpk'],1868.67,'Santee Agency, Nebraska, 1 Sept. 1868',P['santee'],15,CIAL(1868,', no. 64')),
 *agl('bru',1868.6,'Upper Platte Agency, North Platte, 22 Aug. 1868: the Indians “engaged in hunting on the south side of the South Platte river… only visiting the agency when they wished supplies”',(40.8,-100.8),120,CIAL(1868,', no. 66')),
 *agl('kaw',1868.69,'Kaw Indian Agency, Council Grove, Kansas, 10 Sept. 1868',P['council_grove'],15,CIAL(1868,', no. 70')),
 *agl(['osg','osl'],1868.69,'Neosho Agency, 8 Sept. 1868 (the Osage reservation in southern Kansas; the hunt that winter was driven off the plains by the Arapaho)',(37.4,-95.4),60,CIAL(1868,', no. 78')),
 *agl('wic',1868.75,'Wichita Agency, 1 Oct. 1868: the Indians “all removed from their temporary home on the Arkansas river to their old home on the Washita, in the vicinity of old Fort Cobb”',(35.1,-98.42),15,CIAL(1868,', no. 87')),
 *agl('sho',1868.7,'Fort Bridger Agency, 12 Sept. 1868',(41.32,-110.39),40,CIAL(1868,', no. 30')),
 *agl('jic',1868.64,'Cimarron Agency, New Mexico, 21 Aug. 1868, for the Moache Ute and Jicarilla Apache',(36.51,-104.92),20,CIAL(1868,', no. 34')),
 # ---- 1874: the Commissioner's summary gives each agency's location
 *agl('ynk',1874.7,'“The Yankton Sioux have a reservation of 400,000 acres in the south part of Dakota, fifty miles from Yankton”',P['yankton_ag'],25,C74+', p. 42'),
 *agl(['sis','wpt'],1874.7,'“The Sissiton and Wahpeton band of Sioux, on Lake Traverse Reservation… now number 1,677”',LT,40,C74+', p. 40'),
 *agl(['hnk','yku','ykl','sih'],1874.7,'Standing Rock: “the Upper and Lower Yanctonnais… 1,406 and 2,607… with 1,556 Uncpapas and 871 Blackfeet, are located on the Missouri River, about one hundred miles nearly due south from Bismarck, to which place the agency was removed last year from Grand River” (1,200 Lower Yanktonai also at Crow Creek)',P['standing_rock'],30,C74+', p. 43'),
 *agl(['twk','min','sna'],1874.7,'“The Two-Kettle, Minneconjou, Sans Arc, and Blackfeet bands of Sioux, numbering in all 4,982, have an agency on the west side of the Missouri, near the mouth of Cheyenne River”',P['chyR_agency'],40,C74+', pp. 43–44'),
 *agl('ogl',1874.7,'Red Cloud Agency “is located on White River, to which it was removed in August, 1873”',RC74,15,C74+', p. 45'),
 *agl('arn',1874.7,'Red Cloud Agency on the White River, the agency for the Oglala, Northern Cheyenne and Arapaho, 1871–78',RC74,30,C74+', p. 45; '+WP('Red Cloud Agency')),
 *agl('bru',1874.7,'Spotted Tail Agency, “removed during the year twelve miles… ten miles south of the Nebraska line”',SPT74,20,C74+', p. 46'),
 *agl('pon',1874.7,'“The Poncas… near the junction of the Missouri and Niobrara Rivers… gathered for mutual protection into three villages not over ten miles apart”',P['ponca_ck'],12,C74+', p. 47'),
 *agl(['ari','hid','man'],1874.7,'Fort Berthold: “the Arickarees, numbering 975, the Gros Ventres, numbering 620, and the Mandans, numbering 420”',P['like_fishhook'],15,C74+', p. 48'),
 *agl('ass',1874.7,'1,998 Assiniboine at the Fort Peck agency, “on the north bank of the Missouri… one hundred and fifty miles by land west of Fort Buford”, and 1,700 Upper Assiniboine at Fort Belknap; centre of the two',(48.25,-107.6),150,C74+', p. 50'),
 *agl('gv',1874.7,'“A special agency for 960 Gros Ventres and 1,700 Upper Assinaboines was established in July, 1873… at Fort Belknap”',P['ft_belknap'],20,C74+', p. 50'),
 *agl('sho',1874.7,'Shoshone Agency, Wind River valley: “an agency was established” in the fall of 1870',P['wind_res'],30,C74+', p. 52'),
 *agl(['osg','osl'],1874.7,'“The Osages… are on a reservation… bounded by the State line of Kansas, the ninety-sixth meridian, and the Arkansas River”',(36.7,-96.4),50,C74+', p. 66'),
 *agl('kaw',1874.7,'Osage and Kaw agencies consolidated; the Kaw on their new reservation in the Indian Territory',P['kaw_ok'],15,C74+', p. 66'),
 *agl(['wic','cyp'],1874.7,'Wichita Agency: “the affiliated bands of Caddoes, Wichitas, Tawacanies, Keechies, Penetethka Comanches, with 300 Pawnees, numbering in all 1,897”',P['anadarko'],25,C74+', p. 71'),
 *agl(['pwc','pwk','pws'],1874.6,'“The Pawnees, 1,788 in number, are on a reservation on the South Branch of the Platte [the Loup]… a little east of the center of the State”',P['genoa'],15,C74+', p. 35'),
 *agl('oma',1874.7,'“The Omahas are located on a reservation in the eastern part of Nebraska, on the Missouri River”',P['omaha_res'],15,C74+', p. 62'),
 *agl('iow',1874.7,'“The Iowas, numbering 226… in the southeastern corner of Nebraska”',P['nemaha'],15,C74+', p. 62'),
 *agl('oto',1874.7,'“The confederated tribes of Otoes and Missourias, 453 in number, have a reservation on the southern boundary of Nebraska”',P['big_blue'],15,C74+', p. 34'),
 *agl(['mde','wpk'],1874.7,'“The Santee Sioux, 791 in number, are located in Northern Nebraska, on the Missouri River”',P['santee'],15,C74+', p. 36'),
 *agl('jic',1874.7,'Cimarron Indian Agency, New Mexico, 1874',(36.51,-104.92),20,CIAL(1874,', Cimarron Indian Agency, p. 305')),
 # ---- 1878 agents' reports
 *agl(['chs','ars'],1878.65,'Cheyenne and Arapahoe Agency, Indian Territory, 25 Aug. 1878',(35.55,-98.0),40,CIAL(1878,', Cheyenne and Arapahoe Agency')),
 *agl(['kio','kap','cyy','cyk','cyn','cyq'],1878.62,'Kiowa and Comanche Agency, Indian Territory, 15 Aug. 1878',P['ft_sill'],40,CIAL(1878,', Kiowa and Comanche Agency')),
 *agl('wic',1878.66,'Wichita Agency, Indian Territory, 31 Aug. 1878',P['anadarko'],20,CIAL(1878,', Wichita Agency')),
 *agl(['pwc','pwk','pws'],1878.61,'Pawnee Agency, Indian Territory, 12 Aug. 1878',P['pawnee_ok'],15,CIAL(1878,', Pawnee Agency')),
 *agl(['twk','min','sna'],1878.62,'Cheyenne River Agency, Dakota, 14 Aug. 1878',P['chyR_agency'],40,CIAL(1878,', Cheyenne River Agency')),
 *agl('ynk',1878.65,'Yankton Agency, Dakota, 26 Aug. 1878',P['yankton_ag'],25,CIAL(1878,', Yankton Agency')),
 *agl('ass',1878.63,'Fort Peck Indian Agency, Poplar River, Montana, 17 Aug. 1878',P['ft_peck'],60,CIAL(1878,', Fort Peck Agency')),
 # ---- sites and Bent's Fort
 *pls('chy',1735.0,'Biesterfeldt site on the Sheyenne River near Lisbon, North Dakota: “an independent group of Cheyennes is believed to have occupied it c. 1724–1780”',(46.42,-97.67),15,WP('Biesterfeldt Site')),
 *pls('chy',1765.0,'Biesterfeldt site, occupied c. 1724–1780',(46.42,-97.67),15,WP('Biesterfeldt Site')),
 *pls('hid',1760.0,'Big Hidatsa village, “occupied between ca. 1740 and 1850”, Knife River',(47.339,-101.382),5,WP('Big Hidatsa Village Site')),
 *pls(['chs','ars'],1834.0,'Bent’s Fort, built in 1833 “to trade with Southern Cheyenne and Arapaho”',(38.04,-103.43),60,WP('Bent’s Old Fort National Historic Site')),
 # ---- Maximilian, 1833–34
 pl('yku',1833.46,'June 1833, between the Heart River and Fort Clark: a party from “a camp of the Yanktonans, consisting of 300 tents, which was in the neighbourhood; they generally lived on the banks of the Chayenne… near the Devil’s Lake”',(47.0,-100.9),40,MAX+', vol. 22, p. 315'),
 pl('cwm',1833.47,'Fort Clark, June 1833: “seventy leather tents of the Crows” of Eripuass (Rotten Belly), whose nation “consisting of 400 tents” was on the Missouri to trade (a trading visit, kept off the division track)',P['ft_clark'],150,MAX+', vol. 22, pp. 323–28',seasonal=True),
 pl('gv',1833.6,'Aug. 1833: the Gros Ventres des Prairies meet the keelboat on the Missouri just above the Judith; later they camp about Fort McKenzie',(47.75,-109.9),40,MAX+', vol. 23, pp. 49–58, 131–33'),
 pl('pik',1833.6,'Fort McKenzie, July–Sept. 1833: “150 tents of the Piekanns” at the fort, the rest on the Marias; on 30 Aug. “the great Indian camp, consisting of about 400 tents”',(47.83,-110.6),20,MAX+', vol. 23, pp. 34, 82, 121'),
 pl('sik',1833.62,'Aug. 1833: “a numerous body of Blackfeet of 250 tents, which he had left on the Muscleshell River” (which Blackfoot division is not said; kept off the Siksika track)',(46.9,-108.6),120,MAX+', vol. 23, p. 109',whole=False),
 pl('pon',1834.35,'May 1834: “the village of these Indians, consisting of nearly 100 tents, was about four days’ journey up L’Eau qui Court”',(42.75,-99.3),50,MAX+', vol. 24, p. 74'),
 # ---- Thompson
 pl('ass',1797.93,'Dec. 1797, on the Souris: “five Tents of Stone Indians”, then “eight tents of Stone Indians”',P['souris'],80,THOMPSON+', pp. 212–14'),
 pl('ass',1798.08,'1 Feb. 1798: “eight Tents of Stone Indians, in the same place as [when] we went”',P['souris'],80,THOMPSON+', p. 240'),
 pl('sho',1730.0,'Saukamappee’s youth (about 1730): “a large camp of the Snake Indians on the Plains of the Eagle Hill”; date from his age, place from Thompson’s gloss; a war-season camp at the northern reach of Shoshone raiding, dated only by the narrator’s age (kept off the division track, which would otherwise put the Shoshone north of every Blackfoot division)',(52.2,-109.0),200,THOMPSON+', pp. 328–29',whole=False),
 pl('pws',1820.4,'The Palmer site, the Skiri village “documented by an American exploratory expedition led by Stephen H. Long in 1820”; 120 lodge sites',(41.22,-98.25),8,WP('Palmer Site')),
]
RUSSELL = 'Osborne Russell, Journal of a Trapper, 1834–1843 (1914; 1921 ed.)'
LCM = LCJ+', with Moulton’s notes'
ARIKMK = 'Historical Marker Database, “Arikara villages” marker (hmdb.org, marker 113316)'
OBS += [
 pl('mde',1700.0,'The great Dakota village of Kathio (Izatys) at Mille Lacs, the source of the Rum River; Du Lhut counted “40 Sioux villages in the vicinity” in 1679',(46.15,-93.75),25,WP('Battle of Kathio')+' (belligerent: Mdewakanton Dakota)'),
 pl('mde',1745.0,'Mille Lacs, before the Ojibwe destroyed Kathio “in about the year 1750” and expelled the Dakota (a battle there is recorded in 1745)',(46.15,-93.75),25,WP('Battle of Kathio')),
 pl('hid',1700.0,'Knife River villages: “the Big Hidatsa village was established around 1600”; Awatixa Xi’e the oldest of the three',(47.354,-101.386),5,WP('Knife River Indian Villages National Historic Site')),
 pl('kap',1700.0,'Northern Arapaho tradition (1892) of the Kiowa at the Three Forks of the Missouri, applied to the Plains Apache only on the assumption that they were already with the Kiowa (kept off the division track)',(45.9,-111.5),200,MOONEY+', pp. 155–56',whole=False),
 *pls(['kio'],1700.0,'Northern Arapaho tradition (1892): when they first knew the Kiowa, the Kiowa “lived about the Three forks of the Missouri”; date ours (“probably about or before 1700”)',(45.9,-111.5),200,MOONEY+', pp. 155–56'),
 *pls(['kio','kap'],1755.0,'“Situated east of the Crows, the Kiowa took possession of the Black Hills… They continued to occupy the Black Hills until about the close of the last century”; the Apache part of their camp circle',P['blackhills'],120,MOONEY+', p. 156'),
 pl('man',1750.0,'Clark, 20 Oct. 1804: old fortified Mandan villages below the Heart River; the Arikara chief “tels me that nation lived in a number villages on each side of the river and the Troubleson Seauex caused them to move about 40 miles higher up”',(46.75,-100.85),25,LCJ+', entries for 19–20 Oct. 1804'),
 pl('man',1779.0,'Clark, 22 Oct. 1804: “the upper of the 6 Villages the Mandans occupied about 25 years ago… entirely cut off by the Sioux”',(47.0,-101.0),25,LCJ+', entry for 22 Oct. 1804'),
 pl('man',1790.0,'Clark’s map shows “some six old villages in present Oliver County, below Hensler, some of them indicated as having been abandoned nine years, that is, since 1795” (Moulton)',(47.17,-101.2),20,LCM+', 24 Oct. 1804, n. 3'),
 pl('chy',1795.0,'After the Ojibwe destroyed the Sheyenne River town, “a number of villages belonging to the tribe along the Missouri near the point where the boundary line between North and South Dakota crosses it”; Ordway passes “an old village some years ago of the Chien Nation”, 15 Oct. 1804',(45.95,-100.6),40,SW+'; '+LCJ+', entry for 15 Oct. 1804'),
 pl('ari',1770.0,'“In 1770 when French traders opened relations with them they were a little below Cheyenne River”',(44.6,-100.7),30,SW),
 pl('ari',1796.0,'In 1796 the Arikara lived in “two consolidated villages just below the mouth of the Cheyenne River”',(44.68,-100.9),15,ARIKMK),
 pl('ari',1824.5,'(Contradicted by Parks, Handbook 13, pp. 366–67, who has the Arikara near the Mandan villages in 1823–24, back at the Grand River from spring 1824 and on the Loup only in 1833–35; kept as a record, off the track.) After the Leavenworth fight “they abandoned their country and went to live with the Skidi on Loup River. Two years later they returned to the Missouri”',P['skidi_loup'],30,SW,whole=False),
 pl('ari',1833.5,'“1832: They left the Grand River and rejoined the Pawnee on the Loup River”; in 1837 they moved back north to the Mandan villages',P['skidi_loup'],30,ARIKMK),
 pl('iow',1800.0,'“Their principal town was on the Des Moines River and for a long time at a spot in the northwestern part of Van Buren County”',(40.8,-92.1),15,SW),
 pl('ass',1738.83,'La Vérendrye, from Fort La Reine (Oct. 1738): “Joining a large band of Assiniboines, he pushed southwest across the prairie” to the Mandan',(49.6,-99.3),120,WP('Pierre Gaultier de Varennes, sieur de La Vérendrye')),
 pl('asn',1754.72,'Henday meets “Asinepoets” (“thought by some to be Assiniboines”) on 20 Sept. 1754, nine days after crossing into present Alberta near Chauvin',(52.6,-110.4),100,WP('Anthony Henday')),
 pl('sik',1754.79,'14–17 Oct. 1754: Henday “came to 200 tents of Archithinue Natives, pitched in two rows”; on the 17th “322 tents of Archithinue Natives unpitched and moved Westward”. Burpee places the camp southwest of the Red Deer crossing near Knee Hills Creek; others put it west of Pine Lake near Innisfail. Which people is disputed: Burpee reads Blackfoot, Ewers probably Gros Ventre; placed with the Siksika, the northernmost Blackfoot',(51.6,-113.5),60,HENDAY('pp. 337–40 (pdf 37–40)')),
 pl('gv',1754.8,'“The earliest known contact of Gros Ventre with whites was around 1754, between the north and south forks of the Saskatchewan River”',(52.6,-106.8),120,WP('Gros Ventre')),
 pl('sho',1835.32,'27 April [1835]: at the outlet of Bear River from the Snake (Bear) Lake “we found about 300 lodges of Snake Indians”',(42.05,-111.3),40,RUSSELL+', pp. 17–18'),
 pl('sho',1836.35,'8 May [1836]: on Bear River at Thomas Fork, the trappers “encamped with 400 lodges of Snakes and Bannocks and 100 lodges of Nez Perces and Flatheads”',(42.25,-111.05),30,RUSSELL+', pp. 44–45'),
]
OBS += [
 pl('ari',1838.0,'“1837: They moved back north to the Mandan villages on the Knife River”; Warren (1856) finds them “in a village near Fort Clark”',P['ft_clark'],10,ARIKMK),
 *pls(['kio','kap'],1840.6,'The great peace of 1840 with the Cheyenne and Arapaho, made “at the mouth of the Two Butte Creek, at the south side of the Arkansas River… about fifty miles below Bent’s Fort”',(38.03,-102.2),15,GRF+', pp. 62–66'),
]
# Southern plains, 1835–64: Comanche councils, reserve and camps, checked against the sources named.
TSHA='Texas State Historical Association, Handbook of Texas Online'
HMDB_HOLMES='Historical Marker Database, “Camp Holmes Treaty” (Lexington, Okla.)'
OBS += [
 *pls(['cyk','cyp'],1835.64,'Camp Holmes treaty council, 24 Aug. 1835: about 5,000 Comanche, Wichita and other Plains Indians camped for six weeks a mile northwest of present Lexington (Comanche bands not named; division ours)',(35.03,-97.35),15,HMDB_HOLMES),
 pl('cyp',1840.21,'Council House Fight, San Antonio, 19 Mar. 1840: Muguara’s Penateka delegation of 65, chiefs, women and children (a delegation, kept off the division track)',(29.425,-98.494),2,WP('Council House Fight'),seasonal=True),
 pl('cyp',1847.17,'Meusebach council with the Penateka chiefs Buffalo Hump, Santa Anna and Old Owl on the lower San Saba, about 25 miles from the Colorado, 1–2 Mar. 1847',(31.05,-99.05),30,WP('Meusebach–Comanche Treaty')),
 st('cyp',1855.66,450,'Comanche reserve on the Clear Fork of the Brazos by Camp Cooper: “about 450 Penateka Comanches settled there under the treaty of August 30, 1855”; Ketumse’s principal village in a bend of the river (part of the Penateka; kept off the division track)',(33.07,-99.21),12,TSHA+', “Comanche Indian Reservation”',whole=False),
 pl('cyp',1859.67,'The reserve Comanches, consolidated at the Red River, delivered to the agency in Indian Territory, 1 Sept. 1859, on a tract near Anadarko assigned to the Wichita Agency (part of the Penateka; kept off the division track)',(35.1,-98.25),20,TSHA+', “Comanche Indian Reservation” and “Comanche Indians”',whole=False),
 *pls(['cyy','cyk'],1864.9,'First Battle of Adobe Walls, 25 Nov. 1864: a Comanche village of about 500 lodges near Bent’s ruined post on the north side of the Canadian (division ours; the source names no chief)',(35.89,-101.40),10,WP('First Battle of Adobe Walls')),
 pl('kio',1864.9,'First Battle of Adobe Walls, 25 Nov. 1864: Dohäsan’s Kiowa village of 176 lodges about four miles from Adobe Walls',(35.85,-101.35),6,WP('First Battle of Adobe Walls')),
]
TSHA_C=TSHA+', “Comanche Indians”'
COMSP='Wikipedia, “Comanche–Spanish peace treaties”'
OBS += [
 pl('cyp',1758.2,'Mission Santa Cruz de San Sabá near present Menard attacked by “a force of some 2,000 Comanches and allied tribes”, March 1758 (a war expedition, kept off the division track)',(30.92,-99.79),10,TSHA_C,seasonal=True),
 *pls(['cyj','cyy'],1785.85,'Before 10 Dec. 1785 the western Comanche held a conference of “600 rancherias (family groups)” on the Arkansas in Colorado and chose Ecueracapa to treat with Anza (site not given; placed on the Arkansas below the Purgatoire)',(38.1,-103.4),150,COMSP),
 *pls(['cyj','cyy'],1786.16,'Pecos, 28 Feb.–3 Mar. 1786: “two hundred Comanche chiefs waited in Pecos” for the treaty and trade fair with Anza (a delegation, kept off the division track)',(35.55,-105.68),3,COMSP,seasonal=True),
 pl('cyp',1840.8,'Oct. 1840: Moore’s expedition “destroyed a Comanche encampment near the site of present Colorado City”; the Penateka then crossed the Red River',(32.39,-100.86),25,TSHA_C),
 pl('cyp',1844.5,'Treaty of Tehuacana Creek, 1844, “signed by Buffalo Hump and other chiefs” (a council, kept off the division track; month not given)',(31.6,-97.05),15,TSHA_C,seasonal=True),
]
# Lakota winter counts as printed by Mallery: Battiste Good's (Brulé) and the first Corbusier count (Oglala). Read in the
# Project Gutenberg texts; cited by year entry and figure, since those texts carry no page numbers.
MAL93='Mallery, Picture-Writing of the American Indians (BAE 10th Annual Report, 1893), Battiste Good’s winter count'
MAL86='Mallery, Pictographs of the North American Indians (BAE 4th Annual Report, 1886), Corbusier winter count no. I'
OBS += [
 pl('bru',1818.95,'Winter 1818–19, “Smallpox-used-them-up-again”: “They at this time lived on the Little White river, about 20 miles above the Rosebud agency”',(43.0,-100.95),25,MAL93+', fig. 375'),
 pl('bru',1831.95,'Winter 1831–32: a Dakota “watching for buffalo at Buffalo Gap, in the Black Hills” is shot by the Crows (the camp placed near the gap; ours)',(43.49,-103.31),60,MAL93+', fig. 388'),
 pl('bru',1834.95,'Winter 1834–35, “Killed-the-Cheyenne-who-came-to-the-camp”: “The village was near what is now the Pine Ridge agency”',(43.03,-102.55),25,MAL93+', fig. 391'),
 pl('kio',1814.95,'Winter 1814–15: the Dakotas “went to a Kaiowa village, about 6 miles from Scott’s Bluff, and near the mouth of Horse Creek, to treat for peace”',(41.92,-103.98),10,MAL86+', 1814–15'),
]
# Travellers' narratives read in the Project Gutenberg texts: Irving's Astoria (1836), Gregg (1844, Thwaites's edition), Parkman (1849).
GREGG='Gregg, Commerce of the Prairies (1844), in Thwaites ed., Early Western Travels, vol. 20 (1905)'
PARK='Parkman, The Oregon Trail (1849)'
IRV='Irving, Astoria (1836), ch. 28'
OBS += [
 pl('chy',1811.56,'Late July 1811: Hunt’s Astorians, camped “upon the banks of Big River” west of the Arikara villages, find “a band of Cheyenne Indians” on a small stream and trade with them for a fortnight (Big River identified by us as the Grand; recalled)',(45.8,-102.0),80,IRV),
 *pls(['cyy','cyk'],1839.44,'June 1839, “Camp Comanche”: Gregg’s caravan, five or six miles from the North Fork of the Canadian, is met by about sixty warriors whose people are “encamped just above on yonder creek… nearly all the Comanche nation” gathered to fight the Pawnees (Thwaites places the camp in Lipscomb or Ochiltree County; division ours)',(36.15,-100.5),40,GREGG+', pp. 124–26 and n. 88'),
 pl('ogl',1846.45,'Mid-June 1846: Old Smoke’s village, moving toward Fort Laramie, met on the plain west of Scott’s Bluff',(41.85,-103.8),20,PARK+', ch. 8'),
 pl('ogl',1846.5,'Early July 1846: The Whirlwind’s Oglala village, “150 tall lodges”, joins Parkman’s camp at a bend of Laramie Creek above Fort Laramie (camp site ours, within about 30 km)',(42.0,-104.85),30,PARK+', ch. 11'),
]
# Frémont's report (1845) and Garrard's Wah-to-yah (1850), read in the Internet Archive texts.
FREM='Frémont, Report of the Exploring Expedition to the Rocky Mountains in the Year 1842, and to Oregon and North California in the Years 1843–’44 (1845)'
GARR='Garrard, Wah-to-yah and the Taos Trail (1850)'
OBS += [
 *pls(['arn','ars'],1842.52,'July 1842: an Arapaho village of about three hundred men, with “about twenty lodges” of Cheyennes, met on the South Platte below St. Vrain’s fort (site ours, from Frémont’s route; division ours)',(40.3,-104.1),50,FREM+', pp. 28–29'),
 pl('ogl',1843.505,'3 July 1843: “a village of Oglallah Sioux, who had lost all their animals in the severity of the preceding winter”, on the South Platte near the mouth of the Bijou, going up the Bijou to beg horses from the Arapahoes',(40.3,-103.9),30,FREM+', p. 109'),
 *pls(['arn','ars'],1843.515,'7 July 1843: “the Arapaho village… encamped in a beautiful bottom, and consisting of about 160 lodges”, on the South Platte a few miles above a camp sixteen miles from St. Vrain’s (division ours)',(40.02,-104.92),15,FREM+', pp. 109–10'),
 *pls(['chs','ars'],1844.51,'5 July 1844, about twenty miles below Bent’s Fort: “a very large village of Sioux and Cheyenne Indians, who, with the Arapahoes, were returning from the crossing of the Arkansas, where they had been to meet the Kioway and Camanche”',(37.98,-103.1),20,FREM+', p. 288'),
 pl(['pwc','pwk','pws'],1844.54,'17 July 1844: “nearly all the Pawnee tribe” camped at the mouth of a wooded stream on the Smoky Hill, returning from the crossing of the Arkansas (a hunting camp, kept off the division tracks; site approximate)',(38.85,-98.8),80,FREM+', pp. 288–89',seasonal=True),
 pl('chs',1846.88,'Nov. 1846: the Cheyenne village on the Arkansas near the mouth of the Purgatoire; the people “talked of moving to the ‘Big Timber,’ a few miles” off',(38.07,-103.05),25,GARR+', pp. 45–53'),
 pl('chs',1847.05,'Winter 1846–47: the Cheyenne village at the “Big Timber”, “a strip of woods extending for several miles along the river… which the Indians consider their future home”',(38.08,-102.75),20,GARR+', p. 127'),
]
LARP='Larpenteur, Forty Years a Fur Trader on the Upper Missouri, ed. Quaife (1933)'
OBS += [
 *pls(['cwm','cwr'],1833.62,'Summer 1833, on the way from the Green River rendezvous to the Yellowstone: the whole Crow camp, “upward of 400 lodges”, one day’s march from the fort where it had just traded (“the Crows, at that time, generally roamed together”); fort taken by us to be Fort Cass at the Bighorn mouth',(46.05,-107.6),50,LARP+', p. 36'),
 pl('crs',1844.07,'Late January 1844: “a camp of Crees and Chippewas, who have plenty of robes”, at Woody (Wood) Mountain',(49.4,-106.4),40,LARP+', p. 154'),
]
# Bradbury and Brackenridge (1811) and Raynolds (1859–60), read in the Internet Archive texts.
BRAD='Bradbury, Travels in the Interior of America (1817)'
BRACK='Brackenridge, Journal of a Voyage up the River Missouri (1814), in Thwaites ed., Early Western Travels, vol. 6 (1904)'
RAYN='Raynolds, Report on the Exploration of the Yellowstone River (1868)'
OBS += [
 *pls(['bru','min','ykl'],1811.41,'End of May 1811, below the Big Bend of the Missouri: Hunt’s Astorians learn that three Sioux tribes, the “Yanktons Ahnah”, the Teton “Bois Brulé” and the Teton “Minenackinie”, are camped about a league off, near 280 lodges by Bradbury’s two-warriors-a-lodge reckoning, waiting to stop the boats (site ours, below the bend; Yanktons Ahnah taken as Yanktonai)',(43.9,-99.4),40,BRAD+'; '+BRACK+', pp. 98–99'),
 pl('cwm',1859.62,'17 Aug. 1859: two Crows at Raynolds’s camp near Fort Sarpy on the Yellowstone report “their village of 100 lodges” two days’ march behind them, coming in for annuities (part of the Crow; kept off the division track)',(46.2,-107.3),60,RAYN+', p. 46',whole=False),
 pl('cwm',1859.67,'3 Sept. 1859: Red Bear’s Crow “village of 130 lodges” on Raynolds’s trail near Fort Sarpy, proposing to follow the party to the head of Powder River (part of the Crow; kept off the division track)',(46.1,-107.1),30,RAYN+', p. 53',whole=False),
 pl('arn',1859.72,'Late Sept. 1859, on the way south from the Powder River toward the Platte road: Little Owl’s and Friday’s Arapaho “whole village of 180 lodges was within six or seven miles”; Maynadier met Little Owl’s village on Crazy Woman’s Fork on 30 Sept. (site ours)',(44.1,-106.4),50,RAYN+', pp. 64, 130'),
 pl('pik',1860.55,'21 July 1860, in the Judith Mountains: the “Little Robes”, a band of the Blackfeet, 54 lodges and about 150 or 200 people (a single band; kept off the division track)',(47.1,-109.2),20,RAYN+', p. 163',whole=False),
]
# ======== Handbook of North American Indians, vol. 13, Plains (2001), part 1, read chapter by chapter ========
HB13='DeMallie, ed., Handbook of North American Indians, vol. 13: Plains (2001)'
def HBC(ch,au,pp): return f'{HB13}, {au}, “{ch}”, {pp}'
HBA=lambda pp: HBC('Assiniboine','DeMallie and Miller',pp)
HBCR=lambda pp: HBC('Plains Cree','Darnell',pp)
HBOJ=lambda pp: HBC('Plains Ojibwa','Albers',pp)
HBBF=lambda pp: HBC('Blackfoot','Dempsey',pp)
OBS += [
 # ---- Assiniboine
 pl('asn',1766.0,'William Pink reports a small group of Assiniboines in the Prince Albert area with many horses; they had given up canoes (a single group; kept off the division track)',(53.2,-105.75),60,HBA('p. 574'),whole=False),
 pl('asn',1795.0,'1790s (Mackenzie): the western Assiniboine bands in eastern Alberta near Fort George on the North Saskatchewan, some in the woodlands north of the river',(53.88,-110.88),100,HBA('p. 574')),
 pl('asn',1794.95,'Winter 1794–95 (M’Gillivray at Fort George): the Strong Wood and Grand River bands build buffalo pounds near the fort; the Canoe band comes in to trade (two bands; kept off the division track)',(53.88,-110.88),40,HBA('p. 574'),whole=False),
 pl('asn',1824.0,'1823–24 (Hudson’s Bay Company reports): a group of Assiniboines, Plains Crees and Métis living near Fort Edmonton; the Strong Wood Assiniboine farther northwest on the McLeod River (kept off the division track)',(53.54,-113.5),40,HBA('p. 574'),whole=False),
 pl('ass',1840.0,'By 1840 three-quarters of the tribe lived on the Missouri in the area of Montana; Fort Union (1829) had been sited by the chief of the Rock band',(48.0,-104.0),150,HBA('pp. 572, 574')),
 dict(g=['ass','asn'],y=1850.5,pop=4800,raw='1850 (Culbertson): about 1,500 lodges given in the table, 4,800 people',basis='souls',loc='inferred',at=(49.0,-105.0),r=300,src=HBA('p. 590, table 2'),kind='primary'),
 dict(g=['ass','asn'],y=1860.0,pop=5000,raw='Palliser: 5,000 (expedition of 1857–60; the Handbook’s table dates it 1863)',basis='souls',loc='inferred',at=(49.5,-105.0),r=300,src=HBA('p. 590, table 2'),kind='primary'),
 pl('ass',1869.7,'Milk River Agency established at Fort Browning, Sept. 1869, for the Assiniboine, Gros Ventre, River Crow and some Sioux (kept off the division track)',(48.4,-108.2),20,HBA('pp. 574–75'),whole=False),
 st('ass',1873.4,1944,'May 1873, agency moved to Fort Peck: the Lower Assiniboine Canoe Paddler bands of Red Stone (648), Broken Arm (416), Bobtail Bear (480) and Red Snow (400) (part of the division)',(48.0,-106.45),15,HBA('p. 583'),basis='census',whole=False),
 st('ass',1873.5,2595,'1873, Fort Belknap subagency near present Chinook: the Upper Assiniboine North band (1,100), Stone or Rocky band (1,070) and Dogtail band (425) (part of the division)',(48.47,-109.27),15,HBA('p. 583'),basis='census',whole=False),
 dict(g='ass',y=1873.45,pop=4539,raw='1873: the Fort Peck and Fort Belknap Assiniboine bands together, 1,944 + 2,595 (agent A.J. Simmons’s figures)',basis='census',loc='inferred',at=(48.2,-107.8),r=150,src=HBA('p. 583'),kind='primary'),
 pl('asn',1873.33,'1 May 1873, Cypress Hills Massacre: wolfers attack 40 lodges of starving Assiniboines under Little Soldier on Battle Creek, killing 16 (one band; kept off the division track)',(49.6,-109.95),5,HBA('p. 584'),whole=False),
 pl('asn',1875.69,'9 Sept. 1875: “Stonies” under Piapot, Pheasant Rump and Striped Blanket sign an adhesion to Treaty No. 4 at Qu’Appelle Lakes (kept off the division track)',(50.77,-103.8),15,HBA('p. 585'),whole=False),
 pl('asn',1877.73,'25 Sept. 1877: the Assiniboine bands of Long Lodge, Man Who Took the Coat, Poorman and Lean Man sign Treaty No. 4 at Fort Walsh in the Cypress Hills',(49.57,-109.88),10,HBA('p. 585')),
 pl('asn',1882.5,'1882: the bands of Long Lodge and Man Who Took the Coat removed under protest to the vicinity of Indian Head (later the Carry The Kettle reserve)',(50.53,-103.67),15,HBA('p. 586')),
 *[st('ass',y,p,f'Fort Belknap and Fort Peck reservations together: {a} + {b}',(48.2,-107.8),150,HBA('p. 590, table 3'),basis='census') for (y,p,a,b) in [(1885,2372,700,1672),(1895,1479,763,716),(1905,1262,689,573)]],
 # ---- Plains Cree
 pl('cre',1874.71,'Treaty No. 4 signed at Qu’Appelle, 15 Sept. 1874, by Plains Cree, Plains Ojibwa and Assiniboine bands',(50.77,-103.8),15,HBCR('p. 641')+'; '+HBA('p. 584')),
 pl('crw',1876.6,'Treaty No. 6 signed at Fort Carlton and Fort Pitt, 1876, by the Plains and Western Woods Cree of central Saskatchewan and Alberta (placed at Fort Pitt; month not given)',(53.57,-109.8),60,HBCR('p. 641')),
 # ---- Plains Ojibwa
 pl('ojb',1825.0,'A large fortified village called Buffalo Lodge, near present Towner, North Dakota, formed by part of the Turtle Mountain Ojibwa, destroyed by the Yanktonai in 1824–25 (part of the division; kept off the track)',(48.35,-100.4),15,HBOJ('pp. 653–54'),whole=False),
 pl('ojb',1840.0,'1820s–1850s: the largest body of fully equestrian Plains Ojibwa between the Assiniboine and Souris rivers, including the Turtle Mountain and Moose Mountain People; after the 1830s epidemics dominant on the plains straddling the Souris',(49.5,-100.8),120,HBOJ('pp. 653–54')),
 # ---- Blackfoot
 dict(g=['sik','kai','pik'],y=1780,pop=15000,raw='Mooney: 15,000 in 1780',basis='souls',loc='inferred',at=(50.5,-112.0),r=300,src=HBBF('p. 622, table 1')+', citing Mooney 1928',kind='secondary'),
 dict(g=['sik','kai','pik'],y=1814,pop=8000,raw='Schermerhorn (1814): 8,000',basis='souls',loc='inferred',at=(50.5,-112.0),r=300,src=HBBF('p. 622, table 1'),kind='primary'),
 *[st(g,y,p,f'{lab}: {p:,}',at,r,HBBF('p. 622, table 1')+f', citing {who}',kind='primary') for (y,who,lab,vals) in [
     (1823,'T. Heron, Chesterfield House journals','Heron, 1823',{'sik':4200,'kai':2800,'pik':4200}),
     (1859,'J. Rowand in Hind 1859','Rowand, 1859',{'sik':2400,'kai':2000,'pik':2600}),
     (1872,'J. L’Heureux in Dempsey 1961','L’Heureux, 1872',{'sik':3568,'kai':2508,'pik':4184}),
     (1885,'H. Hale 1885','Hale, 1885',{'sik':2400,'kai':2800,'pik':3100})]
   for (g,p) in vals.items() for (at,r) in [({'sik':((51.0,-112.5),250),'kai':((49.7,-112.8),250),'pik':((48.8,-112.3),250)})[g]]],
 pl('pik',1815.0,'Early 19th century, under pressure from Cree and Assiniboine: the Piegan withdraw to the Missouri River and foothills region',(48.6,-112.3),120,HBBF('p. 607')+', citing MacGregor 1967'),
 pl('kai',1815.0,'Early 19th century: the Blood centered on the Bow and Belly rivers',(49.9,-112.6),100,HBBF('p. 607')+', citing MacGregor 1967'),
 pl('sik',1815.0,'Early 19th century: the Blackfoot proper remain near the Red Deer River',(51.4,-112.4),100,HBBF('p. 607')+', citing MacGregor 1967'),
]
for _o in OBS:   # tribe-wide counts from the Handbook's tables carry no place of their own
    if _o['raw'].startswith(('Heron, 1823','Rowand, 1859','L’Heureux, 1872','Hale, 1885','Fort Belknap and Fort Peck reservations together')): _o['loc']='inferred'
for _o in OBS:   # Fort Peck counts alone leave out the Upper Assiniboine at Fort Belknap (Handbook 13, p. 583), so they are partial counts
    if _o.get('g')=='ass' and _o.get('pop') in (1998,1615) and 'Fort Peck' in _o['raw']: _o['whole']=False

HBMA=lambda pp: HBC('Mandan','Wood and Irwin',pp)
HBHI=lambda pp: HBC('Hidatsa','Stewart',pp)
HBAR=lambda pp: HBC('Arikara','Parks',pp)
HBPA=lambda pp: HBC('Pawnee','Parks',pp)
HBWI=lambda pp: HBC('Wichita','Newcomb',pp)
PW3=['pwc','pwk','pws']
OBS += [
 # ---- Mandan and Hidatsa
 dict(g='man',y=1750,pop=9000,raw='“The Mandan population in 1750 seems to have been about 9,000”',basis='souls',loc='inferred',at=(46.85,-100.75),r=20,src=HBMA('p. 351'),kind='secondary'),
 dict(g='man',y=1778,pop=4400,raw='Lehmer: villages reduced between 1750 and 1780, population about 4,400 before the epidemic',basis='souls',loc='inferred',at=(46.85,-100.75),r=20,src=HBMA('p. 351'),kind='secondary'),
 dict(g='man',y=1782,pop=1250,raw='The 1781 smallpox epidemic “left only 1,000–1,500 individuals”',basis='souls',loc='inferred',at=(46.85,-100.75),r=20,src=HBMA('p. 351'),kind='secondary'),
 dict(g='man',y=1838,pop=150,raw='Smallpox, 1837: “fewer than 150 survived” (Hayden 1862; Chardon)',basis='souls',loc='inferred',at=(47.3,-101.3),r=20,src=HBMA('p. 351'),kind='primary'),
 dict(g='hid',y=1780,pop=4000,raw='Before the 1781 smallpox: the survivors, about 2,000, were “probably no more than half the pre-epidemic population”',basis='souls',loc='inferred',at=(47.35,-101.38),r=10,src=HBHI('p. 329'),kind='secondary'),
 dict(g='hid',y=1782,pop=2000,raw='Survivors of the 1781 smallpox, about 2,000',basis='souls',loc='inferred',at=(47.35,-101.38),r=10,src=HBHI('p. 329'),kind='secondary'),
 dict(g='hid',y=1837.4,pop=2100,raw='Population about 2,100 before the 1837 smallpox, of whom about two-thirds died',basis='souls',loc='inferred',at=(47.35,-101.38),r=10,src=HBHI('p. 330'),kind='secondary'),
 dict(g='hid',y=1838.5,pop=700,raw='After the 1837 smallpox, about a third of 2,100 survived',basis='souls',loc='inferred',at=(47.35,-101.38),r=10,src=HBHI('p. 330'),kind='secondary'),
 pl('hid',1870.0,'About 1870 the Crow Flies High band breaks away from Like-a-Fishhook; villages near Fort Buford (Garden Coulee) and elsewhere until 1894 (a band; kept off the division track)',(48.0,-104.0),30,HBHI('pp. 329–31'),whole=False),
 # ---- Arikara
 pl('ari',1714.0,'Bourgmont: three Arikara villages on the west bank of the Missouri above the Niobrara, and 40 villages farther upriver on both banks (kept off the division track)',(43.0,-98.6),40,HBAR('p. 366'),whole=False),
 pl('ari',1785.0,'Miró: seven Arikara villages on the Missouri below the Cheyenne River',(44.5,-100.6),40,HBAR('p. 366')),
 pl('ari',1796.4,'1796: expecting a Sioux attack, the Arikara abandon their two villages below the Cheyenne; one group goes north to the Mandan, the others west to the Cheyenne (Truteau) (kept off the division track)',(44.68,-100.9),40,HBAR('p. 366'),whole=False),
 pl('ari',1823.7,'After the Leavenworth fight, Aug. 1823, the Arikara flee upriver and live near the Mandan villages for a year',(47.2,-101.2),20,HBAR('pp. 366–67')),
 pl('ari',1824.3,'Spring 1824: the Arikara return to reoccupy the Cottonwood Creek villages near the Grand River',(45.55,-100.47),5,HBAR('p. 367')),
 pl('ari',1832.5,'1832: still at the Grand River villages (Catlin)',(45.55,-100.47),5,HBAR('p. 367')),
 pl('ari',1835.7,'Summer 1835: after friction with the Skiri, the Arikara leave the Loup and live for two years as nomadic hunters in western Nebraska and South Dakota (place ours)',(43.3,-101.5),200,HBAR('p. 367')),
 *[dict(g='ari',y=y,pop=p,raw=f'{who}: {p:,}',basis='souls',loc='inferred',at=at,r=20,src=HBAR('p. 387, table 3')+f', citing {who}',kind=k) for (y,p,who,at,k) in [
     (1770,16000,'Truteau’s pre-epidemic 4,000 warriors (Parks: about 16,000, at least 10,000)',(44.6,-100.6),'secondary'),
     (1834,2200,'Allis',(41.6,-98.3),'primary'),(1842,1200,'ARCIA 1842',(47.25,-101.27),'primary'),(1850,1500,'Culbertson',(47.25,-101.27),'primary'),
     (1855,840,'ARCIA 1855 (60 lodges, 14 to a lodge)',(47.25,-101.27),'primary'),(1866,1500,'Kane',(47.25,-101.27),'primary'),
     (1875,900,'ARCIA 1875',(47.6,-101.85),'primary'),(1885,529,'ARCIA 1885',(47.6,-101.85),'primary'),(1895,420,'ARCIA 1895',(47.6,-101.85),'primary')]],
 # ---- Pawnee
 pl('pws',1723.0,'Renaudière: a Pawnee village of 150 lodges 15 leagues up the Loup, and eight more villages farther upriver about half a league apart',(41.38,-97.95),30,HBPA('pp. 517–18')),
 pl('pws',1739.5,'The Mallet brothers visit the Panimaha (Skiri) at the mouth of the Loup, 1739',(41.43,-97.36),10,HBPA('p. 518')),
 st('pws',1758.0,2400,'Kerlerec: the Panimaha, on the Platte 25 leagues from its mouth, number 600 men bearing arms',(41.45,-96.8),40,HBPA('pp. 518, 563'),basis='men × 4 (ours)'),
 pl('pwc',1777.0,'Cruzat, Nov. 1777: the Chawi on the west bank of Skull Creek below the Platte (Barcal site)',(41.37,-96.93),8,HBPA('p. 518')),
 pl('pwk',1777.0,'Cruzat, 1777: the Kitkahahki in a village on the Republican River',(40.05,-98.1),40,HBPA('p. 518')),
 pl('pws',1777.5,'1777: about 300 Panimahas leave the Skiri on the Loup for the Red River, joining the Taovaya; they stay into the 19th century (part; kept off the division track)',(33.95,-97.65),30,HBPA('p. 518'),whole=False),
 *[st(g,1785.0,4*m,f'Miró, 1785: {m} “men capable of bearing arms”',at,50,HBPA('p. 563'),basis='men × 4 (ours)') for (g,m,at) in [('pws',350,(41.3,-98.0)),('pwc',400,(41.3,-97.3)),('pwk',220,(40.05,-98.1))]],
 *[st(g,1804.0,4*m,f'Pierre Chouteau, 1804: {m} men',at,50,HBPA('p. 563'),basis='men × 4 (ours)') for (g,m,at) in [('pws',400,(41.22,-98.25)),('pwc',500,(41.33,-97.25)),('pwk',300,(41.33,-97.25))]],
 pl('pwc',1806.75,'Pike’s map, 1806: the Chawi below the mouth of Shell Creek (Linwood site)',(41.4,-96.93),5,HBPA('p. 519')),
 pl('pws',1806.75,'Pike’s map, 1806: the Skiri at the Palmer site on the Loup',(41.22,-98.25),5,HBPA('p. 519')),
 *pls(['pwc','pwk'],1811.5,'Sibley, 1811: the Kitkahahki have left the Republican for the Platte, and the three South Bands have moved to the Loup just south of the Skiri village (Horse Creek site)',(41.2,-98.15),15,HBPA('p. 519')),
 pl('pwc',1833.5,'1833: the four Pawnee bands sign the cession treaty at the Clarks village site',(41.21,-97.84),5,HBPA('p. 520')),
 *pls(['pwc','pwk'],1841.0,'By 1841: the Chawi, Kitkahahki and Pitahawirata in one combined village (Mission site) between Plum and Council creeks on the north bank of the Loup',(41.38,-97.98),8,HBPA('p. 520')),
 pl('pws',1841.0,'By 1841: the Skiri on Cedar Creek where it joins the Loup, about four miles above the Mission site',(41.42,-98.05),8,HBPA('p. 520')),
 pl('pwk',1855.5,'Agent’s report, 1855: the Kitkahahki at the Linwood site, south of the Platte',(41.4,-96.93),5,HBPA('p. 520')),
 pl('pwc',1855.5,'Agent’s report, 1855: the Chawi at the Leshara site, south of the Platte',(41.33,-96.43),5,HBPA('p. 520')),
 pl('pws',1855.5,'Agent’s report, 1855: the Skiri at the McClaine site, south of the Platte (site ours, near the others)',(41.38,-96.7),25,HBPA('p. 520')),
 *pls(PW3,1859.9,'After the summer hunt of 1859 the Pawnee move to their reservation; three contiguous villages where Beaver Creek joins the Loup, at Genoa',(41.45,-97.73),5,HBPA('pp. 520–21')),
 *pls(PW3,1875.1,'February 1875: some 1,760 Pawnees gathered among the Wichita; 400 still in Nebraska',(35.1,-98.25),15,HBPA('p. 522')),
 dict(g=PW3,y=1875.1,pop=2160,raw='February 1875: 1,760 among the Wichita and 400 remaining in Nebraska',basis='census',loc='inferred',at=(35.1,-98.25),r=100,src=HBPA('p. 522'),kind='primary'),
 dict(g=PW3,y=1702,pop=10000,raw='Iberville (1702): 2,000 “Panas” families, “a population in excess of 10,000, assuming a minimum of five individuals in a family” (Parks)',basis='families × 5 (Parks)',loc='inferred',at=(41.3,-97.6),r=100,src=HBPA('p. 563'),kind='secondary'),
 dict(g=['pwc','pwk'],y=1798,pop=3200,raw='Zenon Trudeau, 1798: 800 men for the “Panis” on the Platte (the South Bands)',basis='men × 4 (ours)',loc='inferred',at=(41.3,-97.3),r=60,src=HBPA('p. 563'),kind='primary'),
 *[dict(g=PW3,y=y,pop=p,raw=f'{who}: {p:,}',basis='census' if y>=1867 else 'souls',loc='inferred',at=at,r=60,src=HBPA('p. 563, table 3')+f', citing {who}',kind='primary') for (y,p,who,at) in [
     (1819,6500,'James (Long expedition)',(41.3,-97.9)),(1840,7500,'J.B. Dunbar',(41.38,-97.98)),(1847,8400,'J.B. Dunbar',(41.38,-96.8)),
     (1867,2935,'ARCIA 1867',(41.45,-97.73)),(1872,2447,'ARCIA 1872',(41.45,-97.73)),(1892,798,'ARCIA 1892',(36.34,-96.8)),(1901,629,'ARCIA 1902',(36.34,-96.8))]],
 *[st(g,1840.0,p,f'ARCIA 1840: {lab}',at,30,HBPA('p. 563'),basis='census') for (g,p,lab,at) in [
     ('pws',1906,'Skiri 1,906',(41.42,-98.05)),('pwk',1823,'Kitkahahki 1,823',(41.38,-97.98)),('pwc',2515,'Chawi 1,683 and Pitahawirata 832',(41.38,-97.98))]],
 # ---- Wichita
 dict(g='wic',y=1719.75,pop=2340,raw='Du Tisné’s two Taovaya villages near Neodesha, 130 grass houses and 200–250 warriors each: between them 2,080–2,600 people (the Taovaya only; a partial count)',basis='souls',loc='inferred',at=(37.42,-95.68),r=10,src=HBWI('pp. 550, 561'),kind='primary',whole=False),
 st('wic',1749.0,2000,'1748–49: French deserters pass two Wichita villages a mile and a half apart on the west side of the Arkansas (Deer Creek and Bryson-Paddock), population 1,500–2,500, mostly Taovaya (a partial count)',(36.93,-97.12),5,HBWI('p. 550'),whole=False),
 pl('wic',1757.0,'By 1757 the Taovaya have moved to the Red River just west of the Western Cross Timbers: a fortified village on the north bank (Longest site), an Iscani village downstream',(33.97,-97.6),5,HBWI('p. 550')),
 pl('wic',1778.3,'18 Apr. 1778, De Mézières at the Spanish Fort villages: “The nation of the Taovayazes is divided into two villages”, 37 houses on the north bank of the Red River and 123 on the opposite bank, 10–12 beds to a house, “more than eight hundred” men and youths (the Handbook dates the visit 1779 and calls the north-bank town Wichita proper; De Mézières calls both Taovaya)',(33.95,-97.63),5,BOLTON('vol. 2, pp. 201–2 (pdf 207–8), De Mézières to Croix, 18 Apr. 1778')+'; '+HBWI('p. 551')),
 pl('wic',1801.0,'1801: smallpox leaves the Spanish Fort villages about 400 men, half the number of a quarter-century before (Sibley); Tawakoni village north of the Red, Taovaya and Wichita proper south',(33.95,-97.63),5,HBWI('p. 551')),
 dict(g='wic',y=1806,pop=2600,raw='Early in the 19th century, “again ravaged by smallpox”, the consolidated tribe about 2,600 (Mooney 1910)',basis='souls',loc='inferred',at=(33.95,-97.65),r=50,src=HBWI('p. 561'),kind='secondary'),
 pl('wic',1858.8,'After Van Dorn destroys the Rush Creek village, Oct. 1858, the Wichita flee to Fort Arbuckle, where Agent Rector designates a reservation',(34.53,-97.17),10,HBWI('p. 559')),
 pl('wic',1882.0,'1882: the Wichita settled at Rush Springs, south of the Washita',(34.78,-97.95),15,HBWI('p. 559')),
 dict(g='wic',y=1896,pop=365,raw='Nadir population in 1896: 365 (G.A. Dorsey)',basis='census',loc='inferred',at=(35.07,-98.24),r=30,src=HBWI('p. 561'),kind='primary'),
]

# ---------------- Handbook 13, Dhegiha and Chiwere chapters ----------------
HBOM=lambda pp: HBC('Omaha','Liberty, Wood, and Irwin',pp)
HBPO=lambda pp: HBC('Ponca','Brown and Irwin',pp)
HBIO=lambda pp: HBC('Iowa','Wedel',pp)
HBOT=lambda pp: HBC('Otoe and Missouria','Schweitzer',pp)
HBKA=lambda pp: HBC('Kansa','Bailey and Young',pp)
HBOS=lambda pp: HBC('Osage','Bailey',pp)
def _tab(g,rows,src,at,r=40,basis='souls',**o):
    return [dict(g=g,y=y,pop=p,raw=f'{who}: {lab}',basis=b if b else basis,loc='inferred',at=at,r=r,src=src+f', citing {who}',kind='primary',**o)
            for (y,p,lab,who,b) in rows]
OBS += [
 # ---- Omaha
 pl('oma',1820.3,'By 1820, divided by internal conflicts and pressed by the Sauk and Iowa, the Omaha build an earthlodge village on the Elkhorn River, where they stay until 1833 (place on the lower Elkhorn ours)',(41.75,-96.65),35,HBOM('p. 401')),
 pl('oma',1833.7,'After the Black Hawk War of 1832 the Omaha under Big Elk reestablish themselves at the Big Village site, where they live until driven out by the Teton in 1841',P['omaha_vil'],5,HBOM('p. 401')),
 pl('oma',1845.5,'Driven from Big Village by the Sioux in 1845, “this time permanently”, the Omaha move to a site west of the agency at Bellevue, near the mouth of the Platte, where they stay until the treaty of 1854',(41.15,-96.0),10,HBOM('p. 401')),
 *_tab('oma',[(1758,3200,'800 men','Kerlerec','men × 4 (ours)'),(1796,1100,'1,100','Truteau',None),(1798,2400,'600 men','Z. Trudeau','men × 4 (ours)'),
     (1812,800,'800','Schermerhorn',None),(1834,1400,'1,400','ARCIA 1835',None),(1849,1300,'1,300','ARCIA 1849',None),(1855,800,'800','ARCIA 1855',None),
     (1871,984,'984','ARCIA 1871',None),(1883,1226,'1,226','J.O. Dorsey',None),(1891,1153,'1,153','J.O. Dorsey',None)],HBOM('p. 415, table 2'),P['omaha_vil'],r=60),
 # ---- Ponca
 pl('pon',1785.0,'Miró, 1785: the Ponca “probably” on Bazile Creek, just below the mouth of the Niobrara',(42.75,-97.95),15,HBPO('p. 416')),
 pl('pon',1825.44,'Treaty signed 9 June 1825 at the Ponca village on Bazile (White Paint) Creek; Backing Water Village there was the main Ponca settlement from the late 18th century until at least 1858',(42.75,-97.95),8,HBPO('pp. 416, 418')),
 pl('pon',1859.55,'Summer 1859: Sioux and Cheyenne attack the Ponca on their summer hunt at the headwaters of the Elkhorn, killing 15 (the summer hunting ground)',(42.45,-99.1),40,HBPO('p. 425'),whole=False),
 pl('pon',1877.6,'Removal begun spring 1877, a two-month trek; the Ponca reach lands reserved for the Quapaw near Baxter Springs, Kansas, where nothing has been prepared',(36.98,-94.75),15,HBPO('pp. 425–26')),
 pl('pon',1878.55,'1878: the Ponca move to north-central Oklahoma; agency on the Salt Fork two miles above its mouth on the Arkansas, reached in summer 1878',P['ponca_ok'],8,HBPO('pp. 426–27')),
 *_tab('pon',[(1836,900,'900','Cass',None),(1846,2000,'2,000','Bent',None),(1847,1600,'1,600','Matlock',None),(1852,800,'800','Mitchell',None),
     (1862,1054,'1,054','ARCIA 1862',None)],HBPO('p. 430, table 1'),P['ponca_ck'],r=60),
 *_tab('pon',[(1880,825,'825 (225 northern, 600 southern)','Dorsey and Thomas',None),(1892,775,'775 (208 northern, 567 southern)','Dorsey',None)],HBPO('p. 430, table 1'),P['ponca_ok'],r=150),
 # ---- Iowa
 pl('iow',1701.0,'1701: the Iowa join the tribes gathering at Fort L’Huillier on the Blue Earth River, then flee west again',(44.12,-94.05),15,HBIO('p. 434')),
 pl('iow',1710.0,'After leaving Fort L’Huillier the Iowa “may have chosen to live along the Little Sioux River below Spirit and Okoboji lakes” (date ours)',(43.15,-95.4),50,HBIO('p. 434')),
 pl('iow',1755.0,'An “old” Iowa village on the site of Council Bluffs, seen by Lewis and Clark; occupied within reach of Fort de Cavagnial (1744); date ours, before the move east about 1765',(41.25,-95.87),15,HBIO('p. 434')),
 pl('iow',1766.0,'1765 and the years following: the Iowa move east near the mouth of the Des Moines (On the Des Moines River, 1765–1837)',(40.45,-91.6),25,HBIO('p. 435')),
 pl('iow',1820.0,'1819: refused by the Otoe, the Des Moines River Iowa move to a site 70 miles up the Chariton',(40.1,-92.75),30,HBIO('pp. 435–36')),
 pl('iow',1822.6,'1822: the Iowa move to the Grand River, “perhaps on the north fork”',(40.25,-94.05),40,HBIO('p. 436')),
 pl('iow',1827.0,'By 1827 most of the tribe on the Little Platte in northwest Missouri, on high land near Robidoux’s trading house',(39.65,-94.65),15,HBIO('p. 436')),
 pl('iow',1837.6,'1837: the Iowa move onto a 200-section reservation west of the Missouri and south of the Great Nemaha, administered by the Great Nemaha Subagency',P['nemaha'],10,HBIO('p. 436')),
 dict(g='iow',y=1837.6,pop=800,raw='“In 1837, when reservation life began, Hamilton (1885:64) estimated that about 800 lived there”',basis='souls',loc='inferred',at=P['nemaha'],r=20,src=HBIO('p. 444'),kind='primary'),
 *_tab('iow',[(1814,1400,'1,400','table 2',None),(1848,669,'669','Vaughan',None),(1858,498,'498','ARCIA 1858',None),(1861,305,'305','ARCIA 1861',None),
     (1875,219,'219','ARCIA 1875',None),(1880,222,'222','ARCIA 1880',None),(1890,267,'267','ARCIA 1890',None),(1899,318,'318','ARCIA 1899',None)],HBIO('p. 445, table 2'),P['nemaha'],r=80),
 # ---- Otoe and Missouria
 pl('oto',1714.0,'Bourgmont, about 1714: the Otoe at a village on Salt Creek about 10 leagues from the mouth of the Platte; no Otoe villages east of the Missouri after this',(41.0,-96.45),20,HBOT('p. 447')),
 pl('oto',1836.0,'Persuaded by the Baptist missionary Moses Merrill, by 1836 half the tribe lives six miles west of Bellevue, on the north bank of the Platte (half; kept off the division track)',(41.14,-96.03),5,HBOT('p. 454'),whole=False),
 pl('mis',1839.5,'1839: after factional quarrels, the Missouria leave the Otoe village and move south of the Platte',(40.98,-96.15),20,HBOT('p. 454')),
 *pls(['oto','mis'],1842.0,'By 1842 the Otoe and Missouria live in five small villages on the south side of the Platte from the Missouri to the mouth of the Elkhorn (ARCIA 1842)',(41.0,-96.1),20,HBOT('p. 454')),
 pl('oto',1855.6,'1855: the Otoe-Missouria move to the Big Blue reservation on the Nebraska-Kansas border',P['big_blue'],10,HBOT('pp. 454–55')),
 pl('oto',1880.15,'February 1880: families of the Coyote faction leave the Big Blue for the Sac and Fox reservation; 238 there by March 1881 (a faction; kept off the division track)',(35.6,-96.75),25,HBOT('p. 456'),whole=False),
 pl('oto',1881.8,'October 1881: the Quaker band, 234 people, moves to its reservation on Red Rock Creek, Indian Territory',P['oto_ok'],8,HBOT('p. 456')),
 *_tab('mis',[(1758,600,'150 Missouria men','Kerlerec','men × 4 (ours)'),(1777,800,'200 Missouria warriors','Houck','men × 4 (ours)')],HBOT('p. 453, table 1'),(39.33,-93.22),r=30),
 *_tab('oto',[(1758,400,'100 Otoe men','Kerlerec','men × 4 (ours)'),(1777,400,'100 Otoe warriors','Houck','men × 4 (ours)')],HBOT('p. 453, table 1'),(41.0,-96.3),r=40),
 dict(g=['oto','mis'],y=1798,pop=1600,raw='Trudeau, 1798: 400 men',basis='men × 4 (ours)',loc='inferred',at=P['oto_vil'],r=40,src=HBOT('p. 453, table 1'),kind='primary'),
 dict(g='oto',y=1829,pop=1200,raw='P.B. Porter, 1829: 1,200 Otoe (and 80 Missouria)',basis='souls',loc='inferred',at=P['oto_vil'],r=40,src=HBOT('p. 453, table 1'),kind='primary'),
 dict(g=['oto','mis'],y=1830,pop=1500,raw='B.B. Chapman, 1830: 1,500',basis='souls',loc='inferred',at=P['oto_vil'],r=40,src=HBOT('p. 453, table 1'),kind='secondary'),
 *_tab('oto',[(1835,964,'964','B.B. Chapman',None),(1855,600,'600','B.B. Chapman',None),(1866,513,'513','A.L. Green',None),(1867,430,'430','Hayden',None),
     (1878,459,'459','Milner',None),(1881,473,'473','B.B. Chapman',None),(1890,358,'358','U.S. Census 1894',None)],HBOT('p. 453, table 1'),P['big_blue'],r=150),
 # ---- Kansa
 pl('kaw',1724.55,'July 1724: Bourgmont finds the principal Kansa village on the west bank of the Missouri north of Independence Creek, Doniphan County',(39.68,-95.12),8,HBKA('pp. 462–63')),
 pl('kaw',1740.5,'1739 or 1740: the French build Fort de Cavagnial next to the Kansa village, then near the mouth of Salt Creek',(39.4,-94.93),8,HBKA('p. 463')),
 pl('kaw',1752.6,'1752: seeking better trade, the Kansa move their village to the Kansas River near its confluence with the Missouri',(39.12,-94.75),15,HBKA('p. 464')),
 pl('kaw',1830.6,'1830: the full bloods leave Blue Earth Village for three villages about 35 miles east, where they stay until 1845–48: American Chief’s 20 lodges on Mission Creek, Hard Chief’s 100 lodges near the Kansas River a mile away, Fool Chief’s, the largest, on the north bank',(39.08,-95.85),10,HBKA('pp. 469, 471')),
 pl('kaw',1848.6,'Under the 1846 treaty, a reservation some 20 miles square on the Neosho around Council Grove; the villages there date 1848–73 (map caption)',P['council_grove'],12,HBKA('pp. 462, 471')),
 pl('kaw',1873.6,'1873: on the new reservation bought from the Osage, where Beaver Creek empties into the Arkansas; the tribe then goes on its last bison hunt',P['kaw_ok'],10,HBKA('p. 472')),
 dict(g='kaw',y=1702,pop=1500,raw='Iberville, 1702: 1,500',basis='souls',loc='inferred',at=(39.65,-95.1),r=60,src=HBKA('p. 472, table 2'),kind='primary'),
 *_tab('kaw',[(1837,1471,'1,471','ARCIA 1837',None),(1841,1606,'1,606','ARCIA 1841',None),(1853,1375,'1,375','ARCIA 1853',None),(1860,803,'803','ARCIA 1860',None),
     (1870,574,'574','ARCIA 1870',None),(1880,350,'300+ full bloods and 50 mixed bloods','ARCIA 1880',None),(1887,193,'nadir, 140 full and 53 mixed bloods','ARCIA 1888',None),
     (1890,198,'198','ARCIA 1890',None),(1900,217,'217 (97 full, 120 mixed)','ARCIA 1900',None)],HBKA('p. 472, table 2'),P['council_grove'],r=150),
 # ---- Osage
 pl('osa',1817.8,'1817: a Cherokee war party attacks the Osage village at Claremore Mound on the Verdigris while the men are away on the bison hunt, killing 53 and taking more than 100 captives',(36.32,-95.55),8,HBOS('p. 478')),
 pl('osa',1821.5,'1821: the Cherokee again attack the Osage village on the Verdigris',(36.32,-95.55),15,HBOS('p. 478')),
 dict(g=['osg','osl'],y=1754,pop=3800,raw='Louisiana governor, 1754: about 950 warriors (Din and Nasatir)',basis='men × 4 (ours)',loc='inferred',at=P['osage_vil'],r=80,src=HBOS('p. 492'),kind='primary'),
 dict(g=['osg','osl'],y=1780,pop=7000,raw='Bailey: Mooney’s 6,200 for 1780 too low; “a more realistic estimate would probably be about 7,000”',basis='souls',loc='inferred',at=P['osage_vil'],r=80,src=HBOS('p. 493'),kind='secondary'),
 dict(g=['osg','osl'],y=1855,pop=5000,raw='Bailey: “By the 1850s their population was about 5,000”',basis='souls',loc='inferred',at=(37.5,-95.3),r=80,src=HBOS('p. 493'),kind='secondary'),
 *_tab(['osg','osl'],[(1872,3956,'3,679 full bloods and 277 mixed bloods','ARCIA 1872',None),(1880,2008,'2,008','Bailey 1973',None),(1889,1496,'1,496, the nadir','agency',None),
     (1900,1783,'1,783 (866 full bloods)','Bailey 1973',None)],HBOS('pp. 485, 493'),P['pawhuska'],r=80),
]

# ---------------- Handbook 13, Lehmer, “Plains Village Tradition: Postcontact” ----------------
HBLE=lambda pp: HBC('Plains Village Tradition: Postcontact','Lehmer',pp)
OBS += [
 dict(g='hid',y=1712,pop=8300,raw='Lehmer: villages provisionally Hidatsa, about 1675–1750, hold over 640 houses; at Thompson’s 13 to a household, “over 8,300”',basis='earth lodges × 13 (Lehmer, from Thompson)',loc='inferred',at=(47.2,-101.1),r=40,src=HBLE('pp. 246–48, table 1'),kind='secondary'),
 dict(g='man',y=1712,pop=8000,raw='Lehmer: six sites between Square Buttes and the Heart River, about 1675–1750, with some 620 houses: a Mandan population “of over 8,000”',basis='earth lodges × 13 (Lehmer, from Thompson)',loc='inferred',at=(46.75,-100.85),r=30,src=HBLE('pp. 246–48, table 1'),kind='secondary'),
 dict(g='ari',y=1712,pop=8800,raw='Lehmer: of more than 60 Arikara village sites, perhaps 22 occupied at once, at 40 houses and 10 to a household: 8,800 for the early 18th century',basis='villages × houses × 10 (Lehmer)',loc='inferred',at=(44.9,-100.5),r=120,src=HBLE('pp. 246–48, table 1'),kind='secondary'),
 dict(g='wic',y=1719,pop=15000,raw='Lehmer: “a conservative estimate for the year 1719 is 15,000, based on historical sources” (the Wichita “and closely related groups”)',basis='souls',loc='inferred',at=(36.5,-97.3),r=200,src=HBLE('p. 247'),kind='secondary'),
 pl('man',1780.5,'The Mandan villages around the mouth of the Heart River abandoned about 1780; the survivors move up near the mouth of the Knife (Lewis and Clark)',(46.82,-100.82),10,HBLE('p. 255')),
]
EPI += [
 (1831.3,1831.9,'Smallpox, 1831 (lower Missouri)',{'kaw':.19,'oma':.2},
   HBKA('p. 472')+' (“in 1831 as many as 300 may have died”, of about 1,550); '+HBOM('p. 412')+' (smallpox 1831 among the three devastating epidemics)','sourced for the Kansa; assumed for the Omaha'),
 (1851.4,1851.9,'Smallpox and cholera, 1851 (lower Missouri)',{'oto':.33,'mis':.33,'oma':.25,'iow':.1},
   HBOT('p. 454')+' (the Otoe-Missouria “lost one-third of their population” in 1851); '+HBOM('p. 412')+' (“heavy losses from smallpox and cholera in 1851”)','sourced for the Otoe-Missouria; assumed for the Omaha and Iowa'),
 (1856.4,1856.9,'Smallpox, 1856 (upper Missouri)',{'man':.15,'hid':.15,'ari':.15},
   HBLE('p. 255')+' (the outbreak “devastated both the Mandan and Hidatsa at Like-a-Fishhook Village and the Arikara living near Fort Clark”)','rate assumed'),
]

# ---------------- Handbook 13, Swagerty and Brown history chapters ----------------
HBSW=lambda pp: HBC('History of the United States Plains Until 1850','Swagerty',pp)
HBBR=lambda pp: HBC('History of the Canadian Plains Until 1870','Brown',pp)
OBS += [
 pl('osg',1795.5,'After a short war with the Osage, the Spanish build Fort Carondelet in 1795 near their villages on the Osage River',P['osage_vil'],12,HBSW('p. 266')),
 pl('osa',1820.5,'1820: the United Foreign Missionary Society founds Union Mission for the Osage under Claremore in present Oklahoma, on the Grand (Neosho) River (site recalled)',(36.07,-95.32),25,HBSW('p. 275')),
 pl('osg',1821.5,'1821: Presbyterian missionaries arrive at Harmony Mission, near the Grand Osage village on the Marais des Cygnes (site recalled)',(38.1,-94.25),15,HBSW('p. 275')),
]
EPI += [
 (1819.8,1820.4,'Measles, 1819–20 (north)',{'pik':.33,'kai':.33},
   HBBR('p. 309')+' (“about one-third of the Piegan and Blood population had been lost to measles in 1819–1820”, after Milloy)','sourced for the Piegan and Blood'),
]
HBTA=lambda pp: HBC('Three Affiliated Tribes','Schneider',pp)
OBS += [
 pl('ari',1885.0,'Leaving the overcrowded Like-a-Fishhook in the early 1880s, the Arikara stay nearby and found Nishu, or Armstrong (site approximate; now under Lake Sakakawea)',(47.63,-101.75),15,HBTA('pp. 393–94')),
 pl('hid',1885.0,'Many Hidatsa cross the Missouri and settle the community that becomes Independence; others take scattered farms on the east bank (site approximate; now under Lake Sakakawea)',(47.6,-102.25),25,HBTA('pp. 393–94')),
 pl('man',1885.0,'The Mandan settle Charging Eagle and Red Butte, south of the mouth of the Little Missouri (site approximate; now under Lake Sakakawea)',(47.45,-102.1),25,HBTA('pp. 393–94')),
 pl('hid',1894.5,'1894: Crow Flies High and his band return from Fort Buford and take allotments near Shell Creek (a band; kept off the division track)',(47.95,-102.35),15,HBTA('p. 394'),whole=False),
 *_tab(['man','hid','ari'],[(1880,1252,'1,252 (the three tribes)','ARCIA 1880',None),(1890,1183,'1,183 (the three tribes)','ARCIA 1890',None)],HBTA('p. 397, table 1'),P['like_fishhook'],r=40),
]

# ---------------- Handbook 13, part 2: the Sioux chapters (DeMallie) ----------------
HB13B=HB13.replace('(2001)','(2001), part 2')
def HBC2(ch,au,pp): return f'{HB13}, {au}, “{ch}”, {pp}'
HBSU=lambda pp: HBC2('Sioux Until 1850','DeMallie',pp)
HBYK=lambda pp: HBC2('Yankton and Yanktonai','DeMallie',pp)
HBTE=lambda pp: HBC2('Teton','DeMallie',pp)
TETON7=['bru','ogl','min','hnk','sih','sna','twk']
SIOUX14=TETON7+['ynk','yku','ykl','mde','wpk','wpt','sis']
def _t6(g,y,p,who,basis='souls',**o):
    return dict(g=g,y=y,pop=p,raw=f'{who}: {p:,}',basis=basis,loc='inferred',at=(44.8,-98.0),r=400,src=HBSU('p. 748, table 6')+f', citing {who}',kind='primary',**o)
OBS += [
 # ---- before 1800
 dict(g=SIOUX14,y=1702,pop=20000,raw='Le Sueur, 1702: the Sioux number 4,000 families',basis='families × 5 (ours)',loc='inferred',at=(45.0,-94.5),r=300,src=HBSU('p. 748'),kind='primary'),
 dict(g=SIOUX14,y=1736,pop=9200,raw='1736: 300 Sioux men east of the Mississippi and 2,000 on the prairies',basis='men × 4 (ours)',loc='inferred',at=(45.0,-95.0),r=300,src=HBSU('p. 722'),kind='primary'),
 pl('ynk',1700.9,'Winter 1700–01: 150 lodges of Yankton winter with Le Sueur at Fort L’Huillier on the Blue Earth River; in May 1701, 200 lodges camp near the fort',(44.12,-94.05),15,HBSU('p. 726')),
 pl('wpk',1700.9,'Winter 1700–01: 60 lodges of Wahpekute Santee winter at Le Sueur’s Fort L’Huillier',(44.12,-94.05),15,HBSU('p. 726')),
 pl('mde',1748.0,'After abandoning Mille Lacs in the mid-18th century the Mdewakanton settle on the Rum River, and a few years later move their villages to the Mississippi and lower Minnesota (date ours)',(45.45,-93.5),40,HBSU('p. 727')),
 pl('mde',1765.0,'From the 1760s to 1851 the Mdewakanton villages stand on the Mississippi and the lower Minnesota (a range; centre ours)',(44.85,-93.25),35,HBSU('pp. 727–29')),
 pl('wpt',1765.0,'1760s: the Wahpeton villages on the Minnesota, above the Mdewakanton (a range; centre ours)',(44.6,-94.3),60,HBSU('p. 727')),
 pl('wpk',1765.0,'1760s: the Wahpekute villages on the Cannon River and at Traverse des Sioux (a range; centre ours)',(44.35,-93.75),45,HBSU('p. 729')),
 pl('sis',1800.0,'By 1800 the Sisseton on Big Stone Lake and Lake Traverse, joined by most of the Wahpeton (a range)',(45.55,-96.6),40,HBSU('pp. 727–29')),
 pl('wpt',1800.0,'By 1800 most of the Wahpeton have joined the Sisseton at Big Stone Lake and Lake Traverse (a range)',(45.4,-96.4),60,HBSU('p. 729')),
 pl('ynk',1760.0,'Mid-18th century: Yankton territory the lower Big Sioux and the heads of the Floyd, Little Sioux and Des Moines (a range; centre ours)',(43.4,-96.0),120,HBSU('p. 731')),
 *pls(['yku','ykl'],1760.0,'Mid-18th century: Yanktonai territory from Big Stone Lake and Lake Traverse west to the Missouri (a range; centre ours)',(45.6,-98.6),200,HBSU('p. 731')),
 pl('yku',1775.3,'Winter 1774–75: Peter Pond travels nine days up the Minnesota to a camp of Sioux he calls Yankton (“probably Yanktonai”), some 200 miles above his post (a camp; kept off the division track)',(44.95,-95.9),80,HBSU('p. 731'),whole=False),
 pl('bru',1804.9,'Winter 1804–05: Loisel trades with the Brule at his Fort aux Cedres on Cedar Island (Tabeau)',(44.08,-99.55),30,HBSU('p. 732')),
 *pls(['ogl','min'],1804.9,'Winter 1804–05: Hugh Heney trades with the Oglala and northern Teton at a post near the mouth of the Cheyenne (Tabeau)',(44.72,-100.62),40,HBSU('p. 732')),
 # ---- table 6
 _t6('mde',1805,2105,'Pike 1805'),_t6('wpk',1805,450,'Pike 1805'),_t6('wpt',1805,1060,'Pike 1805'),_t6('sis',1805,2160,'Pike 1805'),
 _t6(['ynk','yku','ykl'],1805,4300,'Pike 1805 (Yankton and Yanktonai together)'),_t6(TETON7,1805,11600,'Pike 1805 (Teton)'),
 _t6('mde',1820,1650,'Morse 1822'),_t6('sis',1820,1950,'Morse 1822'),_t6('ynk',1820,1000,'Morse 1822'),_t6(['yku','ykl'],1820,2500,'Morse 1822'),
 _t6('bru',1820,1500,'Morse 1822'),_t6(['sih','twk','sna','hnk'],1820,1500,'Morse 1822 (the Saone)'),
 _t6('mde',1823,1500,'Long in Keating 1825'),_t6('wpk',1823,800,'Long in Keating 1825'),_t6('wpt',1823,900,'Long in Keating 1825'),_t6('sis',1823,2500,'Long in Keating 1825'),
 _t6('ynk',1823,2000,'Long in Keating 1825'),_t6(['yku','ykl'],1823,5200,'Long in Keating 1825'),_t6(TETON7,1823,14400,'Long in Keating 1825 (Teton)'),
 _t6('wpk',1849,800,'Ramsey 1849'),_t6('wpt',1849,1500,'Ramsey 1849'),_t6('sis',1849,3800,'Ramsey 1849'),_t6('ynk',1849,3200,'Ramsey 1849'),
 _t6(['yku','ykl'],1849,4000,'Ramsey 1849'),_t6(TETON7,1849,6000,'Ramsey 1849 (Teton)'),
 *[_t6(g,1856,p,f'Warren 1856 ({p//8} lodges at 8 to a lodge)',basis='lodges × 8 (Warren)') for g,p in [('bru',3840),('ogl',2880),('sih',1280),('twk',800),('sna',1360),('ynk',2880),(['yku','ykl'],6400)]],
 _t6(['mde','wpk'],1868,1340,'ARCIA 1868'),_t6('ynk',1868,2500,'ARCIA 1868'),_t6('ykl',1868,2250,'ARCIA 1868 (Lower Yanktonai)'),_t6('yku',1868,2400,'ARCIA 1868 (Upper Yanktonai)'),
 _t6(['bru','ogl'],1868,12485,'ARCIA 1868 (Brule and Oglala on the Platte 7,885; Lower Brule 1,600; Oglala on the Missouri 3,000)'),
 _t6('min',1868,3060,'ARCIA 1868'),_t6('sih',1868,1200,'ARCIA 1868'),_t6('twk',1868,750,'ARCIA 1868'),_t6('sna',1868,720,'ARCIA 1868'),_t6('hnk',1868,3000,'ARCIA 1868'),
 # ---- Yankton and Yanktonai, 1850-80
 pl('ynk',1853.45,'June 1853: annuities at the mouth of the Vermillion; the Yankton, 375 lodges, live on both sides of the Missouri from the White River to Fort Pierre and hunt east to the James (a range; centre ours)',(43.9,-99.6),130,HBYK('pp. 777–78')),
 pl('ynk',1857.45,'June 1857: the Lower Yankton villages: Struck by the Ree’s main village just above the James, Smutty Bear’s a few miles upriver, Feather in the Ear’s 100 lodges above the Big Sioux, Mad Bull’s on the Vermillion (Redfield) (half the tribe; kept off the division track)',(42.88,-97.4),25,HBYK('p. 778'),whole=False),
 pl('ynk',1859.55,'July 1859: almost all the Yankton, nearly 2,000 people, at the new agency site (Greenwood) for the annuities',P['yankton_ag'],8,HBYK('p. 779')),
 dict(g='ynk',y=1859.55,pop=2000,raw='July 1859: almost all the Yankton present at Greenwood, “nearly 2,000 people” (Redfield)',basis='souls',loc='stated',at=P['yankton_ag'],r=8,src=HBYK('p. 779'),kind='primary'),
 pl('yku',1855.6,'1855: Little Soldier’s band of Upper Yanktonai has built a village of 12 earthlodges on the east bank of the Missouri near present Pollock, its first attempt at a fixed village (a band; kept off the division track)',(45.92,-100.29),8,HBYK('p. 780'),whole=False),
 pl('ykl',1855.6,'1855–56: Two Bears’s band of Lower Yanktonai lives above Little Soldier’s village, on the Missouri near present Pollock (Vaughan)',(46.1,-100.5),30,HBYK('p. 780')),
 pls(['yku','ykl'],1869.5,'1869: Two Bears’s Lower Yanktonai and the Upper Yanktonai of All Over Black and Big Head, with Hunkpapa and Blackfeet, settle at the new Grand River Agency at the mouth of the Grand',(45.63,-100.52),10,HBYK('p. 785'))[1],
 pl('yku',1869.8,'Autumn 1869: more than 1,000 Upper Yanktonai (Cuthead, Wazikute and Thakmi bands) come to Fort Buford, and winter there with the Lower Assiniboine',(47.98,-104.0),20,HBYK('p. 786')),
 pl('yku',1870.45,'June 1870: 2,500 Upper Yanktonai near Fort Buford',(47.98,-104.0),25,HBYK('p. 786')),
 dict(g='yku',y=1870.45,pop=2500,raw='June 1870: “there were 2,500 Upper Yanktonai near Fort Buford” (Morrow)',basis='souls',loc='stated',at=(47.98,-104.0),r=25,src=HBYK('p. 786'),kind='primary',whole=False),
 pl('ykl',1870.6,'August 1870: 375 lodges of Lower Yanktonai under Black Eye camped at the mouth of the Poplar River (part; kept off the division track)',(48.1,-105.2),15,HBYK('p. 786'),whole=False),
 *[dict(g=g,y=y,pop=p,raw=f'{lab}',basis='census',loc='stated',at=at,r=20,src=HBYK(pp),kind='primary',whole=False) for (g,y,p,lab,at,pp) in [
     ('ykl',1871,1000,'Crow Creek, 1871: 1,000 Lower Yanktonai on the reservation (Livingston); the rest at Grand River',P['crow_creek'],'p. 782'),
     ('ykl',1875,2730,'Standing Rock, 1875: 2,730 Lower Yanktonai',P['standing_rock'],'p. 786'),('yku',1875,1473,'Standing Rock, 1875: 1,473 Upper Yanktonai',P['standing_rock'],'p. 786'),
     ('ykl',1877,768,'Standing Rock, 1877: 768 Lower Yanktonai (during the war of 1876–77)',P['standing_rock'],'p. 786'),('yku',1877,462,'Standing Rock, 1877: 462 Upper Yanktonai (during the war of 1876–77)',P['standing_rock'],'p. 786'),
     ('ykl',1878.2,751,'Crow Creek, March 1878: 751 Lower Yanktonai at the agency (Dougherty)',P['crow_creek'],'p. 782'),('ykl',1879,900,'Crow Creek, 1879: 900 (Dougherty)',P['crow_creek'],'p. 782'),
     ('ykl',1881,1061,'Crow Creek, 1880–81: 1,061 after 140 were transferred, mostly from Standing Rock',P['crow_creek'],'p. 783')]],
 pl('ykl',1880.5,'Drifting Goose’s Lower Yanktonai band, which kept an earthlodge village on the James from about 1859, arrives at Crow Creek, 30 June 1880 (a band; kept off the division track)',P['crow_creek'],10,HBYK('pp. 782–83'),whole=False),
 # ---- Teton
 pl('hnk',1869.95,'Winter 1869–70: the Hunkpapa winter on the Yellowstone (a range; centre ours)',(46.6,-106.0),150,HBTE('p. 797')),
 pl('min',1876.69,'9 Sept. 1876: Mills attacks American Horse’s Minneconjou village at Slim Buttes, south of the Grand River (a village; kept off the division track)',(45.53,-103.17),5,HBTE('p. 799'),whole=False),
]
HBSA=lambda pp: HBC2('Santee','Albers',pp)
OBS += [
 *[dict(g=g,y=1810,pop=p,raw=f'Albers, early 1800s: {lab}',basis='souls',loc='inferred',at=at,r=80,src=HBSA('p. 761'),kind='secondary') for (g,p,lab,at) in [
     ('wpt',1500,'“the vast majority of the 1,500 Wahpeton lived along the lower reaches of the Minnesota River”',(44.6,-94.3)),
     ('sis',2500,'“most of the 2,500 Sisseton stayed in areas west of Lac qui Parle”',(45.5,-96.5)),
     ('wpk',600,'“the Wahpekute numbered no more than 600 people”, from the Cannon River southwest to the Blue Earth',(44.2,-94.0)),
     ('mde',2000,'“the 2,000 Mdewakanton were concentrated in fairly stable locations along the Mississippi and lower Minnesota rivers”',(44.85,-93.25))]],
 pls(['sis','wpt'],1873.5,'1873: Sisseton, Wahpeton and a few Mdewakanton who fled to Canada settle on the Sioux Valley (Oak River) and Birdtail Creek reserves, Manitoba (part; kept off the division track)',(49.9,-100.6),40,HBSA('p. 772'),whole=False)[0],
]

# ---------------- Handbook 13, part 2: Arapaho, Cheyenne, Crow, Gros Ventre ----------------
HBAP=lambda pp: HBC2('Arapaho','Fowler',pp)
HBCH=lambda pp: HBC2('Cheyenne','Moore, Liberty, and Straus',pp)
HBCW=lambda pp: HBC2('Crow','Voget',pp)
HBGV=lambda pp: HBC2('Gros Ventre','Fowler and Flannery',pp)
def _cnt(g,y,p,lab,src,at,r=60,basis='souls',kind='primary',**o):
    return dict(g=g,y=y,pop=p,raw=lab,basis=basis,loc='inferred',at=at,r=r,src=src,kind=kind,**o)
OBS += [
 # ---- Arapaho
 pl('ara',1795.0,'Truteau, 1795: the Arapaho (Caminanbiches) live on the headwaters of the Cheyenne River in western South Dakota and eastern Wyoming, near the Kiowa (a range; centre ours)',(43.7,-104.3),120,HBAP('p. 840')),
 pl('kio',1795.0,'Truteau, 1795: the Kiowa live near the Arapaho on the headwaters of the Cheyenne River (a range; centre ours)',(43.9,-104.0),200,HBAP('p. 840')),
 pl('ara',1800.5,'Tabeau, about 1800: the Arapaho live between the Yellowstone and the Platte (a range; centre ours)',(44.0,-106.0),250,HBAP('p. 840')),
 *pls(['ara','kio','kap'],1800.6,'About 1800: Arikara traders meet the Arapaho, Kiowa and Plains Apache at a trade fair in the Black Hills (Tabeau)',(44.1,-103.8),100,HBAP('p. 840')),
 *pls(['ara','chy'],1805.95,'Henry, 1806: the Cheyenne and Arapaho winter together in Arapaho territory, “probably at the foot of the Rockies in Wyoming and Colorado”, and part in spring when the Cheyenne go to trade at the Missouri villages (place Fowler’s guess)',(41.0,-105.2),200,HBAP('p. 840')),
 pl('ara',1811.0,'By 1811 the Arapaho range mainly along the North Platte and south as far as the Arkansas; the Cheyenne generally farther north (a range; centre ours)',(40.0,-104.8),250,HBAP('pp. 840–41')),
 *pls(['ars'],1851.7,'Under the 1851 treaty the Cheyenne and Arapaho range between the Platte and the Arkansas east to the head of the Republican; the Arapaho generally in the western part (a range; centre ours)',(39.5,-104.8),150,HBAP('p. 842')),
 pl('arn',1851.7,'Under the 1851 treaty the Cheyenne and Arapaho range between the Platte and the Arkansas east to the head of the Republican (a range; centre ours; kept off the Northern Arapaho track, which the dated Horse Creek council places on the North Platte)',(39.5,-104.8),150,HBAP('p. 842'),whole=False),
 pl('arn',1859.5,'After the Pikes Peak rush of 1858 the Northern Arapahoe withdraw north of the Platte into Wyoming and Montana, to the Bighorn country (a range; centre ours)',(44.5,-106.8),200,HBAP('p. 842')),
 pl('ars',1859.5,'After the Pikes Peak rush of 1858 the Southern Arapaho withdraw down the Arkansas (a range; centre ours)',(38.0,-100.5),150,HBAP('p. 842')),
 pl('arn',1878.2,'March 1878: the Northern Arapahoe arrive at the Wind River Reservation from Red Cloud Agency',(43.0,-108.6),20,HBAP('p. 843')),
 _cnt('ara',1835,3600,'Dodge, 1835: the Arapaho number “at least 3,600”',HBAP('p. 857'),(40.0,-104.8),r=200),
 _cnt(['arn','ars'],1854,2000,'ARCIA 1854: about 2,000, evenly divided between the Northern and Southern divisions, “one hundred and thirty lodges each”',HBAP('p. 857'),(40.5,-104.8),r=250),
 *[_cnt(g,y,p,lab,HBAP(pp),at,r=60,basis='census' if y>=1870 else 'souls') for (g,y,p,lab,at,pp) in [
     ('arn',1861,650,'ARCIA 1861: Northern Arapaho 650',(43.5,-106.5),'p. 857'),('ars',1861,1500,'ARCIA 1861: Southern Arapaho 1,500',(38.3,-101.5),'p. 857'),
     ('ars',1869,1100,'ARCIA 1869: Southern Arapaho about 1,100 (all Arapaho 1,440)',(35.6,-98.0),'p. 857'),
     ('ars',1872,1500,'ARCIA 1872: 1,500 at the agency in Indian Territory',(35.6,-98.0),'pp. 857–58'),
     ('arn',1874,1092,'ARCIA 1874: Northern Arapahoe 1,092',(42.9,-103.4),'p. 858'),('ars',1874,1644,'ARCIA 1874: Southern Arapaho 1,644',(35.6,-98.0),'p. 858'),
     ('arn',1887,988,'ARCIA 1887: Northern Arapahoe 988',(43.0,-108.6),'p. 858'),('ars',1887,1072,'ARCIA 1887: Southern Arapaho 1,072',(35.6,-98.0),'p. 858'),
     ('arn',1892,829,'ARCIA 1892: Northern Arapahoe 829',(43.0,-108.6),'p. 858'),('ars',1892,1091,'ARCIA 1892: Southern Arapaho 1,091',(35.6,-98.0),'p. 858')]],
 _cnt('arn',1872,1342,'ARCIA 1872: 1,342 at Red Cloud Agency (“probably too high an estimate”, Fowler)',HBAP('pp. 857–58'),(42.9,-103.4),r=40),
 # ---- Cheyenne
 pl('chy',1780.0,'1760–1850: the Cheyenne bands unite in the Black Hills; the Sacred Arrows come to them at Bear Butte, and the Sutaio join them (a range over ninety years; centre ours; kept off the division track, since Truteau still found the Cheyenne on the Missouri in 1795)',(44.3,-103.7),100,HBCH('p. 863'),whole=False),
 *[_cnt(g,y,p,lab,HBCH('p. 880, table 2'),at,r=r,basis='census' if y>=1870 else 'souls') for (g,y,p,lab,at,r) in [
     (['chn','chs'],1837,3200,'ARCIA 1837: 3,200',(40.5,-103.5),300),(['chn','chs'],1850,3000,'Schoolcraft: 3,000',(40.5,-103.5),300),
     ('chs',1863,1800,'Southern Cheyenne 1,800 (Mooney; ARCIA 1863)',(38.3,-101.0),150),
     ('chs',1875,2055,'Southern Cheyenne 2,055 (Mooney)',(35.6,-98.0),60),('chn',1875,1727,'Northern Cheyenne 1,727 (Mooney)',(44.5,-104.5),200),
     (['chn','chs'],1880,3887,'ARCIA 1880: 3,767 Southern (with the Northern Cheyenne then in Indian Territory) and 120 at Pine Ridge',(35.6,-98.0),300),
     ('chs',1890,2272,'ARCIA 1890: Southern Cheyenne 2,272',(35.6,-98.0),60),('chn',1890,865,'ARCIA 1890: Northern Cheyenne 865 (the Tongue River agency only)',(45.6,-106.7),40),
     ('chs',1900,2037,'ARCIA 1900: Southern Cheyenne 2,037',(35.6,-98.0),60),('chn',1900,1379,'ARCIA 1900: Northern Cheyenne 1,379',(45.6,-106.7),40)]],
 # ---- Crow
 pl('cwm',1825.0,'1820s: the Mountain Crow hunt about the Bighorn, middle Yellowstone, upper Tongue and Powder rivers and into the Bighorn, Absaroka, Beartooth and Wind River ranges (a range; centre ours)',(45.3,-107.4),200,HBCW('p. 695')),
 pl('cwr',1825.0,'1820s: the River Crow range over the lower Yellowstone and north along the Marias and Milk, turning to the Judith Basin for fall and winter hunting (a range; centre ours)',(47.4,-107.8),250,HBCW('p. 695')),
 pl('cwr',1835.5,'After Rotten Belly’s death at Fort McKenzie (1834) the River Crow may have drawn their range back to the Musselshell (a range; centre ours)',(46.8,-108.3),150,HBCW('p. 697')),
 pl('cwr',1849.95,'After Denig brokers peace about 1849, the Assiniboine let the Crow winter in Assiniboine territory (a range; centre ours)',(48.0,-106.0),200,HBCW('p. 698')),
 pl('cwm',1864.6,'August 1864: in the Pryor Mountains the Crow beat back a combined Teton, Arapaho and Cheyenne force',(45.1,-108.4),30,HBCW('p. 698')),
 pl('cwm',1870.5,'1870: the Mountain Crow must report to the Fort Parker Agency on Mission Creek near Livingston; they keep a seasonal hunt',(45.65,-110.35),15,HBCW('p. 698')),
 pl('cwr',1870.5,'1870: the River Crow must report to the Milk River Agency near Chinook; they keep a seasonal hunt',(48.5,-109.2),25,HBCW('p. 698')),
 *pls(['cwm','cwr'],1875.6,'1875: the Crow consolidated at a new agency on Rosebud Creek at Absarokee',(45.52,-109.44),15,HBCW('p. 698')),
 pl('cwm',1884.5,'1883–84: the Crow move to the present Crow Agency; Mountain Crow settle south of the agency at Reno, Pryor and the upper Bighorn, the Kicked in the Bellies at Lodge Grass and Wyola',(45.3,-107.8),35,HBCW('p. 698')),
 pl('cwr',1884.5,'1883–84: the Crow move to the present Crow Agency; River Crow settle north of it at Black Lodge, on the lower Little Bighorn and Bighorn',(45.67,-107.5),15,HBCW('p. 698')),
 _cnt(['cwm','cwr'],1779,9000,'Voget: “a population between 8,000 and 10,000 before the smallpox epidemics of 1781”',HBCW('p. 714'),(45.8,-107.5),r=250,kind='secondary'),
 _cnt(['cwm','cwr'],1850,5000,'Voget: “between 1830 and 1870 Crow population approximated 5,000”',HBCW('p. 714'),(45.8,-107.5),r=250,kind='secondary'),
 # ---- Gros Ventre
 pl('gv',1772.92,'Early December 1772: Cocking meets 28 tepees of Gros Ventre at a buffalo pound near the Eagle Hills; they have already split into winter bands (a band; kept off the division track)',(52.6,-108.6),30,HBGV('p. 678'),whole=False),
 pl('gv',1830.0,'By 1830 the last Gros Ventre bands, with the Piegan, are south of the Cypress Hills: a territory from the Judith River and the Bear Paw Mountains down the Missouri to the mouths of the Milk and Musselshell (a range; centre ours)',(47.9,-108.0),150,HBGV('p. 678')),
 pl('gv',1880.5,'1878–90: the Gros Ventre camp in three or four large bands along Cow, Peoples, Beaver, Snake and Clear creeks near Fort Belknap Agency',(48.2,-108.6),40,HBGV('p. 678')),
 *[_cnt('gv',y,p,lab,HBGV('p. 692, table 2'),at,r=r,basis='census' if y>=1860 else 'souls',**o) for (y,p,lab,at,r,o) in [
     (1805,2250,'Larocque 1805: 2,100–2,400',(49.5,-108.0),250,{}),(1823,4200,'Chesterfield House report 1822–23: 4,200',(49.5,-108.5),250,{}),
     (1830,3000,'Rowand 1830: 2,800–3,200 (“perhaps only the bands trading in British territory”)',(49.0,-108.5),250,{'whole':False}),
     (1835,4500,'Bradley: 4,000–5,000',(47.9,-108.0),200,{}),(1855,2970,'Fowler 1987: 2,970',(47.9,-108.0),150,{'kind':'secondary'}),
     (1860,2100,'ARCIA 1860: 2,100 (400 men, 700 women, 1,000 children)',(47.9,-108.0),150,{}),(1879,1135,'ARCIA 1879: 1,135',P['ft_belknap'],40,{}),
     (1895,624,'ARCIA 1896: 624',P['ft_belknap'],20,{})]],
]
EPI += [
 (1854.4,1854.9,'Smallpox and cholera, 1854 (Arapaho)',{'arn':.15,'ars':.15},
   HBAP('p. 857')+' (the Arapaho “further decimated by smallpox and cholera in 1854”: 3,600 in 1835, about 2,000 in 1854)','rate assumed'),
]

# ---------------- Handbook 13, part 2: Comanche, Kiowa, Plains Apache, Lipan ----------------
HBCO=lambda pp: HBC2('Comanche','Kavanagh',pp)
HBKI=lambda pp: HBC2('Kiowa','Levy',pp)
HBPP=lambda pp: HBC2('Plains Apache','Foster and McCollough',pp)
HBLI=lambda pp: HBC2('Lipan Apache','Opler',pp)
COM5=['cyy','cyk','cyp','cyn','cyq']
CPH=lambda pp: f'Kavanagh, Comanche Political History: An Ethnohistorical Perspective, 1706–1875 (1996), {pp}'
OBS += [
 # ---- Comanche
 _cnt('cyk',1786.3,8400,'Spring 1786: eight Kotsoteka rancherías of 700 lodges in an area 40 leagues square; “at 12 residents each, there were 8,400 persons”',HBCO('p. 900'),(35.3,-101.0),r=250,basis='lodges × 12 (Kavanagh)'),
 pl('cyk',1788.55,'July 1788: a Comanche village of 372 lodges on the upper Red River (Loomis and Nasatir; division ours)',(34.6,-100.6),80,HBCO('p. 900')),
 _cnt(COM5,1846,15600,'Butler and Lewis, final report, July 1846: Yamparika 500 lodges and 3,500 souls; Hois 400 and 2,800; Kotsoteka over 300 and 2,000; Noonah 250 and 2,750; Nokoni 250 and 1,750; Tenewa 400 and 2,800 (sum 15,600; Butler’s March letter had five bands of about 500 lodges at 5 a lodge, 12,500). Kavanagh calls the list confused and the figures unreliable; the Handbook gives 14,300',CPH('pp. 297–99'),(34.0,-100.5),r=300),
 _cnt('cyp',1859.6,384,'August 1859: 384 Penatika Comanches moved from the Brazos reserve to the Wichita Agency at Fort Cobb (the reserve Comanches only)',HBCO('p. 888'),(35.1,-98.45),r=15,whole=False),
 *pls(['cyy','cyq'],1874.4,'Spring 1874: the Yamparika, Kwahada and other Comanches convene on Elk Creek in western Oklahoma before the attack on the hunters at Adobe Walls',(35.2,-99.35),25,HBCO('p. 889')),
 # ---- Kiowa
 _cnt('kio',1875,1000,'1875: the Kiowa and Plains Apache together 1,414, “the Kiowa accounting for about 1,000”',HBKI('p. 921'),(34.9,-98.6),r=60,basis='census'),
 # ---- Plains Apache
 pl('kap',1717.0,'Vermale’s map of 1717 shows 10 Padouca villages north of the Pawnee villages; earlier maps had put the Plains Apacheans south of the Pawnee (a range; centre ours)',(42.5,-100.0),250,HBPP('p. 928')),
 pl('kap',1785.0,'Miró, 1785: the “Pados” in “small forts” near the Bad River, in four small wandering groups (the first unambiguous reference to the Plains Apache)',(44.3,-101.0),100,HBPP('p. 928')),
 _cnt('kap',1785,1400,'Miró, 1785: the Pados “number about three hundred and fifty men”',HBPP('p. 928'),(44.3,-101.0),r=100,basis='men × 4 (ours)'),
 pl('kap',1796.0,'Truteau, 1796: the Pados live on the southwest branch of the Platte (a range; centre ours)',(40.5,-103.8),150,HBPP('p. 928')),
 _cnt('kap',1820,375,'Morse, 1820: the Cataka 375 (not first-hand)',HBPP('p. 937'),(38.5,-101.0),r=300),
 _cnt('kap',1835,1200,'Dodge, 1835: 1,200 “Appachees of the Plains”',HBPP('p. 938'),(37.5,-100.5),r=250),
 *[_cnt('kap',y,p,lab,HBPP('p. 938'),at,r=r,basis='census',**o) for (y,p,lab,at,r,o) in [
     (1861,415,'Boone, 1861: 60 lodges, 415 people',(38.0,-100.0),200,{}),
     (1867.8,516,'Medicine Lodge, 1867: 86 lodges, 516 people (“probably the most accurate”; some absent)',(37.25,-98.58),40,{}),
     (1869,288,'1869: 288 camped on the Kiowa-Comanche-Apache Reservation',(35.0,-98.4),40,{'whole':False}),
     (1874,602,'1874: twelve bands, 602 (most absent from the reservation)',(35.0,-98.4),150,{}),
     (1880,332,'1880: 332',(35.0,-98.4),40,{}),(1900,173,'1900: 173',(35.0,-98.4),30,{})]],
 # ---- Lipan
 _cnt('lip',1700,6000,'Opler: “a judicious estimate of all Lipan Apache in 1700, including those living in Mexico, would be about 6,000”',HBLI('p. 945'),(31.0,-100.0),r=300,kind='secondary'),
 _cnt('lip',1736,8000,'M.H. Wright: about 8,000 in 1736',HBLI('p. 945'),(30.5,-100.0),r=300,kind='secondary'),
 _cnt('lip',1762,3500,'1762: the two leaders at the El Cañón missions had 700 followers, and ten other local groups were known: “between 3,000 and 4,000 Lipans living in central Texas” (Tunnell and Newcomb)',HBLI('p. 942'),(29.7,-99.9),r=200,kind='secondary'),
 _cnt('lip',1807,1250,'Sibley, 1807: 1,200–1,300 Lipans between the Llano and the San Saba, with 200–250 warriors',HBLI('p. 945'),(30.9,-99.6),r=60,whole=False),
 pl('lip',1807.0,'Sibley, 1807: Lipans between the Llano and the San Saba (part)',(30.9,-99.6),60,HBLI('p. 945'),whole=False),
 _cnt('lip',1820,3500,'Morse, 1820: 3,500 between the Rio Grande and the sources of the Nueces',HBLI('p. 945'),(29.3,-100.2),r=150),
 pl('lip',1820.0,'Morse, 1820: the Lipan between the Rio Grande and the sources of the Nueces (a range; centre ours)',(29.3,-100.2),150,HBLI('p. 945')),
 pl('lip',1822.5,'By 1822 the alliance with the Comanche has failed; the Lipan flee farther south beyond the line of Spanish settlement (a range; centre ours)',(28.0,-99.0),150,HBLI('p. 943')),
 pl('lip',1828.0,'1828: Cuelgas de Castro’s Lipans, about 150 families, travel continually between Goliad and Laredo (part)',(28.1,-98.5),80,HBLI('p. 945'),whole=False),
 _cnt('lip',1830,2000,'Berlandier, about 1830: 400 families (400 men)',HBLI('p. 945'),(28.5,-99.5),r=200,basis='families × 5 (ours)'),
 pl('lip',1840.0,'1840: Lipans range between the Guadalupe and the Rio Grande, about 200 warriors or 1,000 people (Nance) (a range; centre ours)',(29.2,-99.0),120,HBLI('p. 945')),
 _cnt('lip',1847,900,'1847: the Lipan “raise about 200 warriors of their own band” (800–1,000 people)',HBLI('p. 945'),(29.5,-98.8),r=200,basis='warriors × 4–5 (Opler)'),
 _cnt('lip',1849,500,'Neighbors, 1849: 100 warriors and 500 people',HBLI('p. 945'),(29.5,-98.8),r=200),
 pl('lip',1850.0,'By the mid-19th century the Lipan have moved north again to the Colorado above Austin, hunting east to the Brazos with the Tonkawa (a range; centre ours)',(30.6,-97.9),90,HBLI('p. 941')),
 pl('lip',1873.38,'18 May 1873: Mackenzie crosses into Mexico and destroys a Lipan encampment with Mescalero and Kickapoo villages (Remolino, Coahuila; site approximate)',(28.95,-100.95),25,HBLI('p. 944')),
 pl('lip',1883.5,'1883: 19 Lipans camp with 79 Tonkawas at Fort Griffin (part; kept off the division track)',(32.92,-99.22),5,HBLI('p. 944'),whole=False),
]
EPI += [
 (1764.3,1764.9,'Smallpox, 1764 (Texas)',{'lip':.2},HBLI('p. 943')+' (“in 1764 an outbreak of smallpox devastated the mission area”); Swagerty, Handbook 13 (2001), p. 257 (1762–66 outbreak infecting the Lipan)','rate assumed'),
 (1895.9,1896.4,'Measles, 1895–96 (Kiowa)',{'kio':.15,'kap':.15},HBKI('p. 921')+' (“in 1896, 15 percent of the population died in a measles epidemic”, after Mooney)','sourced for the Kiowa; assumed for the Plains Apache'),
 (1901.0,1901.5,'Measles, 1901 (Comanche)',{g:.065 for g in COM5},HBCO('p. 901')+' (“measles in 1901 took 98 lives” of 1,499)','sourced'),
]
HBEN=lambda pp: HBC2('Enigmatic Groups','Parks',pp)
OBS += [
 pl('kap',1820.61,'11 Aug. 1820: Long’s party on the Canadian meets a large band of Kaskaias (“Bad-hearts”), who “frequent the country about the sources of the Platte, Arkansa, and Rio Del Norte”; Parks judges the Kaskaia most likely Plains Apache (identity probable; kept off the division track)',(35.45,-102.5),40,JAMES.replace('vol. 1','vol. 2')+', pp. 102–8; identification '+HBEN('pp. 972–73'),whole=False),
]
# ADDITIONS: eighteenth-century places for the peoples whose pre-1800 tracks rested on keyframes alone
HBGU=lambda pp: HBC('Plains Village Tradition: Western Periphery','Gunnerson',pp)
ESK='Encyclopedia of Saskatchewan, “Cocking, Matthew (1743–99)”; DCB, “Cocking, Matthew”'
OBS += [
 # Plains Cree
 pl('crw',1772.6,'Cocking travels inland with Pegogamaw Cree, “who met their families at the well-known rendezvous at present James Smith First Nation”, summer 1772 (the Pegogamaw a band of the Saskatchewan Cree, filed with the Fort des Prairies division; a band, kept off the division track)',(53.0,-104.6),30,ESK,whole=False),
 pl('crw',1772.9,'From the rendezvous the Pegogamaw make a circuit west to the Eagle Hills and the Thickwood Hills, “hunting out on the open plains southwest of modern Biggar”, autumn–winter 1772–73',(52.0,-108.3),90,ESK,whole=False),
 pl('crw',1773.3,'The circuit ends at a bison pound near Red Deer Hill, south of Prince Albert, spring 1773',(53.1,-105.7),25,ESK,whole=False),
 pl('crw',1755.17,'Henday, with his Cree guide Attickasish and Cree companions, reaches the North Saskatchewan near the mouth of the Sturgeon River, 3 Mar. 1755, and camps while canoes are built; “more fur-laden Indians arrived”; leaves 27 Apr.',(53.73,-113.2),30,WP('Anthony Henday')),
 # Plains Ojibwe
 pl('ojb',1785.0,'“As early as the 1780s, Ojibwas were observed at trading posts along the Assiniboine River catering to a largely Plains clientele” (a range; centre ours)',(49.85,-98.6),150,HBOJ('pp. 652–53')),
 pl('ojb',1795.0,'“By the 1790s, a steadily growing number were utilizing the prairies west of the Red River as far as the Pembina Hills”; also reported on the Souris, Qu’Appelle and Saskatchewan, but not settled there until the 19th century (a range; centre ours)',(49.1,-97.9),110,HBOJ('p. 653')),
 # Jicarilla
 pl('jic',1706.55,'Ulibarrí, leaving Taos on 20 July 1706, meets “several friendly Apache bands, probably Jicarilla” on “the upper courses of the Canadian and Cimarron rivers” (identification probable; centre ours)',(36.45,-104.6),90,WP('Juan de Ulibarrí')),
 pl('jic',1715.0,'Before about 1730 the Jicarilla and Carlana, “close relatives” of the Cuartelejo and Paloma, “lived in fixed villages along the foothills of the Sangre de Cristo Mountains” (a range; centre ours)',(36.5,-105.0),100,HBGU('p. 244')),
]
OBS += [
 pl('sho',1851.71,'Horse Creek (Fort Laramie) treaty council, Sept. 1851: Washakie’s Shoshone attend without signing (a visit by part of the people; kept off the division track)',(41.93,-104.0),25,WP('Treaty of Fort Laramie (1851)')+' (Shoshone attendance recalled)',whole=False),
 pl('lip',1904.5,'“In 1904, 37 more Lipans reached Mescalero, the remnants of a band that had been living in Coahuila, Mexico” (ARCIA 1905)',(33.15,-105.7),20,HBLI('p. 944')),
]
OBS += [
 _cnt(['cyy','cyk','cyp'],1829,11000,'Late 1820s: Ruiz puts the Texas Comanche at 1,000–1,500 families, and Berlandier at 10,000–12,000 “for the same” (Berlandier’s figure is usually read as the whole nation; applied to the three divisions then distinguished)',HBCO('pp. 900–901'),(34.0,-100.0),r=400),
]
# Comanche, 1785–1904: Hämäläinen, The Comanche Empire (2008), read in full text, with Kavanagh's figures in Handbook 13.
# Hämäläinen's figures for c. 1849 (“near the twenty-thousand level”, p. 293) and 1870 (“four or five thousand”, p. 339) rest on
# Neighbors 1849 and Tatum 1870, which are already records; they are not entered again, so those counts are not weighted twice.
HM='Hämäläinen, The Comanche Empire (2008)'
OBS += [
 _cnt(COM5[:3]+['cyj'],1785,25000,'Mid-1780s: “according to Spanish observers, the western Comanches alone numbered between sixteen and eighteen thousand, while a 1785 account states that the eastern Comanches had two thousand fighting men, which translates into a total eastern Comanche population of some eight thousand”',HM+', p. 102',(35.0,-101.0),r=400,kind='secondary'),
 _cnt(['cyy','cyk','cyp'],1830,25000,'“Most estimates in the 1820s and 1830s put it between twenty and thirty thousand”',HM+', p. 179',(34.5,-100.5),r=400,kind='secondary'),
 _cnt(COM5,1865,5000,'“As many as four thousand Comanches may have perished during the early 1860s, leaving a total population of only five thousand in 1865”',HM+', p. 313',(35.0,-100.5),r=400,kind='secondary'),
 _cnt(COM5,1900,1499,'“In 1900, there were 1,499 Comanches, but measles in 1901 took 98 lives. The low point of 1,399 was reached in 1904”',HBCO('p. 901'),P['ft_sill'],r=40,basis='census'),
 _cnt(COM5,1904,1399,'“The low point of 1,399 was reached in 1904”',HBCO('p. 901'),P['ft_sill'],r=40,basis='census'),
]
EPI += [
 (1848.2,1848.8,'Smallpox, 1848 (Comanchería)',{**{g:.05 for g in COM5}},'Hämäläinen, The Comanche Empire (2008), p. 302: “In 1848, three years into a dry spell, smallpox ravaged Comanchería, and in 1849 a virulent cholera epidemic … carried away uncounted numbers”; Kavanagh, “Comanche”, Handbook 13 (2001), p. 902: “L.H. Williams (1849) and R.S. Neighbors (1849) reported that the 1848–1849 smallpox-cholera epidemic killed 300”','event sourced; the only contemporary count (300 deaths for both years) is taken as a floor, and 5% a year applied for 1848 and 1849 (rate ours)'),
 (1850.0,1861.0,'Drought and famine, 1850–60 (Comanchería)',{**{g:.35 for g in COM5}},'Hämäläinen, The Comanche Empire (2008), ch. 7, pp. 294–302 and n. 9 (p. 431): a drought from 1845, the collapse of the southern bison herds and malnutrition that lowered fertility, so that “Comanches’ population dropped in the 1850s and 1860s from around 20,000 to below 5,000”','decline sourced; the rate is scaled so that, with the 1848–49 and early-1860s losses, Hämäläinen’s series is reproduced (ours)'),
 (1871.0,1874.0,'Hunger and war, 1871–73 (Comanchería)',{**{g:.15 for g in COM5}},'Hämäläinen, The Comanche Empire (2008), pp. 339–40: the population “plummeted from four or five thousand in 1870 to around fifteen hundred in 1875” through “a systematic assault on the Comanches’ economy”; Kavanagh, Comanche Political History (1996), pp. 471–73: 3,742 in Dec. 1870 (1,000 of them an estimate of those never reported) and 2,643 at the census of March 1874','decline sourced; rate ours'),
 (1874.5,1875.5,'Red River War and surrender, 1874–75 (Comanchería)',{**{g:.3 for g in COM5}},'Kavanagh, Comanche Political History (1996), p. 473, and Handbook 13 (2001), p. 901: 2,643 at the census of March 1874, 1,721 in 1875 (1,556 south of the Washita and 165 Penateka at the Wichita agency); Hämäläinen, p. 339: “only a few hundred casualties” in battle, the rest hunger, flight and loss of the herds','decline sourced; rate ours (part of the fall is people not yet counted in 1875)'),
]

# ---------------------------------------------------------------------------------------------
# U.S. Census Office, Report on Indians Taxed and Indians Not Taxed (1894): the special Indian census of 1 June 1890,
# read from the page images of each state's table “Indian population of reservations”. Dated 1890.42 (1 June), so a count
# is never summed with an Indian Office figure for 1890. Figures identical to an 1890 record already present (Crow 2,287;
# Kansa 198; Otoe and Missouria 358; Iowa 165 + 102 = 267; Southern Cheyenne 2,272) are not entered again. The table's
# footnote splitting the Cheyenne and Arapaho reservation (“Cheyennes, 1,091; Arapahos, 2,272”, p. 528) reverses the Indian
# Office figures for the same year (Cheyenne 2,272, Arapaho 1,091) and is not used.
CEN90=lambda pp: f'U.S. Census Office, Report on Indians Taxed and Indians Not Taxed in the United States … at the Eleventh Census: 1890 (1894), {pp}, “Indian population of reservations”'
def c90(g,p,raw,pp,at,r=40,**o):
    return dict(g=g,y=1890.42,pop=p,raw='Census of 1 June 1890: '+raw,basis='census',loc='stated',at=at,r=r,src=CEN90(pp),kind='primary',**o)
OBS += [
 # South Dakota, p. 573
 c90('ogl',5016,'Pine Ridge reservation, “Ogalalla Sioux, 4,488; mixed bloods, 528”','p. 573',P['pine_ridge']),
 c90('bru',6012,'Rosebud reservation 5,381 (“Brule Sioux No. 1, 1,288; Brule Sioux No. 2, 750; Loafer Sioux, 1,052; Wazhazhah Sioux, 1,184; Two Kettle Sioux, 228; Northern Sioux, 167; mixed bloods, 762”), less the Two Kettle and Northern (Oglala) Sioux, plus Lower Brule reservation 1,026','p. 573',P['rosebud'],r=120),
 c90(['min','sna','twk','sih'],3622,'Cheyenne River reservation, “Blackfeet Sioux, Sans Arcs Sioux, Minneconjou Sioux, and Two Kettle Sioux”, 2,823; with the Blackfeet Sioux at Standing Rock (571, p. 509) and the Two Kettle at Rosebud (228)','pp. 509, 573',P['chyR_agency'],r=120),
 c90('ynk',1725,'Yankton reservation, “Yankton Sioux”, 1,725','p. 573',P['yankton_ag']),
 c90(['wpt','sis'],2084,'Lake Traverse reservation, “Sisseton and Wahpeton Sioux”, 1,522 (p. 573); at Devils Lake, Sisseton 420 and Wahpeton 142 (p. 509)','pp. 509, 573',P['sisseton'],r=120),
 # North Dakota, p. 509
 c90('hnk',1739,'Standing Rock reservation, “Uncapapa (Hunkpapa) Sioux”, 1,739','p. 509',P['standing_rock']),
 c90(['yku','ykl'],4383,'Yanktonai: Standing Rock 1,786 and Crow Creek (“Lower Yanktonnai Sioux”) 1,058 (pp. 509, 573); Fort Peck “Yankton Sioux” (the Upper Yanktonai) 1,121 (p. 356); at Devils Lake, Cuthead 295 and “Yankton” 123 (p. 509)','pp. 356, 509, 573',(46.5,-101.0),r=300),
 c90('man',251,'Fort Berthold reservation, “Mandan”, 251','p. 509',P['like_fishhook']),
 c90('hid',690,'Fort Berthold reservation, “Gros Ventre” (Hidatsa) 522, and “Dull Knife’s band of Gros Ventres” 168, “nominally at Fort Berthold, but roaming” (Crow Flies High’s band)','p. 509',P['like_fishhook']),
 c90('ari',447,'Fort Berthold reservation, “Arickaree”, 447','p. 509',P['like_fishhook']),
 c90('ojb',1458,'Turtle Mountain reservation, “Chippewas and Crees, 251; Chippewas, Crees, and other mixed bloods, many perhaps belonging in Canada, 1,197”','p. 509',P['turtle_mt']),
 # Montana, p. 356
 c90('ass',1673,'Assiniboine: Fort Belknap 952 and Fort Peck 719 (p. 356), and 2 at Devils Lake (p. 509)','pp. 356, 509',(48.3,-106.5),r=150),
 c90('gv',770,'Fort Belknap reservation, “Gros Ventre”, 770','p. 356',P['ft_belknap']),
 c90('pik',1811,'Blackfeet reservation, “Piegan”, 1,811 (the South Piegan of Montana only; the North Piegan were on their Alberta reserve)','p. 356',P['blackfeet_ag'],whole=False),
 c90('chn',1382,'Northern Cheyenne: Tongue River reservation 865 (p. 356) and Pine Ridge reservation 517 (p. 573)','pp. 356, 573',P['lame_deer'],r=150),
 # Wyoming, p. 627
 c90('sho',916,'Wind River reservation, “Shoshone, Eastern band”, 916','p. 627',P['wind_res']),
 c90('arn',885,'Wind River reservation, “Arapaho, Northern”, 885','p. 627',P['wind_res']),
 # Nebraska, p. 373, and Oklahoma, p. 528
 c90('oma',1158,'Omaha reservation, “Omaha”, 1,158','p. 373',P['omaha_res']),
 c90('pon',822,'Ponca reservation, Oklahoma, 605 (p. 528), and “Ponca of Dakota” on the Niobrara, 217 (p. 373)','pp. 373, 528',P['ponca_ok'],r=300),
 c90(['pwc','pwk','pws'],804,'Pawnee reservation, “Pawnee”, 804','p. 528',P['pawnee_ok']),
 c90(['osg','osl'],1509,'Osage reservation, “Osage”, 1,509','p. 528',P['pawhuska']),
 c90('kio',1140,'Kiowa and Comanche reservation, “Kiowa”, 1,140','p. 528',P['ft_sill']),
 c90(COM5,1598,'Kiowa and Comanche reservation, “Comanche”, 1,598','p. 528',P['ft_sill']),
 c90('kap',326,'Kiowa and Comanche reservation, “Apache”, 326','p. 528',P['ft_sill']),
 # New Mexico, p. 396
 c90('jic',808,'Jicarilla Apache reservation, “Jicarilla (Apache)”, 808','p. 396',(36.93,-107.0)),
]
# The Indian Office's 1890 Northern Cheyenne figure counts the Tongue River agency only; 517 more were at Pine Ridge (above).
for _o in OBS:
    if _o['g']=='chn' and _o['y']==1890 and _o['pop']==865: _o['whole']=False

# ---------------------------------------------------------------------------------------------
# Four peoples added from Handbook 13 (2001), read chapter by chapter in the PDF supplied by the project's owner:
# Dempsey, “Sarcee” (pp. 629–37); Getty and Gooding, “Stoney” (pp. 596–603); Newcomb and Campbell, “Tonkawa” (pp. 953–64);
# Parks, “Kitsai” (pp. 567–71). Where a chapter gives tents or warriors without a ratio, the multiplier is ours and the basis says so.
FAM['tonkawan']=9; FAMNAME['tonkawan']='Tonkawa (isolate)'
GROUPS += [
 ('sar','Sarsi','Tsuut’ina (Sarsi)','athabaskan',1700,1905,'nomadic'),
 ('sto','Stoney','Mountain Stoney (Nakoda)','dakotan',1700,1905,'nomadic'),
 ('tkw','Tonkawa','Tonkawa','tonkawan',1700,1905,'nomadic'),
 ('kit','Kitsai','Kitsai','caddoan',1700,1894,'village'),
]
HBSA=lambda pp: HBC('Sarcee','Dempsey',pp)
HBST=lambda pp: HBC('Stoney','Getty and Gooding',pp)
HBTO=lambda pp: HBC2('Tonkawa','Newcomb and Campbell',pp)
HBKT=lambda pp: HBC('Kitsai','Parks',pp)
OBS += [
 # ---- Sarsi
 pl('sar',1790.5,'Umfreville, 1790: “a small tribe which has separated from the main body, and now harbor in some country about the Stony [Rocky] Mountains” (a range; centre ours)',(52.3,-114.3),200,HBSA('p. 629')),
 pl('sar',1815.5,'1815: Sarsi hunting grounds “the territory between the Red Deer and Battle rivers, bounded on the east by Beaverhill Lake and on the west by the Rocky Mountains” (HBC 1967; a range, centre ours)',(52.55,-113.6),130,HBSA('p. 629')),
 pl('sar',1855.5,'By the mid-19th century the Sarsi “normally hunted along the Red Deer and Bow rivers” (a range; centre ours)',(51.4,-113.4),110,HBSA('pp. 629, 635')),
 pl('sar',1877.72,'Treaty No. 7, Blackfoot Crossing, Sept. 1877: signed for the Sarsi by Bull Head',(50.77,-112.87),10,HBSA('p. 635')),
 pl('sar',1883.5,'1883: the Sarsi receive their own reserve just west of Calgary, 108 square miles',(50.95,-114.25),10,HBSA('p. 635')),
 _cnt('sar',1785,650,'1780s: 90 tents, 650 people (Thompson in Glover 1962:240)',HBSA('p. 636, table 2'),(52.5,-113.5),r=200),
 _cnt('sar',1801,480,'1801: 35 tents, 120 men (Mackenzie 1802)',HBSA('p. 636, table 2'),(52.5,-113.5),r=200,basis='warriors × 4 (ours)'),
 _cnt('sar',1801.1,500,'1801: 70 tents (Fidler); at Thompson’s 7.2 to a tent from the same table',HBSA('p. 636, table 2'),(52.5,-113.5),r=200,basis='tents × 7.2 (Thompson’s ratio in the same table; ours)'),
 _cnt('sar',1810,600,'1810: 90 tents, 150 men (Henry in Coues 1897)',HBSA('p. 636, table 2'),(52.5,-113.4),r=200,basis='warriors × 4 (ours)'),
 _cnt('sar',1824,720,'1824: 100 tents (Franklin 1824)',HBSA('p. 636, table 2'),(52.4,-113.4),r=200,basis='tents × 7.2 (ours)'),
 _cnt('sar',1841,350,'1841: 50 tents, 100 men, 350 people (Simpson 1841)',HBSA('p. 636, table 2'),(51.8,-113.4),r=200),
 _cnt('sar',1843,350,'1843: 45 tents, 350 people (Rowand)',HBSA('p. 636, table 2'),(51.8,-113.4),r=200),
 _cnt('sar',1859,360,'1859: 45 tents, 360 people (Hind 1859)',HBSA('p. 636, table 2'),(51.5,-113.4),r=150),
 _cnt('sar',1869.5,420,'1870: 40 tents, 420 people (Sully 1870; taken as the count before the epidemic of winter 1869–70)',HBSA('p. 636, table 2'),(51.4,-113.4),r=150),
 _cnt('sar',1871,86,'1870: 12 tents (Butler 1874:370); “in 1869–1870 another smallpox epidemic reduced the number of Sarcee lodges from 50 to 12”',HBSA('pp. 635–36'),(51.4,-113.4),r=150,basis='tents × 7.2 (ours)'),
 _cnt('sar',1877.72,255,'Treaty No. 7, 1877: “a total of 255 Sarcee were entered on the Canadian government rolls”',HBSA('p. 635'),(50.77,-112.87),r=20,basis='census'),
 # ---- Stoney
 pl('sto',1754.9,'Winter 1754–55: Henday, wintering in central Alberta, “acknowledged the assistance of ‘Assiniboine’ families who were doubtless Stoneys” (place ours)',(52.4,-113.6),150,HBST('p. 596')),
 pl('sto',1845.5,'1840–48: Rundle travels each summer along the foothills from Rocky Mountain House to the Bow River, preaching to the Stoney (a range; centre ours)',(51.8,-114.8),110,HBST('pp. 596–97')),
 pl('sto',1873.5,'1873: the McDougalls’ Methodist mission at Morleyville on the Bow, where the Stoney reserve was surveyed in 1879',(51.16,-114.85),10,HBST('p. 597')),
 pl('sto',1877.72,'Treaty No. 7, Blackfoot Crossing, Sept. 1877: three Stoney chiefs attend (Bearspaw, Chiniki, Wesley)',(50.77,-112.87),10,HBST('p. 596')),
 pl('sto',1879.5,'1879: the Stoney reserve at Morley, 109 square miles on the Bow about 30 miles from Calgary',(51.16,-114.85),10,HBST('p. 596')),
 _cnt('sto',1877.72,556,'556 in 1877 (Treaty Paylist 1877); “there are no reliable population statistics from before the reserve period”',HBST('p. 602'),(51.16,-114.85),r=40,basis='census'),
 _cnt('sto',1885,647,'647 in 1885 (Department of Indian Affairs 1886)',HBST('p. 602'),(51.16,-114.85),r=40,basis='census'),
 _cnt('sto',1895,570,'570 in 1895 (Department of Indian Affairs 1897)',HBST('p. 602'),(51.16,-114.85),r=40,basis='census'),
 # ---- Tonkawa
 pl('tkw',1719.6,'1719: du Rivage, 70 leagues up the Red River near present Paris, Texas, meets warriors of five groups, among them Tonkawa and Yojuane, returning from an attack on Apaches farther west (a war party; kept off the track)',(33.66,-95.55),40,HBTO('p. 954')+'; '+HBKT('p. 567'),whole=False),
 pl('tkw',1758.2,'March 1758: Tonkawas join the Comanche, Taovaya and others in sacking the San Sabá mission (a raid; kept off the track)',(30.92,-99.79),10,HBTO('p. 955'),whole=False),
 pl('tkw',1768.5,'1768: Fray Gaspar José de Solís visits encampments of Coco, Mayeye, Tonkawa, Yojuane and others on the Brazos northwest of modern College Station',(30.85,-96.6),40,HBTO('pp. 953–54')),
 pl('tkw',1828.4,'1828: the Mexican boundary survey visits a Tonkawa village about halfway between the Guadalupe and Colorado rivers, allied with the Lipan (Berlandier)',(29.85,-97.65),40,HBTO('p. 955')),
 pl('tkw',1855.0,'1854–55: the Tonkawa are moved to the Brazos reservation at the junction of the Clear Fork',(33.1,-98.7),15,HBTO('p. 955')),
 pl('tkw',1859.6,'1859: escorted with the other Brazos reservation Indians north across the Red River to the Wichita Agency in the Leased District',(35.1,-98.45),20,HBTO('p. 955')),
 pl('tkw',1867.5,'1867: the Tonkawa gather around newly established Fort Griffin on the Clear Fork of the Brazos, rationed by the army for scouting',(32.93,-99.23),10,HBTO('p. 955')),
 pl('tkw',1885.3,'Spring 1885: moved from the Iowa reservation to the former Nez Perce reservation on the Chikaskia River in northern Oklahoma',(36.68,-97.31),15,HBTO('pp. 955–56')),
 _cnt('tkw',1772,600,'1772: “something more than 150 warriors, which included Mayeyes and Yojuanes” (Bolton 1914)',HBTO('p. 956'),(31.2,-96.8),r=150,basis='warriors × 4 (ours)'),
 _cnt('tkw',1810,1000,'“Apparently Tonkawa population was fairly stable from the late eighteenth century into the third decade of the following century, hovering around 1,000 persons”',HBTO('p. 956'),(30.8,-96.9),r=150,kind='secondary'),
 _cnt('tkw',1849,650,'1849: estimated at 650, including 130 warriors (Winfrey and Day)',HBTO('p. 956'),(30.5,-97.6),r=150),
 _cnt('tkw',1859.6,245,'1859: “about 245 Tonkawas” escorted from the Brazos reservation to the Wichita Agency',HBTO('p. 955'),(35.1,-98.45),r=20),
 _cnt('tkw',1863,165,'1863: about 165, including about 50 warriors (Winfrey and Day)',HBTO('p. 956'),(32.9,-99.0),r=100),
 _cnt('tkw',1884.5,92,'1884: 92 survivors, “including some Lipan Apaches”, moved to Indian Territory from Fort Griffin',HBTO('p. 955'),(32.93,-99.23),r=20),
 _cnt('tkw',1891,73,'1891: “the 73 surviving Tonkawa were each allotted approximately 160 acres”',HBTO('p. 956'),(36.68,-97.31),r=15,basis='census'),
 c90('tkw',76,'Oakland reservation, “Tonkawa and Lipans”, 76','p. 528',(36.68,-97.31),r=15),
 # ---- Kitsai
 pl('kit',1718.5,'1718: Bienville lists a Kitsai group living with several Caddo groups in a single village 150 leagues up the Red River (place ours)',(33.4,-94.1),60,HBKT('p. 567')),
 pl('kit',1745.5,'1745: Ortiz places the Kitsai on the upper Trinity, Brazos and Red rivers (a range; centre ours)',(33.0,-96.9),150,HBKT('p. 568')),
 pl('kit',1772.3,'1772: De Mézières’ first stop, the Kitsai village on the east side of the Trinity near present Palestine, Texas',(31.78,-95.85),15,HBKT('p. 568')),
 pl('kit',1778.5,'1778: a small Kitsai village of 20 warriors, separated from the larger one, near present Grand Saline, Texas (part of the people)',(32.67,-95.71),10,HBKT('p. 568'),whole=False),
 pl('kit',1820.5,'1820 and 1828: still living east of the Trinity, trading at Nacogdoches and Trinidad (a range; centre ours)',(31.8,-95.8),50,HBKT('p. 568')),
 pl('kit',1841.4,'1841: Texans attack the Kitsai and Waco villages on the West Fork of the Trinity near present Arlington',(32.75,-97.1),10,HBKT('p. 568')),
 pl('kit',1846.5,'1846: on the Brazos, 100 miles north of Comanche Peak (P.M. Butler; place ours)',(33.4,-98.5),50,HBKT('p. 568')),
 pl('kit',1851.5,'1851: Stem reports only 38 Kitsai on the Brazos reservation; “two-thirds of the tribe had joined the Wichita and were living in the Wichita Mountains”',(34.8,-98.6),40,HBKT('p. 568')),
 pl('kit',1859.6,'1859: the remaining Kitsai moved from the Brazos reservation to the Wichita Agency, “located on the site of an old Kitsai village”',(35.1,-98.45),15,HBKT('p. 569')),
 _cnt('kit',1772.3,320,'1772: the Trinity village “comprised 30 lodges and 80 warriors” (De Mézières)',HBKT('p. 568'),(31.78,-95.85),r=20,basis='warriors × 4 (ours)'),
 _cnt('kit',1778.01,360,'Council of war at San Antonio, 5 Jan. 1778 (Merino y Moreno, secretary): the Kitsai 90 warriors (a compiled estimate)',BOLTON('vol. 2, pp. 165–66 (pdf 171–72)')+'; '+HBKT('p. 570'),(31.8,-95.85),r=60,basis='warriors × 4 (ours)'),
 _cnt('kit',1805,240,'1805: 60 warriors (Sibley 1832)',HBKT('p. 570'),(31.8,-95.85),r=60,basis='warriors × 4 (ours)'),
 _cnt('kit',1809,220,'1809: 50–60 warriors (Salcedo)',HBKT('p. 570'),(31.8,-95.85),r=60,basis='warriors × 4 (ours)'),
 _cnt('kit',1849,300,'1849: a total population of 300 (Schoolcraft)',HBKT('p. 570'),(33.5,-98.2),r=200),
 _cnt('kit',1855,500,'1855: 500 (Whipple, Ewbank and Turner)',HBKT('p. 570'),(34.0,-98.4),r=200),
 _cnt('kit',1857,300,'1857: 300 (ARCIA 1857)',HBKT('p. 570'),(34.5,-98.5),r=150),
 _cnt('kit',1893,52,'“By 1893 the population had dropped to 52 individuals” (Mooney 1896)',HBKT('p. 570'),(35.1,-98.3),r=30,basis='census'),
 c90(['wic','kit'],424,'Wichita reservation: “Wichita and affiliated Towaconie” 150, “Keechie and Wichita” 66, “Waco and Wichita” 34, “Wichita” 174','p. 528',P['anadarko'],r=40),
]
EPI += [
 (1780.6,1782.0,'Smallpox, 1780–82 (Sarsi and Stoney)',{'sar':.55,'sto':.55},'Fenn, Pox Americana (2001), ch. 6: the rate sourced for their neighbours (no figure for either people)','assumed, at the rate used for their neighbours'),
 (1837.45,1838.0,'Smallpox, 1837–38 (Sarsi and Stoney)',{'sar':.5,'sto':.25},'Dempsey, “Sarcee”, Handbook 13 (2001), p. 635: “They suffered a major loss during the smallpox epidemic of 1837–1838” (100 tents in 1824, 50 in 1841, p. 636); Stoney: none stated','Sarsi scaled from the tent counts; Stoney assumed, as the Northern Assiniboine'),
 (1870.6,1870.9,'Smallpox, 1870 (Sarsi)',{'sar':.45},'Dempsey, “Sarcee”, Handbook 13 (2001), p. 635: lodges reduced “from 50 to 12”; 420 people in 1870 before it and 255 on the 1877 roll (p. 636); dated by Jenness, The Sarcee Indians of Alberta (1938), pp. 7–8, whose informant places the outbreak in the late summer of 1870, when the berries were ripening','scaled between the lodge count and the 1877 roll (ours)'),
 (1862.8,1862.85,'Attack on the Tonkawa near Anadarko, Oct. 1862',{'tkw':.4},'Newcomb and Campbell, “Tonkawa”, Handbook 13 (2001), p. 955: “Some 137 men, women, and children were killed”; about 245 had come north in 1859','sourced (fraction of about 300 to 340)'),
 (1801.3,1802.3,'Smallpox, 1801–02 (Kitsai)',{'kit':.3},'Morse via Mooney: the Wichita and Caddo suffered “almost as severely” as the prairie tribes, who lost more than half; Kitsai warriors fall from 90 (1770s) to 60 (1805), Parks, “Kitsai”, Handbook 13 (2001), p. 570','assumed'),
 (1845.5,1846.5,'Smallpox and war, 1845–46 (Kitsai)',{'kit':.2},'Parks, “Kitsai”, Handbook 13 (2001), p. 568: in 1846 the Kitsai had “suffered a loss in population because of smallpox and war with Texans” (P.M. Butler)','event sourced; rate assumed'),
]
GUESS['sar']=[g(1700,(54.6,-113.0),800,'Parkland edge: hunting on the plains, wintering with the Beaver (Dempsey)'),g(1740,(53.6,-112.8),900,'Cut off from the Beaver by the Cree advance; allied with the Blackfoot'),
              g(1772.9,(52.8,-111.0),800,'Cocking’s “Equestrian Indians”, 1772–73'),g(1782,None,450,'1780–82 smallpox'),g(1840,(51.9,-113.5),370,''),g(1866,(51.3,-113.3),420,'Travelling into Montana with the Blackfoot (Doty; Dempsey)'),
              g(1879,(50.95,-114.25),240,'Common reserve on the Bow with the Blood and Blackfoot, then their own'),g(1900,(50.95,-114.25),200,'Tuberculosis; 160 by 1924'),g(1905,(50.95,-114.25),190,'')]
GUESS['sto']=[g(1700,(53.4,-111.0),700,'Allied with the Plains Cree; “groups migrating west to the mountains to escape the diseases” (Bearspaw tradition)'),g(1740,(52.8,-113.0),800,''),
              g(1782,None,400,'1780–82 smallpox (assumed)'),g(1800,(52.2,-114.6),550,'Foothills from Rocky Mountain House south toward the Bow'),g(1837,None,650,''),g(1838,None,500,'1837–38 smallpox (assumed)'),
              g(1860,(51.7,-114.9),550,''),g(1905,(51.16,-114.85),580,'Morley reserve')]
GUESS['tkw']=[g(1700,(34.0,-97.6),900,'By 1691 south at least to the Red River (Casañas); in 1601 north-central Oklahoma'),g(1730,(33.0,-96.9),850,'Entering Texas at the north end of the Blackland Prairie'),
              g(1760,(31.6,-96.9),800,'Along the grassland–woodland edge; absorbing the Yojuane after 1759'),g(1790,(31.0,-96.8),1000,'Not much south of the Brazos–Little River junction until late in the century'),
              g(1840,(30.3,-97.8),800,'Pushed west by Anglo settlement after 1836'),g(1874,(32.93,-99.23),120,'Fort Griffin scouts')]
GUESS['kit']=[g(1700,(33.2,-95.6),500,'Upper Trinity and Red River country (du Rivage, Bienville)'),g(1760,(32.3,-96.0),450,''),g(1800,None,330,''),
              g(1830,(31.9,-95.9),200,'East of the Trinity until the end of the 1820s'),g(1836,(32.8,-97.4),190,'North to the upper Trinity and Brazos'),
              g(1870,(35.1,-98.3),120,'With the Wichita at the Wichita Agency'),g(1885,(35.1,-98.3),70,'')]

# ---------------------------------------------------------------------------------------------
# Eastern Shoshone and Jicarilla from their Handbook chapters (read in the PDFs supplied by the project's owner):
# Shimkin, “Eastern Shoshone”, Handbook of North American Indians, vol. 11, Great Basin (1986), pp. 308–35;
# Tiller, “Jicarilla Apache”, Handbook of North American Indians, vol. 10, Southwest (1983), pp. 440–61.
HB11=lambda pp: f'D’Azevedo, ed., Handbook of North American Indians, vol. 11: Great Basin (1986), Shimkin, “Eastern Shoshone”, {pp}'
HB10=lambda pp: f'Ortiz, ed., Handbook of North American Indians, vol. 10: Southwest (1983), Tiller, “Jicarilla Apache”, {pp}'
OBS += [
 # ---- Eastern Shoshone
 pl('sho',1805.6,'1805: Larocque meets 20 Shoshone lodges visiting the Mandan with a much larger Crow party; they travel together to the Bighorn (a visiting party; kept off the track)',(45.6,-107.6),80,HB11('pp. 308–9'),whole=False),
 pl('sho',1821.5,'1821: Jacob Fowler sees Shoshones at a large trading rendezvous dominated by Comanches on the upper Arkansas (a trading visit; kept off the track)',(38.3,-104.6),60,HB11('p. 309'),whole=False),
 pl('sho',1837.5,'1837: O. Russell, travelling with them, gives the Shoshone country as “all the regions drained by the head branches of Green and Bear Rivers and the east and southern head branches of the Snake River” (a range; centre ours)',(42.5,-110.6),150,HB11('p. 309')),
 _cnt('sho',1837.5,3000,'1837: “the leadership of the Buffalo Eaters Pah-da-hewakunda and Mawoma over 3,000 Shoshones was beginning to break up” (after O. Russell)',HB11('p. 311'),(42.5,-110.6),r=150),
 _cnt('sho',1840,3000,'The Eastern Shoshone fell “from a population of perhaps 3,000 in 1840 to 800 in 1900”',HB11('p. 308'),(42.5,-109.8),r=200,kind='secondary'),
 # ---- Jicarilla
 pl('jic',1700.5,'1700: the name first recorded, when Governor Rodríguez Cubero has a condemned man’s head set on a pole at Taos to warn the “apaches de la xicarilla” (their mountains northeast of Taos; place ours)',(36.6,-105.3),40,HB10('p. 449')),
 pl('jic',1733.5,'1733: a mission founded for the Jicarilla five leagues north of Taos; the governor soon drives them back into the mountains',(36.62,-105.57),10,HB10('p. 450')),
 pl('jic',1752.5,'1752: Jicarilla trading at Pecos with the Carlana (a trading visit; kept off the track)',(35.55,-105.68),10,HB10('p. 450'),whole=False),
 pl('jic',1850.5,'1850: Jicarilla hunting territory “extending from the Arkansas River, south to Mora, New Mexico, and from the Canadian River on the east to Chama, New Mexico, on the west” (a range; centre ours)',(36.8,-105.0),160,HB10('p. 450')),
 pl('jic',1855.69,'10 Sept. 1855: treaty of peace with the Jicarilla and Ute signed at Abiquiu',(36.21,-106.32),10,HB10('p. 451')),
 pl('jic',1883.64,'20 Aug. 1883: all the Jicarilla removed to the Mescalero Apache reservation',(33.15,-105.77),20,HB10('p. 452')),
 _cnt('jic',1846.8,500,'1846: Charles Bent reports “about 100 lodges of 500 Jicarillas throughout New Mexico”',HB10('p. 451'),(36.5,-105.4),r=150),
 _cnt('jic',1900,815,'1900: 815 (Jicarilla Apache tribal census rolls)',HB10('p. 454, table 1'),(36.93,-107.0),r=30,basis='census'),
]

# ---------------------------------------------------------------------------------------------
# Kavanagh, Comanche Political History (1996), read in full in the PDF supplied by the project's owner.
# Table 7.12 (pp. 472–73) gives band populations by division for Nov. 1869 (Badger), Dec. 1870 (Tatum) and March 1874,
# the last a census taken for Agent Haworth, who thought its total “not above their actual number”. Tatum's 1870 total is
# already a record. Divisions as Kavanagh assigns them; the Detsakana go with the Yamparika and the Tenewa with the Nokoni.
OBS += [
 _cnt(COM5,1838.4,20000,'Bonnell, Texan commissioner of Indian affairs, after a trading trip to one village, 1838: “We learned from them that the Nation consisted of about 20,000 souls and could raise about 5,000 warriors” (hearsay in a polemical letter, Kavanagh says)',CPH('p. 228'),(33.5,-99.5),r=400),
 _cnt('cyp',1846,2800,'Butler and Lewis 1846: the “Hooish” (Hois, the Penateka) “about 400 lodges, averaging about seven to the lodge making about 2800 souls”, probably on Neighbors’s information; “the only pre-epidemic count … it is unreliable”',CPH('pp. 299, 332, 385'),(31.5,-98.8),r=150),
 _cnt('cyp',1854.6,1200,'1854: the “whole Southern Band”, including Ketumsee, Potsanaquahip and Sanaco, “consisted of 1,200 people”',CPH('p. 385'),(33.2,-99.2),r=120),
 _cnt(['cyy','cyk'],1856.5,3200,'Whitfield, 1856: the Arkansas River Comanches, 400 lodges, 800 men, 1,200 women, 3,200 in all (the northern divisions trading on the Arkansas only)',CPH('p. 381, table 6.10'),(37.8,-99.5),r=150,whole=False),
 _cnt(['cyk','cyq'],1866.8,2000,'Norton, New Mexico superintendent, 1866: “a large body (about two thousand) continually occupying the eastern portion of this territory” under Mowway, Puertas and others (the New Mexico-trading Kotsoteka and Kwahada only)',CPH('pp. 405–6'),(35.0,-103.0),r=150,whole=False),
 _cnt(COM5,1869.9,4445,'Badger’s list, Nov. 1869: 1,927 present, 558 absent, and an estimated 1,960 never reported, off the reservation',CPH('pp. 472–73, table 7.12'),P['ft_sill'],r=200),
 _cnt('cyy',1874.2,1228,'March 1874 census (Haworth): Yamparika bands 1,128 and Detsakana 100',CPH('p. 472, table 7.12'),P['ft_sill'],r=60,basis='census'),
 _cnt('cyn',1874.2,322,'March 1874 census (Haworth): Nokoni bands 272 and Tenewa 50',CPH('p. 472, table 7.12'),P['ft_sill'],r=60,basis='census'),
 _cnt('cyk',1874.2,310,'March 1874 census (Haworth): Kotsoteka bands under Mowway, Kawertzeme, Black Duck and Prairie Fire, 310',CPH('p. 472, table 7.12'),P['ft_sill'],r=60,basis='census'),
 _cnt('cyq',1874.2,649,'March 1874 census (Haworth): Kwahada bands 649, besides those still out',CPH('p. 472, table 7.12'),P['ft_sill'],r=60,basis='census'),
 _cnt('cyp',1874.2,195,'March 1874 census (Haworth): Penateka under Seichinicah and Asatoyet, 195; the bands of Asehabit and Tosaway were at the Wichita agency and not counted',CPH('p. 473, table 7.12'),P['ft_sill'],r=60,basis='census',whole=False),
]

# ---------------------------------------------------------------------------------------------
# West, The Contested Plains (1998), read in full in an EPUB-derived PDF supplied by the project's owner; it carries no print
# page numbers, so it is cited by chapter. Chapter 4 is the Cheyenne history (the annual cycle, the winter camps, 1849);
# chapters 8 and 10–11 the Dog Soldiers, the 1850s and the war of 1864–69.
WEST2=lambda ch: f'West, The Contested Plains: Indians, Goldseekers, and the Rush to Colorado (1998), {ch}'
# Winfrey and Day, eds., The Indian Papers of Texas and the Southwest, vol. 1 (1825–43), read in the PDF supplied by the
# project's owner. Its counts are of chiefs and escorts at councils, not of peoples; what it adds is places, above all
# Eldredge's report of his 1843 journey to the Comanche (doc. 211, pp. 251–71), which finds the Wichita, Waco, Tawakoni
# and Kitsai villages and Pahayuko's Penateka camp, none of them otherwise fixed in the 1840s.
TIP1=lambda pp: f'Winfrey and Day, eds., The Indian Papers of Texas and the Southwest, 1825–1916, vol. 1 (1966; repr. 1995), {pp}'
OBS += [
 *pls(['chs','ogl','bru'],1848.3,'Spring 1848: Fitzpatrick finds “a string of Lakota and Cheyenne villages with thousands of horses strung out for nearly eighty miles along the South Platte, plus another twenty miles up Lodgepole Creek” (a range; centre ours)',(40.75,-103.0),70,WEST2('ch. 4'),whole=False),
 *pls(['chs','ars'],1848.87,'Nov. 1848: “an estimated 6,000 Indians” camp at the Arkansas “big timbers” in weather “cruelly, bitterly cold… snowing and freezing” (the timbers ran some sixty miles down from near the mouth of the Purgatoire; centre ours)',(38.08,-102.6),40,WEST2('chs. 4, 9')),
 pl('chs',1857.47,'Early July 1857: Sumner’s column finds on Beaver Creek, a tributary of the Republican, the great lodge the Cheyennes had built a few weeks earlier for their sun dance (place ours)',(39.85,-101.0),50,WEST2('ch. 1')),
 pl('chs',1857.58,'End of July 1857: Sumner finds the Cheyenne village abandoned fifteen miles south of the Solomon battlefield; nearly 200 lodges still standing are burned',(39.13,-99.95),10,WEST2('ch. 1')),
 pl('chs',1858.0,'Winter 1857–58: most Cheyennes flee south of the Arkansas and live and hunt among the Kiowas and Comanches until spring (a range; centre ours)',(36.8,-99.8),200,WEST2('ch. 1')),
 pl('kio',1859.71,'16 Sept. 1859: William Bent meets Kiowa and Comanche leaders at the great bend of the Arkansas, “more than 2,500 warriors” camped nearby',(38.36,-98.77),30,WEST2('ch. 8')),
 pl('cyy',1859.71,'16 Sept. 1859: Kiowas and Comanches camped at the great bend of the Arkansas, more than 2,500 warriors (the Comanches there not named; part)',(38.36,-98.77),30,WEST2('ch. 8'),whole=False),
 pl('chs',1862.95,'Winters of 1861–64: the reservation bands, the minority who signed at Fort Wise, drift back each fall to the agency at Point of Rocks, just upstream from Bent’s Old Fort, and hunt in summer with the militants on the Smoky Hill, Republican and Solomon (place ours; part)',(38.05,-103.3),25,WEST2('ch. 11'),whole=False),
 pl('chs',1864.69,'Sept. 1864: Wynkoop’s meeting with the Cheyenne leaders “at the big timbers of the Smoky Hill” (placed by Fort Wallace, which West puts near those timbers; centre ours)',(38.9,-101.5),30,WEST2('ch. 11')),
 pl('kio',1868.54,'July 1868: Satanta’s party of 108 Kiowas, camped “at what had been the heart of the Arkansas big timbers”, approaches Fort Lyon (part)',(38.08,-102.65),20,WEST2('ch. 11'),whole=False),
 # ---- Texas Indian Papers, vol. 1
 pl('cyp',1839.12,'15 Feb. 1839: Moore’s rangers and Castro’s Lipans attack a Comanche village “on a small Stream called Spring Creek, in the valley of the San Saba”, found from the Colorado above the mouth of the Llano (centre ours)',(31.2,-98.85),25,TIP1('pp. 57–59, doc. 32')),
 pl('kit',1843.4,'May 1843: a Keechi hunting party under the principal chief camps within a few miles of José María’s Anadarko village, “on a western branch of the Trinity about eight miles from the main river”; the tribe’s main body is “residing on the Brazos and Trinity” (a range; centre ours)',(32.9,-97.8),60,TIP1('pp. 254, 256, 263')),
 pl('wic',1843.43,'5–10 June 1843: the Waco village and, four miles from it, the Tawakoni village “on a very high hill”, its hundred acres of corn, beans, melons and pumpkins “in the bottom of one of the branches of the Trinity”; Eldredge dates a letter “Tawakoni Village, Trinity River, June 11, 1843” (reached by the Santa Fe Expedition’s trail north from Comanche Peak; centre ours)',(33.05,-97.75),35,TIP1('pp. 214, 256–57')),
 pl('wic',1843.61,'11 Aug. 1843: Eldredge crosses Cache Creek “near the mountains” and camps by the Wichita or Tawehash village, most of its warriors away hunting and raiding',(34.7,-98.4),20,TIP1('p. 262')),
 pl('kit',1843.62,'Aug. 1843: “about four miles distant” from the Wichita village, “a settlement of Keechi, who becoming dissatisfied with the balance of their tribe residing on the Brazos and Trinity seceded, elected a Chief of their own and moved up here to live” (part)',(34.7,-98.35),20,TIP1('p. 263'),whole=False),
 pl('cyp',1843.6,'4–9 Aug. 1843: Pahayuko’s camp south of the Red River, a few miles from the crossing, “in the open prairie on the bank of a small creek”, covering “about half a mile”; the Penateka chief signs an armistice there on 9 Aug. (centre ours)',(34.0,-98.9),60,TIP1('pp. 229–30, 265–67')),
]
EPI += [
 (1867.6,1868.2,'Cholera, 1867–68 (Wichita)',{'wic':.15},WEST2('ch. 12')+': a Wichita village “contracted cholera from the soldiers escorting them to a reservation on the Washita River. More than 100 died”; it broke out again on the way, and so many died at one camp that it was called Skeleton Creek','event sourced; the rate ours (more than 100 of a confederacy counted at 572 in 1868)'),
]

# ---------------------------------------------------------------------------------------------
# Second set of sources read in PDFs supplied by the project's owner: Bolton's De Mézières papers (1914); Henday, Cocking
# and La Vérendrye in Burpee's editions; Ewers (BAE 159); Denig (BAE 46); Jenness (1938); Texas Indian Papers vols. 2–5.
# Extracted with a verbatim quotation and page for each record; the comment above a record gives the identification and
# placement judgments. Councils, visits, parties and single bands are partial (whole=False) and stay off the tracks.
OBS += [
 # ---- Bolton, ed., Athanase de Mézières (1914)
  # wic = Tawakoni + Iscani subgroups only. Describes the situation c.1769-early 1770 (driven south by Osage raids). A broad triangle San Saba–San Antonio–La Bahía; centre and radius ours. Shows Wichita southern subgroups, T
 dict(g=['wic', 'tkw', 'kit'],y=1769.9,pop=None,raw='it has come to pass that in despair the Tuacanas, Yscanis, Tancaoueys, and Quitseys have retreated toward the south until they are now in the neighborhood of the presidios of San Saba, Bexar, and Espiritu Santo (place ours) (part)',basis='',loc='stated',at=(30.0, -98.0),r=150,src=BOLTON('vol. 1, pp. 167-168 (pdf 174-175), Doc. 30'),kind='primary',whole=False),
  # Tawakoni and Iscani subgroups. San Pedro = San Pedro de los Nabedachos (upper Neches, ~31.55,-95.25); 'off to one side, not far' – placed west of it toward the Trinity (ours). De M. adds they 'have taken refuge in the di
 dict(g='wic',y=1770.8,pop=None,raw='the Tuacanas and Yscanis, immediately upon learning of the wish of the great Captain of La Luiziana, have abandoned the establishment which they had in the vicinity of San Antonio de Vexar and San Saba and are to-day living off to one side, not far from San Pedro (place ours) (part)',basis='',loc='stated',at=(31.6, -95.5),r=50,src=BOLTON('vol. 1, p. 212 (pdf 219); cf. p. 214 (pdf 221), Doc. 69'),kind='primary',whole=False),
  # Taovaya subgroup, hearsay ('I am informed'); they had deserted their Red River village (where they buried Parrilla's cannon). Region between Red and Arkansas rivers – centre and wide radius ours. Bolton (fn 318) doubts t
 dict(g='wic',y=1770.8,pop=None,raw="the Tavai'ases, who, although they form with the foregoing a single nation, live apart for greater convenience in hunting ... have gone to the interior, far to the north, seeking asylum in the dark solitudes which lie between the Natchitoches and Akensas Rivers (place ours) (part)",basis='',loc='stated',at=(35.3, -97.0),r=200,src=BOLTON('vol. 1, p. 215 (pdf 222), Doc. 69'),kind='primary',whole=False),
  # Rumour via Nacogdoches Indians. Earliest dated mention in the volume of Panis-mahas (Skidi?) joining the Taovaya. Placed at Taovaya village by us; low value as a place record.
 dict(g='wic',y=1770.45,pop=None,raw="the Taoua'iches nation has been joined recently by another numerous tribe from the Missuris, namely, the Panis-maha, and that these two, having joined the Tuacanas, Caranamez, and Maheys, have gone at the instigation of the Comanchez (place ours) (part)",basis='',loc='stated',at=(33.947, -97.626),r=80,src=BOLTON('vol. 1, p. 202 (pdf 209), Doc. 66'),kind='primary',whole=False),
  # Iscani subgroup of Wichita; dispersed homesteads ('estancias') not a village. 8 leagues W of Kitsai, east of the Trinity; coords ours.
 dict(g='wic',y=1772.28,pop=240,raw='Having found the Iscanis scattered about and settled on different farms, I encouraged them to unite to form a single village ... They comprise sixty warriors, and many more women and children. ... They live at a distance of eight leagues westward from the Quitseys pueblo. (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(31.85, -95.95),r=30,src=BOLTON('vol. 1, pp. 286, 289 (pdf 293, 296), Doc. 90'),kind='primary',whole=False),
  # Tawakoni ('Toicanne') + Xaraname ('Anamas') village, 100 leagues from the Taovaya. Location not stated; presumably Brazos or Trinity Tawakoni village (ours, wide radius).
 dict(g='wic',y=1774.6,pop=None,raw='it will be necessary for this purpose even to have in the village of the Toicanne and the Anamas, who have united, a trader ... the convoy which was going to the Toicanne a hundred leagues distant from the Panis (place ours) (part)',basis='',loc='stated',at=(31.6, -97.0),r=150,src=BOLTON('vol. 2, p. 97 (pdf 103), Doc. 136'),kind='primary',whole=False),
  # Rumour only. Bolton fn 120 notes the Little Osage split off about this time and moved to the Missouri. Possibly an early report of an Arkansas-River Osage settlement (cf. osa from 1802). Coords and radius ours; low weigh
 dict(g=['osg', 'osl'],y=1774.67,pop=None,raw='The rumor is spreading among the Indians that the Osages have abandoned their ancient village in order to form another far distant from the first, and far up the Rio de los Arkansas. (place ours) (part)',basis='',loc='stated',at=(37.3, -95.5),r=250,src=BOLTON('vol. 2, p. 110 (pdf 116), Doc. 145'),kind='primary',whole=False),
  # Lipan range late 1777 straddling the Rio Grande near San Juan Bautista (Guerrero, Coah.), Aguaverde and Monclova; centroid ours. Same council: 'the whole body of the Apaches would number as many as five thousand warriors
 dict(g='lip',y=1777.94,pop=None,raw='these Lipanes, Natages, and Mescaleros, are known as Apaches de Oriente [Eastern Apaches] ; that the first live on both sides of the Rio Grande del Norte, under shelter of the presidios of San Juan Bautista, Monclova, and Santa Rosa de Aguaverde, part of them withdrawing at times to the Parage de la Nogalera (place ours)',basis='',loc='stated',at=(28.6, -100.6),r=120,src=BOLTON('vol. 2, p. 153 (pdf 159), Doc. 165'),kind='primary'),
  # Rio Puerco = Pecos (Bolton fn 202). Lipan refuge at Pecos–Rio Grande confluence; coords ours.
 dict(g='lip',y=1778.14,pop=None,raw='the first division may go towards the junction of Rio Puerco with the Rio Grande, the asylum most frequented by the Lipan (place ours) (part)',basis='',loc='stated',at=(29.7, -101.37),r=60,src=BOLTON('vol. 2, p. 183 (pdf 189), Doc. 167'),kind='primary',whole=False),
  # Tawakoni first village (later named El Quiscat, Doc. 225), on the W bank of the Brazos 'protected from the overflows of the river ... by a high, thick wall, at whose base rises a spring'; Bolton (vol. 1 p. 114) 'evidentl
 dict(g='wic',y=1778.26,pop=600,raw='Marching sixteen leagues in the same direction, west, from El Parage de la Tortuga ... I arrived at the bank of the River Brazos de Dios ... the Tuacanas, who have settled on the opposite bank ... This village contains about one hundred fifty warriors. (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(31.56, -97.13),r=15,src=BOLTON('vol. 2, pp. 193, 195 (pdf 199, 201), Doc. 171'),kind='primary',whole=False),
  # Tawakoni second village (Puesto Mayor; called El Flechazo in 1779, Doc. 225). 8 leagues upstream of the first; coords ours (Brazos above Waco, McLennan Co.). Population: 'exceed the former' (>150 warriors).
 dict(g='wic',y=1778.27,pop=None,raw='Continuing in the same westward direction, at a distance of eight leagues above the former village I found another settlement of the Tuacanas on the bank of the same Brazos River ... The character of the people, who exceed the former in number, is the same (place ours) (part)',basis='',loc='stated',at=(31.72, -97.33),r=20,src=BOLTON('vol. 2, pp. 196-197 (pdf 202-203), Doc. 172'),kind='primary',whole=False),
  # Eastern Comanche bands living on the Brazos above (upstream of) the Tawakoni, spring 1778; three bands had 'gone into the interior' (p. 197). Coords ours. Bolton (vol. 1 p. 116) also says Comanche were 'some distance up 
 dict(g='cyp',y=1778.27,pop=None,raw='They complain bitterly of the continued thieving of the Comanches, who have settled in large numbers on the same river, the Brazos (place ours) (part)',basis='',loc='stated',at=(32.3, -98.0),r=120,src=BOLTON("vol. 2, p. 195 (pdf 201); cf. p. 212 (pdf 218): 'eight of the Comanches who live above the Tuacanas on the bank of the Brazos River', Docs. 171 & 181"),kind='primary',whole=False),
  # Tonkawa hunting near the Brazos by the Tawakoni (Quiscat) village, Sept 1779. Chief died in epidemic; El Mocho (adopted Apache) now head chief; promised to settle at La Tortuga.
 dict(g='tkw',y=1779.68,pop=None,raw='Two leagues from the first village of the Tuacanas I met a large party of the Tancagues, who were awaiting me there. They at once dispatched messengers and made signals with smoke, in order to report my arrival to others, who were hunting in the vicinity. (place ours) (part)',basis='',loc='stated',at=(31.55, -97.05),r=15,src=BOLTON('vol. 2, p. 269 (pdf 275), Doc. 222'),kind='primary',whole=False),
  # Tonkawa party (75 Tonkawa and Xaraname went to Bexar with De M., Bolton vol. 1 p. 119) escorted back to the Colorado en route to 'their lands' (north). Coords = Colorado crossing (ours). Part only.
 dict(g='tkw',y=1779.8,pop=None,raw='set out for the Colorado River to accompany the Tancagues, who were returning to their lands (which precaution was taken by the chevalier governor, in view of the threats made by the Lipanes, who were staying in this vicinity, watching them (place ours) (part)',basis='',loc='stated',at=(30.25, -97.7),r=80,src=BOLTON('vol. 2, p. 322 (pdf 328), Doc. 238'),kind='primary',whole=False),
  # Some Lipan near San Antonio de Béxar in October 1779 (a band, not the division). Coords Béxar (ours).
 dict(g='lip',y=1779.8,pop=None,raw='the Lipanes, who were staying in this vicinity, watching them and intending to attack them on their way out (place ours) (part)',basis='',loc='stated',at=(29.42, -98.49),r=60,src=BOLTON('vol. 2, p. 322 (pdf 328), Doc. 238'),kind='primary',whole=False),
  # Taovaya village on the Red ('Natchitoches') River, 60 leagues NE of the Wichita village; hearsay (not visited). Placed at Spanish Fort site (ours); Bolton (vol. 1 pp. 48-49, 223 fn 318) puts the Taovaya town 'on the Red 
 dict(g='wic',y=1772.36,pop=None,raw='The other, called the village of the Taouaiaz, is sixty leagues farther up towards the northeast, on the banks of the Natchitoches River, at the foot of a ridge which furnishes this river its chief supply of water. (place ours)',basis='',loc='stated',at=(33.947, -97.626),r=15,src=BOLTON('vol. 1, p. 294 (pdf 301), Doc. 90'),kind='primary'),
  # 'Usually camped' – habitual campground in the Monte Grande (Galván) timber belt between the San Xavier (San Gabriel) and the Brazos, near Little River mouth (Bolton fn 424). Coords ours (Milam Co.).
 dict(g='tkw',y=1772.5,pop=None,raw='a spring called Las Puentecitas, in whose neighborhood the nation of the Maheyes, Yocuanas, and Tancagues is usually camped (place ours)',basis='',loc='stated',at=(30.75, -96.85),r=30,src=BOLTON('vol. 1, p. 308 (pdf 315), Doc. 90 (itinerary appended)'),kind='primary'),
  # Main Kitsai village 1779, 15 leagues from San Pedro de los Nabedachos, 'distant two leagues' from the Trinity ford; Bolton fn 331 infers W of the Trinity; Bolton intro calls it 'the Kichai village on the Trinity'. Coords
 dict(g='kit',y=1779.66,pop=None,raw='Being now in the village of the Quitseis, I am going to continue for the Tuacanas by the same route as last year. (place ours)',basis='',loc='stated',at=(31.65, -95.95),r=25,src=BOLTON('vol. 2, p. 265 (pdf 271), Doc. 217'),kind='primary'),
  # Eastern Comanche gathering under chief Evea (Euea/Puvea) at or near the Wichita village (Ouedsita) on the upper Brazos, spring 1772. Ripperda (Doc. 95, July 5, 1772, vol. 1 p. 320) confirms Evea 'assembled with more than
 dict(g='cyp',y=1772.36,pop=500,raw='The Comanche nation is very large, as is evident to me from the fact that while more than five hundred visited me, the chief men apologized for not having come in greater numbers ... They are divided into various tribes or bands, named Naitanes, Yarambicas, etc. (place ours) (part)',basis='visitors (a gathering, not the nation)',loc='stated',at=(33.15, -98.7),r=70,src=BOLTON('vol. 1, p. 297 (pdf 304), Doc. 90'),kind='primary',whole=False),
  # Great + Little Osage, as seen from Natchitoches (hearsay). Location given only as 'on the Missuris' – Great Osage were on the Osage R. (Vernon Co., MO) and Little Osage on the Missouri (Saline Co.); one centroid and big 
 dict(g=['osg', 'osl'],y=1772.5,pop=4000,raw="The Osage nation, established on the Missuris River, and divided into two villages, reaches the number of one thousand men. They are not more than seven regular days' journey from Los Ylinuezes (place ours)",basis='warriors × 4 (ours)',loc='stated',at=(38.3, -93.8),r=200,src=BOLTON('vol. 1, p. 304 (pdf 311), Doc. 90'),kind='primary'),
  # Probably the Great Osage village (singular 'village'); hearsay. Houses 'of straw, with a narrow street between them'; best time to attack 'late in August or early in September' when nearby arroyos dry (seasonal note). Co
 dict(g='osg',y=1777.7,pop=3200,raw='The village of the Osages, which, according to men of experience, contains eight hundred men, is situated on an eminence in the midst of a large plain, in which they pasture their horses and raise their crops (place ours)',basis='warriors × 4 (ours)',loc='stated',at=(38.0, -94.3),r=80,src=BOLTON('vol. 2, p. 144 (pdf 150), Doc. 164'),kind='primary'),
  # Taovaya, Wichita proper, Iscani and a Tawakoni group all at the Red River site in Feb 1774; 1000 warriors for the four. Gaignard stayed Feb 16–Aug 14, 1774. Not whole wic: Gaignard also reports a separate Tawakoni ('Toic
 dict(g='wic',y=1774.13,pop=4000,raw='On the sixteenth we arrived at the village of the Panis. They are situated in a prairie on the bank of the Red River, west of the Cados one hundred leagues. The name of the nation is Panis. It contains four villages, namely, the Tavoyache, the Ouatchita, the Niscaniche, and the Toyacane. There are in all one thousand warriors. (place ours) (Taovaya, Wichita proper, Iscani and a Tawakoni village together)',basis='warriors × 4 (ours)',loc='stated',at=(33.947, -97.626),r=15,src=BOLTON('vol. 2, p. 85 (pdf 91), Doc. 136'),kind='primary'),
  # Whole Comanche (generic, 'various groups'), official estimate. Bolton fn 185 compares Gaignard's 4,000 Naytane alone. Same page: 'recently war has been declared between the Comanches, Taguacanas, and Tancagues, and the n
 dict(g=['cyj', 'cyy', 'cyk', 'cyp'],y=1778.01,pop=20000,raw='And the Comanche nation, whose name is applied generically to various groups of Indians . . . 5000 Total . 7280 (a compiled estimate of warriors)',basis='warriors × 4 (ours)',loc='inferred',at=(37.93, -103.44),r=150,src=BOLTON('vol. 2, p. 166 (pdf 172), Doc. 165'),kind='primary'),
  # La Tortuga: eminence with a large spring 15 leagues W of the Kitsai rancheria; Bolton fn 216a suggests Tehuacana, Limestone Co. (coords). Chiefs scattered; not met. Croix's summary (Doc. 188, p. 225) repeats 'three hundr
 dict(g='tkw',y=1778.24,pop=1200,raw='I arrived at the place which the natives call La Tortuga ... The Tancagues live in its neighborhood, not in permanent houses and in a village, but underneath [tents of] skins, and in various bands ... They number about three hundred warriors, including not a few apostates. (place ours)',basis='warriors × 4 (ours)',loc='stated',at=(31.74, -96.55),r=25,src=BOLTON('vol. 2, p. 192 (pdf 198), Doc. 170'),kind='primary'),
  # Tonkawa 150 warriors after the 1777-78 epidemic (vs 300 in Mar 1778). Croix (1780): 'the Tuacanas were reduced to the number of two hundred fifty, and the Tancagües to a hundred less'.
 dict(g='tkw',y=1779.69,pop=600,raw='The Tancagues remain since the last epidemic at the number of one hundred fifty; the Tuacanas, to whom it was very fatal, have one hundred men more; among the Indians of San Theodoro and the Panis-mahas, where it fell with less force, there was not so great a diminution; among the Comanches, none. (place ours)',basis='warriors × 4 (ours)',loc='stated',at=(31.55, -97.05),r=40,src=BOLTON("vol. 2, p. 274 (pdf 280); Croix's summary vol. 2, p. 313 (pdf 319), Doc. 223"),kind='primary'),
  # Tawakoni = 150+100 = 250 men (Croix's 1780 summary reads it so explicitly). Bolton fn 347 notes an alternative reading of 'mas' giving 150. Villages named El Quiscat (first) and El Flechazo (second) in the present list o
 dict(g='wic',y=1779.69,pop=1000,raw='The Tancagues remain since the last epidemic at the number of one hundred fifty; the Tuacanas, to whom it was very fatal, have one hundred men more (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(31.56, -97.13),r=25,src=BOLTON('vol. 2, p. 274 (pdf 280); vol. 2, p. 313 (pdf 319), Doc. 223'),kind='primary',whole=False),
  # South-bank village, 123 houses (= Spanish Fort site). The 800+ 'men, including youths' covers BOTH villages (160 houses). DUP of Swanton p. 303 (1778 wic 3200) and Wikipedia 'Taovaya' (1778.0). FLAG: De M. calls both vil
 dict(g='wic',y=1778.3,pop=3200,raw='The nation of the Taovayazes is divided into two villages, one situated on the northern bank of the Vermejo, or Natchitoches, River, the other opposite the first on the other bank. The former is composed of thirty-seven houses, the latter of one hundred twenty-three. ... more than eight hundred (part)',basis='warriors × 4 (ours)',loc='stated',at=(33.947, -97.626),r=5,src=BOLTON('vol. 2, pp. 201-202 (pdf 207-208), Doc. 175'),kind='primary',whole=False),
  # Taovayases: warriors per San Antonio council table, compiled from 'reports ... in the archives of the secretariat of the commandancy-general' (secondary official estimate, Jan 1778). Table read from page image (OCR garbl
 dict(g='wic',y=1778.01,pop=3200,raw='Council of war at San Antonio, 5 Jan. 1778 (Merino y Moreno, secretary): the Taovaya 500 warriors, the Tawakoni 250, the Iscani 50 (the Panis-mahas’ 600 not counted here) (a compiled official estimate)',basis='warriors × 4 (ours)',loc='inferred',at=(33.95, -97.63),r=150,src=BOLTON('vol. 2, pp. 165-166 (pdf 171-172), Doc. 165'),kind='primary'),
  # Wichita proper ('Ouedsitas') + Taovaya combined: 600 warriors. DUP of Swanton p. 306 (1772 wic 2400, 'about 600 warriors'). This record placed at the WICHITA village, which De M. visited: on the (upper) Brazos, houses 'm
 dict(g='wic',y=1772.36,pop=3120,raw='De Mézières’s 1772 report: the Wichita and Taovaya together 600 warriors; the Tawakoni of the Trinity village 120 (36 houses); the Iscani 60, scattered on farms; with a second Tawakoni village on the Brazos of 30 families (not counted here) (place ours)',basis='warriors × 4 (ours)',loc='stated',at=(33.0, -97.5),r=150,src=BOLTON('vol. 1, pp. 286–94 (pdf 293–301), Doc. 90'),kind='primary'),
 # ---- Henday (1754–55), Cocking (1772–73), La Vérendrye (1733–43), Burpee’s editions
  # 'Our Indians'/'our Traders' = the Cree (with some Assiniboine) trading Indians who took Henday inland; coded crw (Saskatchewan/Fort des Prairies Cree) as a judgment — Burpee gives no tribal name; on 21 May 1755 Henday na
 dict(g='crw',y=1754.574,pop=None,raw='Very shoal water. Here we left our Canoes and travelled 4 miles S.W.b.S. Here were our Indians Families in a starving condition, for want of food; and we are in the same condition. (place ours) (part)',basis='',loc='stated',at=(53.45, -102.95),r=60,src=HENDAY('p. 326 (pdf 26), Henday (Burpee ed. 1907), entry of 27 July 1754'),kind='primary',whole=False),
  # Asinepoet = Assiniboine (Burpee n., p. 327). Place by dead reckoning: 83 miles SW of the Carrot R. landing, between it and Burpee's 9 Aug position (~70 mi E of Clark Crossing).
 dict(g='asn',y=1754.585,pop=None,raw='Came to two tents of Asinepoet Indians. I smoaked with them, and talked with them to go down with me to York Fort in the summer, but they answered, “We are conveniently supplied from the Pagua-Mistagushewuck Whiskeheginish.” That is, the Frenchman’s House of Trade. (place ours) (part)',basis='',loc='stated',at=(52.9, -104.05),r=50,src=HENDAY('p. 327 (pdf 27), Henday (Burpee ed. 1907), entry of 31 July 1754'),kind='primary',whole=False),
  # Dead reckoning between Carrot R. and Burpee's 9 Aug fix (~225 mi from Pasquia post, ~70 mi E of Clark Crossing, p. 328 n.).
 dict(g='asn',y=1754.594,pop=None,raw='Met with 7 tents of Asinepoet Indians. I smoaked with them,—but have no hopes of getting them to the Fort,—as what cloth &c. they had were French, and, by their behaviour, I perceived they were strongly attached to the French interest. (place ours) (part)',basis='',loc='stated',at=(52.6, -104.6),r=50,src=HENDAY('p. 327 (pdf 27), Henday (Burpee ed. 1907), entry of 4 Aug. 1754'),kind='primary',whole=False),
  # Three days (32 mi W/WbN) up the south bank of the North Saskatchewan from Burpee's 24 Aug fix 'at or about the Elbow (107° W.)' (p. 330 n.).
 dict(g='asn',y=1754.657,pop=None,raw='Passed several ponds, & one creek of running water, in which we caught 17 small Trout. In the evening came to 24 tents of Asinepoet Indians. They have plenty of moose & Beaver flesh, with which they treated us liberally. (place ours) (part)',basis='',loc='stated',at=(52.6, -107.85),r=35,src=HENDAY('p. 330 (pdf 30), Henday (Burpee ed. 1907), entry of 27 Aug. 1754'),kind='primary',whole=False),
  # Henday's travelling company (Cree trading Indians and Assiniboine who had joined), not a division total; 'above 400' persons is a stated minimum. 'Our Indians'/'our Traders' = the Cree (with some Assiniboine) trading Ind
 dict(g=['crw', 'asn'],y=1754.669,pop=None,raw='Seven tents of Indians pitched another way. We are yet above 400 in number, two-thirds of whom live chiefly on fruit. (place ours) (part)',basis='',loc='stated',at=(52.85, -108.2),r=40,src=HENDAY('p. 331 (pdf 31), Henday (Burpee ed. 1907), entry of 1 Sept. 1754'),kind='primary',whole=False),
  # Burpee n.: Henday 'has been travelling along the south bank of the North Saskatchewan, and is now somewhere about Battleford' (p. 331). Seasonal: buffalo moving 'upwards' (west/upriver) in early Sept.
 dict(g='asn',y=1754.68,pop=None,raw='We are yet in Muscuty plains. Here are a great many Asinepoet Indians. The Buffalo has taken the route upwards, and is the reason we have not yet met with Archithinue Natives (part)',basis='',loc='stated',at=(52.75, -108.35),r=30,src=HENDAY('p. 331 (pdf 31), Henday (Burpee ed. 1907), entry of 5 Sept. 1754'),kind='primary',whole=False),
  # Eagle (Eagle-eyed) Indians = an Assiniboine band (Henday's own statement; Burpee n. links name to Eagle Hills, S of N. Saskatchewan near Battleford). Graham n.: 'Since 1755 the Eagle-Eyed Indians have traded annually at 
 dict(g='asn',y=1754.683,pop=None,raw='met with five tents of Mekesue, or Eagle Indians. ... I could perceive no difference between them and the Asinepoet Natives with regard to the language ... The Natives inform me that they are a tribe of that brave Nation; and take their name from Eagles being plenty in the district they inhabit. (place ours) (part)',basis='',loc='stated',at=(52.65, -108.55),r=40,src=HENDAY('p. 331 (pdf 31), Henday (Burpee ed. 1907), entry of 6 Sept. 1754'),kind='primary',whole=False),
  # Dead reckoning W/SW from Sounding Creek toward the Red Deer crossing of 11 Oct (Burpee: a little above Knee Hills Creek, 51°32'). Assiniboine using pack-horses, 1754.
 dict(g='asn',y=1754.749,pop=None,raw='No Musketoes to trouble us; Travelled 7 Miles W.S.W. Level lands, & small hommocks of woods. Joined by more Asinepoet Indians, who have 6 pack-horses loaded with provisions, &c. (place ours) (part)',basis='',loc='stated',at=(52.0, -111.2),r=60,src=HENDAY('p. 335 (pdf 35), Henday (Burpee ed. 1907), entry of 30 Sept. 1754'),kind='primary',whole=False),
  # Identification (judgment): 'Archithinue' = Blackfoot confederacy per Burpee (introd., p. 316, using Cocking's list of the five 'Equestrian' tribes); division not determinable, so coded to the three Blackfoot divisions. G
 dict(g=['sik', 'kai', 'pik'],y=1754.753,pop=None,raw='Came to us 7 tents of Archithinue Indians; the men all mounted on Horse-back, with Bows and Arrows, & bone spears & darts. I gave the Leader a foot of tobacco, one fire Steel, a string of beads, a knife; and smoked with them. (place ours) (part)',basis='',loc='stated',at=(51.95, -111.35),r=60,src=HENDAY('p. 335 (pdf 35), Henday (Burpee ed. 1907), entry of 1 Oct. 1754'),kind='primary',whole=False),
  # Assiniboine (possibly Stoney, sto — cf. records.csv R0066) camped with Henday's party at the Archithinue camp; they leave northward for the winter.
 dict(g='asn',y=1754.797,pop=None,raw='322 tents of Archithinue Natives unpitched and moved Westward; 17 tents of Asinepoet Natives moved Northwards; and we moved S.W.b.W. 9 Miles. (place ours) (part)',basis='',loc='stated',at=(51.38, -113.35),r=40,src=HENDAY('p. 340 (pdf 40), Henday (Burpee ed. 1907), entry of 17 Oct. 1754'),kind='primary',whole=False),
  # Burpee n.: 'he was on the 21st day of November, 1754, in about lat. 51° 50’ N., long. 114° W. This was his farthest point west' (p. 342). Henday's winter companions (Cree trading Indians, with Assiniboine; 'Our Indians'/
 dict(g='crw',y=1754.891,pop=None,raw='Clear frosty weather. Travelled 6 Miles S.E. Plains & Ledges of tall Birch trees. Thaws very little to-day. (part)',basis='',loc='stated',at=(51.83, -114.0),r=15,src=HENDAY('p. 342 (pdf 42), Henday (Burpee ed. 1907), entry of 21 Nov. 1754'),kind='primary',whole=False),
  # Mid-winter position (ours) between Knee Hills Creek (crossed 23 Dec; Burpee n. p. 344) and Three Hills Creek (crossed 22 Jan; n. p. 346). Small winter tent groups follow buffalo; 2 Jan 'Three tents of Indians joined us',
 dict(g='crw',y=1755.033,pop=None,raw='Travelled 6 Miles W.b.S. The Buffalo & Waskesew being gone that way: killed one Buffalo & four Beaver: Level land, plenty of Creeks, & Beaver houses. (place ours) (part)',basis='',loc='stated',at=(51.95, -113.55),r=40,src=HENDAY('p. 345 (pdf 45), Henday (Burpee ed. 1907), entry of 12 Jan. 1755'),kind='primary',whole=False),
  # Archithinue Lake = Devil's Pine (Ghostpine) Lake, 'about in long. 113° 30’, lat. 52° 10’' (Burpee n., p. 347). Late-winter gathering of the York Fort trading bands before canoe-building.
 dict(g=['crw', 'asn'],y=1755.157,pop=None,raw='We were joined by different tribes of Natives, who yearly visited our Settlements: they brought with them several Archithinue Women & Children Captives, with many Scalps quite green: We are now at Archithinue lake, about one mile broad, & a good days journey in length (part)',basis='',loc='stated',at=(52.17, -113.5),r=15,src=HENDAY('p. 347 (pdf 47), Henday (Burpee ed. 1907), entry of 27 Feb. 1755'),kind='primary',whole=False),
  # Canoe-building camp on the Red Deer 'above Tail Creek' (Burpee n., p. 347); embarkation 28 Apr 'about the mouth of Tail Creek' (n., p. 349). Spring round: Mar–Apr canoe building on the river, ice breaks 23 Apr, embark 28
 dict(g='crw',y=1755.216,pop=None,raw='Ten tents came & pitched alongside of us in order to build Canoes. (place ours) (part)',basis='',loc='stated',at=(52.22, -113.05),r=20,src=HENDAY('p. 348 (pdf 48), Henday (Burpee ed. 1907), entry of 18 Mar. 1755'),kind='primary',whole=False),
  # Assiniboine canoe camp just below Henday's on the Red Deer near Tail Creek (Burpee). On 9–12 Apr 'Several Asinepoet Indians pitched their tents a small distance below us' and promised to go to York Fort (pp. 348–49).
 dict(g='asn',y=1755.235,pop=None,raw='All hands preparing Wood &c for building Canoes: The Asinepoet Natives are building Canoes below us. (place ours) (part)',basis='',loc='stated',at=(52.2, -113.0),r=25,src=HENDAY('p. 348 (pdf 48), Henday (Burpee ed. 1907), entry of 25 Mar. 1755'),kind='primary',whole=False),
  # Count of canoes, not tents (not convertible without assumptions). Embarkation about the mouth of Tail Creek (Burpee n., p. 349).
 dict(g='asn',y=1755.327,pop=None,raw='Embarked on board my Canoe, & paddled down the river 34 Miles, in company with 20 Canoes of Assinipoet Natives (place ours) (part)',basis='',loc='stated',at=(52.22, -113.05),r=20,src=HENDAY('p. 349 (pdf 49), Henday (Burpee ed. 1907), entry of 28 Apr. 1755'),kind='primary',whole=False),
  # Identification (judgment): 'Archithinue' = Blackfoot confederacy per Burpee (introd., p. 316, using Cocking's list of the five 'Equestrian' tribes); division not determinable, so coded to the three Blackfoot divisions. G
 dict(g=['sik', 'kai', 'pik'],y=1755.366,pop=None,raw='Paddled 10 miles E.b.N. then came to one hundred tents of Archithinue Natives. Their Leader invited me to his tent, and gave me plenty of Buffalo flesh: our Indians bought a great many Wolves from them, for old axes &c. I could not persuade them to go to the Fort. (place ours) (part)',basis='',loc='stated',at=(51.55, -106.9),r=90,src=HENDAY('p. 350 (pdf 50), Henday (Burpee ed. 1907), entry of 12 May 1755'),kind='primary',whole=False),
  # Identification (judgment): 'Archithinue' = Blackfoot confederacy per Burpee (introd., p. 316, using Cocking's list of the five 'Equestrian' tribes); division not determinable, so coded to the three Blackfoot divisions. G
 dict(g=['sik', 'kai', 'pik'],y=1755.374,pop=None,raw='One hundred and twenty seven tents of Archithinue Natives came to us: I bought 30 Wolves’ skins from them, and the Indians purchased great numbers of Wolves, Beaver & Foxes etc. (place ours) (part)',basis='',loc='stated',at=(51.9, -106.75),r=80,src=HENDAY('p. 350 (pdf 50), Henday (Burpee ed. 1907), entry of 15 May 1755'),kind='primary',whole=False),
  # Identification (judgment): 'Archithinue' = Blackfoot confederacy per Burpee (introd., p. 316, using Cocking's list of the five 'Equestrian' tribes); division not determinable, so coded to the three Blackfoot divisions. G
 dict(g=['sik', 'kai', 'pik'],y=1755.377,pop=None,raw='Paddled 30 Miles N.b.E. when we came to 30 tents of Archithinue Natives: I talked with them as I did with the others; but all to no purpose. Our Indians traded a great many Furs from them. They have the finest Horses I have yet seen here (place ours) (part)',basis='',loc='stated',at=(52.2, -106.6),r=70,src=HENDAY('p. 351 (pdf 51), Henday (Burpee ed. 1907), entry of 16 May 1755'),kind='primary',whole=False),
  # Eagle Indians = Assiniboine band (Henday). Same camp as 16 May.
 dict(g='asn',y=1755.38,pop=None,raw='Ten tents of Eagle Indians joined the Archithinue Indians. Five Canoes of them are going to the Fort with me. They are a tribe of the Asinepoet Nation; and like them use the Horses for carrying the baggage and not to ride on. (place ours) (part)',basis='',loc='stated',at=(52.2, -106.6),r=70,src=HENDAY('p. 351 (pdf 51), Henday (Burpee ed. 1907), entry of 17 May 1755'),kind='primary',whole=False),
  # Identification (judgment): 'Archithinue' = Blackfoot confederacy per Burpee (introd., p. 316, using Cocking's list of the five 'Equestrian' tribes); division not determinable, so coded to the three Blackfoot divisions. G
 dict(g=['sik', 'kai', 'pik'],y=1755.391,pop=None,raw='Seventy tents of Archithinue Natives came to us, headed by the Leader that I saw in the Muscuty Country ... They had very few Wolves or Furs of any kind, having traded them before with the Pegogamaw Indians who are gone to the Fort. (place ours) (part)',basis='',loc='stated',at=(52.85, -105.75),r=60,src=HENDAY('p. 351 (pdf 51), Henday (Burpee ed. 1907), entry of 21 May 1755'),kind='primary',whole=False),
  # Henday's downriver brigade the day after leaving Basquea (The Pas): Cree trading Indians and Assiniboine bound for York Fort; on 21 May 'We are above 60 Canoes' (p. 351). Canoes, not tents.
 dict(g=['crw', 'asn'],y=1755.425,pop=None,raw='Paddled none: mustered my Gang total 70 Canoes. (place ours) (part)',basis='',loc='stated',at=(53.85, -101.0),r=40,src=HENDAY('p. 353 (pdf 53), Henday (Burpee ed. 1907), entry of 3 June 1755'),kind='primary',whole=False),
  # Cocking's companions: Cree ('Neheathaway', Burpee n. p. 107) and Assiniboine ('Asinepoet') York Fort traders; Cocking never names the band (records.csv R0103 calls them Pegogamaw, from DCB). Coded crw (judgment).
 dict(g='crw',y=1772.616,pop=None,raw='We did not proceed. I am informed that there are 18 tents of Natives a short distance off (place ours) (part)',basis='',loc='stated',at=(53.2, -104.6),r=25,src=COCKING('p. 102 (pdf 16), Cocking (Burpee ed. 1908), entry of 12 Aug. 1772'),kind='primary',whole=False),
  # South Saskatchewan (Burpee n.), crossed 'somewhere below Clark Crossing' (introd. p. 92); 4 days later Cocking observed lat. 52°37'. Commeseskew had been at York Fort the previous summer (Graham n.) — a trading-Indian le
 dict(g='crw',y=1772.644,pop=None,raw='Travelled 9 miles S.W.b.S., came to a branch of Saskatchewan River, where we put up. ... Here we met with a Leader named Commeseskew, with 14 tents full of natives; They heard of Buffalo up this branch. (place ours) (part)',basis='',loc='stated',at=(52.7, -105.9),r=30,src=COCKING('p. 103 (pdf 17), Cocking (Burpee ed. 1908), entry of 22 Aug. 1772'),kind='primary',whole=False),
  # Cocking's companions: Cree ('Neheathaway', Burpee n. p. 107) and Assiniboine ('Asinepoet') York Fort traders; Cocking never names the band (records.csv R0103 calls them Pegogamaw, from DCB). Coded crw (judgment). Latitud
 dict(g='crw',y=1772.655,pop=None,raw='We did not proceed: Hunters killed several Buffalo. This day I took an Observation per noon Altitude. Latitude 52° 37’ North. (part)',basis='',loc='stated',at=(52.62, -106.1),r=25,src=COCKING('p. 104 (pdf 18), Cocking (Burpee ed. 1908), entry of 26 Aug. 1772'),kind='primary',whole=False),
  # Cocking's companions: Cree ('Neheathaway', Burpee n. p. 107) and Assiniboine ('Asinepoet') York Fort traders; Cocking never names the band (records.csv R0103 calls them Pegogamaw, from DCB). Coded crw (judgment). Eagle H
 dict(g='crw',y=1772.683,pop=None,raw='We proceeded all in Company: Our Course West, distance 13 miles. Leaving the river on one hand, came to some high land named Mikisew Wache, or Eagle hills, where we pitched (part)',basis='',loc='stated',at=(52.4, -108.1),r=25,src=COCKING('p. 105 (pdf 19), Cocking (Burpee ed. 1908), entry of 6 Sept. 1772'),kind='primary',whole=False),
  # Cocking's camp near Eagle Hills creek; 21 Sept he observed lat. 52°13' N (p. 106). These Assiniboine 'were strangers' unacquainted with canoes (19 Sept).
 dict(g='asn',y=1772.716,pop=None,raw='Ten tents of Asinepoet Natives came to us: they say they left several tents of Asinepoet Natives & Archithinue Natives (their friends) two days’ journey beyond Manitow-Sakahegan. (place ours) (part)',basis='',loc='stated',at=(52.25, -108.3),r=30,src=COCKING('p. 106 (pdf 20), Cocking (Burpee ed. 1908), entry of 18 Sept. 1772'),kind='primary',whole=False),
  # Manitow-Sakahegan = Manito Lake (c. 52.73 N, 109.75 W; our identification). 'Two days beyond' = W/SW of it (ours).
 dict(g='asn',y=1772.716,pop=None,raw='they say they left several tents of Asinepoet Natives & Archithinue Natives (their friends) two days’ journey beyond Manitow-Sakahegan. (place ours) (part)',basis='',loc='stated',at=(52.6, -110.3),r=70,src=COCKING('p. 106 (pdf 20), Cocking (Burpee ed. 1908), entry of 18 Sept. 1772'),kind='primary',whole=False),
  # Burpee glosses Archithinue as 'Blackfeet' (n.); coded gv as a judgment because the Archithinue whom Cocking actually met (1 Dec) were the Water-fall Indians (Gros Ventre). Could be any Blackfoot division.
 dict(g='gv',y=1772.716,pop=None,raw='they say they left several tents of Asinepoet Natives & Archithinue Natives (their friends) two days’ journey beyond Manitow-Sakahegan. (place ours) (part)',basis='',loc='stated',at=(52.6, -110.3),r=70,src=COCKING('p. 106 (pdf 20), Cocking (Burpee ed. 1908), entry of 18 Sept. 1772'),kind='primary',whole=False),
  # Autumn dispersal into wintering groups (seasonal round). Neheathaway = Cree (Burpee n.).
 dict(g=['asn', 'crw'],y=1772.732,pop=None,raw='Travelled 3 miles S.E.: the Asinepoet Natives that last arrived going N.W.: Others with Neheathaway Indians going easterly: all to trap Wolves, & pound Buffalo; at present only eight tents. (place ours) (part)',basis='',loc='stated',at=(52.2, -108.25),r=30,src=COCKING('p. 107 (pdf 21), Cocking (Burpee ed. 1908), entry of 24 Sept. 1772'),kind='primary',whole=False),
  # Cocking's companions: Cree ('Neheathaway', Burpee n. p. 107) and Assiniboine ('Asinepoet') York Fort traders; Cocking never names the band (records.csv R0103 calls them Pegogamaw, from DCB). Coded crw (judgment). WINTER 
 dict(g=['crw', 'asn'],y=1772.777,pop=None,raw='We proceeded: Our Course West & distance 2 miles, arriving at the ridge of small poplars where the Natives intend to trap the winter season. Two tents separated from us, going more northerly (place ours) (part)',basis='',loc='stated',at=(51.95, -109.0),r=50,src=COCKING('p. 108 (pdf 22), Cocking (Burpee ed. 1908), entry of 10 Oct. 1772'),kind='primary',whole=False),
  # Spring 1772 use of this pound by 'Archithinue' (coded gv, judgment as above) — evidence that Archithinue pounded buffalo in spring in the plains SW of the Eagle Hills. Date of event = spring 1772; y set to Oct 1772 repor
 dict(g='gv',y=1772.813,pop=None,raw='Every person repairing the Beast pound. ... This pound was made by our Archithinue friends last spring, who had great success, many Skulls & Bones lying in the pound. (place ours) (part)',basis='',loc='stated',at=(51.9, -109.0),r=50,src=COCKING('p. 109 (pdf 23), Cocking (Burpee ed. 1908), entry of 23 Oct. 1772'),kind='primary',whole=False),
  # At the edge of Mikisew-Wachee (Eagle Hills), reached 19 Dec (p. 112).
 dict(g='asn',y=1772.974,pop=None,raw='We were joined by ten tents of Asinepoet Indians. (place ours) (part)',basis='',loc='stated',at=(52.35, -108.3),r=30,src=COCKING('p. 112 (pdf 26), Cocking (Burpee ed. 1908), entry of 21 Dec. 1772'),kind='primary',whole=False),
  # Nehetheway = Cree (Burpee n., p. 107). Edge of Eagle Hills.
 dict(g='crw',y=1772.977,pop=None,raw='Joined by five tents of Nehetheway Indians. There are but few furs amongst us as yet. (place ours) (part)',basis='',loc='stated',at=(52.35, -108.3),r=30,src=COCKING('p. 112 (pdf 26), Cocking (Burpee ed. 1908), entry of 22 Dec. 1772'),kind='primary',whole=False),
  # N of the North Saskatchewan (crossed 19 Jan), on the side of Saketakow-Wachee (31 Jan) — Sacketagow Hills, 'where the Asinepoet natives go yearly for Birch-rind to cover their Canoes' (29 Aug, p. 104). Placement ours.
 dict(g='asn',y=1773.092,pop=None,raw='Two Asinepoet Natives joined us, they left their people 7 tents, this morning: They say Buffalo are very scarce; plenty of Waskesew but no Ammunition (place ours) (part)',basis='',loc='stated',at=(52.95, -107.6),r=60,src=COCKING('p. 114 (pdf 28), Cocking (Burpee ed. 1908), entry of 3 Feb. 1773'),kind='primary',whole=False),
  # Late-winter aggregation of Assiniboine with Cocking's Cree/Assiniboine company. Placement ours.
 dict(g=['asn', 'crw'],y=1773.097,pop=None,raw='We proceeded: Our Course N.N.E. & distance 10 miles, where we joined the Asinepoet Natives; & likewise the Natives who left us Yesterday: At present 20 tents of Indians (place ours) (part)',basis='',loc='stated',at=(53.0, -107.5),r=60,src=COCKING('p. 114 (pdf 28), Cocking (Burpee ed. 1908), entry of 5 Feb. 1773'),kind='primary',whole=False),
  # 'There' = 'towards Waskesew-Wachee, intending to build a Beast-pound there'. Two Assiniboine groups: 11 tents to the pound, 9 tents (part) remaining to build canoes at Saketow-Wachee. Coded as 11 lodges (the departing gr
 dict(g='asn',y=1773.146,pop=None,raw='my Leader with eleven tents of Asinepoet Natives unpitched intending to proceed there: but I with nine tents part; Asinepoet Natives lay still: they intend to build Canoes at Saketow-Wachee. (place ours) (part)',basis='',loc='stated',at=(53.0, -107.4),r=60,src=COCKING('p. 115 (pdf 29), Cocking (Burpee ed. 1908), entry of 23 Feb. 1773'),kind='primary',whole=False),
  # Pound towards Waskesew-Wachee (Red Deer Hill); records.csv R0107 puts it near Red Deer Hill S of Prince Albert (53.1,-105.7); Cocking's distances suggest farther W. Late-winter pound.
 dict(g='asn',y=1773.241,pop=None,raw='We arrived at the Beast pound, where we met with my Leader again, with 4 tents of Neheathaway & 20 tents of Asinepoet Natives; The last are most part of them unacquainted with Canoes (place ours) (part)',basis='',loc='stated',at=(53.05, -106.6),r=80,src=COCKING('p. 116 (pdf 30), Cocking (Burpee ed. 1908), entry of 27 Mar. 1773'),kind='primary',whole=False),
  # Cree: 4 tents at the pound + 30 tents moving to the canoe-building place = 34 tents in the vicinity. Spring movement to canoe sites.
 dict(g='crw',y=1773.241,pop=None,raw='with 4 tents of Neheathaway & 20 tents of Asinepoet Natives; ... the others, 30 tents of Neheathaway Natives, had unpitched, intending to proceed slowly towards the place of building Canoes, hunting as they go. (place ours) (part)',basis='',loc='stated',at=(53.05, -106.6),r=80,src=COCKING('p. 116 (pdf 30), Cocking (Burpee ed. 1908), entry of 27 Mar. 1773'),kind='primary',whole=False),
  # Spring canoe-building camp (9 Apr–15 May) on a branch of the Saskatchewan 3–4 days' slow paddle above the Forks (reached 19 May). River broke up 20 Apr; embarked 16 May (p. 117). Placement ours.
 dict(g=['crw', 'asn'],y=1773.277,pop=None,raw='All hands employed collecting materials & building Canoes. No Snow on the ground, but what is in the Woods. Indian Visitors coming & going; whose people generally employed as we are, preparing Canoes. (place ours) (part)',basis='',loc='stated',at=(53.0, -106.7),r=70,src=COCKING('p. 117 (pdf 31), Cocking (Burpee ed. 1908), entry of 10 Apr. 1773'),kind='primary',whole=False),
  # Delegation encamped half a day from Fort St. Charles (NW Angle, Lake of the Woods). Assiniboine part = 90 persons (60 men + 30 wives); 10 Cree additional. Assiniboine of the 1730s (Lake Winnipeg–Red/Assiniboine River cou
 dict(g=['asn', 'ass'],y=1733.996,pop=None,raw='After six hours they found them encamped to the number of 60 Assiniboin, 30 of their wives, and 10 Cree, awaiting my reply. (place ours) (part)',basis='',loc='stated',at=(49.3, -95.1),r=15,src=VEREND('p. 144 (pdf 178), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (undated)'),kind='primary',whole=False),
  # Seen by La Vérendrye's son (at Fort Maurepas, lower Red River, 1734–35). Partial count (explicitly 'a great many more'). Same letter: the Assiniboine 'were going to start with their families and go to the Ouachipouennes 
 dict(g=['asn', 'ass'],y=1735.457,pop=None,raw='My cousin La Vérendrye has written to me to say that he had seen three hundred cabins of Assiniboin and that he would have seen a great many more if he had had a supply of goods. (place ours) (part)',basis='',loc='stated',at=(50.2, -97.2),r=150,src=VEREND('p. 199 (pdf 235), La Vérendrye (Burpee ed. 1927): La Jemeraye to Beauharnois, 23 July 1735'),kind='primary',whole=False),
  # Pointe du Bois fort, 'the usual rendezvous for Assiniboin, Cree and Monsoni', on the Red River some distance above the Assiniboine (Burpee n., p. 222). Mixed war assembly.
 dict(g=['cre', 'asn', 'ass'],y=1736.797,pop=None,raw='Eight hundred Cree and Assiniboin already assembled at Pointe du Bois fort are awaiting us. (part)',basis='',loc='stated',at=(49.6, -97.2),r=40,src=VEREND('p. 228 (pdf 264), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (headed 2 June 1736; journal to 173'),kind='primary',whole=False),
  # Winter buffalo hunt of Assiniboine and Cree near Fort Maurepas/Red River (seasonal). Assiniboine of the 1730s (Lake Winnipeg–Red/Assiniboine River country) were ancestral to both later divisions; coded [asn, ass] (judgme
 dict(g=['asn', 'ass'],y=1737.044,pop=None,raw='On the sixteenth La Colle’s man who passed by the Assiniboin said that the two tribes are at present hunting buffalo to get meat and fats for the fort ; some of them return laden every day. (place ours) (part)',basis='',loc='stated',at=(50.0, -97.2),r=80,src=VEREND('p. 240 (pdf 276), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (headed 2 June 1736; journal to 173'),kind='primary',whole=False),
  # Escort party (men) near Fort Maurepas; Assiniboine 70, Cree 50 (separate Cree record not made). 'the chiefs were sending their entire families to fort Maurepas'. Assiniboine of the 1730s (Lake Winnipeg–Red/Assiniboine Ri
 dict(g=['asn', 'ass'],y=1737.089,pop=None,raw='there were seventy of their people and fifty Cree a day’s journey away laden with meat and fats to escort me. (place ours) (part)',basis='',loc='stated',at=(50.2, -96.9),r=40,src=VEREND('p. 241 (pdf 277), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (headed 2 June 1736; journal to 173'),kind='primary',whole=False),
  # Forks of the Red and Assiniboine (Winnipeg). On 4 Mar an Assiniboine chief called the fork 'their own proper territory' (p. 250). Winter villages. Assiniboine of the 1730s (Lake Winnipeg–Red/Assiniboine River country) we
 dict(g=['asn', 'ass'],y=1737.138,pop=None,raw='time was required to notify two villages of the Assiniboin situated at the great fork of the Red river (part)',basis='',loc='stated',at=(49.89, -97.13),r=10,src=VEREND('p. 244 (pdf 280), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (headed 2 June 1736; journal to 173'),kind='primary',whole=False),
  # SEASONAL: Assiniboine summer = war, then trading trip to the Mandan (Koüathéattes = Mandan, Burpee n. p. 215). Point placed at the Mandan villages (ours) for the summer visit; dated to the statement (Mar 1737), refers to
 dict(g=['asn', 'ass'],y=1737.18,pop=None,raw='I enquired of the Assiniboin where they meant to spend the summer ; and they said that on returning from the war they would go to the country of the Koüathéattes to buy Indian corn and beans (place ours) (part)',basis='',loc='stated',at=(46.85, -100.75),r=60,src=VEREND('p. 253 (pdf 289), La Vérendrye (Burpee ed. 1927): Report of La Vérendrye (headed 2 June 1736; journal to 173'),kind='primary',whole=False),
  # War party (warriors). Place unknown — Lake of the Woods/Red River region (ours). See notes: smallpox 1737.
 dict(g=['asn', 'ass'],y=1737.327,pop=None,raw='the Assiniboin to the number of eight hundred had left at the end of April to go and take vengeance on the Sioux for the Frenchmen [they had killed], and that the Cree and the Monsoni had also raised war parties ... but that small-pox having broken out among them they were obliged to stop (place ours) (part)',basis='',loc='stated',at=(49.5, -96.8),r=200,src=VEREND('p. 282 (pdf 318), La Vérendrye (Burpee ed. 1927): Beauharnois to Maurepas, 1 Oct. 1738'),kind='primary',whole=False),
  # Cree at the Forks (Winnipeg); they went yearly to York Factory (p. 299). Lower Red River Cree — coded cre (Qu'Appelle–Touchwood ancestors?) as a judgment; could be off-track.
 dict(g='cre',y=1738.732,pop=None,raw='I proceeded to the fork of the Assiniboine and, reaching there on the 24th, I found ten cabins of Cree, including two war chiefs, awaiting me with a large quantity of meat (part)',basis='',loc='stated',at=(49.89, -97.13),r=5,src=VEREND('p. 298 (pdf 336), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # Three days SSW of Fort La Reine toward the 'first mountain' (Pembina Mtn, 26 leagues S1/4W; Upham in Burpee n.). Coded ass (Assiniboine S of the Assiniboine R., trading to the Missouri; judgment). Dog transport only (no 
 dict(g='ass',y=1738.805,pop=None,raw='On the third day after our departure an Assiniboin village of forty lodges joined us with the object of speaking to me. (place ours) (part)',basis='',loc='stated',at=(49.6, -98.5),r=40,src=VEREND('p. 311 (pdf 349), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # Assiniboine (the village guides him to the Mandan). Place: between Turtle Mountain and the Missouri, diverted from the trail (Upham in Burpee n., p. 312); very uncertain. Repeated in Report of 31 Oct. 1744, p. 446: 'a vi
 dict(g='ass',y=1738.883,pop=None,raw='To crown our luck he took us twenty-two leagues out of our way to visit a village of a hundred and two lodges that he had gone to discover (place ours) (part)',basis='',loc='stated',at=(48.9, -100.6),r=100,src=VEREND('p. 313 (pdf 351), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # The men of the 102-lodge village (plus French) marching to the Mandan, families left behind; '600 men' includes ~20 French. Place: 3 days N of the first Mandan fort (ours).
 dict(g='ass',y=1738.916,pop=None,raw='We left on the morning of the 30th, about 600 men and several women without children, some of the best walkers. (place ours) (part)',basis='',loc='stated',at=(47.4, -100.9),r=60,src=VEREND('p. 324 (pdf 362), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # One Mandan fort, the chief's (smaller than the others and 'a little far from the river', p. 320). Location disputed: Burpee/Upham put the 1738 villages near the Heart River (Bismarck–Mandan); La Vérendrye's latitude 48°1
 dict(g='man',y=1738.933,pop=None,raw='I gave orders to count the cabins, and we found that there were about one hundred and thirty. (place ours) (part)',basis='',loc='stated',at=(46.85, -100.75),r=40,src=VEREND('p. 339 (pdf 377), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # SEASONAL: Mandan summer field villages (40–50 cabins each) vs. main fortified villages occupied in winter. Lodge counts here are of empty summer villages — do not add to population.
 dict(g='man',y=1738.936,pop=None,raw='We remarked that in the plain there are several small forts of from forty to fifty cabins each, constructed in the same manner as the large ones. At present they are uninhabited. We were given to understand that they went there in summer in order to work in the fields (place ours) (part)',basis='',loc='stated',at=(46.85, -100.75),r=40,src=VEREND('p. 346 (pdf 384), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # SEASONAL: spring canoe-building by Assiniboine at Lake Manitoba/Winnipegosis ('Lake of the Prairies', Burpee n. p. 304) for the summer trip to York Factory. Place = S end of Lake Manitoba (ours).
 dict(g=['asn', 'ass'],y=1739.31,pop=None,raw='On the 22nd of the present month I learnt from a savage that a large band of Assiniboin had gathered at the Lake of the Prairies, and are making canoes in order to go to the English. (place ours) (part)',basis='',loc='stated',at=(50.4, -98.5),r=60,src=VEREND('p. 358 (pdf 396), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # Band trading at Fort La Reine (Portage la Prairie) in May; another 30 lodges announced on 20 May (p. 359).
 dict(g=['asn', 'ass'],y=1739.361,pop=None,raw='On the same day, the 10th, in the evening fifteen Assiniboin came to tell us that they belonged to a band of sixty lodges ... They came on the 18th and did their trading in a short time. (part)',basis='',loc='stated',at=(49.97, -98.3),r=40,src=VEREND('p. 359 (pdf 397), La Vérendrye (Burpee ed. 1927): Journal of La Vérendrye, 20 July 1738–May 1739'),kind='primary',whole=False),
  # Fort Dauphin, autumn 1741, near Winnipegosis (Burpee n., p. 379). The 1749 memorandum says it was made 'at the request of the Cree of the Prairies and the Canoe Assiniboin' (p. 485). Mountain/Prairie Cree W of Lake Winni
 dict(g='cre',y=1741.79,pop=None,raw='I established a new fort at the request of the mountain Cree on the Lake of the Prairies last autumn, and named it fort Dauphin. (part)',basis='',loc='stated',at=(51.65, -99.95),r=25,src=VEREND('p. 378 (pdf 416), La Vérendrye (Burpee ed. 1927): La Vérendrye to Maurepas, 12 May 1742'),kind='primary',whole=False),
  # Canoe Assiniboine (Northern Assiniboine using canoes) around Lake Winnipegosis/Dauphin (judgment asn).
 dict(g='asn',y=1741.79,pop=None,raw='fort Dauphin, the fifth establishment, made at the request of the Cree of the Prairies and the Canoe Assiniboin. (part)',basis='',loc='stated',at=(51.65, -99.95),r=40,src=VEREND('p. 485 (pdf 525), La Vérendrye (Burpee ed. 1927): Mémorandum respecting the map [1749]'),kind='primary',whole=False),
  # SEASONAL (high priority): Forks of the Saskatchewan = annual SPRING rendezvous of the Cree. The Chevalier's ascent was in spring (he was sent 10 Apr 1739 toward the Poskoyac, Report 1744 p. 447); y set to spring 1739 (ju
 dict(g=['crw', 'cre'],y=1739.318,pop=None,raw='ascended it as far as the fork, which is the rendezvous every spring of the Cree of the Mountains, Prairies, and Rivers to deliberate as to what they shall do— go and trade with the French or with the English. (part)',basis='',loc='stated',at=(53.25, -105.08),r=10,src=VEREND('p. 487 (pdf 527), La Vérendrye (Burpee ed. 1927): Mémorandum respecting the map [1749]'),kind='primary',whole=False),
  # Gens du Serpent = Shoshoni per Parkman/Neill (Burpee n. p. 412); Doane Robinson argued Kiowa. Coded sho as instructed, flagged. 12 days' march from the Gens de l'Arc camp to the mountains; place very uncertain (Bighorns?
 dict(g='sho',y=1743.055,pop=None,raw='Being near the main village of the Gens du Serpent our scouts came to inform us that they had all made their escape with great precipitation, and that they had abandoned their lodges and a large part of their effects. (place ours) (part)',basis='',loc='stated',at=(44.5, -106.8),r=300,src=VEREND('p. 420 (pdf 458), La Vérendrye (Burpee ed. 1927): Journal of the Chevalier de la Vérendrye, 1742–43'),kind='primary',whole=False),
  # Petite Cerise = Arikara band (Robinson, Burpee n. p. 424). SEASONAL: winter quarters away from (W of) the Missouri village, return by mid-March. Place = two days W/WNW of Fort Pierre (ours).
 dict(g='ari',y=1743.208,pop=None,raw='On the 15th of March we arrived among the Gens de la Petite Cerise. They were returning from their winter quarters, and were two days’ march from their fort, which is on the bank of the Missouri. (place ours) (part)',basis='',loc='stated',at=(44.45, -100.9),r=50,src=VEREND('p. 425 (pdf 463), La Vérendrye (Burpee ed. 1927): Journal of the Chevalier de la Vérendrye, 1742–43'),kind='primary',whole=False),
  # Fort La Butte = Assiniboine rendezvous, 'probably the Maison du Chien, or Dog Den butte' on the Coteau du Missouri (Burpee n.). 'over a hundred' persons (men?) returning N from the Mandan in late May.
 dict(g='ass',y=1743.407,pop=None,raw='We passed by fort La Butte on the morning of the 27th, but the Assiniboin had just left. ... We hastened our march somewhat and caught up with the Assiniboin at their encampment. There were over a hundred of them and we continued our route together. (place ours) (part)',basis='',loc='stated',at=(47.9, -100.6),r=50,src=VEREND('p. 430 (pdf 468), La Vérendrye (Burpee ed. 1927): Journal of the Chevalier de la Vérendrye, 1742–43'),kind='primary',whole=False),
  # Tribe not named; judged Assiniboine (the 1738 route's 'first/second mountain' = Pembina Mtn/Turtle Mtn, Upham in Burpee n. p. 311). Low confidence.
 dict(g='ass',y=1743.422,pop=None,raw='We reached the village near the mountain on the 2nd of June. As our horses were tired we suspended our journey and remained in the village till the 20th. (place ours) (part)',basis='',loc='stated',at=(49.0, -99.3),r=120,src=VEREND('p. 431 (pdf 469), La Vérendrye (Burpee ed. 1927): Journal of the Chevalier de la Vérendrye, 1742–43'),kind='primary',whole=False),
 # ---- Ewers (BAE 159), Denig (BAE 46), Jenness (1938)
  # Winter range of the three Blackfoot tribes (US side) 1853, Stevens quoted by Ewers. Centre ours, between the Teton, middle Marias and Milk rivers. Count 6-7,000 is for those wintering there (mostly Piegan and Blood), not
 dict(g=['sik', 'kai', 'pik'],y=1853.85,pop=None,raw='In 1853 Governor Stevens mentioned these posts and added, "the winter homes of the Blackfeet, some six to seven thousand strong are on the Teton, the Marias, and Milk Rivers (Stevens, 1860, vol. 12, p. 239).',basis='',loc='stated',at=(48.35, -110.9),r=130,src=EWERS2('p. 125 (pdf 149)'),kind='primary'),
  # One Piegan band's winters c.1849-61; modal winter ground the Marias valley. Centre ours on the middle Marias (Shelby crossing to below Willow Rounds).
 dict(g='pik',y=1855.9,pop=None,raw='The winter count of Elk Horn, a Piegan ... lists the winter camps of his band for 12 successive years beginning ca. 1849. During that period these camps ranged from the Sweetgrass Hills ... to "south of the Missouri," yet more than half of the winters were spent on the Marias. (part)',basis='',loc='stated',at=(48.4, -111.7),r=60,src=EWERS2('p. 125 (pdf 149)'),kind='primary',whole=False),
  # THE sourced Piegan winter ground 1848-80 (informants + Schultz). Junction of Cut Bank Cr. and Two Medicine R. c. 48.45N 112.25W; p.41 adds 'from the present Shelby-Great Falls Railway crossing eastward'. Centre ours mid-
 dict(g='pik',y=1864.9,pop=None,raw='The valley of the Marias was a favorite winter camp ground for Piegan bands from ca. 1848 to 1880. ... the several bands were spread out, at distances of several miles apart, from near the junction of Cut Bank and Two Medicine Creeks forming the Marias to the big bend of the Marias.',basis='',loc='stated',at=(48.38, -111.75),r=45,src=EWERS2('p. 125 (pdf 149)'),kind='primary'),
  # Specific winter campsite (plate 7); one or more bands. Coordinates ours from junction + 5 mi downstream; Baker & Bro. winter post there 1868-69.
 dict(g='pik',y=1862.9,pop=None,raw='The vicinity known to the Indians as Willow Rounds, located some 5 miles down the Marias from the junction of Cut Bank and Two Medicine Creeks ... This area was occupied by Piegan winter camps during the third quarter of the 19th century. (part)',basis='',loc='stated',at=(48.42, -112.13),r=10,src=EWERS2('p. 125 (pdf 149)–126 (pdf 149–150)'),kind='primary',whole=False),
  # Head chief's band camp, early winter; exact reach not given.
 dict(g='pik',y=1858.79,pop=None,raw='The trader W. T. Hamilton found the camp of the Piegan head chief, Little Dog, on the Marias in October 1858 (Hamilton, 1900, p. 58) (part)',basis='',loc='stated',at=(48.35, -111.6),r=60,src=EWERS2('p. 125 (pdf 149)'),kind='primary',whole=False),
  # Late-1870s Blood and N. Blackfoot bands wintering on the Marias near Fort Conrad (position ours, near the GN bridge west of Shelby/Conrad). Only 'some' bands; buffalo-collapse period.
 dict(g=['kai', 'sik'],y=1878.9,pop=None,raw='In the late seventies James Kipp and James Willard Schultz operated Fort Conrad near the present Great Northern Railway bridge over the Marias. At that time some Blood and even North Blackfoot bands, as well as the Piegan, wintered on that river (Schultz, 1907, pp. 60, 105). (part)',basis='',loc='stated',at=(48.3, -111.9),r=25,src=EWERS2('p. 125 (pdf 149)'),kind='primary',whole=False),
  # c.1833 Piegan winter ground: lower Sun and Teton rivers (centre ours between them, west of Great Falls/Fort Benton). Occasional winters at Three Forks (45.93N 111.5W) not modelled. Ewers adds no Three Forks winters after
 dict(g='pik',y=1833.9,pop=None,raw='Bradley, on the basis of information furnished by Alexander Culbertson, stated that in earlier times (ca. 1833) the Piegan wintered on Sun and Teton Rivers and sometimes as far south as the Three Forks of the Missouri.',basis='',loc='stated',at=(47.6, -111.9),r=60,src=EWERS2('p. 126 (pdf 150)'),kind='primary'),
  # c.1833 Blood winter ground: 'the Marias OR Belly River' - two alternatives c.200 km apart (Marias c.48.4N 111.5W; lower Belly c.49.6N 112.8W). Centre ours between them, large r. Could be split into two records.
 dict(g='kai',y=1833.9,pop=None,raw='At that time the Blood Indians wintered on the Marias or on Belly River, and the North Blackfoot on Belly and Bow Rivers (Bradley, MSS., Mont. Hist. Soc, book A, p. 179). (place ours)',basis='',loc='stated',at=(49.0, -112.3),r=110,src=EWERS2('p. 126 (pdf 150)'),kind='primary'),
  # c.1833 North Blackfoot (Siksika) winter ground on the Belly and Bow rivers; centre ours between lower Belly and middle Bow (Blackfoot Crossing 50.77N 112.9W is on the Bow).
 dict(g='sik',y=1833.9,pop=None,raw='At that time the Blood Indians wintered on the Marias or on Belly River, and the North Blackfoot on Belly and Bow Rivers (Bradley, MSS., Mont. Hist. Soc, book A, p. 179). (place ours)',basis='',loc='stated',at=(50.2, -112.6),r=90,src=EWERS2('p. 126 (pdf 150)'),kind='primary'),
  # THE sourced Piegan summer (tribal camp / Sun Dance) ground, late buffalo days (c.1860s-1880). Tribal camp assembled from early June, Sun Dance in August, dispersal ~1 Sept. Sweetgrass Hills c.48.9N 111.5W: only ~60-100 k
 dict(g='pik',y=1870.6,pop=None,raw='The neighborhood of the Sweetgrass Hills was a favorite site for the Piegan Sun Dance in late buffalo days, but it was often held at other locations within their range. ... The Sun Dance was timed to coincide with the ripening of the sarvisberries ... This was in the month of August.',basis='',loc='stated',at=(48.92, -111.5),r=40,src=EWERS2('p. 128 (pdf 152)'),kind='primary'),
  # Mid-19th-c. range limits (map fig. 24, 'in 1850'): Rockies W, Bearpaw Mts E (~109.5W), Musselshell S (~46.6N), Red Deer N (~51.5N). Centre ours. Useful as a hard bound on any seasonal offset.
 dict(g=['sik', 'kai', 'pik'],y=1850.5,pop=None,raw='It was rare for any Piegan, Blood, or North Blackfoot band to hunt east of the Bearpaw Mountains, south of the Musselshell River, or north of the Red Deer River. I have indicated the common hunting territory of the Blackfoot tribes on the map (fig. 24) (place ours)',basis='',loc='stated',at=(49.3, -111.8),r=260,src=EWERS2('p. 123 (pdf 147)'),kind='primary'),
  # A Piegan band (ancestors of the North Piegan per Sanderville) living year-round in the foothills, 1811. Placement ours along the foothills. Not a whole-division count.
 dict(g='pik',y=1811.5,pop=None,raw='Alexander Henry ... in describing the Piegan in 1811, observed: There are 30 or 40 tents who seldom resort to the plains, either in summer or winter ... This small band generally inhabit the thick, woody country along the foot of the mountains (place ours) (part)',basis='',loc='stated',at=(49.8, -114.2),r=120,src=EWERS2('p. 244 (pdf 268)'),kind='primary',whole=False),
  # Pre-horse Piegan location, early 18th c. (Saukamappee via Thompson). Eagle Hills SW of Battleford. Ewers ASSUMES (his word) Blood and N. Blackfoot lay 'at no great distance from them to the northward or eastward' - not a
 dict(g='pik',y=1720.5,pop=None,raw="David Thompson, in 1787, found that the testimony of elderly Piegan ... clearly pointed to that tribe's residence on the Saskatchewan Plains, near the Eagle Hills, some 400 miles east of the Rockies, in the early 18th century.",basis='',loc='stated',at=(52.4, -108.6),r=120,src=EWERS2('p. 300 (pdf 324)'),kind='secondary'),
  # A poor Blood band on the Bow in fall 1855 (did not reach the Judith council). Reach of Bow not stated; centre ours near Blackfoot Crossing.
 dict(g='kai',y=1855.75,pop=None,raw='In the fall of 1855, James Doty (MS., p. 23) met a Blood chief, "The Man who sits by the Eagle\'s Tail," on Bow River. He was chief of a small band of 18 lodges which was at that time so poor "they had only dogs to move with (part)',basis='',loc='stated',at=(50.8, -112.9),r=100,src=EWERS2('p. 248 (pdf 272)'),kind='primary',whole=False),
  # Table 2. A camp near Fort Union seen by Boller c.1858-60 (Ewers dates 1860).
 dict(g='ass',y=1860.5,pop=None,raw='Assiniboin ... 1860 ... [Lodges] 150 ... Assiniboin camp near Fort Union-"few horses, depending almost entirely on dogs." Boller, 1868, p. 39. (part)',basis='',loc='stated',at=(48.0, -104.04),r=40,src=EWERS2('p. 24 (pdf 48)'),kind='primary',whole=False),
  # Table 2. Garrard's visit, autumn 1846; a single camp.
 dict(g='chs',y=1846.85,pop=None,raw='Cheyenne ... 1846 ... [Lodges] 18 ... Ca. 200 [horses] ... Cheyenne camp visited near Fort Bent ... Garrard, 1927, pp. 52, 55. (part)',basis='',loc='stated',at=(38.04, -103.43),r=30,src=EWERS2('p. 24 (pdf 48)'),kind='primary',whole=False),
  # Table 2. Quanah's party surrendering at Fort Sill.
 dict(g='cyq',y=1875.42,pop=None,raw='Comanche ... 1875 ... [Persons] 175 [Horses] 700 ... Kwahari Comanche surrendered at Fort Sill, June 2. Nye, 1943, p. 235. (part)',basis='',loc='stated',at=(34.65, -98.4),r=5,src=EWERS2('p. 24 (pdf 48)'),kind='primary',whole=False),
  # Table 2.
 dict(g='kio',y=1875.15,pop=None,raw='Kiowa ... 1875 ... [Persons] 253 [Horses] 475 ... Kiowa party surrendered at Fort Sill, Feb. 26. Nye, 1943, p. 231. (part)',basis='',loc='stated',at=(34.65, -98.4),r=5,src=EWERS2('p. 25 (pdf 49)'),kind='primary',whole=False),
  # Table 2. Sitting Bull's refugees in Canada (mostly Hunkpapa); placed near Wood Mountain by us (not on Ewers's page).
 dict(g=['hnk', 'min', 'sna', 'sih', 'ogl'],y=1878.5,pop=None,raw="Teton Dakota ... 1878 ... [Persons] 2,900 [Horses] 3,500 ... Canadian Government report on Sitting Bull's camp. Denny, 1939, p. 120. (place ours) (part)",basis='',loc='stated',at=(49.4, -106.4),r=80,src=EWERS2('p. 26 (pdf 50)'),kind='primary',whole=False),
  # Gens des Roches band near the mouth of White Earth River (ND) in spring 1805 (L&C passed it c.21 Apr 1805). Coordinates ours.
 dict(g='ass',y=1805.3,pop=None,raw='He stated that when Lewis and Clark came up the Missouri in 1805 his band of about 60 lodges (called Les Gens des Roches) had after a severe war made peace with the Sioux ... and that he saw the expedition referred to near White Earth River (part)',basis='',loc='stated',at=(48.1, -102.8),r=40,src=DENIG46('p. 395 (pdf 13)'),kind='primary',whole=False),
  # Bands camped at Fort Union in summer 1838; 250 -> c.30 lodges (88% loss).
 dict(g='ass',y=1838.6,pop=None,raw='250 lodges contracted the disease at one time, who in the course of the summer and fall were reduced to 65 men, young and old, or about 30 lodges in all. (part)',basis='',loc='stated',at=(48.0, -104.04),r=15,src=DENIG46('p. 399 (pdf 14)'),kind='primary',whole=False),
  # Gens du Nord (Gens du Lac) move from asn to ass in 1839 (p.430). Transfer between divisions.
 dict(g='ass',y=1839.5,pop=None,raw='though in 1839, 60 lodges of Assiniboin came over from the British northern possessions and joined those of the Missouri, since which time they have resided together. (place ours) (part)',basis='',loc='stated',at=(48.6, -105.0),r=200,src=DENIG46('p. 403 (pdf 16)'),kind='primary',whole=False),
  # A Crow village at the Yellowstone mouth (Fort Union) in spring 1853 - fits the post-1850 pattern of Crow wintering with the Assiniboine. Division identification ours.
 dict(g='cwr',y=1853.3,pop=None,raw='Five Blackfeet were caught stealing horses from the Crow village in the spring of 1853, then at the mouth of the Yellowstone River (part)',basis='',loc='stated',at=(47.98, -104.0),r=10,src=DENIG46('p. 491 (pdf 63)'),kind='primary',whole=False),
  # Gens des Canots in three camps within 15 miles, c.1849 (council on Crow peace; 'a few years since'). Place not stated (Crow deputation 'at the Fort' = Fort Union); placement ours.
 dict(g='ass',y=1849.5,pop=None,raw='The camp when I was a visitor consisted of about 110 lodges and in the neighborhood, say, 10 or 15 miles off were two other camps, respectively 50 and 60 lodges, all being of the band Gens des Canots. (place ours) (part)',basis='',loc='stated',at=(48.3, -104.0),r=120,src=DENIG46('p. 436 (pdf 36)'),kind='primary',whole=False),
  # Part of Gens des Canots on the lower Yellowstone c.1847; date from council c.1849 minus 2. Reach of Yellowstone not stated.
 dict(g='ass',y=1847.5,pop=None,raw='the Crow Indians had massacred about 30 lodges of this same band two years previous on the banks of the Yellowstone (part)',basis='',loc='stated',at=(47.5, -105.2),r=120,src=DENIG46('p. 438 (pdf 37)'),kind='primary',whole=False),
  # Henry (Fort Augustus/Edmonton House). 1810-11: 'near the mountains' (placement ours, foothills W of Red Deer-Rocky Mtn House); usual station 'environs of the Beaver Hills' (c.53.3N 112.9W) - an alternative usual-year rec
 dict(g='sar',y=1810.9,pop=None,raw='The Sarcees, who all traded at this post in the winter of 1810-11 ... A quarrel which they had last summer with the Assiniboines has caused them to remain near the mountains for the present; the environs of the Beaver Hills are generally their station.',basis='',loc='stated',at=(52.6, -114.7),r=100,src=JENNESS('p. 2 (pdf 12)'),kind='primary'),
  # Usual (normal-year) Sarsi station c.1810, Henry. Season unspecified.
 dict(g='sar',y=1810.5,pop=None,raw='the environs of the Beaver Hills are generally their station.',basis='',loc='stated',at=(53.3, -112.9),r=50,src=JENNESS('p. 2 (pdf 12)'),kind='primary'),
  # Whole tribe moving camp near (old) Fort Vermilion on the N. Saskatchewan, c.1862 (informant's date); then a disastrous battle with Cree and allies: 'the Sarcee lost at least twenty families ... Never again did they recov
 dict(g='sar',y=1862.5,pop=None,raw='"About 1862, when the Sarcee were travelling near Fort Vermilion, a dense fog arrested their progress and caused them to pitch their tents under a hill not far from a lake.',basis='',loc='stated',at=(53.85, -110.9),r=60,src=JENNESS('p. 4 (pdf 14)–6 (pdf 14–16)'),kind='primary'),
  # Many Wounds' account: 1870, late summer, camped with the Blackfoot just N of the Red Deer R. (reach not given; placement ours on middle Red Deer). Fled south. Conflicts with records dating the Sarsi epidemic to winter 18
 dict(g='sar',y=1870.65,pop=None,raw='In the late summer of this year, when the berries had begun to ripen and we had encamped near the Blackfoot just north of the Red Deer River, smallpox broke out among us ... We broke up camp and moved south ... it had wiped out nearly 200 families.',basis='',loc='stated',at=(51.9, -113.2),r=80,src=JENNESS('p. 7 (pdf 17)–8 (pdf 17–18)'),kind='primary'),
  # Table 2. Compare R0441 (Swanton: 3,250-3,560 in 1833). 4,500 at 400 lodges = 11.25/lodge, high; Ewers combines Maximilian's lodges with a Hodge figure. Whole Crow nation.
 dict(g=['cwm', 'cwr'],y=1833.5,pop=4500,raw='Crow ... 1833 ... [Lodges] 400 [Persons] 4,500 [Horses] 9,000+ ... "... said to possess more horses than any other tribe on the Missouri." Maximilian, 1906, vol. 22, pp. 351-352; Hodge, pt. 1, p. 368.',basis='souls (as tabulated; Maximilian/Hodge)',loc='inferred',at=(45.42, -108.01),r=150,src=EWERS2('p. 25 (pdf 49)'),kind='secondary'),
  # Ewers Table 2 (secondary compilation). Catlin's figure for the Hidatsa, 1832-33.
 dict(g='hid',y=1833.5,pop=1500,raw='Hidatsa ... 1833 ... [Persons] 1,500 [Horses] 300- ... Horse population: Maximilian, 1906, vol. 23 p. 370. Human population: Catlin, 1841, vol. 1. p. 185.',basis='souls (Catlin)',loc='inferred',at=(47.3, -101.35),r=150,src=EWERS2('p. 25 (pdf 49)'),kind='secondary'),
  # Ewers Table 2 (secondary compilation). 
 dict(g=['osg', 'osl'],y=1850.5,pop=4561,raw='Osage ... 1850 ... [Persons] 4,561 [Horses] 10,000 ... Great and Little Osage ... U. S. Comm. Ind. Affairs, 1850, pp. 35, 37.',basis='agency count (ARCIA 1850)',loc='inferred',at=(37.4, -95.3),r=150,src=EWERS2('p. 26 (pdf 50)'),kind='secondary'),
  # Spring rendezvous (Dakota Rendezvous) on the James R., c.1803-04 (Tabeau). Site placement ours on the James in NE South Dakota; which Teton divisions not stated. Seasonal evidence: Yankton/Yanktonai spring gathering on t
 dict(g='ynk',y=1803.4,pop=None,raw='Each spring the Teton met their Dakota relatives, the Yankton, Yanktonai, and Eastern Dakota at a great trading fair on the James River in present South Dakota ... Tabeau (1939, pp. 121, 131) reported that this Sioux trading fair sometimes attracted as many as 1,000 to 1,200 tents (part)',basis='',loc='stated',at=(45.1, -98.4),r=80,src=EWERS2('p. 10 (pdf 34)'),kind='primary',whole=False),
  # Spring rendezvous (Dakota Rendezvous) on the James R., c.1803-04 (Tabeau). Site placement ours on the James in NE South Dakota; which Teton divisions not stated. Seasonal evidence: Yankton/Yanktonai spring gathering on t
 dict(g='yku',y=1803.4,pop=None,raw='Each spring the Teton met their Dakota relatives, the Yankton, Yanktonai, and Eastern Dakota at a great trading fair on the James River in present South Dakota ... Tabeau (1939, pp. 121, 131) reported that this Sioux trading fair sometimes attracted as many as 1,000 to 1,200 tents (part)',basis='',loc='stated',at=(45.1, -98.4),r=80,src=EWERS2('p. 10 (pdf 34)'),kind='primary',whole=False),
  # Spring rendezvous (Dakota Rendezvous) on the James R., c.1803-04 (Tabeau). Site placement ours on the James in NE South Dakota; which Teton divisions not stated. Seasonal evidence: Yankton/Yanktonai spring gathering on t
 dict(g='ykl',y=1803.4,pop=None,raw='Each spring the Teton met their Dakota relatives, the Yankton, Yanktonai, and Eastern Dakota at a great trading fair on the James River in present South Dakota ... Tabeau (1939, pp. 121, 131) reported that this Sioux trading fair sometimes attracted as many as 1,000 to 1,200 tents (part)',basis='',loc='stated',at=(45.1, -98.4),r=80,src=EWERS2('p. 10 (pdf 34)'),kind='primary',whole=False),
  # Pre-1837/38 Mandan 600 warriors at the two villages (Mitutanka by Fort Clark, and Ruptare); after: c.30 men; c.1854: c.25 lodges. Compare R0512 ('fewer than 150 survived').
 dict(g='man',y=1837.4,pop=2400,raw='With the Mandan the disease was even more destructive. Before it they numbered 600 warriors and inhabited two large villages where the Arikara are now stationed, and when the disease ceased about 30 men remained, from which remnant have since sprung about 25 lodges.',basis='warriors × 4 (ours)',loc='stated',at=(47.25, -101.27),r=10,src=DENIG46('p. 400 (pdf 15)'),kind='primary'),
  # Arikara return from the Platte and occupy the vacated Mandan village (near Fort Clark) after the 1837-38 smallpox; 500 men. Consistent with R0510.
 dict(g='ari',y=1838.5,pop=2000,raw='The Arikara ... having left the Missouri, had been for years residing on the Platte River ... they returned suddenly from the Platte and took possession of their village a short distance from the Mandan. Now the Arikara numbered about 500 men',basis='warriors × 4 (ours)',loc='stated',at=(47.25, -101.27),r=10,src=DENIG46('p. 400 (pdf 15)'),kind='primary'),
  # 1880 pay-sheet.
 dict(g='sar',y=1880.5,pop=396,raw='for the pay-sheet of the following year records only 396 persons (pay-sheet)',basis='census',loc='inferred',at=(50.95, -114.25),r=150,src=JENNESS('p. 8 (pdf 18)'),kind='primary'),
  # Two conflicting totals in the agency papers.
 dict(g='sar',y=1881.5,pop=470,raw='the pay-sheet for 1881 (the first year in which the annuity was distributed on the present Sarcee reserve near Calgary) 485 or 458, and the pay-sheets for succeeding years numbers that are still smaller. (pay-sheet)',basis='census',loc='stated',at=(50.95, -114.25),r=15,src=JENNESS('p. 8 (pdf 18)'),kind='primary'),
 # ---- Winfrey and Day, eds., Texas Indian Papers, vols. 2–5 (and vol. 1 again)
  # The 'Comanche' proper (lower band) of 1818-19, identified by us with the Penateka ancestors; range centre ours.
 dict(g=['cyp'],y=1819.5,pop=None,raw='The former, with whom we have most intercourse, from their geographical position, occupy the region between the Rivers Colorado of Texas and the Red River of Louisiana; ranging from the sources of the Colorado, including its western affluents, down to the Llano Bayou (place ours)',basis='',loc='stated',at=(32.3, -99.3),r=250,src=TIPV3('doc. No. 78'),kind='primary'),
  # Relative statement only; placement entirely ours (north and west of the Colorado-Red River range). Tenawa (not in division list) further interior.
 dict(g=['cyy'],y=1819.5,pop=None,raw='The Yamparack range the country north and west of the Comanche; and the Tenawa again interior from the latter. (place ours)',basis='',loc='stated',at=(35.0, -101.5),r=350,src=TIPV3('doc. No. 78'),kind='primary'),
  # 'then' = 1818-19, Burnet's visit. Trinity basin centre ours.
 dict(g=['kit'],y=1819.5,pop=None,raw='They held the Keechi, a small and distinct tribe then residing on the waters of the River Trinity, in peculiar detestation, on account of their supposed powers of sorcery. (place ours)',basis='',loc='stated',at=(32.5, -96.3),r=120,src=TIPV3('doc. No. 78'),kind='primary'),
  # Combined figure for Keechi (kit) and the Wichita-group tribes (wic), Oct. 1837; cannot be split. Not found in records.csv. Committee admits 'limited means of information'. Lipan, Karankawa and Tonkawa: 'They occupy the W
 dict(g=['wic', 'kit'],y=1837.78,pop=2000,raw='The Keechi, Tawakoni, Waco and Tawehash or Pawnee are Indians of the Praries ... Their number is about 500 warriors ... These indians reside mostly on the Head waters of the Trinity Brazos and Colorado (place ours)',basis='warriors × 4 (ours)',loc='stated',at=(32.8, -98.5),r=200,src=TIPV1('doc. No. 14'),kind='primary'),
  # Cedar Creek of the Colorado (Bastrop Co.) assumed; Tonkawa without horses.
 dict(g=['tkw'],y=1844.12,pop=None,raw='On the 11th Feby last I left here and proceded direct to the Tonkawa Indians Encampment on Cedar Creek',basis='',loc='stated',at=(30.1, -97.45),r=30,src=TIPV2('doc. No. 111'),kind='primary'),
  # Lipan camps near Goliad, Feb. 1844; most men away on the Rio Grande.
 dict(g=['lip'],y=1844.12,pop=None,raw='From the Tonkawa I proceded direct to the Lipan Camps near Goliad, where I found but few of their tribe—most of them were out as I was informed on the Rio Grande stealing Beef etc. (part)',basis='',loc='stated',at=(28.67, -97.39),r=30,src=TIPV2('doc. No. 111'),kind='primary',whole=False),
  # Keechi village on the Brazos, Mar.-Apr. 1844 (Anadarko village 'about fifty miles above the Council ground on Tehuacana Creek'). The Keechi were 'out hunting' when visited. Placement ours from the distances (Clear Fork m
 dict(g=['kit'],y=1844.2,pop=None,raw='he left for the Keechi village, 200 miles above the Anadarko town, upon the east bank of the river, and 15 or 17 miles from the Clear Fork.',basis='',loc='stated',at=(33.1, -98.55),r=35,src=TIPV2('doc. No. 35'),kind='primary'),
  # Mopechucope (Old Owl), Penateka chief, writing from his camp; 'head of Colorado' placement ours. He adds his people are 'scattered'.
 dict(g=['cyp'],y=1844.22,pop=None,raw='Near the head of Colorado March 21st 1844. (part)',basis='',loc='stated',at=(32.3, -101.0),r=80,src=TIPV2('doc. No. 9'),kind='primary',whole=False),
  # Pahayuko's band (Penateka) at the Salt Plain(s), spring 1844. Watson's version (doc. 18, pdf 17) says 'Pah-hah-yuco is at the Salt Plains Red River', and Sanchez (doc. 35, pdf 36) that he took new skins 'to the Salt Plai
 dict(g=['cyp'],y=1844.22,pop=None,raw='Pah-hah-yuco with some of his band have gone to the Salt plain on Arkansas some have gone over to the Pecos and Rio Grande (part)',basis='',loc='stated',at=(36.7, -98.2),r=120,src=TIPV2('doc. No. 9'),kind='primary',whole=False),
  # Territorial claim of the (Penateka) Comanche, 1844, not a camp. Watson's paraphrase: 'he claimed no territory East of the Brazos that their hunting grounds are west of that river'. Centre of the claimed range ours.
 dict(g=['cyp'],y=1844.22,pop=None,raw='all I want now is a line run between our countries which line I want to commence on Brazos river passing over the Comanche Peak from thare direct to the mouth of the first large creek running in the Colorado on the west-side below the mouth of the San Saba; from thence in a direct line to the Rio Grande; all above that line is Comanche Country (place ours)',basis='',loc='stated',at=(31.5, -99.8),r=250,src=TIPV2('doc. No. 9'),kind='primary'),
  # Meeting on Pecan Bayou, 17-22 Mar. 1844; the Comanche camp itself was not reached (they 'might have crossed to the Pecos, over from the head of the Colorado'). Weak placement.
 dict(g=['cyp'],y=1844.22,pop=None,raw='on the 17th Inst. struck the Pecan Bayou of the Colorado ... two Comanche came into camp, known to John Conner and the head chiefs of the tribe, who informed us it would be impossible for them to come in to the Council ground at the time required, as all their young men were out in different directions (part)',basis='',loc='stated',at=(31.9, -99.1),r=60,src=TIPV2('doc. No. 21'),kind='primary',whole=False),
  # Party of Waco and Tawakoni coming to the Tehuacana Creek council; part of the people remained at their village on the Trinity (upper Trinity, placement ours). Compare Western's figure of 130 souls (next record).
 dict(g=['wic'],y=1844.34,pop=108,raw='There are 54 men, 35 women and 19 children (Waco and Tawakoni). The two tribes live together. part are now at their village planting corn. it is situated on the Trinity, and no village between here and there. (place ours) (part)',basis='census of a travelling party (54 men, 35 women, 19 children)',loc='stated',at=(33.0, -97.5),r=90,src=TIPV2('doc. No. 22'),kind='primary',whole=False),
 dict(g=['wic'],y=1843.5,pop=126,raw='Ledger of gifts to Indians, “Names and number of the different Tribes”: Waco and Tawakoni, number 126, warriors 54 (the Indians present to receive presents; place and month not given)',basis='persons present (part)',loc='inferred',at=(31.5,-97.1),r=150,src=TIPV1('doc. No. 217, table'),kind='primary',whole=False),
 dict(g=['kit'],y=1843.5,pop=28,raw='Ledger of gifts to Indians, “Names and number of the different Tribes”: Keechi, number 28, warriors 12 (the Indians present to receive presents; place and month not given)',basis='persons present (part)',loc='inferred',at=(31.5,-97.1),r=150,src=TIPV1('doc. No. 217, table'),kind='primary',whole=False),
 dict(g=['lip'],y=1845.45,pop=270,raw='“List of the chiefs of the Lipan Tribs as they Gave them to me in council”: Lemas Castro, principal chief; Raymond and John Castro, war chiefs; Capt. Roan, Chicito and Chico, civil chiefs; “By thire own account 67. warriers” (Neighbors, report endorsed June 15, 1845; the printed dateline, Jan. 15, is contradicted by the endorsement and the council of 3 June it reports)',basis='warriors × 4 (ours)',loc='inferred',at=(28.9,-98.5),r=150,src=TIPV2('doc. No. 125, table'),kind='primary'),
  # Waco + Tawakoni (not the Wichita/Tawehash) as brought in to the Tehuacana Creek council, 11 May 1844; Western (doc. 23) says 'Acaquash with about 130 Waco and Tawakoni finally got in'. Ambiguous whether 'they number' mea
 dict(g=['wic'],y=1844.36,pop=130,raw='The next object ... was, to bring into Council the Waco and Tawakoni, who, notwithstanding the Treaty had committed several outrages upon our ceticens, this was effected on the 11th May, they number about 130 souls 60 of whom were Warriors (part)',basis='souls',loc='inferred',at=(34.7, -98.4),r=150,src=TIPV2('doc. No. 114'),kind='primary',whole=False),
  # Council at Tehuacana Creek, 14 Apr.-16 May 1844: Waco, Tawakoni and Keechi (Cho-nah-cio, Kah-te-ah-tic, Sah-sah-roque) present; one Kiowa ('Good Shirt') present (doc. 27-28). Comanche did not come.
 dict(g=['wic', 'kit'],y=1844.36,pop=None,raw='On Saturday, the 11th Ult the Waco and Tawakoni arrived at the Council ground ... Council Ground on Tehuacana Creek (part)',basis='',loc='stated',at=(31.47, -97.05),r=10,src=TIPV2('doc. No. 31'),kind='primary',whole=False),
  # One Kiowa (Good Shirt) at the Tehuacana Creek council. SEASONAL: the Kiowa come nearer (south) 'when the leaves fall'. The place is the council, not the Kiowa range.
 dict(g=['kio'],y=1844.36,pop=None,raw='Coms. “Where do you live, and when do you intend to return to your people?” Kiwh. “My people now live far away, but when the leaves fall they will be near, and I shall go to them. they fear your race and do not come here, yet would be glad of peace.” (part)',basis='',loc='stated',at=(31.47, -97.05),r=10,src=TIPV2('doc. No. 28'),kind='primary',whole=False),
  # Tonkawa near Gonzales, 27 May-1 Sept. 1844; then to the Colorado (camp near Bastrop, women picking cotton, autumn 1844) and later 'encamped on the head of Buckners Creek' (Fayette Co.).
 dict(g=['tkw'],y=1844.5,pop=None,raw='I found on the 27h of May the Tonkawa in the vicinity of Gonzales ... I remained with them until the first of September—The Tonkawa left for the Colorado—by way of the San Marcos.',basis='',loc='stated',at=(29.5, -97.45),r=30,src=TIPV2('doc. No. 111'),kind='primary'),
  # Red Bear's hearsay (via Keechi and Waco), July 1844. Placement on the upper Canadian ours.
 dict(g=['cyy'],y=1844.55,pop=None,raw='the Comanche were of the Yamparika bands who inhabit high up on the Canadian in New Mexico (place ours)',basis='',loc='stated',at=(35.6, -103.0),r=200,src=TIPV2('doc. No. 50'),kind='primary'),
  # Mopechucope's 'Hoish' (Hois = Penateka) band on Pecan Bayou, c. July 1844, heading for the Brazos villages in roasting-ear season. 'Two Great hills' unidentified.
 dict(g=['cyp'],y=1844.55,pop=None,raw="on their way in, they saw on Pecan Bayou at the two Great hills a large number of Comanche coming towards the Villages on this river they were Mopechucope's the Hoish band, he was with them, he said he was going to the Caddo villages Red Bear's house for ear Corn (part)",basis='',loc='stated',at=(31.95, -99.15),r=50,src=TIPV2('doc. No. 50'),kind='primary',whole=False),
  # Wichita (Tawehash) left their Wichita Mountains villages ('about fifty miles north of Red River') to join the Comanche on the Clear Fork, summer 1844. Placement on the Clear Fork ours.
 dict(g=['wic'],y=1844.62,pop=None,raw='whilst traveling on Walnut Bayou we met with some Waco whoom informed us that the Wichita had deserted those Villages and gone with the Comanche to the Clear Fork of the Brazos (part)',basis='',loc='stated',at=(33.0, -99.4),r=80,src=TIPV2('doc. No. 77'),kind='primary',whole=False),
  # Camp of Buffalo Hump and Mopechucope, c. Aug. 1844, reached by heading for the Clear Fork; '200 miles from the Keechi Village' is probably exaggerated. Placement ours (upper Clear Fork/Double Mountain area).
 dict(g=['cyp'],y=1844.65,pop=None,raw='we then left for the Comanche on the Clear Fork of Brazos after traveling some nine or ten days through the heat on tired animals we found the Comanche about two hundred miles from the Keechi Village after our arrival we held a council with the Comanche whoom all appeared to be well disposed but the young man (Buffalo Hump) (place ours) (part)',basis='',loc='stated',at=(32.9, -100.3),r=120,src=TIPV2('doc. No. 74'),kind='primary',whole=False),
  # Waco and Tawakoni, after a horse-stealing alarm, moved from their villages to the mouth of the Clear Fork, Aug.-Sept. 1844.
 dict(g=['wic'],y=1844.68,pop=None,raw='on our rout we passed through the Waco and Tawakoni villages which we found all evacuated none of them to be found; though we found plenty of peas and pumpkins ... then they removed to the mouth of the Clear Fork of the Brazos whare we understand they still remain (part)',basis='',loc='stated',at=(33.0, -98.75),r=30,src=TIPV2('doc. No. 77'),kind='primary',whole=False),
  # Council at the Keechi village on the Brazos, 13 Sept. 1844 (placement as for the Keechi village above).
 dict(g=['cyp', 'kit', 'wic'],y=1844.7,pop=None,raw='on the 12th of Sept we landed at the Keechi village whare we found James Shaw with the Comanche ... we also found some of the Waco and Tawakoni; on the following day we met the Comanche Keechi Waco Tawakoni and Caddo in Council (place ours) (part)',basis='',loc='stated',at=(33.1, -98.55),r=35,src=TIPV2('doc. No. 77'),kind='primary',whole=False),
  # Buffalo Hump, Oct. 1844: his people range on the Brazos ('this river'); they follow the buffalo down in season. Also: the Kiowa 'are more powerful than the Comanche and we fear them'. Placement ours.
 dict(g=['cyp'],y=1844.77,pop=None,raw='Comanche Chief “I do not think that my people will go in that direction, there are many bad indians traveling through there, the Kiowa are now at war with your people. I shall stay on this river and in this direction.” ... “The Comanche never understood it so, when the buffalo come below there is nothing for us to eat above.” (place ours) (part)',basis='',loc='stated',at=(32.3, -98.5),r=150,src=TIPV2('doc. Nos. 75-76'),kind='primary',whole=False),
  # Tonkawa on the Colorado near Bastrop and at the head of Buckner's Creek, autumn 1844; 'a portion of their tribe was out west stealing Mexican horses'.
 dict(g=['tkw'],y=1844.8,pop=None,raw='I returned to the Tonkawa camp on the Colorado—where I found the women picking out cotton and many of the men lying about Bastrop drunk ... I came by Tonkawa Encamped on the head of Buckners Creek (part)',basis='',loc='stated',at=(30.0, -97.25),r=30,src=TIPV2('doc. No. 111'),kind='primary',whole=False),
  # Tawakoni village ~15 miles from the Keechi village, Waco village beyond, Oct.-Nov. 1844; four Waco horses 'then absent on a Buffalo Hunt'. Acaquash had been living at the Keechi village since April. Placement ours.
 dict(g=['wic'],y=1844.84,pop=None,raw='We then proceeded in the direction of the Waco Village and after proceeding some 15 miles came upon the Tawakoni Village ... We then proceeded to the Waco Village where we arrived on the 1st Nov. (place ours) (part)',basis='',loc='stated',at=(33.15, -98.45),r=50,src=TIPV2('doc. No. 103'),kind='primary',whole=False),
  # Autumn 1844 grand council of Comanche, Kiowa, Arapaho and Cheyenne with Buffalo Hump; NO location given (so no coordinates). Kept as context only.
 dict(g=['cyp', 'cyn', 'cyy', 'cyk', 'cyq', 'kio'],y=1844.85,pop=None,raw='they all stated to me that the Comanche Kiowa Arapaho and Cheyenne were counseling together in large numbers with Buffalo Hump and his party',basis='',loc='inferred',at=(32.73, -99.03),r=150,src=TIPV2('doc. No. 103'),kind='primary',whole=False),
  # SEASONAL: Pahayuko, at the Brazos trading house in January 1845, says his people come down with their families among the buffalo near the trading house in winter; in spring they will range from the Colorado to the Guadal
 dict(g=['cyp'],y=1845.05,pop=None,raw='The Buffalo are close by here, and we are obliged to come down with our families among them ... In the Spring some of my men will be down about San Antonio ... We shall rang[e] from the Colorado to the Guadalupe (place ours) (part)',basis='',loc='stated',at=(31.47, -97.05),r=80,src=TIPV2('doc. No. 129'),kind='primary',whole=False),
  # Lipan camp on the Cibolo near the La Bahia road crossing, Mar.-May 1845 (repeated doc. 206, 216). La Bahia road crossing location approximate.
 dict(g=['lip'],y=1845.17,pop=None,raw='It appears that the information had that the Lipan were on the Bosque was erroneous; Ramon Castro one of their Captains and another individual of are now here, they say their Camp is on the Cibolo—San Baitolo—near the Crossing of the La Bahía Road. (part)',basis='',loc='stated',at=(29.3, -98.0),r=30,src=TIPV2('doc. No. 169'),kind='primary',whole=False),
  # Hunting ground designated on the San Marcos (doc. 160: 'a Suitable place for third Camps on the St. Marks Either above or below the San Antonio Road'). Placement ours.
 dict(g=['tkw'],y=1845.25,pop=None,raw='I am happy to find that the Tonkawa Indians are all collected together on the hunting grounds designated for their use that they are doing well and are contented and that game is in abundance. (place ours)',basis='',loc='stated',at=(29.9, -97.95),r=40,src=TIPV2('doc. No. 195'),kind='primary'),
  # Second-hand report reaching Western, May 1845. 'The main body' of the Comanche who were treating with Texas (Penateka-led; Pahayuko, Buffalo Hump, Mopechucope) - divisions not stated, so all five listed; probably mainly 
 dict(g=['cyp', 'cyn', 'cyy', 'cyk', 'cyq'],y=1845.36,pop=None,raw='Information has just been recd at this office of the arrival at the trading House on the Brazos of a party of Comanche, and that the main body of them Consisting of about 1000. Lodges are encamped on Little River, they are bound Westward to redress their wrongs beyond the Rio Grande (part)',basis='',loc='stated',at=(31.0, -97.5),r=60,src=TIPV2('doc. Nos. 204'),kind='primary',whole=False),
  # Lipan main camp, visited 5 June 1845 (talk held 3 June). Doc. heading reads 'Jan. 14th 1845' but the text dates events to June 1845. Also 'about 30 Comanche' of Santa Anna's party (cyp), whipped near Matamoros, staying i
 dict(g=['lip'],y=1845.43,pop=None,raw='I found that there main camp was on the Borrego [Boregas], a branch of the Atascosa about 50 miles South of San Antonio. A small party of them near Dn. Erasmo Seguins Ranch',basis='',loc='stated',at=(28.85, -98.5),r=30,src=TIPV2('doc. No. 124'),kind='primary'),
  # A small Penateka party (Santa Anna's) with the Lipan; leader Ta-na-cio-quache (Bear's Tail).
 dict(g=['cyp'],y=1845.43,pop=30,raw='I found about 30 Comanche in Their camp on the Borrego [Boregas Creek] ... they say they belong to Santa Anna party.',basis='persons in a war party',loc='stated',at=(28.85, -98.5),r=30,src=TIPV2('doc. No. 124'),kind='primary',whole=False),
  # Mopechucope's village on the waters of Little River, June 1845.
 dict(g=['cyp'],y=1845.47,pop=None,raw='with these proceed to the Comanche Village on the waters of Little River and having amicably arranged with Mopechucope. with him proceed to the City of Austin (part)',basis='',loc='stated',at=(31.0, -97.7),r=50,src=TIPV2('doc. No. 237'),kind='primary',whole=False),
  # Mopechucope on the Colorado above Austin (to remain there until the September council); Pahayuko's band on the headwaters of the Brazos, 'out of the Buffalo Range' in June. A large party of Comanche near San Antonio.
 dict(g=['cyp'],y=1845.48,pop=None,raw='Mopechucope who is now encamped on the Colorado above Austin ... Pah-hah yuco is on the head waters of the Brazos but that he will be down and join Mopechucope. in a short time, as they are in want of meat, and are out of the Buffalo Range where they are. (part)',basis='',loc='stated',at=(30.5, -98.0),r=50,src=TIPV2('doc. No. 238'),kind='primary',whole=False),
  # Pahayuko's band, June 1845, headwaters of the Brazos (placement ours).
 dict(g=['cyp'],y=1845.48,pop=None,raw='Pah-hah yuco is on the head waters of the Brazos but that he will be down and join Mopechucope. in a short time, as they are in want of meat, and are out of the Buffalo Range where they are. (place ours) (part)',basis='',loc='stated',at=(33.2, -100.8),r=150,src=TIPV2('doc. No. 238'),kind='primary',whole=False),
  # Tonkawa on Cibolo Creek near the old Gonzales crossing, 30 June 1845 (date as printed). The Lipan wished the Tonkawa to join them for 'a long Buffalo Hunt on the upper Brazos and Colorado' with families before the Septem
 dict(g=['tkw'],y=1845.49,pop=None,raw='On the 30th Jun I visited the Tonkawa Camp. and found Them Camped on the Cibolo near the old Gonzales crossing.',basis='',loc='stated',at=(29.45, -98.05),r=25,src=TIPV2('doc. No. 124'),kind='primary'),
  # Mopechucope's village on the San Saba, mid-July to late Aug. 1845; Buffalo Hump arrived with his band 6 Aug. ('Buffalo Hump arived to this Mopechucope vilage on the San Saba from Pah hah yuco vilage', doc. 290). Later th
 dict(g=['cyp'],y=1845.54,pop=None,raw='the fifth Day after levin Austin i found them incamped on the San Saba this was Mopechucope Band (part)',basis='',loc='stated',at=(31.0, -99.4),r=60,src=TIPV2('doc. No. 262'),kind='primary',whole=False),
  # Villages of Buffalo Hump and Pahayuko on the Clear Fork, July 1845.
 dict(g=['cyp'],y=1845.56,pop=None,raw='Buffalo Hump and Pah hah yu co vilag air on the Clear Fork of the Brazos which they will rmane thair untl wee can get thir (part)',basis='',loc='stated',at=(32.9, -99.6),r=70,src=TIPV2('doc. No. 262'),kind='primary',whole=False),
  # Council of 12-25 Sept. 1845: Comanche (Mopechucope's band with Saviah etc.; Pahayuko/'Powauca' absent), Lipan (Ramon Castro, Chicito, Chico + 3 warriors), Tonkawa (Campo, Placido, Jose + 5 warriors). Lipan and Tonkawa 'c
 dict(g=['cyp', 'lip', 'tkw'],y=1845.72,pop=None,raw='On the 12th Inst we met the Comanche Indians under Mo-pe-chu-co-pe, and encamped with them at the Council Ground near the Brazos River, and within four miles of this Post. In a day or two representatives from the Anadarko, Caddo, Cherokee, Delaware, Ioni, Lipan and Tonkawa, arrived (part)',basis='',loc='stated',at=(31.47, -97.05),r=10,src=TIPV2('doc. No. 300'),kind='primary',whole=False),
  # Pahayuko's band, autumn 1845, 'a long way off, up among the Mountains' (Wichita Mountains? ours, very uncertain).
 dict(g=['cyp'],y=1845.8,pop=None,raw='Mopechucope started in quest of Pah-hah yuco, and struck his trail high up the country and followed on it for several days, but was unable to overtake them ... Pah-hah yuco has gone a long way off, up among the Mountains and they do not think he will return this fall (place ours) (part)',basis='',loc='stated',at=(34.8, -99.0),r=250,src=TIPV2('doc. No. 364'),kind='primary',whole=False),
  # Council at Torrey's Post No. 2 (Tehuacana Creek): Acaquash (Waco), Kechikaroqua (Tawakoni), Saatzarook (Keechi), Saatzarwaritz (Wichita, 'first of all the Wichita Chiefs that has come down to make peace').
 dict(g=['wic', 'kit'],y=1845.87,pop=None,raw='by the 13th the Chiefs of Waco, Tawakoni, Keechi and Wichita, together with a number of their warriors, women and children, were upon the ground (part)',basis='',loc='stated',at=(31.47, -97.05),r=10,src=TIPV2('doc. Nos. 367-371'),kind='primary',whole=False),
  # Santa Anna's party (Penateka) with Mopechucope at Post No. 2: 12 named chiefs/captains plus nearly 40 warriors. A visiting party, not a band total.
 dict(g=['cyp'],y=1845.89,pop=160,raw="Report of a Council held with the Comanche Indians ... Mopechucope Ahkatsica, Santa Anna, ... who are all with exception of the first two, chiefs or captains belonging to Santa Anna's party. There was also present nearly Forty warriours (part)",basis='warriors × 4 (ours)',loc='stated',at=(31.47, -97.05),r=10,src=TIPV2('doc. No. 376'),kind='primary',whole=False),
  # Winter 1845-46. 'Above this place' = above Austin. A later letter (doc. 394, Post No. 2) says 'the tribe of Lipan are all in this neighborhood hunting'.
 dict(g=['lip'],y=1845.95,pop=None,raw='The Lipan have been removed from the San Antonio River to the San Gabriel above this place—The Tonkawa are on the Rio Blanco',basis='',loc='stated',at=(30.65, -97.75),r=40,src=TIPV2('doc. No. 386'),kind='primary'),
  # Blanco River (Hays Co.), winter 1845-46.
 dict(g=['tkw'],y=1845.95,pop=None,raw='The Tonkawa are on the Rio Blanco',basis='',loc='stated',at=(29.95, -98.0),r=30,src=TIPV2('doc. No. 386'),kind='primary'),
  # Winter 1845-46. 'During the past cold weather they have scatered very much in pursuit of Game rendering it impossible for me to take their sensus'. No numbers given.
 dict(g=['lip', 'tkw'],y=1846.09,pop=None,raw='the Lipan and Tonkawa are in much the same position, as regards locality, as they were at my last report. They are contented to occupy the vacant country between the San Marks [Marcos] and San Antonio Rivers',basis='',loc='stated',at=(29.55, -98.0),r=50,src=TIPV3('doc. No. 21'),kind='primary'),
  # Comanche Peak (Hood Co.) council site, early 1846; Lipan and Tonkawa en route (party only).
 dict(g=['lip', 'tkw'],y=1846.1,pop=None,raw='The two tribes has been invited to attend a council to be held at the Comanche Peak by Col. Butler and Majr. Lewis U. S. Commissioners on the part of the U. States and are now on their way to meet them. (part)',basis='',loc='stated',at=(32.25, -97.78),r=25,src=TIPV3('doc. No. 21'),kind='primary',whole=False),
  # Intended planting place for 1846 ('old Town' on Cibolo Creek); exact site unknown, Cibolo centre ours.
 dict(g=['lip'],y=1846.25,pop=None,raw='The Lipan are also anxious to be settled and will plant corn and grain, this year on the Cibolo at their old Town. (part)',basis='',loc='stated',at=(29.45, -98.15),r=40,src=TIPV3('doc. No. 21'),kind='primary',whole=False),
  # Council/treaty: Comanche signers Pah-hah-yuco, Mopechucope (Old Owl), Pochanaquarhip (Buffalo Hump), Santa Anna, Saviah etc. = Penateka (cyp); Waco, Tawakoni, Wichita signers (wic); Keechi (kit); Tonkawa signers (Campos 
 dict(g=['cyp', 'wic', 'kit', 'tkw', 'lip'],y=1846.37,pop=None,raw='Articles of a treaty made and concluded at Council Springs, in the county of Robertson Texas, near the Brazos River, this 15th day of May, A.D. 1846 ... Comanche, Ioni, Anadarko, Caddo, Lipan, Longwa, Keechi, Tah-wa-carro [Tawakoni], Wichita, and Waco (part)',basis='',loc='stated',at=(31.3, -96.9),r=35,src=TIPV3('doc. Nos. 59-60'),kind='primary',whole=False),
  # Council at Torrey's Trading House (Tehuacana Creek near Waco), c. Dec. 1846-early Jan. 1847. 'Friendly Comanche chiefs' = Penateka by inference. A council ground near Torrey's is again mentioned for Sept. 1847 (doc. 77) 
 dict(g=['cyp'],y=1846.95,pop=None,raw='Major Nabors [Neighbors] returned to this place a few days since from Torreys trading house where he met the friendly Comanche Chiefs and various other Indian Tribes (part)',basis='',loc='stated',at=(31.48, -97.05),r=15,src=TIPV3('doc. No. 76'),kind='primary',whole=False),
  # Tonkawa, 1847.
 dict(g=['tkw'],y=1847.6,pop=600,raw='There are about 150 warriors of this tribe—they have usually warred within the limits of our settlements.',basis='warriors × 4 (ours)',loc='inferred',at=(31.72, -98.26),r=150,src=TIPV3('doc. No. 78'),kind='primary'),
  # Waco only (part of the wic aggregate). 'Upper Brazos' village placement ours (Waco then above Torrey's trading house, Bosque/Brazos area). Seasonal: winters spent hunting away from the village.
 dict(g=['wic'],y=1847.6,pop=600,raw='The Waco are the most considerable of these bands, amounting probably to 150 warriors, it being understood among Indians that every adult male is a warrior. ... They live in a village on the Upper Brazos, and raise corn, beans, pumpkins, etc., and usually spend the winter months in hunting. (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(31.9, -97.6),r=100,src=TIPV3('doc. No. 78'),kind='primary',whole=False),
  # 'Other small parties' = Tawakoni, Tawehash, Aynic, San Pedro's, Nabaduco, Nacadoche (Hitchi=Keechi said merged). Only Tawakoni/Tawehash (wic) and possibly Keechi in scope; no total population can be read; pop left null. 
 dict(g=['wic', 'kit'],y=1847.6,pop=None,raw='The other small parties, amounting to about fifty families each, live in villages, on the waters of the Trinity and Neches, and cultivate the ground to a small extent. (place ours) (part)',basis='',loc='stated',at=(32.3, -96.0),r=150,src=TIPV3('doc. No. 78'),kind='primary',whole=False),
  # Waco on the upper Brazos, summer 1847 (Santa Anna's report). Same letter: Santa Anna had 'lately left that section of country very suddenly ... with all the women & children of his tribe' and was advised to move near Tor
 dict(g=['wic'],y=1847.6,pop=None,raw='He states also that during his absence he had occasion to visit the Wacoes on the upper waters of the Brassos River and that while there the Wacoes had a “Scalp dance” (place ours) (part)',basis='',loc='stated',at=(32.2, -97.8),r=100,src=TIPV5('doc. No. 27'),kind='primary',whole=False),
  # Santa Anna's band near the German settlements (Fredericksburg) before its sudden flight north, summer 1847. Placement ours.
 dict(g=['cyp'],y=1847.6,pop=None,raw='Santa Anna the Comanche Indian Chief who lately left that section of country very suddenly & under suspicious circumstances with all the women & children of his tribe, has returned ... Capt Grumbles advised Santa Anna to take his people and move on near Torreys Trading house on the Brassos river (place ours) (part)',basis='',loc='stated',at=(30.3, -98.9),r=80,src=TIPV5('doc. No. 27'),kind='primary',whole=False),
  # Winter ground statement (Neighbors, 1849). 'These Indians' = the Texas tribes of his (missing) estimate table, chiefly the Comanche; Kiowa and Apache are named in the same paragraph as little known, so their inclusion is
 dict(g=['cyp', 'cyn', 'cyy', 'cyk', 'cyq', 'kio', 'kap'],y=1849.0,pop=None,raw='These Indians range promiscuously across our frontier, from Red River to the Rio Grande, during the greater portion of the year, and seek shelter during the winter in the uppor cross timbers of Texas, between the head waters of the Colorado River and the Wichita Mountains. (place ours)',basis='',loc='stated',at=(33.3, -99.4),r=200,src=TIPV3('doc. No. 87'),kind='primary'),
  # Lipan band of Chiquito and Chapota, Sept. 1850, on the Concho (placement on the river ours).
 dict(g=['lip'],y=1850.72,pop=None,raw='The party encamped on the Concho and seen by Major Henry and his party came in manifesting every token of friendship ... This party is under the control of the Civil Chief Che-ke-to and the war chief Cha-po-ta (part)',basis='',loc='stated',at=(31.45, -100.45),r=60,src=TIPV3('doc. No. 94'),kind='primary',whole=False),
  # Larger Lipan division, summer/autumn 1850, planting on the Pecos; stretch of Pecos not stated (placement ours, wide radius).
 dict(g=['lip'],y=1850.72,pop=None,raw='The larger portion of the Lipan are encamped on the Pecos where they made corn this year and the accounts as to these are not very full or satisfactory. (place ours) (part)',basis='',loc='stated',at=(30.6, -101.9),r=150,src=TIPV3('doc. No. 94'),kind='primary',whole=False),
  # Hearsay from the Lipan (Rollins warns 'to be taken with some allowance'). The Comanche near the Texas settlements = Penateka; 'all' suggests whole division. Left the Colorado about a month before (Aug. 1850).
 dict(g=['cyp'],y=1850.72,pop=None,raw='The Lipan report the Comanche hostile. That they have all gone to the “Clear Fork of the Brazos” and would kill any white persons they might find. That there are no Comanche West of the Colorado except occasionally a small war party',basis='',loc='stated',at=(32.9, -99.5),r=70,src=TIPV3('doc. No. 94'),kind='primary'),
  # Council. Signers: Comanche Po-cha-na-quar-hip (Buffalo Hump), Sa-vi-ah, Ka-tumpsa (cyp); Lipan Chi-ci-to; Tawakoni and Waco chiefs (wic); also Caddo, Quapaw. Spring Creek head spring location approximate (ours).
 dict(g=['cyp', 'lip', 'wic'],y=1850.94,pop=None,raw='Held at the head spring of Spring Cr. South of but near the River San Saba. made and concluded on Spring Creek, near the River San Saba, in the Indian Country of the State of Texas, this, the 10th day of December, A.D. 1850 (part)',basis='',loc='stated',at=(30.85, -100.0),r=35,src=TIPV3('doc. No. 98'),kind='primary',whole=False),
  # Council with Katumpsa (Ketumsee) 'principle chief of the Comanche of the South' (cyp) and Lipan chiefs Chiquito, Quaco, Col. Lamos, Hernandes for Shanaca (lip). Old fort = Presidio de San Saba (Menard); 7 miles below = o
 dict(g=['cyp', 'lip'],y=1851.82,pop=None,raw='I consented to fill his Appointment at a point Seven miles below the old Fort on the San Saba, on the 10th of October next ... Proceedings had at ... San Saba, treaty Grounds 26th October 1851 ... the Comanche, (Known as the Southern Comanche,) the Lipan and Mescalero (part)',basis='',loc='stated',at=(30.93, -99.68),r=15,src=TIPV3('doc. Nos. 101-105'),kind='primary',whole=False),
  # Pecos Lipan move to San Fernando (Zaragoza), Coahuila, Jan. 1854. Another Lipan party and the Tonkawa remained near Fort Inge.
 dict(g=['lip'],y=1854.03,pop=None,raw='Early in January last the party of Lipans who have always resided on the Pecos, crossed the Rio Grande, at the solicitation of the Mexican authorities and Established themselves in the neighborhood of San Fernando (part)',basis='',loc='stated',at=(28.5, -100.9),r=30,src=TIPV5('doc. No. 128'),kind='primary',whole=False),
  # Lipan band of Chepita at the agency near Fort Inge / head of the Nueces, early 1854. 'Not more than one hundred' warriors is a hostile estimate.
 dict(g=['lip'],y=1854.2,pop=400,raw='Lipan Indians, who are encamped on the head waters of the Nueces, having an agent living among them; and we understand are even now being fed from the U. S. Post of Fort Inge on the Leona ... the names of the warriors of the Lipan tribe at his agency, (not believed to be more than one hundred) (part)',basis='warriors × 4 (ours)',loc='stated',at=(29.5, -99.9),r=50,src=TIPV5('doc. No. 120'),kind='primary',whole=False),
  # Lipan (one party) and Tonkawa camped near Fort Inge on the Leona, spring 1854; doc. 132 (Neighbors, May 1854) assembles 'that Tribe' (Tonkawa) at Fort Inge.
 dict(g=['lip', 'tkw'],y=1854.27,pop=None,raw='He has remained constantly in Camp with the party of Lipans, near Fort Inge as well as the Tonkawas (part)',basis='',loc='stated',at=(29.18, -99.77),r=20,src=TIPV5('doc. No. 128'),kind='primary',whole=False),
  # SEASONAL: Clear Fork of the Brazos = the Southern Comanche's 'old wintering grounds'. Reserve tract 'about forty miles from Fort Belknap' (Camp Cooper area).
 dict(g=['cyp'],y=1854.6,pop=None,raw='We have also conferred with Sanaco, Katumpsa, and other chiefs of the southern Comanche, and have found many of them apparently united in their willingness to accede ... in establishing a permanent settlement near their old wintering grounds upon the Clear Fork of the Brazos.',basis='',loc='stated',at=(32.98, -99.3),r=40,src=TIPV3('doc. No. 125'),kind='primary'),
  # Waco (part of wic) living on the Brazos below Fort Belknap, summer 1854; they 'are already making preparations to go upon the tract and erect their winter habitations'.
 dict(g=['wic'],y=1854.6,pop=None,raw='We have accordingly counciled with the Chiefs of the Ioni, Anadarko, Caddo and Waco living upon the Brazos below Fort Belknap (part)',basis='',loc='stated',at=(33.05, -98.65),r=25,src=TIPV3('doc. No. 125'),kind='primary',whole=False),
  # Northern Comanche and Kiowa claim the hunting grounds north of the Brazos (1854). Placement ours; which northern divisions is not stated.
 dict(g=['cyy', 'cyk', 'cyn', 'cyq', 'kio'],y=1854.6,pop=None,raw='they have no protection from the northern Comanche and Kiowa who are much more numerous than themselves, and do not even allow them to hunt north of the Brazos River ... the section of country which they (the northern Indians) claim as their own hunting grounds (place ours) (part)',basis='',loc='stated',at=(33.8, -99.5),r=200,src=TIPV3('doc. No. 125'),kind='primary',whole=False),
  # 1854: 'many of the Lipan are now hostile'. West of the Pecos, placement ours.
 dict(g=['lip'],y=1854.6,pop=None,raw='These indians are at present living west of the Pecos River and consist of the Mescalero Apache, and the Lipan. (place ours) (part)',basis='',loc='stated',at=(30.5, -103.0),r=200,src=TIPV3('doc. No. 125'),kind='primary',whole=False),
  # Waco and Tawakoni with Caddo, Ioni, Anadarko, on the Brazos below Fort Belknap; Parker accompanied Marcy in 1854. The Parker census table (doc. 131) is NOT reproduced in this edition.
 dict(g=['wic'],y=1854.6,pop=None,raw='They (with the Waco and Tawakoni) live in houses built of a framework of poles ... They live in great harmony together, on the Brazos, below Fort Belknap (part)',basis='',loc='stated',at=(33.05, -98.65),r=25,src=TIPV3('doc. No. 130'),kind='primary',whole=False),
  # 'Kush Creek' = Rush Creek (Rush Springs, Okla.), by our identification. Wichita proper (part of wic).
 dict(g=['wic'],y=1854.6,pop=None,raw='The Wichita live in the Choctaw territory, on Kush Creek (part)',basis='',loc='stated',at=(34.78, -97.95),r=25,src=TIPV3('doc. No. 130'),kind='primary',whole=False),
  # Near Fort Belknap (Maj. Steen's post). Mixed 'friendly Indians' awaiting the reserves: Caddo, Anadarko, Ioni, Waco, Tawakoni, Tonkawa and Southern Comanche probably (tribes not named; group list ours). Do not attribute t
 dict(g=['cyp', 'wic', 'tkw'],y=1854.9,pop=1800,raw='there is a huge Body of the Friendly Indians Now assembled near his post. They number about 1800 Souls, and have assembled with the full intention of settling on the Indian Reservations (part)',basis='souls (mixed tribes)',loc='stated',at=(33.15, -98.74),r=25,src=TIPV3('doc. No. 126'),kind='primary',whole=False),
  # Crossing 'near the large Spring and Double Hills about halfway between Laredo and Eagle Pass'; Lipan camp a few miles inside Mexico. Hearsay at Laredo; whether 'the tribe' means all Lipan is uncertain.
 dict(g=['lip'],y=1855.55,pop=300,raw='there learned that the Lipan tribe, for some time, had been concentrated and established in Mexico, a few miles from the point at which the trail crossed the Rio Grande—and that the number of the tribe was about three hundred; who had about fifteen hundred horses. (place ours)',basis="souls (hearsay, 'number of the tribe')",loc='stated',at=(28.1, -100.0),r=60,src=TIPV3('doc. No. 140'),kind='secondary'),
  # SEASONAL: summer 1855, the Northern Comanche bands with their families are near the Arkansas. Raiding parties 'not more than from 30 to 50 in all'.
 dict(g=['cyy', 'cyk', 'cyn', 'cyq'],y=1855.57,pop=None,raw='All the Northern Comanches bands, are now north near the Arkansas river with their families—and the few parties who are stealing are parties, who as soon as the families of the Indians went North out of our reach—detached themselves for the purposes of horse stealing (place ours)',basis='',loc='stated',at=(37.5, -99.5),r=200,src=TIPV5('doc. No. 142'),kind='primary'),
  # Rumour from Waco about the Clear Fork (Comanche) reserve, winter 1857-58; probably exaggerated (cf. R0721: about 450 Penateka settled there in 1855).
 dict(g=['cyp'],y=1858.12,pop=600,raw='information received of the absconding of some 600 Comanches from the uper agency above Fort Belknap, after having received their Winter supplies (part)',basis='persons (rumour)',loc='stated',at=(32.98, -99.3),r=20,src=TIPV5('doc. No. 162'),kind='primary',whole=False),
  # The hostile (northern) Comanche camps, spring 1858, as located by Ford's informants; placement ours between the Wichita Mountains and the Canadian. Ford found them on the Canadian on 12 May.
 dict(g=['cyy', 'cyk', 'cyn', 'cyq'],y=1858.27,pop=None,raw='The Comanches are now on Red River, just below the mountains, and not far from the Fort Smith and Santa Fe road. We can reach them in twelve or fifteen days. (place ours) (part)',basis='',loc='stated',at=(35.2, -99.4),r=120,src=TIPV5('doc. No. 164'),kind='primary',whole=False),
  # Buffalo Hump's band on the Canadian ~12 miles below Iron Jacket's camp, 12 May 1858 (placement ours).
 dict(g=['cyp'],y=1858.36,pop=None,raw='We learned from a captured woman that Buffalo Hump was twelve miles below us with a considerable body of warriors (place ours) (part)',basis='',loc='stated',at=(35.9, -99.65),r=20,src=TIPV5('doc. No. 169'),kind='primary',whole=False),
  # Seasonal claim only, no location stated. Context for notes.
 dict(g=['cyp', 'cyn', 'cyy', 'cyk', 'cyq'],y=1858.4,pop=None,raw='The Comanches and other tribes are raging a relentless and exterminating war upon us ... We have now a correct idea of its geography and topography. We know where they winter—when, where and how to find them (part)',basis='',loc='inferred',at=(34.95, -98.25),r=150,src=TIPV5('doc. No. 172'),kind='primary',whole=False),
  # Keechi village (with the Kickapoo) in the Chickasaw/leased district near Fort Arbuckle, June 1858; men away on the buffalo hunt. Keechi chief Chic-ah-heh. Placement ours.
 dict(g=['kit'],y=1858.45,pop=None,raw='They visited Fort Arbuckle, the Keechie and Kickapoo villages. At these villages they found no men, the women said the warriors were out hunting Buffalo. (place ours)',basis='',loc='stated',at=(34.75, -97.6),r=50,src=TIPV5('doc. No. 176'),kind='primary'),
  # Hearsay, June 1858: one Comanche band's families moved into the Creek country (Indian Territory); 'the other six bands are to continue the war'. Seven bands. Placement ours.
 dict(g=['cyp', 'cyn', 'cyy', 'cyk', 'cyq'],y=1858.45,pop=None,raw='the different bands of the Comanches had recently held a council, and agreed to consolidate the seven bands into one, under the leadership of the nephew of the late chief Pa.ha.yo co.— ... the headchief has taken the women, children, and old men into the Creek country, which he deems a place of safety for them (place ours) (part)',basis='',loc='stated',at=(35.3, -96.5),r=150,src=TIPV5('doc. No. 176'),kind='primary',whole=False),
  # Buffalo Hump's band, late Aug. 1858, north of the Big Wichita towards the Wichita villages (where Van Dorn attacked it on 1 Oct., R0780). Placement ours.
 dict(g=['cyp'],y=1858.65,pop=180,raw='Chul-equa and his command returned this morning, bringing with them 60 head of horses, and mules, captured from Buffalo Humps band of Comanches. He had no fight with them, as when about to attack a party of some 40 or 50 warriors, he was met by a Witchita chief (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(34.8, -98.0),r=60,src=TIPV5('doc. No. 190'),kind='primary',whole=False),
  # Hearsay (Chul-e-qua), Aug. 1858. Comanche divisions not stated (northern bands assumed).
 dict(g=['kio', 'cyy', 'cyk', 'kit'],y=1858.65,pop=None,raw='large bodies of hostile Indians, composed of Kioways, Comanches, Chyennes & Keechies—were encamped near. Antelope Hills on the Canadian, with the declared intention of making a descent upon this frontier (part)',basis='',loc='stated',at=(35.95, -99.85),r=40,src=TIPV5('doc. No. 190'),kind='primary',whole=False),
  # SEASONAL: winter 1858-59 camps of the hostile Comanche on the heads of the Red and 'Arkansas' (probably the Canadian is meant); horses wintered on cottonwood bark. Placement ours.
 dict(g=['cyy', 'cyk', 'cyn', 'cyq'],y=1859.14,pop=None,raw='The main Comanche camps are on the head-waters of the Red and Arkansas rivers. They are subsisting their horses on cotton-wood and it is almost certain they have a camp on this side of Red River, in the Cedar mountains (place ours) (part)',basis='',loc='stated',at=(35.3, -101.0),r=250,src=TIPV5('doc. No. 222'),kind='primary',whole=False),
  # Penateka on the Comanche (Clear Fork) Reserve, July 1859, just before removal; fight with Nowlin's state troops near the reserve 24 July 1859. Ford reached the Comanche Agency 30 Mar. 1859 (doc. 251).
 dict(g=['cyp'],y=1859.56,pop=None,raw='the fight occurred near the Comanche Reserve ... Proceeding up the valley of the Clear Fork I visited the Comanche Agency & notified Agent Leeper',basis='',loc='stated',at=(32.98, -99.3),r=15,src=TIPV5('doc. Nos. 264'),kind='primary'),
  # Tonkawa, Waco and Tawakoni (with Caddo, Anadarko) on the lower (Brazos) Reserve, July 1859; Brown camped at Caddo Springs. 'From all I can learn the Indians will leave by the first of August' (vol. 3 doc. 227). Keechi pr
 dict(g=['tkw', 'wic'],y=1859.56,pop=None,raw='we had come near falling in with a party of Tonkaways from the lower Reserve who had been up there unaccompanied by white men & without permit ... My head quarters for the present will be on the Brazos near Caddo Springs and just outside of the Reserve',basis='',loc='stated',at=(33.05, -98.62),r=15,src=TIPV5('doc. No. 267')+'; vol. 3, doc. No. 224',kind='primary'),
  # The Leased District (Wichita Agency near Fort Cobb), spring 1860, after the 1859 removal. Comanche here = the former reserve Penateka.
 dict(g=['cyp', 'tkw', 'kit', 'wic'],y=1860.3,pop=None,raw='there are nine different bands & parts of bands now resident in this district, viz; Caddo, Anadarko, Comanche, Tonkawa, Ioni, Keechi, Wichita, Waco, and Tawakoni',basis='',loc='stated',at=(35.12, -98.43),r=40,src=TIPV4('doc. No. 22'),kind='primary'),
  # Territorial claim of the Wichita, Waco and Tawakoni (1860), not a camp; centre ours.
 dict(g=['wic'],y=1860.3,pop=None,raw='They say that this Country, by which they mean all that country lying between the Red River and the Canadian River, from the mouth of the False Washita on River to a point due north of the same on the Canadian as its Eastern boundary, and as far west as the west end of the Wichita Mountains is exclusively their own (place ours)',basis='',loc='stated',at=(34.9, -98.0),r=150,src=TIPV4('doc. No. 22'),kind='primary'),
  # Comanche on the Arkansas, c. 1861-62 (Loving's cattle trip to Pikes Peak). 'Fort Adams' unidentified (Fort Larned/Fort Wise?). Divisions ours (the Arkansas-river Comanche = Yamparika/Kotsoteka).
 dict(g=['cyy', 'cyk'],y=1862.3,pop=None,raw='the general rendezvous of the Indians who depredate upon the frontier of Texas is upon the Arkansas River say 350 or 400 miles from here, As I returned home some two months since I saw a large number of Comanche with some four or five thousand horses ... fed by the U. S. Posts at Fort Adams on the Arkansas and Fort Bent (place ours) (part)',basis='',loc='stated',at=(38.0, -100.5),r=200,src=TIPV4('doc. No. 46'),kind='primary',whole=False),
  # The 1862 Tonkawa massacre at their home 'on the U. S. Indian reservation, near old Fort Cobb, on Washita River I. T.'; no date or death toll given here (date Oct. 1862 from general knowledge, ours). Site placement ours.
 dict(g=['tkw'],y=1862.8,pop=None,raw='Shortly after the late civil war began and all troops were withdrawn from Fort Cobb, a portion of several of the Tribes living on the reservations, determined to make war upon the white people ... The Tonkawa refused to engage in it, and in consequence, the disaffected ones attacked, and after a day and nights fight, nearly exterminated them. (place ours)',basis='',loc='stated',at=(35.08, -98.3),r=25,src=TIPV4('doc. No. 80'),kind='primary'),
  # Lipan camp, Mar. 1866-Jan. 1867, as seen by a 13-year-old captive. '60 miles from the Sabinal' does not reach the Pecos: placement on the lower Pecos/Devils River area ours, wide radius. 'About Month January AD 1867, the
 dict(g=['lip'],y=1866.6,pop=150,raw='to their camp on Pecos River, about 60 miles from the Setlement on the Sabinal Creek, in Said Indian Camp (Lipan) was about fifty wariors, and about 150 all together men, woomen, and childreen (part)',basis="persons in one camp (captive's estimate)",loc='stated',at=(29.9, -101.2),r=100,src=TIPV4('doc. No. 150'),kind='primary',whole=False),
  # Hostile Comanche camps on the Arkansas, Sept. 1866 (hearsay via Robert Wolsey). Divisions and Kiowa inclusion ours.
 dict(g=['cyy', 'cyk', 'kio'],y=1866.74,pop=None,raw='the Comanche Cheif reached home for a visit to the camps of Those Indians who are now depredating upon us, they are camped some 3 or 4 hundred miles N.W. of Arbuckle on the Arkansas River (place ours) (part)',basis='',loc='stated',at=(37.8, -99.8),r=150,src=TIPV4('doc. No. 81'),kind='primary',whole=False),
  # Post-war location of the 'friendly Comanche' (former reserve Penateka) and Caddo, 1866. Doc. 81 (Sept. 1866): the hostile Comanche 'camped some 3 or 4 hundred miles N.W. of Arbuckle on the Arkansas River'.
 dict(g=['cyp'],y=1866.85,pop=None,raw='the Wichita Agency, near Fort Arbuckle, where the friendly Comanche and Caddo are located (part)',basis='',loc='stated',at=(34.5, -97.3),r=50,src=TIPV4('doc. No. 90'),kind='primary',whole=False),
  # Lipan camp in Coahuila, winter 1866-67; the 80-100 includes Mescalero and Gila. Morelos, Coahuila (families). Placement ours.
 dict(g=['lip'],y=1867.0,pop=360,raw='there are with the Lipan both Mescalero and Gila Indians ... betwen the different tribes they muster betwen 80 and 100 fighting men and boys ... There has come in to Moreles (about 4 miles from here) in the last few days some 8 or 10 families of Lipan with onely one man (place ours) (part)',basis='warriors × 4 (ours)',loc='stated',at=(28.4, -100.9),r=40,src=TIPV4('doc. No. 96 (enclosed letter)'),kind='primary',whole=False),
  # Lipan camp in Coahuila, Feb. 1867; doc. 123 (Mar. 1867) 'the Lipan had left their encampment above Piedras Negras'. Doc. 123 also: Lipan 'kept and maintained ... in the vicinity of Fort Inge, until ... In 1858 they left'
 dict(g=['lip'],y=1867.15,pop=None,raw='the Kickapoo and Lipan Tribes commit most all the stealing and murdering the former are encamped near Santa Rosa, and the latter near Monclova Viejo about 25 miles above Piedras Negras in Mexico (part)',basis='',loc='stated',at=(29.0, -100.75),r=25,src=TIPV4('doc. No. 116'),kind='primary',whole=False),
  # Tonkawa at Waco during their removal from Austin to Jacksboro, 25 Mar.-3 Apr. 1867. Table read from page image.
 dict(g=['tkw'],y=1867.24,pop=125,raw='Ration counts on the removal: 135 at Salado (March 6–8), 125 at Mastersville and Waco (March 12–April 3), 103 on the march from Waco to Jacksboro (April 5–17). To five beeves for the subsistence of the Tonkawa Indians ... purchased at Waco McLennan Co. Indians -------------- 125 Days 10',basis='ration count',loc='stated',at=(31.55, -97.15),r=15,src=TIPV4('doc. No. 130'),kind='primary'),
 dict(g=['tkw'],y=1867.18,pop=None,raw='To two beeves for the subsistence of the Tonkawa Indians bot at Salado Texas ... No of Indians 135, days 4 (March 6–8, 1867, on the removal from Austin to Jacksboro; the count is in the next record’s table)',basis='',loc='stated',at=(30.95,-97.54),r=15,src=TIPV4('doc. No. 130, table'),kind='primary'),
 dict(g=['tkw'],y=1867.28,pop=None,raw='for the subsistence of 103 Tonkawa Indians while “En rout” to Jacksboro Jack Co from Waco (vouchers of April 5–17, 1867, bought at Clifton, Fort Graham, Kimball, Acton and Weatherford)',basis='',loc='stated',at=(32.4,-97.75),r=60,src=TIPV4('doc. No. 130'),kind='primary'),
  # Tonkawa at Jacksboro from 18 Apr. 1867; beef furnished later at Belknap (doc. 163, Oct. 1867: 'approved by Col Starr then commanding at Belknap'). Doc. 158 (Aug. 1867): about 18 months earlier the tribe had camped on the
 dict(g=['tkw'],y=1867.3,pop=None,raw='the Tonkawa Indians were removed to the frontier, and turned over to the care of Maj. Starr, Commandant of the post at Jacksboro, on the 18th day of April 1867',basis='',loc='stated',at=(33.22, -98.16),r=10,src=TIPV4('doc. No. 144'),kind='primary'),
  # Nokoni chief Horse Back at Fort Arbuckle (a visit), May 1867.
 dict(g=['cyn'],y=1867.37,pop=None,raw='I have had an interview with To-ho-ye-qua-ih or Horse Back, of the Noconi band of Comanche (part)',basis='',loc='stated',at=(34.52, -97.25),r=30,src=TIPV4('doc. No. 140'),kind='primary',whole=False),
  # Lipan camp near Zaragoza, Coahuila, spring 1868 (month not given; 'the 25th of this month'); Kickapoo attack. Lipan leaders Gicare, Soli, Costalitas. A second Kickapoo attack killed 26 Lipan and Mescalero 'of both sexes'
 dict(g=['lip'],y=1868.4,pop=None,raw='the Lipan, the latter having been in their camp located on the North side of the River San Diego a distance of _____ leagues from this city ... they surprised the Lipan at sunset of the day mentioned, the Lipan lost five men, six women and two prisoners twenty five horses and three tents (part)',basis='',loc='stated',at=(28.55, -100.85),r=25,src=TIPV4('doc. No. 189'),kind='primary',whole=False),
  # Council at Fort Sill, Oct. 1873: Kiowa (Lone Wolf, Kicking Bird, Satanta, Big Tree), Apache (Pacer), Comanche (Horse-Back of the Nokoni, Ese-to-yeh, Quirts-quip 'Yamparika'), Waco (Buffalo Good). Agency issues: the Kiowa
 dict(g=['kio', 'kap', 'cyn', 'cyy', 'wic'],y=1873.77,pop=None,raw='Commissioner Smith—— My Friends, Chiefs and young men of the Comanche and Kiowa ... At Fort Sill (part)',basis='',loc='stated',at=(34.67, -98.4),r=10,src=TIPV4('doc. Nos. 224-226'),kind='primary',whole=False),
  # Kiowa hunting camp off the Fort Sill reservation, Jan. 1879, with a 10th Cavalry escort. Doc. 254 (15 Feb. 1879): 'there must be at least two thousand of these Indians now in Texas' (Fort Sill Indians on the Wichita and 
 dict(g=['kio'],y=1879.04,pop=38,raw="“Heap of Bear's” bands of Kiowa Indians to Pease River, Texas, to hunt.” I went into their camp and found about 18 warriors, and about 20 squaws and children ... This camp is about 10 miles below the fork of N & S Pease Rivers. (part)",basis="persons in one hunting camp (18 warriors + ~20 women and children); endorsement: 'a camp of 14 Lodges'",loc='stated',at=(34.05, -99.75),r=20,src=TIPV4('doc. No. 247'),kind='primary',whole=False),
]

# ---------------------------------------------------------------------------------------------
# Indian Office population tables, 1854–1899 (Annual Reports of the Commissioner of Indian Affairs), read from the page images of
# three compilations supplied by the project's owner. One count per division and report year: the same figure printed in two tables
# is taken once; the same people at different agencies are added (from 1873, when the tables name agencies). Not used: years already
# in the record, figures marked as carried forward or taken from the last report, residual lines ("Northern Sioux", "Other Sioux",
# absentees, children at school), divisions the tables count only in part (Rosebud by district, the Yanktonai, the Blackfeet agency
# after 1878, which held only the South Piegan; the Turtle Mountain full-bloods; the Lipan), and 45 figures less than half or more than
# twice the fit (most of them peoples partly in Canada or off the reservation, or misprints). The years are the report years.
OBS += [
 dict(g='iow',y=1854,pop=433,raw='Iowas 433',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1854, population table, p. 574 (read from the page images of the 1852–72 tables, pdf 7)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1854,pop=2379,raw='Medawakantoan and Wahpakootah 2,379',basis='souls',loc='inferred',at=(44.53, -94.97),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1854, population table, p. 574 (read from the page images of the 1852–72 tables, pdf 7)',kind='primary'),
 dict(g='oma',y=1854,pop=800,raw='Omahas 800',basis='souls',loc='inferred',at=(41.15, -96.07),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1854, population table, p. 574 (read from the page images of the 1852–72 tables, pdf 7)',kind='primary'),
 dict(g=['osg', 'osl'],y=1854,pop=4098,raw='Osages 4,098',basis='souls',loc='inferred',at=(37.4, -95.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1854, population table, p. 574 (read from the page images of the 1852–72 tables, pdf 7)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1854,pop=4004,raw='Sioux of Mississippi, viz: Seseetoan and Wahpaytoan band 4,004',basis='souls',loc='inferred',at=(45.05, -95.96),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1854, population table, p. 574 (read from the page images of the 1852–72 tables, pdf 7)',kind='primary'),
 dict(g=['arn', 'ars'],y=1855,pop=3000,raw='Arrapahoes 3,000',basis='souls',loc='inferred',at=(43.02, -105.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='ass',y=1855,pop=3360,raw='Assinaboines 3,360',basis='souls',loc='inferred',at=(48.27, -104.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g=['chn', 'chs'],y=1855,pop=2800,raw='Cheyennes 2,800',basis='souls',loc='inferred',at=(42.75, -104.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='iow',y=1855,pop=433,raw='Iowas 433',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='kap',y=1855,pop=320,raw='Apaches 320',basis='souls',loc='inferred',at=(38.22, -100.39),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='kaw',y=1855,pop=1375,raw='Kansas 1,375',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='kio',y=1855,pop=2800,raw='Kioways 2,800',basis='souls',loc='inferred',at=(37.46, -100.03),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='man',y=1855,pop=250,raw='Mandans 250',basis='souls',loc='inferred',at=(47.3, -101.35),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 575 (read from the page images of the 1852–72 tables, pdf 8)',kind='primary'),
 dict(g='pon',y=1855,pop=700,raw='Poncas 700',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 576 (read from the page images of the 1852–72 tables, pdf 9)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1855,pop=4000,raw='Pawnees 4,000',basis='souls',loc='inferred',at=(41.33, -96.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 576 (read from the page images of the 1852–72 tables, pdf 9)',kind='primary'),
 dict(g='tkw',y=1855,pop=400,raw='Tonkawas 400',basis='souls',loc='inferred',at=(33.1, -98.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 576 (read from the page images of the 1852–72 tables, pdf 9)',kind='primary'),
 dict(g='wic',y=1855,pop=950,raw='Wichitas 950',basis='souls',loc='inferred',at=(34.79, -97.97),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1855, population table, p. 576 (read from the page images of the 1852–72 tables, pdf 9)',kind='primary'),
 dict(g='ari',y=1861,pop=980,raw='Arickarees 980 (Upper Missouri agency)',basis='souls',loc='inferred',at=(47.25, -101.27),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='ass',y=1861,pop=2880,raw='Assinaboines 2,880 (Upper Missouri agency)',basis='souls',loc='inferred',at=(48.24, -104.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1861,pop=3900,raw='Crows 3,900 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.15, -108.94),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='gv',y=1861,pop=2100,raw='Gros Ventres 2,100 (Blackfeet agency)',basis='souls',loc='inferred',at=(48.01, -109.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='hid',y=1861,pop=800,raw='Gros Ventres 800 (Upper Missouri agency)',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='hnk',y=1861,pop=2680,raw='Uncpapas 2,680 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.58, -102.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='jic',y=1861,pop=800,raw='Icearilla Apaches 800 (Utah agency)',basis='souls',loc='inferred',at=(36.33, -105.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 827 (read from the page images of the 1852–72 tables, pdf 16)',kind='primary'),
 dict(g='kai',y=1861,pop=2400,raw='Bloods 2,400 (Blackfeet agency)',basis='souls',loc='inferred',at=(49.2, -112.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='kaw',y=1861,pop=803,raw='Kansas 803 (Kansas agency)',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 825 (read from the page images of the 1852–72 tables, pdf 14)',kind='primary'),
 dict(g='min',y=1861,pop=1280,raw='Minneconjoux 1,280 (Upper Missouri agency)',basis='souls',loc='inferred',at=(43.89, -104.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='oma',y=1861,pop=950,raw='Omahas 950 (Omaha agency)',basis='souls',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 824 (read from the page images of the 1852–72 tables, pdf 13)',kind='primary'),
 dict(g='oto',y=1861,pop=708,raw='Ottoes and Missourias 708 (Ottoe and Missouri agency)',basis='souls',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 824 (read from the page images of the 1852–72 tables, pdf 13)',kind='primary'),
 dict(g='pik',y=1861,pop=3700,raw='Piegans 3,700 (Blackfeet agency)',basis='souls',loc='inferred',at=(48.16, -111.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='pon',y=1861,pop=973,raw='Poncas 973 (Ponca agency (special))',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 824 (read from the page images of the 1852–72 tables, pdf 13)',kind='primary'),
 dict(g='pwc',y=1861,pop=1464,raw='Grands, or Chowees 903 (Pawnee agency (special)); Tappas, or Tapahowerats 561 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='pwk',y=1861,pop=784,raw='Republicans, or Kattahawkees 784 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='pws',y=1861,pop=1166,raw='Loups, or Skeedees 1,166 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='sih',y=1861,pop=1248,raw='Blackfeet Sioux 1,248 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.54, -102.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='twk',y=1861,pop=960,raw='Two Kettles 960 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.47, -100.52),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1861, population table, p. 823 (read from the page images of the 1852–72 tables, pdf 12)',kind='primary'),
 dict(g='ari',y=1862,pop=1080,raw='Arickarees 1,080 (Upper Missouri agency)',basis='souls',loc='inferred',at=(47.25, -101.27),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='ars',y=1862,pop=1500,raw='Arapahoes 1,500 (Upper Arkansas agency)',basis='souls',loc='inferred',at=(38.36, -101.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='ass',y=1862,pop=3280,raw='Assinaboines 3,280 (Upper Missouri agency)',basis='souls',loc='inferred',at=(48.23, -104.76),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='chs',y=1862,pop=1600,raw='Cheyennes 1,600 (Upper Arkansas agency)',basis='souls',loc='inferred',at=(37.73, -99.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1862,pop=3900,raw='Crows 3,900 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.29, -108.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='hnk',y=1862,pop=2680,raw='Uncpapas 2,680 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.78, -102.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='iow',y=1862,pop=298,raw='Iowas 298 (Great Nemaha agency) (a digit uncertain in the print)',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 356 (read from the page images of the 1852–72 tables, pdf 24)',kind='primary'),
 dict(g='jic',y=1862,pop=960,raw='Jicarilla Apaches 960 (Utah agency (New Mexico))',basis='souls',loc='inferred',at=(36.36, -105.64),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 358 (read from the page images of the 1852–72 tables, pdf 26)',kind='primary'),
 dict(g='kap',y=1862,pop=500,raw='Apaches 500 (Upper Arkansas agency)',basis='souls',loc='inferred',at=(37.76, -99.27),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='kio',y=1862,pop=1800,raw='Kioways 1,800 (Upper Arkansas agency)',basis='souls',loc='inferred',at=(37.67, -99.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='min',y=1862,pop=1280,raw='Minneconjoux 1,280 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.04, -105.03),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='oma',y=1862,pop=953,raw='Omahas 953 (Omaha agency)',basis='souls',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 356 (read from the page images of the 1852–72 tables, pdf 24)',kind='primary'),
 dict(g='pwc',y=1862,pop=1464,raw='Grands 903 (Pawnee agency (special)); Tappas 561 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 356 (read from the page images of the 1852–72 tables, pdf 24)',kind='primary'),
 dict(g='pwk',y=1862,pop=784,raw='Republicans 784 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 356 (read from the page images of the 1852–72 tables, pdf 24)',kind='primary'),
 dict(g='pws',y=1862,pop=1166,raw='Loups 1,166 (Pawnee agency (special))',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 356 (read from the page images of the 1852–72 tables, pdf 24)',kind='primary'),
 dict(g='sih',y=1862,pop=2080,raw='Blackfoot Sioux 2,080 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.73, -102.69),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1862,pop=2811,raw='Upper Sioux 2,811 (Agency for the Sioux of Minnesota (No. 74 table))',basis='souls',loc='inferred',at=(44.89, -95.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 354 (read from the page images of the 1852–72 tables, pdf 22)',kind='primary'),
 dict(g='twk',y=1862,pop=960,raw='Two Kettles 960 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.48, -100.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='ynk',y=1862,pop=2104,raw='Yancton Sioux 2,104 (Yancton Sioux agency)',basis='souls',loc='inferred',at=(42.98, -98.55),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1862, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 23)',kind='primary'),
 dict(g='ari',y=1863,pop=1080,raw='Aricarees 1,080 (Upper Missouri agency)',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g='arn',y=1863,pop=720,raw='Arapahoes 720 (Upper Platte agency)',basis='souls',loc='inferred',at=(44.62, -106.83),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g='ass',y=1863,pop=3280,raw='Assinaboines 3,280 (Upper Missouri agency)',basis='souls',loc='inferred',at=(48.21, -104.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g='chn',y=1863,pop=1800,raw='Cheyennes 1,800 (Upper Platte agency)',basis='souls',loc='inferred',at=(44.15, -105.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g='hnk',y=1863,pop=2680,raw='Uncpapas 2,680 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.98, -103.06),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 502 (read from the page images of the 1852–72 tables, pdf 37)',kind='primary'),
 dict(g='iow',y=1863,pop=291,raw='Ioways 291 (Great Nemaha agency)',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 506 (read from the page images of the 1852–72 tables, pdf 41)',kind='primary'),
 dict(g='kaw',y=1863,pop=741,raw='Kansas 741 (Kansas agency)',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 507 (read from the page images of the 1852–72 tables, pdf 42)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1863,pop=1598,raw="Total full Indians 1,489 (Census of the Indian camp - Recapitulation); Eagle Head's band 109 (Census of the Indian camp - Recapitulation)",basis='souls',loc='inferred',at=(44.7, -95.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 316 (read from the page images of the 1852–72 tables, pdf 32)',kind='primary'),
 dict(g='oto',y=1863,pop=470,raw='Ottoes and Missourias 470 (Ottoe and Missouria agency)',basis='souls',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g='pon',y=1863,pop=864,raw='Poncas 864 (Ponca agency (special))',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 506 (read from the page images of the 1852–72 tables, pdf 41)',kind='primary'),
 dict(g='sih',y=1863,pop=2080,raw='Blackfoot Sioux 2,080 (Upper Missouri agency)',basis='souls',loc='inferred',at=(46.91, -102.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 502 (read from the page images of the 1852–72 tables, pdf 37)',kind='primary'),
 dict(g='twk',y=1863,pop=960,raw='Two Kettles 960 (Upper Missouri agency)',basis='souls',loc='inferred',at=(44.5, -100.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1863, population table, p. 503 (read from the page images of the 1852–72 tables, pdf 38)',kind='primary'),
 dict(g=['ars', 'chs'],y=1864,pop=3100,raw='Arapahoes and Cheyennes 3,100 (Colorado - Upper Arkansas)',basis='souls',loc='inferred',at=(38.53, -102.23),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='ass',y=1864,pop=3280,raw='Assinaboines 3,280 (Dakota - Upper Missouri (component))',basis='souls',loc='inferred',at=(48.2, -104.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1864,pop=3500,raw='Crows 3,500 (Dakota - Upper Missouri (component))',basis='souls',loc='inferred',at=(44.57, -108.96),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1864,pop=1800,raw='Comanches 1,800 (Central - Kiowas and Apaches (component))',basis='souls',loc='inferred',at=(36.5, -100.89),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='gv',y=1864,pop=1800,raw='Gros-Ventres 1,800 (Montana - Blackfeet (component))',basis='souls',loc='inferred',at=(48.18, -108.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='iow',y=1864,pop=294,raw='Sacs and Foxes, 95; and Iowas, 294 294 (Northern - Sac and Foxes of Missouri)',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='kai',y=1864,pop=2150,raw='Bloods 2,150 (Montana - Blackfeet (component))',basis='souls',loc='inferred',at=(49.36, -112.62),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='kap',y=1864,pop=500,raw='Apaches 500 (Central - Kiowas and Apaches (component))',basis='souls',loc='inferred',at=(37.75, -98.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='kaw',y=1864,pop=631,raw='Kansas, (or Kaws) 631 (Central - Kansas)',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='kio',y=1864,pop=1800,raw='Kiowas 1,800 (Central - Kiowas and Apaches (component))',basis='souls',loc='inferred',at=(36.59, -98.93),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1864,pop=1043,raw='Sioux of the Mississippi 1,043 (Dakota - Crow Creek)',basis='souls',loc='inferred',at=(44.34, -95.91),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='min',y=1864,pop=2220,raw='Minneconjoux 2,220 (Dakota - Upper Missouri Sioux (component))',basis='souls',loc='inferred',at=(44.35, -105.62),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='oma',y=1864,pop=1000,raw='Omahas 1,000 (Northern - Omaha)',basis='souls',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='oto',y=1864,pop=708,raw='Ottoes and Missourias 708 (Northern - Ottoe and Missouria)',basis='souls',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='pik',y=1864,pop=1870,raw='Piegans 1,870 (Montana - Blackfeet (component))',basis='souls',loc='inferred',at=(48.31, -111.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='pon',y=1864,pop=1100,raw='Poncas 1,100 (Dakota - Poncas)',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1864,pop=2800,raw='Pawnees 2,800 (Northern - Pawnee)',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 590 (read from the page images of the 1852–72 tables, pdf 57)',kind='primary'),
 dict(g='sik',y=1864,pop=2450,raw='Blackfeet 2,450 (Montana - Blackfeet (component))',basis='souls',loc='inferred',at=(50.9, -112.47),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='twk',y=1864,pop=780,raw='Two Kettles 780 (Dakota - Upper Missouri Sioux (component))',basis='souls',loc='inferred',at=(44.51, -100.59),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='ynk',y=1864,pop=2530,raw='Yancton Sioux 2,530 (Dakota - Yancton)',basis='souls',loc='inferred',at=(42.98, -98.51),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1864, population table, p. 589 (read from the page images of the 1852–72 tables, pdf 56)',kind='primary'),
 dict(g='arn',y=1866,pop=750,raw='Arapahoes 750',basis='souls',loc='inferred',at=(44.81, -107.22),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='ass',y=1866,pop=2640,raw='Assinaboines 2,640',basis='souls',loc='inferred',at=(48.17, -104.94),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='chn',y=1866,pop=1800,raw='Cheyennes 1,800',basis='souls',loc='inferred',at=(44.45, -106.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1866,pop=3900,raw='Crows 3,900',basis='souls',loc='inferred',at=(44.95, -109.37),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='gv',y=1866,pop=1500,raw='Gros Ventres 1,500',basis='souls',loc='inferred',at=(48.29, -108.68),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='hid',y=1866,pop=400,raw='Gros Ventres 400',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='hnk',y=1866,pop=3600,raw='Uncpapas 1,800; Oncpapas 1,800',basis='souls',loc='inferred',at=(46.6, -104.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 347, p. 371 (read from the page images of the 1852–72 tables, pdf 61, 75)',kind='primary'),
 dict(g='iow',y=1866,pop=303,raw='Iowas 303',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='kai',y=1866,pop=4300,raw='Bloods 2,150; Bloods* 2,150',basis='souls',loc='inferred',at=(49.46, -112.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 348, p. 371 (read from the page images of the 1852–72 tables, pdf 62, 75)',kind='primary'),
 dict(g='kaw',y=1866,pop=670,raw='Kansas or Kaws 670',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='kit',y=1866,pop=144,raw='Keechies 144',basis='souls',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 372 (read from the page images of the 1852–72 tables, pdf 76)',kind='primary'),
 dict(g='man',y=1866,pop=400,raw='Mandans 400',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1866,pop=1350,raw='Santee Sioux 1,350',basis='souls',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='ogl',y=1866,pop=2100,raw='Ogalallahs 2,100',basis='souls',loc='inferred',at=(44.18, -105.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='oma',y=1866,pop=1994,raw='Omahas 997; Omahas† 997',basis='souls',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 346, p. 371 (read from the page images of the 1852–72 tables, pdf 60, 75)',kind='primary'),
 dict(g='pik',y=1866,pop=3740,raw='Piegans 1,870; Piegans* 1,870',basis='souls',loc='inferred',at=(48.5, -111.28),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 348, p. 371 (read from the page images of the 1852–72 tables, pdf 62, 75)',kind='primary'),
 dict(g='pon',y=1866,pop=980,raw='Poncas 980',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1866,pop=2750,raw='Pawnees 2,750',basis='souls',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 371 (read from the page images of the 1852–72 tables, pdf 75)',kind='primary'),
 dict(g='sik',y=1866,pop=4900,raw='Blackfeet 2,450; Blackfeet* 2,450',basis='souls',loc='inferred',at=(50.88, -112.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 348, p. 371 (read from the page images of the 1852–72 tables, pdf 62, 75)',kind='primary'),
 dict(g='wic',y=1866,pop=678,raw='Wichitas 392; Wacoes 135; Tawacairoes 151',basis='souls',loc='inferred',at=(37.69, -97.34),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1866, population table, p. 372 (read from the page images of the 1852–72 tables, pdf 76)',kind='primary'),
 dict(g='ari',y=1867,pop=1500,raw='Arickarees 1,500',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='arn',y=1867,pop=750,raw='Arapahoes 750',basis='souls',loc='inferred',at=(44.84, -107.32),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='ass',y=1867,pop=2640,raw='Assinaboines 2,640',basis='souls',loc='inferred',at=(48.16, -104.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='chn',y=1867,pop=1800,raw='Cheyennes 1,800',basis='souls',loc='inferred',at=(44.69, -106.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1867,pop=3900,raw='Crows 3,900',basis='souls',loc='inferred',at=(45.16, -109.65),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='gv',y=1867,pop=1500,raw='Gros Ventres 1,500',basis='souls',loc='inferred',at=(48.34, -108.59),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='hid',y=1867,pop=400,raw='Gros Ventres 400',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='hnk',y=1867,pop=3000,raw='Uncpapas 3,000',basis='souls',loc='inferred',at=(46.58, -104.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='iow',y=1867,pop=254,raw='Iowas 254',basis='souls',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='jic',y=1867,pop=1045,raw='Jicarilla Apaches 1,045',basis='souls',loc='inferred',at=(36.47, -105.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 395 (read from the page images of the 1852–72 tables, pdf 79)',kind='primary'),
 dict(g='kai',y=1867,pop=2150,raw='Bloods 2,150',basis='souls',loc='inferred',at=(49.52, -112.37),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='kaw',y=1867,pop=658,raw='Kansas or Kaws 658',basis='souls',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='kit',y=1867,pop=127,raw='Keechies 127',basis='souls',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 397 (read from the page images of the 1852–72 tables, pdf 81)',kind='primary'),
 dict(g='man',y=1867,pop=400,raw='Mandans 400',basis='souls',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='min',y=1867,pop=3000,raw='Minneconjoux 3,000',basis='souls',loc='inferred',at=(44.81, -106.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='ogl',y=1867,pop=3000,raw='Ogallallas 3,000',basis='souls',loc='inferred',at=(44.39, -106.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='oma',y=1867,pop=995,raw='Omahas 995',basis='souls',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g=['osg', 'osl'],y=1867,pop=2412,raw='Osages 2,412',basis='souls',loc='inferred',at=(37.4, -95.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='pik',y=1867,pop=1890,raw='Piegans 1,890',basis='souls',loc='inferred',at=(48.62, -111.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='pon',y=1867,pop=980,raw='Poncas 980',basis='souls',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='sih',y=1867,pop=1200,raw='Blackfeet 1,200',basis='souls',loc='inferred',at=(46.94, -102.22),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='sik',y=1867,pop=2450,raw='Blackfeet 2,450',basis='souls',loc='inferred',at=(50.87, -112.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='sna',y=1867,pop=750,raw='Sans Arcs 750',basis='souls',loc='inferred',at=(44.94, -101.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='twk',y=1867,pop=750,raw='Two Kettles 750',basis='souls',loc='inferred',at=(44.56, -100.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='wic',y=1867,pop=631,raw='Wichitas 364; Wacoes 124; Tawaccaras 143',basis='souls',loc='inferred',at=(37.69, -97.34),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 397 (read from the page images of the 1852–72 tables, pdf 81)',kind='primary'),
 dict(g='ynk',y=1867,pop=2500,raw='Yancton Sioux 2,500',basis='souls',loc='inferred',at=(42.98, -98.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1867, population table, p. 396 (read from the page images of the 1852–72 tables, pdf 80)',kind='primary'),
 dict(g='ari',y=1868,pop=1500,raw='Arickarees 1,500',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='arn',y=1868,pop=750,raw='Arapahoes 750',basis='census',loc='inferred',at=(46.65, -107.86),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g=['ars', 'chs'],y=1868,pop=2800,raw='Arapahoes † 2,800',basis='census',loc='inferred',at=(37.05, -98.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 355 (read from the page images of the 1852–72 tables, pdf 87)',kind='primary'),
 dict(g='ass',y=1868,pop=2640,raw='Assinaboines 2,640',basis='census',loc='inferred',at=(48.15, -105.04),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='chn',y=1868,pop=1800,raw='Cheyennes 1,800',basis='census',loc='inferred',at=(44.78, -106.97),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='cwm',y=1868,pop=2500,raw='Mountain Crows 2,500',basis='census',loc='inferred',at=(45.37, -109.94),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='cwr',y=1868,pop=2500,raw='River Crows 2,500',basis='census',loc='inferred',at=(48.01, -108.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='gv',y=1868,pop=3000,raw='Gros Ventres 3,000',basis='census',loc='inferred',at=(48.4, -108.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='hid',y=1868,pop=400,raw='Gros Ventres 400',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='iow',y=1868,pop=246,raw='Iowas 246',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='jic',y=1868,pop=878,raw='Jicarilla Apaches 878',basis='census',loc='inferred',at=(36.5, -104.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='kai',y=1868,pop=2380,raw='Bloods 2,380',basis='census',loc='inferred',at=(49.57, -112.28),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='kit',y=1868,pop=123,raw='Keechies 123',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='man',y=1868,pop=400,raw='Mandans 400',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='ogl',y=1868,pop=3000,raw='Ogallallas 3,000',basis='census',loc='inferred',at=(43.91, -106.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='oma',y=1868,pop=1002,raw='Omahas 1,002',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g=['osg', 'osl'],y=1868,pop=3490,raw='Osages 3,490',basis='census',loc='inferred',at=(37.4, -95.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='oto',y=1868,pop=471,raw='Ottoes and Missourias 471',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='pik',y=1868,pop=4200,raw='Piegans 4,200',basis='census',loc='inferred',at=(48.74, -111.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g='pon',y=1868,pop=979,raw='Poncas 979',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1868,pop=2831,raw='Pawnees 2,831',basis='census',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 353 (read from the page images of the 1852–72 tables, pdf 85)',kind='primary'),
 dict(g='sik',y=1868,pop=2980,raw='Blackfeet 2,980',basis='census',loc='inferred',at=(50.85, -112.61),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g=['wpt', 'sis'],y=1868,pop=1637,raw='Wahpeton Sioux, &c 1,637',basis='census',loc='inferred',at=(45.6, -97.08),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1868, population table, p. 352 (read from the page images of the 1852–72 tables, pdf 84)',kind='primary'),
 dict(g=['ars', 'chs'],y=1869,pop=3390,raw='Arapahoes and Cheyennes, (3,390) 3,390',basis='census',loc='inferred',at=(35.99, -99.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g='chs',y=1869,pop=1950,raw='Cheyennes, (supposed) 1,950',basis='census',loc='inferred',at=(35.87, -99.26),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 462 (read from the page images of the 1852–72 tables, pdf 93)',kind='primary'),
 dict(g='cwm',y=1869,pop=2000,raw='Mountain Crows 2,000',basis='census',loc='inferred',at=(45.58, -110.23),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1869,pop=2538,raw='Comanches 2,538',basis='census',loc='inferred',at=(36.89, -98.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 462 (read from the page images of the 1852–72 tables, pdf 93)',kind='primary'),
 dict(g='iow',y=1869,pop=546,raw='Iowas and Sacs and Foxes of Missouri 318; Iowas 228',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461, p. 462 (read from the page images of the 1852–72 tables, pdf 92, 93)',kind='primary'),
 dict(g='jic',y=1869,pop=788,raw='Jicarilla Apaches 788',basis='census',loc='inferred',at=(36.51, -104.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 463 (read from the page images of the 1852–72 tables, pdf 94)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1869,pop=970,raw='Santee Sioux 970',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g='oma',y=1869,pop=1020,raw='Omahas 1,020',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g=['osg', 'osl'],y=1869,pop=4481,raw='Osages 4,481',basis='census',loc='inferred',at=(37.4, -95.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 463 (read from the page images of the 1852–72 tables, pdf 94)',kind='primary'),
 dict(g='oto',y=1869,pop=440,raw='Ottoes and Missourias 440',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g='pon',y=1869,pop=768,raw='Poncas 768',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1869,pop=2398,raw='Pawnees 2,398',basis='census',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g='sho',y=1869,pop=1600,raw='Eastern Shoshones 1,600',basis='census',loc='inferred',at=(41.42, -110.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 460 (read from the page images of the 1852–72 tables, pdf 91)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1869,pop=1800,raw='Sisseton and Wahpeton Sioux 1,800',basis='census',loc='inferred',at=(45.61, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g='ynk',y=1869,pop=2500,raw='Yankton Sioux 2,500',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1869, population table, p. 461 (read from the page images of the 1852–72 tables, pdf 92)',kind='primary'),
 dict(g=['ars', 'chs'],y=1870,pop=3390,raw='Upper Arkansas agency 3,390',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g='cwm',y=1870,pop=2330,raw='Crow agency 2,330',basis='census',loc='inferred',at=(45.4, -110.06),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g='iow',y=1870,pop=294,raw='Great Nemaha agency 294',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g='jic',y=1870,pop=900,raw='Cimarron agency 900',basis='census',loc='inferred',at=(36.51, -104.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 332 (read from the page images of the 1852–72 tables, pdf 97)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1870,pop=967,raw='Santee Sioux agency 967',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 334 (read from the page images of the 1852–72 tables, pdf 99)',kind='primary'),
 dict(g='oma',y=1870,pop=984,raw='Omaha agency 984',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g=['osg', 'osl'],y=1870,pop=5352,raw='Neosho agency 5,352',basis='census',loc='inferred',at=(37.4, -95.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g='oto',y=1870,pop=434,raw='Otoe and Missouria agency 434',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 334 (read from the page images of the 1852–72 tables, pdf 99)',kind='primary'),
 dict(g='pon',y=1870,pop=747,raw='Ponca agency 747',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 332 (read from the page images of the 1852–72 tables, pdf 97)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1870,pop=2398,raw='Pawnee agency ‡ 2,398',basis='census',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 334 (read from the page images of the 1852–72 tables, pdf 99)',kind='primary'),
 dict(g='wic',y=1870,pop=1016,raw='Wichita agency 1,016',basis='census',loc='inferred',at=(35.1, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 333 (read from the page images of the 1852–72 tables, pdf 98)',kind='primary'),
 dict(g='ynk',y=1870,pop=1886,raw='Yancton agency 1,886',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1870, population table, p. 332 (read from the page images of the 1852–72 tables, pdf 97)',kind='primary'),
 dict(g=['ars', 'chs'],y=1871,pop=3390,raw='Arapahoes and Cheyennes 3,390',basis='census',loc='inferred',at=(35.59, -98.09),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 613 (read from the page images of the 1852–72 tables, pdf 110)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1871,pop=3218,raw='Comanches 3,218',basis='census',loc='inferred',at=(36.23, -98.94),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 612 (read from the page images of the 1852–72 tables, pdf 109)',kind='primary'),
 dict(g='hid',y=1871,pop=600,raw='Gros Ventres 600',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 616 (read from the page images of the 1852–72 tables, pdf 113)',kind='primary'),
 dict(g='hnk',y=1871,pop=1700,raw='Oncpapa Sioux 1,700',basis='census',loc='inferred',at=(46.43, -104.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 616 (read from the page images of the 1852–72 tables, pdf 113)',kind='primary'),
 dict(g='kaw',y=1871,pop=627,raw='Kansas or Kaw Indians 627',basis='census',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 612 (read from the page images of the 1852–72 tables, pdf 109)',kind='primary'),
 dict(g='ogl',y=1871,pop=6000,raw='Ogallalla Sioux 6,000',basis='census',loc='inferred',at=(42.44, -104.64),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 617 (read from the page images of the 1852–72 tables, pdf 114)',kind='primary'),
 dict(g=['osg', 'osl'],y=1871,pop=3375,raw='Osages 3,375',basis='census',loc='inferred',at=(37.4, -95.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 612 (read from the page images of the 1852–72 tables, pdf 109)',kind='primary'),
 dict(g='sih',y=1871,pop=1150,raw='Blackfeet Sioux 1,150',basis='census',loc='inferred',at=(46.5, -101.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 616 (read from the page images of the 1852–72 tables, pdf 113)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1871,pop=1426,raw='Sisseton and Wahpeton Sioux 1,426',basis='census',loc='inferred',at=(45.61, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 617 (read from the page images of the 1852–72 tables, pdf 114)',kind='primary'),
 dict(g='sna',y=1871,pop=1100,raw='Sans Arc Sioux 1,100',basis='census',loc='inferred',at=(44.76, -101.09),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 616 (read from the page images of the 1852–72 tables, pdf 113)',kind='primary'),
 dict(g='ynk',y=1871,pop=1947,raw='Yankton Sioux 1,947',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1871, population table, p. 615 (read from the page images of the 1852–72 tables, pdf 112)',kind='primary'),
 dict(g='ari',y=1873,pop=1096,raw='Arickarees 1,096 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='ars',y=1873,pop=1650,raw='Arapahoes 1,650 (Upper Arkansas agency)',basis='census',loc='inferred',at=(35.58, -98.07),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 5)',kind='primary'),
 dict(g='chs',y=1873,pop=2200,raw='Cheyennes 2,200 (Upper Arkansas agency)',basis='census',loc='inferred',at=(35.27, -100.78),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 5)',kind='primary'),
 dict(g='cwm',y=1873,pop=3000,raw='Mountain Crows 3,000 (Crow agency)',basis='census',loc='inferred',at=(45.17, -109.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='cwr',y=1873,pop=2440,raw='River Crows 1,200 (Crow agency); River Crows 1,240 (Fort Belknap special agency. (a))',basis='census',loc='inferred',at=(47.04, -109.32),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338, p. 340 (read from the page images of the 1873–83 tables, pdf 7, 9)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1873,pop=2543,raw='Penetethka Comanches 345 (Wichita agency); Comanches 2,198 (Kiowa agency)',basis='census',loc='inferred',at=(35.58, -99.17),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='gv',y=1873,pop=1100,raw='Gros Ventres 1,100 (Fort Belknap special agency. (a))',basis='census',loc='inferred',at=(48.45, -108.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 340 (read from the page images of the 1873–83 tables, pdf 9)',kind='primary'),
 dict(g='hid',y=1873,pop=528,raw='Gros Ventres 528 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='hnk',y=1873,pop=1502,raw='Uncpapa Sioux 1,502 (Grand River agency)',basis='census',loc='inferred',at=(46.25, -102.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 5)',kind='primary'),
 dict(g='iow',y=1873,pop=221,raw='Iowas 221 (Great Nemaha agency)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='jic',y=1873,pop=960,raw='Jicarilla Apaches 400 (Abiquin or Tierra Amarilla agency); Jicarilla Apaches 560 (Cimarron agency)',basis='census',loc='inferred',at=(36.51, -104.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 342 (read from the page images of the 1873–83 tables, pdf 11)',kind='primary'),
 dict(g='kai',y=1873,pop=1750,raw='Bloods 1,750 (Blackfeet agency)',basis='census',loc='inferred',at=(50.03, -112.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='kaw',y=1873,pop=533,raw='Kaws 533 (Kaw agency)',basis='census',loc='inferred',at=(38.66, -96.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='kio',y=1873,pop=2000,raw='Kiowas 2,000 (Kiowa agency)',basis='census',loc='inferred',at=(35.08, -99.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='kit',y=1873,pop=106,raw='Keechies 106 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='man',y=1873,pop=479,raw='Mandans 479 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1873,pop=1017,raw='Santee Sioux 917 (Santee Sioux agency); Santee Sioux (b) 100 (Flandrau special agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 332, p. 338 (read from the page images of the 1873–83 tables, pdf 1, 7)',kind='primary'),
 dict(g='ogl',y=1873,pop=6320,raw='Ogallalla Sioux 6,320 (Red Cloud agency. (c))',basis='census',loc='inferred',at=(42.54, -103.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='oma',y=1873,pop=1001,raw='Omahas 1,001 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g=['osg', 'osl'],y=1873,pop=2823,raw='Great and Little Osages 2,823 (Neosho agency)',basis='census',loc='inferred',at=(36.68, -96.35),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='oto',y=1873,pop=447,raw='Otoes and Missourias 447 (Otoe ageny)',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='pik',y=1873,pop=2750,raw='Piegans 2,750 (Blackfeet agency)',basis='census',loc='inferred',at=(49.27, -112.19),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='pon',y=1873,pop=738,raw='Poncas 738 (Ponca agency)',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1873,pop=2376,raw='Pawnees 2,376 (Pawnee agency)',basis='census',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='sho',y=1873,pop=1024,raw='Eastern Band of Shoshones 1,024 (Shoshone agency)',basis='census',loc='inferred',at=(42.68, -109.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='sih',y=1873,pop=847,raw='Blackfeet Sioux 847 (Grand River agency)',basis='census',loc='inferred',at=(46.28, -100.98),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 5)',kind='primary'),
 dict(g='sik',y=1873,pop=3000,raw='Blackfeet 3,000 (Blackfeet agency)',basis='census',loc='inferred',at=(50.79, -112.78),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1873,pop=1540,raw='Sisseton and Wahpeton Sioux 1,540 (Sisseton Sioux agency)',basis='census',loc='inferred',at=(45.61, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 5)',kind='primary'),
 dict(g='wic',y=1873,pop=565,raw='Wichitas 300 (Wichita agency); Wacoes 140 (Wichita agency); Tawacanies 125 (Wichita agency)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 3)',kind='primary'),
 dict(g='ynk',y=1873,pop=1947,raw='Yankton Sioux (a) 1,947 (Yankton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1873, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 7)',kind='primary'),
 dict(g='ari',y=1874,pop=975,raw='Arickarees 975 (Fort Berthold ageney)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='chn',y=1874,pop=1202,raw='Northern Cheyennes 1,202 (Red-Cloud agency)',basis='census',loc='inferred',at=(45.32, -107.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='chs',y=1874,pop=2250,raw='Cheyennes 2,250 (Upper Arkansas agency)',basis='census',loc='inferred',at=(35.11, -101.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1874,pop=2988,raw='Penetethka Comanches 345 (Wichita agency); Comanches 2,643 (Kiowa agency)',basis='census',loc='inferred',at=(35.25, -99.28),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g='gv',y=1874,pop=1000,raw='Gros Ventres 1,000 (Fort Belknap special agency)',basis='census',loc='inferred',at=(48.47, -108.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 104 (read from the page images of the 1873–83 tables, pdf 28)',kind='primary'),
 dict(g='hid',y=1874,pop=620,raw='Gros Ventres 620 (Fort Berthold ageney)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='hnk',y=1874,pop=2976,raw='Oncpapa Sioux 1,556 (Grand River agency); Oncpapa Sioux 1,420 (Milk River agency)',basis='census',loc='inferred',at=(46.15, -101.37),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102, p. 104 (read from the page images of the 1873–83 tables, pdf 26, 28)',kind='primary'),
 dict(g='iow',y=1874,pop=226,raw='Iowas 226 (Great Nemaha agency)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 98 (read from the page images of the 1873–83 tables, pdf 22)',kind='primary'),
 dict(g='jic',y=1874,pop=960,raw='Jicarilla Apaches 500 (Abiquiu or Tierra Amarilla agency); Jicarilla Apaches 460 (Cimarron agency)',basis='census',loc='inferred',at=(36.51, -104.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 32)',kind='primary'),
 dict(g='kai',y=1874,pop=1500,raw='Bloods 1,500 (Blackfeet agency)',basis='census',loc='inferred',at=(50.18, -112.46),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 104 (read from the page images of the 1873–83 tables, pdf 28)',kind='primary'),
 dict(g='kaw',y=1874,pop=523,raw='Kaws 523 (Osage agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g='kit',y=1874,pop=106,raw='Keechies 106 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g='man',y=1874,pop=420,raw='Mandans 420 (Fort Berthold ageney)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1874,pop=1103,raw='Santee Sioux 791 (Santee Sioux agency); Santee Sioux 312 (Flandreau special agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102, p. 98 (read from the page images of the 1873–83 tables, pdf 22, 26)',kind='primary'),
 dict(g='min',y=1874,pop=1655,raw='Minneconjou Sioux 1,655 (Cheyenne River agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='oma',y=1874,pop=951,raw='Omahas 951 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 98 (read from the page images of the 1873–83 tables, pdf 22)',kind='primary'),
 dict(g='oto',y=1874,pop=453,raw='Otoes and Missourias 453 (Otoe agency)',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g='pik',y=1874,pop=2450,raw='Piegans 2,450 (Blackfeet agency)',basis='census',loc='inferred',at=(49.15, -112.23),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 104 (read from the page images of the 1873–83 tables, pdf 28)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1874,pop=2148,raw='Pawnees 1,788 (Pawnee agency); Pawnees 360 (Wichita agency)',basis='census',loc='inferred',at=(41.45, -97.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100, p. 98 (read from the page images of the 1873–83 tables, pdf 22, 24)',kind='primary'),
 dict(g='sih',y=1874,pop=1571,raw='Blackfeet Sioux 871 (Grand River agency); Blackfeet Sioux 700 (Cheyenne River agency)',basis='census',loc='inferred',at=(46.17, -100.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='sik',y=1874,pop=1500,raw='Blackfeet 1,500 (Blackfeet agency)',basis='census',loc='inferred',at=(50.78, -112.82),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 104 (read from the page images of the 1873–83 tables, pdf 28)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1874,pop=1677,raw='Sissiton and Wahpeton Sioux 1,677 (Sisseton Sioux agency)',basis='census',loc='inferred',at=(45.61, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='twk',y=1874,pop=1100,raw='Two-Kettle Sioux 1,100 (Cheyenne River agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='wic',y=1874,pop=565,raw='Wichitas 300 (Wichita agency); Wacoes 140 (Wichita agency); Tawacamies 125 (Wichita agency)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 100 (read from the page images of the 1873–83 tables, pdf 24)',kind='primary'),
 dict(g='ynk',y=1874,pop=2000,raw='Yancton Sioux 2,000 (Yankton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1874, population table, p. 102 (read from the page images of the 1873–83 tables, pdf 26)',kind='primary'),
 dict(g='arn',y=1875,pop=1565,raw='Arapahoes 1,565 (Red Cloud agency)',basis='census',loc='inferred',at=(42.68, -103.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106 (read from the page images of the 1873–83 tables, pdf 37)',kind='primary'),
 dict(g='ars',y=1875,pop=1664,raw='Arapahoes 1,664 (Cheyenne and Arapahoe agency)',basis='census',loc='inferred',at=(35.57, -98.04),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 39)',kind='primary'),
 dict(g='ass',y=1875,pop=3500,raw='Assinaboines 3,500 (Fort Belknap agency)',basis='census',loc='inferred',at=(48.24, -107.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g='cwm',y=1875,pop=3000,raw='Mountain Crows 3,000 (Crow agency)',basis='census',loc='inferred',at=(45.42, -109.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g='cwr',y=1875,pop=1200,raw='River Crows 1,200 (Crow agency)',basis='census',loc='inferred',at=(45.87, -109.41),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g='gv',y=1875,pop=950,raw='Gros Ventres 950 (Fort Belknap agency)',basis='census',loc='inferred',at=(48.47, -108.76),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g='hid',y=1875,pop=600,raw='Gros Ventres 600 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106 (read from the page images of the 1873–83 tables, pdf 37)',kind='primary'),
 dict(g='hnk',y=1875,pop=2100,raw='Oncpapa Sioux 2,100 (Standing Rock agency)',basis='census',loc='inferred',at=(46.06, -101.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 39)',kind='primary'),
 dict(g='jic',y=1875,pop=950,raw='Jicarilla Apaches 400 (Abiquiu agency); Jicarila Apaches 550 (Cimarron agency)',basis='census',loc='inferred',at=(36.41, -104.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 114 (read from the page images of the 1873–83 tables, pdf 45)',kind='primary'),
 dict(g='kaw',y=1875,pop=516,raw='Kaws 516 (Osage agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 39)',kind='primary'),
 dict(g='kit',y=1875,pop=90,raw='Keechies 90 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 110 (read from the page images of the 1873–83 tables, pdf 41)',kind='primary'),
 dict(g='man',y=1875,pop=420,raw='Mandans 420 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106 (read from the page images of the 1873–83 tables, pdf 37)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1875,pop=1159,raw='Flandreau Sioux 359 (Flandreau agency); Santee Sioux 800 (Santee agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106, p. 112 (read from the page images of the 1873–83 tables, pdf 37, 43)',kind='primary'),
 dict(g='oma',y=1875,pop=1005,raw='Omahas 1,005 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g=['osg', 'osl'],y=1875,pop=3001,raw='Osages 3,001 (Osage agency)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 39)',kind='primary'),
 dict(g='oto',y=1875,pop=457,raw='Otoes and Missourias 457 (Otoe agency)',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 112 (read from the page images of the 1873–83 tables, pdf 43)',kind='primary'),
 dict(g='pon',y=1875,pop=734,raw='Poncas 734 (Ponca agency)',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106 (read from the page images of the 1873–83 tables, pdf 37)',kind='primary'),
 dict(g='sho',y=1875,pop=1800,raw='Shoshones, (eastern band) 1,800 (Shoshone agency)',basis='census',loc='inferred',at=(43.0, -108.63),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 120 (read from the page images of the 1873–83 tables, pdf 51)',kind='primary'),
 dict(g='sih',y=1875,pop=1749,raw='Blackfeet Sioux 730 (Cheyenne River agency); Blackfeet Sioux 1,019 (Standing Rock agency)',basis='census',loc='inferred',at=(46.01, -101.59),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106, p. 108 (read from the page images of the 1873–83 tables, pdf 37, 39)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1875,pop=1807,raw='Sisseton and Wahpeton Sioux 1,807 (Sisseton agency)',basis='census',loc='inferred',at=(45.61, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 106 (read from the page images of the 1873–83 tables, pdf 37)',kind='primary'),
 dict(g='wic',y=1875,pop=396,raw='Wichitas 228 (Wichita agency); Tawacanies 102 (Wichita agency); Wacos 66 (Wichita agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 110 (read from the page images of the 1873–83 tables, pdf 41)',kind='primary'),
 dict(g='ynk',y=1875,pop=2000,raw='Yankton Sioux 2,000 (Yankton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1875, population table, p. 108 (read from the page images of the 1873–83 tables, pdf 39)',kind='primary'),
 dict(g='ari',y=1876,pop=692,raw='Arickarees 692 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.86),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208 (read from the page images of the 1873–83 tables, pdf 58)',kind='primary'),
 dict(g='ars',y=1876,pop=1703,raw='Arapahoes 1,703 (Cheyenne and Arapahoe agency)',basis='census',loc='inferred',at=(35.57, -98.03),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='cwm',y=1876,pop=1500,raw='Mountain Crows 1,500 (Crow agency)',basis='census',loc='inferred',at=(45.59, -109.19),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 214 (read from the page images of the 1873–83 tables, pdf 64)',kind='primary'),
 dict(g='cwr',y=1876,pop=1000,raw='River Crows 1,000 (Crow agency)',basis='census',loc='inferred',at=(45.59, -109.2),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 214 (read from the page images of the 1873–83 tables, pdf 64)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1876,pop=1570,raw='Comanches 1,570 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(34.69, -98.48),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='hid',y=1876,pop=514,raw='Gros Ventres 414 (Fort Berthold agency); Gros Ventres, (seceders) f 100 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208 (read from the page images of the 1873–83 tables, pdf 58)',kind='primary'),
 dict(g='iow',y=1876,pop=224,raw='Iowas 224 (Great Nemaha agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 214 (read from the page images of the 1873–83 tables, pdf 64)',kind='primary'),
 dict(g='jic',y=1876,pop=746,raw='Jicarilla Apaches 326 (Abiquiu agency); Jicarilla Apaches 420 (Cimarron agency)',basis='census',loc='inferred',at=(36.08, -105.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 216 (read from the page images of the 1873–83 tables, pdf 66)',kind='primary'),
 dict(g='kap',y=1876,pop=373,raw='Apaches 48 (Cheyenne and Arapahoe agency); Apaches 325 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(35.27, -99.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='kaw',y=1876,pop=443,raw='Kaws 443 (Osage agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='kio',y=1876,pop=1090,raw='Kiowas 1,090 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(35.1, -99.62),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='kit',y=1876,pop=155,raw='Keechies and Wacos 155 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 212 (read from the page images of the 1873–83 tables, pdf 62)',kind='primary'),
 dict(g='man',y=1876,pop=241,raw='Mandans 241 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208 (read from the page images of the 1873–83 tables, pdf 58)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1876,pop=1154,raw='Flandreau Sioux 361 (Flandreau agency); Santee Sioux 793 (Santee agency.†)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208, p. 214 (read from the page images of the 1873–83 tables, pdf 58, 64)',kind='primary'),
 dict(g='oma',y=1876,pop=1027,raw='Omahas 1,027 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 214 (read from the page images of the 1873–83 tables, pdf 64)',kind='primary'),
 dict(g=['osg', 'osl'],y=1876,pop=2679,raw='Osage 2,679 (Osage agency)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='oto',y=1876,pop=454,raw='Otoes and Missourias 454 (Otoe agency)',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 214 (read from the page images of the 1873–83 tables, pdf 64)',kind='primary'),
 dict(g='pon',y=1876,pop=730,raw='Poncas 730 (Ponca agency)',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208 (read from the page images of the 1873–83 tables, pdf 58)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1876,pop=2026,raw='Pawnees 2,026 (Pawnee agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1876,pop=1745,raw='Sisseton and Wahpeton Sioux 1,745 (Sisseton agency)',basis='census',loc='inferred',at=(45.62, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 208 (read from the page images of the 1873–83 tables, pdf 58)',kind='primary'),
 dict(g='wic',y=1876,pop=317,raw='Tawacanies 100 (Wichita agency); Wichitas 217 (Wichita agency)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 212 (read from the page images of the 1873–83 tables, pdf 62)',kind='primary'),
 dict(g='ynk',y=1876,pop=1992,raw='Yankton Sioux 1,992 (Yancton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1876, population table, p. 210 (read from the page images of the 1873–83 tables, pdf 60)',kind='primary'),
 dict(g='ari',y=1877,pop=670,raw='Arickaree 670 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.86),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g='arn',y=1877,pop=1198,raw='Northern Arapaho 1,198 (Red Cloud agency)',basis='census',loc='inferred',at=(42.84, -106.03),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g='ars',y=1877,pop=1766,raw='Southern Arapaho 1,766 (Cheyenne and Arapaho agency)',basis='census',loc='inferred',at=(35.56, -98.02),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='ass',y=1877,pop=1719,raw='Assinaboine 1,719 (Fort Peck agency)',basis='census',loc='inferred',at=(48.16, -106.2),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g='chn',y=1877,pop=937,raw='Northern Cheyenne 937 (Cheyenne and Arapaho agency)',basis='census',loc='inferred',at=(45.02, -106.52),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='chs',y=1877,pop=2299,raw='Southern Cheyenne 2,299 (Cheyenne and Arapaho agency)',basis='census',loc='inferred',at=(35.32, -99.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='cwm',y=1877,pop=2200,raw='Mountain Crow 2,200 (Crow agency)',basis='census',loc='inferred',at=(45.76, -108.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g='cwr',y=1877,pop=1100,raw='River Crow 1,100 (Crow agency)',basis='census',loc='inferred',at=(45.76, -108.59),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1877,pop=1545,raw='Comanche 1,545 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(34.68, -98.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='gv',y=1877,pop=600,raw='Gros Ventre 600 (Fort Peck agency)',basis='census',loc='inferred',at=(48.37, -108.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g='hid',y=1877,pop=466,raw='Gros Ventre 466 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g='iow',y=1877,pop=217,raw='Iowa 217 (Great Nemaha agency)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g='jic',y=1877,pop=442,raw='Jicarilla Apache e 442 (Pueblo agency)',basis='census',loc='inferred',at=(35.74, -105.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 298 (read from the page images of the 1873–83 tables, pdf 90)',kind='primary'),
 dict(g='kap',y=1877,pop=343,raw='Apache 343 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(35.14, -99.63),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='kaw',y=1877,pop=424,raw='Kaw 424 (Osage agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='kio',y=1877,pop=1090,raw='Kiowa 1,090 (Kiowa and Comanche agency)',basis='census',loc='inferred',at=(34.64, -98.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='kit',y=1877,pop=90,raw='Keechie 90 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 294 (read from the page images of the 1873–83 tables, pdf 86)',kind='primary'),
 dict(g='man',y=1877,pop=257,raw='Mandan 257 (Fort Berthold agency)',basis='census',loc='inferred',at=(47.58, -101.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1877,pop=1108,raw='Flandreau (Santee) Sioux 364 (Flandreau agency); Santee Sioux 744 (Santee agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290, p. 296 (read from the page images of the 1873–83 tables, pdf 82, 88)',kind='primary'),
 dict(g='oma',y=1877,pop=1061,raw='Omaha 1,061 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 296 (read from the page images of the 1873–83 tables, pdf 88)',kind='primary'),
 dict(g=['osg', 'osl'],y=1877,pop=2391,raw='Osage 2,391 (Osage agency)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='pon',y=1877,pop=717,raw='Ponca 717 (Ponca agency)',basis='census',loc='inferred',at=(42.8, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1877,pop=1521,raw='Pawnee 1,521 (Pawnee agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 292 (read from the page images of the 1873–83 tables, pdf 84)',kind='primary'),
 dict(g='sih',y=1877,pop=562,raw='Blackfeet Sioux 562 (Standing Rock agency.g)',basis='census',loc='inferred',at=(45.62, -105.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1877,pop=1715,raw='Sisseton and Wahpeton Sioux 1,715 (Sisseton agency)',basis='census',loc='inferred',at=(45.62, -97.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g='sna',y=1877,pop=512,raw='Sans Arcs 512 (Spotted-Tail Agency)',basis='census',loc='inferred',at=(45.2, -104.89),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 67 (read from the page images of the 1873–83 tables, pdf 77)',kind='primary'),
 dict(g='wic',y=1877,pop=409,raw='Tawacanie 154 (Wichita agency); Waco 45 (Wichita agency); Wichita 210 (Wichita agency)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 294 (read from the page images of the 1873–83 tables, pdf 86)',kind='primary'),
 dict(g='ynk',y=1877,pop=2182,raw='Yankton Sioux 2,182 (Yankton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1877, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 82)',kind='primary'),
 dict(g='ass',y=1878,pop=2499,raw='Assinnaboine 884 (Fort Belknap agency); Assinnaboine 1,615 (Fort Peck agency)',basis='census',loc='inferred',at=(48.12, -105.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 288 (read from the page images of the 1873–83 tables, pdf 111)',kind='primary'),
 dict(g=['chs', 'chn'],y=1878,pop=3298,raw='Cheyenne 3,298 (Cheyenne and Arapaho agency)',basis='census',loc='inferred',at=(35.46, -98.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 284 (read from the page images of the 1873–83 tables, pdf 107)',kind='primary'),
 dict(g='cwm',y=1878,pop=2100,raw='Mountain Crow 2,100 (Crow agency)',basis='census',loc='inferred',at=(45.93, -107.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 288 (read from the page images of the 1873–83 tables, pdf 111)',kind='primary'),
 dict(g='cwr',y=1878,pop=1200,raw='River Crow 1,200 (Fort Belknap agency)',basis='census',loc='inferred',at=(45.94, -107.98),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 288 (read from the page images of the 1873–83 tables, pdf 111)',kind='primary'),
 dict(g='gv',y=1878,pop=1000,raw='Gros Ventre 1,000 (Fort Belknap agency)',basis='census',loc='inferred',at=(48.32, -108.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 288 (read from the page images of the 1873–83 tables, pdf 111)',kind='primary'),
 dict(g='iow',y=1878,pop=213,raw='Iowa 213 (Great Nemaha agency)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 288 (read from the page images of the 1873–83 tables, pdf 111)',kind='primary'),
 dict(g='jic',y=1878,pop=769,raw='Jicarilla Apache 769 (Abiquiu agency)',basis='census',loc='inferred',at=(35.41, -105.25),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 113)',kind='primary'),
 dict(g='kaw',y=1878,pop=424,raw='Kaw 424 (Osage agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 284 (read from the page images of the 1873–83 tables, pdf 107)',kind='primary'),
 dict(g='kit',y=1878,pop=87,raw='Keechie 87 (Wichita agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 286 (read from the page images of the 1873–83 tables, pdf 109)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1878,pop=1121,raw='Santee Sioux of Flandreau 364 (Flandreau agency); Santee Sioux 757 (Santee agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 282, p. 290 (read from the page images of the 1873–83 tables, pdf 105, 113)',kind='primary'),
 dict(g='ogl',y=1878,pop=6035,raw='Ogalalla Sioux 6,035 (Red Cloud agency)',basis='census',loc='inferred',at=(42.95, -102.74),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 284 (read from the page images of the 1873–83 tables, pdf 107)',kind='primary'),
 dict(g='oma',y=1878,pop=1100,raw='Omaha 1,100 (Omaha agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 290 (read from the page images of the 1873–83 tables, pdf 113)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1878,pop=1438,raw='Pawnee 1,438 (Pawnee agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 286 (read from the page images of the 1873–83 tables, pdf 109)',kind='primary'),
 dict(g='sih',y=1878,pop=813,raw='Blackfeet Sioux 223 (Cheyenne River agency); Blackfeet Sioux 590 (Standing Rock agency)',basis='census',loc='inferred',at=(45.61, -103.96),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 282, p. 284 (read from the page images of the 1873–83 tables, pdf 105, 107)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1878,pop=1500,raw='Sisseton and Wahpeton Sioux 1,500 (Sisseton agency)',basis='census',loc='inferred',at=(45.63, -97.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 284 (read from the page images of the 1873–83 tables, pdf 107)',kind='primary'),
 dict(g='twk',y=1878,pop=917,raw='Two Kettle Sioux 917 (Cheyenne River agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 105)',kind='primary'),
 dict(g='wic',y=1878,pop=431,raw='Wichita 206 (Wichita agency); Waco 65 (Wichita agency); Towaconie 160 (Wichita agency)',basis='census',loc='inferred',at=(35.07, -98.24),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 286 (read from the page images of the 1873–83 tables, pdf 109)',kind='primary'),
 dict(g='ynk',y=1878,pop=2112,raw='Yankton Sioux 2,112 (Yankton agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1878, population table, p. 284 (read from the page images of the 1873–83 tables, pdf 107)',kind='primary'),
 dict(g='ari',y=1880,pop=724,raw='Arickaree 724 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240 (read from the page images of the 1873–83 tables, pdf 147)',kind='primary'),
 dict(g='arn',y=1880,pop=913,raw='Arapaho 913 (Shoshone Agency)',basis='census',loc='inferred',at=(42.63, -107.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 254 (read from the page images of the 1873–83 tables, pdf 161)',kind='primary'),
 dict(g='ars',y=1880,pop=2132,raw='Arapaho 2,132 (Cheyenne and Arapaho Agency)',basis='census',loc='inferred',at=(35.56, -98.01),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 242 (read from the page images of the 1873–83 tables, pdf 149)',kind='primary'),
 dict(g='ass',y=1880,pop=2365,raw='Assinaboine 1,430 (Fort Peck Agency); Assinaboine 935 (Fort Belknap Agency)',basis='census',loc='inferred',at=(48.12, -105.35),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 246 (read from the page images of the 1873–83 tables, pdf 153)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1880,pop=3470,raw='Mountain and River Crow 3,470 (Crow Agency)',basis='census',loc='inferred',at=(45.82, -107.72),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 246 (read from the page images of the 1873–83 tables, pdf 153)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1880,pop=1568,raw='Comanche 1,413 (Kiowa, Comanche, and Wichita Agency); Penetethka Comanche 155 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.66, -98.41),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 242 (read from the page images of the 1873–83 tables, pdf 149)',kind='primary'),
 dict(g='gv',y=1880,pop=1148,raw='Gros Ventre 1,148 (Fort Belknap Agency)',basis='census',loc='inferred',at=(48.22, -108.61),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 246 (read from the page images of the 1873–83 tables, pdf 153)',kind='primary'),
 dict(g='hid',y=1880,pop=450,raw='Gros Ventre 450 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240 (read from the page images of the 1873–83 tables, pdf 147)',kind='primary'),
 dict(g='jic',y=1880,pop=752,raw='Jicarilla Apache 752 (Abiquiu)',basis='census',loc='inferred',at=(34.74, -105.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 248 (read from the page images of the 1873–83 tables, pdf 155)',kind='primary'),
 dict(g='kit',y=1880,pop=75,raw='Keechie 75 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 242 (read from the page images of the 1873–83 tables, pdf 149)',kind='primary'),
 dict(g='man',y=1880,pop=228,raw='Mandan 228 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.83),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240 (read from the page images of the 1873–83 tables, pdf 147)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1880,pop=1068,raw='Santee Sioux 764 (Santee Agency); Santee Sioux at Flandreau, in Dakota 304 (Santee Agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 246 (read from the page images of the 1873–83 tables, pdf 153)',kind='primary'),
 dict(g='ogl',y=1880,pop=7200,raw='Ogalala Sioux 7,200 (Pine Ridge Agency)',basis='census',loc='inferred',at=(43.03, -102.55),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240 (read from the page images of the 1873–83 tables, pdf 147)',kind='primary'),
 dict(g='oto',y=1880,pop=438,raw='Otoe and Missouri a 438 (Otoe Agency)',basis='census',loc='inferred',at=(40.05, -96.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 246 (read from the page images of the 1873–83 tables, pdf 153)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1880,pop=1306,raw='Pawnee 1,306 (Pawnee Agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 244 (read from the page images of the 1873–83 tables, pdf 151)',kind='primary'),
 dict(g='sho',y=1880,pop=1150,raw='Shoshone 1,150 (Shoshone Agency)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 254 (read from the page images of the 1873–83 tables, pdf 161)',kind='primary'),
 dict(g='sih',y=1880,pop=959,raw='Blackfeet Sioux 239 (Cheyenne River Agency); Blackfeet Sioux 720 (Standing Rock Agency)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240, p. 242 (read from the page images of the 1873–83 tables, pdf 147, 149)',kind='primary'),
 dict(g='twk',y=1880,pop=680,raw='Two Kettle Sioux 680 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 240 (read from the page images of the 1873–83 tables, pdf 147)',kind='primary'),
 dict(g='wic',y=1880,pop=391,raw='Wichita 198 (Kiowa, Comanche, and Wichita Agency); Waco 47 (Kiowa, Comanche, and Wichita Agency); Towaconie 146 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.97, -98.14),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 242 (read from the page images of the 1873–83 tables, pdf 149)',kind='primary'),
 dict(g='ynk',y=1880,pop=2019,raw='Yankton Sioux 2,019 (Yankton Agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1880, population table, p. 242 (read from the page images of the 1873–83 tables, pdf 149)',kind='primary'),
 dict(g='ari',y=1881,pop=678,raw='Arickaree 678 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='ars',y=1881,pop=2258,raw='Arapaho 2,258 (Cheyenne and Arapaho Agency)',basis='census',loc='inferred',at=(35.56, -98.02),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g=['chs', 'chn'],y=1881,pop=4197,raw='Cheyenne 4,197 (Cheyenne and Arapaho Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1881,pop=1561,raw='Comanche 1,396 (Kiowa, Comanche, and Wichita Agency); Penetheka Comanche 165 (Kiowa, Comanche, and Wichita Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(34.66, -98.41),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='hid',y=1881,pop=445,raw='Gros Ventre 445 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='hnk',y=1881,pop=1224,raw='Uncapapa Sioux 521 (Standing Rock Agency); Uncapapa Sioux 703 (Standing Rock Agency ("Hostile" Indians added July 28, 1881.))',basis='census',loc='inferred',at=(46.29, -101.74),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='iow',y=1881,pop=176,raw='Iowa 46 (Sac and Fox Agency (Indian Territory)); Iowa 130 (Great Nemaha Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278, p. 282 (read from the page images of the 1873–83 tables, pdf 172, 174)',kind='primary'),
 dict(g='jic',y=1881,pop=705,raw='Jicarilla Apache 705 (Jicarilla Subagency)',basis='census',loc='inferred',at=(34.41, -105.55),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 174)',kind='primary'),
 dict(g='kap',y=1881,pop=337,raw='Apache 337 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.02, -99.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='kaw',y=1881,pop=305,raw='Kaw 305 (Osage Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='kio',y=1881,pop=1145,raw='Kiowa 1,145 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.93, -99.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='kit',y=1881,pop=77,raw='Keechie 77 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='man',y=1881,pop=223,raw='Mandan 223 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.83),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1881,pop=1073,raw='Santee Sioux 767 (Santee Agency); Santee Sioux at Flandreau, Dakota 306 (Santee Agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 174)',kind='primary'),
 dict(g='min',y=1881,pop=1290,raw='Minneconjou Sioux 537 (Cheyenne River Agency); Minneconjou Sioux 753 (Standing Rock Agency ("Hostile" Indians added July 28, 1881.))',basis='census',loc='inferred',at=(44.67, -100.97),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 274, p. 276 (read from the page images of the 1873–83 tables, pdf 168, 170)',kind='primary'),
 dict(g='ogl',y=1881,pop=7758,raw='Ogallala Sioux 7,202 (Pine Ridge Agency); Ogallala Sioux 556 (Standing Rock Agency ("Hostile" Indians added July 28, 1881.))',basis='census',loc='inferred',at=(43.03, -102.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='oma',y=1881,pop=1121,raw='Omaha 1,121 (Winnebago Agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 174)',kind='primary'),
 dict(g=['osg', 'osl'],y=1881,pop=1806,raw='Osage 1,806 (Osage Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='pon',y=1881,pop=690,raw='Ponca 515 (Ponca Agency); Ponca 175 (Santee Agency)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278, p. 282 (read from the page images of the 1873–83 tables, pdf 172, 174)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1881,pop=1241,raw='Pawnee 1,241 (Pawnee Agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='sih',y=1881,pop=1094,raw='Blackfeet Sioux 259 (Cheyenne River Agency); Blackfeet Sioux 728 (Standing Rock Agency); Blackfeet Sioux 107 (Standing Rock Agency ("Hostile" Indians added July 28, 1881.))',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 274, p. 276 (read from the page images of the 1873–83 tables, pdf 168, 170)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1881,pop=1377,raw='Sisseton and Wahpeton Sioux 1,377 (Sisseton Agency)',basis='census',loc='inferred',at=(45.64, -97.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='sna',y=1881,pop=870,raw='Sans Arc Sioux 346 (Cheyenne River Agency); Sans Arc Sioux 524 (Standing Rock Agency ("Hostile" Indians added July 28, 1881.))',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 274, p. 276 (read from the page images of the 1873–83 tables, pdf 168, 170)',kind='primary'),
 dict(g='twk',y=1881,pop=759,raw='Two Kettle Sioux 759 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 274 (read from the page images of the 1873–83 tables, pdf 168)',kind='primary'),
 dict(g='wic',y=1881,pop=406,raw='Wichita 206 (Kiowa, Comanche, and Wichita Agency); Waco 49 (Kiowa, Comanche, and Wichita Agency); Towaconie 151 (Kiowa, Comanche, and Wichita Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(34.83, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 278 (read from the page images of the 1873–83 tables, pdf 172)',kind='primary'),
 dict(g='ynk',y=1881,pop=1998,raw='Yankton Sioux 1,998 (Yankton Agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1881, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 170)',kind='primary'),
 dict(g='arn',y=1882,pop=940,raw='Northern Arapaho 940 (Shoshone Agency)',basis='census',loc='inferred',at=(42.7, -107.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 344 (read from the page images of the 1873–83 tables, pdf 205)',kind='primary'),
 dict(g='ars',y=1882,pop=2314,raw='Arapahoe 2,314 (Cheyenne and Arapaho Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(35.56, -98.03),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='ass',y=1882,pop=2150,raw='Assinaboine 850 (Fort Belknap Agency); Assinaboine 1,300 (Fort Peck Agency)',basis='census',loc='inferred',at=(48.16, -105.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 197)',kind='primary'),
 dict(g=['chs', 'chn'],y=1882,pop=4255,raw='Cheyenne 4,255 (Cheyenne and Arapaho Agency)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1882,pop=1572,raw='Penetheka Comanche 165 (Kiowa, Comanche, and Wichita Agency); Comanche 1,407 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.67, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='hnk',y=1882,pop=1519,raw='Uncapapa Sioux 1,519 (Standing Rock Agency)',basis='census',loc='inferred',at=(46.09, -100.63),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='iow',y=1882,pop=217,raw='Iowa 86 (Sac and Fox Agency (Indian Territory)); Iowa 131 (Pottawatomie and Great Nemaha Agency (Kansas))',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 195)',kind='primary'),
 dict(g='jic',y=1882,pop=717,raw='Jicarilla Apache 717 (Mescalero and Jicarilla Agency)',basis='census',loc='inferred',at=(34.07, -105.65),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 338 (read from the page images of the 1873–83 tables, pdf 199)',kind='primary'),
 dict(g='kap',y=1882,pop=340,raw='Apache 340 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.03, -99.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='kaw',y=1882,pop=285,raw='Kaw 285 (Osage Agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 195)',kind='primary'),
 dict(g='kio',y=1882,pop=1176,raw='Kiowa 1,176 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.11, -98.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='kit',y=1882,pop=78,raw='Keechie 78 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1882,pop=1102,raw='Santee Sioux 762 (Santee and Flandreau Agency); Santee Sioux at Flandreau 340 (Santee and Flandreau Agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 197)',kind='primary'),
 dict(g='min',y=1882,pop=1399,raw='Minneconjou Sioux 1,399 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.7, -101.07),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 330 (read from the page images of the 1873–83 tables, pdf 191)',kind='primary'),
 dict(g='ogl',y=1882,pop=8117,raw='Ogalalla Sioux 8,117 (Pine Ridge Agency)',basis='census',loc='inferred',at=(43.03, -102.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='oma',y=1882,pop=1193,raw='Omaha 1,193 (Winnebago and Omaha Agency)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 336 (read from the page images of the 1873–83 tables, pdf 197)',kind='primary'),
 dict(g='oto',y=1882,pop=274,raw='Otoe and Missouria c 274 (Otoe Agency)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 195)',kind='primary'),
 dict(g='pon',y=1882,pop=710,raw='Ponca 542 (Ponca Agency); Ponca 168 (Santee and Flandreau Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 334, p. 336 (read from the page images of the 1873–83 tables, pdf 195, 197)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1882,pop=1251,raw='Pawnee 1,251 (Pawnee Agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 334 (read from the page images of the 1873–83 tables, pdf 195)',kind='primary'),
 dict(g='sho',y=1882,pop=842,raw='Shoshone 842 (Shoshone Agency)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 344 (read from the page images of the 1873–83 tables, pdf 205)',kind='primary'),
 dict(g='sih',y=1882,pop=928,raw='Blackfeet Sioux 239 (Cheyenne River Agency); Blackfeet Sioux 689 (Standing Rock Agency) (a digit uncertain in the print)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 330, p. 332 (read from the page images of the 1873–83 tables, pdf 191, 193)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1882,pop=1466,raw='Sisseton and Wahpeton Sioux 1,466 (Sisseton Agency)',basis='census',loc='inferred',at=(45.64, -97.15),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='sna',y=1882,pop=776,raw='Sans Arc Sioux 776 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 330 (read from the page images of the 1873–83 tables, pdf 191)',kind='primary'),
 dict(g='twk',y=1882,pop=774,raw='Two Kettle Sioux 774 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 330 (read from the page images of the 1873–83 tables, pdf 191)',kind='primary'),
 dict(g='wic',y=1882,pop=415,raw='Wichita 214 (Kiowa, Comanche, and Wichita Agency); Towaconie 152 (Kiowa, Comanche, and Wichita Agency); Waco 49 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='ynk',y=1882,pop=1977,raw='Yankton Sioux 1,977 (Yankton Agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1882, population table, p. 332 (read from the page images of the 1873–83 tables, pdf 193)',kind='primary'),
 dict(g='ari',y=1883,pop=591,raw='Arickaree 591 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g='arn',y=1883,pop=952,raw='Northern Arapaho 952 (Shoshone Agency)',basis='census',loc='inferred',at=(42.73, -107.82),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 228)',kind='primary'),
 dict(g='ars',y=1883,pop=2310,raw='Arapaho 2,310 (Cheyenne and Arapaho Agency)',basis='census',loc='inferred',at=(35.57, -98.04),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g='ass',y=1883,pop=2125,raw='Assinaboine 750 (Fort Belknap Agency); Assinaboine 1,375 (Fort Peck Agency)',basis='census',loc='inferred',at=(48.17, -105.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 274 (read from the page images of the 1873–83 tables, pdf 220)',kind='primary'),
 dict(g=['chs', 'chn'],y=1883,pop=4186,raw='Cheyenne 4,186 (Cheyenne and Arapaho Agency)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1883,pop=3200,raw='Crows 3,200 (Crow Agency)',basis='census',loc='inferred',at=(45.47, -107.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 274 (read from the page images of the 1873–83 tables, pdf 220)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1883,pop=1561,raw='Comanche 1,396 (Kiowa, Comanche, and Wichita Agency); Penetheka Comanche 165 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.67, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='hid',y=1883,pop=347,raw='Gros Ventre 347 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g='hnk',y=1883,pop=1829,raw='Uncapapa Sioux 1,829 (Standing Rock Agency)',basis='census',loc='inferred',at=(46.09, -100.64),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g='iow',y=1883,pop=220,raw='Iowa 88 (Sac and Fox Agency (Indian Territory)); Iowa 132 (Pottawatomie and Great Nemaha Agency (Kansas)) (a digit uncertain in the print)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272, p. 274 (read from the page images of the 1873–83 tables, pdf 218, 220)',kind='primary'),
 dict(g='jic',y=1883,pop=700,raw='Jicarilla Apache 700 (Mescalero and Jicarilla Agency)',basis='census',loc='inferred',at=(33.74, -105.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 222)',kind='primary'),
 dict(g='kap',y=1883,pop=337,raw='Apache 337 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.04, -98.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='kaw',y=1883,pop=292,raw='Kaw 292 (Osage Agency)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='kio',y=1883,pop=1167,raw='Kiowa 1,167 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.1, -98.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='kit',y=1883,pop=77,raw='Keechie 77 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='man',y=1883,pop=308,raw='Mandan 308 (Fort Berthold Agency)',basis='census',loc='inferred',at=(47.58, -101.83),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1883,pop=1030,raw='Santee Sioux 762 (Santee and Flandreau Agency); Santee Sioux at Flandreau 268 (Santee and Flandreau Agency)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 276 (read from the page images of the 1873–83 tables, pdf 222)',kind='primary'),
 dict(g='min',y=1883,pop=1423,raw='Minneconjou Sioux 1,423 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.72, -101.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g='ogl',y=1883,pop=7800,raw='Ogalalla Sioux 7,800 (Pine Ridge Agency)',basis='census',loc='inferred',at=(43.03, -102.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g=['osg', 'osl'],y=1883,pop=1764,raw='Osage 1,764 (Osage Agency)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='oto',y=1883,pop=262,raw='Otoe and Missouria 262 (Otoe Agency)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='pon',y=1883,pop=707,raw='Ponca 537 (Ponca Agency); Ponca 170 (Santee and Flandreau Agency)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272, p. 276 (read from the page images of the 1873–83 tables, pdf 218, 222)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1883,pop=1212,raw='Pawnee 1,212 (Pawnee Agency)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='sho',y=1883,pop=928,raw='Shoshone d 928 (Shoshone Agency)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 282 (read from the page images of the 1873–83 tables, pdf 228)',kind='primary'),
 dict(g='sih',y=1883,pop=936,raw='Blackfeet Sioux 238 (Cheyenne River Agency); Blackfeet Sioux 698 (Standing Rock Agency)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268, p. 270 (read from the page images of the 1873–83 tables, pdf 214, 216)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1883,pop=1479,raw='Sisseton and Wahpeton Sioux 1,479 (Sisseton Agency)',basis='census',loc='inferred',at=(45.65, -97.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g='sna',y=1883,pop=771,raw='Sans-Arc Sioux 771 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g='twk',y=1883,pop=783,raw='Two Kettle Sioux 783 (Cheyenne River Agency)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 268 (read from the page images of the 1873–83 tables, pdf 214)',kind='primary'),
 dict(g='wic',y=1883,pop=429,raw='Wichita 216 (Kiowa, Comanche, and Wichita Agency); Wacoe 51 (Kiowa, Comanche, and Wichita Agency); Towaconie 162 (Kiowa, Comanche, and Wichita Agency)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 272 (read from the page images of the 1873–83 tables, pdf 218)',kind='primary'),
 dict(g='ynk',y=1883,pop=1950,raw='Yankton Sioux 1,950 (Yankton Agency)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1883, population table, p. 270 (read from the page images of the 1873–83 tables, pdf 216)',kind='primary'),
 dict(g='ari',y=1884,pop=544,raw='Arickaree 544 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.58, -101.87),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='arn',y=1884,pop=965,raw='Northern Arapaho 965 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.77, -107.92),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 300 (read from the page images of the 1884–99 tables, pdf 19)',kind='primary'),
 dict(g='ars',y=1884,pop=2366,raw='Arapaho 2,366 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.57, -98.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 288 (read from the page images of the 1884–99 tables, pdf 7)',kind='primary'),
 dict(g='ass',y=1884,pop=2195,raw='Assinaboine 1,000 (Fort Belknap Agency, Montana); Assinaboine 1,195 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.19, -105.78),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 292 (read from the page images of the 1884–99 tables, pdf 11)',kind='primary'),
 dict(g='chs',y=1884,pop=3905,raw='Cheyenne 3,905 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 288 (read from the page images of the 1884–99 tables, pdf 7)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1884,pop=3226,raw='Crows 3,226 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.36, -107.79),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 292 (read from the page images of the 1884–99 tables, pdf 11)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1884,pop=1547,raw='Comanche 1,382 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Penetheka Comanche 165 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.67, -98.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='gv',y=1884,pop=1150,raw='Gross Ventre 1,150 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 292 (read from the page images of the 1884–99 tables, pdf 11)',kind='primary'),
 dict(g='hid',y=1884,pop=347,raw='Gros Ventre 347 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='hnk',y=1884,pop=1976,raw='Uncapapa Sioux 1,976 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(46.1, -100.65),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 288 (read from the page images of the 1884–99 tables, pdf 7)',kind='primary'),
 dict(g='iow',y=1884,pop=231,raw='Iowa 88 (Sac and Fox Agency, Indian Territory); Iowa 143 (Pottawatomie and Great Nemaha Agency, Kansas)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290, p. 292 (read from the page images of the 1884–99 tables, pdf 9, 11)',kind='primary'),
 dict(g='jic',y=1884,pop=890,raw='Jicarilla Apache 890 (Mescalero and Jicarilla Agency, New Mexico)',basis='census',loc='inferred',at=(33.84, -105.93),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 294 (read from the page images of the 1884–99 tables, pdf 13)',kind='primary'),
 dict(g='kap',y=1884,pop=308,raw='Apache 308 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.04, -98.84),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='kaw',y=1884,pop=245,raw='Kaw 245 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='kio',y=1884,pop=1152,raw='Kiowa 1,152 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.1, -98.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='kit',y=1884,pop=79,raw='Keechie 79 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='man',y=1884,pop=311,raw='Mandan 311 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.58, -101.83),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1884,pop=1479,raw='Santee Sioux 423 (Fort Peck Agency, Montana); Santee Sioux 806 (Santee and Flandreau Agency, Nebraska); Santee Sioux at Flandreau 250 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 292, p. 294 (read from the page images of the 1884–99 tables, pdf 11, 13)',kind='primary'),
 dict(g='min',y=1884,pop=1382,raw='Minneconjou Sioux 1,382 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.75, -101.25),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='ogl',y=1884,pop=7800,raw='Ogalalla Sioux 7,800 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='oma',y=1884,pop=1167,raw='Omaha 1,167 (Winnebago and Omaha Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 294 (read from the page images of the 1884–99 tables, pdf 13)',kind='primary'),
 dict(g=['osg', 'osl'],y=1884,pop=1570,raw='Osage 1,570 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='oto',y=1884,pop=514,raw='Otoe and Missouria 274 (Osage Agency, Indian Territory); Otoe 240 (Sac and Fox Agency, Indian Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='pon',y=1884,pop=734,raw='Ponca 560 (Osage Agency, Indian Territory); Ponca 174 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290, p. 294 (read from the page images of the 1884–99 tables, pdf 9, 13)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1884,pop=1142,raw='Pawnee 1,142 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='sho',y=1884,pop=890,raw='Shoshone 890 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 300 (read from the page images of the 1884–99 tables, pdf 19)',kind='primary'),
 dict(g='sih',y=1884,pop=878,raw='Blackfeet Sioux 224 (Cheyenne River Agency, Dakota); Blackfeet Sioux 654 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286, p. 288 (read from the page images of the 1884–99 tables, pdf 5, 7)',kind='primary'),
 dict(g='sna',y=1884,pop=788,raw='Sans-Arc Sioux 788 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='twk',y=1884,pop=750,raw='Two Kettle Sioux 750 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 286 (read from the page images of the 1884–99 tables, pdf 5)',kind='primary'),
 dict(g='wic',y=1884,pop=412,raw='Wichita 209 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Wacoe 40 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Towaconie 163 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 290 (read from the page images of the 1884–99 tables, pdf 9)',kind='primary'),
 dict(g='ynk',y=1884,pop=1950,raw='Yankton Sioux 1,950 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1884, population table, p. 288 (read from the page images of the 1884–99 tables, pdf 7)',kind='primary'),
 dict(g='arn',y=1885,pop=971,raw='Northern Arapaho 971 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.8, -108.02),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 44)',kind='primary'),
 dict(g='ars',y=1885,pop=1327,raw='Arapaho 1,327 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.58, -98.06),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='chs',y=1885,pop=2282,raw='Cheyenne 2,282 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1885,pop=1544,raw='Comanche 1,544 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.67, -98.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='gv',y=1885,pop=852,raw='Gros Ventre 852 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 344 (read from the page images of the 1884–99 tables, pdf 34)',kind='primary'),
 dict(g='hid',y=1885,pop=435,raw='Gros Ventre 435 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.6, -102.25),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 340 (read from the page images of the 1884–99 tables, pdf 30)',kind='primary'),
 dict(g='hnk',y=1885,pop=1805,raw='Uncapapa Sioux 1,805 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(46.1, -100.66),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 340 (read from the page images of the 1884–99 tables, pdf 30)',kind='primary'),
 dict(g='jic',y=1885,pop=721,raw='Jicarilla Apache 721 (Mescalero Agency, New Mexico)',basis='census',loc='inferred',at=(34.72, -106.23),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 346 (read from the page images of the 1884–99 tables, pdf 36)',kind='primary'),
 dict(g='kap',y=1885,pop=319,raw='Apache 319 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.05, -98.68),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='kaw',y=1885,pop=225,raw='Kaw 225 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='kit',y=1885,pop=74,raw='Keechie 74 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1885,pop=1086,raw='Santee Sioux 843 (Santee and Flandreau Agency, Nebraska); Santee Sioux at Flandreau 243 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 346 (read from the page images of the 1884–99 tables, pdf 36)',kind='primary'),
 dict(g='min',y=1885,pop=1221,raw='Minneconjou Sioux 1,221 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.78, -101.35),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 338 (read from the page images of the 1884–99 tables, pdf 28)',kind='primary'),
 dict(g='ogl',y=1885,pop=7155,raw='Ogalalla Sioux 7,155 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 340 (read from the page images of the 1884–99 tables, pdf 30)',kind='primary'),
 dict(g='oma',y=1885,pop=1188,raw='Omaha 1,188 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 346 (read from the page images of the 1884–99 tables, pdf 36)',kind='primary'),
 dict(g=['osg', 'osl'],y=1885,pop=1552,raw='Osage 1,552 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='oto',y=1885,pop=266,raw='Otoe and Missouria 266 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='pon',y=1885,pop=752,raw='Ponca 574 (Ponca, Pawnee, and Otoe Agency, Indian Territory); Ponca of Dakota 178 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342, p. 346 (read from the page images of the 1884–99 tables, pdf 32, 36)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1885,pop=1045,raw='Pawnee 1,045 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='sho',y=1885,pop=870,raw='Shoshone 870 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 44)',kind='primary'),
 dict(g='sih',y=1885,pop=872,raw='Blackfeet Sioux 210 (Cheyenne River Agency, Dakota); Blackfeet Sioux 662 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 338, p. 340 (read from the page images of the 1884–99 tables, pdf 28, 30)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1885,pop=1484,raw='Sisseton and Wahpeton Sioux 1,484 (Sisseton Agency, Dakota)',basis='census',loc='inferred',at=(45.66, -97.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 340 (read from the page images of the 1884–99 tables, pdf 30)',kind='primary'),
 dict(g='sna',y=1885,pop=736,raw='Sans-Arc Sioux 736 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 338 (read from the page images of the 1884–99 tables, pdf 28)',kind='primary'),
 dict(g='twk',y=1885,pop=740,raw='Two Kettle Sioux 740 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 338 (read from the page images of the 1884–99 tables, pdf 28)',kind='primary'),
 dict(g='wic',y=1885,pop=390,raw='Towaconie 162 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Wacoe 39 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Wichita 189 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 342 (read from the page images of the 1884–99 tables, pdf 32)',kind='primary'),
 dict(g='ynk',y=1885,pop=1726,raw='Yankton Sioux 1,726 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1885, population table, p. 340 (read from the page images of the 1884–99 tables, pdf 30)',kind='primary'),
 dict(g='ari',y=1886,pop=517,raw='Arickaree 517 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.63, -101.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='arn',y=1886,pop=950,raw='Northern Arapaho 950 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.84, -108.11),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 410 (read from the page images of the 1884–99 tables, pdf 69)',kind='primary'),
 dict(g='ars',y=1886,pop=1217,raw='Arapaho 1,217 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.58, -98.06),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='ass',y=1886,pop=1688,raw='Assinaboine 794 (Fort Belknap Agency, Montana); Assinaboine 894 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.22, -106.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 400, p. 402 (read from the page images of the 1884–99 tables, pdf 59, 61)',kind='primary'),
 dict(g='chn',y=1886,pop=1064,raw='Northern Cheyenne 269 (Pine Ridge Agency, Dakota); Northern Cheyenne 795 (Tongue River Agency, Montana)',basis='census',loc='inferred',at=(45.59, -106.64),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396, p. 402 (read from the page images of the 1884–99 tables, pdf 55, 61)',kind='primary'),
 dict(g='chs',y=1886,pop=2217,raw='Cheyenne 2,217 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1886,pop=3226,raw='Crow 3,226 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.32, -107.78),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 400 (read from the page images of the 1884–99 tables, pdf 59)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1886,pop=1592,raw='Comanche 1,592 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.67, -98.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='gv',y=1886,pop=856,raw='Gros Ventre 856 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 400 (read from the page images of the 1884–99 tables, pdf 59)',kind='primary'),
 dict(g='hid',y=1886,pop=522,raw='Gros Ventre 522 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.6, -102.25),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='hnk',y=1886,pop=1905,raw='Uncapapa Sioux 1,905 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(46.11, -100.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='iow',y=1886,pop=227,raw='Iowa 84 (Sac and Fox Agency, Indian Territory); Iowa 143 (Pottawatomie and Great Nemaha, Kansas)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398, p. 400 (read from the page images of the 1884–99 tables, pdf 57, 59)',kind='primary'),
 dict(g='jic',y=1886,pop=785,raw='Jicarilla Apache 785 (Mescalero Agency, New Mexico)',basis='census',loc='inferred',at=(35.61, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 402 (read from the page images of the 1884–99 tables, pdf 61)',kind='primary'),
 dict(g='kap',y=1886,pop=332,raw='Apache 332 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.01, -98.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='kio',y=1886,pop=1164,raw='Kiowa 1,164 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.82, -98.69),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='man',y=1886,pop=283,raw='Mandan 283 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.45, -102.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='min',y=1886,pop=1221,raw='Minneconjou Sioux 1,221 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.81, -101.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 394 (read from the page images of the 1884–99 tables, pdf 53)',kind='primary'),
 dict(g='ogl',y=1886,pop=4159,raw='Ogalalla Sioux 4,159 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='oma',y=1886,pop=1160,raw='Omaha 1,160 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 402 (read from the page images of the 1884–99 tables, pdf 61)',kind='primary'),
 dict(g=['osg', 'osl'],y=1886,pop=1582,raw='Osage 1,582 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='pon',y=1886,pop=753,raw='Ponca 546 (Ponca, Pawnee, and Otoe Agency, Indian Territory); Ponca of Dakota 207 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398, p. 402 (read from the page images of the 1884–99 tables, pdf 57, 61)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1886,pop=998,raw='Pawnee 998 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='sho',y=1886,pop=850,raw='Shoshone 850 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 410 (read from the page images of the 1884–99 tables, pdf 69)',kind='primary'),
 dict(g='sih',y=1886,pop=812,raw='Blackfeet Sioux 204 (Cheyenne River Agency, Dakota); Blackfeet Sioux 608 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 394, p. 396 (read from the page images of the 1884–99 tables, pdf 53, 55)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1886,pop=1496,raw='Sisseton and Wahpeton Sioux 1,496 (Sisseton Agency, Dakota)',basis='census',loc='inferred',at=(45.66, -97.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='sna',y=1886,pop=735,raw='Sans-Arc Sioux 735 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 394 (read from the page images of the 1884–99 tables, pdf 53)',kind='primary'),
 dict(g='twk',y=1886,pop=647,raw='Two Kettle Sioux 647 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 394 (read from the page images of the 1884–99 tables, pdf 53)',kind='primary'),
 dict(g='wic',y=1886,pop=400,raw='Towaconie 133 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Waco 80 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Wichita 187 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 398 (read from the page images of the 1884–99 tables, pdf 57)',kind='primary'),
 dict(g='ynk',y=1886,pop=1776,raw='Yankton Sioux 1,776 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1886, population table, p. 396 (read from the page images of the 1884–99 tables, pdf 55)',kind='primary'),
 dict(g='ari',y=1887,pop=501,raw='Arickaree 501 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.62, -101.76),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='ass',y=1887,pop=1643,raw='Assinaboine 816 (Fort Belknap Agency, Montana); Assinaboine 827 (Fort Peck Agency, Montana) (a digit uncertain in the print)',basis='census',loc='inferred',at=(48.24, -106.11),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 356 (read from the page images of the 1884–99 tables, pdf 82)',kind='primary'),
 dict(g='chn',y=1887,pop=1142,raw='Northern Cheyenne 323 (Pine Ridge Agency, Dakota); Northern Cheyenne 819 (Tongue River Agency, Montana)',basis='census',loc='inferred',at=(45.56, -106.62),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350, p. 356 (read from the page images of the 1884–99 tables, pdf 76, 82)',kind='primary'),
 dict(g='chs',y=1887,pop=2058,raw='Cheyenne 2,058 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1887,pop=2456,raw='Crow 2,456 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.34, -107.76),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 356 (read from the page images of the 1884–99 tables, pdf 82)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1887,pop=1646,raw='Comanche 1,646 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.67, -98.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='gv',y=1887,pop=904,raw='Gros Ventre 904 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 356 (read from the page images of the 1884–99 tables, pdf 82)',kind='primary'),
 dict(g='hid',y=1887,pop=502,raw='Gros Ventre 502 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.6, -102.19),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='hnk',y=1887,pop=1736,raw='Uncapapa Sioux 1,736 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(46.11, -100.69),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='iow',y=1887,pop=234,raw='Iowa 89 (Sac and Fox Agency, Indian Territory); Iowa 145 (Pottawatomie and Great Nemaha, Kansas)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 80)',kind='primary'),
 dict(g='jic',y=1887,pop=785,raw='Jicarilla Apache a 785 (Southern Ute Agency, Colorado)',basis='census',loc='inferred',at=(36.49, -106.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='kap',y=1887,pop=332,raw='Apache 332 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.94, -98.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='kio',y=1887,pop=1179,raw='Kiowa 1,179 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.89, -98.67),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='kit',y=1887,pop=72,raw='Keechie 72 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='man',y=1887,pop=286,raw='Mandan 286 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.47, -102.06),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1887,pop=1094,raw='Santee Sioux 853 (Santee and Flandreau Agency, Nebraska); Santee Sioux at Flandreau 241 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 356 (read from the page images of the 1884–99 tables, pdf 82)',kind='primary'),
 dict(g='min',y=1887,pop=1212,raw='Minneconjou Sioux 1,212 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.84, -101.53),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='ogl',y=1887,pop=4197,raw='Ogalalla Sioux 4,197 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g=['osg', 'osl'],y=1887,pop=1501,raw='Osage 1,501 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 80)',kind='primary'),
 dict(g='oto',y=1887,pop=355,raw='Otoe and Missouria 355 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 80)',kind='primary'),
 dict(g='pon',y=1887,pop=731,raw='Ponca 523 (Ponca, Pawnee, and Otoe Agency, Indian Territory); Ponca of Dakota 208 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 354, p. 356 (read from the page images of the 1884–99 tables, pdf 80, 82)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1887,pop=918,raw='Pawnee 918 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 354 (read from the page images of the 1884–99 tables, pdf 80)',kind='primary'),
 dict(g='sho',y=1887,pop=876,raw='Shoshone 876 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 364 (read from the page images of the 1884–99 tables, pdf 90)',kind='primary'),
 dict(g='sih',y=1887,pop=783,raw='Blackfeet Sioux 199 (Cheyenne River Agency, Dakota); Blackfeet Sioux 584 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350, p. 352 (read from the page images of the 1884–99 tables, pdf 76, 78)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1887,pop=1519,raw='Sisseton and Wahpeton Sioux 1,519 (Sisseton Agency, Dakota)',basis='census',loc='inferred',at=(45.67, -97.16),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='sna',y=1887,pop=730,raw='Sans-Arc Sioux 730 (Cheyenne River Agency, Dakota) (a digit uncertain in the print)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='twk',y=1887,pop=642,raw='Two Kettle Sioux 642 (Cheyenne River Agency, Dakota)',basis='census',loc='inferred',at=(44.6, -100.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 350 (read from the page images of the 1884–99 tables, pdf 76)',kind='primary'),
 dict(g='wic',y=1887,pop=386,raw='Waco 37 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Towaconie 157 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Wichita 192 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='ynk',y=1887,pop=1777,raw='Yankton Sioux 1,777 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1887, population table, p. 352 (read from the page images of the 1884–99 tables, pdf 78)',kind='primary'),
 dict(g='arn',y=1888,pop=1008,raw='Northern Arapaho 1,008 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.91, -108.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 428 (read from the page images of the 1884–99 tables, pdf 113)',kind='primary'),
 dict(g='ars',y=1888,pop=1106,raw='Arapahoes 1,106 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.59, -98.08),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='ass',y=1888,pop=1543,raw='Assinaboine 830 (Fort Belknap Agency, Montana); Assinaboine 713 (Fort Peck Agency, Montana) (a digit uncertain in the print)',basis='census',loc='inferred',at=(48.26, -106.22),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 418 (read from the page images of the 1884–99 tables, pdf 103)',kind='primary'),
 dict(g='chn',y=1888,pop=1401,raw='Cheyenne (northern) 557 (Pine Ridge Agency, Dakota); Northern Cheyenne 844 (Tongue River Agency, Montana)',basis='census',loc='inferred',at=(45.53, -106.6),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 412, p. 418 (read from the page images of the 1884–99 tables, pdf 97, 103)',kind='primary'),
 dict(g='chs',y=1888,pop=2096,raw='Cheyennes 2,096 (Cheyenne and Arapaho Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1888,pop=1564,raw='Comanche 1,564 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.67, -98.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='gv',y=1888,pop=964,raw='Gros Ventre 964 (Fort Belknap Agency, Montana) (a digit uncertain in the print)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 418 (read from the page images of the 1884–99 tables, pdf 103)',kind='primary'),
 dict(g='hid',y=1888,pop=540,raw='Gros Ventre 540 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.59, -101.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 412 (read from the page images of the 1884–99 tables, pdf 97)',kind='primary'),
 dict(g='hnk',y=1888,pop=1808,raw='Hunkpapa Sioux 1,808 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(46.11, -100.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='iow',y=1888,pop=231,raw='Iowa 84 (Sac and Fox Agency, Indian Territory); Iowa 147 (Pottawatomie and Great Nemaha Agency, Kansas)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='kap',y=1888,pop=348,raw='Apache 348 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.86, -98.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='kaw',y=1888,pop=196,raw='Kansas 196 (Osage Agency, Indian Territory) (a digit uncertain in the print)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='kio',y=1888,pop=1121,raw='Kiowa 1,121 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.97, -98.65),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='kit',y=1888,pop=61,raw='Keechee 61 (Kiowa, Comanche, and Wichita Agency, Indian Territory) (a digit uncertain in the print)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='man',y=1888,pop=253,raw='Mandans 253 (Fort Berthold Agency, Dakota)',basis='census',loc='inferred',at=(47.53, -101.94),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 412 (read from the page images of the 1884–99 tables, pdf 97)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1888,pop=1078,raw='Santee Sioux at Flandreau, Dak. 221 (Santee and Flandreau Agency, Nebraska); Santee Sioux 857 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 418 (read from the page images of the 1884–99 tables, pdf 103)',kind='primary'),
 dict(g='ogl',y=1888,pop=4549,raw='Ogalalla Sioux 4,549 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 412 (read from the page images of the 1884–99 tables, pdf 97)',kind='primary'),
 dict(g='oma',y=1888,pop=1135,raw='Omaha 1,135 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 418 (read from the page images of the 1884–99 tables, pdf 103)',kind='primary'),
 dict(g=['osg', 'osl'],y=1888,pop=1504,raw='Osage 1,504 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.7, -96.4),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='oto',y=1888,pop=316,raw='Otoe and Missouria 316 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='pon',y=1888,pop=737,raw='Ponca 520 (Ponca, Pawnee, and Otoe Agency, Indian Territory); Ponca of Dakota 217 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416, p. 418 (read from the page images of the 1884–99 tables, pdf 101, 103)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1888,pop=869,raw='Pawnee 869 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='sho',y=1888,pop=877,raw='Shoshone 877 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.9),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 428 (read from the page images of the 1884–99 tables, pdf 113)',kind='primary'),
 dict(g='sih',y=1888,pop=542,raw='Blackfeet Sioux 542 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1888,pop=1487,raw='Sisseton and Wahpeton Sioux 1,487 (Sisseton Agency, Dakota)',basis='census',loc='inferred',at=(45.67, -97.17),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='tkw',y=1888,pop=79,raw='Tonkawa 79 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.66, -97.32),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 416 (read from the page images of the 1884–99 tables, pdf 101)',kind='primary'),
 dict(g='wic',y=1888,pop=338,raw='Wichita 165 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Tehuacana 143 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Waco 30 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='ynk',y=1888,pop=1837,raw='Yankton Sioux 1,837 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1888, population table, p. 414 (read from the page images of the 1884–99 tables, pdf 99)',kind='primary'),
 dict(g='ari',y=1889,pop=454,raw='Arickaree 454 (Fort Berthold Agency c, Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g='ars',y=1889,pop=1272,raw='Arapaho 1,272 (Cheyenne and Arapahoe Agency, Indian Territory)',basis='census',loc='inferred',at=(35.6, -98.09),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='chn',y=1889,pop=1424,raw='Cheyenne (northern) 557 (Pine Ridge Agency, Dakota); Northern Cheyenne 867 (Tongue River Agency, Montana)',basis='census',loc='inferred',at=(45.51, -106.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498, p. 504 (read from the page images of the 1884–99 tables, pdf 120, 126)',kind='primary'),
 dict(g='chs',y=1889,pop=2229,raw='Cheyenne 2,229 (Cheyenne and Arapahoe Agency, Indian Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1889,pop=2456,raw='Crow 2,456 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.37, -107.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 504 (read from the page images of the 1884–99 tables, pdf 126)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1889,pop=1590,raw='Comanche 1,590 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.68, -98.46),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='hid',y=1889,pop=495,raw='Gros Ventre 495 (Fort Berthold Agency c, Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g='hnk',y=1889,pop=1738,raw='Hunkpapa Sioux 1,738 (Standing Rock Agency, Dakota) (a digit uncertain in the print)',basis='census',loc='inferred',at=(46.12, -100.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='jic',y=1889,pop=801,raw='Jicarilla Apache, Olleros 300 (Southern Ute Agency, Colorado); Jicarilla Apache, Llañeros 501 (Southern Ute Agency, Colorado)',basis='census',loc='inferred',at=(36.95, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g='kap',y=1889,pop=349,raw='Apache 349 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -98.44),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='kaw',y=1889,pop=200,raw='Kansas 200 (Osage Agency, Indian Territory)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='kit',y=1889,pop=62,raw='Keechee 62 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='man',y=1889,pop=246,raw='Mandan 246 (Fort Berthold Agency c, Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1889,pop=1130,raw='Santee Sioux at Flandreau, Dak 280 (Santee and Flandreau Agency, Nebraska); Santee Sioux 850 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 504 (read from the page images of the 1884–99 tables, pdf 126)',kind='primary'),
 dict(g='ogl',y=1889,pop=4552,raw='Ogalalla Sioux 4,552 (Pine Ridge Agency, Dakota)',basis='census',loc='inferred',at=(43.03, -102.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g='oma',y=1889,pop=1137,raw='Omaha 1,137 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 504 (read from the page images of the 1884–99 tables, pdf 126)',kind='primary'),
 dict(g='oto',y=1889,pop=320,raw='Otoe and Missouria 320 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='pon',y=1889,pop=757,raw='Ponca 533 (Ponca, Pawnee, and Otoe Agency, Indian Territory); Ponca of Dakota 224 (Santee and Flandreau Agency, Nebraska)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500, p. 504 (read from the page images of the 1884–99 tables, pdf 122, 126)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1889,pop=851,raw='Pawnee 851 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='sih',y=1889,pop=545,raw='Blackfeet Sioux 545 (Standing Rock Agency, Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1889,pop=1487,raw='Sisseton and Wahpeton Sioux 1,487 (Sisseton Agency, Dakota)',basis='census',loc='inferred',at=(45.68, -97.17),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 498 (read from the page images of the 1884–99 tables, pdf 120)',kind='primary'),
 dict(g='tkw',y=1889,pop=76,raw='Tonkawa 76 (Ponca, Pawnee, and Otoe Agency, Indian Territory)',basis='census',loc='inferred',at=(36.66, -97.32),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='wic',y=1889,pop=338,raw='Wichita 164 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Tehuacana 145 (Kiowa, Comanche, and Wichita Agency, Indian Territory); Waco 29 (Kiowa, Comanche, and Wichita Agency, Indian Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='ynk',y=1889,pop=1760,raw='Yankton Sioux 1,760 (Yankton Agency, Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1889, population table, p. 500 (read from the page images of the 1884–99 tables, pdf 122)',kind='primary'),
 dict(g='ars',y=1891,pop=1137,raw='Arapaho 1,137 (Cheyenne and Arapaho Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g='chs',y=1891,pop=2132,raw='Cheyenne 2,132 (Cheyenne and Arapaho Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1891,pop=2214,raw='Crow 2,214 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.4, -107.69),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 78 (read from the page images of the 1884–99 tables, pdf 145)',kind='primary'),
 dict(g='iow',y=1891,pop=264,raw='Iowa 158 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 106 (Sac and Fox Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 76, p. 82 (read from the page images of the 1884–99 tables, pdf 143, 149)',kind='primary'),
 dict(g='kaw',y=1891,pop=196,raw='Kansas 196 (Osage Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g='kit',y=1891,pop=66,raw='Keechie 66 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1891,pop=1203,raw='Santeee Sioux 894 (Santee Agency, Nebraska); Santee Sioux at Flandreau 309 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 78 (read from the page images of the 1884–99 tables, pdf 145)',kind='primary'),
 dict(g='oto',y=1891,pop=377,raw='Otoe and Missouria 377 (Ponca, Pawnee, and Otoe Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g='sih',y=1891,pop=602,raw='Blackfeet Sioux 602 (Standing Rock Agency, North Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 80 (read from the page images of the 1884–99 tables, pdf 147)',kind='primary'),
 dict(g='wic',y=1891,pop=360,raw='Wichita 175 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory); Wacoe 35 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory); Towaconie 150 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1891, population table, p. 82 (read from the page images of the 1884–99 tables, pdf 149)',kind='primary'),
 dict(g='ari',y=1892,pop=416,raw='Arickaree 416 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g='ass',y=1892,pop=1560,raw='Assinaboine 859 (Fort Belknap Agency, Montana); Assinaboine 701 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.48),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 788 (read from the page images of the 1884–99 tables, pdf 165)',kind='primary'),
 dict(g='chn',y=1892,pop=1320,raw='Northern Cheyenne 1,200 (Tongue River Agency, Montana); Northern Cheyenne 120 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 790, p. 796 (read from the page images of the 1884–99 tables, pdf 167, 173)',kind='primary'),
 dict(g='chs',y=1892,pop=2119,raw='Cheyenne 2,119 (Cheyenne and Arapaho Agencies, Oklahoma Territory)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1892,pop=2202,raw='Crow 2,202 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.41, -107.68),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 788 (read from the page images of the 1884–99 tables, pdf 165)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1892,pop=1541,raw='Comanche 10 (Mescalero Agency, New Mexico); Comanche 1,531 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(34.68, -98.48),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 790, p. 792 (read from the page images of the 1884–99 tables, pdf 167, 169)',kind='primary'),
 dict(g='gv',y=1892,pop=718,raw='Gros Ventre 718 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 788 (read from the page images of the 1884–99 tables, pdf 165)',kind='primary'),
 dict(g='hid',y=1892,pop=453,raw='Gros Ventre 453 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g='hnk',y=1892,pop=1496,raw='Hunkpapa Sioux 1,496 (Standing Rock Agency, North Dakota)',basis='census',loc='inferred',at=(46.12, -100.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g='iow',y=1892,pop=260,raw='Iowa 159 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 101 (Sac and Fox Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 788, p. 794 (read from the page images of the 1884–99 tables, pdf 165, 171)',kind='primary'),
 dict(g='jic',y=1892,pop=842,raw='Jicarilla Apache 842 (Pueblo Agency, New Mexico)',basis='census',loc='inferred',at=(36.94, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 790 (read from the page images of the 1884–99 tables, pdf 167)',kind='primary'),
 dict(g='kaw',y=1892,pop=209,raw='Kansas 209 (Osage Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 794 (read from the page images of the 1884–99 tables, pdf 171)',kind='primary'),
 dict(g='kit',y=1892,pop=54,raw='Keechi 54 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g='man',y=1892,pop=245,raw='Mandan 245 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1892,pop=1222,raw='Santee Sioux 915 (Santee Agency, Nebraska); Santee Sioux of Flandreau 307 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 790 (read from the page images of the 1884–99 tables, pdf 167)',kind='primary'),
 dict(g='ogl',y=1892,pop=4493,raw='Ogalalla Sioux 4,493 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(43.03, -102.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 796 (read from the page images of the 1884–99 tables, pdf 173)',kind='primary'),
 dict(g='oma',y=1892,pop=1186,raw='Omaha 1,186 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 790 (read from the page images of the 1884–99 tables, pdf 167)',kind='primary'),
 dict(g=['osg', 'osl'],y=1892,pop=1608,raw='Osage 1,608 (Osage Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 794 (read from the page images of the 1884–99 tables, pdf 171)',kind='primary'),
 dict(g='oto',y=1892,pop=362,raw='Otoe and Missouri 362 (Ponca, Pawnee, and Otoe Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 794 (read from the page images of the 1884–99 tables, pdf 171)',kind='primary'),
 dict(g='sho',y=1892,pop=890,raw='Shoshone 890 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.66),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 800 (read from the page images of the 1884–99 tables, pdf 177)',kind='primary'),
 dict(g='sih',y=1892,pop=609,raw='Blackfeet Sioux 609 (Standing Rock Agency, North Dakota)',basis='census',loc='inferred',at=(45.6, -100.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1892,pop=1831,raw='Sisseton and Wahpeton Sioux 1,831 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.69, -97.17),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 796 (read from the page images of the 1884–99 tables, pdf 173)',kind='primary'),
 dict(g='tkw',y=1892,pop=66,raw='Tonkawa 66 (Ponca, Pawnee, and Otoe Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 794 (read from the page images of the 1884–99 tables, pdf 171)',kind='primary'),
 dict(g='wic',y=1892,pop=325,raw='Wichita 151 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory); Towaconie 133 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory); Waco 41 (Kiowa, Comanche, and Wichita Agency, Oklahoma Territory)',basis='census',loc='inferred',at=(34.78, -97.95),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 792 (read from the page images of the 1884–99 tables, pdf 169)',kind='primary'),
 dict(g='ynk',y=1892,pop=1715,raw='Yankton Sioux 1,715 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1892, population table, p. 796 (read from the page images of the 1884–99 tables, pdf 173)',kind='primary'),
 dict(g='ari',y=1894,pop=426,raw='Arickaree 426 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='arn',y=1894,pop=838,raw='Northern Arapaho 838 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.99, -108.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 582 (read from the page images of the 1884–99 tables, pdf 196)',kind='primary'),
 dict(g='ars',y=1894,pop=1020,raw='Arapaho 1,020 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='ass',y=1894,pop=1492,raw='Assinaboine 782 (Fort Belknap Agency, Montana); Assinaboine 710 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.48),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 186)',kind='primary'),
 dict(g='chn',y=1894,pop=1301,raw='Northern Cheyenne 1,227 (Tongue River Agency, Montana); Cheyenne 74 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 574, p. 580 (read from the page images of the 1884–99 tables, pdf 188, 194)',kind='primary'),
 dict(g='chs',y=1894,pop=2056,raw='Cheyenne 2,056 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1894,pop=2126,raw='Crow 2,126 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.44, -107.64),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 186)',kind='primary'),
 dict(g='gv',y=1894,pop=645,raw='Gros Ventre 645 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 186)',kind='primary'),
 dict(g='hid',y=1894,pop=468,raw='Gros Ventre 468 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='iow',y=1894,pop=266,raw='Iowa 179 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 87 (Sac and Fox Agency, Oklahoma)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 572, p. 578 (read from the page images of the 1884–99 tables, pdf 186, 192)',kind='primary'),
 dict(g='kaw',y=1894,pop=218,raw='Kaw 218 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='man',y=1894,pop=253,raw='Mandan 253 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1894,pop=1266,raw='Santee Sioux 964 (Santee Agency, Nebraska); Santee Sioux, of Flandreau 302 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 188)',kind='primary'),
 dict(g='oma',y=1894,pop=1170,raw='Omaha 1,170 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 188)',kind='primary'),
 dict(g=['osg', 'osl'],y=1894,pop=1656,raw='Osage 1,656 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='oto',y=1894,pop=340,raw='Otoe and Missouria 340 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='pon',y=1894,pop=793,raw='Ponca in Nebraska a 205 (Santee Agency, Nebraska); Ponca 588 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 574, p. 576 (read from the page images of the 1884–99 tables, pdf 188, 190)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1894,pop=731,raw='Pawnee 731 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='sho',y=1894,pop=927,raw='Shoshone (or Snake) 927 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.01, -108.71),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 582 (read from the page images of the 1884–99 tables, pdf 196)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1894,pop=1859,raw='Sisseton and Wahpeton Sioux 1,859 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.7, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 580 (read from the page images of the 1884–99 tables, pdf 194)',kind='primary'),
 dict(g='tkw',y=1894,pop=57,raw='Tonkawa 57 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 190)',kind='primary'),
 dict(g='ynk',y=1894,pop=1738,raw='Yankton Sioux 1,738 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1894, population table, p. 580 (read from the page images of the 1884–99 tables, pdf 194)',kind='primary'),
 dict(g='arn',y=1895,pop=837,raw='Northern Arapaho 837 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.99, -108.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 580 (read from the page images of the 1884–99 tables, pdf 219)',kind='primary'),
 dict(g='ars',y=1895,pop=1032,raw='Arapaho 1,032 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='chn',y=1895,pop=1359,raw='Northern Cheyenne 1,333 (Tongue River Agency, Montana); Cheyenne 26 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 570, p. 576 (read from the page images of the 1884–99 tables, pdf 209, 215)',kind='primary'),
 dict(g='chs',y=1895,pop=2046,raw='Cheyenne 2,046 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1895,pop=2133,raw='Crow 2,133 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.45, -107.63),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 207)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1895,pop=1507,raw='Comanche 1,507 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.68, -98.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='hid',y=1895,pop=481,raw='Gros Ventre 481 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='iow',y=1895,pop=262,raw='Iowa 167 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 95 (Sac and Fox Agency, Oklahoma)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 568, p. 574 (read from the page images of the 1884–99 tables, pdf 207, 213)',kind='primary'),
 dict(g='jic',y=1895,pop=845,raw='Jicarilla Apache 845 (Pueblo Agency, New Mexico)',basis='census',loc='inferred',at=(36.9, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 570 (read from the page images of the 1884–99 tables, pdf 209)',kind='primary'),
 dict(g='kap',y=1895,pop=226,raw='Apache 226 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(35.08, -98.48),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='kaw',y=1895,pop=208,raw='Kaw 208 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 213)',kind='primary'),
 dict(g='kio',y=1895,pop=1037,raw='Kiowa 1,037 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.99, -98.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='kit',y=1895,pop=453,raw='Keechie / Delaware / Towaconie / Waco / Wichita 453 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(35.1, -98.3),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g='man',y=1895,pop=265,raw='Mandan 265 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 572 (read from the page images of the 1884–99 tables, pdf 211)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1895,pop=1288,raw='Santee Sioux 980 (Santee Agency, Nebraska); Santee Sioux of Flandreau 308 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 570 (read from the page images of the 1884–99 tables, pdf 209)',kind='primary'),
 dict(g='oma',y=1895,pop=1182,raw='Omaha 1,182 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 570 (read from the page images of the 1884–99 tables, pdf 209)',kind='primary'),
 dict(g=['osg', 'osl'],y=1895,pop=1657,raw='Osage 1,657 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 213)',kind='primary'),
 dict(g='oto',y=1895,pop=348,raw='Otoe and Missouria 348 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 213)',kind='primary'),
 dict(g='pon',y=1895,pop=798,raw='Ponca in Nebraska 211 (Santee Agency, Nebraska); Ponca 587 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 570, p. 574 (read from the page images of the 1884–99 tables, pdf 209, 213)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1895,pop=710,raw='Pawnee 710 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 213)',kind='primary'),
 dict(g='sho',y=1895,pop=911,raw='Shoshone (or Snake) 911 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.01, -108.73),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 580 (read from the page images of the 1884–99 tables, pdf 219)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1895,pop=1863,raw='Sisseton and Wahpeton Sioux 1,863 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.7, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 215)',kind='primary'),
 dict(g='tkw',y=1895,pop=56,raw='Tonkawa 56 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 574 (read from the page images of the 1884–99 tables, pdf 213)',kind='primary'),
 dict(g='ynk',y=1895,pop=1735,raw='Yankton Sioux 1,735 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1895, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 215)',kind='primary'),
 dict(g='ari',y=1896,pop=422,raw='Arickaree 422 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='arn',y=1896,pop=856,raw='Northern Arapaho 856 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.99, -108.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 534 (read from the page images of the 1884–99 tables, pdf 238)',kind='primary'),
 dict(g='ars',y=1896,pop=1005,raw='Arapaho 1,005 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='ass',y=1896,pop=1386,raw='Assinniboine 687 (Fort Belknap Agency, Montana); Assinniboine 699 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 524 (read from the page images of the 1884–99 tables, pdf 228)',kind='primary'),
 dict(g='chn',y=1896,pop=1468,raw='Northern Cheyenne 1,341 (Tongue River Agency, Montana); Northern Cheyenne 127 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 524, p. 530 (read from the page images of the 1884–99 tables, pdf 228, 234)',kind='primary'),
 dict(g='chs',y=1896,pop=2063,raw='Cheyenne 2,063 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1896,pop=2135,raw='Crow 2,135 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.47, -107.61),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 524 (read from the page images of the 1884–99 tables, pdf 228)',kind='primary'),
 dict(g='gv',y=1896,pop=596,raw='Gros Ventre 596 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 524 (read from the page images of the 1884–99 tables, pdf 228)',kind='primary'),
 dict(g='hid',y=1896,pop=456,raw='Gros Ventre 456 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='iow',y=1896,pop=271,raw='Iowa 174 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 97 (Sac and Fox Agency, Oklahoma)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 522, p. 528 (read from the page images of the 1884–99 tables, pdf 226, 232)',kind='primary'),
 dict(g='jic',y=1896,pop=853,raw='Jicarilla Apache 853 (Pueblo Agency, New Mexico)',basis='census',loc='inferred',at=(36.88, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 526 (read from the page images of the 1884–99 tables, pdf 230)',kind='primary'),
 dict(g='kaw',y=1896,pop=207,raw='Kaw 207 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='man',y=1896,pop=262,raw='Mandan 262 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1896,pop=1279,raw='Santee Sioux of Flandreau 297 (Santee Agency, Nebraska); Santee Sioux 982 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 526 (read from the page images of the 1884–99 tables, pdf 230)',kind='primary'),
 dict(g='ogl',y=1896,pop=5470,raw='Ogalalla Sioux 5,470 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(43.03, -102.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 530 (read from the page images of the 1884–99 tables, pdf 234)',kind='primary'),
 dict(g='oma',y=1896,pop=1158,raw='Omaha 1,158 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 524 (read from the page images of the 1884–99 tables, pdf 228)',kind='primary'),
 dict(g=['osg', 'osl'],y=1896,pop=1716,raw='Osage 1,716 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='oto',y=1896,pop=354,raw='Otoe and Missouria 354 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='pon',y=1896,pop=810,raw='Ponca in Nebraska 214 (Santee Agency, Nebraska); Ponca 596 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 526, p. 528 (read from the page images of the 1884–99 tables, pdf 230, 232)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1896,pop=702,raw='Pawnee 702 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='sho',y=1896,pop=890,raw='Shoshone (or Snake) 890 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.02, -108.75),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 534 (read from the page images of the 1884–99 tables, pdf 238)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1896,pop=1867,raw='Sisseton and Wahpeton Sioux 1,867 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.71, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 532 (read from the page images of the 1884–99 tables, pdf 236)',kind='primary'),
 dict(g='tkw',y=1896,pop=55,raw='Tonkawa 55 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 528 (read from the page images of the 1884–99 tables, pdf 232)',kind='primary'),
 dict(g='ynk',y=1896,pop=1757,raw='Yankton Sioux 1,757 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1896, population table, p. 532 (read from the page images of the 1884–99 tables, pdf 236)',kind='primary'),
 dict(g='ari',y=1897,pop=424,raw='Arickaree 424 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='arn',y=1897,pop=815,raw='Northern Arapaho 815 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.99, -108.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 496 (read from the page images of the 1884–99 tables, pdf 259)',kind='primary'),
 dict(g='ass',y=1897,pop=1413,raw='Assinniboine 711 (Fort Belknap Agency, Montana); Assinniboine 702 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 486 (read from the page images of the 1884–99 tables, pdf 249)',kind='primary'),
 dict(g='chn',y=1897,pop=1379,raw='Northern Cheyenne 1,330 (Tongue River Agency, Montana); Cheyenne 49 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 486, p. 492 (read from the page images of the 1884–99 tables, pdf 249, 255)',kind='primary'),
 dict(g='chs',y=1897,pop=2089,raw='Cheyenne 2,089 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1897,pop=2139,raw='Crow 2,139 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.48, -107.59),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 486 (read from the page images of the 1884–99 tables, pdf 249)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1897,pop=1526,raw='Comanche 1,526 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.69, -98.5),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='gv',y=1897,pop=594,raw='Gros Ventre 594 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 486 (read from the page images of the 1884–99 tables, pdf 249)',kind='primary'),
 dict(g='hid',y=1897,pop=469,raw='Gros Ventre 469 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.91),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='iow',y=1897,pop=262,raw='Iowa 176 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 86 (Sac and Fox Agency, Oklahoma)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 484, p. 490 (read from the page images of the 1884–99 tables, pdf 247, 253)',kind='primary'),
 dict(g='jic',y=1897,pop=841,raw='Jicarilla Apache 841 (Pueblo Agency, New Mexico)',basis='census',loc='inferred',at=(36.87, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 488 (read from the page images of the 1884–99 tables, pdf 251)',kind='primary'),
 dict(g='kap',y=1897,pop=197,raw='Apache 197 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(35.09, -98.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='kaw',y=1897,pop=208,raw='Kaw 208 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='kio',y=1897,pop=1105,raw='Kiowa 1,105 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.99, -98.7),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='man',y=1897,pop=267,raw='Mandan 267 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.56, -101.89),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1897,pop=1281,raw='Santee Sioux 988 (Santee Agency, Nebraska); Santee Sioux of Flandreau 293 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 488 (read from the page images of the 1884–99 tables, pdf 251)',kind='primary'),
 dict(g='oma',y=1897,pop=1170,raw='Omaha 1,170 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 486 (read from the page images of the 1884–99 tables, pdf 249)',kind='primary'),
 dict(g=['osg', 'osl'],y=1897,pop=1729,raw='Osage 1,729 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='oto',y=1897,pop=350,raw='Otoe and Missouria 350 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='pon',y=1897,pop=816,raw='Ponca, in Nebraska 214 (Santee Agency, Nebraska); Ponca 602 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 488, p. 490 (read from the page images of the 1884–99 tables, pdf 251, 253)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1897,pop=710,raw='Pawnee 710 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='sho',y=1897,pop=872,raw='Shoshone (or Snake) 872 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.02, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 496 (read from the page images of the 1884–99 tables, pdf 259)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1897,pop=1869,raw='Sisseton and Wahpeton Sioux 1,869 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.71, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 494 (read from the page images of the 1884–99 tables, pdf 257)',kind='primary'),
 dict(g='tkw',y=1897,pop=53,raw='Tonkawa 53 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 490 (read from the page images of the 1884–99 tables, pdf 253)',kind='primary'),
 dict(g='ynk',y=1897,pop=1728,raw='Yankton Sioux 1,728 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1897, population table, p. 494 (read from the page images of the 1884–99 tables, pdf 257)',kind='primary'),
 dict(g='ari',y=1898,pop=426,raw='Arickaree 426 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.58, -101.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g='arn',y=1898,pop=829,raw='Northern Arapaho 829 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(42.99, -108.57),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 614 (read from the page images of the 1884–99 tables, pdf 280)',kind='primary'),
 dict(g='ars',y=1898,pop=1011,raw='Arapaho 1,011 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.6, -98.1),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g='ass',y=1898,pop=1376,raw='Assinniboine 716 (Fort Belknap Agency, Montana); Assinniboine 660 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604 (read from the page images of the 1884–99 tables, pdf 270)',kind='primary'),
 dict(g='chn',y=1898,pop=1405,raw='Northern Cheyenne 1,349 (Tongue River Agency, Montana); Cheyenne 56 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604, p. 610 (read from the page images of the 1884–99 tables, pdf 270, 276)',kind='primary'),
 dict(g='chs',y=1898,pop=2069,raw='Cheyenne 2,069 (Cheyenne and Arapaho Agency, Oklahoma)',basis='census',loc='inferred',at=(35.55, -98.0),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1898,pop=2003,raw='Crow 2,003 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.5, -107.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 602 (read from the page images of the 1884–99 tables, pdf 268)',kind='primary'),
 dict(g=['cyy', 'cyk', 'cyp', 'cyn', 'cyq'],y=1898,pop=1553,raw='Comanche 1,553 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.69, -98.51),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g='gv',y=1898,pop=574,raw='Gros Ventre 574 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604 (read from the page images of the 1884–99 tables, pdf 270)',kind='primary'),
 dict(g='iow',y=1898,pop=289,raw='Iowa 200 (Pottawatomie and Great Nemaha Agency, Kansas); Iowa 89 (Sac and Fox Agency, Oklahoma)',basis='census',loc='inferred',at=(40.0, -95.45),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 602, p. 608 (read from the page images of the 1884–99 tables, pdf 268, 274)',kind='primary'),
 dict(g='jic',y=1898,pop=840,raw='Jicarilla Apache 840 (Pueblo and Jicarilla Agency, New Mexico)',basis='census',loc='inferred',at=(36.85, -106.99),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604 (read from the page images of the 1884–99 tables, pdf 270)',kind='primary'),
 dict(g='kap',y=1898,pop=193,raw='Apache 193 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(35.09, -98.43),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g='kaw',y=1898,pop=211,raw='Kaw 211 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.75, -96.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 608 (read from the page images of the 1884–99 tables, pdf 274)',kind='primary'),
 dict(g='kio',y=1898,pop=1126,raw='Kiowa 1,126 (Kiowa Agency, Oklahoma)',basis='census',loc='inferred',at=(34.99, -98.66),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g='man',y=1898,pop=253,raw='Mandan 253 (Fort Berthold Agency, North Dakota)',basis='census',loc='inferred',at=(47.5, -102.01),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 606 (read from the page images of the 1884–99 tables, pdf 272)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1898,pop=1315,raw='Santee Sioux 1,019 (Santee Agency, Nebraska); Santee Sioux of Flandreau 296 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604 (read from the page images of the 1884–99 tables, pdf 270)',kind='primary'),
 dict(g='oma',y=1898,pop=1202,raw='Omaha 1,202 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604 (read from the page images of the 1884–99 tables, pdf 270)',kind='primary'),
 dict(g=['osg', 'osl'],y=1898,pop=1761,raw='Osage 1,761 (Osage Agency, Oklahoma)',basis='census',loc='inferred',at=(36.67, -96.33),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 608 (read from the page images of the 1884–99 tables, pdf 274)',kind='primary'),
 dict(g='oto',y=1898,pop=360,raw='Otoe and Missouria 360 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.47, -97.18),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 608 (read from the page images of the 1884–99 tables, pdf 274)',kind='primary'),
 dict(g='pon',y=1898,pop=835,raw='Ponca 227 (Santee Agency, Nebraska); Ponca 608 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.68, -97.05),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 604, p. 608 (read from the page images of the 1884–99 tables, pdf 270, 274)',kind='primary'),
 dict(g=['pwc', 'pwk', 'pws'],y=1898,pop=706,raw='Pawnee 706 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.34, -96.8),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 608 (read from the page images of the 1884–99 tables, pdf 274)',kind='primary'),
 dict(g='sho',y=1898,pop=842,raw='Shoshone (or Snake) 842 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.03, -108.79),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 614 (read from the page images of the 1884–99 tables, pdf 280)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1898,pop=1871,raw='Sisseton and Wahpeton Sioux 1,871 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.72, -97.19),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 610 (read from the page images of the 1884–99 tables, pdf 276)',kind='primary'),
 dict(g='tkw',y=1898,pop=57,raw='Tonkawa 57 (Ponca, Pawnee, and Otoe Agency, Oklahoma)',basis='census',loc='inferred',at=(36.66, -97.31),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1898, population table, p. 608 (read from the page images of the 1884–99 tables, pdf 274)',kind='primary'),
 dict(g='arn',y=1899,pop=806,raw='Northern Arapahoe 806 (Shoshone Agency, Wyoming)',basis='census',loc='inferred',at=(43.0, -108.58),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 580 (read from the page images of the 1884–99 tables, pdf 297)',kind='primary'),
 dict(g='ass',y=1899,pop=1323,raw='Assinniboine 681 (Fort Belknap Agency, Montana); Assinniboine 642 (Fort Peck Agency, Montana)',basis='census',loc='inferred',at=(48.3, -106.49),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 291)',kind='primary'),
 dict(g='chn',y=1899,pop=1424,raw='Northern Cheyenne 1,363 (Tongue River Agency, Montana); Cheyenne 61 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(45.47, -106.54),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568, p. 576 (read from the page images of the 1884–99 tables, pdf 291, 293)',kind='primary'),
 dict(g=['cwm', 'cwr'],y=1899,pop=1962,raw='Crow 1,962 (Crow Agency, Montana)',basis='census',loc='inferred',at=(45.51, -107.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 291)',kind='primary'),
 dict(g='gv',y=1899,pop=619,raw='Gros Ventre 619 (Fort Belknap Agency, Montana)',basis='census',loc='inferred',at=(48.48, -108.77),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 291)',kind='primary'),
 dict(g=['mde', 'wpk'],y=1899,pop=1285,raw='Santee Sioux 998 (Santee Agency, Nebraska); Santee Sioux of Flandreau 287 (Santee Agency, Nebraska)',basis='census',loc='inferred',at=(42.83, -97.85),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 291)',kind='primary'),
 dict(g='ogl',y=1899,pop=6452,raw='Ogalalla Sioux 6,452 (Pine Ridge Agency, South Dakota)',basis='census',loc='inferred',at=(43.03, -102.56),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 293)',kind='primary'),
 dict(g='oma',y=1899,pop=1157,raw='Omaha 1,157 (Omaha and Winnebago Agency, Nebraska)',basis='census',loc='inferred',at=(42.12, -96.36),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 568 (read from the page images of the 1884–99 tables, pdf 291)',kind='primary'),
 dict(g=['sis', 'wpt'],y=1899,pop=1884,raw='Sisseton and Wahpeton Sioux 1,884 (Sisseton Agency, South Dakota)',basis='census',loc='inferred',at=(45.72, -97.19),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 293)',kind='primary'),
 dict(g='ynk',y=1899,pop=1701,raw='Yankton Sioux 1,701 (Yankton Agency, South Dakota)',basis='census',loc='inferred',at=(42.98, -98.42),r=60,src='Annual Report of the Commissioner of Indian Affairs, 1899, population table, p. 576 (read from the page images of the 1884–99 tables, pdf 293)',kind='primary'),
]
