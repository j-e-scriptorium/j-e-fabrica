# Ecological and archaeological tables used to place the extrapolation. Entries citing the Handbook of North American Indians were
# read for this build; the others are recalled from the works named and marked so.

SMITH='Smith, Like-a-Fishhook Village and Fort Berthold (1972) (recalled)'
ARIK='Swanton, The Indian Tribes of North America (1952); Meyer, The Village Indians of the Upper Missouri (1977)'
# Dated relocations of village peoples. Between two places the village holds at the first and moves at this date
# (over about five months); without a dated move it moves at the midpoint.
PARKS_P='Parks, “Pawnee”, Handbook of North American Indians 13 (2001), pp. 519–22'
NEWC='Newcomb, “Wichita”, Handbook of North American Indians 13 (2001), p. 559'
PARKS_A='Parks, “Arikara”, Handbook of North American Indians 13 (2001), pp. 366–67'
HB13P='Handbook of North American Indians 13 (2001)'
HBOM=f'Liberty, Wood, and Irwin, “Omaha”, {HB13P}, p. 401'
HBPO=f'Brown and Irwin, “Ponca”, {HB13P}, pp. 425–26'
HBIO=f'Wedel, “Iowa”, {HB13P}, pp. 434–36'
HBOT=f'Schweitzer, “Otoe and Missouria”, {HB13P}, pp. 454–56'
HBKA=f'Bailey and Young, “Kansa”, {HB13P}, pp. 464, 469–72'
HBOS=f'Bailey, “Osage”, {HB13P}, p. 478'
HBTA=f'Schneider, “Three Affiliated Tribes”, {HB13P}, pp. 393–94'
VMOVE={
 'ari':[(1823.65,'fled upriver to the Mandan villages after Leavenworth’s attack, Aug. 1823',PARKS_A),
        (1824.3,'returned to the Cottonwood Creek villages near the Grand River, spring 1824',PARKS_A),
        (1833.4,'abandoned the Grand River villages for the Skiri on the Loup, 1833',PARKS_A),
        (1835.6,'left the Loup in summer 1835 to live two years as nomadic hunters',PARKS_A),
        (1837.6,'moved into the Mandan village at Fort Clark emptied by the smallpox, 1837',PARKS_A),
        (1862.3,'joined the Hidatsa and Mandan at Like-a-Fishhook, 1862',SMITH+'; '+PARKS_A),(1884.5,'out of Like-a-Fishhook to Nishu, early 1880s; the village deserted by 1886 (date ours)',HBTA)],
 'pwc':[(1811.3,'the South Bands move from south of the Platte to the Loup beside the Skiri (Sibley, 1811)',PARKS_P),(1838.5,'the South Bands relocate north of the Platte after the 1833 treaty, into one village between Plum and Council creeks by 1841 (date ours, between 1833 and 1841)',PARKS_P),(1846.5,'Sioux attacks drive the Pawnee from the Loup to new villages south of the Platte, 1846',PARKS_P),(1859.7,'after the summer hunt of 1859, to the reservation at Genoa on the Loup',PARKS_P),(1874.9,'most of the tribe moves south to the Wichita Agency, winter 1874–75',PARKS_P),(1875.7,'to the new reservation on Black Bear Creek, Indian Territory, 1875',PARKS_P)],
 'pwk':[(1811.3,'the South Bands move from south of the Platte to the Loup beside the Skiri (Sibley, 1811)',PARKS_P),(1838.5,'the South Bands relocate north of the Platte after the 1833 treaty, into one village between Plum and Council creeks by 1841 (date ours, between 1833 and 1841)',PARKS_P),(1846.5,'Sioux attacks drive the Pawnee from the Loup to new villages south of the Platte, 1846',PARKS_P),(1859.7,'after the summer hunt of 1859, to the reservation at Genoa on the Loup',PARKS_P),(1874.9,'most of the tribe moves south to the Wichita Agency, winter 1874–75',PARKS_P),(1875.7,'to the new reservation on Black Bear Creek, Indian Territory, 1875',PARKS_P)],
 'pws':[(1846.5,'Sioux attacks drive the Pawnee from the Loup to new villages south of the Platte, 1846',PARKS_P),(1859.7,'after the summer hunt of 1859, to the reservation at Genoa on the Loup',PARKS_P),(1874.9,'most of the tribe moves south to the Wichita Agency, winter 1874–75',PARKS_P),(1875.7,'to the new reservation on Black Bear Creek, Indian Territory, 1875',PARKS_P)],
 'wic':[(1862.95,'fled to Kansas in the winter of 1862–63',NEWC),(1867.4,'returned to the Washita, 1867',NEWC)],
 'man':[(1845.4,'survivors joined the Hidatsa in founding Like-a-Fishhook village, 1845',SMITH),(1884.5,'out of Like-a-Fishhook to Charging Eagle and Red Butte, early 1880s (date ours)',HBTA)],
 'hid':[(1845.4,'founded Like-a-Fishhook village at the Fishhook bend, 1845',SMITH),(1884.5,'out of Like-a-Fishhook, across the river to Independence, early 1880s (date ours)',HBTA)],
 'mde':[(1853.6,'removed to the Lower Sioux reservation on the Minnesota River under the treaty of 1851, 1853–54','Anderson, Kinsmen of Another Kind (1984) (recalled)')],
 'oma':[(1820.3,'to the Elkhorn, by 1820 (date ours)',HBOM),(1833.6,'back to the Big Village after the Black Hawk War of 1832',HBOM),
        (1841.3,'driven out by the Teton, spring 1841, to the Little Village on the Elkhorn',HBOM+'; Fletcher & La Flesche, The Omaha Tribe (1911), p. 100'),
        (1843.3,'returned to the Big Village, spring 1843',HBOM),(1845.4,'driven out again by the Sioux, 1845, to a site west of Bellevue',HBOM),
        (1855.9,'moved from Bellevue to the Blackbird Hills reservation, winter 1855–56','Fletcher & La Flesche, The Omaha Tribe (1911) (recalled)')],
 'pon':[(1877.4,'removal to Indian Territory, a two-month trek begun in spring 1877',HBPO),(1878.4,'from the Quapaw lands to the Salt Fork, 1878',HBPO)],
 'iow':[(1765.5,'east to the mouth of the Des Moines, 1765 and after',HBIO),(1819.6,'70 miles up the Chariton after the Otoe refused them, 1819',HBIO),
        (1822.4,'to the Grand River, 1822',HBIO),(1826.5,'to the Little Platte, by 1827 (date ours)',HBIO),(1837.4,'to the Great Nemaha reservation, 1837',HBIO)],
 'oto':[(1835.5,'north of the Platte near Bellevue, half the tribe by 1836 (date ours)',HBOT),(1841.4,'village on the north bank burnt, 1841; five villages south of the Platte by 1842',HBOT),
        (1855.4,'to the Big Blue reservation, 1855',HBOT),(1881.8,'the Quaker band to Red Rock Creek, Oct. 1881 (the Coyote band went in Feb. 1880)',HBOT)],
 'mis':[(1839.5,'south of the Platte, apart from the Otoe, 1839',HBOT)],
 'kaw':[(1752.5,'to the Kansas River near its mouth, 1752',HBKA),(1830.4,'from Blue Earth Village to three villages 35 miles east, 1830',HBKA),
        (1848.4,'to the Council Grove reservation under the treaty of 1846 (villages there dated 1848–73)',HBKA),(1873.4,'to Indian Territory, 1873',HBKA+'; Unrau, The Kansa Indians (1971) (recalled)')],
 'osg':[(1871.6,'all the full bloods and most mixed bloods move to the new reservation in the Cherokee Outlet, 1871',HBOS)],
 'osl':[(1871.6,'as for the Great Osage',HBOS)],
}

