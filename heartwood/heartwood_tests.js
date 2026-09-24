// Heartwood — regression suite. Pulls the model straight out of the HTML
// between /*BEGIN SIM*/ and /*END SIM*/, so the tests cannot drift from the game.
//   node heartwood_tests.js [index.html]
const fs = require("fs");
const FILE = process.argv[2] || __dirname + "/index.html";
const html = fs.readFileSync(FILE, "utf8");
const sim = new Function(html.split("/*BEGIN SIM*/")[1].split("/*END SIM*/")[0] + `
  return {S, newTree, step, layout, cutNode, makeGraft, bendGroup, bendLimit, stiffOf,
          bestFan, bestSpire, loopPoly, figureNodes, greenOf, capacity, forkLen,
          makeBolt, stepBolt, buildGrid, gridNear, pressure, muzzleFor,
          valueCuts, loopAmp, markLoops, periapsis, frameView, circuitArea,
          genome, resist, coreOf, targetOf, shotForce, frontWide, bindGrafts, graftSides,
          biteBolt, muzzleSpeed, reachChain, chainTip, volleyFrom, shotFrom};`)();
const S = sim.S, D2R = Math.PI/180;
const BASE = JSON.parse(JSON.stringify(S));
function reset(){ for (const k in BASE) S[k] = BASE[k]; }

let failures = 0;
function check(label, ok, detail){
  if (!ok) failures++;
  console.log("  " + (ok ? "ok  " : "FAIL") + "  " + label + (detail ? "   " + detail : ""));
}
function suite(name){ console.log("\n" + name); }
// Trees are planted from a genome. GENES, when set, overrides the default
// seedling's for every tree grown until it is cleared.
let GENES = null;
const seed = over => Object.assign(sim.genome(), over || {});
function grow(secs, dt){
  dt = dt || 0.05;
  const T = sim.newTree(0, seed(GENES));
  for (let t = 0; t < secs; t += dt) sim.step(T, dt);
  sim.layout(T); return T;
}
const tips = T => T.list.filter(n => n.bud).length;
// the main axis, pot to tip: at every fork, the child of the lowest order
function leader(T){
  const out = [];
  let q = T.nodes.get(T.roots[0]);
  while (q){
    out.push(q);
    let next = null;
    for (const id of q.children){ const c = T.nodes.get(id); if (c && (!next || c.order < next.order)) next = c; }
    q = next;
  }
  return out;
}
// the first internode of the main axis past a fraction of the reach
const leaderPast = (T, f) => leader(T).find(n => Math.hypot(n.x1, n.y1) > f*T.maxR);
const wrap = a => { while (a > Math.PI) a -= 2*Math.PI; while (a < -Math.PI) a += 2*Math.PI; return a; };
function cross(ax,ay,bx,by,cx,cy,dx,dy){
  const o=(px,py,qx,qy,rx,ry)=>(qy-py)*(rx-qx)-(qx-px)*(ry-qy);
  return ((o(ax,ay,bx,by,cx,cy)>0)!==(o(ax,ay,bx,by,dx,dy)>0)) &&
         ((o(cx,cy,dx,dy,ax,ay)>0)!==(o(cx,cy,dx,dy,bx,by)>0));
}

// ── growth ─────────────────────────────────────────────────────────────
suite("Growth");
{
  const T = grow(480);
  const r = T.list.filter(n => n.bud).map(n => Math.hypot(n.x1, n.y1)).sort((a,b)=>a-b);
  const p10 = r[Math.floor(r.length*0.1)], p90 = r[Math.floor(r.length*0.9)];
  // a lateral is born mid-step and waits one tick for its share; everything
  // that has been through a redistribution should be moving
  check("no tip is starved",
        T.list.every(n => !n.bud || n.share > 0 || n.age < 0.2),
        tips(T) + " tips, all growing");
  check("it grows from a single trunk", T.roots.length === 1);
  let fork = T.nodes.get(T.roots[0]);
  while (fork && fork.children.length === 1) fork = T.nodes.get(fork.children[0]);
  check("the first fork sits low on the trunk",
        fork && Math.hypot(fork.x1, fork.y1) < 0.28*T.maxR,
        fork ? (Math.hypot(fork.x1,fork.y1)/T.maxR*100).toFixed(0) + "% of the way out" : "");
  check("it forks many generations deep", Math.max(...T.list.map(n => n.gen)) >= 8,
        Math.max(...T.list.map(n => n.gen)) + " generations");
  // The pipe model: girth follows flow, so at every fork the branch that peeled
  // off is thinner than the axis that carried on, and nothing is thicker than
  // the trunk everything passes through.
  const trunk = T.nodes.get(T.roots[0]).thick;
  let ratio = 0, forks = 0;
  for (const n of T.list){
    if (n.children.length !== 2) continue;
    const [a, b] = n.children.map(id => T.nodes.get(id));
    if (!a || !b) continue;
    const main = a.order <= b.order ? a : b, lat = main === a ? b : a;
    if (main.thick < 3) continue;          // the twig forks at the rim are all girth 1
    ratio += lat.thick/main.thick; forks++;
  }
  check("thickness tapers like a pipe",
        trunk/T.maxR > 0.05 && ratio/forks < 0.8 && T.list.every(n => n.thick <= trunk + 1e-9),
        "trunk " + (trunk/T.maxR*100).toFixed(1) + "% of reach; a branch leaves its axis at " +
        (ratio/forks).toFixed(2) + "\u00d7 the axis's girth");
  check("tips converge on a rim", p10/p90 > 0.6, "p10 " + p10.toFixed(0) + " vs p90 " + p90.toFixed(0));
  let chir = 0, nb = 0;
  for (const n of T.list) if (n.bud){
    const a = Math.atan2(n.y1, n.x1);
    let best = 9; for (const b of [0, 2.0944, -2.0944]){ const d = wrap(a-b); if (Math.abs(d) < Math.abs(best)) best = d; }
    chir += best; nb++;
  }
  check("no pinwheel bias", Math.abs(chir/nb*57.3) < 5, (chir/nb*57.3).toFixed(1) + "\u00b0 mean offset");
}
{
  // Wood fattens and never lengthens. A junction stays where it was born, so
  // a tree kept cut back stays exactly as small as it is kept.
  const at = T => { let f = T.nodes.get(T.roots[0]);
                    while (f && f.children.length === 1) f = T.nodes.get(f.children[0]);
                    return f ? Math.hypot(f.x1, f.y1) : 0; };
  const early = at(grow(90)), late = at(grow(500));
  const T5 = grow(500);
  check("the first junction stays where it was born", Math.abs(late - early) < 1e-6,
        early.toFixed(1) + "u at 90s, " + late.toFixed(1) + "u at 500s, while the trunk went to " +
        T5.nodes.get(T5.roots[0]).thick.toFixed(0) + " thick");
}

// ── apical control ─────────────────────────────────────────────────────
suite("Apical control");
{
  reset();
  // the budget is handed down the tree, fork by fork; at one half that is
  // exactly a flat split and the tree is a broom
  GENES = { apical: 0.5 };
  const B = grow(240);
  const bs = B.list.filter(n => n.bud).map(n => n.share);
  check("at one half every tip grows alike", Math.max(...bs) - Math.min(...bs) < 1e-9,
        bs.length + " tips, each drawing " + bs[0].toFixed(4) + " u/s");
  reset(); GENES = null;

  // above it the axis that carried on outgrows the branch that left it, at
  // every fork, and the tree grows a leader
  const U = grow(240);
  const us = U.list.filter(n => n.bud).sort((a,b) => b.share - a.share);
  const mean = U.g.vigor/us.length;
  const lead = leader(U).pop();
  check("above it the tree grows a leader",
        lead && lead.bud && lead.share >= us[0].share - 1e-9 && U.maxR > B.maxR*1.3,
        "the tip at the end of the main axis draws " + (lead.share/mean).toFixed(1) +
        "\u00d7 the average; reach " + B.maxR.toFixed(0) + "u as a broom, " + U.maxR.toFixed(0) + "u with a leader");
  check("and no tip draws past the ceiling",
        us[0].share <= S.leadCap*mean*(1 + 1e-6),
        "the strongest tip at " + (us[0].share/mean).toFixed(2) + "\u00d7 the average, against a ceiling of " + S.leadCap);

  // dominance compounds with every fork the leader grows through; the ceiling
  // is what turns that into a plateau, so a tree with a leader can be kept
  GENES = { apical: 0.7 };
  const a4 = grow(240).maxR, a10 = grow(600).maxR;
  const held = S.leadCap; S.leadCap = 0;
  const r4 = grow(240).maxR, r10 = grow(600).maxR;
  S.leadCap = held;
  check("with the ceiling a strong leader still plateaus",
        a10 < a4*1.2 && r10 > a10*1.4,
        "\u03bb 0.7: " + a4.toFixed(0) + "u \u2192 " + a10.toFixed(0) + "u from four minutes to ten; " +
        "without the ceiling " + r4.toFixed(0) + "u \u2192 " + r10.toFixed(0) + "u");
  reset(); GENES = null;

  // cut the leader and its share flows to whatever continues the line below
  const V = grow(200);
  const cutAt = leaderPast(V, 0.4);
  const heir0 = new Map(V.list.filter(n => n.bud).map(n => [n.id, n.share]));
  sim.cutNode(V, cutAt); sim.layout(V);
  sim.step(V, 0.05); sim.layout(V);
  const heir = V.list.filter(n => n.bud).sort((a,b) => b.share - a.share)[0];
  check("cut the leader and the next branch down becomes it",
        heir && heir0.has(heir.id) && heir.share > heir0.get(heir.id)*1.5,
        "a tip that drew " + (heir0.get(heir.id)||0).toFixed(3) + " u/s now draws " +
        heir.share.toFixed(3));

  // a floor turns suppression into dormancy, and dormancy is released by the
  // cut, because the question is asked again every step
  GENES = { apical: 0.7 };
  const W0 = grow(300);
  check("the dormancy floor is inert on its own",
        W0.list.every(n => !n.bud || n.share > 0), "every tip still growing at floor 0");
  S.dormantMin = 0.01;
  const W = grow(300);
  const asleep = W.list.filter(n => n.bud && n.share === 0);
  check("with a floor, the most suppressed tips stop",
        asleep.length > 0 && asleep.length < tips(W),
        asleep.length + " of " + tips(W) + " tips dormant under the leader");
  const wcut = leaderPast(W, 0.3);
  const ids = new Set(asleep.map(n => n.id));
  sim.cutNode(W, wcut); sim.layout(W); sim.step(W, 0.05); sim.layout(W);
  const woke = W.list.filter(n => ids.has(n.id) && n.share > 0).length;
  check("and cutting the leader wakes them", woke > 0,
        woke + " of the dormant tips growing again the moment the leader was cut");
  reset(); GENES = null;
}

