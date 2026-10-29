// Temper against temper, headless. Each pairing is played from both sides on
// a seedling both mages share, over several seeds, so the only difference
// between the two trees is the hand on them. Prints who won, how long it
// took, and what each landed.
//
//   node ladder.js                              keeper, adept, master, 6 seeds
//   node ladder.js minds=feral,keeper seeds=4 secs=900 seedling=spear,open
//   node ladder.js seedling=random master.aimFor=4     one seedling per seed; a temper retuned
//   node ladder.js pair=keeper,adept seed=3 side=0     one match, as JSON (used for running in parallel)
const path = require("path");
const load = require(path.join(__dirname, "harness.js"));

const opt = {};
for (const a of process.argv.slice(2)){ const [k, v] = a.split("="); opt[k] = v === undefined ? true : v; }
const SECS = +(opt.secs || 900);

function picks(str){
  const g = load(), out = {};
  for (const w of String(str || "").split(",").filter(Boolean))
    for (const ax of g.AXES) if (w in g.TRAITS[ax].options) out[ax] = w;
  return out;
}

// one match: `mine` plays the tree at the origin, `theirs` the one across the field
function duel(mine, theirs, sd, seedling){
  const g = load();
  // a temper retuned for the run: master.aimFor=4 and the like
  for (const k in opt) if (k.includes(".")){ const [m, f] = k.split("."); if (g.MINDS[m]) g.MINDS[m][f] = +opt[k]; }
  for (const k in opt) if (k in g.S) g.S[k] = +opt[k];
  const gen = () => g.genome(seedling);
  g.T = g.newTree(0, gen()); g.layout(g.T); g.buildGrid(g.T);
  g.T.hpMax = g.T.hp = g.coreOf(g.T.g);
  g.newFoe(gen(), theirs, sd);
  g.T.mind = g.newMind(mine, sd + 1000);
  const dt = 0.05, dealt = [0, 0], shots = [0, 0];
  let t = 0;
  for (; t < SECS; t += dt){
    const T = g.T, TD = g.TD;
    g.step(T, dt, null); g.step(TD, dt, null);
    g.layout(T); g.buildGrid(T); g.layout(TD); g.buildGrid(TD);
    const atT = g.targetOf(T), atTD = g.targetOf(TD);     // both read before either cuts
    const a = g.mindStep(T, T.mind, dt, atTD); if (a){ g.launch(a, false); shots[0]++; }
    const b = g.mindStep(TD, TD.mind, dt, atT); if (b){ g.launch(b, true); shots[1]++; }
    g.layout(T); g.buildGrid(T); g.layout(TD); g.buildGrid(TD);
    g.stepWards(T, dt); g.stepWards(TD, dt);
    const h0 = T.hp, h1 = TD.hp;
    for (let k = 0; k < 3; k++) g.stepBolts(dt/3);
    dealt[1] += h0 - T.hp; dealt[0] += h1 - TD.hp;
    if (T.hp <= 0 || TD.hp <= 0) break;
  }
  const left = [g.T.hp/g.T.hpMax, g.TD.hp/g.TD.hpMax];
  const winner = left[0] <= 0 ? 1 : left[1] <= 0 ? 0 : left[0] > left[1] ? 0 : left[1] > left[0] ? 1 : -1;
  const ms = [g.T.mind, g.TD.mind].map(M => {
    const st = M.stat || { shots: 0, run: 0, gain: 0 };
    return { grafts: M.grafted, wards: M.warded, run: st.shots ? st.run/st.shots : 0, gain: st.shots ? st.gain/st.shots : 1 };
  });
  return { t: Math.round(t), winner, killed: left[0] <= 0 || left[1] <= 0, left, dealt, shots, ms };
}

