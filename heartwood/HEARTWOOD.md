# Heartwood

*A real-time duel fought by shaping a thing that grows on its own.*

**Manual, v0.18.** This describes the game as built. Anything not yet built is
marked **[not built]** and collected in §11. Every number quoted is the current
default and is a slider in the Constants panel.

---

## 1. What it is

Two mages face each other across a field 700 units wide. Neither casts
directly. Each has a **trunk** standing in a pot, growing and forking by rules
it obeys whether or not you are watching. Both trees run the same model on the
same clock out of the same budget; what differs is what each was planted as and
how it is played, both settled before you commit (§3, §8). Everything else
follows from three gestures acting on a plant that never stops.

Magic is not a verb you possess; it is what an arrangement of wood *does*. You
never pull a trigger — you build a thing that goes off when you cut it, and the
cut costs you the limb. The trees are line segments from a pot and look like it:
the eye stays on geometry.

---

## 2. The three verbs

| | input | time | what it costs | what it does |
|---|---|---|---|---|
| **Bend** | drag the wood | as long as you hold it | your hand | the limb keeps whatever shape it reached |
| **Slice** | drag through open air across a limb | instant, on release | the limb and everything past it | cuts — **and fires**; across several limbs, a **volley** |
| **Graft** | press a suggested pair and hold still for 0.8 s — or drag one tip onto another and hold | 0.8 s | both growing points | joins them into one node, closing a **ring** of wood and binding the two limbs together |

While your hand is on a limb you are not cutting, that limb is not growing, and
the rest of the tree grows untended in front of an opponent who can see what you
are working on. That is the whole price of a bend.

**A pull is limited; a hand is not.** One grab may take a limb `bendPer` degrees
per joint off its rest angle — ±90° across a young limb, ±20° across an old one
— and whatever it reaches, it keeps. Let go and take hold again for another
pull's worth: green wood can be walked right round by a series of tugs, set wood
will not move however often you ask.

**And wood travels; it does not teleport.** Your **grip** crosses the world at
40 units a second, walking to the pointer rather than jumping; the **wood**
turns at 16° a second, a budget for the *whole* limb, so thirty pliant joints
turn no faster than three. A small correction takes a third of a second; the
full span of a pull, three and a half.

**A slice does not bite until you let go.** While you draw the stroke, everything
it would take is painted over at its own girth — amber for a trim, red once it
is a fifth of your wood or carries a ring — and a line beside the blade says how
much of the tree that is. The flight arc of every shot it would throw is already
on the board. You commit on release: you do not hover a thing you mean to cut,
you slash at it. **And you can change your mind**: right-click (any second
button), `Esc`, or a second finger on a touch screen puts the blade away with
nothing cut.

Your own blade will not cut your own trunk. Enemy fire can, and a pot left
empty starts again from a seedling (§3); what loses is the core (§8).

---

## 3. The tree

**Planting.** What kind of tree you grow is chosen once, on three axes of three,
and carried by the tree itself. Each option is a trade, and the other mage's
seedling is on screen before you commit, so what you plant can answer it.

| | | what it gives | what it costs |
|---|---|---|---|
| **Habit** | Broom (apical control 0.5) | low, wide, every tip alike | reach, and so fan power; no leader |
| | Upright (0.55) | a rounded crown on a central trunk | — the middle |
| | Spear (0.60) | a cone round a strong leader, the longest reach | the barest core |
| **Grain** | Fine (forks every 17u) | many tips: armour, grafts, a hard core to reach | short, weak shots |
| | Even (26u) | — the middle | |
| | Open (34u) | long straight wood, fewer faster tips, reach | little to hide behind |
| **Wood** | Light (vigour 16, density 0.8) | grows and heals fast | soft wood, a core of 24 |
| | Seasoned (14, 1.0) | — the middle | |
| | Dense (12.5, 1.35) | wood that turns fire, a core of 40 | slow to grow |

**One trunk**, from a pot of radius 11, pointing at the other mage. There is no
separate opponent model: each tree is grown and measured in its own frame,
facing the other pot along +x, and theirs is mirrored only when it is drawn and
when something lands on it — so two identical seedlings under the same temper
play a mirror match that stays level to the last node.