// ── the seedling ───────────────────────────────────────────────────────
suite("The seedling");
{
  reset();
  const plant = (picks, secs) => {
    const T = sim.newTree(0, sim.genome(picks));
    for (let t = 0; t < secs; t += 0.05) sim.step(T, 0.05);
    sim.layout(T); return T;
  };
  const d = sim.genome();
  check("an unchosen seedling is the middle of every axis",
        d.picks.habit === "upright" && d.picks.grain === "even" && d.picks.wood === "seasoned",
        "upright, even, seasoned");

  const br = plant({habit:"broom"}, 240), up = plant({habit:"upright"}, 240), sp = plant({habit:"spear"}, 240);
  check("habit runs from a low round broom to a tall spear",
        br.maxR < up.maxR && up.maxR < sp.maxR,
        "reach " + br.maxR.toFixed(0) + "u, " + up.maxR.toFixed(0) + "u, " + sp.maxR.toFixed(0) + "u");

  const fi = plant({grain:"fine"}, 240), op = plant({grain:"open"}, 240);
  check("fine grain is dense and short, open grain sparse and long",
        tips(fi) > tips(op) && fi.maxR < op.maxR,
        tips(fi) + " tips in " + fi.maxR.toFixed(0) + "u against " + tips(op) + " in " + op.maxR.toFixed(0) + "u");

  const wood = T => T.list.reduce((a, n) => a + n.len, 0);
  const li = plant({wood:"light"}, 120), se = plant({wood:"seasoned"}, 120), de = plant({wood:"dense"}, 120);
  check("light wood grows fastest and dense wood slowest",
        wood(li) > wood(se) && wood(se) > wood(de),
        Math.round(wood(li)) + ", " + Math.round(wood(se)) + ", " + Math.round(wood(de)) + " units of wood at two minutes");
  const tr = T => T.nodes.get(T.roots[0]);
  check("and what grows slowest is hardest to cut and to kill",
        sim.resist(tr(de))/tr(de).thick > sim.resist(tr(li))/tr(li).thick &&
        sim.coreOf(de.g) > sim.coreOf(se.g) && sim.coreOf(se.g) > sim.coreOf(li.g),
        "cores of " + sim.coreOf(li.g) + ", " + sim.coreOf(se.g) + " and " + sim.coreOf(de.g).toFixed(1));

  // the genome is the tree's own: two on one field do not share rules
  const A = sim.newTree(0, sim.genome({habit:"broom"})), B = sim.newTree(180, sim.genome({habit:"spear"}));
  for (let t = 0; t < 200; t += 0.05){ sim.step(A, 0.05); sim.step(B, 0.05); }
  sim.layout(A); sim.layout(B);
  const spread = T => { const s = T.list.filter(n => n.bud).map(n => n.share); return Math.max(...s)/Math.min(...s); };
  check("two seedlings on one field keep their own rules",
        spread(A) < 1 + 1e-9 && spread(B) > 2 && A.list.every(n => n.g === A.g) && B.list.every(n => n.g === B.g),
        "the broom's tips all draw alike; the spear's strongest draws " + spread(B).toFixed(0) + "\u00d7 its weakest");
}

// ── cutting, healing, ramification ─────────────────────────────────────
suite("Cutting and recovery");
{
  const T = grow(200);
  const before = tips(T);
  const limb = T.list.find(n => n.parent !== null && Math.hypot(n.x1,n.y1) > 0.4*T.maxR);
  sim.cutNode(T, limb); sim.layout(T);
  const after = tips(T);
  sim.cutNode(T, T.nodes.get(T.roots[0])); sim.layout(T);
  check("a cut redistributes vigour", after < before, before + " tips -> " + after);
  check("felling the trunk ends the tree", T.roots.length === 0 && T.list.length === 0,
        "nothing left in the pot");

  const U = grow(200);
  const vic = U.list.filter(n => {
    const p = n.parent === null ? null : U.nodes.get(n.parent);
    const rp = p ? Math.hypot(p.x1, p.y1) : S.coreR;
    return Math.hypot(n.x1, n.y1) > 50 && rp <= 50;
  });
  for (const v of vic) if (U.nodes.has(v.id)) sim.cutNode(U, v);
  sim.layout(U);
  check("a stub starts healing", U.list.some(n => n.healGoal > 0));
  check("a chop ramifies the spot", U.list.some(n => n.ram > 0));
  for (let t = 0; t < 60; t += 0.05) sim.step(U, 0.05);
  sim.layout(U);
  check("shoots break out and branch", tips(U) > 8, tips(U) + " tips 60s after the chop");
}
{
  // eleven chops: reach should fall and the trunk should win on ratio
  // Chop back to the same structure every time, the way a keeper does, rather
  // than to a fixed radius: with age the tree grows out faster and a fixed
  // radius stops landing on the same stubs at all.
  function regime(ramify){
    reset(); S.chopRamify = ramify;
    const T = sim.newTree(0);
    for (let t = 0; t < 120; t += 0.05) sim.step(T, 0.05);
    sim.layout(T);
    const stubs = T.list.filter(n => {
      const p = n.parent === null ? null : T.nodes.get(n.parent);
      return p && Math.hypot(n.x1,n.y1) > 45 && Math.hypot(p.x1,p.y1) <= 45;
    }).map(n => n.parent);
    let next = 120 + 55;
    for (let t = 120; t < 660; t += 0.05){
      sim.step(T, 0.05);
      if (t < next) continue;
      sim.layout(T); next += 55;
      for (const id of stubs){
        const st = T.nodes.get(id);
        if (!st) continue;
        for (const kid of st.children.slice()){
          const k = T.nodes.get(kid);
          if (k) sim.cutNode(T, k);
        }
      }
      sim.layout(T);
    }
    sim.layout(T);
    const trunk = T.nodes.get(T.roots[0]).thick;
    return { reach: T.maxR, ratio: trunk/T.maxR, tips: tips(T) };
  }
  const off = regime(0), on = regime(1);
  reset();
  check("ramification makes it squat", on.reach < off.reach*0.85,
        off.reach.toFixed(0) + "u -> " + on.reach.toFixed(0) + "u");
  check("ramification makes it denser", on.tips > off.tips,
        off.tips + " tips -> " + on.tips);
  {
    // the claim at its own scale: cut the same spot again and again, and the
    // wood that grows back forks sooner every time
    reset();
    const T = grow(200);
    const spot = T.list.find(n => n.parent !== null && n.children.length &&
                                  Math.hypot(n.x1,n.y1) > 0.4*T.maxR);
    const stub = T.nodes.get(spot.parent);
    const first = sim.forkLen(stub);
    for (let round = 0; round < 5; round++){
      const kid = stub.children.map(id => T.nodes.get(id)).filter(Boolean)[0];
      if (kid) sim.cutNode(T, kid);
      sim.layout(T);
      for (let t = 0; t < 40; t += 0.05) sim.step(T, 0.05);
      sim.layout(T);
    }
    check("chopping the same spot shortens what grows back",
          sim.forkLen(stub) < first*0.7 && stub.ram >= 3,
          "fork interval " + first.toFixed(1) + "u -> " + sim.forkLen(stub).toFixed(1) +
          "u after five chops, " + stub.ram + " levels of ramification");
  }
  check("the trunk wins on ratio", on.ratio > off.ratio*1.3,
        (off.ratio*100).toFixed(1) + "% -> " + (on.ratio*100).toFixed(1) + "%");
}

