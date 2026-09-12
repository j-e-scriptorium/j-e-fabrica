/* Exhibit-specific map helpers for Strata. The coastlines, land dots,
   rivers, and the decodeLand() decoder are shared with Thirty-Two Journeys
   and live in ../../assets/worldmap.js — load that script before this one.
   This file just turns that shared data into GeoJSON for Leaflet. */

/* land as a Leaflet-ready GeoJSON MultiPolygon, plus the too-small-to-be-a-
   polygon islands as points (LAND_DOTS, [lon,lat] pairs already). Rings are
   closed explicitly, since decodeLand()'s rings only close visually via an
   SVG "Z" in the voyages map and are not literally first===last here. */
function landGeoJSON(){
  var rings=decodeLand().map(function(r){
    var closed=r.slice();
    var a=closed[0],b=closed[closed.length-1];
    // +180 and -180 are the same meridian: a ring clipped there closes
    // fine even though the two endpoints don't match numerically.
    var av=a[0]===180?-180:a[0], bv=b[0]===180?-180:b[0];
    if(av!==bv||a[1]!==b[1])closed.push([a[0],a[1]]);
    return closed;
  });
  return {type:'MultiPolygon',coordinates:rings.map(function(r){return [r];})};
}
function riversGeoJSON(){
  return {type:'MultiLineString',coordinates:Object.keys(RIVERS).map(function(k){return RIVERS[k];})};
}
/* lakes as a GeoJSON MultiPolygon. Unlike decodeLand()'s rings, LAKES'
   rings are already explicitly closed (first point === last), and none
   of them cross the antimeridian, so no extra handling is needed here. */
function lakesGeoJSON(){
  return {type:'MultiPolygon',coordinates:Object.keys(LAKES).map(function(k){return [LAKES[k]];})};
}