**Growth** is one vigour budget — 14 length-units per second for seasoned wood,
16 light, 12.5 dense — so more tips means slower tips. Wounds are paid first,
out of 35% off the top, split among open stubs by girth.

**The budget is handed down the tree, not out to the tips.** What is left enters
at the pot and is divided at every fork: the axis that carries on is weighted by
**apical control** (the habit), the branch that leaves it by one minus that,
each in proportion to the growing tips it feeds — Borchert and Honda's rule
(recalled, not checked). At 0.5 the split is flat and the tree is a broom; above
it the axis outgrows its laterals and grows a **leader**, whose share flows, when
you cut it, to whatever continues the line below. Dominance compounds at every
fork, so unchecked a leader never stops pulling ahead — 474u by four minutes at
0.7. The **leader ceiling** holds any tip to three times the average.

**Forking.** The trunk runs 9 units and forks; after that each axis runs
`26 × 0.82^(generation-1)` units between forks, each opening 46° split 38/62
between the continuing axis and the new branch — so an axis zigzags and nothing
grows straight for long. Left alone, a default tree has 270 tips and 183u of
reach at four minutes, 820 tips and 209u at ten.

**Thickness** follows the pipe model: radius ∝ √(accumulated flow), so a branch
leaves its axis at about 0.63× the axis's girth and nothing outgrows the trunk.
And **wood fattens without lengthening** — the first junction sits 20u out at
90 s and still at 500 s, while the trunk under it goes from nothing to 19 thick
— so a tree you keep cut back stays exactly as small as you keep it.

**Stiffening** is flow-based, not age-based: wood rigidifies in proportion to
the growth that has passed through it (3500 units to set). A trunk locks almost
at once; an outer twig stays green however old. A side branch at three-quarters
of the reach gives ±100° in a single pull at 150 s, ±83° at 300 s, ±37° at 700 s
— and by then that give is all in the outermost twigs. The trunk has a window of
a minute or two in which it will move at all; the line you give it then is the
line it keeps.

**Healing and ramification.** A slice leaves a stub that keeps every bit of
girth it earned, and a fresh shoot climbs inside the stem to break out at the
cut face ready to branch. The stub gains a **level of ramification**: cut the
same spot five times and its fork interval goes from 26u to 9.6u. Chop, let it
run, chop again — the trunk fattens while the tree stays small. Where scarred
wood puts out no shoot the fattest stub **coppices** instead, and an empty pot
starts again from a seedling.

**The husk.** A seedling's core sits inside a seed coat of radius 19, and a shot
that reaches it is spent on it whole. The coat cannot be broken from outside: it
splits when the trunk inside it reaches a girth of 10, at 105 s on light wood,
120 on seasoned, 134 on dense. Until then neither mage can be killed, and the
opening is all shape, position and wood.

**Style.** The habit decides what tree you have to work with; the hand decides
which it becomes, and the bonsai styles fall out of the gestures rather than
being coded. A green trunk pulled over is a slant, whose every shot starts
turned; pulled one way and back, an informal upright; cut low and early, a twin
trunk with two lines of fire; walked right round, a cascade pointing away and
lying low; trunk and tiers pulled together, a windswept crown whose shots arrive
from the side; the kinks pulled out of a leader, a formal upright, which is also
how you make a barrel (§4).

---

## 4. Figures

Three primitives, measured continuously: no grid, no completion event, no
arming step. Every **tip** counts — a live bud, a bare stub, a fused junction
alike — so the question is never whether you have a figure but how much better
than the plant's own habit yours is.

### Fan — magnitude

Take the tips whose bearings fall inside a wedge. Its strength is

> **P = 10 × √(mean radius ÷ pot radius) × convergence**

where **convergence** is how much narrower those tips sit than they would if
nobody had bent them. A cluster the plant grew itself reads 1.00 however tight
it looks. The cap at 4× is where limbs foul each other; without it a fan
squeezed onto one bearing fires a needle nothing can stop. Reach enters under a
square root, because linear it made the tallest tree the strongest whatever else
it did badly. Gathering by hand takes power from 40 to 154 but *costs reach*, so
the optimum is interior.

