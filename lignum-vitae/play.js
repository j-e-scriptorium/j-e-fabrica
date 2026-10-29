// A headless duel. Both trees grow on the same clock; this one shoots, and
// the other grows, heals and — given a temper — shoots back. Drives the real
// firing path: gather a fan by bending, weave loops by grafting, aim by the
// predicted closest pass, slice a limb, and watch what the shot actually does.
//
//   node play.js policy=loop turns=24
//   node play.js policy=aim mind=master     (the other mage plays)
//
// policies: naive  cut at random, shape nothing
//           random cut at random, bend at random
//           glow   cut whatever the charge glow says is brightest
//           aim    gather a fan, aim each cut by its predicted pass
//           loop   aim, and weave grafts so the loops amplify the shot
//
// seedlings: mine=broom,fine,dense  theirs=spear,open,light  (any order, any
//            subset; whatever is not named is the default for that axis)
// tempers:   mind=still|feral|keeper|master  (default still: it only grows)
const fs = require("fs");
const path = require("path");
const load = require(path.join(__dirname, "harness.js"));

const opt = {};
for (const a of process.argv.slice(2)){
  const [k,v] = a.split("=");
  opt[k] = v === undefined ? true : (isNaN(+v) ? v : +v);
}
const g = load(opt.file);
const S = g.S;
for (const k in opt) if (k in S) S[k] = opt[k];
// a seedling named by its options, in any order
function picks(str){
  const out = {};
  for (const w of String(str || "").split(",").filter(Boolean))
    for (const ax of g.AXES) if (w in g.TRAITS[ax].options) out[ax] = w;
  return out;
}
const MINE = g.genome(picks(opt.mine)), THEIRS = g.genome(picks(opt.theirs));
g.T = g.newTree(0, MINE);

let seed = opt.seed || 7;
const rnd = () => ((seed = (seed*1103515245 + 12345) & 0x7fffffff) / 0x7fffffff);

const POLICY = opt.policy || "loop";
const WARM   = opt.warm   || 240;
const TURNS  = opt.turns  || 24;
const GROW   = opt.grow   || 12;     // seconds of growth between turns
const FRAMES = opt.frames ? String(opt.frames).split("+").map(Number) : [];
const SHAPES = POLICY === "aim" || POLICY === "loop";

g.newFoe(THEIRS, opt.mind || "still", opt.seed || 7);
g.T.hpMax = g.T.hp = g.coreOf(g.T.g);
const MIND = g.TD.mind;
let theirShots = 0;
// both trees grow, on the same clock and out of the same rules; if the other
// mage has a temper it plays in real time while this one waits for its turn
const grow = s => {
  for (let t = 0; t < s; t += 0.05){
    if (g.T.hp > 0) g.step(g.T, 0.05, null);
    if (g.TD.hp > 0) g.step(g.TD, 0.05, null);
    if (MIND.lv.fires && g.T.hp > 0 && g.TD.hp > 0){
      g.layout(g.T); g.buildGrid(g.T);
      const b = g.mindStep(g.TD, MIND, 0.05, g.T);
      if (b){ g.launch(b, true); theirShots++; }
      g.layout(g.TD); g.buildGrid(g.TD);
    }
    if (g.bolts.length){ g.stepBolts(0.025); g.stepBolts(0.025); }
  }
  g.layout(g.T); g.layout(g.TD); g.buildGrid(g.TD); g.buildGrid(g.T);
};
grow(WARM);
g.measure();

// ── the player ─────────────────────────────────────────────────────────
function livingTips(){ return g.T.list.filter(n => n.bud); }
function cuttable(){ return g.T.list.filter(n => n.parent !== null && n.children.length); }

