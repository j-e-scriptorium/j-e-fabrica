/* ============================================================
   THIRTY-TWO JOURNEYS — data
   leg fields: x lon, y lat, p place, d date, n note,
               c certainty (3 stated/documented, 2 inferred, 1 notional),
               t track ('m' main, 'told' narrated-within, 'pro' prologue),
               k marker kind (landfall, death, wreck, turn, told)
   voyage fields: kind ('real'/'fiction'), domain ('sea'/'land' — a river counts as land)
   ============================================================ */

var VOYAGES=[

/* ============================================================
   REAL — SEA (8)
   ============================================================ */

/* ---------------------------------------------------------- 1 */
{id:"columbus",kind:"real",domain:"sea",title:"Columbus",sub:"Santa María, Pinta, Niña",
 years:"1492–93",colour:"#c0392b",
 stat:{out:"3 ships, about 90 men",back:"2 ships; 39 left behind at La Navidad, all dead within a year",
       days:224,note:"Palos to Palos, 3 August 1492 – 15 March 1493."},
 gist:"A voyage that succeeded by being wrong. Columbus had underestimated the size of the earth by about a third, and the only reason he did not starve was that a continent he did not believe in was in the way.",
 legs:[
 {x:-6.89,y:37.23,p:"Palos de la Frontera",d:"3 Aug 1492",c:3,n:"Out over the bar at sunrise with three ships and a cosmography that was wrong in his favour."},
 {x:-17.11,y:28.09,p:"La Gomera, Canaries",d:"6 Sep 1492",c:3,n:"Nearly a month refitting the Pinta's rudder and re-rigging the Niña. The last European port for ten weeks."},
 {x:-40,y:27.5,p:"The Sargasso",d:"16 Sep 1492",c:2,n:"Weed on the surface and a steady following wind — reassuring until the crew worked out that a wind which never shifts is a wind you cannot come home against."},
 {x:-55,y:25.5,p:"False landfalls",d:"25 Sep–7 Oct 1492",c:2,n:"Cries of land three times, and nothing there. Columbus kept two reckonings, a short one for the crew and a true one for himself. The short one was the more accurate."},
 {x:-74.48,y:24.05,p:"Guanahani",d:"12 Oct 1492",c:1,k:"landfall",n:"Rodrigo de Triana saw it at two in the morning. Which island this is has been argued for two centuries: Watlings, renamed San Salvador in 1925, is the usual answer; Samana Cay and Grand Turk both have serious advocates."},
 {x:-75.13,y:23.18,p:"Fernandina (Long Island)",d:"16 Oct 1492",c:2,n:"Island-hopping and asking, in a language nobody shared, where the gold was. He was told: further on."},
 {x:-76.13,y:21.11,p:"Cuba",d:"28 Oct 1492",c:3,n:"He decided this was the Asian mainland, or possibly Cipangu, and sent an embassy inland with a letter for the Great Khan. They found people smoking rolled leaves."},
 {x:-73.38,y:19.80,p:"Hispaniola",d:"6 Dec 1492",c:3,n:"Named for its likeness to Spain. Martín Alonso Pinzón had already taken the Pinta off on his own account and would not reappear for six weeks.",v:[[-75.5,22.17]]},
 {x:-72.05,y:19.75,p:"La Navidad",d:"25 Dec 1492",c:3,k:"wreck",n:"The Santa María ran quietly aground on a reef on Christmas morning while the watch was asleep. Her timbers became a fort, and thirty-nine men were left in it."},
 {x:-60,y:33,p:"The northern return",d:"Jan–Feb 1493",c:2,n:"His one navigational masterstroke: instead of beating back against the trades he sailed north until he found the westerlies. Every returning ship for three centuries used it."},
 {x:-25.09,y:36.97,p:"Santa Maria, Azores",d:"18 Feb 1493",c:3,n:"A storm so bad he wrote an account of the voyage, sealed it in a cask and threw it overboard. Half his shore party was arrested by the Portuguese."},
 {x:-9.14,y:38.71,p:"Lisbon",d:"4 Mar 1493",c:3,n:"Blown into the wrong kingdom's river and obliged to explain himself to João II, who had turned the expedition down and now had to listen to it."},
 {x:-6.89,y:37.23,p:"Palos",d:"15 Mar 1493",c:3,n:"Home in the afternoon. The Pinta came in the same evening; Pinzón went to bed and died within the month.",v:[[-10.17,37.17],[-8.83,35.83]]}
]},

/* ---------------------------------------------------------- 2 */
{id:"magellan",kind:"real",domain:"sea",title:"Magellan–Elcano",sub:"Trinidad, San Antonio, Concepción, Victoria, Santiago",
 years:"1519–22",colour:"#8e44ad",
 stat:{out:"5 ships, about 270 men",back:"1 ship, 18 men",days:1082,
       note:"Sanlúcar to Sanlúcar, 20 September 1519 – 6 September 1522."},
 gist:"The first circumnavigation, completed by the fourth man to command it. Magellan died a third of the way round; the ship that finished was leaking so badly her crew pumped her across the Indian Ocean.",
 legs:[
 {x:-6.35,y:36.78,p:"Sanlúcar de Barrameda",d:"20 Sep 1519",c:3,n:"Five ships, a Portuguese captain in Spanish service, and a Castilian officer corps that regarded him as an enemy agent."},
 {x:-16.62,y:28.29,p:"Tenerife",d:"26 Sep 1519",c:3,n:"Where a message reached him that his Spanish captains had orders to watch him, and had discussed killing him."},
 {x:-20,y:5,p:"The doldrums",d:"Oct–Nov 1519",c:2,n:"Three weeks of calm and squall off the Guinea coast, with St Elmo's fire at the mastheads, which the crew took as a good sign."},
 {x:-43.17,y:-22.91,p:"Rio de Janeiro",d:"13 Dec 1519",c:3,n:"Thirteen days of provisioning in a harbour they were technically forbidden to enter, it being Portuguese by treaty.",v:[[-36.83,-12.5],[-39.5,-22.17],[-41.83,-24.17]]},
 {x:-56.5,y:-35.0,p:"Río de la Plata",d:"Jan 1520",c:3,n:"Explored for a fortnight in the hope it was the strait. It was a river, and Juan Díaz de Solís had already been eaten there trying the same idea.",v:[[-54.17,-36.17]]},
 {x:-67.72,y:-49.31,p:"Puerto San Julián",d:"31 Mar–24 Aug 1520",c:3,k:"death",n:"Five months wintering. A mutiny on Easter Sunday put three ships against two; Magellan won it by boarding party. Quesada was beheaded, Cartagena marooned, and the Santiago wrecked scouting south.",v:[[-55.5,-37.5],[-66.5,-49.83]]},
 {x:-68.35,y:-52.34,p:"Cabo Vírgenes",d:"21 Oct 1520",c:3,k:"landfall",n:"An opening the pilots said was a bay. He sent two ships in to check and they came back firing salutes.",v:[[-66.83,-50.17]]},
 {x:-71.0,y:-53.6,p:"The Strait",d:"Oct–Nov 1520",c:3,n:"Thirty-eight days of blind channels, tide races and fires burning on the southern shore, which is why it is called Tierra del Fuego. The San Antonio deserted here and sailed home with most of the food."},
 {x:-74.7,y:-52.9,p:"Cape Deseado",d:"28 Nov 1520",c:3,n:"Out into an ocean so unexpectedly gentle after the strait that he named it Pacific, which has misled people ever since."},
 {x:-140,y:-14,p:"The empty crossing",d:"Dec 1520–Mar 1521",c:2,n:"Ninety-eight days without fresh food. They ate sawdust, leather from the yards, and rats at half a ducat each. Pigafetta counted nineteen dead and thought the smell of the gums the worst of it. In the widest ocean on earth they found two uninhabited rocks."},
 {x:144.75,y:13.44,p:"Guam",d:"6 Mar 1521",c:3,n:"Named the Islands of Thieves after a skiff was taken, which was a Chamorro reading of hospitality rather than theft. He burned a village for it."},
 {x:125.68,y:10.75,p:"Homonhon, Samar",d:"16 Mar 1521",c:3,n:"The Philippines. Enrique, Magellan's Malay slave taken a decade earlier at Malacca, was understood by the people who came out to the ship — the moment the circle closed, if you count it his way."},
 {x:123.89,y:10.32,p:"Cebu",d:"7 Apr 1521",c:3,n:"An alliance, a mass baptism of some eight hundred people, and a promise to settle a local quarrel by force."},
 {x:124.02,y:10.31,p:"Mactan",d:"27 Apr 1521",c:3,k:"death",n:"Magellan waded ashore with about forty-nine men against Lapulapu's several hundred, having declined native allies to make the demonstration purer. He was speared in the shallows and his body was not given up."},
 {x:114.94,y:4.89,p:"Brunei",d:"Jul 1521",c:3,n:"Down to two ships — the Concepción had been burned for want of men to sail her — and six months of wandering the archipelago, part trade, part piracy."},
 {x:127.40,y:0.69,p:"Tidore, Moluccas",d:"8 Nov 1521",c:3,k:"landfall",n:"The Spice Islands, the entire point of the voyage. Cloves at last, and enough of them to pay for the expedition several times over.",v:[[114.5,5.17],[116.83,9.17],[123.17,2.83],[127.17,1.17]]},
 {x:125.0,y:-9.5,p:"Timor",d:"Feb 1522",c:3,n:"The Trinidad stayed behind leaking and tried to recross the Pacific; she failed, and her men were taken by the Portuguese. Elcano took the Victoria west, into waters where being caught meant hanging.",v:[[127.17,1.17],[125.83,-0.17],[126.83,-2.17],[125.5,-5.17],[127.5,-9.5],[125.5,-9.5]]},
 {x:80,y:-35,p:"The Indian Ocean",d:"Mar–May 1522",c:2,n:"Elcano kept far south to avoid Portuguese patrols and paid for it in weather. Twenty-one men died. The cargo of cloves was never touched, because it was the only asset they had."},
 {x:18.47,y:-34.36,p:"Cape of Good Hope",d:"6 May 1522",c:3,n:"Nine weeks trying to round it, the ship pumping constantly, the foremast gone."},
 {x:-23.51,y:15.0,p:"Cape Verde",d:"9 Jul 1522",c:3,n:"They had to put in for food and pretend they were coming from America. The lie held until someone paid for provisions with cloves. Thirteen men were seized ashore."},
 {x:-6.35,y:36.78,p:"Sanlúcar",d:"6 Sep 1522",c:3,n:"Eighteen men, too weak to walk, worked the ship up the river. They had kept a careful log and it was a day out — the first proof that going west round the world costs you a date."}
]},

/* ---------------------------------------------------------- 3 */
{id:"gama",kind:"real",domain:"sea",title:"Vasco da Gama",sub:"São Gabriel, São Rafael, Bérrio, and a store ship",
 years:"1497–99",colour:"#16a085",
 stat:{out:"4 ships, about 170 men",back:"2 ships, about 55 men",days:790,
       note:"Lisbon, 8 July 1497 – Lisbon, late summer 1499."},
 gist:"The first sea route from Europe to India, opened by a man whose diplomatic method was to bombard the place he wanted to trade with. The outbound Atlantic arc — ninety-odd days out of sight of land — is the real feat.",
 legs:[
 {x:-9.20,y:38.69,p:"Belém, Lisbon",d:"8 Jul 1497",c:3,n:"Four ships fitted for two years, after a decade of Portuguese probing down the African coast had established roughly where the continent ended."},
 {x:-15.6,y:28.0,p:"Canaries",d:"15 Jul 1497",c:3,n:"Passed in fog without stopping."},
 {x:-23.6,y:15.0,p:"São Tiago, Cape Verde",d:"26 Jul 1497",c:3,n:"The last provisioning. Then he did the thing nobody had done."},
 {x:-28,y:-8,p:"The great arc",d:"Aug–Oct 1497",c:2,n:"Instead of creeping down the African coast against the current, he stood far out into the south Atlantic to pick up the westerlies — a wide loop through open ocean, ninety-three days without sight of land, three times what Columbus endured."},
 {x:18.03,y:-32.75,p:"St Helena Bay",d:"4 Nov 1497",c:3,k:"landfall",n:"They came in almost exactly where they meant to, which given the instruments is the most impressive number in this whole atlas. A scuffle on the beach; da Gama took a spear in the leg."},
 {x:18.47,y:-34.36,p:"Cape of Good Hope",d:"22 Nov 1497",c:3,n:"Four days of trying, then round. The store ship was broken up and burned on the far side."},
 {x:22.14,y:-34.18,p:"Mossel Bay",d:"Dec 1497",c:3,n:"Trading bracelets for an ox, and a padrão set up which the locals pulled down as soon as the ships left.",v:[[19.5,-36.17]]},
 {x:36.89,y:-17.88,p:"Rio dos Bons Sinais",d:"Jan 1498",c:3,n:"The River of Good Omens, so called because the people on it wore cotton and knew about ships from the north. Scurvy took thirty men here.",v:[[26.5,-35.17],[32.17,-30.5],[36.83,-24.17]]},
 {x:40.73,y:-15.03,p:"Mozambique",d:"2 Mar 1498",c:3,n:"An Indian Ocean world of Arab and Swahili trade that had been running for centuries and had no use for Portuguese cloth. He left under fire, and shelled the town on the way out.",v:[[39.83,-17.83]]},
 {x:39.67,y:-4.05,p:"Mombasa",d:"7 Apr 1498",c:3,n:"A trap, or he believed it was, and he tortured two prisoners with boiling oil to find out.",v:[[41.83,-8.5]]},
 {x:40.12,y:-3.22,p:"Malindi",d:"14 Apr 1498",c:3,k:"turn",n:"Here he got what he actually needed: a pilot who knew the monsoon. Portuguese tradition made him Ibn Majid, the great Arab navigator; the evidence for that is thin, and he was more likely a Gujarati."},
 {x:75.78,y:11.25,p:"Calicut",d:"20 May 1498",c:3,k:"landfall",n:"Twenty-three days across the Arabian Sea. The gifts he had brought for the Zamorin — striped cloth, hats, sugar, honey — were laughed at by the customs officials, who asked why he had not brought gold."},
 {x:74.05,y:14.75,p:"Anjediva",d:"Oct 1498",c:3,n:"He left in August against the monsoon and took three months to cross back, against twenty-three days coming. Half the crew died of scurvy; there were not enough men left to sail three ships.",v:[[73.5,12.5]]},
 {x:40.12,y:-3.22,p:"Malindi",d:"7 Jan 1499",c:3,n:"The São Rafael was burned here for want of hands."},
 {x:18.47,y:-34.36,p:"Cape of Good Hope",d:"20 Mar 1499",c:3,n:"Round again, in a fair wind, with two ships.",v:[[42.17,-15.17],[36.83,-20.83],[36.83,-24.17],[33.83,-28.5],[24.83,-35.83],[19.5,-36.17]]},
 {x:-9.20,y:38.69,p:"Lisbon",d:"Aug–Sep 1499",c:2,n:"The Bérrio got in first, in July; da Gama stopped at the Azores to bury his brother and came in weeks later. The cargo paid for the voyage sixty times over, and the Indian Ocean stopped being anybody else's.",v:[[16.5,-33.17],[10.5,-17.83],[-18.17,12.5],[-19.17,28.83]]}
]},

/* ---------------------------------------------------------- 4 */
{id:"cook",kind:"real",domain:"sea",title:"Cook's Endeavour",sub:"HM Bark Endeavour",
 years:"1768–71",colour:"#2980b9",
 stat:{out:"94 aboard",back:"about 56; 38 dead, almost all of dysentery and malaria caught at Batavia",days:1051,
       note:"Plymouth, 26 August 1768 – the Downs, 12 July 1771."},
 gist:"A Whitby collier sent to the Pacific to watch Venus cross the sun, carrying sealed orders to look for a continent afterwards. Cook did not find the continent, because it was not there, and proved it by looking.",
 legs:[
 {x:-4.14,y:50.37,p:"Plymouth",d:"26 Aug 1768",c:3,n:"A flat-bottomed coal ship, chosen because she could take the ground without breaking, which later saved everyone's life."},
 {x:-16.92,y:32.65,p:"Madeira",d:"13 Sep 1768",c:3,n:"Wine and onions. A seaman drowned taking the anchor buoy."},
 {x:-43.17,y:-22.91,p:"Rio de Janeiro",d:"13 Nov 1768",c:3,n:"The viceroy refused to believe a ship this small was on a scientific voyage and assumed smuggling. Banks had to botanise by sending servants ashore for salad.",v:[[-23.5,20.5],[-26.83,17.17],[-26.83,13.17],[-33.17,-0.17],[-33.5,-8.17],[-37.5,-13.5],[-39.5,-22.17],[-41.83,-24.17]]},
 {x:-65.18,y:-54.82,p:"Bay of Good Success",d:"15 Jan 1769",c:3,k:"death",n:"Banks took a party up into the hills; a snowstorm caught them and two of his black servants, Thomas Richmond and George Dorlton, died in the night."},
 {x:-67.28,y:-55.98,p:"Cape Horn",d:"25 Jan 1769",c:3,n:"Round in a fortnight and easily, which Cook noted was luck and warned others not to expect.",v:[[-64.17,-53.5],[-62.83,-54.5],[-63.83,-56.17]]},
 {x:-149.49,y:-17.50,p:"Matavai Bay, Tahiti",d:"13 Apr 1769",c:3,k:"landfall",n:"Three months ashore at Fort Venus. Cook's standing orders about behaviour towards the Tahitians were the most humane written by any European commander of the century and were broken within a week."},
 {x:-149.49,y:-17.50,p:"The transit",d:"3 Jun 1769",c:3,k:"turn",n:"A clear day, three observing stations, and the black-drop effect blurring every contact time so badly that the results were nearly useless. The whole point of the voyage, and it half failed."},
 {x:-151.45,y:-16.82,p:"Raiatea",d:"Jul–Aug 1769",c:3,n:"Tupaia came aboard here: a priest and navigator who could name some seventy islands and draw a chart of them, and whose knowledge Cook used without ever quite crediting."},
 {x:-147,y:-40,p:"South to 40°",d:"Sep 1769",c:3,n:"The sealed orders: find the Great Southern Continent. He went down to forty degrees, found nothing but sea, and turned west."},
 {x:178.03,y:-38.68,p:"Poverty Bay, New Zealand",d:"6 Oct 1769",c:3,k:"landfall",n:"The first contact went wrong within hours and several Māori were shot. Cook named the bay for what it failed to give him, and afterwards was more careful, and it kept happening anyway."},
 {x:174.0,y:-41.1,p:"Queen Charlotte Sound",d:"Jan 1770",c:3,n:"Six months charting both islands, over 2,400 miles of coast, with an accuracy still visible on a modern chart. He settled that New Zealand was not part of any continent.",v:[[178.17,-38.83],[176.5,-41.83],[174.17,-41.17]]},
 {x:151.22,y:-34.00,p:"Botany Bay",d:"29 Apr 1770",c:3,k:"landfall",n:"Two Gweagal men stood on the beach and refused to move aside for a landing party of forty. Cook fired birdshot at their legs. Banks collected so many plants the bay was renamed for them."},
 {x:145.62,y:-15.83,p:"Endeavour Reef",d:"11 Jun 1770",c:3,k:"wreck",n:"Aground at eleven at night on a rising tide already past the full. They threw the guns overboard, fothered a sail under the hole, and pumped for twenty-three hours. A lump of coral had wedged in the breach and was holding the sea out.",v:[[151.5,-33.83],[154.17,-31.83],[154.83,-24.83],[145.5,-15.83]]},
 {x:145.25,y:-15.47,p:"Endeavour River",d:"Jun–Aug 1770",c:3,n:"Seven weeks careened on a beach, mending. Here they saw the animal that could not be described, and got the word kangaroo from the Guugu Yimithirr."},
 {x:142.40,y:-10.72,p:"Possession Island",d:"22 Aug 1770",c:3,k:"turn",n:"He claimed the entire eastern coast for George III, on an islet, in front of nobody."},
 {x:106.83,y:-6.13,p:"Batavia",d:"Oct–Dec 1770",c:3,k:"death",n:"He had crossed the Pacific without losing a man to scurvy, which was the achievement of the age. Then he refitted in the unhealthiest port in Asia and buried seven men there and thirty more on the way home.",v:[[142.5,-10.83],[127.17,-9.83],[123.17,-12.17],[120.17,-12.17],[116.17,-10.17],[106.5,-8.83],[105.17,-7.5],[106.5,-5.83]]},
 {x:18.42,y:-33.92,p:"Cape Town",d:"Mar 1771",c:3,n:"Dying men landed at the hospital. The ship's company was too thin to work her properly.",v:[[106.5,-5.83],[104.5,-6.83],[77.17,-6.83],[57.5,-15.83],[46.83,-26.5],[42.83,-26.83],[33.5,-36.17],[19.5,-36.17],[17.5,-34.83],[18.17,-33.83]]},
 {x:1.35,y:51.22,p:"The Downs",d:"12 Jul 1771",c:3,n:"Home. Banks got the fame, Cook got another ship, and Tupaia had died at Batavia.",v:[[18.17,-33.83],[16.5,-33.17],[11.5,-19.17],[-5.5,-2.17],[-17.5,11.17],[-18.83,14.5],[-19.17,28.83],[-10.83,37.17],[-10.5,43.17],[-6.17,48.5],[1.5,51.17]]}
]},

/* ---------------------------------------------------------- 5 */
{id:"beagle",kind:"real",domain:"sea",title:"Darwin's Beagle",sub:"HMS Beagle, Capt. Robert FitzRoy",
 years:"1831–36",colour:"#27ae60",
 stat:{out:"about 74 aboard",back:"most of them",days:1741,
       note:"Plymouth, 27 December 1831 – Falmouth, 2 October 1836. Planned as two years."},
 gist:"A survey voyage with a spare passenger. Darwin was aboard because FitzRoy wanted a gentleman to dine with and feared going mad alone; he spent three-fifths of the five years ashore, which is where the work happened.",
 legs:[
 {x:-4.14,y:50.37,p:"Plymouth",d:"27 Dec 1831",c:3,n:"Two false starts in December gales. Darwin was violently seasick for most of five years and never got used to it."},
 {x:-23.51,y:14.92,p:"São Tiago, Cape Verde",d:"16 Jan 1832",c:3,k:"turn",n:"A white band of shells and coral fused into rock, high in a cliff. Lyell's first volume was in his cabin, and standing on that band he understood he was looking at deep time. He decided here that he might write a book about geology."},
 {x:-38.51,y:-12.97,p:"Bahia",d:"29 Feb 1832",c:3,n:"His first rainforest, and a long entry about the impossibility of conveying it. He and FitzRoy nearly parted company over slavery within weeks.",v:[[-29.17,7.5],[-33.5,-1.83],[-33.83,-8.83],[-37.5,-13.5]]},
 {x:-43.17,y:-22.91,p:"Rio de Janeiro",d:"Apr 1832",c:3,n:"Three months collecting inland while the ship surveyed.",v:[[-37.5,-16.17],[-39.5,-22.17],[-41.83,-24.17]]},
 {x:-62.1,y:-38.9,p:"Punta Alta",d:"Sep 1832",c:3,k:"turn",n:"Giant fossil bones in a low cliff — Megatherium, Toxodon, a horse — extinct animals that were plainly related to the living ones around them. The question was in the ground here, six years before he had an answer.",v:[[-57.5,-39.5],[-60.83,-40.17]]},
 {x:-68.2,y:-54.9,p:"Tierra del Fuego",d:"Dec 1832",c:3,n:"FitzRoy was returning three Fuegians he had taken to England and educated. Within a year Jemmy Button was living as he had before, and content, which shook Darwin more than the fossils.",v:[[-61.17,-41.17],[-62.5,-43.5],[-62.5,-54.83],[-66.83,-56.83],[-67.83,-55.5]]},
 {x:-59.0,y:-51.7,p:"Falkland Islands",d:"Mar 1833",c:3,n:"Just annexed, twice, and almost empty. Darwin found the fossil brachiopods and disliked the place.",v:[[-67.83,-55.5],[-67.17,-56.83],[-63.83,-56.17],[-62.5,-51.83],[-61.17,-50.5],[-59.5,-51.17]]},
 {x:-68.6,y:-50.1,p:"Río Santa Cruz",d:"Apr 1834",c:3,n:"Two hundred miles up the river hauling boats, and back, having failed to reach the Andes but crossed the great stepped plains that made him think about slow uplift.",v:[[-59.5,-51.17]]},
 {x:-70.9,y:-53.6,p:"Strait of Magellan",d:"Jun 1834",c:3,n:"Through to the Pacific.",v:[[-67.83,-51.5]]},
 {x:-73.05,y:-36.83,p:"Concepción",d:"4 Mar 1835",c:3,k:"turn",n:"He had felt the earthquake at Valdivia and now saw what it did: a town flattened, and mussel beds standing several feet clear of the water. The land had gone up while he watched. Lyell was right.",v:[[-75.17,-53.5],[-76.83,-50.83],[-76.83,-43.5],[-75.17,-37.5]]},
 {x:-70.0,y:-32.8,p:"Across the Andes",d:"Mar–Apr 1835",c:3,n:"Over the Portillo pass at 13,000 feet, and near the top a band of fossil seashells and a stand of petrified pines that had grown on a beach."},
 {x:-77.15,y:-12.06,p:"Callao and Lima",d:"Jul 1835",c:3,n:"A miserable month in a country at war with itself, waiting for the ship."},
 {x:-90.35,y:-0.45,p:"Galápagos",d:"15 Sep–20 Oct 1835",c:3,k:"landfall",n:"Five weeks; he did not label his finch specimens by island and had to reconstruct it later from FitzRoy's and his servant's collections. The mockingbirds, not the finches, were what first bothered him."},
 {x:-149.49,y:-17.53,p:"Tahiti",d:"Nov 1835",c:3,n:"He liked the Tahitians and defended the missionaries in print, which was not the fashionable position."},
 {x:174.08,y:-35.28,p:"Bay of Islands",d:"Dec 1835",c:3,n:"He disliked New Zealand thoroughly and said so."},
 {x:151.21,y:-33.87,p:"Sydney",d:"Jan 1836",c:3,n:"Struck by the platypus and the potoroo: two separate creations, or one that had diverged? He wrote the thought down and let it lie."},
 {x:96.87,y:-12.13,p:"Cocos (Keeling)",d:"Apr 1836",c:3,k:"turn",n:"His coral reef theory, worked out before he ever saw a reef, tested against a real atoll and confirmed. It is still broadly correct, and he thought it his best piece of pure reasoning.",v:[[151.5,-33.83],[151.17,-37.5],[146.5,-39.83],[141.5,-39.83],[135.83,-36.5],[115.83,-36.17],[101.17,-21.83],[96.83,-12.17]]},
 {x:18.42,y:-33.92,p:"Cape Town",d:"Jun 1836",c:3,n:"Dinner with John Herschel, who had been writing about the mystery of mysteries — the replacement of extinct species by new ones.",v:[[96.83,-12.17],[65.5,-12.17],[57.5,-15.83],[46.83,-26.5],[35.83,-26.83],[25.5,-35.5],[19.5,-36.17],[17.5,-34.83],[18.17,-33.83]]},
 {x:-38.51,y:-12.97,p:"Bahia again",d:"Aug 1836",c:3,n:"FitzRoy doubled back across the Atlantic to re-check a chronometer reading. Darwin, desperate to be home, was not grateful."},
 {x:-5.07,y:50.15,p:"Falmouth",d:"2 Oct 1836",c:3,n:"Ashore in the night mail coach to Shrewsbury. He never left Britain again.",v:[[-38.5,-13.17],[-31.17,-7.17],[-19.83,17.83],[-19.17,28.83],[-11.17,36.83],[-10.5,43.17],[-5.17,50.17]]}
]},

/* ---------------------------------------------------------- 6 */
{id:"mayflower",kind:"real",domain:"sea",title:"The Mayflower",sub:"and, briefly, the Speedwell",
 years:"1620",colour:"#d35400",
 stat:{out:"102 passengers, about 30 crew",back:"the ship went home in April; 45 of the passengers died the first winter",days:66,
       note:"Plymouth, 6 September – Cape Cod, 11 November 1620 (Old Style)."},
 gist:"A voyage that arrived in the wrong place, in the wrong season, and survived on the strength of a document written because it had arrived in the wrong place.",
 legs:[
 {x:-1.40,y:50.90,p:"Southampton",d:"5 Aug 1620",c:3,n:"Two ships. The Speedwell had been re-rigged with masts too large for her and was working her seams open before she cleared the Solent."},
 {x:-3.58,y:50.35,p:"Dartmouth",d:"Aug 1620",c:3,n:"Put in leaking. Repaired. Sailed. Leaked again."},
 {x:-4.14,y:50.37,p:"Plymouth",d:"6 Sep 1620",c:3,k:"turn",n:"The Speedwell abandoned, her passengers crammed aboard or sent home, and six weeks of the sailing season gone. They left with the equinox behind them."},
 {x:-35,y:44,p:"Mid-Atlantic",d:"Sep–Oct 1620",c:2,n:"Autumn gales. A main beam cracked and was jacked back into place with a great iron screw, probably from a printing press. John Howland went over the side and caught a topsail halyard trailing in the water."},
 {x:-70.19,y:42.05,p:"Cape Cod",d:"9 Nov 1620",c:3,k:"landfall",n:"Land at daybreak, and about two hundred miles north of the Hudson, where their patent was. They turned south for it."},
 {x:-69.98,y:41.55,p:"Pollock Rip",d:"9 Nov 1620",c:2,k:"turn",n:"Roaring breakers and shoals off the elbow of the Cape in a falling wind. They put about — and so the colony went where the sandbank sent it."},
 {x:-70.18,y:42.05,p:"Provincetown Harbor",d:"11 Nov 1620",c:3,n:"Anchored. Being outside their patent meant being outside any law, and some of the non-Separatist passengers said so out loud. Forty-one men signed the Compact that morning to hold the thing together."},
 {x:-70.00,y:41.83,p:"First Encounter Beach",d:"8 Dec 1620",c:3,n:"The third exploring party was shot at with arrows by Nauset men, who had cause: an English captain had kidnapped seven of them six years earlier."},
 {x:-70.66,y:41.96,p:"Plymouth Harbor",d:"21 Dec 1620",c:3,n:"Cleared fields, a good brook, a hill to fort. The fields were clear because a plague brought by earlier European fishermen had emptied Patuxet three years before. Half the passengers were dead by March."}
]},

/* ---------------------------------------------------------- 7 */
{id:"zhenghe",kind:"real",domain:"sea",title:"Zheng He's treasure fleets",sub:"Seven voyages, Ming dynasty",
 years:"1405–33",colour:"#c0a020",
 stat:{out:"up to 300 ships, some 27,000 men per voyage",back:"seven voyages; Zheng He died on the seventh",days:10200,
       note:"First fleet sailed 1405; the seventh returned in 1433 and the programme was cancelled."},
 gist:"Fleets an order of magnitude larger than anything Europe put to sea for another four centuries, sent out to make the Indian Ocean acknowledge the Ming, and then stopped by a change of policy at court. The track shown is the cumulative reach of all seven.",
 legs:[
 {x:118.78,y:32.06,p:"Nanjing",d:"from 1405",c:3,n:"The Longjiang yards. The largest ships were reported at over 120 metres, which naval architects have disputed for a century; even the sceptical estimates leave them the biggest wooden ships ever built."},
 {x:121.1,y:31.5,p:"Liujiagang",d:"assembly",c:3,n:"The fleet mustered at the Yangtze mouth, sixty-odd ocean-going junks with a supporting cast of water tankers, horse transports and troop ships.",v:[[120.5,33.83],[121.83,32.17]]},
 {x:119.52,y:25.96,p:"Changle, Fujian",d:"waiting for the monsoon",c:3,n:"They wintered here for the north-east monsoon. On the seventh voyage Zheng He left an inscribed stele recording the previous six, which is the main reason we have the itineraries.",v:[[121.83,32.17],[123.5,29.5]]},
 {x:109.22,y:13.77,p:"Champa",d:"voyages 1–7",c:3,n:"First foreign landfall every time, at Qui Nhon."},
 {x:112.75,y:-7.25,p:"Java",d:"voyage 1",c:3,k:"death",n:"A hundred and seventy of his men were killed by mistake in a Javanese civil war. The Ming demanded 60,000 taels of gold in compensation, then waived it, which was the point of the exercise.",v:[[110.83,12.83],[110.83,8.17],[106.83,3.83],[107.83,-1.17],[112.17,-6.5]]},
 {x:104.75,y:-2.99,p:"Palembang",d:"1407",c:3,n:"A Chinese pirate lord, Chen Zuyi, had made himself master of the Malacca Strait. Zheng He destroyed his fleet, took him back to Nanjing and had him beheaded there.",v:[[112.17,-6.5],[106.5,-0.5],[104.83,-1.83]]},
 {x:102.25,y:2.19,p:"Malacca",d:"voyages 1–7",c:3,n:"Built up as the fleet's forward depot, with a stockaded compound. Malacca's rise as the great entrepôt of the East dates from this patronage.",v:[[104.83,-1.83],[106.17,0.17]]},
 {x:97.15,y:5.55,p:"Semudera",d:"voyages 1–7",c:3,n:"Northern Sumatra, and another intervention in a succession dispute that ended with a claimant shipped to China."},
 {x:80.22,y:6.04,p:"Ceylon",d:"1411",c:3,n:"A trilingual stele at Galle in Chinese, Tamil and Persian, making offerings to the Buddha, to a Hindu god and to Allah — three religions, three sets of gifts, one stone. Then he deposed the king for attacking him."},
 {x:75.78,y:11.25,p:"Calicut",d:"voyages 1–7",c:3,k:"turn",n:"The hinge of the Indian Ocean trade and the fleet's usual turning point. Ma Huan wrote down how business was done here: brokers, buyers and sellers clasping hands under a cloth and settling the price by finger pressure.",v:[[79.83,6.5],[75.17,8.83]]},
 {x:56.45,y:27.15,p:"Hormuz",d:"voyages 4–7",c:3,n:"From the fourth voyage the fleets went beyond India: the Gulf, and the horse trade, and the western terminus of everything."},
 {x:45.03,y:12.79,p:"Aden",d:"voyages 5–7",c:3,n:"A squadron detached to Arabia; another went on to Mecca. They brought back a giraffe, which the court read as a qilin and therefore as heaven's approval.",v:[[61.17,22.5],[59.17,18.83],[52.17,14.17],[47.17,12.17]]},
 {x:45.34,y:2.05,p:"Mogadishu",d:"voyages 5–7",c:3,n:"Detached squadrons on the Somali coast, trading for ambergris, ivory and zebras.",v:[[51.17,13.17],[52.5,11.83],[49.83,5.17]]},
 {x:40.12,y:-3.22,p:"Malindi",d:"voyages 5–7",c:2,k:"landfall",n:"The furthest documented reach, some sixty years before da Gama's pilot took him the other way along the same coast. Everything beyond this is speculation, and there has been a great deal of it.",v:[[41.5,-3.17]]},
 {x:75.78,y:11.25,p:"Calicut",d:"1433",c:2,k:"death",n:"Zheng He died on the return leg of the seventh voyage, most probably here, and was buried at sea; the tomb at Nanjing is a cenotaph."},
 {x:118.78,y:32.06,p:"Nanjing",d:"1433",c:3,n:"The fleet came home to a Confucian bureaucracy that regarded the voyages as a eunuch admiral's vanity and the expense as ruinous. The programme was cancelled, the shipyards let go, and some of the records destroyed.",v:[[75.17,8.83],[80.5,4.5],[97.83,6.83],[103.5,2.83],[122.5,22.5],[123.5,30.17],[122.83,32.5],[120.5,33.83]]}
]},

/* ---------------------------------------------------------- 8 */
{id:"caird",kind:"real",domain:"sea",title:"Shackleton's James Caird",sub:"a 22½-foot ship's boat",
 years:"1916",colour:"#2c3e50",
 stat:{out:"6 men",back:"6 men; and all 28 of the Endurance party lived",days:16,
       note:"Elephant Island, 24 April – South Georgia, 10 May 1916. About 800 miles."},
 gist:"The best small-boat navigation ever done, and it had to be: Worsley got four sextant sights in sixteen days, and a target 800 miles away that was 100 miles wide. Miss it and the next land is South Africa.",
 legs:[
 {x:-36.51,y:-54.28,p:"Grytviken",d:"5 Dec 1914",c:3,t:"pro",n:"The Endurance sailed from South Georgia into the Weddell Sea, warned by the whalers that the ice was the worst in memory."},
 {x:-31.5,y:-76.57,p:"Beset, 76°34'S",d:"19 Jan 1915",c:3,t:"pro",k:"turn",n:"One day's sail from the intended landing, the pack closed on her. She was never free again."},
 {x:-52.97,y:-68.64,p:"Endurance crushed",d:"21 Nov 1915",c:3,t:"pro",k:"wreck",n:"Ten months drifting north in the floe, then the pressure took her. Twenty-eight men on the ice with three boats and no way of telling anyone."},
 {x:-55.22,y:-61.13,p:"Elephant Island",d:"15 Apr 1916",c:3,t:"pro",k:"landfall",n:"After five days in open boats, the first solid ground under their feet in sixteen months. Uninhabited, off every shipping route, and no one on earth knew they were there."},
 {x:-55.22,y:-61.13,p:"Departure",d:"24 Apr 1916",c:3,n:"Six men, a decked-over boat ballasted with shingle, and provisions for four weeks — deliberately, because if they had not reached South Georgia by then they would not be reaching anywhere."},
 {x:-50,y:-59.5,p:"Into the Drake",d:"late April",c:2,n:"The Furious Fifties in winter. They took spells of four hours steering and four hours in wet reindeer-hide bags that were shedding hair into everything, and chipped ice off the decking to keep her from turning turtle."},
 {x:-45,y:-57.5,p:"The rogue sea",d:"5 May 1916",c:2,n:"Shackleton saw a line of white astern and took it for a clearing sky. It was the crest of a wave bigger than anything in his twenty-six years at sea. She came through it full to the thwarts."},
 {x:-39,y:-55,p:"Worsley's fourth sight",d:"8 May 1916",c:2,k:"turn",n:"Four workable sun-sights in sixteen days, taken kneeling, with two men holding him, from a boat that never stopped moving. Everything else was dead reckoning on a soaked chart."},
 {x:-37.5,y:-54.15,p:"King Haakon Bay",d:"10 May 1916",c:3,k:"landfall",n:"They raised South Georgia on the ninth and could not land for a hurricane that sank a 500-ton steamer the same night. They got in the following afternoon, on the wrong side of the island, and drank from a stream."},
 {x:-37.0,y:-54.1,p:"Across South Georgia",d:"19–20 May 1916",c:3,n:"Shackleton, Worsley and Crean crossed the unmapped interior in thirty-six hours with fifty feet of rope, a carpenter's adze and screws from the boat put through their boot soles for grip. Nobody repeated it for thirty-nine years, and that party had proper equipment."},
 {x:-36.70,y:-54.15,p:"Stromness",d:"20 May 1916",c:3,n:"They walked into the whaling station filthy and bearded and the manager did not know them. Shackleton's first question was about the war. He was told it was still going on and that millions were dead."}
]},

/* ============================================================
   REAL — LAND (8)
   ============================================================ */

/* ---------------------------------------------------------- 9 */
{id:"xenophon",kind:"real",domain:"land",title:"Xenophon's Ten Thousand",sub:"the Cyreian mercenary army",
 years:"401–399 BC",colour:"#a2601f",
 stat:{out:"about 10,400 Greek hoplites and 2,500 peltasts, hired by Cyrus the Younger",
       back:"roughly 8,600 reached the sea, by Xenophon's own count",days:730,
       note:"Sardis to Cunaxa and the fighting retreat to Trapezus and Byzantium: about 1,700 miles over some fifteen months, with a further year of freelance service before the survivors were formally discharged."},
 gist:"Ten thousand Greek mercenaries hired for someone else's civil war, stranded eight hundred miles from the sea when their employer died in the first battle and their own generals were murdered under a truce flag. What follows is not a retreat so much as an army electing new officers on the march and fighting its way home through five hostile nations — which is why every later general who tried the same thing had read this book first.",
 legs:[
 {x:28.04,y:38.48,p:"Sardis",d:"401 BC",c:3,n:"The mustering point for Cyrus's army, ostensibly bound against the Pisidian hill tribes. Nobody below the satrap level was told the truth for months."},
 {x:34.90,y:36.92,p:"The Cilician Gates and Tarsus",d:"401 BC",c:3,n:"Through the mountain pass and into Tarsus, where the Greek contingents worked out roughly where they were actually being taken, and had to be paid a bonus to keep marching."},
 {x:38.15,y:35.95,p:"Thapsacus, on the Euphrates",d:"401 BC",c:2,n:"The river was unexpectedly low, which the guide called an omen and everyone else called luck. They crossed on foot."},
 {x:43.77,y:33.35,p:"Cunaxa",d:"3 Sep 401 BC",c:3,k:"death",n:"Cyrus's own cavalry charge broke the Persian centre; then Cyrus, ignoring the plan, went personally for his brother Artaxerxes and was killed doing it. The battle the Greeks had just won had lost its cause in the same afternoon."},
 {x:44.30,y:33.10,p:"Stranded near Babylon",d:"Sep 401 BC",c:3,k:"turn",n:"With no employer and no way home, they negotiated safe conduct under a Persian escort they did not trust — correctly, as it turned out."},
 {x:43.55,y:36.05,p:"The Great Zab",d:"Oct 401 BC",c:3,k:"death",n:"Tissaphernes invited the five Greek generals, Clearchus among them, to a conference and had them seized and beheaded under the truce. Xenophon, a gentleman-volunteer with no command, was elected general that same night by soldiers who had never taken an order from him before."},
 {x:43.70,y:37.50,p:"The Carduchian mountains",d:"Oct 401 BC",c:3,n:"Seven days fighting through mountains whose inhabitants answered to no king, and disliked the Greeks rather less than they disliked the Persians — which was not much comfort."},
 {x:41.49,y:38.73,p:"Crossing into Armenia",d:"Nov–Dec 401 BC",c:2,n:"Snow to the thighs, men going blind from the glare and lame with frostbite, and villages that had never seen a foreign army and had already buried their grain against exactly this."},
 {x:39.27,y:40.66,p:"Mount Theches",d:"Dec 401 BC",c:2,k:"turn",n:"The front of the column started shouting, and Xenophon, at the rear expecting an attack, rode up to find them weeping: Thalatta! Thalatta! The sea. They were still a week from any port, but the sea meant Greek cities, and Greek cities meant they might actually go home."},
 {x:39.72,y:41.00,p:"Trapezus",d:"Dec 401 BC",c:3,k:"landfall",n:"A Greek colony on the Black Sea, the first Greek city in eight months — the point where the story stops being about survival and starts being about how to get paid and get a passage home, which took another year of freelance soldiering along the coast."},
 {x:28.98,y:41.01,p:"Byzantium",d:"399 BC",c:3,n:"Xenophon finally disbanded them into Spartan service against Persia's former ally, having brought home roughly eight men in ten of those who had marched out of Sardis — the best survival rate of any army stranded this far from home in the ancient world."}
]},

/* ---------------------------------------------------------- 10 */
{id:"alexander",kind:"real",domain:"land",title:"Alexander's campaign",sub:"the Macedonian army, Companions and phalanx",
 years:"334–323 BC",colour:"#6b4fa0",
 stat:{out:"roughly 40,000 infantry and cavalry crossing into Asia",
       back:"an unknown fraction; the Gedrosian desert alone may have cost more lives than any battle of the campaign",
       days:4015,note:"Pella to the Hyphasis and back to Babylon: something over 20,000 miles of marching across eleven years, by conservative reckoning."},
 gist:"Eleven years without losing a pitched battle, ended not by an enemy but by his own army's refusal to cross one more river. The return through the Gedrosian desert — a punishing shortcut he insisted on for reasons his own officers thought closer to spite than strategy — did more damage to his men than Persia, Egypt and India combined.",
 legs:[
 {x:22.53,y:40.76,p:"Pella",d:"334 BC",c:3,n:"Left Antipater as regent and barely enough silver in the treasury to feed the army for a month, against an enterprise he was effectively betting on Persian gold he did not yet have."},
 {x:26.40,y:40.20,p:"The Hellespont, at Abydos",d:"334 BC",c:3,k:"turn",n:"He threw a spear into Asian soil from the ship and claimed the whole continent as spear-won land, then detoured to Troy to sacrifice at Achilles's tomb — a piece of theatre no officer in the army would have missed."},
 {x:27.13,y:40.18,p:"The Granicus",d:"334 BC",c:3,k:"death",n:"His first pitched battle in Asia, won by leading the cavalry charge himself into the stronger side of the enemy line — either courage or a demonstration for an army that did not yet fully trust him."},
 {x:31.99,y:39.65,p:"Gordium",d:"333 BC",c:2,n:"The knot that whoever undid would rule Asia. He cut it with his sword, or pulled the pin from the yoke-pole, depending which ancient source you prefer; both agree he did not untie it."},
 {x:36.16,y:36.59,p:"Issus",d:"Nov 333 BC",c:3,k:"turn",n:"Darius fled the field in his own chariot, leaving his mother, wife and children to be captured. Alexander treated them with a chivalry that was also, not incidentally, very good propaganda."},
 {x:35.19,y:33.27,p:"Tyre",d:"Jan–Jul 332 BC",c:3,k:"wreck",n:"A seven-month siege of an island city that required building a half-mile causeway under fire. When it fell he crucified two thousand men along the shore, which is the other half of the chivalry."},
 {x:25.52,y:29.20,p:"Siwa Oasis",d:"332 BC",c:3,n:"A detour of several hundred miles into the desert to ask an oracle whether he was the son of a god. What the priest actually said is not recorded; what Alexander afterwards told people the priest said became state policy."},
 {x:43.35,y:36.35,p:"Gaugamela",d:"1 Oct 331 BC",c:3,k:"turn",n:"The decisive battle, fought on ground Darius had leveled for his chariots. Alexander drove a wedge through a gap that opened in the Persian line and went straight for Darius again, who ran again."},
 {x:52.89,y:29.94,p:"Persepolis",d:"Jan 330 BC",c:3,k:"death",n:"The Persian ceremonial capital, burned to the ground after a drinking party, on Alexander's order or a courtesan's suggestion, depending on the historian and how much they liked him."},
 {x:66.90,y:36.76,p:"Bactra and Sogdiana",d:"329–327 BC",c:3,n:"Two years pinning down guerrilla resistance in mountains no Persian king had ever fully controlled, ending with his marriage to Roxana, a local chieftain's daughter — policy, and by every account genuine feeling as well."},
 {x:73.73,y:32.93,p:"The Hydaspes",d:"May 326 BC",c:3,k:"death",n:"A night crossing in a thunderstorm and a battle against Porus's war elephants — the hardest fight of the campaign, by his own admission. Bucephalas, his horse of twenty years, died here or soon after; Alexander founded a city and named it for him."},
 {x:75.15,y:31.65,p:"The Hyphasis",d:"Aug 326 BC",c:3,k:"turn",n:"The army stopped. Not defeated — mutinous, quietly and completely, after eight years and a monsoon they had never trained for. Alexander sulked in his tent for three days and then, for the only time in his career, gave in."},
 {x:68.37,y:25.38,p:"Patala, on the Indus",d:"Sep 325 BC",c:3,n:"He sent the fleet home by sea under Nearchus and took the army itself south to the desert, apparently to punish the peoples who had failed to supply him on the way up."},
 {x:62.0,y:26.0,p:"The Gedrosian desert",d:"Oct–Dec 325 BC",c:3,k:"wreck",n:"Sixty days of the Makran desert, historians differ on whether as a deliberate ordeal or simply bad planning, at a cost — unrecorded but clearly enormous — in soldiers, camp followers and pack animals to thirst."},
 {x:48.26,y:32.19,p:"Susa",d:"324 BC",c:3,n:"A mass wedding of Macedonian officers to Persian noblewomen, meant to fuse the two aristocracies into a single ruling class. It did not outlive him."},
 {x:44.42,y:32.54,p:"Babylon",d:"Jun 323 BC",c:3,k:"death",n:"He died here the following year, probably of a fever, possibly helped along, not yet thirty-three and with the empire's succession entirely unplanned — which is exactly how it was fought over for the next forty years."}
]},

/* ---------------------------------------------------------- 11 */
{id:"xuanzang",kind:"real",domain:"land",title:"Xuanzang's pilgrimage",sub:"the monk Xuanzang, alone",
 years:"629–645",colour:"#c98a2b",
 stat:{out:"one monk, without a travel permit",
       back:"one monk, with 657 Buddhist texts on twenty packhorses and an imperial reception",
       days:5840,note:"Chang'an to Nalanda and back, roughly 10,000 miles, by two different routes around the Taklamakan."},
 gist:"A monk who left China illegally, defying an imperial travel ban, to fetch scriptures nobody in China had accurate copies of — and came back seventeen years later with such prestige that the emperor who would have executed him for leaving instead pardoned him on the spot and asked him to write a report.",
 legs:[
 {x:108.95,y:34.27,p:"Chang'an",d:"629",c:3,k:"turn",n:"Left at night, alone, without the permit border guards were under standing orders to check. He would spend the whole outbound journey one step ahead of arrest."},
 {x:102.64,y:37.93,p:"Liangzhou",d:"629",c:2,n:"A local governor recognized him and warned him to leave before an arrest order arrived from the capital. He left that same night."},
 {x:95.8,y:40.5,p:"The beacon towers beyond Yumen Pass",d:"629",c:2,k:"wreck",n:"Five days without water after dropping his waterskin in the desert, before his horse — an old one, by his account, that had made the crossing before — turned off the road toward a spring he had not known was there."},
 {x:89.18,y:42.95,p:"Gaochang, Turfan",d:"629",c:3,k:"landfall",n:"King Qu Wentai, a devout Buddhist, tried to keep him at court by force, then by a hunger strike of his own — Xuanzang refused food for three days in return — and finally let him go only after making him swear to lecture there on the way back. He never did; the king was dead and his kingdom annexed to China by then."},
 {x:82.93,y:41.72,p:"Kucha and the northern Tian Shan",d:"630",c:2,n:"The passes were still under snow in what should have been the low season; several of the escort provided by local rulers froze to death crossing them with him."},
 {x:66.97,y:39.65,p:"Samarkand and Bactria",d:"630",c:3,n:"A Buddhist community already in visible decline, and a colossal shrine at Bamiyan he described in enough architectural detail to help later scholars reconstruct its original form after the Taliban destroyed the two Buddha statues in 2001."},
 {x:71.58,y:34.01,p:"The Khyber Pass into Gandhara",d:"630",c:3,k:"turn",n:"Down into a subcontinent whose scriptural texts, garbled by centuries of transliteration, had made Chinese Buddhism increasingly uncertain of its own sources. This was the entire point of the trip."},
 {x:74.80,y:34.08,p:"Kashmir",d:"631–633",c:3,n:"Two years studying with local scholars, and having a complete philosophical canon copied out for him by hand — an operation that occupied twenty scribes for most of that time."},
 {x:85.44,y:25.14,p:"Nalanda",d:"c. 637–642",c:3,k:"landfall",n:"The great Buddhist university: several thousand monks, and a curriculum in logic, grammar and medicine as well as scripture. He studied under the abbot Shilabhadra, then stayed to teach, and was still there five years later when he finally decided it was time to go home."},
 {x:79.92,y:27.05,p:"Kanauj",d:"642",c:3,n:"King Harsha staged a public debate and put Xuanzang up as champion of Mahayana Buddhism against all comers, then built a tower to display the silence of the opposition. Xuanzang was, by his own account and everyone else's, unbeatable in argument."},
 {x:75.99,y:39.47,p:"Kashgar and the southern Taklamakan",d:"644",c:2,n:"This time he wrote ahead asking the emperor's pardon before crossing back into China proper, having spent seventeen years assuming, correctly, that the ban on leaving had never technically been lifted."},
 {x:94.66,y:40.14,p:"Dunhuang",d:"644–645",c:3,n:"He waited at the border for the pardon to arrive rather than risk a return the same way he had left. It came, with an invitation to court that amounted to a state welcome."},
 {x:108.95,y:34.27,p:"Chang'an",d:"645",c:3,k:"landfall",n:"A procession is said to have taken days to pass, carrying 657 texts on twenty horses. He spent the rest of his life translating them and dictating the travelogue — the Great Tang Records on the Western Regions — that remains the single best written source for seventh-century Central Asia."}
]},

/* ---------------------------------------------------------- 12 */
{id:"marcopolo",kind:"real",domain:"land",title:"Marco Polo",sub:"Marco, Niccolò and Maffeo Polo",
 years:"1271–95",colour:"#b5533c",
 stat:{out:"three merchants",
       back:"three merchants, one Mongol princess delivered to her betrothed, and a manuscript later ghostwritten in a Genoese prison",
       days:8760,note:"Acre to Shangdu overland, and home by sea via Sumatra and the Malabar coast: about seventeen years abroad, some 15,000 miles each way by his own reckoning."},
 gist:"The outbound leg, three and a half years overland to Kublai Khan's summer court, made the family famous; the return — three years escorting a Mongol bride-to-be by sea because the overland roads had grown too dangerous — is the less-told half, and cost the fleet all but eighteen of roughly six hundred passengers and crew to disease.",
 legs:[
 {x:35.08,y:32.92,p:"Acre",d:"1271",c:3,n:"They picked up papal letters and holy oil for the Khan, who had specifically requested both on the family's previous trip, along with a hundred Christian scholars the Pope could not actually supply."},
 {x:46.29,y:38.08,p:"Tabriz",d:"1272",c:3,n:"A Mongol Ilkhanate capital Marco calls the finest trading city in the whole region, high praise from a man who saw most of them."},
 {x:56.45,y:27.15,p:"Hormuz",d:"1272",c:3,k:"turn",n:"They inspected ships here with a view to sailing on to China, and pronounced them unseaworthy — sewn hulls, no iron nails — and turned back inland instead, a decision that added a year to the journey and probably saved their lives."},
 {x:57.08,y:30.28,p:"Kerman and the Persian desert",d:"1272",c:2,n:"Bandits, by Marco's account, worked this stretch by raising a dust storm and riding out of it; whether or not that detail is true, caravans this size travelled together here for good reason."},
 {x:70.58,y:37.12,p:"Badakhshan and the Pamirs",d:"1273",c:3,k:"turn",n:"A year recovering from illness in the mountains — Marco credits the thin, clean air with curing him — before crossing what he calls the Roof of the World, where he reports fires burning less brightly and food taking longer to cook: both real effects of low-oxygen air he had no way of explaining."},
 {x:75.99,y:39.47,p:"Kashgar",d:"1273",c:3,n:"A market where, he says, merchants of every nation under the sun could be found — for a Venetian, a considered judgment rather than a figure of speech."},
 {x:79.93,y:37.11,p:"Khotan and the Lop Nor crossing",d:"1273",c:2,n:"Provisioned with extra fodder for the animals before the desert crossing, because grazing along the route was known in advance to be unreliable — logistics that argue for a well-established road rather than an improvised one."},
 {x:100.45,y:38.93,p:"Ganzhou",d:"1274",c:3,n:"A year's delay here, for reasons Marco does not explain, in the last Chinese-administered territory before the frontier proper."},
 {x:116.18,y:42.36,p:"Shangdu",d:"May 1275",c:3,k:"landfall",n:"Kublai Khan's summer capital, and the end of the outbound overland journey: three and a half years from Acre. Marco was then kept in Mongol service for the better part of two decades, sent on missions across the empire that supply most of the geography in the rest of his book."},
 {x:118.58,y:24.91,p:"Zaiton (Quanzhou)",d:"1291",c:3,k:"turn",n:"The great port of Mongol China, from which the family finally left — not for home, but escorting the Mongol princess Kököchin to Persia by sea, at the Khan's request, after the overland roads had grown too dangerous for a royal bride."},
 {x:97.90,y:4.90,p:"Sumatra",d:"1292",c:2,n:"Five months waiting out the monsoon on an island Marco describes with real ethnographic interest and considerable disgust at several of the customs he reports secondhand."},
 {x:76.60,y:8.88,p:"The Malabar coast",d:"1293",c:2,n:"Ports he describes in detail he could only have got from direct observation, in the middle of a book otherwise stitched together from what he was told."},
 {x:56.45,y:27.15,p:"Hormuz",d:"1294",c:2,k:"death",n:"The fleet that left Zaiton with roughly six hundred people arrived here with eighteen. Kököchin survived; her betrothed had died in the interval, and she married his son instead."},
 {x:39.72,y:41.00,p:"Trebizond and Constantinople",d:"1295",c:2,n:"The last stretch overland and by sea through territory the family, unlike most of the outbound route, already half-knew."},
 {x:12.34,y:45.44,p:"Venice",d:"1295",c:3,n:"Home, unrecognized by their own relatives after a quarter-century away, in clothes so worn that a later, probably embellished, story has them ripping open the seams to spill out the jewels sewn inside as proof of who they were."}
]},

/* ---------------------------------------------------------- 13 */
{id:"mansamusa",kind:"real",domain:"land",title:"Mansa Musa's hajj",sub:"Musa I of Mali",
 years:"1324–25",colour:"#c1440e",
 stat:{out:"a retinue reported — almost certainly inflated — at 60,000, including 12,000 enslaved attendants",
       back:"the same, minus an unrecorded number lost to the crossing, plus an Andalusian architect hired in Cairo",
       days:425,note:"Niani to Mecca and back, roughly 4,000 miles each way across the Sahara and the Nile valley, in about fourteen months."},
 gist:"A pilgrimage so heavily gilded — camels loaded with gold to be given away at every stop — that Musa's three-month stopover alone depressed the price of gold in Cairo for over a decade: the only medieval journey in this atlas with a documented, datable macroeconomic footprint.",
 legs:[
 {x:-8.65,y:11.93,p:"Niani",d:"1324",c:2,n:"The Malian capital's exact site is still argued over; the best candidate is near modern Kangaba on the upper Niger. Musa left a deputy in charge and set out with a retinue that later chroniclers, writing decades on, competed to exaggerate."},
 {x:-3.01,y:16.77,p:"Timbuktu",d:"1324",c:3,n:"Already a great trading and scholarly city before he left; it would be transformed on his return, when he brought an architect home with him."},
 {x:-7.03,y:17.32,p:"Walata",d:"1324",c:2,n:"The last major town before the open desert, and the customary hand-off point where Saharan Berber guides took over from the Malian escort for the crossing proper."},
 {x:-3.99,y:23.33,p:"The Taghaza salt crossing",d:"1324",c:1,n:"Salt mined here was worth its weight in gold on the far side of the desert Musa was heading toward — and would be worth exactly its weight in gold going the other way, once his spending had finished reordering regional prices."},
 {x:31.24,y:30.04,p:"Cairo",d:"Jul–Oct 1324",c:3,k:"turn",n:"Three months of gift-giving on a scale the Mamluk chronicler al-Umari — who interviewed people that had met him, a dozen years later — says Cairo had still not forgotten: enough gold changed hands that its market value there did not fully recover for about a decade, a documented instance of one visitor's spending moving a medieval economy."},
 {x:39.83,y:21.42,p:"Mecca",d:"1324",c:3,k:"landfall",n:"The hajj itself, nominally the entire point of the expedition, and the one stage the gold-obsessed sources spend almost no time describing."},
 {x:31.24,y:30.04,p:"Cairo, on the return",d:"1325",c:3,n:"Forced to borrow at ruinous interest from Cairo merchants to get his depleted retinue home, having given away more on the way out than he had budgeted for the way back — the gold crash's mirror image."},
 {x:0.04,y:16.27,p:"Gao",d:"1325",c:2,k:"turn",n:"Met by news that a general had used his absence to expand the empire, and by al-Sahili, the Andalusian poet and architect he had hired in Cairo, who would go on to build in Gao and Timbuktu the mudbrick style still associated with the region."},
 {x:-3.01,y:16.77,p:"Timbuktu",d:"1325",c:3,n:"Al-Sahili's Djinguereber Mosque, commissioned on the spot, still stands in something like its original form and is usually dated to this year."},
 {x:-8.65,y:11.93,p:"Niani",d:"1325",c:2,n:"Home a little over a year after leaving, to an empire whose reputation in Cairo, Mecca, and eventually European cartography — Musa appears crowned, holding a gold nugget, on the 1375 Catalan Atlas — now rested substantially on how much money he had thrown away in someone else's capital."}
]},

/* ---------------------------------------------------------- 14 */
{id:"lewisclark",kind:"real",domain:"land",title:"Lewis and Clark",sub:"the Corps of Discovery",
 years:"1804–06",colour:"#2e6f6e",
 stat:{out:"about 33 permanent members, plus Sacagawea, her infant son, and York, Clark's enslaved manservant",
       back:"all but one — Sergeant Charles Floyd, of a ruptured appendix, the expedition's only death",
       days:863,note:"St. Louis to the Pacific and back, about 8,000 miles round trip in two and a half years."},
 gist:"Sent to find a water passage across the continent that did not exist, and returned having found the thing that actually mattered instead: a continuous chain of Native nations whose knowledge, food and goodwill the expedition depended on at every stage, and without which it would not have survived its first winter, let alone reached the ocean.",
 legs:[
 {x:-90.15,y:38.85,p:"Camp Dubois",d:"May 1804",c:3,n:"Up the Missouri against the current from the start, the keelboat hauled, poled and sailed by turns, making perhaps fifteen miles on a good day."},
 {x:-96.4,y:42.5,p:"Council Bluffs",d:"Aug 1804",c:3,k:"death",n:"The expedition's only fatality: Sergeant Charles Floyd, of what a modern reading of the journals suggests was a burst appendix, buried on a bluff that still bears his name."},
 {x:-101.09,y:47.29,p:"Fort Mandan",d:"winter 1804–05",c:3,k:"turn",n:"Five months wintering among the Mandan and Hidatsa, who had traded with Europeans for a century already and knew more about the geography ahead than the expedition did. Sacagawea, a Shoshone woman taken young by the Hidatsa, was hired here with her French-Canadian husband, for her language and, it turned out, her diplomacy."},
 {x:-111.30,y:47.50,p:"The Great Falls of the Missouri",d:"Jun 1805",c:3,k:"wreck",n:"A portage of nearly eighteen miles around five waterfalls, hauling the boats on crude cottonwood-wheeled carts through prickly pear and hailstorms, that took a month rather than the half-day they had budgeted."},
 {x:-111.55,y:45.91,p:"Three Forks",d:"Aug 1805",c:3,n:"The three rivers that make the Missouri, named for Jefferson, Madison and Gallatin. Sacagawea recognized the country as her own homeland, from which she had been taken as a child."},
 {x:-113.45,y:45.03,p:"Lemhi Pass",d:"12 Aug 1805",c:3,k:"turn",n:"The Continental Divide, and the discovery that quietly killed the mission's actual premise: no navigable water route to the Pacific existed. Beyond the pass was not a gentle westward river but another, worse range of mountains."},
 {x:-113.9,y:45.17,p:"The Shoshone camp",d:"Aug 1805",c:3,n:"Sacagawea's own brother, Cameahwait, turned out to be chief of the very band they needed horses from — a coincidence so useful that Lewis's journal records it with visible disbelief."},
 {x:-114.9,y:46.5,p:"The Bitterroot crossing",d:"Sep 1805",c:3,k:"death",n:"Eleven days of the worst going of the whole trip, freezing and starving, eating candles and a colt, on a trail the Nez Perce used routinely and the Corps very nearly did not survive."},
 {x:-123.87,y:46.13,p:"Fort Clatsop",d:"Nov 1805–Mar 1806",c:3,k:"landfall",n:"The Pacific at last, and a miserable, rain-sodden winter camp near present Astoria, where it rained all but twelve days out of four months and the men voted — York and Sacagawea included, a franchise no other American institution of the period would have granted either of them — on where to build the fort."},
 {x:-114.09,y:46.75,p:"Travelers' Rest",d:"Jul 1806",c:3,k:"turn",n:"The party split to cover more ground on the return: Lewis north to explore the Marias River, Clark south and east down the Yellowstone."},
 {x:-112.5,y:48.5,p:"The Marias River",d:"Jul 1806",c:3,k:"death",n:"A shootout with Blackfeet warriors — the expedition's only violent encounter with Native people in two and a half years — left two men dead on the Blackfeet side and Lewis's party riding hard for the Missouri."},
 {x:-104.0,y:48.0,p:"The Missouri–Yellowstone confluence",d:"Aug 1806",c:3,n:"The two parties reunited within a day of each other's arrival at the meeting point — an almost absurd feat of dead-reckoning navigation after a thousand miles of separate travel."},
 {x:-90.15,y:38.85,p:"St. Louis",d:"23 Sep 1806",c:3,n:"Given up for dead by nearly everyone, including Jefferson; they arrived to a city that had to be told who they were before it could celebrate them."}
]},

/* ---------------------------------------------------------- 15 */
{id:"longmarch",kind:"real",domain:"land",title:"The Long March",sub:"the Chinese Red Army, First Front Army",
 years:"1934–35",colour:"#a4342a",
 stat:{out:"about 86,000 troops and cadres left the Jiangxi Soviet",
       back:"perhaps 7,000–8,000 reached Shaanxi with the main column — figures vary widely and were shaped afterward for propaganda purposes",
       days:368,note:"Ruijin to Yan'an, officially 25,000 li (about 8,000 miles); the true distance covered by any single unit was shorter, since the route looped west to evade encirclement rather than running straight north."},
 gist:"A retreat rebranded, with total success, as a foundation myth: the mileage is inflated and the casualty figures are contested by every historian who has looked closely, but the river crossings, the mountain passes, and the fact that a defeated army of tens of thousands walked itself into Shaanxi a year later with Mao Zedong now unambiguously in command, are not in dispute.",
 legs:[
 {x:116.03,y:25.89,p:"Ruijin",d:"16 Oct 1934",c:3,k:"turn",n:"A breakout, not a plan: Chiang Kai-shek's fifth encirclement campaign had closed in with a ring of blockhouses and roads the Communists could no longer out-manoeuvre from inside."},
 {x:110.6,y:25.6,p:"The Xiang River",d:"Nov–Dec 1934",c:3,k:"death",n:"The single worst loss of the campaign: caught crossing in the open by Nationalist forces, the column was roughly halved, from around 86,000 to nearer 30,000, in a matter of days."},
 {x:106.94,y:27.73,p:"Zunyi",d:"Jan 1935",c:3,k:"turn",n:"A conference held in a captured warlord's house that reorganized the military leadership and confirmed Mao's rising authority over the party's Moscow-trained faction — arguably the single most consequential meeting of the whole march."},
 {x:105.9,y:28.3,p:"The four crossings of the Chishui River",d:"Jan–Mar 1935",c:2,n:"Doubling back across the same river four times in ten weeks specifically to confuse the pursuit — a manoeuvre still taught in Chinese military academies as a model of mobile warfare."},
 {x:102.9,y:26.7,p:"The Jinsha River",d:"May 1935",c:3,k:"turn",n:"Crossed on a handful of ferried boats at a lightly guarded bend of the upper Yangtze while Nationalist forces watched further downstream — nine days to get the whole column over, unopposed."},
 {x:102.23,y:29.90,p:"The Luding Bridge",d:"29 May 1935",c:2,k:"death",n:"A chain suspension bridge over the Dadu River, its planking stripped by the defenders; the Party's account has a small assault party crossing hand over hand under fire to secure it. Later scholarship has questioned how contested the crossing actually was, without dislodging the story's central place in Party mythology."},
 {x:102.55,y:30.75,p:"The Jiajin Shan snow mountains",d:"Jun 1935",c:3,k:"death",n:"The first of several passes above 4,000 metres, crossed by soldiers from subtropical Jiangxi with no winter clothing; altitude sickness and exposure killed men who had survived every battle of the campaign so far."},
 {x:102.97,y:32.90,p:"Maoergai",d:"Jun–Aug 1935",c:2,k:"turn",n:"A meeting with the Fourth Front Army under Zhang Guotao that ended in a split rather than a merger: Zhang took his forces south and west on a route of his own that cost him most of his army; Mao's column went north."},
 {x:102.97,y:33.58,p:"The Zoige grasslands",d:"Aug 1935",c:3,k:"death",n:"An alpine marsh with no solid ground and no clean water, crossed in a week that left men who had survived the mountains dead of dysentery and drowning in bog."},
 {x:104.0,y:34.1,p:"Lazikou Pass",d:"Sep 1935",c:2,n:"A narrow gorge held by a small Nationalist garrison, taken by a night assault that opened the last mountain barrier before the loess plateau of the north."},
 {x:108.17,y:36.92,p:"Wuqi, Shaanxi",d:"19 Oct 1935",c:3,k:"landfall",n:"The end of the main column's march, and its joining-up with the existing Shaanxi Soviet under Liu Zhidan — the base from which the Party rebuilt for the next decade, at Yan'an, thirty miles south of here."}
]},

/* ---------------------------------------------------------- 16 */
{id:"burkewills",kind:"real",domain:"land",title:"Burke and Wills",sub:"the Victorian Exploring Expedition",
 years:"1860–61",colour:"#8a6d3f",
 stat:{out:"19 men, 26 camels, 23 horses and six wagons of supplies, leaving Melbourne",
       back:"one man, John King, found alive with the Yandruwandha community that had been feeding him",
       days:396,note:"Melbourne to the Gulf of Carpentaria and back: about 2,000 miles each way, the first south–north crossing of the continent, achieved by a party that then died completing it."},
 gist:"The best-funded and most lavishly equipped expedition in this atlas, and the one whose disaster is most obviously self-inflicted: Burke split his party three times against advice, missed his own depot camp by a matter of hours on the way back, and died within reach of a cache of food and water he had walked past without recognizing the marked tree above it.",
 legs:[
 {x:144.96,y:-37.79,p:"Royal Park, Melbourne",d:"20 Aug 1860",c:3,n:"A crowd of some 15,000 saw them off on an expedition equipped with, among other things, a cedar-topped oak table and rockets — the best-supplied party ever to leave the colony, and the first to use camels on this scale."},
 {x:142.42,y:-32.39,p:"Menindee",d:"Oct 1860",c:3,k:"turn",n:"The last outpost of settlement, and where Burke split the party for the first time, against nearly everyone's advice, to push ahead faster with a smaller group and let the rest follow at their own pace."},
 {x:140.73,y:-27.62,p:"Cooper Creek depot camp",d:"Nov 1860",c:3,k:"turn",n:"A base camp under William Brahe, with orders to wait three months. Burke took Wills, Charles Gray and John King and four months of supplies for a dash to the Gulf, intending to be back well inside that window."},
 {x:140.0,y:-25.0,p:"The Sturt Stony Desert",d:"Dec 1860–Jan 1861",c:2,n:"Wet-season conditions Burke had not planned for turned firm ground to bog for weeks at a stretch, eating into a schedule that had no slack in it to begin with."},
 {x:139.5,y:-17.5,p:"The Gulf of Carpentaria",d:"9 Feb 1861",c:3,k:"landfall",n:"They never actually saw open water: mangrove swamp blocked the last approach to the coast, and they turned back having smelled salt air rather than sighted the sea — the technical completion of the crossing resting on that alone."},
 {x:140.5,y:-24.0,p:"The return march",d:"Apr 1861",c:3,k:"death",n:"Charles Gray died on the way back, of exhaustion and dysentery, and the burial delayed the remaining three by a crucial half-day."},
 {x:140.73,y:-27.62,p:"Cooper Creek, again",d:"21 Apr 1861",c:3,k:"turn",n:"They reached the depot tree to find Brahe's party had left that same morning, after waiting four and a half months rather than the ordered three, having judged — correctly, if not in time — that the advance party was lost. A message and supplies lay buried under the tree, marked DIG."},
 {x:140.0,y:-29.7,p:"Toward Mount Hopeless",d:"May–Jun 1861",c:2,n:"Too weak to catch Brahe, they tried instead for a South Australian police outpost, failed, and turned back a third time to the depot — where, by extraordinary bad luck, Brahe, sent back by the search parties to check the cache once more, had already come, found no new message, and left again only days before."},
 {x:140.68,y:-27.68,p:"Death near Cooper Creek",d:"Jun 1861",c:3,k:"death",n:"Burke and Wills died within days of each other, kept alive for weeks beforehand on nardoo, a fern the Yandruwandha processed to remove a toxin the expedition did not know had to be removed. King survived because the Yandruwandha fed and sheltered him until a relief party found him in September."}
]},

/* ============================================================
   INVENTED — SEA (8)
   ============================================================ */

/* ---------------------------------------------------------- 17 */
{id:"odyssey",kind:"fiction",domain:"sea",title:"The Odyssey",sub:"Odysseus of Ithaca",
 years:"c. 8th c. BC",colour:"#b8763a",
 stat:{out:"12 ships, some 600 men",back:"Odysseus alone",days:3650,
       note:"Ten years from Troy, of which seven were spent on Ogygia and one with Circe."},
 gist:"Almost every monster in the poem is inside a story Odysseus tells to the Phaeacians while sitting in a chair on Corfu. The pale track is where the telling goes; the solid one is where the body actually is.",
 told:{x:19.92,y:39.62,p:"Scheria (Corfu), Books 9–12"},
 legs:[
 {x:26.24,y:39.96,p:"Troy",d:"Book 9",c:3,t:"told",n:"Twelve ships leave the beach at Ilium. Everything after this comes to us in his own voice."},
 {x:25.50,y:40.90,p:"Ismarus",d:"Book 9",c:3,t:"told",k:"landfall",n:"The Cicones, on the Thracian coast — a real town, and he admits to sacking it. The last identifiable place in the tale."},
 {x:23.20,y:36.43,p:"Cape Malea",d:"Book 9",c:3,t:"told",k:"turn",n:"The current takes him round the southern cape of the Peloponnese, and the map leaves the world.",v:[[26.83,36.5]]},
 {x:10.85,y:33.80,p:"The Lotus-eaters",d:"Book 9",c:1,t:"told",n:"Herodotus put the Lotophagi on the Libyan coast; the usual pin is Djerba. Nobody has found it because it is not there."},
 {x:15.16,y:37.56,p:"The Cyclopes",d:"Book 9",c:1,t:"told",n:"Thucydides records a Sicilian tradition placing them near Etna. Odysseus blinds Polyphemus and then shouts his own name at him, which costs him ten years."},
 {x:14.95,y:38.47,p:"Aeolia",d:"Book 10",c:1,t:"told",n:"Strabo's identification is the Lipari islands. The bag of winds is opened in sight of Ithaca by a crew who think it is treasure."},
 {x:9.16,y:41.39,p:"Telepylus",d:"Book 10",c:1,t:"told",k:"death",n:"Eleven ships speared like fish in a cliff-walled harbour. Bérard put it at Bonifacio, Pliny at Formiae, Thucydides in Sicily, and Crates of Mallus in the sub-arctic on the strength of the short nights."},
 {x:13.09,y:41.24,p:"Aeaea",d:"Books 10, 12",c:1,t:"told",n:"Monte Circeo by Roman tradition — though Homer says Circe lives where Dawn has her dwelling, which is the other end of the world."},
 {x:20.50,y:39.24,p:"The gate of Hades",d:"Book 11",c:1,t:"told",n:"On the leading identification, the Acheron mouth in Thesprotia: the entrance to the underworld is 150 km from his own front door, the shortest journey in the poem.",v:[[16.83,37.5]]},
 {x:14.42,y:40.57,p:"The Sirens",d:"Book 12",c:1,t:"told",n:"The Sirenusae off Sorrento. Wax in their ears and rope round his own chest, because he wanted both to survive and to hear it.",v:[[16.83,37.5]]},
 {x:15.63,y:38.25,p:"Scylla and Charybdis",d:"Book 12",c:2,t:"told",k:"death",n:"The Strait of Messina, the one fabulous place nearly everyone agrees on. Six men taken, and he had not told them it was coming."},
 {x:14.30,y:37.10,p:"Thrinacia",d:"Book 12",c:1,t:"told",k:"wreck",n:"The cattle of the Sun, a month of contrary wind, and a starving crew. Everyone else dies here, which leaves no witnesses to any of it.",v:[[15.17,36.5]]},
 {x:14.25,y:36.04,p:"Ogygia",d:"Book 5",c:1,n:"Seven years with Calypso, and the only leg of the wanderings the poet vouches for in his own voice. Gozo by Maltese tradition; Plutarch put it in the Atlantic."},
 {x:19.92,y:39.62,p:"Scheria",d:"Books 6–13",c:2,k:"landfall",n:"Corfu, on Thucydides' identification. He washes up naked, is fed, and tells the story — after being shown, by a blind singer, that a story can be worth a great deal."},
 {x:20.71,y:38.42,p:"Ithaca",d:"Books 13–24",c:2,n:"Put ashore asleep. Then eleven books of lying to everyone he meets, in real and reachable places: Crete, Egypt, Phoenicia, Thesprotia. The lies are all mappable. The truths are not.",v:[[20.17,38.83]]}
]},

/* ---------------------------------------------------------- 18 */
{id:"aeneid",kind:"fiction",domain:"sea",title:"The Aeneid",sub:"Aeneas out of Troy",
 years:"c. 29–19 BC",colour:"#a04545",
 stat:{out:"20 ships",back:"7 reach the Tiber",days:2555,
       note:"Seven years from the fall of Troy to the Latin shore."},
 gist:"Virgil's answer to Homer: the same sea, run backwards. Where Odysseus is trying to get home, Aeneas is looking for a home he has never seen, and the poem's first six books are a refugee convoy with a state to found.",
 told:{x:10.32,y:36.85,p:"Carthage, Books 2–3"},
 legs:[
 {x:26.24,y:39.96,p:"Troy",d:"Book 2",c:3,t:"told",k:"turn",n:"The sack, the horse, Laocoön, the night. Narrated at a dinner in Carthage to a queen who is already in love with him, which is exactly how the Odyssey does it."},
 {x:26.75,y:39.50,p:"Antandros",d:"Book 3",c:3,t:"told",n:"Twenty ships built under Ida in the first summer after the city fell."},
 {x:26.08,y:40.72,p:"Thrace",d:"Book 3",c:2,t:"told",n:"He starts to found a city, pulls up a shrub, and it bleeds and speaks: Polydorus, murdered and buried there. They leave the same day."},
 {x:25.27,y:37.39,p:"Delos",d:"Book 3",c:3,t:"told",n:"The oracle tells them to seek their ancient mother. Anchises guesses Crete, and is wrong."},
 {x:24.9,y:35.4,p:"Crete",d:"Book 3",c:2,t:"told",n:"Pergamea founded, and plague. The household gods appear at night to say the ancient mother is Italy.",v:[[26.83,36.5]]},
 {x:21.0,y:37.25,p:"The Strophades",d:"Book 3",c:2,t:"told",n:"The Harpies foul the meal, and Celaeno prophesies that they will not build their city until hunger makes them eat their tables.",v:[[21.83,35.5]]},
 {x:20.02,y:39.75,p:"Buthrotum",d:"Book 3",c:3,t:"told",k:"landfall",n:"The strangest scene in the poem: Andromache and Helenus have built a miniature Troy in Epirus, with a little Xanthus and a false gate, and are living in it. Aeneas is being shown what he must not do.",v:[[19.17,37.83]]},
 {x:18.43,y:40.1,p:"The Italian heel",d:"Book 3",c:3,t:"told",n:"First sight of Italy at dawn, and four white horses on the shore — an omen read both ways, war and eventually peace."},
 {x:15.2,y:37.6,p:"Under Etna",d:"Book 3",c:3,t:"told",n:"They take off Achaemenides, a Greek left behind by Odysseus, and hear the Cyclops story from the losing side. Virgil is annexing Homer in public.",v:[[18.83,39.17]]},
 {x:12.51,y:38.02,p:"Drepanum",d:"Book 3",c:3,t:"told",k:"death",n:"Anchises dies here, and Aeneas ends his account: after everything, the loss he cannot narrate past.",v:[[14.17,39.5]]},
 {x:10.32,y:36.85,p:"Carthage",d:"Books 1, 4",c:3,k:"turn",n:"Juno's storm drives them onto the African coast. A year, a hunt, a cave, and then Mercury telling him to go. Dido builds her own pyre and he sees the light of it from the sea."},
 {x:12.51,y:38.02,p:"Drepanum again",d:"Book 5",c:3,n:"Funeral games for Anchises, and the Trojan women — sick of the sea and put up to it by Juno — set fire to the ships. Four are lost. He leaves the unwilling behind and sails with the rest."},
 {x:13.57,y:41.21,p:"Caieta",d:"Books 6–7",c:3,n:"Palinurus the helmsman goes overboard in a calm, and is the last man to die before landfall."},
 {x:14.07,y:40.84,p:"Cumae and Avernus",d:"Book 6",c:3,k:"turn",n:"The Sibyl, the golden bough, and the descent — the still centre of the poem. He is shown the future of Rome and comes back out through the gate of false dreams, which Virgil does not explain."},
 {x:12.28,y:41.75,p:"The mouth of the Tiber",d:"Book 7",c:3,k:"landfall",n:"They eat the flat bread they have been using as plates, and Ascanius says they are eating their tables. The prophecy is discharged, the voyage ends, and the second half of the poem is a war.",v:[[12.5,40.17]]}
]},

/* ---------------------------------------------------------- 19 */
{id:"pequod",kind:"fiction",domain:"sea",title:"The Pequod",sub:"Moby-Dick",
 years:"1851",colour:"#e07a5f",
 stat:{out:"about 30 hands",back:"Ishmael",days:420,
       note:"Sailed from Nantucket on Christmas Day; lost on the Line the following year."},
 gist:"A Nantucket whaler taking the standard commercial track — Atlantic grounds, the Cape, the Indian Ocean, the archipelagoes, Japan, the Line — with one deviation, which is that the captain has decided to spend it on a single fish.",
 told:{x:-77.0,y:-12.06,p:"Lima: the Town-Ho's story"},
 legs:[
 {x:-70.10,y:38.42,p:"Nantucket",d:"Ch. 22, Christmas Day",c:3,n:"Bildad singing psalms, Peleg kicking men aloft, and then both of them over the side into the pilot boat.",v:[[-77.5,-51.17],[-74.83,-53.5],[-68.5,-52.17],[-45.5,-28.83],[-39.5,-22.17],[-37.5,-13.5],[-33.5,-8.17],[-33.83,-5.5],[-63.83,24.5]]},
 {x:-28,y:38.5,p:"Azores ground",d:"Ch. 29–35",c:3,n:"Named in Chapter 51 as the first of four Atlantic cruising grounds. The ship is here while Ishmael builds his library of whales."},
 {x:-25,y:16,p:"Cape de Verde ground",d:"Ch. 36–46",c:3,n:"The doubloon nailed to the mainmast and the crew sworn in over crossed lances, somewhere on this ground."},
 {x:-36,y:-14,p:"South Atlantic",d:"Ch. 47–48",c:2,k:"turn",n:"The first lowering. Ahab's five stowaways appear from nowhere, and Ishmael's boat is swamped and lost overnight in fog."},
 {x:-52,y:-36,p:"On the Plate",d:"Ch. 50",c:3,n:"The third named ground. The Pequod crosses the Atlantic twice on this leg, which most published charts of the voyage quietly straighten out.",v:[[-39.5,-22.17],[-50.5,-33.17]]},
 {x:-8,y:-24,p:"The Carrol Ground",d:"Ch. 51",c:3,n:"Southerly from St Helena. The spirit-spout appears by moonlight and leads them on."},
 {x:19,y:-36,p:"Cape of Good Hope",d:"Ch. 51",c:3,n:"Cape Tormentoto, as called of yore."},
 {x:34,y:-42,p:"Off the Crozetts",d:"Ch. 52",c:3,k:"landfall",n:"The Goney, bleached white and four years out, the first of nine gams. Ahab's speaking trumpet falls in the sea."},
 {x:52,y:-46,p:"The Crozettes",d:"Ch. 58",c:3,n:"Steering north-eastward through meadows of brit, right whales mowing it like reapers."},
 {x:62,y:-38,p:"Toward Java",d:"Ch. 59",c:3,n:"The great white squid comes up — furlongs long, no face, and never explained or mentioned again."},
 {x:70,y:-30,p:"Indian Ocean",d:"Ch. 61",c:2,n:"Stubb kills the first sperm whale of the voyage, smoking throughout."},
 {x:85,y:-18,p:"The Jeroboam",d:"Ch. 71",c:2,k:"landfall",n:"Epidemic aboard, and Gabriel the Shaker prophet forbidding the hunt from a boat kept at arm's length."},
 {x:105,y:-6,p:"Straits of Sunda",d:"Ch. 87",c:3,k:"turn",n:"Malay proas astern and a herd ahead, hunter and hunted at once, and at the centre of it the enchanted calm where the cows suckle their young."},
 {x:111,y:-2,p:"Java Sea",d:"Ch. 93",c:2,k:"death",n:"Pip jumps twice; the second time the boat leaves him. He is picked up alive and mad.",v:[[110.17,-3.17]]},
 {x:115,y:7.5,v:[[110.17,-3.17],[107.83,-1.17],[107.5,1.17]],p:"The Samuel Enderby",d:"Ch. 100",c:2,k:"landfall",n:"Captain Boomer lost an arm to the same whale, laughs about it, and has the sense to leave him alone. Ahab hears one word — eastward — and goes."},
 {x:122,y:21,p:"The Bashee Isles",d:"Ch. 111",c:3,n:"Gliding by them into the Pacific: the most exact and most exultant sentence of position in the book."},
 {x:138,y:31,p:"The Japan ground",d:"Ch. 114",c:3,n:"Long calm weeks, the sea like a gold meadow, and three men looking at the same water and saying three incompatible things about it."},
 {x:152,y:30,p:"The typhoon",d:"Ch. 119",c:2,n:"Corpusants burning white at all three mastheads, and Ahab with his foot on Fedallah claiming the fire as his father."},
 {x:171,y:2,p:"The Rachel",d:"Ch. 128",c:3,k:"landfall",n:"Gardiner has lost a boat with his twelve-year-old son in it and begs for two days' help. Ahab has the news he wanted and will not stop."},
 {x:175,y:-0.5,p:"On the Line",d:"Ch. 133–135",c:1,k:"wreck",n:"Three days of chase, and the ship goes down with a sky-hawk nailed to her mast. Melville never gives a longitude, so this pin is a guess between the Marshalls and the Gilberts.",v:[[172.83,-0.5]]}
]},

/* ---------------------------------------------------------- 20 */
{id:"sindbad",kind:"fiction",domain:"sea",title:"Sindbad's seven voyages",sub:"the Thousand and One Nights",
 years:"c. 9th–10th c.",colour:"#c9a227",
 stat:{out:"seven times",back:"seven times, each time richer",days:0,
       note:"Told in a single afternoon in Baghdad to a porter of the same name."},
 gist:"Seven voyages out of Basra, each following the same shape: shipwreck, marvel, fortune, home. The geography is the real Indian Ocean trade — the Gulf, Malabar, Serendib, the Zanj coast, China — with the monsters put in the gaps.",
 told:{x:44.36,y:33.31,p:"Baghdad: the whole thing"},
 legs:[
 {x:47.81,y:30.51,p:"Basra",d:"every voyage",c:3,n:"Down the Shatt al-Arab, which is where every real Gulf merchant of the ninth century started too. The frame is a rich man explaining to a poor man of the same name why the difference is not injustice.",v:[[48.5,29.5],[48.83,29.83]]},
 {x:58.0,y:22.0,p:"The island that was a whale",d:"First voyage",c:1,t:"told",k:"wreck",n:"They land, light a fire, and the island submerges. Sindbad floats away on a wooden trough. The motif is older than the Nights and turns up in the Physiologus as the aspidochelone."},
 {x:73.0,y:4.0,p:"King Mihrjan's isle",d:"First voyage",c:1,t:"told",n:"He washes up, is taken into service inspecting the harbour, and one day his own goods are landed off a passing ship with his name still on the bales."},
 {x:80.7,y:7.3,p:"The Valley of Diamonds",d:"Second voyage",c:1,t:"told",n:"Left behind by his ship, he is carried off by a roc, and then escapes a valley of serpents by strapping himself under a carcass thrown down by diamond-hunters. Marco Polo reports the same technique, as fact, from Ceylon.",v:[[80.83,4.5],[83.17,6.5],[81.83,8.17]]},
 {x:93.0,y:10.0,p:"The hairy men and the giant",d:"Third voyage",c:1,t:"told",k:"death",n:"The Andaman coast in the ninth-century sailing directions is full of warnings about cannibals. The one-eyed giant roasting the crew is Polyphemus, arrived by sea from the other end of the same ocean."},
 {x:75.5,y:11.5,p:"The buried-alive kingdom",d:"Fourth voyage",c:1,t:"told",n:"A country where a widowed spouse is entombed with the dead. He marries locally, his wife dies, and he is lowered into a cave of bones with seven loaves and a jug of water.",v:[[86.5,9.83],[80.5,4.5],[75.17,8.83]]},
 {x:45.0,y:0.0,p:"The Old Man of the Sea",d:"Fifth voyage",c:1,t:"told",n:"He carries the old man on his shoulders for weeks and is freed only by getting him drunk. The Zanj coast, where the real trade in ambergris and slaves ran."},
 {x:80.6,y:7.9,p:"Serendib",d:"Sixth voyage",c:2,t:"told",k:"landfall",n:"Sri Lanka, and the one place in the seven voyages named on a real chart. He climbs the mountain where Adam's footprint is, and carries a letter from its king to Harun al-Rashid — two rulers who genuinely exchanged embassies."},
 {x:112.0,y:10.0,p:"The far eastern sea",d:"Seventh voyage",c:1,t:"told",n:"The last voyage runs beyond India towards China, into a sea where merchants grow wings once a month. He comes home for good and endows the frame story.",v:[[79.5,8.83],[78.5,6.83],[80.5,4.5],[92.83,4.5],[95.17,6.83],[97.83,6.83],[103.5,2.83]]},
 {x:47.81,y:30.51,p:"Basra",d:"seven times",c:3,n:"Each voyage ends with the same sentence and the same resolution never to go again, which he keeps for about a paragraph."}
]},

/* ---------------------------------------------------------- 21 */
{id:"gulliver",kind:"fiction",domain:"sea",title:"Gulliver's Travels",sub:"Lemuel Gulliver, surgeon",
 years:"1699–1715",colour:"#6a8caf",
 stat:{out:"four voyages",back:"four times, progressively less able to bear other people",days:5900,
       note:"Sixteen years and seven months abroad, by his own reckoning."},
 gist:"Swift gives latitudes and longitudes throughout, in the deadpan register of the voyage literature he is parodying, and they are gloriously unreliable — Brobdingnag is a peninsula sitting on top of the Pacific coast of North America.",
 told:{x:-0.05,y:51.50,p:"Redriff: written up afterwards"},
 legs:[
 {x:-2.60,y:51.45,p:"Bristol",d:"4 May 1699",c:3,n:"Ship's surgeon on the Antelope, bound for the South Seas. Swift furnishes the departures with exactly the detail a real voyage narrative would."},
 {x:142.0,y:-30.5,p:"Lilliput",d:"Voyage I",c:1,t:"told",k:"wreck",n:"Wrecked at 30°2' south, and the 1726 map puts Lilliput and Blefuscu north-west of Van Diemen's Land — which is to say, in the middle of Australia. Swift either did not care or wanted you to notice."},
 {x:-170.0,y:46.0,p:"Brobdingnag",d:"Voyage II",c:1,t:"told",n:"A peninsula of the north-west coast of America, per the map, roughly where British Columbia is. The King hears an account of English institutions and concludes the natives are the most pernicious race of little odious vermin nature ever suffered to crawl upon the earth."},
 {x:155.0,y:42.0,p:"Laputa and Balnibarbi",d:"Voyage III",c:1,t:"told",n:"East of Japan: a flying island of mathematicians who cannot build a house with square corners, over a country ruined by an Academy of projectors extracting sunbeams from cucumbers."},
 {x:160.0,y:44.0,p:"Luggnagg",d:"Voyage III",c:1,t:"told",k:"turn",n:"The Struldbruggs, born immortal and therefore condemned to grow indefinitely old. Gulliver's enthusiasm on hearing of them, and what he is then shown, is the cruellest passage Swift ever wrote."},
 {x:129.87,y:32.75,p:"Nagasaki",d:"Voyage III",c:3,t:"told",n:"He passes through the one real and verifiable place in the book, and gets out of trampling on the crucifix by pretending to be Dutch.",v:[[153.5,43.83],[150.5,42.5],[139.83,31.83],[133.83,31.83],[130.5,29.17],[128.83,31.17]]},
 {x:128.0,y:-45.0,p:"Houyhnhnmland",d:"Voyage IV",c:1,t:"told",k:"landfall",n:"South of Australia on the map. Rational horses and filthy human Yahoos. He is expelled for being too like the second, comes home, and cannot stand the smell of his own wife.",v:[[123.17,25.17],[118.5,15.83],[106.83,4.17],[107.17,-4.5],[105.17,-6.83],[111.5,-13.83],[111.5,-25.83],[113.5,-29.17],[113.5,-34.17],[121.5,-42.17]]},
 {x:-0.05,y:51.50,p:"Redriff",d:"5 Dec 1715",c:3,n:"Rotherhithe, writing it all up, and spending four hours a day talking to two horses in the stable. The frame insists on its own truthfulness right up to the last page."}
]},

/* ---------------------------------------------------------- 22 */
{id:"argo",kind:"fiction",domain:"sea",title:"The Argo",sub:"Apollonius, Argonautica",
 years:"3rd c. BC",colour:"#9b7fbf",
 stat:{out:"about 50 heroes",back:"most of them",days:120,
       note:"Four months, on Apollonius' reckoning, out and back."},
 gist:"Out along a real trade route to the Black Sea, and home by a route that is geographically impossible — up the Danube and out into the Adriatic. Apollonius knew it was impossible and did it anyway.",
 legs:[
 {x:23.0,y:39.32,p:"Pagasae",d:"Book 1",c:3,n:"Fifty heroes, a ship with a talking beam of Dodonian oak in her prow, and a king who has sent Jason for the fleece expecting him not to come back."},
 {x:25.25,y:39.90,p:"Lemnos",d:"Book 1",c:3,n:"An island whose women have killed every man on it, and the crew stays long enough that Heracles has to shout at them from the beach."},
 {x:27.88,y:40.39,p:"Cyzicus",d:"Book 1",c:3,k:"death",n:"Blown back to a shore they have just left as friends, in the dark, and they fight their hosts and kill the king before the light shows them what they have done."},
 {x:28.9,y:40.4,p:"Mysia",d:"Book 1",c:3,n:"Hylas is pulled into a spring by a nymph, and Heracles will not leave without him. The strongest man in the crew is written out at the earliest opportunity."},
 {x:29.9,y:41.2,p:"Bebrycia",d:"Book 2",c:2,n:"Amycus makes all comers box him. Polydeuces takes the fight and kills him with a punch behind the ear."},
 {x:28.1,y:41.9,p:"Salmydessus",d:"Book 2",c:3,k:"turn",n:"Phineus, blind and starved by the Harpies, is rescued and pays them with the sailing directions for everything ahead. It is the exact structural equivalent of a portolan."},
 {x:29.13,y:41.23,p:"The Symplegades",d:"Book 2",c:3,n:"The clashing rocks at the Bosporus. They loose a dove, watch it lose its tail feathers, and row through on the recoil losing only an ornament from the stern."},
 {x:35.15,y:42.03,p:"Sinope",d:"Book 2",c:3,n:"Along the Anatolian shore of the Black Sea, past the Amazons, through country that any Greek trader of the period could have named for you.",v:[[32.17,43.17]]},
 {x:41.67,y:42.15,p:"Colchis",d:"Books 3–4",c:3,k:"landfall",n:"The Phasis. Medea does everything: the ointment, the sleeping dragon, the fleece. Book 3 is the first real love story in European literature and Jason is barely in it."},
 {x:29.7,y:45.2,p:"Mouth of the Ister",d:"Book 4",c:2,n:"Pursued, they do not go back the way they came. They go up the Danube."},
 {x:21.0,y:44.8,p:"Up the Danube",d:"Book 4",c:1,n:"Apollonius believed, or affected to believe, a geography in which the Ister forked and one branch ran to the Adriatic. It does not. This is the most confident wrong turning in ancient literature."},
 {x:15.0,y:44.0,p:"Out into the Adriatic",d:"Book 4",c:1,k:"death",n:"Absyrtus, Medea's brother, is lured out and murdered by Jason at a shrine, and Medea holds the ambush open. The poem never lets either of them off it."},
 {x:12.3,y:44.9,p:"The Eridanus",d:"Book 4",c:1,n:"Up the Po, where Phaethon fell and the poplars weep amber, and the stench of the burning is still on the water."},
 {x:4.85,y:43.4,p:"The Rhône",d:"Book 4",c:1,n:"Across from one river system to another as though Europe were a lagoon, and out into the western sea."},
 {x:13.09,y:41.24,p:"Aeaea",d:"Book 4",c:1,n:"Circe, who is Medea's aunt, purifies them for the murder and then will not have them in the house.",v:[[5.83,41.83]]},
 {x:15.63,y:38.25,p:"Scylla and the Planctae",d:"Book 4",c:2,n:"Thetis and the Nereids pass the ship between the rocks hand to hand like a ball, which is Apollonius solving Homer's hardest passage by making it prettier."},
 {x:19.92,y:39.62,p:"Drepane",d:"Book 4",c:2,k:"turn",n:"Corcyra, and the Colchian pursuit demands Medea back unless she is married. Arete arranges the wedding overnight in a cave, on a bed spread with the fleece.",v:[[17.17,37.5]]},
 {x:18.5,y:30.9,p:"The Syrtes",d:"Book 4",c:2,k:"wreck",n:"A wave throws the Argo far up into the Libyan shallows, and the crew carry her on their shoulders for twelve days across the desert to Lake Tritonis."},
 {x:24.0,y:35.3,p:"Crete",d:"Book 4",c:3,n:"Talos, the bronze man who circles the island three times a day, is killed by Medea from the deck, at a distance, by the evil eye and a single vein in his ankle."},
 {x:25.77,y:36.35,p:"Anaphe",d:"Book 4",c:3,n:"A black night with no stars until Apollo strikes a light. The poem is nearly out of magic by now and running on ritual explanation.",v:[[26.17,33.83]]},
 {x:23.0,y:39.32,p:"Pagasae",d:"Book 4",c:3,n:"Home, and Apollonius stops. What Medea does next in Iolcus and in Corinth is Euripides' business.",v:[[26.5,37.5]]}
]},

/* ---------------------------------------------------------- 23 */
{id:"mariner",kind:"fiction",domain:"sea",title:"The Ancient Mariner",sub:"Coleridge, 1798",
 years:"1798",colour:"#5f9ea0",
 stat:{out:"a crew of 200",back:"the Mariner, and the ship sinks in sight of home",days:0,
       note:"No dates. The poem measures time in thirst and in the position of the sun."},
 gist:"The one voyage here with no coordinates at all. Coleridge gives you a direction and a latitude of feeling — south, then ice, then the Line, then home — and every pin below is a reasonable person's guess.",
 told:{x:-3.5,y:51.2,p:"Outside a wedding, three doors down"},
 legs:[
 {x:-3.5,y:51.2,p:"The harbour",d:"stanza 1",c:1,n:"The kirk, the hill, the lighthouse top, and a wedding guest stopped on the way in by a man with a glittering eye. Everything after this is inside his account."},
 {x:-25.0,y:0.0,p:"Below the kirk, below the hill, below the line",d:"Part I",c:1,t:"told",k:"turn",n:"The sun comes up on the left and sets on the right: he is running south down the Atlantic, and Coleridge tells you so by where the sun is, which is how a sailor would."},
 {x:-55.0,y:-62.0,p:"The land of ice",d:"Part I",c:1,t:"told",n:"Mast-high, green as emerald, and the noise of it — cracked and growled and roared and howled. Coleridge had never seen ice and got it from Frederick Martens' Spitzbergen voyage."},
 {x:-62.0,y:-65.0,p:"The albatross",d:"Part I–II",c:1,t:"told",k:"death",n:"Wordsworth suggested the bird, out of Shelvocke's 1719 privateering voyage, in which a mate shot a black albatross off Cape Horn believing it caused the contrary winds. The crime and its motive are both borrowed.",v:[[-53.83,-63.5],[-56.17,-65.83],[-61.5,-65.5]]},
 {x:-95.0,y:-25.0,p:"North into the Pacific",d:"Part II",c:1,t:"told",n:"A good south wind, and the crew reverse their verdict on the killing as soon as the weather improves — which is the poem's clearest moral observation and the one nobody quotes."},
 {x:-115.0,y:0.0,p:"The silent sea",d:"Part II–IV",c:1,t:"told",k:"wreck",n:"Becalmed on the Line: the bloody sun at noon, the painted ship, the water burning green and blue and white, and two hundred men dying one by one with their eyes on him. The whole centre of the poem happens at a dead stop."},
 {x:-115.0,y:0.0,p:"The spectre-bark",d:"Part III",c:1,t:"told",n:"Death and Life-in-Death throw dice for the crew, and she wins him. The sun goes down between the ribs of her hull as through a grate."},
 {x:-60.0,y:20.0,p:"Borne northward",d:"Part V–VI",c:1,t:"told",n:"He blesses the water-snakes unaware, the albatross falls off, and the ship is moved home without wind by something under her keel that he is not permitted to see."},
 {x:-3.5,y:51.2,p:"His own countree",d:"Part VI–VII",c:1,n:"The same harbour bar, the same weathercock. The ship goes down like lead, the Hermit shrieves him, and he is left with a compulsion to tell it that comes back at uncertain intervals for the rest of his life."}
]},

/* ---------------------------------------------------------- 24 */
{id:"nautilus",kind:"fiction",domain:"sea",title:"The Nautilus",sub:"Twenty Thousand Leagues Under the Seas",
 years:"1867–68",colour:"#3d7a8c",
 stat:{out:"Aronnax, Conseil, Ned Land — involuntarily",back:"all three, out of the Maelstrom",days:232,
       note:"About ten months and, by Verne's count, 20,000 leagues — roughly twice round the world."},
 gist:"The most precisely charted voyage in this atlas after Bligh's, because Verne posts positions like a ship's log. He also sends the Nautilus through a tunnel under Suez and stands Nemo on the South Pole two years before anyone had seen the Antarctic mainland properly.",
 told:{x:2.35,y:48.86,p:"Aronnax's memoir, written after"},
 legs:[
 {x:136.7,y:31.25,p:"Off Japan",d:"Nov 1867",c:3,n:"The Abraham Lincoln, hunting a monster that has been holing ships, is holed. Aronnax, his servant and a Canadian harpooner go over the side and are taken aboard the thing itself.",v:[[1.17,50.17],[-4.5,50.17],[-6.17,48.5],[-10.5,43.17],[-10.83,37.17],[-19.17,28.83],[-18.83,14.5],[-14.17,7.5],[10.5,-17.17],[16.5,-33.17],[19.5,-36.17],[27.83,-34.5],[35.83,-26.83],[45.5,-26.83],[50.5,-22.83],[66.5,-21.17],[93.17,5.5],[97.83,6.83],[103.5,2.83],[122.83,22.83]]},
 {x:-155.0,y:20.0,p:"The North Pacific",d:"Nov 1867",c:3,n:"Aronnax is shown a library of twelve thousand volumes, an organ, and a man who has renounced the land entirely and will not say why."},
 {x:166.9,y:-11.65,p:"Vanikoro",d:"Dec 1867",c:3,k:"turn",n:"The wreck of La Pérouse's expedition, lost in 1788 and only identified in 1826. Verne uses a real maritime mystery as a set piece, which is the whole method of the book."},
 {x:142.5,y:-10.5,p:"Torres Strait",d:"Jan 1868",c:3,k:"wreck",n:"Aground on a coral shelf for several days, waiting on the tide, with Papuan canoes closing in and Ned Land wanting his freedom badly enough to eat unripe breadfruit for it."},
 {x:79.9,y:8.9,p:"The Ceylon pearl banks",d:"Jan 1868",c:3,n:"A walk on the sea floor, a diver, and a shark. Nemo saves the man's life and gives him a bag of pearls, then remarks that he is an oppressed Indian and Nemo is on his side to the last.",v:[[127.17,-9.83],[122.83,-12.17],[106.5,-8.83],[104.5,-6.83],[102.17,-6.83],[92.17,3.17],[89.17,4.5],[80.5,4.5],[78.5,6.83]]},
 {x:43.0,y:12.6,p:"The Red Sea",d:"Feb 1868",c:3,n:"In through Bab el Mandeb, and then Nemo announces there is a natural tunnel under the isthmus. There is not."},
 {x:32.55,y:29.97,p:"The Arabian Tunnel",d:"Feb 1868",c:1,k:"turn",n:"Suez to Pelusium in twenty minutes at forty knots, under the desert. Verne's one flat impossibility in an otherwise fanatically researched book, and he brazens it out with a lot of confident hydrography."},
 {x:25.4,y:36.4,p:"Santorini",d:"Feb 1868",c:3,n:"Through the Mediterranean in forty-eight hours, past an underwater eruption that boils the sea around the hull."},
 {x:-8.75,y:42.24,p:"Vigo Bay",d:"Feb 1868",c:3,n:"The Spanish treasure fleet sunk in 1702. This is where Nemo's money comes from, and where he tells Aronnax what he does with it: he funds rebellions.",v:[[18.5,35.5],[14.17,39.5],[11.17,39.5],[8.83,37.83],[3.83,38.5],[-1.83,36.17],[-8.83,35.83],[-10.83,38.83]]},
 {x:-25.0,y:32.0,p:"Atlantis",d:"Feb 1868",c:1,n:"A midnight walk up the slope of a drowned volcano to look down on the ruins of a city, by the light of the eruption. No dialogue: Nemo writes the name on a rock and that is all."},
 {x:-60.0,y:-60.0,p:"The ice barrier",d:"Mar 1868",c:3,n:"South until the pack stops them, and then Nemo takes the ship under the ice, which nobody would do for another eighty years.",v:[[-24.83,19.17],[-26.83,17.17],[-26.83,12.17],[-33.5,-2.17],[-33.5,-8.17],[-37.5,-13.5],[-39.5,-22.17],[-55.83,-40.5],[-55.83,-51.5]]},
 {x:0.0,y:-85.0,p:"The South Pole",d:"21 Mar 1868",c:1,k:"landfall",n:"He plants a black flag with a gold N. In 1869 nobody had established that Antarctica was a continent, and Verne gives Nemo open water and a beach. Then the Nautilus is trapped under an overturned iceberg and they nearly suffocate.",v:[[-125.83,-60.17],[-139.5,-73.83],[-169.83,-73.83],[178.5,-85.5],[0.17,-85.17]]},
 {x:-45.0,y:-5.0,p:"Off the Amazon",d:"Apr 1868",c:3,n:"North again, the giant squid, and the one fight in the book that costs a life: a crewman taken off the platform by a tentacle, and Nemo weeping over it.",v:[[178.5,-85.5],[-149.5,-53.5],[-74.83,-53.5],[-68.5,-52.17],[-39.5,-22.17],[-37.5,-13.5],[-33.5,-6.5],[-39.83,-1.5],[-42.5,-2.5]]},
 {x:-45.0,y:45.0,p:"The Gulf Stream",d:"May–Jun 1868",c:3,k:"death",n:"A warship of an unnamed nation attacks; the Nautilus rams her below the waterline and Nemo watches her go down with all hands, in front of a portrait of a dead woman and two children."},
 {x:12.9,y:67.9,p:"The Maelstrom",d:"Jun 1868",c:3,k:"wreck",n:"Off the Lofotens, the ship drives into the whirlpool — whether by Nemo's decision or his despair, Verne does not say. The three prisoners wake in a fisherman's hut and the Nautilus is never accounted for."}
]},

/* ============================================================
   INVENTED — LAND (8)
   ============================================================ */

/* ---------------------------------------------------------- 25 */
{id:"huck",kind:"fiction",domain:"land",title:"Huck and Jim's raft",sub:"Adventures of Huckleberry Finn",
 years:"1884",colour:"#8a9a5b",
 stat:{out:"two, and various passengers who should not have been let on",back:"both alive",days:60,
       note:"Some weeks in high summer, down about 1,100 river miles."},
 gist:"The only voyage in this atlas with a current instead of a wind, and the only one whose entire tragedy is a missed turning. Cairo is the pivot: the Ohio was the road north to freedom, they pass it in fog, and every mile after that carries Jim deeper into slave country.",
 river:"mississippi",
 legs:[
 {x:-91.36,y:39.71,p:"St Petersburg",d:"ch. 1",c:2,n:"Hannibal, Missouri under a different name, forty years before Twain wrote it and already gone."},
 {x:-91.34,y:39.65,p:"Jackson's Island",d:"ch. 7–11",c:2,k:"turn",n:"Huck fakes his own murder and hides on the island, and finds Jim already there, running because he has heard Miss Watson mean to sell him down to New Orleans."},
 {x:-91.0,y:39.2,p:"The Walter Scott",d:"ch. 12–13",c:1,k:"wreck",n:"A steamboat broken on a rock with three murderers aboard arguing about whether to leave the third to drown. Huck steals their skiff and then, unable to leave it, tries to get them rescued."},
 {x:-90.19,y:38.63,p:"Past St Louis",d:"ch. 12",c:2,n:"A whole city passed in the dark, all lights and no people. The raft chapters are night chapters; the daylight ones are all ashore, and all worse."},
 {x:-89.6,y:37.5,p:"The Grangerfords",d:"ch. 17–18",c:1,k:"death",n:"A house with a parlour organ and a dead daughter's sentimental verses, and a thirty-year feud in which nobody can remember the original offence. It ends with boys shot in the river."},
 {x:-89.18,y:37.00,p:"Cairo, missed",d:"ch. 15–16",c:3,k:"turn",n:"Fog on the river, the raft and the canoe separated, and they go past the Ohio mouth without seeing it. That is the turning north. Everything after this is the wrong direction, and both of them know it."},
 {x:-90.0,y:36.0,p:"The Duke and the Dauphin",d:"ch. 19–20",c:1,n:"Two confidence men swim out to the raft and take it over by claiming to be royalty, and Huck lets them, having concluded that the best way to get along with that kind is to let them have their own way."},
 {x:-90.3,y:35.4,p:"Bricksville",d:"ch. 21–23",c:1,k:"death",n:"Colonel Sherburn shoots the drunk Boggs in the street in front of his daughter, and then disperses the lynch mob with a speech about their cowardice from his porch roof. Twain does not undercut it."},
 {x:-90.6,y:34.4,p:"The Wilks funeral",d:"ch. 24–29",c:1,n:"The con men impersonate the English brothers of a dead man to steal from his orphaned nieces, and Huck, who has gone along with everything until now, starts stealing the money back."},
 {x:-91.2,y:33.4,p:"The Phelps farm",d:"ch. 31–43",c:1,k:"landfall",n:"Jim is sold for forty dollars. Huck writes the letter that would turn him in, and then tears it up — All right, then, I'll go to hell — which is the moral centre of American literature, followed immediately by twelve chapters of Tom Sawyer ruining it."}
],
ghost:{label:"the Ohio: the way north they missed",pts:[[-89.18,37.00],[-88.60,37.08],[-87.57,37.97],[-85.76,38.26],[-84.51,39.10]]}},

/* ---------------------------------------------------------- 26 */
{id:"marlow",kind:"fiction",domain:"land",title:"Marlow up the Congo",sub:"Heart of Darkness",
 years:"1899",colour:"#6b705c",
 stat:{out:"one steamboat, a pilgrim cargo",back:"Marlow, and a packet of letters",days:240,
       note:"Conrad made the same journey himself in 1890 and it wrecked his health for good."},
 gist:"A frame inside a frame: an unnamed man on a yawl in the Thames repeating what Marlow told him about a river 4,000 miles away. The two rivers are deliberately the same river, and the book says so in its first pages.",
 told:{x:0.37,y:51.44,p:"The Nellie, on the Thames"},
 river:"congo",
 legs:[
 {x:0.37,y:51.44,p:"Gravesend",d:"the frame",c:3,n:"Four men waiting for the tide on a cruising yawl, and Marlow saying that this too has been one of the dark places of the earth. The story is told to the sound of the Thames going out."},
 {x:4.35,y:50.85,p:"Brussels",d:"ch. 1",c:2,t:"told",n:"The sepulchral city, and an office with a map of Africa coloured by empire, where two women in black knit and a doctor measures his skull and asks whether there is madness in his family."},
 {x:-17.0,y:14.7,p:"Down the coast",d:"ch. 1",c:1,t:"told",n:"Thirty days on a French steamer landing soldiers and customs officers at trading posts with names like a farce, and once a man-of-war shelling an empty continent."},
 {x:13.05,y:-5.85,p:"The mouth",d:"ch. 1",c:2,t:"told",k:"landfall",n:"Boma, and then the Company Station at Matadi. A boiler wallowing in the grass, an undersized railway truck on its back, and a chain gang of men called criminals."},
 {x:13.46,y:-5.82,p:"The grove of death",d:"ch. 1",c:2,t:"told",k:"death",n:"Men who have crawled off into the shade of the trees to die, and among them the Company's chief accountant in a starched collar, boned cuffs and a snowy cravat, keeping his books in apple-pie order."},
 {x:14.4,y:-5.1,p:"The caravan",d:"ch. 1",c:2,t:"told",n:"Two hundred miles overland round the cataracts, fifteen days on foot with sixty carriers, past a dead man in the path with a bullet hole in his forehead."},
 {x:15.31,y:-4.32,p:"The Central Station",d:"ch. 1",c:2,t:"told",k:"turn",n:"Kinshasa, and his steamboat at the bottom of the river. Three months waiting for rivets that never come, among pilgrims with staves who talk about ivory the way other men talk about religion."},
 {x:18.26,y:0.05,p:"Up the river",d:"ch. 2",c:2,t:"told",n:"Travelling back to the earliest beginnings of the world, an empty stream, a great silence, an impenetrable forest — and Marlow entirely occupied with not running the boat onto a snag, which is what saves him."},
 {x:22.47,y:2.19,p:"The attack in the fog",d:"ch. 2",c:2,t:"told",k:"death",n:"Arrows out of the bank a mile and a half below the station, and the African helmsman speared through the side. Marlow's shoes fill with the man's blood and he throws them overboard, and cannot say why it upset him so much."},
 {x:25.19,y:0.52,p:"The Inner Station",d:"ch. 2–3",c:2,t:"told",k:"landfall",n:"Stanley Falls. A house, a Russian in harlequin patches, and posts topped with heads turned inward. Kurtz had come out with a report for the Society for the Suppression of Savage Customs, seventeen pages of eloquence, with a note scrawled at the foot of the last page."},
 {x:20.0,y:1.5,p:"Downriver",d:"ch. 3",c:2,t:"told",k:"death",n:"Kurtz dies in his bunk with the manager's steward announcing dinner. Marlow's account of the last words is the most quoted sentence in the book and he heard it, he says, in a whisper."},
 {x:4.35,y:50.85,p:"The Intended",d:"ch. 3",c:2,t:"told",n:"Back in the sepulchral city, in a drawing room with a grand piano like a sarcophagus, he is asked what Kurtz said at the end, and lies — and says he could not have done otherwise, because the truth would have been too dark altogether."},
 {x:0.37,y:51.44,p:"The Thames",d:"the frame",c:3,n:"Marlow stops, indistinct and silent in the pose of a meditating Buddha, and the narrator looks up to find the tide has turned and the offing is barred by a black bank of clouds."}
]},

/* ---------------------------------------------------------- 27 */
{id:"lonesomedove",kind:"fiction",domain:"land",title:"Lonesome Dove",sub:"the Hat Creek cattle drive",
 years:"1876 (novel setting)",colour:"#5c6b73",
 stat:{out:"about ten thousand head of cattle and a dozen or so hands, leaving a played-out Texas border town",
       back:"a handful of drovers, several thousand cattle, and one corpse packed in charcoal for three thousand miles because of a promise",
       days:300,note:"Lonesome Dove, Texas, to the Milk River country of Montana: roughly two thousand miles, the first drive north across open range before the railroads and the fences closed it."},
 gist:"A cattle drive undertaken less for the cattle than for the land at the far end of it — Call wants to be first onto unclaimed Montana grass before someone else gets there — and the book keeps finding reasons for that motive to look worse the further north they get, ending with Call hauling his dead partner's body the length of the drive to bury him back in Texas, a promise nobody asked of him and that does nobody any good.",
 legs:[
 {x:-99.5,y:27.5,p:"Lonesome Dove, Texas",d:"1876",c:1,n:"A played-out town on the Rio Grande where two former Texas Rangers have been running a small outfit for years out of habit rather than purpose. The drive starts as a way to stop standing still."},
 {x:-99.7,y:34.2,p:"The Red River crossing",d:"1876",c:1,k:"wreck",n:"A stampede and a nest of water moccasins in the same crossing, one of several disasters that read, cumulatively, less like bad luck than like the country itself objecting to ten thousand cattle being driven through it."},
 {x:-100.5,y:35.8,p:"North through the Panhandle",d:"1876",c:1,n:"Real cattle-trail geography, borrowed wholesale from the actual Western Trail that historical drovers used in this decade, laid under a wholly invented cast."},
 {x:-101.72,y:41.13,p:"Ogallala, Nebraska",d:"1876",c:1,k:"turn",n:"The railhead where a real drive would have sold out and stopped. This one keeps going, because Call's actual object was never the cattle market — it was the unfenced land past it."},
 {x:-105.8,y:44.5,p:"The Powder River country",d:"1876",c:1,k:"death",n:"Blue Duck's raiders and a rattlesnake pit account for two of the book's more gratuitous deaths here, in territory the drive has no real business crossing except that it is the most direct line north."},
 {x:-105.84,y:46.41,p:"The Yellowstone crossing",d:"1876",c:1,k:"death",n:"Gus McCrae is wounded by Native raiders near here and dies of the gangrene that follows rather than of the wound itself — a death the book takes its time over more than any other in it."},
 {x:-108.0,y:46.9,p:"The Musselshell country, Montana",d:"1876",c:1,k:"landfall",n:"The unclaimed grass Call had been driving toward the entire book, reached with the herd decimated, half the original hands dead, and Gus already buried once in Montana ground before Call digs him up again."},
 {x:-99.5,y:27.5,p:"Back to Texas",d:"epilogue",c:1,n:"Call hauls Gus's coffin, packed in charcoal against the smell, the length of the journey in reverse to bury him where he'd asked, near Lonesome Dove — a promise kept at a cost nobody watching the drive would have judged worth it, which is exactly the point the novel is making about him."}
]},

/* ---------------------------------------------------------- 28 */
{id:"bloodmeridian",kind:"fiction",domain:"land",title:"Blood Meridian",sub:"the kid, and the Glanton gang",
 years:"1849–50 (novel setting)",colour:"#7a1f1f",
 stat:{out:"the kid, alone, then absorbed into a scalp-hunting company of roughly thirty",
       back:"the kid, alone, twenty-eight years later, and almost certainly murdered by Judge Holden in an outhouse the novel declines to show directly",
       days:550,note:"Nacogdoches to the Sonora desert and back and back again: a few thousand miles of a border the party never actually leaves for long."},
 gist:"Not a journey with a destination so much as a loop: the Glanton gang is contracted to hunt Apache scalps for bounty and drifts instead into killing indiscriminately along the Texas–Chihuahua–Sonora line, doubling back across the same stretch of desert so often that the geography starts to feel less like a route than a trap the party has built for itself.",
 legs:[
 {x:-94.66,y:31.60,p:"Nacogdoches, Texas",d:"c. 1849",c:1,n:"The kid's starting point, and about the only fixed biographical fact the novel gives him — no name is ever supplied, before or after."},
 {x:-98.49,y:29.42,p:"San Antonio and Bexar",d:"1849",c:1,n:"He falls in first with a filibustering expedition under Captain White, doomed almost immediately, before drifting toward the border proper and the Glanton company."},
 {x:-108.19,y:30.89,p:"Janos, Chihuahua",d:"1849",c:2,k:"turn",n:"The gang is contracted here by the governor of Chihuahua to bring in Apache scalps at a bounty, on paper a straightforward commercial arrangement; almost immediately they start killing anyone whose hair will pass, Mexican villagers included."},
 {x:-106.07,y:28.63,p:"Chihuahua City",d:"1849",c:1,k:"landfall",n:"A triumphal entry with a wagonload of scalps and a hero's welcome, followed within a chapter by the same city turning on them once the killing of its own citizens becomes impossible to ignore."},
 {x:-110.60,y:31.13,p:"The Sonora desert",d:"1849–50",c:1,k:"death",n:"The gang's operations shift west into Sonora as their welcome in Chihuahua runs out, the killing continuing under a bounty that has effectively stopped mattering to anyone involved."},
 {x:-114.62,y:32.72,p:"The Yuma Crossing",d:"1850",c:2,k:"death",n:"The gang seizes a profitable ferry operation from the Yuma people by force, then is massacred there in turn when the Yuma retake it — the closest the book comes to a conventional narrative reversal, and it happens almost entirely offstage."},
 {x:-112.5,y:31.5,p:"The desert crossing, the survivors",d:"1850",c:1,k:"wreck",n:"The kid and a handful of survivors cross the desert on foot with essentially no supplies, an ordeal the prose renders in the same flat, geological register it uses for the massacres — neither event is allowed to read as more significant than the other."},
 {x:-106.49,y:31.76,p:"Back across the border",d:"1850s",c:1,n:"Years pass in the gap the novel leaves open between the massacre and the epilogue; the kid drifts through the decades of Comanche wars and Texas Ranger violence that follow without the text ever quite anchoring him to a specific event again."},
 {x:-99.25,y:32.93,p:"Fort Griffin, Texas",d:"1878",c:1,k:"death",n:"Twenty-eight years later, the kid — now called the man — meets Judge Holden again, unaged, in a saloon, and follows him to the outhouse behind it. The novel does not describe what happens there, only a witness's later account of what is found, and Holden dancing, elsewhere, still very much alive."}
]},

/* ---------------------------------------------------------- 29 */
{id:"lolita",kind:"fiction",domain:"land",title:"Lolita",sub:"Humbert Humbert and Dolores Haze",
 years:"1947–52 (novel setting)",colour:"#a8628f",
 stat:{out:"two, in a stolen kind of custody",
       back:"Humbert, alone, to prison and a fatal heart attack; Dolores, married and pregnant, dies in childbirth a few months after him, per the fictive editor's foreword",
       days:1825,note:"Two round trips across the whole country, a year apart, staying in what Humbert counts as 342 motels."},
 gist:"The famous first road trip is a year-long circuit designed to keep a captive audience of one from ever standing still long enough to ask for help; the less-remembered second trip retraces almost the same roads a year later, this time with Humbert as the one being followed, by a man he cannot identify and Lolita will not name.",
 legs:[
 {x:-72.68,y:41.76,p:"Ramsdale, New England",d:"1947",c:1,n:"Humbert takes the room, marries the mother for access to the daughter, and inherits sole custody of a twelve-year-old within weeks of the mother's death under the wheels of a car — a plot mechanism so blunt that Nabokov has Humbert comment on its own contrivance."},
 {x:-83.5,y:34.5,p:"Into the South",d:"1947",c:1,n:"The first thousand miles are Humbert's own itemized account of using motel courts, drive-ins and roadside attractions to keep a child in a state of permanent transit and permanent dependence."},
 {x:-99.0,y:31.0,p:"Across Texas",d:"1947",c:1,n:"Nabokov, who drove these roads himself collecting butterflies, gives the landscape more precise attention than almost any American novelist of the period, in the mouth of a narrator who is using that same landscape as a trap."},
 {x:-112.11,y:36.06,p:"The Grand Canyon and the Painted Desert",d:"1947",c:1,k:"turn",n:"The tourist attractions Humbert catalogues become, over the trip, a kind of alibi: proof, retrospectively, of a normal father-daughter vacation, offered to a reader he already knows will not believe him."},
 {x:-119.7,y:36.6,p:"Kasbeam, California",d:"1947",c:1,n:"A haircut Humbert gets here recurs, oddly, in his memory more than almost anything else on the trip — one of the novel's small, unexplained fixations."},
 {x:-122.33,y:47.61,p:"North to the Pacific Northwest",d:"1947",c:1,n:"The northernmost point of the first circuit before turning back east, completing something closer to a loop than a straight crossing."},
 {x:-82.9,y:40.0,p:"Beardsley, Ohio",d:"1947–48",c:1,k:"turn",n:"A year of settled life and a school enrolment, ended when Humbert realizes — correctly — that Dolores has been arranging an escape, and that the drama teacher directing her school play is connected to it."},
 {x:-98.0,y:38.5,p:"The second circuit, west again",d:"1948",c:1,k:"turn",n:"A near-exact retracing of the first year's route, this time with Humbert increasingly certain, and correctly so, that another car is following them — Clare Quilty's, though he cannot yet put the name to it."},
 {x:-106.0,y:39.3,p:"Elphinstone, Colorado",d:"1948",c:1,k:"death",n:"Dolores disappears from a hospital where Humbert has left her recovering from an illness, and is collected by Quilty posing as an uncle. Humbert spends the next two years searching, fruitlessly, for a pattern in hotel registers he cannot decode."},
 {x:-120.5,y:47.0,p:"Coalmont",d:"1952",c:1,n:"Three years later, a letter from a married, pregnant Dolores Schiller leads him here for their last meeting, and the confession — of Quilty, not of anything he imagines she owes him — that sends him to find and kill Quilty at Pavor Manor, back in New England, before his own arrest and death in custody."}
]},

/* ---------------------------------------------------------- 30 */
{id:"kim",kind:"fiction",domain:"land",title:"Kim",sub:"Kimball O'Hara and the Tibetan lama",
 years:"1890s (novel setting)",colour:"#c46210",
 stat:{out:"a boy and an old lama, on foot and by rail",
       back:"both, the lama having found the River he sought and Kim recruited, along the way, into the Great Game",
       days:900,note:"Lahore to the Himalayan foothills and back down the Grand Trunk Road, with side trips by rail the length of northern India. Kipling gives no continuous calendar; this reconstructs a plausible sequence over roughly Kim's early teenage years."},
 gist:"Two journeys running on top of each other without either character fully admitting it to the other: the lama is walking the Grand Trunk Road in search of a river of spiritual purification that may not exist, while Kim, ostensibly his disciple and guide, is simultaneously being trained and used as a courier in the British intelligence service's rivalry with Russia for the frontier.",
 legs:[
 {x:74.31,y:31.55,p:"Lahore",d:"ch. 1",c:3,n:"Kim, an orphaned Irish soldier's son passing as a native street child, meets the lama at the Zam-Zammah gun outside the museum and attaches himself as guide, partly from curiosity and partly because it beats work."},
 {x:74.87,y:31.63,p:"The Grand Trunk Road, eastbound",d:"ch. 3",c:3,k:"turn",n:"Kipling's set-piece description of the road as a river of humanity — every caste, trade and pilgrimage of northern India moving on it at once — is the book's most quoted passage and the clearest statement of what it is actually about: not the plot, but the road."},
 {x:76.78,y:30.38,p:"Umballa",d:"ch. 2",c:2,n:"Kim delivers a message here for a horse-trader who is, unknown to him at this point, a British intelligence agent — the first thread of the espionage plot laid into what still reads as a picaresque travelogue."},
 {x:83.01,y:25.32,p:"Benares",d:"ch. 4",c:2,n:"The lama's own former monastery, and a river — the actual Ganges — that is explicitly not the River he is looking for, though it takes him some time to be sure of that."},
 {x:80.95,y:26.85,p:"St Xavier's, Lucknow",d:"ch. 5–7",c:3,k:"turn",n:"Kim's English blood is discovered by an Anglican chaplain and a Catholic priest, and he is sent to school here against both his own wishes and the lama's, who pays the fees himself out of a monastery's collected alms."},
 {x:77.21,y:28.61,p:"Summer holidays on the road",d:"ch. 8–9",c:2,n:"Kim slips back into disguise and native life every vacation, apprenticed on the side to Mahbub Ali and then to Lurgan Sahib in the tradecraft — memory games, disguise, observation — that the Great Game runs on."},
 {x:77.17,y:31.10,p:"Simla",d:"ch. 9–10",c:3,k:"turn",n:"The colonial government's summer capital in the hills, and the base of the intelligence network Kim is being folded into almost without his noticing the shift from adventure to employment."},
 {x:78.25,y:31.53,p:"The northern frontier hills",d:"ch. 13–14",c:1,k:"turn",n:"Kim's actual mission: intercepting and neutralizing two foreign agents — a Russian and a Frenchman — surveying the frontier, in the book's closest approach to a conventional spy-novel climax."},
 {x:78.5,y:31.7,p:"The high Himalayan foothills",d:"ch. 15",c:2,k:"landfall",n:"The lama, exhausted by the same journey that has just been Kim's espionage triumph, finally experiences the vision he has been walking toward for the whole book and locates, to his own satisfaction, the River."},
 {x:77.55,y:29.97,p:"Back down to the plains",d:"ch. 15",c:2,n:"Kim, sick from the strain of the mission, is nursed by the lama, who has given away the money set aside for his own final pilgrimage to pay for it — the clearest statement the book makes of which of its two plots it actually values."}
]},

/* ---------------------------------------------------------- 31 */
{id:"newsun",kind:"fiction",domain:"land",title:"The Book of the New Sun",sub:"Severian of the Guild of Torturers",
 years:"far future (novel setting); mapped onto South America",colour:"#6e5a7d",
 stat:{out:"one journeyman torturer, exiled",
       back:"the same man, now Autarch and shortly to be the vessel of a star-bringing entity, having become in the meantime both more and less than what he started as",
       days:0,note:"Nessus north to Thrax and into the mountains beyond. Urth's geography is Wolfe's invention, but he gave it a real scale and a real river system, which maps cleanly onto the Río de la Plata basin and the Andes; no calendar is given, so no day count is offered."},
 gist:"A guild torturer exiled from his city for the mercy of giving a condemned prisoner a quick death instead of a slow one, sent north with the same sword he will later use to behead people professionally in a mining town, on a journey that keeps turning out — very slowly, and only in the last volume — to have been about something much larger than his own disgrace.",
 legs:[
 {x:-58.40,y:-34.60,p:"Nessus, on the river Gyoll",d:"vol. 1",c:1,n:"The dying capital of a dying empire, its river running the wrong colour from millennia of dumped waste, at the mouth of a great estuary that Wolfe's own scale notes put comfortably at the latitude of Buenos Aires."},
 {x:-58.40,y:-34.60,p:"Exile from the Citadel",d:"vol. 1",c:1,k:"turn",n:"Exiled for the mercy killing of Thecla, a prisoner he had fallen for during her long torture, and sent to be the new lictor of a distant mining town — a punishment posing as a promotion."},
 {x:-60.64,y:-32.95,p:"North through the pampas",d:"vol. 1",c:1,n:"A landscape Wolfe deliberately keeps disorienting: technology that reads as magic, ruins that are clearly our own civilization's, seen from a distance of enough millennia that Severian cannot recognize them for what they are and the reader mostly can."},
 {x:-60.0,y:-28.0,p:"Saltus",d:"vol. 1",c:1,n:"A town built partly out of the ruins of an earlier city, its economy running on the salvage — Wolfe's word for it is chiliads-old scrap — that gives the region its name."},
 {x:-65.22,y:-26.82,p:"The ascent toward the mountains",d:"vol. 2",c:1,k:"turn",n:"The land rises toward the range that will define the rest of the journey, and the war against the Ascians — a genuinely alien, propaganda-speaking enemy from the far side of the continent — begins to be felt as a presence rather than a rumour."},
 {x:-65.41,y:-24.79,p:"Thrax",d:"vol. 2",c:1,k:"landfall",n:"The City of Windowless Rooms, a mining and mint town built into a canyon, where Severian takes up his post as lictor — the executioner's job he was trained for and had, until now, never actually performed alone."},
 {x:-66.5,y:-23.0,p:"Flight into the mountains",d:"vol. 2–3",c:1,k:"turn",n:"Accused, wrongly, of freeing a prisoner, Severian flees Thrax into higher country, beginning the long central stretch of the book that is as much about the strange fauna and topography of a far-future Urth as about the plot."},
 {x:-68.15,y:-16.50,p:"The war zone near the Wall",d:"vol. 3",c:1,k:"death",n:"Conscripted into the war against the Ascians almost by accident, in country that reads, at this altitude and latitude, like the altiplano: thin air, high cold plains, and an enemy fighting for reasons the text never lets Severian, or the reader, fully understand."},
 {x:-58.40,y:-34.60,p:"Return, as Autarch",d:"vol. 4",c:1,k:"turn",n:"By the fourth volume Severian has become Autarch of the Commonwealth almost by process of elimination, the least likely candidate in the book having simply survived and been present at the right deaths — his own rise to power told in the same flat, unemphatic tone as everything else that has happened to him. The New Sun of the title is a promise made, and, across the sequels Wolfe wrote afterward, eventually kept — ending the neat equivalence a reader might have relied on up to this point."}
]},

/* ---------------------------------------------------------- 32 */
{id:"lotr",kind:"fiction",domain:"land",title:"The Lord of the Rings",sub:"Frodo Baggins and the Fellowship",
 years:"Third Age 3018–19 (novel setting); mapped onto Europe per Tolkien's own stated latitudes",colour:"#5a7d5a",
 stat:{out:"nine companions, then four, then two, then one and his gardener",
       back:"four hobbits; Boromir dead, Gandalf dead and returned, and the Ring itself destroyed rather than carried home",
       days:407,note:"About 1,800 miles by the book's own internal scale — the plotted figure below runs longer, because Tolkien's map is smaller than the equivalence he himself set. He fixed it in a 1967 letter: the Shire at Oxford's latitude, Minas Tirith at Florence's, the mouths of the Anduin at ancient Troy's. Held to those latitudes rather than to Middle-earth's own mileage, the walk stretches to fit the real distance between them."},
 gist:"Tolkien told his own correspondents the equivalence outright, fixing the Shire's latitude at Oxford's and Gondor's capital at Florence's; taken at his own word, the quest maps onto a walk from England across the Alps and down through the Balkans to somewhere in the volcanic country near the Black Sea, which is roughly where illustrators and cartographers converge anyway when they try to pin Mordor down.",
 legs:[
 {x:-1.26,y:51.75,p:"Hobbiton, the Shire",d:"Sep 3018",c:2,n:"Frodo inherits the Ring on Bilbo's eleventy-first birthday and leaves later than Gandalf wanted, once it becomes clear that Sauron's servants are already looking for it."},
 {x:0.5,y:51.3,p:"Bree",d:"Sep 3018",c:2,k:"turn",n:"The first place hobbits and other free peoples of the world routinely mix, and where Aragorn, disguised as the ranger Strider, attaches himself to the party in a tavern that any reader of the period's adventure fiction would recognize as the genre's standard departure point."},
 {x:6.5,y:50.5,p:"Weathertop",d:"Oct 3018",c:2,k:"death",n:"Attacked at night by the Ringwraiths; Frodo is stabbed with a Morgul blade that begins turning him toward the wraith world, a wound that will not fully heal for the rest of the book."},
 {x:9.0,y:51.0,p:"Rivendell",d:"Oct–Dec 3018",c:2,k:"turn",n:"Elrond's council decides, after considerable argument among representatives of every free people in the story, that the Ring must be destroyed rather than used, hidden, or given to anyone — the plot's actual decision, made by committee."},
 {x:8.5,y:46.5,p:"The Misty Mountains and Moria",d:"Jan 3019",c:2,k:"death",n:"Turned back from the high pass by weather, or by Saruman, the Fellowship goes under the mountains instead, through the abandoned dwarf-kingdom of Khazad-dûm, where Gandalf falls fighting a Balrog on the bridge and the party loses its leader at roughly the journey's halfway point."},
 {x:10.5,y:45.5,p:"Lothlórien",d:"Jan–Feb 3019",c:2,n:"An elven refuge on the far side of the mountains where the Fellowship recovers and is given gifts that will matter later, and Galadriel is tested by the offer of the Ring and refuses it — one of the few moments in the book where a powerful character is offered absolute power and simply declines."},
 {x:19.0,y:45.5,p:"The Great River, at Amon Hen",d:"Feb 3019",c:2,k:"turn",n:"Boromir tries to take the Ring by force, fails, and dies defending Merry and Pippin from an orc raid moments later — the Fellowship's actual breaking point, after which the story splits into three separate journeys the book cuts between rather than telling in sequence."},
 {x:24.0,y:43.0,p:"The Dead Marshes",d:"Feb–Mar 3019",c:1,n:"Frodo and Sam, guided now by Gollum, cross a landscape of drowned corpses from an ancient battle, in the sequence generally read as the book's clearest use of First World War battlefield imagery — which Tolkien always denied intending as allegory, without ever quite denying the resemblance."},
 {x:41.0,y:42.0,p:"Cirith Ungol and Mount Doom",d:"Mar 3019",c:1,k:"turn",n:"Sam carries Frodo the last distance up the mountain after Frodo can no longer walk, and at the very end Frodo claims the Ring for himself rather than destroying it. The story's actual climax turns on his failure: Gollum's own greed, biting the Ring from his hand and falling into the fire with it, finishes the job Frodo could not."},
 {x:-1.26,y:51.75,p:"The Shire, on the return",d:"Nov 3019",c:2,n:"The four hobbits come home changed in ways the Shire itself has not, and find it under the petty tyranny of Saruman's men — a final, deliberately anticlimactic conflict the book insists on including rather than ending on the mountain, on the theory that a quest this large has to cost something at home too."}
]}
];