### Spire — velocity

A run of near-collinear wood, and **local**: what counts is the straightness of
the stem you sever, not the best run on the tree. No tree comes with one — every
fork turns the axis further than the tolerance, so the plant's own best is about
27u, firing at 52 u/s. You make a barrel by bending forks back into line, and
since a pull repeats, any chain that still gives can be walked straight: about
140u on a four-minute tree, firing at 150.

### Graft — gain

Two tips joined into one node. What it makes is a **ring** of wood — out along
one limb from where the two part, across the junction, back down the other — and
a ring rings: charge let loose by a cut goes round every ring the grafts have
closed, compounding on each lap, and comes out of the cut face heavier than it
went in. Gain is

> **×1.025 per core-area enclosed, to a ceiling of ×2**

which compounds on *area*, so one wide ring beats several tight ones. Two
sibling twigs enclose a lens worth a percent; a tip reached across to another
limb encloses twenty core-areas and is worth ×1.8 on every shot from then on —
the only thing on the tree worth more than the wood it is made of, and so the
thing to build and the thing to shoot at (§12.5).

**Making one.** With **Grafts** on, the board draws a dashed line between each
of the ten best pairs of tips within reach, a lit bead at its middle. Point at
one and the ring it would close is shaded in, with the gain as it stands and as
it would be: `graft ×1.00 → ×1.78`. Press and hold still for 0.8 s and the two
tips become one node, neither growing while you hold. Pairs the board does not
suggest are made by hand: take a shoot, bring its tip to another, hold your hand
there for the same 0.8 s. Both the tips and *your hand* must be within 20 units
of the partner (§12.14).

**A graft binds.** The two limbs are one piece of wood from then on: take hold
of either and the junction moves, and the other comes with it at the pace a hand
bends wood, keeping what it reaches. It is a linkage as well as a multiplier: a
stiff limb grafted to a green one is a lever for walking the green one round.
Whatever the far limb cannot follow is **strain** — the gap
between where its own wood would put its tip and where the junction is, against
the size of the ring — and past a fifth of that it tears, with a red ring
warning from nearly half way. Sap feeds both sides, so a closed ring thickens
and sets faster than open wood.

**Losing one.** Sever any internode in the ring and the junction lets go and the
gain is gone — which is what enemy fire is for. Your own blade cuts that wood as
readily as any other, but the glow never recommends it and the stroke preview
turns red when it would.

---

## 5. Firing

**A cut fires.** The charge sits in green wood; severing a limb releases what it
held, and the shot leaves **the face you cut, along the line that stem was
pointing**.

- **Where and which way** — the stem you cut. Bending is aiming.
- **How fast** — the straight run behind the cut: 28 u/s out of a kink, plus 0.9
  per unit of run.
- **How hard** — mass and speed, nothing else:
  `0.03 × channelled charge × muzzle speed × graft gain`. A full early channel
  off a kinked stem carries about 9, off a straightened barrel three times that.
- **How wide** — the fan nearest the cut, and only that: `55 × (fan span + 5°)`,
  so gathering does not make a shot bigger, it makes it *sharper*. Gathered to
  ten degrees the front is 14 units and bores; with no fan it leaves 120 units
  wide and shears.

**Capacity** is what one cut can channel, and it is girth and nothing else:
`10 × (girth ÷ 14)^1.6`. Charge past that is thrown away with the limb — a
mid-limb cut on a four-minute tree releases about 120 where a young trunk
channels 10. **Girth is how much a cut can channel, grafts are what the
channelled charge is worth**, and the two are kept apart deliberately.

**Firing costs you the limb.** Your magazine and your structure are the same
wood, so a barrel has to be spare: cut one carrying part of your figure and you
fire once, then have no figure.

### Volleys

