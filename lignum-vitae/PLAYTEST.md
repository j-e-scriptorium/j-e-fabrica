# Playtesting Lignum Vitae

*How to find out whether the game is fun, and what can be found out without a
person.*

---

## 1. What is being tested

Fun is not measurable, but its failures are, and they come in a short list.
Each has a symptom that can be counted, and a place where it can be counted:

| failure | what it looks like | where it shows |
|---|---|---|
| **A choice that isn't one** | one seedling, temper-answer or policy beats everything else | headless (§2) |
| **Nothing to decide** | the glow always offers one obvious limb, or forty equal ones | headless (§2) |
| **Dead time** | the hand is off the tree, waiting for the plant | the log (§3) |
| **Friction** | the hand fights the player: set wood, missed strokes, a tree that closes up | the log, and watching (§3, §4) |
| **No arc** | the match is decided in the first minute, or never | headless and the log |
| **Illegibility** | the player loses and cannot say why | only by asking (§4) |
| **No pull** | the player does not want another | the log, and asking |

The last one is the one that matters and the only one that cannot be faked:
**did they plant again without being asked?** Everything else is a diagnosis of
why not.

The designer is the worst playtester the game has. Anyone who knows that a ward
holds exactly an unaimed shot plays a different game from someone who has to
discover it, and most of what is wrong with a game is in the discovering.

---

## 2. Headless: what play.js can settle

Headless players bend instantly and never hesitate, so nothing here says
anything about pace, feel, or legibility. What it can say is whether the
*structure* has room for a good game.

**The skill ladder** (built: `play.js policy=…`). Naive, random, glow, aim,
loop should each beat the one below by a clear step (manual §12.5). A game is
deep when there are rungs and shallow when the top rung is reached by a trick.
Re-run it after any change to shots, wards or growth; a rung collapsing is a
lost layer of the game.

**Degenerate probes** [not built]. Policies that do one stupid thing
relentlessly, written specifically to break the game: *turtle* (trim every leaf
into wards, never fire), *spray* (volley across the whole crown every time it
regrows), *stump* (keep the tree chopped to a nub and fire the trunk's girth).
If any of them beats `loop`, that is the dominant strategy a player will find
within an hour, and the game around it is ornament.

**The seedling matrix** [not built]. Every seedling against every seedling, 27
by 27, under one temper each side, three seeds a cell. What to look for is not
the best seedling but one with no bad matchup: a row that wins everywhere is an
axis option nobody should ever not pick. Intransitivity — A beats B beats C
beats A — is the good sign.

**Decision richness** [not built]. Sample the glow every few seconds through a
match and count the limbs within 10% of the best. One means the glow is playing
for you; dozens means the choice is noise. A handful, changing over time, is a
decision.

**Arc** [not built]. Temper against temper over many seeds: the length of a
match, how often the lead changes hands, and how often the side behind at half
time wins. Somewhere around a quarter to a third is the usual target for
comebacks; I recall that figure from game-design writing rather than any source
I can name, and it is a starting guess, not a law.

**Friction proxies** (partly built, in the suite). How much of the tree will
bend at all, minute by minute; how far a chopped tree recovers its reach; how
long a graft takes to set up. These are the numbers to watch when a player
says the tree is getting hard to use.

---

## 3. The playtest log

Every match keeps a record in the browser: bends and how long each took,
strokes and what each was (shot, volley, ward, or one that cut nothing),
strokes put away, grafts (suggested or by hand), tries to bend set wood, hits on
either core, wards that caught a shot, the other mage's shots, pauses, the
campaign bout and the tree's age, any knob moved in the tuning drawer, and how
it ended. Nothing is sent anywhere. The last thirty matches are kept; `l` in the
game saves them as a file, and

```
node playlog.js lignum-vitae-playlog-*.json
```

prints a line per match and a summary. What each number is for:

- **Came back for another** — a match planted within two minutes of the last
  ending. The nearest thing to a measure of fun there is.
- **Abandoned** — replanted with neither core spent. Look at when: in the first
  minute it is a bad seedling or a confusing start; late, it is boredom or a
  position the player has decided is lost.
- **Waiting** — game time with the hand off the tree for more than ten seconds
  at a stretch. Some is thinking; a lot is a tree too slow for the hand. Above a
  third of the match is worth looking at.
- **First shot** — against the tempers' 60–90 s. A player who has not cut by
  then is learning under fire, which is the open question in the manual (§11).
- **Strokes put away** — second thoughts. Some mean the preview is doing its
  job; many mean the stroke is hard to draw where it is meant.
- **Strokes that cut nothing** — a blade drawn at wood that missed it. Pure
  friction.
- **Tried to bend set wood** — reaching for something the tree no longer
  allows. In the campaign's later bouts this is the number to watch.
- **Shots aimed into their core** — as forecast at the moment the blade bit.
  Low and flat across matches means the player is not using the aim arc, or
  cannot.
- **Volleys / shots / wards, grafts** — which verbs the player found. A verb
  nobody uses is either undiscovered or not worth it, and asking (§4) tells
  which.
- **Their shots caught by a ward** — whether warding works in practice.
- **Lead changes, deepest hole climbed out of** — the arc, as played.
- **Bouts** — attempts and wins at each rung of the campaign. A rung that takes
  many attempts is a wall; one that never takes a second is a step.

---

## 4. Sessions with people

**Who.** People who have not seen the game. Five or so per round finds most of
what is confusing — Nielsen and Landauer's usability figure, recalled rather
than checked, and it is about usability, not fun — so play in rounds: a few
people, fix what they found, a few new people.

**The first session** is the valuable one and cannot be repeated with the same
person. Give them the page and nothing else. Ask them to think aloud. Do not
explain, and do not help unless they have been stuck for two minutes; when you
do, write down at what and when, because everything you had to say is something
the game failed to. Note the time of every moment of confusion, delight, or
annoyance; the log's timestamps line up with them afterwards.

**Watch for:**

- what they call things. The names a player invents for a ward or a graft say
  what the game is showing them;
- whether they find each verb unaided, and how long it takes — trim, volley,
  graft, bending a barrel straight;
- whether they ever look at the other tree. The tell is useless if nobody reads it;
- where they lean in, and where they sit back.

**After each match**, the same three questions, every time, before anything else
is said:

1. When were you most tense?
2. What did you want to do that the game would not let you?
3. Do you want another? (Ask before they see any numbers.)

And one rating, one to five: *how much did your choices decide that match?* A
game that scores low here is one the player experiences as happening to them.

**Across sessions.** Bring the same people back. What should change is how
they play — the openings they choose, what they make of their tree in the first
bout — and what should not change is whether they want another. Matches five to
ten that look like match one mean the game has no depth to grow into; matches
that converge on one approach mean there is a dominant strategy (§2 should then
find it headless).

**Comparing a change.** The tuning drawer (`t`) changes any listed knob live,
and the log records what was moved. Play three matches each way against the
same temper and seedlings, alternating, and compare. Three is not a sample; it
is enough to notice a large difference and nothing else.

---

## 5. When the designer is the only player

Most of the testing will be this, and it is worth making it as honest as it can
be:

- Play in sets of three against the same temper. Save the log after each set.
- One line per match, written immediately: the moment it turned, and the
  moment it annoyed you. Annoyance fades in minutes and is the most useful
  thing you will notice.
- Play the campaign through from a new seedling every so often, without the
  drawer open. The campaign is what a player will meet, and it is where an
  early design decision comes back to bite twenty minutes later.
- When something is annoying, ask whether it is the rule or the reading of it.
  A rule that is right but cannot be seen (§12.7 of the manual) is fixed on
  the board, not in the model.
