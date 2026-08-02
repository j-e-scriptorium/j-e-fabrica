/* Territorial acquisitions of the United States, simplified: each of the 50 states
   assigned to the one acquisition its land is dominantly identified with. Not a precise
   territorial-boundary history (short-lived territories, exact border shifts, and land
   contested between more than one acquisition are not modeled) — states.json's own blurbs
   carry that nuance in prose. This just drives when a state's outline turns from blank to
   "territory" on the map; each state turns from "territory" to "state" at its own admission
   year (see states.json), independent of this file. */
var ACQUISITIONS = [
  { name: "The Thirteen Colonies", year: 1776,
    note: "Plus Kentucky and Tennessee (claimed westward from Virginia and North Carolina), and the future Maine, Vermont, and West Virginia — already inside the colonies' claims or (Vermont) contemporaneously contested, none later ceded by a foreign power.",
    states: ["CT","DE","GA","KY","MD","MA","ME","NH","NJ","NY","NC","PA","RI","SC","TN","VT","VA","WV"] },
  { name: "Northwest Territory", year: 1787,
    note: "Ceded to Congress by the states with western claims; organized under the Northwest Ordinance, which barred slavery.",
    states: ["OH","IN","IL","MI","WI"] },
  { name: "Georgia's Western Cession", year: 1802,
    note: "Georgia ceded its western land claims to Congress, forming the Mississippi Territory.",
    states: ["AL","MS"] },
  { name: "Louisiana Purchase", year: 1803,
    note: "Bought from France; roughly the Mississippi's western watershed to the Rockies.",
    states: ["LA","AR","MO","IA","MN","ND","SD","NE","KS","OK","MT","WY","CO"] },
  { name: "Florida Cession", year: 1819,
    note: "Ceded by Spain (Adams–Onís Treaty), formalizing a border Jackson had already crossed by force.",
    states: ["FL"] },
  { name: "Texas Annexation", year: 1845,
    note: "The Republic of Texas, independent since 1836, annexed by joint resolution.",
    states: ["TX"] },
  { name: "Oregon Country", year: 1846,
    note: "Divided from British joint occupation at the 49th parallel.",
    states: ["OR","WA","ID"] },
  { name: "Mexican Cession", year: 1848,
    note: "Ceded by Mexico after the Mexican–American War; includes the Gadsden Purchase strip added in 1853.",
    states: ["CA","NV","UT","AZ","NM"] },
  { name: "Alaska Purchase", year: 1867,
    note: "Bought from Russia — \"Seward's Folly.\"",
    states: ["AK"] },
  { name: "Hawaii Annexation", year: 1898,
    note: "Annexed after American planters overthrew the Hawaiian monarchy.",
    states: ["HI"] },
];