// ── bending ────────────────────────────────────────────────────────────
suite("Bending");
{
  const T = grow(150);
  let g0 = null, bd = 1e9;
  for (const n of T.list){ const d = Math.abs(Math.hypot(n.x1,n.y1) - 0.7*T.maxR); if (d < bd){ bd = d; g0 = n; } }
  const grp = sim.bendGroup(T, g0);
  const pliant = grp.filter(n => sim.bendLimit(n) > 0.005);
  const give = grp.reduce((a,n) => a + sim.bendLimit(n), 0)*57.3;
  check("the chain reaches the pot", grp[grp.length-1].parent === null, grp.length + " joints");
  const root = T.nodes.get(T.roots[0]);
  check("the trunk is the stiffest wood there is",
        grp.every(n => sim.bendLimit(n) >= sim.bendLimit(root) - 1e-9),
        "the trunk gives \u00b1" + (sim.bendLimit(root)*57.3).toFixed(1) +
        "\u00b0 a joint, the outermost \u00b1" + (sim.bendLimit(grp[0])*57.3).toFixed(1));
  const old = grow(700);
  check("an old trunk is locked", sim.bendLimit(old.nodes.get(old.roots[0])) < 1e-9,
        "nothing left to do to it at 700s");
  check("there is room to aim", give > 25, "\u00b1" + (give/2).toFixed(0) + "\u00b0 at this limb");

  // pull to a fraction of what the wood can actually take; asking for more
  // than it has is a test of the wood's range, not of the solver
  const times = [];
  for (const frac of [0.05, 0.15, 0.3, 0.45]){
    const deg = Math.round(give*frac);
    const keep = grp.map(n => n.rel);
    const r0 = Math.hypot(g0.x1-g0.x0, g0.y1-g0.y0);
    const a0 = Math.atan2(g0.y1-g0.y0, g0.x1-g0.x0) + deg*D2R;
    const px = g0.x0 + Math.cos(a0)*r0, py = g0.y0 + Math.sin(a0)*r0;
    let tx = g0.x1, ty = g0.y1, worst = 0, last = 9, arrived = -1;
    const fdt = 1/60;
    for (let f = 0; f < 900; f++){
      // exactly what the hand does: the grip leads, the wood follows at its pace
      const hx = px-tx, hy = py-ty, hd = Math.hypot(hx,hy), hs = S.handSpeed*fdt;
      if (hd > hs){ tx += hx/hd*hs; ty += hy/hd*hs; } else { tx = px; ty = py; }
      sim.reachChain(grp, tx, ty, S.bendRate*D2R*fdt);
      sim.layout(T);
      const res = wrap(Math.atan2(py-g0.y0, px-g0.x0) - Math.atan2(g0.y1-g0.y0, g0.x1-g0.x0))*57.3;
      worst = Math.max(worst, -res); last = res;
      if (arrived < 0 && Math.abs(res) < Math.max(0.5, deg*0.08)) arrived = f/60;
      if (arrived >= 0 && f > arrived*60 + 90) break;
    }
    check("a " + deg + "\u00b0 pull settles without overshoot",
          worst < 0.5 && Math.abs(last) < Math.max(1.5, deg*0.16),
          "overshoot " + Math.max(0,worst).toFixed(2) + "\u00b0, residual " + last.toFixed(2) +
          "\u00b0, arrived after " + arrived.toFixed(2) + "s");
    times.push([deg, arrived]);
    grp.forEach((n,i) => n.rel = keep[i]); sim.layout(T);
  }
  // Wood travels; it does not teleport. A pull should take about as long as
  // the hand needs to turn the joints that are giving, which is what makes a
  // bend cost the thing it is meant to cost: the time your hand is on it.
  const big = times[times.length-1];
  check("a bend takes time", big[1] > 1.5 && times.every(t => t[1] > 0.2),
        times.map(t => t[0] + "\u00b0 in " + t[1].toFixed(2) + "s").join(", ") +
        ", at " + S.bendRate + "\u00b0/s of wood and " + S.handSpeed + " u/s of hand");
}

// ── grafting ───────────────────────────────────────────────────────────
suite("Grafting");
{
  const T = grow(120);
  let A = null, B = null, bd = 1e9;
  const buds = T.list.filter(n => n.bud);
  for (let i = 0; i < buds.length; i++) for (let j = i+1; j < buds.length; j++){
    if (buds[i].parent === buds[j].parent) continue;
    const d = Math.hypot(buds[i].x1-buds[j].x1, buds[i].y1-buds[j].y1);
    if (d < bd){ bd = d; A = buds[i]; B = buds[j]; }
  }
  const mB = B.mass;
  sim.makeGraft(T, A, B); sim.layout(T);
  check("two tips become one node", !A.bud && !B.bud && A.children.length === 1);
  for (let t = 0; t < 60; t += 0.05) sim.step(T, 0.05);
  sim.layout(T);
  check("the junction stays shut", Math.hypot(A.x1-B.x1, A.y1-B.y1) < 0.01);
  check("sap feeds the far limb", B.mass > mB*1.5,
        "mass " + mB.toFixed(1) + " -> " + B.mass.toFixed(1) + " on a limb with no growing point");
  const lp = sim.loopPoly(T, B);
  check("the loop encloses area", lp && lp.area > 0, lp ? Math.round(lp.area/(S.coreR*S.coreR)) + " core-areas" : "");
  // a hand on one grafted limb, pulling for a second; the other limb is bound to it
  const grp = sim.bendGroup(T, A), hand = new Set(grp.map(n => n.id));
  const sd = sim.graftSides(T, B), was = sd.sb.map(n => n.rel);
  // the hand takes the master's stem and walks it aside at the wood's own pace
  const aim = [A.x1, A.y1 - 60];
  const pull = () => { sim.reachChain(grp, aim[0], aim[1], S.bendRate*D2R/60); sim.layout(T); };
  const jx = A.x1, jy = A.y1;
  for (let f = 0; f < 240; f++){ pull(); sim.bindGrafts(T, hand, 1/60, null); }
  sim.layout(T);
  const swung = Math.max(...sd.sb.map((n, i) => Math.abs(n.rel - was[i])))*57.3;
  check("pull one grafted limb and the other comes with it",
        swung > 2 && Math.hypot(A.x1 - jx, A.y1 - jy) > 2,
        "the junction moved " + Math.hypot(A.x1 - jx, A.y1 - jy).toFixed(1) + "u and the partner's joints swung up to " + swung.toFixed(1) + "\u00b0");
  check("so the graft holds", B.gstrain <= S.graftStrain,
        "strain " + B.gstrain.toFixed(2) + " against a tolerance of " + S.graftStrain);
  // a partner that cannot follow: the hand keeps pulling and the graft tears
  for (const n of sd.sb) n.cracked = true;
  for (let r = 0; r < 20 && B.gstrain <= S.graftStrain; r++){
    for (const n of grp) n.rest = n.rel;               // let go, take hold again
    aim[1] -= 20;
    for (let f = 0; f < 120; f++){ pull(); sim.bindGrafts(T, hand, 1/60, null); }
    sim.layout(T);
  }
  const strained = B.gstrain;
  sim.step(T, 0.05); sim.layout(T);
  check("but a partner that cannot follow tears it", strained > S.graftStrain && B.mate === null &&
        !B.slave && T.grafts.length === 0, "strain reached " + strained.toFixed(2) + "; released");
}

// ── figures ────────────────────────────────────────────────────────────
suite("Figures");
{
  const T = grow(220);
  // Every tip counts toward a fan, live or stopped, so there is no arming
  // step and no completion event: the question is never whether you have a
  // figure but how much better than the plant's own habit yours is.
  const armed = sim.bestFan(T);
  check("a growing tree is already armed",
        sim.figureNodes(T).length > S.fanMin && armed && armed.P > 0,
        sim.figureNodes(T).length + " tips, best wedge " + Math.round(armed.P) + " power");
  check("but it has earned nothing by growing", Math.abs(armed.conv - 1) < 0.02,
        "converged " + armed.conv.toFixed(2) + "\u00d7 \u2014 all reach, no gathering");
  // Nothing on a tree grows straight for long: every fork turns the axis
  // further than the straightness tolerance. A barrel is something you build.
  sim.bestSpire(T);
  const runs = T.list.map(n => n.runLen).sort((a,b) => b-a);
  check("no tree comes with a barrel", runs[0] < 0.25*T.maxR,
        "longest natural run " + runs[0].toFixed(0) + "u, " +
        (runs[0]/T.maxR*100).toFixed(0) + "% of reach");

  const U = grow(220);
  for (const n of U.list) if (n.bud) n.bud = false;
  sim.layout(U);
  const lazy = sim.bestFan(U);
  check("crowding you did not make is worth nothing", Math.abs(lazy.conv - 1) < 0.02,
        "converged " + lazy.conv.toFixed(2) + "\u00d7, power " + Math.round(lazy.P));

  const V = grow(220);
  const picked = [];
  const vb = V.list.filter(n => n.bud).sort((a,b) => Math.atan2(a.y1,a.x1) - Math.atan2(b.y1,b.x1));
  for (let i = 0; i < vb.length; i += Math.floor(vb.length/9)) picked.push(vb[i]);
  for (const n of picked) n.bud = false;
  sim.layout(V);
  const before = sim.bestFan(V).P;
  const mid = Math.atan2(picked[4].y1, picked[4].x1);
  for (let pass = 0; pass < 260; pass++) for (const q of picked){
    const g = sim.bendGroup(V, q);
    let d = Math.atan2(q.y1, q.x1) - mid;
    while (d > Math.PI) d -= 2*Math.PI; while (d < -Math.PI) d += 2*Math.PI;
    if (Math.abs(d) < 0.02) continue;
    for (const n of g){
      const lim = sim.bendLimit(n); if (lim < 0.0005) continue;
      let off = n.rel - 0.03*Math.sign(d) - n.rest;
      while (off > Math.PI) off -= 2*Math.PI; while (off < -Math.PI) off += 2*Math.PI;
      n.rel = n.rest + Math.max(-lim, Math.min(lim, off));
    }
    sim.layout(V);
  }
  const after = sim.bestFan(V);
  check("gathering by hand is worth a great deal", after.P > before*1.8 && after.conv > 2,
        Math.round(before) + " -> " + Math.round(after.P) + " power, converged " + after.conv.toFixed(2) + "\u00d7");
}

