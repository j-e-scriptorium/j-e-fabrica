TWENTY VOYAGES — an atlas
=========================

Open index.html in any browser. No server, no internet, nothing to install.
All four files must stay together in the same folder.

  index.html   the site — layout, map drawing, interaction
  voyages.js   the twenty voyages and their stages. This is the file to edit.
  basemap.js   world coastlines (Natural Earth 1:50m, public domain), rivers, sea labels
  README.txt   this file

USING IT
  Click a voyage name to chart it.
  Click the + beside a name to add it to a comparison; click + again to remove it.
  Two or more selected switches to comparison: a latitude profile, then a table.
  Drag the map to pan, scroll to zoom, or use the buttons at the top right of the map.
  Left and right arrow keys step through the stages of a single voyage.

READING THE MAP
  Solid track      a voyage that happened
  Dashed track     an invented one
  Faint dotted     a prologue (the Endurance drift, the Bounty's outward passage)
  Light dashed     the part being narrated rather than happening — Odysseus talking
                   to the Phaeacians, Marlow on the Thames, Aeneas at Dido's table
  Filled square    position documented, or explicitly stated in the text
  Half-tone disc   inferred from a fixed point nearby
  Hollow ring      notional — somebody's proposal, usually a contested one

ADDING OR EDITING A VOYAGE
  Open voyages.js in a text editor. Each voyage is one block. A stage looks like:

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

  Distances, the latitude profile, label placement and map framing all recalculate
  themselves. If the page comes up blank after an edit you have almost certainly
  dropped a comma or a brace; the browser's developer console will name the line.

THE v: FIELD — IMPORTANT IF YOU MOVE A WAYPOINT
  Sea tracks are routed around land rather than drawn straight, so ships go round
  the Cape instead of through it. Those courses were computed once by search over
  an ocean grid and baked into the data as v:[[lon,lat],...] on the arriving stage.

  If you change a stage's x or y, DELETE the v:[...] on that stage and on the one
  after it. Otherwise the old detour will still be drawn and the track will bend
  towards a coast that is no longer on the route. Removing v: simply gives you a
  straight line again, which is usually fine for short legs.