A stroke across several limbs throws **one shot out of every face it opens**,
each along its own stem, at its own barrel's speed, gathered by the fan nearest
it; siblings leave by the same face and count once, and past eight faces the
rest are cut and their charge goes with the wood. The faces share one trunk and
so one channel, but a channel opened in several places passes more than one
opened in one:

> **channel × (faces)^0.5**, where *faces* is how evenly the charge is spread
> across them — (Σh)²/Σh², the participation ratio

so four equal limbs pass twice what one cut can, while one heavy limb and three
twigs nicked on the way pass barely more than the limb alone. What each face
held is scaled down together to fit, so no one shot in a volley is ever heavier
than a single cut would be.

What it buys is spread. A volley puts more mass in the air than any single cut,
across as many lines as the stems were pointing, each shot lighter and so easier
for wood to stop. It shears a canopy, cuts rings, and finds a bare core by
numbers; it does not bore. Measured headless against a tree nobody tends, at
160, 240, 300 and 420 seconds, a stroke across the four best separate limbs did
more core damage than the best single cut every time — by a fifth to two-thirds where the
single shot landed, and outright where it missed — at three to four times the
charge spent, so about 40% as much damage per unit of wood. Four trials, not
enough to rank. Aimed cuts are the economy; a volley is tempo, bought with the
tree. At `volleyExp` 0 a volley is
never worth throwing.

---

## 6. Ballistics

A bolt leaves the cut face and is then on its own. What pulls it is **the other
tree's weight**, not its core: the mass sits at the centre of mass of their
wood, 85 units out from their pot on a four-minute tree, walking outward as the
crown fills and back as you cut it away. Their canopy is therefore both shield
and attractor: a shot falls into the wood unless it is aimed past it. Softened
inverse-square, velocity Verlet so orbits close.

Escape speed at the pot is 86 u/s. A kinked stem gives 28 and the plant's best
unaided 52, so everything the tree hands you is captured and swings round;
crossing instead of orbiting needs about 65 units of run you straightened
yourself. Sampled across every launch bearing from nine real muzzles, **every
direction lands somewhere and a third pass through the heartwood.**

**A shot runs down against distance rather than time.** It loses half its force
every 2600 units flown: full strength on the approach, still dangerous coming
round the back, spent after five or six laps — 6.5 laps and 14,700 units for a
bolt launched at half escape speed. In units of flight rather than time, it
scales with the separation by itself (§12.6).

**Impact.** A bolt carries a front, not a point, and what has to beat a piece of
wood's thickness is **pressure** — force over that front. Where pressure wins
the segment is severed and the bolt loses force equal to its thickness, **and
the loss comes off its speed**, so a shot that bores through a limb comes out
slower and falls in tighter. Where pressure loses, that part of the front stops
and the rest goes on narrower and therefore harder. Thick wood is armour,
concentrated on the trunk, which faces you: at force 20 the tightest front a fan
can read takes 52 nodes and the widest 20.

---

## 7. Age

**A trunk never stops thickening, and girth is the whole of an old mage's
power.** A wider trunk channels a heavier shot, and only that: age buys weight,
never haste. Wood is laid down around the whole core, so a trunk raises a
**collar** of its own timber round the pot and carries its age in its colour
(§9), which makes an opponent's age legible from across the field for nothing.

A tree chopped back to 45 units every 40 seconds, across its life:

| | trunk | reach | squat | channels |
|---|---|---|---|---|
| 400 s | 16 | 44 | 37% | 13 |
| 800 s | 23 | 44 | 52% | 22 |
| 1200 s | 28 | 44 | 63% | 30 |
| 1600 s | 32 | 44 | **72%** | **37** |

Seventy-two percent as thick as it is long, channelling four times what a young
figure can, in a body a quarter the size of a sprawler with the same girth — and
the reach column does not move, because nothing lengthens. Pruning does not make
the trunk fatten faster; it keeps the tree *short* while the girth accrues, and
a squat tree is hard to hit and cheap to reload.

The tree is just state, so it carries between matches for nothing. **[not
built]** A campaign that keeps your tree across opponents.

---

## 8. Winning