// ── ballistics ─────────────────────────────────────────────────────────
suite("Ballistics");
{
  const esc = Math.sqrt(2*S.gravMass/S.coreSep);
  {
    // A shot that crosses rather than being captured needs a straight run
    // behind it that the plant will not give you. What the hand can give is
    // any chain of joints that still bends at all: a pull is limited, but it
    // can be repeated, so pliant wood can be walked all the way into line.
    const G = grow(400); sim.bestSpire(G);
    const natural = Math.max(...G.list.map(n => n.runLen));
    let built = 0;
    for (const n of G.list){
      let L = 0, q = n;
      while (q && q.parent !== null && sim.bendLimit(q) > 0.0005){
        L += q.len; q = G.nodes.get(q.parent);
      }
      if (q) L += q.len;
      if (L > built) built = L;
    }
    const vNat = S.speedBase + S.speedSpire*natural, vBuilt = S.speedBase + S.speedSpire*built;
    check("crossing takes a barrel you have straightened yourself",
          esc > S.speedBase*1.3 && vNat < esc && vBuilt > esc,
          esc.toFixed(0) + " u/s to cross; the plant's best run of " + natural.toFixed(0) +
          "u gives " + vNat.toFixed(0) + ", a limb pulled straight gives " + vBuilt.toFixed(0) +
          " down " + built.toFixed(0) + "u");
  }
  function flight(th, v){
    const b = { x: Math.cos(th)*S.coreR, y: Math.sin(th)*S.coreR,
                vx: Math.cos(th)*v, vy: Math.sin(th)*v, F: 6, F0: 6, run: 0, trail: [] };
    // the first pass only: a bound shot comes round several times before it
    // is spent, and a later lap would report a different closest approach
    let near = 1e9, bearing = 0, last = 1e9, rising = 0;
    for (let k = 0; k < 200000; k++){
      sim.stepBolt(b, 1/240);
      const dx = b.x - S.coreSep, dy = b.y, d = Math.hypot(dx, dy);
      if (d < near){ near = d; bearing = Math.atan2(dy, dx)*57.3; }
      rising = d > last ? rising + 1 : 0;
      last = d;
      if (d < S.coreR || rising > 2000 || Math.hypot(b.x, b.y) > S.coreSep*4) break;
    }
    return { near, bearing };
  }
  {
    // the shot leaves the cut face, pointing where that stem points
    const T = grow(220);
    sim.bestSpire(T);
    // a limb whose stem still has some give in it: the leader sets early
    const limb = T.list.find(n => n.parent !== null && Math.hypot(n.x1,n.y1) > 60 &&
      sim.bendGroup(T, T.nodes.get(n.parent)).reduce((a,m) => a + sim.bendLimit(m), 0) > 0.3);
    const p = T.nodes.get(limb.parent);
    const m = sim.muzzleFor(T, limb);
    check("the muzzle is the cut face", Math.hypot(m.x-p.x1, m.y-p.y1) < 1e-9,
          "at " + m.x.toFixed(0) + "," + m.y.toFixed(0) + ", not the core");
    const fan = sim.bestFan(T) || { from:0, span:0.3, rbar:120, P:100, conv:1 };
    const b = sim.makeBolt(fan, 6, m);
    const launch = Math.atan2(b.vy, b.vx);
    check("it launches along the stem, not the fan", Math.abs(wrap(launch - p.abs)) < 1e-9,
          "stem points " + (p.abs*57.3).toFixed(0) + "\u00b0, bolt leaves at " + (launch*57.3).toFixed(0) + "\u00b0");
    // bending that stem moves the shot
    const before = launch;
    const g = sim.bendGroup(T, p);
    for (const n of g){ const lim = sim.bendLimit(n); n.rel = n.rest + lim; n.rest = n.rel; }
    sim.layout(T); sim.bestSpire(T);
    const m2 = sim.muzzleFor(T, limb);
    const b2 = sim.makeBolt(fan, 6, m2);
    const moved = Math.abs(wrap(Math.atan2(b2.vy, b2.vx) - before))*57.3;
    check("bending the stem re-aims it", moved > 3,
          "the launch bearing swung " + moved.toFixed(1) + "\u00b0");
    check("a straighter barrel is a faster shot",
          S.speedBase + S.speedSpire*(m.run/S.coreR) > S.speedBase,
          (m.run/S.coreR).toFixed(1) + "\u00d7 of straight run behind that cut");
  }

  const escPot = Math.sqrt(2*S.gravMass/S.coreSep);
  const slow = flight(60*D2R, escPot*0.55), fast = flight(60*D2R, escPot*2.6);
  check("a slow shot is captured and comes round the back", Math.abs(slow.bearing) < 60,
        "arrives at " + slow.bearing.toFixed(0) + "\u00b0, passing " + slow.near.toFixed(0) + "u out");
  check("a fast shot is only deflected", fast.near > slow.near*1.8,
        "closest pass " + fast.near.toFixed(0) + "u against the slow shot's " +
        slow.near.toFixed(0) + "u");
  check("straight on always connects", flight(0, escPot*2).near < S.coreR);
  {
    // the closed form the readout leans on, against the integrator that flies it
    const T = grow(300); sim.bestSpire(T);
    let worst = 0, n = 0;
    for (const limb of T.list){
      if (limb.parent === null || !limb.children.length) continue;
      if (n++ % 97) continue;
      const m = sim.muzzleFor(T, limb);
      const pred = sim.periapsis(m);
      if (pred > S.coreSep*0.4) continue;          // far passes do not matter
      const b = sim.makeBolt({from:0,span:0.2,rbar:100,P:1,conv:1}, 1e9, m);
      let near = 1e9;
      for (let k = 0; k < 90000; k++){          // a full orbit's worth of flight
        sim.stepBolt(b, 1/240);
        const d = Math.hypot(b.x - S.coreSep, b.y);
        if (d < near) near = d;
        if (Math.hypot(b.x, b.y) > S.coreSep*6) break;
      }
      worst = Math.max(worst, Math.abs(pred - near));
    }
    check("the predicted closest approach matches the flown one", worst < 14,
          "worst disagreement " + worst.toFixed(1) + "u, on a field " + S.coreSep + "u across");
  }
  {
    // the pull is the target tree's weight, which sits out in its crown
    const E = grow(240), tg = sim.targetOf(E);
    check("a shot falls toward their wood's centre of mass, not their core",
          S.coreSep - tg.fx > 40 && S.coreSep - tg.fx < E.maxR,
          "the pull sits " + (S.coreSep - tg.fx).toFixed(0) + "u out from their core, in a crown " + E.maxR.toFixed(0) + "u deep");
    // and the coarse flight the glow reads agrees with the fine one, over the
    // first lap round their centre of mass — the lap that carries full force
    const T = grow(300); sim.bestSpire(T);
    let worst = 0, n = 0, tried = 0;
    for (const limb of T.list){
      if (limb.parent === null || !limb.children.length) continue;
      if (n++ % 61) continue;
      const m = sim.muzzleFor(T, limb);
      const pred = sim.periapsis(m, tg);
      if (pred > S.coreSep*0.4) continue;
      tried++;
      const b = sim.makeBolt(null, 1e9, m, tg);
      let near = 1e9, swept = 0, pa = Math.atan2(b.y - tg.fy, b.x - tg.fx);
      for (let k = 0; k < 90000; k++){
        sim.stepBolt(b, 1/240);
        const d = Math.hypot(b.x - S.coreSep, b.y);
        if (d < near) near = d;
        const a = Math.atan2(b.y - tg.fy, b.x - tg.fx);
        swept += wrap(a - pa); pa = a;
        if (Math.abs(swept) >= 2*Math.PI || Math.hypot(b.x, b.y) > S.coreSep*3) break;
      }
      worst = Math.max(worst, Math.abs(pred - near));
    }
    check("the pass the glow reads is the pass the shot flies", tried > 3 && worst < 6,
          "worst disagreement " + worst.toFixed(1) + "u over " + tried + " limbs, the pull " +
          (S.coreSep - tg.fx).toFixed(0) + "u in front of the core");
    // mass times speed
    check("a shot's force is its mass times its speed",
          Math.abs(sim.shotForce(10, 40) - 2*sim.shotForce(5, 40)) < 1e-9 &&
          Math.abs(sim.shotForce(10, 40)/sim.shotForce(10, 0) - sim.muzzleSpeed(40)/sim.muzzleSpeed(0)) < 1e-9,
          "10 charge off a 40u barrel carries " + sim.shotForce(10, 40).toFixed(1) +
          ", off a kink " + sim.shotForce(10, 0).toFixed(1));
    const bb = sim.makeBolt(null, 12, { x: 0, y: 0, dir: 0, run: 20, id: -1 });
    const v0 = Math.hypot(bb.vx, bb.vy);
    sim.biteBolt(bb, 4);
    check("a shot that bites through wood comes out slower", bb.F === 8 &&
          Math.abs(Math.hypot(bb.vx, bb.vy) - v0*8/12) < 1e-9,
          "12 force through wood that resists 4: " + v0.toFixed(0) + " u/s in, " +
          Math.hypot(bb.vx, bb.vy).toFixed(0) + " out");
  }
}
{
  // width is a shape of shot, not an amount of one
  const D = sim.newTree(180);
  for (let t = 0; t < 400; t += 0.15) sim.step(D, 0.15, null);
  sim.layout(D); sim.buildGrid(D);
  const snapshot = JSON.stringify(D.list.map(n => [n.id, n.parent]));
  function volley(spanDeg, force){
    const E = sim.newTree(180);
    for (let t = 0; t < 400; t += 0.15) sim.step(E, 0.15, null);
    sim.layout(E); sim.buildGrid(E);
    const gm = S.gravMass, sb = S.speedBase, ss = S.speedSpire;
    S.gravMass = 1; S.speedBase = 200; S.speedSpire = 0;   // a straight flight
    const fan = { from: -spanDeg*D2R/2, span: spanDeg*D2R, rbar: 150, P: 1, conv: 1 };
    const muzzle = { x: 0, y: 0, dir: 0, run: 0, id: -1 };
    const b = sim.makeBolt(fan, force, muzzle);
    const buf = []; let bites = 0, wood = E.list.length;
    for (let k = 0; k < 60000; k++){
      const prev = sim.stepBolt(b, 1/240);
      const px = prev[0]-S.coreSep, py = prev[1], cx = b.x-S.coreSep, cy = b.y;
      if (cx*cx + cy*cy < S.coreR*S.coreR) break;
      if (!b.alive){ b.alive = []; for (let z = 0; z < b.n; z++) b.alive.push(1); }
      const p = sim.pressure(b.F, b.L);
      let ux = -(b.y-prev[1]), uy = (b.x-prev[0]); const ul = Math.hypot(ux,uy)||1; ux/=ul; uy/=ul;
      let live = 0, dirty = false;
      for (let q = 0; q < b.n; q++){
        if (!b.alive[q]) continue; live++;
        const off = b.n === 1 ? 0 : (q/(b.n-1)-0.5)*b.L0;
        const ax = px+ux*off, ay = py+uy*off, bx = cx+ux*off, by = cy+uy*off;
        let hit = null, bd = 1e9;
        for (const n of sim.gridNear(E, bx, by, buf)){
          if (!E.nodes.has(n.id)) continue;
          if (!cross(ax,ay,bx,by,n.x0,n.y0,n.x1,n.y1)) continue;
          const d = Math.hypot((n.x0+n.x1)/2-ax, (n.y0+n.y1)/2-ay);
          if (d < bd){ bd = d; hit = n; }
        }
        if (!hit) continue;
        if (p > hit.thick){ b.F = Math.max(0, b.F-hit.thick); sim.cutNode(E, hit); dirty = true; bites++; }
        else { hit.cracked = true; b.alive[q] = 0; live--; }
      }
      b.L = b.L0*live/b.n;
      if (dirty){ sim.layout(E); sim.buildGrid(E); }
      if (live <= 0 || b.F < 0.05 || b.run > 4000 || Math.hypot(b.x,b.y) > S.coreSep*3) break;
    }
    S.gravMass = gm; S.speedBase = sb; S.speedSpire = ss;
    return { bites, wood: wood - E.list.length };
  }
  // the tightest front a fan can read against the widest a fan can be
  const spike = volley(0, 20), sheet = volley(S.wedgeCap, 20);
  check("a narrow front gets deeper", spike.wood/Math.max(1,spike.bites) > sheet.wood/Math.max(1,sheet.bites)*1.5,
        (spike.wood/Math.max(1,spike.bites)).toFixed(1) + " nodes per cut vs " +
        (sheet.wood/Math.max(1,sheet.bites)).toFixed(1));
  check("a spike takes the most wood", spike.wood > sheet.wood*1.4,
        "spike " + spike.wood + " nodes vs sheet " + sheet.wood);
  // Recorded, not asserted: on a straight approach a wide front is simply
  // worse. It clips twigs where a spike drops whole limbs, and a deep cut
  // takes the shallow wood with it. Width has no offensive niche yet; the
  // ward is what is meant to give it one, and there is nothing to ward here.
  check("a wide front is the weaker attack, and that is the open question",
        sheet.wood <= spike.wood,
        "sheet " + sheet.wood + " nodes in " + sheet.bites + " cuts, spike " +
        spike.wood + " in " + spike.bites);
}

