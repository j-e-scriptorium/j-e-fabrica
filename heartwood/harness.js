// Loads the real game — model, renderer logic and all — with a null canvas,
// so a headless run exercises exactly the code the browser runs.
const fs = require("fs");
const path = require("path");
module.exports = function load(file){
  const html = fs.readFileSync(file || path.join(__dirname, "index.html"), "utf8");
  const SIM  = html.split("/*BEGIN SIM*/")[1].split("/*END SIM*/")[0];
  const VIEW = html.split("/*BEGIN VIEW*/")[1].split("/*END VIEW*/")[0];
  const pre = `
var CANVAS={width:1400,height:900};
var GRAD={addColorStop:function(){}};
var CTX=new Proxy({},{get:function(t,k){
  if(k==="createRadialGradient"||k==="createLinearGradient") return function(){return GRAD;};
  if(k==="measureText") return function(){return {width:10};};
  return function(){}; },set:function(){return true;}});
function Path2D(){ this.moveTo=this.lineTo=this.arc=this.closePath=function(){}; }
var DOM=new Proxy(function(){},{get:function(t,k){
  return (k==="className"||k==="textContent"||k==="innerHTML")?"":DOM; },
  set:function(){return true;},apply:function(){return DOM;}});
var document={getElementById:function(){return DOM;},createElement:function(){return DOM;}};
var window={devicePixelRatio:1}; var innerWidth=1400, innerHeight=900;
var performance={now:function(){return Date.now();}};
function requestAnimationFrame(){} function addEventListener(){}
`;
  // The interface lives between the two blocks and is not loaded, so what the
  // renderer reaches for out of it — the canvas, the view, the hand, and the
  // graft hints — is stubbed here.
  const glue = `
var cv = CANVAS, ctx = CTX;
function DPR(){ return 1; }
function fit(){}
var T = newTree(0);
var view = {scale:1, cx:0, cy:0, fx:0, fy:0};
var flash = [], hits = [], bolts = [], hitBuf = [];
var drag = null, slice = null, hover = null, hoverPair = null, fuse = null;
function pairLive(){ return false; }
var SHOW = { charge:true, fan:true, spire:true, loops:true, aim:true };
var PAIRS = [];
function graftablePairs(){ return PAIRS; }
function fkChain(){ return []; }
function cross(ax,ay,bx,by,cx2,cy2,dx2,dy2){
  function o(px,py,qx,qy,rx,ry){ return (qy-py)*(rx-qx)-(qx-px)*(ry-qy); }
  var d1=o(ax,ay,bx,by,cx2,cy2), d2=o(ax,ay,bx,by,dx2,dy2),
      d3=o(cx2,cy2,dx2,dy2,ax,ay), d4=o(cx2,cy2,dx2,dy2,bx,by);
  return ((d1>0)!==(d2>0)) && ((d3>0)!==(d4>0));
}
`;
  const tail = `
return { S:S, get T(){return T;}, set T(v){T=v;}, get TD(){return TD;},
  newTree:newTree, step:step, layout:layout, cutNode:cutNode, makeGraft:makeGraft,
  stiffOf:stiffOf, bendGroup:bendGroup, bendLimit:bendLimit, greenOf:greenOf,
  bestFan:bestFan, bestSpire:bestSpire, valueCuts:valueCuts, capacity:capacity,
  loopAmp:loopAmp, figureNodes:figureNodes, forkLen:forkLen, markLoops:markLoops,
  muzzleFor:muzzleFor, makeBolt:makeBolt, stepBolt:stepBolt, frontOf:frontOf,
  pressure:pressure, periapsis:periapsis, connects:connects, girthOf:girthOf,
  buildGrid:buildGrid, gridNear:gridNear, loopPoly:loopPoly,
  FIG:FIG, bolts:bolts, hits:hits, measure:measure, newFoe:newFoe,
  fireFromCut:fireFromCut, stepBolts:stepBolts, volleyFrom:volleyFrom,
  loopArea:loopArea, fanNear:fanNear, forecast:forecast,
  TRAITS:TRAITS, AXES:AXES, genome:genome, resist:resist, coreOf:coreOf, below:below,
  circuitArea:circuitArea, fanAt:fanAt, figuresOf:figuresOf, shotFrom:shotFrom,
  MINDS:MINDS, MIND_ORDER:MIND_ORDER, newMind:newMind, mindStep:mindStep,
  launch:launch, forecastInto:forecastInto, targetOf:targetOf, shotForce:shotForce,
  muzzleSpeed:muzzleSpeed, biteBolt:biteBolt, PASS:PASS, bindGrafts:bindGrafts,
  graftSides:graftSides, chainTip:chainTip };
`;
  return new Function(pre + SIM + glue + VIEW + tail)();
};