Enemy core integrity to zero — once its husk has split (§3). It absorbs 60
force, scaled by the density of the wood they planted: 48 for light, 60 for
seasoned, 81 for dense. A good shot off a young tree carries 9 to 18 and loses
some of that boring in, so a seasoned core takes something like six clean hits,
fewer as your trunk thickens and the channel widens, fewer again with grafts.

**But their wood grows back, and that is the clock.** A shot spends most of its
force boring through their canopy, which they are replacing the whole time. Four
shots take 220 nodes off a four-minute tree; two hundred seconds later it is
larger than before, because a chopped stub ramifies and comes back denser. So
there is no accumulating siege: either your cadence beats their growth and you
reach the core in a handful of shots, or you are pruning them for free while
spending your own limbs on it — which is the pressure behind aiming properly and
behind grafts.

When your core is spent your tree stops, your hand stops, and `r` plants again.

### The other mage

Across the field is a mage with the same hand you have and no other. It grows by
your rules, reads its own tree the way the glow reads yours, and fires by
cutting a limb off; it is told nothing you are not. How it plays is chosen on
the planting screen:

| | first shot | between shots | aims | wind-up |
|---|---|---|---|---|
| **Still** | never | — | — | — |
| **Feral** | 90 s | 16 s | not at all: cuts whatever glows brightest and lets fly | 3.0 s |
| **Keeper** | 75 s | 20 s | walks the stem across for up to 2.5 s, one reversal | 2.5 s |
| **Master** | 60 s | 14 s | up to 6 s and two reversals, or until the arc runs into your heartwood | 1.6 s |

**Its hand is your hand**: the same two speeds, through the same function, down
to paying for changing its mind with the walk back.

**How it chooses.** It takes whatever its own glow says is brightest, but never
a limb carrying more than a third of its green wood and only once that limb
holds a fair part of what its trunk can channel (30% Feral, 45% Keeper, 60%
Master). It picks that limb **early**, a whole aim and wind-up before firing.
Then it aims as a hand aims: hold the stem, walk the grip sideways while the
predicted pass keeps closing, and when it stops come back to the best line and
try the other way. It keeps no joint more than 5° from where it grew, works only
the dozen joints behind the cut, and will not fire over its own shoulder
(§12.10, §12.15).

**Every shot is telegraphed**, for the five to eight seconds between choosing
and firing: the limb lit white, the stem it is working drawn, the arc it would
fly dashed in pink with a ring where it would first meet your wood or core, and
a ring closing round the cut face for the wind-up. Take the loaded limb, or the
stem behind it, and the shot never comes.

**Or hand it your own side.** The planting screen has a row for this side too:
leave it on **Yours** and you play, or give it to a temper and watch the two of
them fight. Both hands read the board before either cuts, so the match is not
decided by who moves first, and while a temper holds your tree the board ignores
your hand entirely.

**How hard each is,** over three seeds of four minutes' fire against a tree
nobody tends: Master lands 151 force into a core that holds 60, Keeper 133,
Feral 52. **Those numbers do not rank reliably** — change a cadence by three
seconds and the measurement swings fivefold either way. What measures cleanly is
what a temper controls: Feral never touches a stem before firing, a Keeper's aim
brings its predicted pass from 41 units of the core to 36 and a Master's from 93
to 77, and Master fires half again as often as Keeper.

**Aiming past a couple of seconds measured worse, every time**: eight seconds of
aim did a quarter of the damage of two and a half, across every configuration
and fix I tried, and I do not know why. Every temper also loses to both headless
players, who bend instantly while everything else now takes seconds. Against a
human, Keeper is meant to be the fair fight and Master the hard one — a guess
about human pace that nothing headless can settle.

**[not built]** A wither timer, so two mages who never commit do not sit there
for ever. With Still across the field that is every match.

---

## 9. What you see

A match opens on the **planting** screen: the three axes, a row for how the
other mage plays, a row for whether this side is yours or a temper's, and
previews of what each seedling grows into if left alone. Nothing grows until you
plant; **New seedling** or `r` brings the screen back mid-match.