// ── fading ─────────────────────────────────────────────────────────────
suite("A shot runs down");
{
  reset();
  // Force is spent against distance flown, not against a clock, so the rule
  // scales with the field the way everything else here does. What it buys is
  // that a captured orbit which meets nothing goes round a few times, dimming,
  // instead of circling the board for ever.
  const esc = Math.sqrt(2*S.gravMass/S.coreSep);
  function fly(v, stop){
    const th = 0.9;
    const b = { x:Math.cos(th)*S.coreR, y:Math.sin(th)*S.coreR,
                vx:Math.cos(th)*v, vy:Math.sin(th)*v, F:6, F0:6, run:0, trail:[] };
    let wound = 0, prev = null;
    for (let k = 0; k < 400000; k++){
      sim.stepBolt(b, 1/240);
      const a = Math.atan2(b.y, b.x - S.coreSep);
      if (prev !== null) wound += wrap(a - prev);
      prev = a;
      if (b.F < 6*stop || Math.hypot(b.x,b.y) > S.coreSep*4) break;
    }
    return { laps: Math.abs(wound)/(2*Math.PI), run: b.run, F: b.F };
  }
  const slow = fly(esc*0.45, 0.02);
  check("a captured shot goes round five or six times before it is spent",
        slow.laps > 4 && slow.laps < 9,
        slow.laps.toFixed(1) + " laps, " + Math.round(slow.run) + "u flown");
  const early = fly(esc*0.45, 0.6);
  check("and it is still dangerous on the first pass", early.laps < 1.2,
        "down to three fifths of its force after " + early.laps.toFixed(2) + " of a lap");
  const held = S.fadeHalf; S.fadeHalf = 0;
  const forever = fly(esc*0.45, 0.02);
  S.fadeHalf = held;
  check("switching the fade off puts it back in orbit for ever",
        forever.run > slow.run*2.5,
        Math.round(slow.run) + "u with the fade, " + Math.round(forever.run) + "u without");
  check("fade is measured in units of flight, not seconds",
        Math.abs(fly(esc*0.45, 0.02).run - slow.run) < 1e-6 &&
        Math.abs(6*Math.pow(0.5, slow.run/S.fadeHalf) - slow.F) < 0.02,
        "half its force every " + S.fadeHalf + "u, whatever the timestep");
}

// ── loops ──────────────────────────────────────────────────────────────
suite("The circuit");
{
  reset();
  const T = grow(220);
  // fuse a pair of tips far enough apart to close something worth having
  // the pair within reach that would close the widest circuit, as a player
  // reaching across from one limb to another would choose it
  const buds = T.list.filter(n => n.bud);
  let A = null, B = null, best = 0;
  for (let i = 0; i < buds.length; i++) for (let j = i+1; j < buds.length; j++){
    if (buds[i].parent === buds[j].parent) continue;
    if (Math.hypot(buds[i].x1-buds[j].x1, buds[i].y1-buds[j].y1) > S.graftR) continue;
    const ar = sim.circuitArea(T, buds[i], buds[j]);
    if (ar > best){ best = ar; A = buds[i]; B = buds[j]; }
  }
  check("the canopy offers pairs close enough to fuse by hand", !!A,
        A ? "nearest usable pair " + Math.hypot(A.x1-B.x1, A.y1-B.y1).toFixed(1) +
            "u apart, inside a reach of " + S.graftR : "none within " + S.graftR + "u");
  sim.makeGraft(T, A, B); sim.layout(T);
  const lp = sim.loopPoly(T, B), area = lp ? lp.area : 0;
  check("one graft closes a circuit worth something",
        sim.loopAmp(area) > 1.05,
        Math.round(area/(S.coreR*S.coreR)) + " core-areas, amplifying \u00d7" +
        sim.loopAmp(area).toFixed(2));
  // (below the ceiling, where compounding is the whole of the rule)
  const small = 5*S.coreR*S.coreR;
  check("gain compounds, so one wide circuit beats two tight ones",
        sim.loopAmp(small*2) > sim.loopAmp(small)*sim.loopAmp(small) - 1e-9,
        "\u00d7" + sim.loopAmp(small).toFixed(3) + " twice over is \u00d7" +
        (sim.loopAmp(small)*sim.loopAmp(small)).toFixed(3) + ", doubled at once is \u00d7" +
        sim.loopAmp(small*2).toFixed(3));

  // the wood carrying a circuit is not offered as a cut, the way the trunk is not
  sim.markLoops(T);
  const inLoop = T.list.filter(n => n.loop);
  check("the circuit is a named piece of the tree", inLoop.length > 2,
        inLoop.length + " internodes carry it");
  sim.bestSpire(T);
  const fan = sim.bestFan(T);
  sim.valueCuts(T, sim.capacity(T.girth), () => fan, sim.targetOf(null), sim.loopAmp(area));
  check("and the glow never recommends cutting it",
        inLoop.every(n => n.eff === 0) && T.list.some(n => n.eff > 0),
        "every limb in the loop scores zero, as the trunk does");

  // but enemy fire goes straight through it
  const carrier = inLoop.find(n => n.parent !== null && T.nodes.has(n.id));
  sim.cutNode(T, carrier); sim.layout(T);
  check("enemy fire through the circuit takes the gain with it",
        T.grafts.length === 0,
        "one severed internode and the junction lets go");
}

// ── charge ─────────────────────────────────────────────────────────────
suite("Charge");
{
  const T = grow(220);
  const green = T.list.reduce((a,n) => a + n.len*(1 - sim.stiffOf(n)), 0);
  const limb = T.list.find(n => n.order <= 1 && Math.hypot(n.x1,n.y1) > 60 && Math.hypot(n.x1,n.y1) < 80);
  const cut = sim.greenOf(T, limb)*S.chargeWood;
  check("one cut oversupplies a young figure", cut > sim.capacity(T.girth),
        cut.toFixed(1) + " released, " + sim.capacity(T.girth).toFixed(1) + " channellable");
  // Two axes, kept apart on purpose: girth is how much a cut can channel,
  // loops are how much what leaves is worth.
  check("only girth widens the channel",
        sim.capacity(S.girthRef*2.5) > sim.capacity(S.girthRef)*3,
        sim.capacity(S.girthRef).toFixed(1) + " at par girth -> " +
        sim.capacity(S.girthRef*2.5).toFixed(1) + " at two and a half times it");
  const A = 12*S.coreR*S.coreR;
  check("a loop multiplies what leaves it", sim.loopAmp(A) > 1.2 && sim.loopAmp(0) === 1,
        "twelve core-areas of circuit amplify every shot \u00d7" + sim.loopAmp(A).toFixed(2));
  check("and the feedback has a ceiling", sim.loopAmp(A*40) <= S.loopCap + 1e-9 &&
        sim.loopAmp(A*40) > sim.loopAmp(A),
        "a lattice bottoms out at \u00d7" + S.loopCap + ", not at infinity");
  check("the whole tree is a finite magazine", green*S.chargeWood < 400,
        (green*S.chargeWood).toFixed(0) + " charge standing");
}