if (opt.pair){
  const [a, b] = opt.pair.split(","), sd = +opt.seed, side = +(opt.side || 0);
  // seedling=random draws one per seed, the same for both sides
  let seedling = picks(opt.seedling || "");
  if (opt.seedling === "random"){
    const g = load(), r = (k) => (Math.imul(sd*7919 + k*104729, 2654435761) >>> 0) % 3;
    seedling = {};
    g.AXES.forEach((ax, k) => { seedling[ax] = Object.keys(g.TRAITS[ax].options)[r(k + 1)]; });
  }
  const r = side ? duel(b, a, sd, seedling) : duel(a, b, sd, seedling);
  // report from the first-named temper's point of view
  const me = side ? 1 : 0, it = 1 - me;
  console.log(JSON.stringify({ a, b, seed: sd, side, t: r.t, killed: r.killed,
    win: r.winner === -1 ? 0.5 : r.winner === me ? 1 : 0,
    left: [r.left[me], r.left[it]], dealt: [r.dealt[me], r.dealt[it]], shots: [r.shots[me], r.shots[it]],
    ms: [r.ms[me], r.ms[it]] }));
  process.exit(0);
}

// the round-robin, spread across the machine's cores
const { execFile } = require("child_process");
const os = require("os");
const minds = (opt.minds || "keeper,adept,master").split(",");
const seeds = +(opt.seeds || 6);
const jobs = [];
for (let i = 0; i < minds.length; i++) for (let j = i + 1; j < minds.length; j++)
  for (let s = 1; s <= seeds; s++) for (const side of [0, 1])
    jobs.push(["pair=" + minds[i] + "," + minds[j], "seed=" + s, "side=" + side, "secs=" + SECS]
              .concat(opt.seedling ? ["seedling=" + opt.seedling] : [])
              .concat(Object.keys(opt).filter(k => k.includes(".") || k in load().S).map(k => k + "=" + opt[k])));
const out = [];
let next = 0, running = 0;
function launch(){
  while (running < os.cpus().length && next < jobs.length){
    const args = jobs[next++]; running++;
    execFile(process.execPath, [__filename].concat(args), { maxBuffer: 1 << 20 }, (err, so) => {
      running--;
      if (err) console.error(args.join(" "), err.message); else out.push(JSON.parse(so));
      process.stderr.write("\r" + out.length + "/" + jobs.length + " matches");
      if (out.length + (jobs.length - next - running) >= jobs.length && !running && next >= jobs.length) report();
      else launch();
    });
  }
}
function report(){
  process.stderr.write("\n");
  const f1 = x => x.toFixed(1);
  const tuned = Object.keys(opt).filter(k => k.includes(".") || k in load().S).map(k => k + "=" + opt[k]).join(" ");
  console.log("\n" + SECS + " s limit, " + seeds + " seeds, both sides, " + (opt.seedling || "default seedling") +
              (tuned ? ", " + tuned : "") + "\n");
  console.log("  pairing              wins (of " + 2*seeds + ")   kills   mean length   core left (a / b)   force landed (a / b)   shots (a / b)");
  for (let i = 0; i < minds.length; i++) for (let j = i + 1; j < minds.length; j++){
    const rs = out.filter(r => r.a === minds[i] && r.b === minds[j]);
    const w = rs.reduce((s, r) => s + r.win, 0), n = rs.length;
    const mean = k => rs.reduce((s, r) => s + k(r), 0)/n;
    console.log("  " + (minds[i] + " v " + minds[j]).padEnd(20) +
      (f1(w) + " – " + f1(n - w)).padStart(13) + String(rs.filter(r => r.killed).length).padStart(8) +
      (mean(r => r.t).toFixed(0) + " s").padStart(14) +
      (Math.round(100*mean(r => r.left[0])) + "% / " + Math.round(100*mean(r => r.left[1])) + "%").padStart(20) +
      (f1(mean(r => r.dealt[0])) + " / " + f1(mean(r => r.dealt[1]))).padStart(23) +
      (f1(mean(r => r.shots[0])) + " / " + f1(mean(r => r.shots[1]))).padStart(16));
  }
  // what each temper's hand actually did, across all its matches
  console.log("\n  temper    grafts a match   wards a match   barrel behind a shot   gain on a shot");
  for (const m of minds){
    const seen = [];
    for (const r of out){ if (r.a === m) seen.push(r.ms[0]); if (r.b === m) seen.push(r.ms[1]); }
    if (!seen.length) continue;
    const avg = k => seen.reduce((s, x) => s + x[k], 0)/seen.length;
    console.log("  " + m.padEnd(8) + f1(avg("grafts")).padStart(15) + f1(avg("wards")).padStart(16) +
                (f1(avg("run")) + " u").padStart(23) + ("\u00d7" + avg("gain").toFixed(2)).padStart(17));
  }
  console.log("");
}
launch();