// Gathering a fan is bending, and nothing else: haul the tips inside a wedge
// toward one bearing. A cluster the plant made on its own is worth nothing;
// convergence is the whole of the player's contribution.
function gather(centre, halfWidth, passes){
  const inWedge = livingTips().filter(b => {
    let d = Math.atan2(b.y1, b.x1) - centre;
    while (d >  Math.PI) d -= 2*Math.PI;
    while (d < -Math.PI) d += 2*Math.PI;
    return Math.abs(d) < halfWidth;
  });
  if (!inWedge.length) return 0;
  for (let pass = 0; pass < (passes || 120); pass++){
    let any = false;
    for (const q of inWedge){
      if (!g.T.nodes.has(q.id)) continue;
      let d = Math.atan2(q.y1, q.x1) - centre;
      while (d >  Math.PI) d -= 2*Math.PI;
      while (d < -Math.PI) d += 2*Math.PI;
      if (Math.abs(d) < 0.02) continue;
      for (const n of g.bendGroup(g.T, q)){
        const lim = g.bendLimit(n); if (lim < 0.0005) continue;
        let off = n.rel - 0.03*Math.sign(d) - n.rest;
        while (off >  Math.PI) off -= 2*Math.PI;
        while (off < -Math.PI) off += 2*Math.PI;
        const was = n.rel;
        n.rel = n.rest + Math.max(-lim, Math.min(lim, off));
        n.rest = n.rel;                    // a pull, released, and taken again
        if (n.rel !== was) any = true;
      }
    }
    g.layout(g.T);
    if (!any) break;
  }
  return inWedge.length;
}

// Weaving. Two tips within reach fuse into one node and close a circuit, and
// the circuit is what multiplies every shot from here on. Which pair matters
// enormously: gain compounds on the area enclosed, so fusing two sibling twigs
// closes a lens worth almost nothing, while reaching a tip across to another
// limb entirely encloses half the canopy. A player takes the widest circuit
// the wood will let them close, and so does this.
function ancestry(n){
  const s = new Map();
  let q = n, L = 0;
  while (q){ s.set(q.id, L); L += q.len; q = q.parent === null ? null : g.T.nodes.get(q.parent); }
  return s;
}
function circuit(a, b){                 // perimeter of the loop a–b would close
  const up = ancestry(a);
  let q = b, L = 0;
  while (q){
    if (up.has(q.id)) return L + up.get(q.id);
    L += q.len; q = q.parent === null ? null : g.T.nodes.get(q.parent);
  }
  return 0;
}
function weave(want){
  let made = 0;
  for (let round = 0; round < want; round++){
    const buds = livingTips().filter(n => n.mate === null);
    let A = null, B = null, bestL = 0;
    for (let i = 0; i < buds.length; i++)
      for (let j = i+1; j < buds.length; j++){
        if (buds[i].parent === buds[j].parent) continue;
        if (Math.hypot(buds[i].x1-buds[j].x1, buds[i].y1-buds[j].y1) >= S.graftR) continue;
        const L = circuit(buds[i], buds[j]);
        if (L > bestL){ bestL = L; A = buds[i]; B = buds[j]; }
      }
    if (!A || !B) break;
    g.makeGraft(g.T, A, B); g.layout(g.T); made++;
  }
  return made;
}

function pickCut(){
  const c = cuttable();
  if (!c.length) return null;
  if (POLICY === "random" || POLICY === "naive") return c[Math.floor(rnd()*c.length)];
  let best = null;
  for (const n of c) if (!best || n.eff > best.eff) best = n;
  return best;
}

// Aim the way a player with the Aim arc up does: pull the stem behind the limb
// one way or the other, keep whichever pull brings the predicted closest pass
// nearer their core, and stop when neither does. A captured shot curves, so
// pointing the stem at the core is not the same thing as hitting it; the closed
// form the glow reads is.
function aimAt(limb){
  const p = g.T.nodes.get(limb.parent);
  if (!p) return 0;
  const peri = () => { g.bestSpire(g.T); return g.periapsis(g.muzzleFor(g.T, limb), g.targetOf(g.TD)); };
  let best = peri(), moved = 0, step = 0.02;
  for (let pass = 0; pass < 400 && best > S.coreR*0.5; pass++){
    const grp = g.bendGroup(g.T, p);
    const keep = grp.map(n => [n.rel, n.rest]);
    let improved = false;
    for (const dir of [1, -1]){
      let any = false;
      for (const n of grp){
        const lim = g.bendLimit(n); if (lim < 0.0005) continue;
        const was = n.rel;
        n.rel = n.rest + Math.max(-lim, Math.min(lim, dir*step));
        n.rest = n.rel;                              // a pull, released, taken again
        if (n.rel !== was) any = true;
      }
      g.layout(g.T);
      const now = any ? peri() : best;
      if (now < best - 1e-6){ best = now; improved = true; moved++; break; }
      grp.forEach((n, i) => { n.rel = keep[i][0]; n.rest = keep[i][1]; });
      g.layout(g.T);
    }
    if (!improved){ if (step < 0.003) break; step /= 2; }
  }
  g.bestSpire(g.T);
  return moved;
}