// ── the paths that are off by default ──────────────────────────────────
suite("Switches and determinism");
{
  reset();
  const a = grow(200), b = grow(200);
  const sig = T => T.list.map(n => n.x1.toFixed(3) + "," + n.y1.toFixed(3)).join("|");
  check("growth is deterministic", sig(a) === sig(b), a.list.length + " nodes, identical twice");

  reset();
  const U = grow(220);
  for (const n of U.list) if (n.bud) n.bud = false;
  sim.layout(U);
  const wide = sim.bestFan(U);
  S.fanRes = 6;
  const thin = sim.bestFan(U);
  check("tip resolution thins a crowded rim", thin.span > wide.span,
        (wide.span*57.3).toFixed(0) + "\u00b0 -> " + (thin.span*57.3).toFixed(0) + "\u00b0");
  reset();

  function pass(selfPull){
    S.selfPull = selfPull;
    const bo = { x: Math.cos(1.2)*S.coreR, y: Math.sin(1.2)*S.coreR,
                 vx: Math.cos(1.2)*90, vy: Math.sin(1.2)*90, F: 6, F0: 6, run: 0, trail: [] };
    let home = 1e9;
    for (let k = 0; k < 80000; k++){
      sim.stepBolt(bo, 1/240);
      home = Math.min(home, Math.hypot(bo.x, bo.y));
      if (bo.F < 0.12 || Math.hypot(bo.x, bo.y) > S.coreSep*4) break;
    }
    return home;
  }
  const free = pass(0), pulled = pass(0.6);
  reset();
  check("your own pull drags a shot back home", pulled < free*0.8,
        "closest approach to your own core " + free.toFixed(0) + "u -> " + pulled.toFixed(0) + "u");

  const deep = sim.forkLen({ gen: 6, order: 0, ram: 40 });
  check("fork interval never falls below a joint and a half",
        deep >= S.internode*1.5 - 1e-9 && deep < sim.genome().forkLen,
        "forty levels of ramification bottoms out at " + deep.toFixed(1) + "u");
}

// ── the frame ──────────────────────────────────────────────────────────
suite("The board holds still");
{
  reset();
  // The two pots are fixed points in the world. They have to be fixed points
  // on the screen too, or the field appears to close up as the trees fill it
  // and everything slides under the hand that is trying to hold a twig.
  const at = (x, v, W) => (x - v.fx)*v.scale + W/2;
  const v0 = sim.frameView(1400, 900);
  const mine = at(0, v0, 1400), theirs = at(S.coreSep, v0, 1400);
  check("the frame is a function of the field and the window, and takes no tree",
        sim.frameView.length <= 3 && v0.fx === S.coreSep/2 && v0.fy === 0,
        "centred on the field at " + v0.fx + ", scale " + v0.scale.toFixed(3));
  check("the two cores sit symmetrically about the middle",
        Math.abs((700 - mine) - (theirs - 700)) < 1e-9,
        "pots at " + Math.round(mine) + " and " + Math.round(theirs) + " of 1400");
  check("a mature canopy fits inside it",
        900/2/v0.scale > 260,
        "the frame shows \u00b1" + Math.round(900/2/v0.scale) +
        "u of sky, against a reach of about 250 at four minutes");
  check("it holds still however the field is repainted",
        JSON.stringify(sim.frameView(1400, 900)) === JSON.stringify(v0),
        "same window, same frame, every time");

  S.coreSep = 1100;
  const wide = sim.frameView(1400, 900);
  reset();
  check("a wider field pulls the view back", wide.scale < v0.scale && wide.fx > v0.fx,
        "scale " + v0.scale.toFixed(2) + " -> " + wide.scale.toFixed(2) +
        " when the mages stand " + 1100 + "u apart");
  const tall = sim.frameView(1400, 1800);
  check("a taller window shows more of the field, never less",
        tall.scale >= v0.scale, v0.scale.toFixed(2) + " -> " + tall.scale.toFixed(2));
}

// ── randomised soak ────────────────────────────────────────────────────
suite("Soak (1400 rounds of random play)");
{
  reset();
  let seed=12345; const rnd=()=>((seed=(seed*1103515245+12345)&0x7fffffff)/0x7fffffff);
const problems=new Map();
function bad(what,extra){ const k=what; problems.set(k,(problems.get(k)||0)+1);
  if(problems.get(k)===1) console.log("  !! "+what+(extra?"   "+extra:"")); }
const fin=v=>typeof v==="number"&&isFinite(v);

function audit(tag){
  if(T2.list.length!==T2.nodes.size) bad("list and map disagree",tag+" "+T2.list.length+" vs "+T2.nodes.size);
  const seen=new Set();
  for(const n of T2.list){
    if(seen.has(n.id)) bad("node listed twice",tag);
    seen.add(n.id);
    for(const f of ["x0","y0","x1","y1","rel","rest","rel0","len","mass","age","abs","thick","healGoal","healAt"])
      if(!fin(n[f])) bad("non-finite "+f,tag+" node "+n.id+" = "+n[f]);
    if(n.len<0) bad("negative length",tag);
    if(n.len>S.internode*1.001&&!n.slave) bad("internode overrun",tag+" "+n.len.toFixed(3));
    if(n.mass<0) bad("negative mass",tag);
    if(n.parent===null){ if(T2.roots.indexOf(n.id)<0) bad("rootless node not in roots",tag); }
    else {
      const p=T2.nodes.get(n.parent);
      if(!p) bad("dangling parent",tag);
      else if(p.children.indexOf(n.id)<0) bad("parent does not own child",tag);
    }
    for(const c of n.children) if(!T2.nodes.has(c)) bad("dangling child",tag);
    if(n.bud&&n.children.length) bad("a bud with children",tag);
  }
  for(const id of T2.roots) if(!T2.nodes.has(id)) bad("dangling root",tag);
  if(T2.roots.length>3) bad("too many primordia",tag+" "+T2.roots.length);
  for(const id of T2.grafts){
    const b=T2.nodes.get(id);
    if(!b){ bad("graft points at a dead node",tag); continue; }
    if(!b.slave) bad("non-slave in the graft list",tag);
    const a=b.mate===null?null:T2.nodes.get(b.mate);
    if(!a) bad("half a graft",tag);
    else if(a.mate!==b.id) bad("graft not mutual",tag);
  }
  for(const n of T2.list) if(n.mate!==null&&!T2.nodes.has(n.mate)) bad("mate points nowhere",tag);
}

const T2=sim.newTree(0);
let ops={grow:0,cut:0,swathe:0,bend:0,graft:0,fire:0};
const sbolts=[]; const D2=sim.newTree(180);
for(let t=0;t<260;t+=0.15) sim.step(D2,0.15,null);
sim.layout(D2); sim.buildGrid(D2); D2.hp=S.coreHP;

for(let round=0;round<1400;round++){
  for(let k=0;k<12;k++) sim.step(T2,0.05);
  sim.layout(T2); ops.grow++;
  const r=rnd();
  if(r<0.22){                                    // slice
    const pool=T2.list.filter(n=>n.parent!==null);
    if(pool.length){ const v=pool[Math.floor(rnd()*pool.length)];
      if(T2.nodes.has(v.id)){ sim.greenOf(T2,v); sim.cutNode(T2,v); ops.cut++; } }
    sim.layout(T2);
  } else if(r<0.40){                             // a stroke across several limbs
    const lo=(rnd()*2-1)*Math.PI, hi=lo+0.5;
    const swathe=T2.list.filter(n=>{
      if(n.parent===null) return false;
      const a=Math.atan2(n.y0,n.x0);
      return a>=lo&&a<=hi;
    });
    for(const v of swathe) if(T2.nodes.has(v.id)) sim.cutNode(T2,v);
    if(swathe.length) ops.swathe++;
    sim.layout(T2);
  } else if(r<0.75){                             // bend and let go early or late
    const pool=T2.list.filter(n=>sim.bendLimit(n)>0.002);
    if(pool.length){
      const g=sim.bendGroup(T2,pool[Math.floor(rnd()*pool.length)]);
      const kept=rnd()<0.5?1:Math.pow(rnd(),2);
      for(const n of g){ const lim=sim.bendLimit(n);
        n.rel=n.rest+(rnd()*2-1)*lim;
        n.rest=n.rest+(n.rel-n.rest)*kept; n.rel=n.rest; }
      sim.layout(T2); ops.bend++;
    }
  } else if(r<0.85){                             // graft any two near tips
    const buds=T2.list.filter(n=>n.bud&&n.mate===null);
    let A=null,B=null,bd=S.graftR;
    for(let i=0;i<buds.length;i++)for(let j=i+1;j<buds.length;j++){
      if(buds[i].parent===buds[j].parent)continue;
      const d=Math.hypot(buds[i].x1-buds[j].x1,buds[i].y1-buds[j].y1);
      if(d<bd){bd=d;A=buds[i];B=buds[j];}}
    if(A&&B){ sim.makeGraft(T2,A,B); sim.layout(T2); ops.graft++; }
  } else {                                       // fire whatever we have
    const f=sim.bestFan(T2);
    if(f){
      sim.bestSpire(T2);                          // runLen/runDir feed the muzzle
      const live=T2.list.filter(n=>n.parent!==null);
      const mz=live.length?sim.muzzleFor(T2,live[Math.floor(rnd()*live.length)]):null;
      if(mz){ sbolts.push(sim.makeBolt(f,S.forceK*f.P,mz)); ops.fire++; }
    }
  }
  // fly the bolts a little
  const buf=[];
  for(let i=sbolts.length-1;i>=0;i--){
    const b=sbolts[i];
    for(let k=0;k<30;k++) sim.stepBolt(b,1/60);
    if(!fin(b.x)||!fin(b.y)||!fin(b.vx)) bad("bolt went non-finite");
    if(b.F<0.05||b.run>4000||Math.hypot(b.x,b.y)>S.coreSep*4) sbolts.splice(i,1);
  }
  if(round%25===0){ sim.markLoops(T2); audit("round "+round); }
  if(T2.roots.length===0){ bad("tree wiped out","round "+round); break; }
}
sim.layout(T2); audit("final");
  check("nothing comes loose", problems.size === 0,
        problems.size ? [...problems].map(function(e){ return e[0]+" x"+e[1]; }).join("; ")
                      : JSON.stringify(ops) + ", final tree " + T2.list.length + " nodes");
}