Then the board, and one row of buttons: **Pause · 1× · New seedling ‖ Charge
Aim Fan Spire Grafts ‖ Readout**. Charge, Aim and Grafts are on by default —
between them, how a stroke is aimed and how a graft is found; everything with a
number on it starts hidden. Keys: `space` pause, `r` new seedling, `Esc` put
away a stroke, `c a f s g` the overlays, `h` the readout, `t` a drawer of tuning knobs with hand speed and
wood speed among them.

**The board does not move.** The view is set by the field and the window and
never by how big either tree has grown, so nothing slides under the hand taking
hold of a twig. The frame shows ±289 units of sky against a tree that plateaus
at about 250; one that outgrew it would clip rather than pull the camera back.

Wood reads two ways at once: across, how set it is, sap to dry grey; along, how
much girth it has put on, drab through a burning prime down to near black.
**Yours runs green→amber→mahogany, theirs pink→purple→violet.** Live buds carry
leaf glyphs sized by their vigour share; stopped tips are pale dots; scarred
joints are dark knots; a healing shoot is a bright bead climbing the stem it
repairs; a husked core wears a pale ring at 19 units that falls away in pieces
when the trunk splits it.

**The charge glow** is the sap alight in the wood, not instrumentation. Every
limb is scored by the shot a cut there would throw and reads three ways at once:
**brightness** is the size of that shot after the
waste penalty and after asking whether it would land, so the brightest band is
the smallest wood that fills your channel; **colour** is where it ends up, pale
gold into their heartwood, green into their canopy, dim blue for one that sails
past; **halo width** is the front it would carry (§11). Wood carrying a ring is
excluded entirely, as the trunk is.

The other overlays: **Aim** draws the barrel and the flight arc for the limb the
stroke would take, or for the limb under the cursor, so you can hover a stem,
bend it and watch the shot move. **Fan** draws the best wedge with a dashed arc
showing where those tips would sit unbent, **Spire** the longest straight run,
**Grafts** the rings already closed and dashed lines to the best pairs one
gesture away — filtered twice, within reach *and* closing a ring worth
something, or a crowded rim offers hundreds of worthless lenses.

A stroke paints everything it would take at its own girth, in amber, and the
limbs it severs brighter; past a fifth of your wood, or across a ring, the patch
and the blade go red and the line beside the blade says so. The readout says
BREAKS A GRAFT in the same breath, and for a volley gives the shots, their force
in all and how hard the hardest presses. Bolts dim as they spend themselves, and
**a shot flies in the colour of the buds that threw it**, as do the rings where
it lands, so a crowded field stays legible. A temper's tell is drawn whatever
the overlays say — on their tree, and on yours when a temper is playing your
side (§8).

---

## 10. How the shot is scored, exactly

Almost every design question ends up here. For every limb, in two sweeps over
the node list:

```
sub   = green wood in the subtree below this limb
held  = sub × 0.06                                    the mass a cut would let go
cap   = 10 × (girth/14)^1.6                           girth, and nothing else
gain  = min(2, 1.025^(total ring area / core area))   the grafts, compounded
speed = 28 + 0.9 × straight run behind the cut
force = 0.03 × min(held, cap) × speed × gain          mass × speed
front = 55 × (fan span + 5°), or 120 with no fan
peri  = closest the shot passes their core, over its first lap round their
        centre of mass                                (flown coarsely, see below)
reach = 1 at the core, 0.55→0.23 through their canopy, 0 past it; and at most
        0.3 into a husk that still holds
eff   = force × min(1, cap/held) × reach              ← what the glow shows
```

The trunk and any wood carrying a ring are skipped outright — `eff` zero — so
the glow never offers a cut that costs you the tree or the gain.

A volley is scored face by face, heaviest first, at most `volleyMax` of them:

```
h_i    = held at face i
spread = (Σh)² / Σh²                                  how many faces, evenly counted
k      = min(1, cap × spread^volleyExp / Σh)
mass_i = min(cap, h_i × k)                            then force as above, per face
```

The glow scores single cuts only; what a volley would do is on the board as a
dashed arc per face while the stroke is drawn.

