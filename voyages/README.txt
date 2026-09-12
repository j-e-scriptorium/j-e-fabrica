THIRTY-TWO JOURNEYS — an atlas
===============================

Open index.html in any browser. No server, no internet, nothing to install.
These files must stay together in the same relative layout — this folder,
plus ../assets/worldmap.js one level up.

  index.html          the site — layout, map drawing, interaction
  voyages.js          the thirty-two journeys and their stages. This is the file to edit.
  basemap.js          exhibit-specific map data: ocean/sea labels (SEAS) only
  ../assets/worldmap.js   world coastlines, land dots, 50 rivers, and the decoder
                          (LAND_ENC, LAND_DOTS, RIVERS, decodeLand()) — the ACTUAL
                          map data, shared with ../strata/ rather than copied. If
                          you add, move, or fix a coastline or river, it changes
                          for both exhibits, since there is only the one file.
  README.txt          this file

Sixteen journeys are real and sixteen are invented; sixteen are by sea and
sixteen are over land (a river counts as land). Each journey carries both a
kind ("real" or "fiction") and a domain ("sea" or "land"), so the menu is
four groups rather than two.

USING IT
  Click a journey's name to chart it.
  Click the + beside a name to add it to a comparison; click + again to remove it.
  Two or more selected switches to comparison: a latitude profile, then a table.
  Drag the map to pan, scroll to zoom, or use the buttons at the top right of the map.
  Left and right arrow keys step through the stages of a single journey.

READING THE MAP
  Solid track      a journey that happened
  Dashed track     an invented one
  Faint dotted     a prologue (the Endurance drift, the Bounty's outward passage)
  Light dashed     the part being narrated rather than happening — Odysseus talking
                   to the Phaeacians, Marlow on the Thames, Aeneas at Dido's table
  Filled square    position documented, or explicitly stated in the text
  Half-tone disc   inferred from a fixed point nearby
  Hollow ring      notional — somebody's proposal, usually a contested one

  Sea tracks are routed around land, so ships go round a cape rather than
  through it. Land tracks are drawn as plain straight lines between waypoints
  (with occasional hand-placed via points for a mountain pass or river bend) —
  crossing land is the point, so there is no routing to avoid it.

ADDING OR EDITING A JOURNEY
  Open voyages.js in a text editor. Each journey is one block. A stage looks like:

    {x:-70.10, y:41.28, p:"Nantucket", d:"Christmas Day", c:3, n:"A note.", k:"landfall"}

    x  longitude in degrees, negative for west
    y  latitude in degrees, negative for south
    p  place name (shown on the map and as the stage heading)
    d  date or chapter reference — optional
    c  how firm the position is: 3 documented/stated, 2 inferred, 1 notional
    n  the note shown in the panel
    k  optional marker: "landfall", "death", "wreck", "turn"
    t  optional track: "told" (narrated within the story) or "pro" (before the voyage)
    v  optional list of via points — see below

  Each journey object also carries kind:"real"/"fiction" and domain:"sea"/"land",
  which decide which of the four menu rows it appears in and whether its track
  is drawn solid or dashed. Get both right or a new entry will render invisibly
  in the wrong chip row rather than erroring.

  Distances, the latitude profile, label placement and map framing all recalculate
  themselves. If the page comes up blank after an edit you have almost certainly
  dropped a comma or a brace; the browser's developer console will name the line.

THE v: FIELD — IMPORTANT IF YOU MOVE A WAYPOINT
  For a sea journey, courses are routed around land rather than drawn straight,
  so ships go round the Cape instead of through it. Those courses were computed
  once by search over an ocean grid and baked into the data as v:[[lon,lat],...]
  on the arriving stage. Land journeys generally don't need this — a straight
  line across a continent is exactly the point — but a via point or two can
  still help a track hug a river or a mountain pass believably.

  If you change a stage's x or y, DELETE the v:[...] on that stage and on the one
  after it. Otherwise the old detour will still be drawn and the track will bend
  towards a coast (or a river bend) that is no longer on the route. Removing v:
  simply gives you a straight line again, which is usually fine for short legs.