// ── reading the tree ───────────────────────────────────────────────────
suite("Where to cut");
{
  reset();
  const T = grow(300);
  sim.bestSpire(T);
  for (const n of T.list) if (n.bud && Math.abs(Math.atan2(n.y1,n.x1)) < 0.45) n.bud = false;
  sim.layout(T);
  const fan = sim.bestFan(T), byB = fan.byBearing;
  const fanOf = b => { let best = fan, bd = 1e9;
    for (const f of byB){ if (!f) continue;
      let d = Math.abs(f.from + f.span/2 - b);
      while (d > Math.PI) d = Math.abs(d - 2*Math.PI);
      if (d < bd){ bd = d; best = f; } }
    return best; };
  const band = girth => {
    const cap = sim.capacity(girth);
    const top = sim.valueCuts(T, cap, fanOf);
    const lit = T.list.filter(n => n.parent !== null && n.eff > top*0.7);
    const mean = a => a.reduce((x,y) => x+y, 0)/Math.max(1, a.length);
    return { r: mean(lit.map(n => Math.hypot(n.x0,n.y0))),
             thick: mean(lit.map(n => n.thick)),
             force: mean(lit.map(n => n.val)), lit: lit.length, top };
  };
  const bare = band(S.girthRef), aged = band(S.girthRef*2.6);
  check("the glow picks out a band, not the whole tree",
        bare.lit > 3 && bare.lit < T.list.length*0.25,
        bare.lit + " limbs of " + T.list.length + " burn near the top value");
  check("on a young trunk the band sits out in the thin wood",
        bare.r > 0.5*T.maxR && bare.thick < 5,
        (bare.r/T.maxR*100).toFixed(0) + "% out, wood " + bare.thick.toFixed(1) + " thick");
  check("girth walks the band onto heavier limbs",
        aged.thick > bare.thick*1.3 && aged.force > bare.force*2,
        (aged.r/T.maxR*100).toFixed(0) + "% out, wood " + aged.thick.toFixed(1) +
        " thick, " + aged.force.toFixed(0) + " force against " + bare.force.toFixed(0));
  const trunk = T.nodes.get(T.roots[0]);
  check("the trunk is never a cut", trunk.val === 0 && trunk.eff === 0,
        "it holds " + (trunk.sub*S.chargeWood).toFixed(0) + " charge and offers none of it");
}

// ── the long game ──────────────────────────────────────────────────────
suite("An old trunk");
{
  reset();
  function life(chopR, every, secs){
    const T = sim.newTree(0);
    let next = every;
    for (let t = 0; t < secs; t += 0.05){
      sim.step(T, 0.05);
      if (t < next) continue;
      sim.layout(T); next += every;
      const v = T.list.filter(n => {
        const p = n.parent === null ? null : T.nodes.get(n.parent);
        return p && Math.hypot(n.x1,n.y1) > chopR && Math.hypot(p.x1,p.y1) <= chopR;
      });
      for (const x of v) if (T.nodes.has(x.id)) sim.cutNode(T, x);
      sim.layout(T);
    }
    sim.layout(T);
    if (chopR < 1e8){                     // measured in its shaped state, as kept
      const v = T.list.filter(n => {
        const p = n.parent === null ? null : T.nodes.get(n.parent);
        return p && Math.hypot(n.x1,n.y1) > chopR && Math.hypot(p.x1,p.y1) <= chopR;
      });
      for (const x of v) if (T.nodes.has(x.id)) sim.cutNode(T, x);
      sim.layout(T);
    }
    const tr = T.nodes.get(T.roots[0]);
    return { girth: tr.thick, reach: T.maxR, squat: tr.thick/T.maxR,
             cap: sim.capacity(T.girth), vig: T.g.vigor };
  }
  const young = life(1e9, 1e9, 300);
  const old   = life(1e9, 1e9, 1600);
  const bonsai = life(45, 40, 1600);
  check("a trunk never stops thickening", old.girth > young.girth*2,
        young.girth.toFixed(0) + " at 300s -> " + old.girth.toFixed(0) + " at 1600s");
  check("girth raises what a cut can channel", old.cap > young.cap*3,
        young.cap.toFixed(0) + " -> " + old.cap.toFixed(0) + " of charge per shot");
  check("girth buys weight, not haste", Math.abs(old.vig - young.vig) < 1e-9,
        "the budget is " + old.vig.toFixed(0) + " u/s at any age \u2014 an old mage " +
        "hits harder, it does not hurry");
  check("a long-pruned tree is absurdly squat", bonsai.squat > 0.6,
        "trunk " + bonsai.girth.toFixed(0) + " against a reach of " +
        bonsai.reach.toFixed(0) + " \u2014 " + (bonsai.squat*100).toFixed(0) + "% as thick as it is long");
  check("and just as powerful as the sprawling one", bonsai.cap > old.cap*0.8,
        bonsai.cap.toFixed(0) + " of capacity in a tree " +
        (bonsai.reach/old.reach*100).toFixed(0) + "% the size");
  reset();
}

// ── the husk ───────────────────────────────────────────────────────────
suite("The husk");
{
  const young = grow(30), old = grow(240);
  check("a seedling's core sits in a husk, and the trunk splits it", young.husk && !old.husk,
        "whole at 30s (trunk " + young.girth.toFixed(1) + "), gone by 240s (trunk " + old.girth.toFixed(1) +
        " against " + S.huskGirth + ")");
  const g = require(__dirname + "/harness.js")(FILE);
  g.T = g.newTree(0, g.genome({})); g.layout(g.T); g.T.hp = g.T.hpMax = 60;
  g.newFoe(g.genome({}), "still", 1);
  const fire = () => {             // straight down the line into their pot, harder than anything
    g.bolts.length = 0;
    const b = g.makeBolt(null, 500, { x: S.coreR, y: 0, dir: 0, run: 300, id: -1 }, g.targetOf(g.TD));
    g.launch(b, false);
    for (let k = 0; k < 4000 && g.bolts.length; k++) g.stepBolts(1/120);
  };
  const hp0 = g.TD.hp; fire();
  const kept = g.TD.hp === hp0;
  g.TD.husk = false; fire();
  check("while it holds nothing reaches the core; once it splits, everything can", kept && g.TD.hp < hp0,
        "a 500-force shot: core untouched through the husk, " + (hp0 - g.TD.hp).toFixed(0) + " taken without it");
}