`peri` is flown, not solved (§12.11): long steps where the pull is weak, short
ones deep in the well, one revolution and stop. That agrees with a fine
integration to within 6 units at about 10 µs a limb, and stays affordable at
eight readings a second on a 1,600-node tree because siblings share a muzzle and
a muzzle that has not moved keeps its answer — 0.5 ms warm against 13 cold.

---

## 11. Not built, and open questions

**The ward.** A fan pointed away from the enemy should emit a repulsion field
across its own arc, widening the turn radius of incoming bolts: same primitive,
different bearing. Two things wait on it. **A wide fan has no job** — at equal
force a spike takes 52 nodes where the widest front takes 20, and gathering is
unambiguously good. And **flanking is beautiful and pointless** — a captured
bolt arrives from behind, where nothing is softer. Both pay only once something
faces the wrong way, which is also why the glow's halo-width channel carries no
information.

**Nobody volleys but you.** The tempers cut one limb at a time. A temper that
answers a thin crown with a volley, and one that strips a canopy before a heavy
shot, are both obvious and both unbuilt; until they exist, whether `volleyExp`
0.5 is generous is a guess.

**Nobody aims at a graft.** The other mage aims at your core and nothing else,
so a ring breaks only when a shot bound for the heartwood crosses it on the way.
A temper that takes grafts apart is the obvious next one; until it exists, graft
play is a solitaire optimisation and its ×2 ceiling is a guess.

**Gathering, for the other mage, was a net loss.** Once a hand cost real time,
hauling a wedge together was a minute of work for a narrower front, measured at
about half the damage of not bothering — so the tempers no longer do it, though
it remains the player's tool. That may say more about the fan being worth less
since force became mass times speed.

**What the husk pushed rather than solved.** A seedling can no longer be killed,
but the first minute after the husk splits is now the sharpest moment in the
match, with the crown thin and the core newly bare. Whether that is a turn or a
cliff is a question for a player; the knobs are the splitting girth and the
radius.

**Captured shots grind.** With the pull at the centre of mass and the well
softened, an orbit precesses, so a shot that misses on its first lap comes round
at a different angle on its second and the glow reads only the first. Over five
or six laps a spent bolt can find a way in that nothing predicted. Unmeasured;
if it matters, the lever is the force half-life.

**Buds.** Every node should lay down a dormant bud that breaks when enough
budget reaches it, instead of a fork arriving on a clock. Branch density would
follow vigour, a cut would send what used to pass it into the buds below —
back-budding — and the remaining styles would follow: multi-trunk, raft, and a
broom cut out of an upright.

**The broom has no job of its own.** It is viable — five kills in six where an
upright takes all six — but a weaker upright rather than a different tree: its
wood sits in front of its core and captured shots arrive from behind, so the
armour it pays for in reach never meets anything.

**Pliancy is not a trade yet.** A species that stays bendable was the obvious
third axis and lost everywhere, because the solver spreads every pull down the
chain to the pot. Supple wood pays only once a bend stays near the hand.

**Concealment.** Fog-of-war for *state* rather than shape: they see your
silhouette but not what is set, dormant or held, unless they spend an action to
read you. Best idea in the drawer and the one most likely to make the game
unteachable. **Campaign:** keep your tree between opponents (§7).

**Open questions I could not settle headlessly:**

- *Cadence, and what a bend now costs.* How many shots an hour a person can set
  up, and whether the tempers' 14–20 s is generous or cruel beside it, cannot be
  answered headlessly, because the headless players bend instantly.
- *Late-game rigidity.* By 700 s nothing but the outermost twigs will bend. The
  model's own answer is to chop back and let a green shoot regrow into a new
  barrel — correct bonsai, and a good reason for ramification — but I have not
  checked whether that cycle is fast enough in play.
- *How much a graft should be worth.* The first pair the board suggests on a
  two-minute tree is often already worth the whole ×2 ceiling: either the
  ceiling is too easy to reach or the suggestions are too generous.
