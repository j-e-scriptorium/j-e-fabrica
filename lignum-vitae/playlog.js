// Reads the playtest logs the game saves (`l` in the game) and prints what
// they say about how the matches went: where the time went, what the hand
// did, what came of it, and whether the player came back for another.
//
//   node playlog.js lignum-vitae-playlog-*.json
//
// Several files may be named; a match that appears in more than one (the game
// keeps the last thirty, so successive saves overlap) is counted once.
const fs = require("fs");

const files = process.argv.slice(2);
if (!files.length){ console.log("usage: node playlog.js <playlog.json> [more.json …]"); process.exit(1); }
const seen = new Map();
for (const f of files)
  for (const m of JSON.parse(fs.readFileSync(f, "utf8"))) seen.set(m.at + "|" + m.ev.length, m);
const matches = [...seen.values()].sort((a, b) => a.at < b.at ? -1 : 1);

const ACTS = new Set(["bend", "shot", "volley", "ward", "miss", "graft", "sheathe", "rigid"]);
const IDLE = 10;          // seconds without the hand doing anything that count as waiting
const pct = (a, b) => b ? Math.round(100*a/b) + "%" : "—";
const f1 = x => x === null || x === undefined || isNaN(x) ? "—" : x.toFixed(1);
const mmss = s => Math.floor(s/60) + ":" + String(Math.floor(s % 60)).padStart(2, "0");
const picks = p => p ? [p.habit, p.grain, p.wood].join("/") : "?";

function read(m){
  const ev = m.ev, end = ev.find(e => e.k === "end");
  const last = end ? end.t : (ev.length ? ev[ev.length-1].t : 0);
  const count = k => ev.filter(e => e.k === k).length;
  const acts = ev.filter(e => ACTS.has(e.k));
  // waiting: stretches of game time with the hand off the tree. Pauses are
  // game time standing still, so they cost nothing here.
  let idle = 0, from = 0;
  for (const e of acts.concat(end ? [end] : [])){ if (e.t - from > IDLE) idle += e.t - from - IDLE; from = e.t; }
  const shots = ev.filter(e => e.k === "shot" || e.k === "volley");
  const firstShot = shots.length ? shots[0].t : null;
  const bends = ev.filter(e => e.k === "bend");
  // who was ahead, read off the cores as each hit landed, and how often that changed
  let mine = m.hp[0], theirs = m.hp[1], lead = 0, swaps = 0, worst = 0;
  for (const e of ev) if (e.k === "core"){
    if (e.foe) mine -= e.F; else theirs -= e.F;
    const now = Math.sign(mine/m.hp[0] - theirs/m.hp[1]);
    if (now && lead && now !== lead) swaps++;
    if (now) lead = now;
    worst = Math.max(worst, 1 - mine/m.hp[0] - (1 - theirs/m.hp[1]));
  }
  return {
    m, end: m.end || "unfinished", secs: last,
    bends: bends.length, bendMs: bends.length ? bends.reduce((a, e) => a + e.ms, 0)/bends.length/1000 : null,
    shots: count("shot"), volleys: count("volley"), wards: count("ward"), misses: count("miss"),
    grafts: count("graft"), hinted: ev.filter(e => e.k === "graft" && e.by === "hint").length,
    sheathes: count("sheathe"), rigid: count("rigid"), pauses: ev.filter(e => e.k === "pause" && e.on).length,
    aimed: shots.filter(e => e.into === "core").length, aimable: shots.filter(e => e.into).length,
    dealt: ev.filter(e => e.k === "core" && !e.foe).reduce((a, e) => a + e.F, 0),
    taken: ev.filter(e => e.k === "core" && e.foe).reduce((a, e) => a + e.F, 0),
    theirShots: count("their-shot"),
    caught: ev.filter(e => e.k === "ward-catch" && e.foe).length,
    stopped: ev.filter(e => e.k === "ward-catch" && e.foe && e.stopped).length,
    apm: last > 0 ? acts.length/(last/60) : 0, idle, firstShot, swaps, worst,
    strokes: count("shot") + count("volley") + count("ward") + count("miss")
  };
}
const R = matches.map(read);

console.log("\nMatch by match\n");
console.log("  when              you vs them                     temper   length  end           acts/min  waiting  1st shot  shots  vol  wards  grafts  put away  core dealt/taken  lead swaps");
for (const r of R){
  console.log("  " + [
    r.m.at.slice(0, 16).replace("T", " "),
    (picks(r.m.mine) + " v " + picks(r.m.theirs)).padEnd(30),
    String(r.m.foe).padEnd(7),
    mmss(r.secs).padStart(6),
    r.end.padEnd(12),
    f1(r.apm).padStart(8),
    pct(r.idle, r.secs).padStart(7),
    (r.firstShot === null ? "—" : mmss(r.firstShot)).padStart(8),
    String(r.shots).padStart(5), String(r.volleys).padStart(4), String(r.wards).padStart(6),
    String(r.grafts).padStart(7), String(r.sheathes).padStart(9),
    (f1(r.dealt) + " / " + f1(r.taken)).padStart(16),
    String(r.swaps).padStart(10)
  ].join("  "));
  const tuned = Object.keys(r.m.tuned || {});
  if (tuned.length) console.log("      tuned: " + tuned.map(k => k + "=" + r.m.tuned[k]).join(", "));
}