// ── the other mage ─────────────────────────────────────────────────────
// Needs shots in the air and landing, which is the renderer's half of the
// file; the harness loads the whole game headless.
suite("The other mage");
{
  const load = require(__dirname + "/harness.js");
  function duel(mine, theirs, secs, sd, over){
    const g = load(FILE), S2 = g.S;
    Object.assign(S2, over || {});
    g.T = g.newTree(0, g.genome({})); g.layout(g.T); g.buildGrid(g.T);
    g.T.hpMax = g.T.hp = g.coreOf(g.T.g);
    g.newFoe(g.genome({}), theirs, sd);
    const M = g.newMind(mine, sd), dt = 0.05, trace = [], log = { ready: [], shots: 0 };
    let readyAt = null, t = 0;
    for (; t < secs; t += dt){
      const T = g.T, TD = g.TD;
      if (T.hp > 0) g.step(T, dt, null);
      if (TD.hp > 0) g.step(TD, dt, null);
      g.layout(T); g.buildGrid(T); g.layout(TD); g.buildGrid(TD);
      if (T.hp > 0 && TD.hp > 0){
        const atT = g.targetOf(T), atTD = g.targetOf(TD);   // both read before either cuts
        const a = g.mindStep(T, M, dt, atTD); if (a) g.launch(a, false);
        const was = TD.mind.state;
        const b = g.mindStep(TD, TD.mind, dt, atT);
        if (TD.mind.state === "ready" && was !== "ready") readyAt = t;
        if (b){ g.launch(b, true); log.shots++; if (readyAt !== null) log.ready.push(t - readyAt); readyAt = null; }
      }
      g.layout(T); g.buildGrid(T); g.layout(TD); g.buildGrid(TD);
      for (let k = 0; k < 3; k++) g.stepBolts(dt/3);
      if (Math.round(t/dt) % 600 === 0) trace.push([T.hp, TD.hp, T.list.length, TD.list.length]);
      if (T.hp <= 0 || TD.hp <= 0) break;
    }
    return { g, t, trace, log, mine: g.T.hp/g.T.hpMax, theirs: g.TD.hp/g.TD.hpMax };
  }

  const g0 = load(FILE);
  g0.newFoe(g0.genome({}), "keeper", 3);
  const A = g0.newTree(0, g0.genome({}));
  for (let t = 0; t < 120; t += 0.05){ g0.step(A, 0.05, null); g0.step(g0.TD, 0.05, null); }
  g0.layout(A); g0.layout(g0.TD);
  const same = A.list.length === g0.TD.list.length &&
               A.list.every((n, i) => Math.abs(n.x1 - g0.TD.list[i].x1) < 1e-9 && Math.abs(n.y1 - g0.TD.list[i].y1) < 1e-9);
  check("their tree stands in its own frame exactly as yours does", same,
        A.list.length + " nodes each, identical coordinates from their own pots");

  const mirror = duel("master", "master", 480, 3);
  const even = mirror.trace.every(r => r[0] === r[1] && r[2] === r[3]);
  check("a mirror match is dead even", even && mirror.mine === mirror.theirs,
        "two Masters from the same seed: cores at " + (mirror.mine*100).toFixed(1) + "% and " +
        (mirror.theirs*100).toFixed(1) + "% after " + Math.round(mirror.t) + "s, trees identical at every check");

  const still = duel("still", "still", 200, 3);
  check("a still mage never fires", still.log.shots === 0 && still.mine === 1, "200s, no shots");

  // Each temper against a tree nobody tends, over three seeds and four
  // minutes of fire: how much force reaches the core, and when.
  function harass(level, secs){
    const out = { dmg: 0, early: 0, shots: 0, ready: [], stat: { shots: 0, pass0: 0, pass1: 0, better: 0, worse: 0 } };
    for (const sd of [1, 3, 5]){
      const g = load(FILE);
      g.T = g.newTree(0, g.genome({})); g.layout(g.T); g.buildGrid(g.T); g.T.hp = g.T.hpMax = 1e9;
      g.newFoe(g.genome({}), level, sd);
      let readyAt = null;
      for (let t = 0; t < secs; t += 0.05){
        g.step(g.T, 0.05, null); g.step(g.TD, 0.05, null);
        g.layout(g.T); g.buildGrid(g.T); g.layout(g.TD);
        const was = g.TD.mind.state;
        const b = g.mindStep(g.TD, g.TD.mind, 0.05, g.T);
        if (g.TD.mind.state === "ready" && was !== "ready") readyAt = t;
        if (b){ g.launch(b, true); out.shots++; if (readyAt !== null) out.ready.push(t - readyAt); readyAt = null; }
        g.layout(g.TD); g.buildGrid(g.TD);
        const hp = g.T.hp, husked = g.T.husk;
        for (let k = 0; k < 3; k++) g.stepBolts(0.05/3);
        out.dmg += hp - g.T.hp; if (husked) out.early += hp - g.T.hp;
      }
      const st = g.TD.mind.stat;
      if (st) for (const k in st) out.stat[k] += st[k];
    }
    return out;
  }
  const hF = harass("feral", 400), hK = harass("keeper", 400), hM = harass("master", 400);
  const aim = h => h.stat || { shots: 0, pass0: 0, pass1: 0, better: 0, worse: 0 };
  const aF = aim(hF), aK = aim(hK), aM = aim(hM);
  check("a Feral mage never touches the stem before it fires",
        aF.better === 0 && aF.worse === 0 && aF.shots > 3,
        aF.shots + " shots, every one out of the limb exactly as it grew");
  check("aiming closes the pass the shot is predicted to make",
        aK.better > aK.worse && aM.better > aM.worse &&
        aK.pass1 < aK.pass0 && aM.pass1 < aM.pass0,
        "Keeper " + (aK.pass0/aK.shots).toFixed(0) + "u \u2192 " + (aK.pass1/aK.shots).toFixed(0) +
        "u, Master " + (aM.pass0/aM.shots).toFixed(0) + "u \u2192 " + (aM.pass1/aM.shots).toFixed(0) +
        "u from their cores");
  check("and they fire at the cadence their temper says",
        hM.shots > hK.shots && hK.shots > 3 && hF.shots > 3,
        "over three seeds and 400s: Master " + hM.shots + " shots, Keeper " + hK.shots +
        ", Feral " + hF.shots + "; into the core, " + hM.dmg.toFixed(0) + ", " +
        hK.dmg.toFixed(0) + " and " + hF.dmg.toFixed(0) + " force against a core that holds " + S.coreHP +
        " (which shot lands is luck enough that these do not rank reliably)");
  check("nothing reaches a seedling's core through its husk", hF.early + hK.early + hM.early === 0,
        (hF.shots + hK.shots + hM.shots) + " shots between them, none of them through the husk");
  const tell = [].concat(hK.ready, hM.ready);
  const MN = g0.MINDS;
  check("every shot is telegraphed for its full wind-up", tell.length > 5 &&
        hM.ready.every(x => x >= MN.master.windup - 0.051) && hK.ready.every(x => x >= MN.keeper.windup - 0.051),
        "shortest tell " + Math.min(...tell).toFixed(2) + "s over " + tell.length + " shots");

  // shoot the loaded limb off and the shot never comes
  {
    const g = load(FILE);
    g.T = g.newTree(0, g.genome({})); g.layout(g.T); g.T.hp = g.T.hpMax = 30;
    g.newFoe(g.genome({}), "master", 5);
    const TD = g.TD, M = TD.mind;
    let t = 0;
    for (; t < 300 && M.state === "grow"; t += 0.05){
      g.step(g.T, 0.05, null); g.step(TD, 0.05, null); g.layout(g.T);
      g.mindStep(TD, M, 0.05, g.T);
    }
    const had = M.state !== "grow", limb = M.limb;
    g.cutNode(TD, TD.nodes.get(limb.parent) || limb); g.layout(TD);
    const shot = g.mindStep(TD, M, 0.05, g.T);
    check("cutting the limb it is aiming disarms it", had && !shot && M.state === "grow" && M.limb === null,
          "chose a limb at " + Math.round(t) + "s; shot off, it went back to growing");
  }

  // coppice: a tree shot down to a scarred stool comes back
  {
    const T = grow(200);
    const root = T.nodes.get(T.roots[0]);
    for (const id of root.children.slice()) sim.cutNode(T, T.nodes.get(id));
    root.cracked = true; root.healGoal = 0;
    for (let t = 0; t < 60; t += 0.05) sim.step(T, 0.05);
    sim.layout(T);
    check("a tree cut to a scarred stool sprouts again", tips(T) > 0 && T.list.length > 3,
          T.list.length + " nodes, " + tips(T) + " tips a minute later");
    const E = sim.newTree(0, seed());
    E.roots.length = 0; E.nodes.clear();
    for (let t = 0; t < 30; t += 0.05) sim.step(E, 0.05);
    sim.layout(E);
    check("and an empty pot starts over from a seedling", E.roots.length === 1 && tips(E) > 0,
          E.list.length + " nodes after 30s");
  }
}

// ── volleys ────────────────────────────────────────────────────────────
suite("Volleys");
{
  const fig = { cap: 10, fan: null, gain: 1 };
  const mz = (deg, run) => ({ x: 40*Math.cos(deg*D2R), y: 40*Math.sin(deg*D2R), dir: deg*D2R, run: run || 0, id: deg });
  const mass = (b, m) => b.F/(S.forceK*sim.muzzleSpeed(m.run));
  const total = (bs, fs) => bs.reduce((a, b, i) => a + mass(b, fs[i].muzzle), 0);
  const charge = h => h/S.chargeWood;          // wood that holds h of charge

  // one face is exactly one cut
  {
    const f = [{ charge: charge(25), muzzle: mz(10, 30) }];
    const v = sim.volleyFrom(fig, f, null), one = sim.shotFrom(fig, f[0].charge, f[0].muzzle, null);
    check("a stroke that opens one face fires exactly the shot a single cut does",
          v.length === 1 && Math.abs(v[0].F - one.F) < 1e-9 && v[0].L === one.L && v[0].vx === one.vx,
          "force " + v[0].F.toFixed(2) + " against " + one.F.toFixed(2));
  }
  // four even faces: one shot each, out of each face, channel widened by √4
  {
    const f = [0, 20, -20, 40].map(d => ({ charge: charge(20), muzzle: mz(d, 10) }));
    const v = sim.volleyFrom(fig, f, null);
    const dirs = v.map(b => Math.round(Math.atan2(b.vy, b.vx)/D2R)).sort((a, b) => a - b);
    check("four even faces throw four shots, each along its own stem",
          v.length === 4 && dirs.join() === "-20,0,20,40", "bearings " + dirs.join("°, ") + "°");
    const m = total(v, f), each = Math.max(...v.map((b, i) => mass(b, f[i].muzzle)));
    check("and pass twice what one cut can channel between them, none more than one cut would",
          Math.abs(m - 2*fig.cap) < 1e-6 && each <= fig.cap + 1e-9,
          m.toFixed(1) + " in all against a channel of " + fig.cap + ", " + each.toFixed(1) + " the heaviest");
    S.volleyExp = 0;
    const flat = total(sim.volleyFrom(fig, f, null), f);
    reset();
    check("with no widening a volley passes exactly one cut's worth, only spread",
          Math.abs(flat - fig.cap) < 1e-6, flat.toFixed(2));
  }
  // a heavy limb with three twigs nicked on the way earns next to nothing for them
  {
    const f = [{ charge: charge(40), muzzle: mz(0) }].concat(
      [15, -15, 30].map(d => ({ charge: charge(0.6), muzzle: mz(d) })));
    const v = sim.volleyFrom(fig, f, null), m = total(v, f);
    check("nicking twigs on the way to a limb does not widen the channel",
          m < fig.cap*1.06, m.toFixed(2) + " against " + fig.cap + " for the limb alone");
  }
  // a stroke across the whole crown throws no more than volleyMax shots
  {
    const f = [];
    for (let d = -60; d <= 60; d += 5) f.push({ charge: charge(3), muzzle: mz(d) });
    const v = sim.volleyFrom(fig, f, null);
    check("and a stroke across the whole crown throws at most " + S.volleyMax,
          v.length === S.volleyMax, f.length + " faces, " + v.length + " shots");
  }
  // on real wood: a stroke across the crown against a stroke across one limb
  {
    const T = grow(240);
    const fig2 = { cap: sim.capacity(T.girth), fan: sim.bestFan(T), gain: 1 };
    const R = T.maxR, X = R*0.7, cut = [];
    for (const n of T.list){
      if (n.parent === null) continue;
      if (cross(X, -R, X, R, n.x0, n.y0, n.x1, n.y1)) cut.push(n);
    }
    const faces = new Map();
    for (const n of cut){
      let q = T.nodes.get(n.parent), shadow = false;
      while (q){ if (cut.includes(q)){ shadow = true; break; } q = q.parent === null ? null : T.nodes.get(q.parent); }
      if (shadow) continue;
      const m = sim.muzzleFor(T, n), f = faces.get(m.id) || { charge: 0, muzzle: m };
      f.charge += sim.greenOf(T, n); faces.set(m.id, f);
    }
    const fs = [...faces.values()];
    const v = sim.volleyFrom(fig2, fs, null);
    const spread = v.map(b => Math.atan2(b.vy, b.vx));
    const arc = (Math.max(...spread) - Math.min(...spread))/D2R;
    check("across a real crown the volley fans out as the stems do",
          v.length > 2 && arc > 20, v.length + " shots across " + arc.toFixed(0) + "°");
  }
}

console.log("\n" + (failures ? failures + " FAILURES" : "all checks passed"));
process.exit(failures ? 1 : 0);