- *Touch.* Precision dragging is fiddly everywhere and lethal on touch. A
  suggested graft is a press on a bead and needs no hover; the unsuggested kind
  still asks for a 20-unit target, and none of it has been tested on a phone.

---

## 12. Design rules that have earned their keep

Each was arrived at by something breaking, and will look arbitrary to anyone who
did not watch it break.

1. **Growth is deterministic.** Same seed, identical geometry; variance comes
   from the opponent. If matches feel samey, randomise the *seedling*, never the
   forking.
2. **Every prune is a reallocation, never a brake.** One budget, redistributed.
   Cut the leader and the laterals surge.
3. **Convergence, not tightness.** Score a fan by how much narrower it sits than
   it would unbent; raw tightness rewards the plant's own habit, to which the
   player contributes about 5%.
4. **The waste penalty is what makes the glow a contour.** Without it every
   inner limb holds more than you can channel, they all tie at maximum, and half
   the tree floodlights.
5. **Aim is the dominant term, and a graft is the term above it.** Over
   twenty-four turns against a tree that only grows, as the state their core is
   left in: cut at random, 99%; cut and bend at random, 92%; follow the glow,
   53%; gather a fan and aim each cut, 9%; weave grafts as well, **dead in ten
   shots**. The gap between the third rung and the fourth is the game.
6. **Nothing that reads as a countdown** — but a rule in the same units as
   everything else is not one. Timed back-budding and hard flight limits were
   clocks; force decay came back as a half-life in units flown.
7. **A gesture you cannot see the result of is not a gesture.** Grafting had no
   way to find a pair or show one in reach; pointing the pairs out was not
   enough while making one still meant finding a tip among the leaves. The
   suggestion has to be the handle.
8. **A kept tree has to stay kept.** Wood used to lengthen as it thickened,
   which made the trunk a free barrel and crept every junction outward all
   match. Any growth rule that moves wood the player has placed is suspect.
9. **Both mages stand in their own frame.** Grown facing +x from its own pot and
   mirrored only when drawn or hit, the other tree uses every rule unchanged;
   rotated half a turn, as it once was, every rule needs a second copy the moment
   it fires.
10. **A bot needs taste as well as rules.** The first aiming hand was legal and
   hideous, coiling a sapling to shave units off a pass and firing backwards over
   its own shoulder. Two limits a human would never think to state — no joint
   more than 5° from where it grew, nothing fired more than 60° off the line —
   made it look like someone keeping a tree, and it aimed better for them.
11. **When the model stops being Keplerian, the readout has to stop being
   closed-form.** Moving the pull to the centre of mass left the closed form
   quietly wrong — an eighty-unit miss reported on shots that went through the
   core — because the softened well bends exactly the close passes the glow
   exists to identify. The first lap is flown instead.
12. **A mechanic that only changes a number is not a mechanic.** A graft
   multiplied every shot and lit up blue while the tree moved as though nothing
   had been joined. If a thing the player builds does not change what the hand
   can do, it is a scoreboard.
13. **A limit the machine does not obey is not a limit — and the limit you are
   tuning may not be the binding one.** The other mage bent in single frames
   until every path went through the same function your hand does, and what
   could not (gathering a wedge in one pass) was cut rather than exempted. The
   player's own rate was no better: a cap per joint is no cap on a limb with
   thirty, and capping the limb still left the grip snapping to the pointer.
14. **The gesture that fires by accident is the one to fix first.** Holding a
   tip near another grafted them, so bending a limb and pausing fused it to
   whatever was beside it, and it looked like bending had stopped working.
   Requiring the *hand* to be at the partner separates the two gestures.
15. **A search that keeps where it stopped is worse than one that goes back.**
   The aim walk kept whatever pose it ended on, so more aiming made it shoot
   worse; and the 5° taste rule, applied on letting go, undid six seconds of
   aim. Constraints belong inside the search.
16. **Sum what you will ask about a thousand times.** Testing every pair of tips
   for the ring it would close walked both limbs down to where they part. The
   shoelace summed from the pot outward makes it two lookups and a subtraction,
   because the shared wood cancels: 56 ms a reading to 8.