const sum = k => R.reduce((a, r) => a + (r[k] || 0), 0);
const done = R.filter(r => r.end === "won" || r.end === "lost");
const won = R.filter(r => r.end === "won").length;
// a rematch is a new match planted within two minutes of the last one ending
let rematches = 0, ended = 0;
for (let i = 0; i < R.length - 1; i++){
  if (!R[i].m.end) continue;
  ended++;
  const gap = (new Date(R[i+1].m.at) - new Date(R[i].m.at))/1000 - R[i].secs;
  if (gap < 120) rematches++;
}
const secs = sum("secs");
console.log("\nAcross " + R.length + " matches, " + mmss(secs) + " of play\n");
const line = (k, v, why) => console.log("  " + k.padEnd(34) + String(v).padEnd(14) + (why ? "  " + why : ""));
line("finished", done.length + " (" + won + " won)", "a match left with neither core spent was abandoned or is still open");
line("abandoned", R.filter(r => r.end === "abandoned").length, "replanted before anyone won: boredom, frustration, or a bad start");
line("came back for another", pct(rematches, ended), "the one number nearest to 'fun'");
line("median length", done.length ? mmss(done.map(r => r.secs).sort((a, b) => a - b)[done.length >> 1]) : "—");
line("hand actions a minute", f1(secs ? (R.reduce((a, r) => a + r.apm*r.secs, 0))/secs : 0));
line("waiting", pct(sum("idle"), secs), "game time with the hand off the tree for over " + IDLE + " s at a stretch");
line("first shot, on average", R.filter(r => r.firstShot !== null).length
     ? mmss(R.filter(r => r.firstShot !== null).reduce((a, r) => a + r.firstShot, 0)/R.filter(r => r.firstShot !== null).length) : "—");
line("strokes put away", pct(sum("sheathes"), sum("strokes") + sum("sheathes")), "second thoughts: high means the preview is doing its job, or the stroke is hard to draw");
line("strokes that cut nothing", pct(sum("misses"), sum("strokes")), "a blade that missed the wood it was drawn at");
line("tried to bend set wood", sum("rigid"), "reaching for something the tree no longer allows");
line("average bend", f1(sumBy(R, "bendMs", "bends")) + " s");
line("shots aimed into their core", pct(sum("aimed"), sum("aimable")), "as forecast when the blade bit");
line("volleys / shots / wards", sum("volleys") + " / " + sum("shots") + " / " + sum("wards"));
line("grafts (of them suggested)", sum("grafts") + " (" + sum("hinted") + ")");
line("their shots caught by a ward", pct(sum("caught"), sum("theirShots")) + ", " + sum("stopped") + " stopped");
line("lead changes a match", f1(R.length ? sum("swaps")/R.length : 0), "how often the cores' relative state flipped");
line("deepest hole climbed out of", (() => {
  const back = done.filter(r => r.end === "won").map(r => r.worst);
  return back.length ? Math.round(100*Math.max(...back)) + "% of a core behind" : "—";
})(), "comebacks: how far behind a won match ever was");

// the campaign, rung by rung
const bouts = new Map();
for (const r of R) if (r.m.bout){
  const b = bouts.get(r.m.bout) || { tries: 0, won: 0, ages: [] };
  b.tries++; if (r.end === "won") b.won++; b.ages.push(r.m.age || 0);
  bouts.set(r.m.bout, b);
}
if (bouts.size){
  console.log("\n  campaign bout   against   tries  won   your tree at the start");
  for (const [n, b] of [...bouts].sort((x, y) => x[0] - y[0])){
    const foe = (R.find(r => r.m.bout === n) || {}).m.foe;
    console.log("  " + String(n).padStart(13) + "   " + String(foe).padEnd(8) + String(b.tries).padStart(6) +
                String(b.won).padStart(5) + "   " + mmss(Math.min(...b.ages)) + "\u2013" + mmss(Math.max(...b.ages)));
  }
}
console.log("");

function sumBy(rs, k, w){
  let a = 0, n = 0;
  for (const r of rs) if (r[k] !== null){ a += r[k]*r[w]; n += r[w]; }
  return n ? a/n : null;
}