// ── firing, exactly as the interface does it ───────────────────────────
const log = [];
function fire(limb){
  const charge = g.greenOf(g.T, limb);
  const muzzle = g.muzzleFor(g.T, limb);
  const before = g.T.list.length, dBefore = g.TD.list.length, hpBefore = g.TD.hp;
  const area = g.loopArea();
  const cap = g.capacity(g.T.girth);
  const gain = g.loopAmp(area);
  const held = charge*S.chargeWood;
  g.cutNode(g.T, limb); g.layout(g.T); g.measure();
  // theirs wait in the air while this one is flown out to the end
  const theirs = g.bolts.filter(x => x.foe);
  g.bolts.length = 0;
  g.fireFromCut(charge, muzzle);
  const b = g.bolts[0];
  const rec = {
    lost: before - g.T.list.length,
    held: held, cap: cap, gain: gain, waste: Math.max(0, held - cap),
    fizzle: !b,
    force: b ? b.F : 0,
    front: b ? b.L : 0,
    speed: b ? Math.hypot(b.vx, b.vy) : 0,
    esc: Math.sqrt(2*S.gravMass/Math.hypot(S.coreSep-muzzle.x, muzzle.y)),
    path: [], near: 1e9, bearing: 0, hit: false, wood: 0, dmg: 0, laps: 0
  };
  if (b){
    for (let k = 0; k < 40000 && g.bolts.length; k++){
      g.stepBolts(1/120);
      if (!g.bolts.length) break;
      rec.path.push(+b.x.toFixed(1), +b.y.toFixed(1));
      const dx = b.x - S.coreSep, dy = b.y, d = Math.hypot(dx, dy);
      if (d < rec.near){ rec.near = d; rec.bearing = Math.atan2(dy, dx)*57.3; }
      if (Math.hypot(b.x, b.y) > S.coreSep*4) break;
    }
    // how far round it got before it spent itself, in laps of its own orbit
    rec.laps = b.run/(2*Math.PI*Math.max(S.coreR, rec.near));
    rec.wood = dBefore - g.TD.list.length;
    rec.dmg  = hpBefore - g.TD.hp;
    rec.hit  = rec.dmg > 0;
  }
  g.bolts.length = 0;
  for (const x of theirs) g.bolts.push(x);
  log.push(rec);
  return rec;
}

// ── the run ────────────────────────────────────────────────────────────
const frames = [];
function snap(tag){
  const o = { tag, maxR:g.T.maxR, top:g.FIG.topVal, hp:g.TD.hp/g.TD.hpMax,
              segs:[], buds:[], enemy:[], sep:S.coreSep, coreR:S.coreR, paths:[],
              loops:g.FIG.loops.map(l => l.pts), gain:g.FIG.gain };
  for (const n of g.T.list){
    o.segs.push([+n.x0.toFixed(1),+n.y0.toFixed(1),+n.x1.toFixed(1),+n.y1.toFixed(1),
                 +g.stiffOf(n).toFixed(2),+n.thick.toFixed(2),
                 +(g.FIG.topVal ? n.eff/g.FIG.topVal : 0).toFixed(3),
                 +(n.front||0).toFixed(1), +(n.peri||0).toFixed(0), +(n.reach||0).toFixed(2)]);
    if (n.bud) o.buds.push([+n.x1.toFixed(1),+n.y1.toFixed(1),+n.share.toFixed(3)]);
  }
  // their tree stands in its own frame; mirrored, so it reads from their pot
  for (const n of g.TD.list)
    o.enemy.push([-n.x0.toFixed(1),+n.y0.toFixed(1),-n.x1.toFixed(1),+n.y1.toFixed(1),+n.thick.toFixed(2)]);
  for (const r of log.slice(-6)) if (r.path.length) o.paths.push(r.path);
  frames.push(o);
}

let woven = 0;
if (SHAPES) gather(0, opt.wedge || 0.55, 200);
if (POLICY === "loop") woven += weave(opt.weave || 6);
g.measure();
if (FRAMES.includes(0)) snap("turn 0");