# Bison range by date, outlines (lon, lat) traced by eye from Hornaday's map of the extermination (1889) and narrowed with
# Isenberg (2000) and Flores (1991). Each outline holds from its year until the next; after 1883 there is no range.
HORNADAY='Hornaday, “The Extermination of the American Bison”, Report of the U.S. National Museum for 1887 (1889), map; Isenberg, The Destruction of the Bison (2000)'
BISON=[
 (1850,[[(-114,54),(-104,54.5),(-100,52),(-99,49),(-98.5,46),(-97.5,42),(-97,38),(-97.5,34),(-99,31),(-101.5,30),(-104,31),(-105,36),(-105.5,41),(-110,42),(-112,45),(-114,49)]]),
 (1865,[[(-114,53.5),(-108,53.5),(-104,51.5),(-101.5,49),(-100,46),(-99,42),(-98.5,38),(-99,34),(-100,31.5),(-102,31),(-104,32),(-105,36),(-105.5,41),(-110,42.5),(-112,45),(-114,49)]]),
 (1870,[[(-98.8,40),(-98.6,37),(-99,34),(-100.5,32),(-102.5,32),(-104,34),(-104,38),(-102.5,40.5)],
        [(-114,53),(-108,53),(-104,51),(-102,49),(-100.5,46.5),(-100.5,44),(-103,42.5),(-107,42.5),(-110,43),(-112,45),(-114,49)]]),
 (1875,[[(-99.5,37),(-99.8,34),(-101,32.3),(-102.8,32.3),(-103.5,34),(-103,36.5),(-101,37.3)],
        [(-114,52.5),(-110,52),(-106,50.5),(-104,49),(-102,47),(-101.5,45),(-104,44),(-107,44),(-111,45),(-113,47)]]),
 (1879,[[(-111,49),(-108,49.1),(-104.5,48.8),(-103,47),(-103.5,45.5),(-106,45),(-109,45.3),(-111,46.5)]]),
 (1882,[[(-109,48),(-106,48),(-104.5,46.5),(-106,45.5),(-108.5,46)]]),
 (1884,[]),
]