for (let turn = 1; turn <= TURNS; turn++){
  grow(GROW);
  g.measure();
  if (SHAPES && turn % 4 === 0) gather((rnd()-0.5)*0.9, 0.45, 60);
  if (POLICY === "loop" && turn % 3 === 0) woven += weave(2);
  if (POLICY === "random" && rnd() < 0.4){
    const pool = g.T.list.filter(n => g.bendLimit(n) > 0.002);
    if (pool.length){
      const grp = g.bendGroup(g.T, pool[Math.floor(rnd()*pool.length)]);
      for (const n of grp){ const lim = g.bendLimit(n);
        n.rel = n.rest + (rnd()*2-1)*lim; n.rest = n.rel; }
      g.layout(g.T);
    }
  }
  g.measure();
  let limb = pickCut();
  if (!limb) break;
  if (SHAPES){
    // the biggest shot that is not mostly waste, then aimed properly
    const cap = g.capacity(g.T.girth);
    let best = null, bv = -1;
    for (const n of cuttable()){
      const held = n.sub*S.chargeWood;
      const v = n.val * Math.min(1, cap/Math.max(1e-6, held));
      if (v > bv){ bv = v; best = n; }
    }
    limb = best || limb;
    aimAt(limb);
    g.measure();
  }
  fire(limb);
  g.measure();
  if (FRAMES.includes(turn)) snap("turn " + turn);
  if (g.TD.hp <= 0 || g.T.hp <= 0) break;
}

if (opt.dump) fs.writeFileSync(opt.dump, JSON.stringify(frames));

// ── what happened ──────────────────────────────────────────────────────
const shots = log.filter(r => !r.fizzle);
const hits  = log.filter(r => r.hit);
const kindOf = r => (r.front < 25 ? "spike" : r.front < 70 ? "blade" : "sheet") +
                    (r.speed > r.esc ? " · crosses" : " · captured");
console.log(`policy ${POLICY}  seed ${opt.seed || 7}  ${log.length} cuts, ` +
            `${log.length-shots.length} fizzles, ${woven} grafts woven`);
console.log("  cut  lost  charge/cap  gain   force  front  speed/esc   kind                arrives          wood  core");
for (let i = 0; i < log.length; i++){
  const r = log[i];
  if (r.fizzle){ console.log(String(i+1).padStart(5)+"  "+String(r.lost).padStart(4)+"   nothing to channel it"); continue; }
  const where = r.hit ? "CORE" :
    Math.abs(r.bearing) > 140 ? "near face" :
    Math.abs(r.bearing) > 70  ? "flank" : "behind";
  console.log(
    String(i+1).padStart(5)+"  "+String(r.lost).padStart(4)+
    "  "+(r.held.toFixed(0)+"/"+r.cap.toFixed(0)).padStart(9)+
    "  "+("×"+r.gain.toFixed(2)).padStart(5)+
    "  "+r.force.toFixed(1).padStart(6)+
    "  "+Math.round(r.front).toString().padStart(5)+
    "  "+(Math.round(r.speed)+"/"+Math.round(r.esc)).padStart(9)+
    "  "+kindOf(r).padEnd(20)+
    (where+" "+Math.round(r.near)+"u").padEnd(17)+
    String(r.wood).padStart(5)+"  "+(r.dmg?r.dmg.toFixed(1):"-").padStart(5));
}
const mean = a => a.length ? a.reduce((x,y)=>x+y,0)/a.length : 0;
console.log(`\n  ${shots.length} shots, ${hits.length} reached the core, enemy tree lost ` +
  `${log.reduce((a,r)=>a+r.wood,0)} nodes, its core is at ${Math.round(g.TD.hp/g.TD.hpMax*100)}%`);
if (MIND.lv.fires)
  console.log(`  they (${MIND.lv.name}) fired ${theirShots} shots; your core is at ` +
    `${Math.round(g.T.hp/g.T.hpMax*100)}%` + (g.T.hp <= 0 ? " — spent" : ""));
console.log(`  your tree: ${g.T.list.length} nodes, ${g.T.list.filter(n=>n.bud).length} tips, ` +
  `reach ${g.T.maxR.toFixed(0)}; you spent ${log.reduce((a,r)=>a+r.lost,0)} nodes firing`);
const kinds = {};
for (const r of shots) kinds[kindOf(r)] = (kinds[kindOf(r)]||0)+1;
console.log("  shot kinds: " + Object.entries(kinds).map(([k,v])=>k+" ×"+v).join(", "));
console.log(`  mean waste ${mean(log.map(r=>r.waste)).toFixed(0)} charge per cut, ` +
  `mean loop gain ×${mean(log.map(r=>r.gain)).toFixed(2)}, ` +
  `${mean(shots.map(r=>r.laps)).toFixed(1)} laps flown before a shot is spent`);
