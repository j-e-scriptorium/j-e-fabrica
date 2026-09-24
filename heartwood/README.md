# Heartwood

A real-time duel fought by shaping a tree that grows on its own. By Hugo Purcell and S. Minerva Scribner.

Only `index.html` is the game, and it is the only file the site needs. It is self-contained (no libraries, no data files, no network). Everything else in this folder is for the people building it and is never loaded by the page.

## Files

- **`index.html`**: the game. Its one `<script>` is split into marked blocks, and the tooling depends on those markers, so keep them when editing:
  - `/*BEGIN SIM*/ … /*END SIM*/` is the model: growth, bending, grafting, the shot rules, ballistics, the computer opponents. It never touches the DOM, so it can run headless.
  - The input layer sits between the two blocks: pointer handling, slicing, grafting by hand. It is not loaded headless.
  - `/*BEGIN VIEW*/ … /*END VIEW*/` holds drawing, measuring the figures, and flying the shots. It runs headless against a stubbed canvas.
  - After that come the planting screen, the frame loop, the readout, and the tuning drawer (`t` in the game).
- **`HEARTWOOD.md`**: the designer's manual. It covers every rule, every default number, why each rule is the way it is, and what is not built yet. Read this first to understand the game.
- **`heartwood_tests.js`**: the regression suite, about 120 checks from growth to the computer opponents. It lifts the SIM block straight out of `index.html` and runs it, so the tests can never drift from the game.
- **`harness.js`**: a loader used by `play.js`. It runs both the SIM and VIEW blocks under a fake canvas and document, so a headless run uses exactly the firing and flight code the browser uses.
- **`play.js`**: a headless duel for measuring balance. A scripted player (random, glow-following, aiming, grafting) fires a set number of turns at the other tree, optionally while one of the computer opponents fires back. It prints a table of every shot. The manual's numbers ("aim is the dominant term", how hard each opponent is) come from runs of this.

## Running the tooling

It needs Node (any recent version) and nothing else.

```
node heartwood_tests.js                 # the suite, about three minutes; exits 1 on any failure
node play.js policy=loop turns=24       # a duel: naive | random | glow | aim | loop
node play.js policy=aim mind=master     # …with the other side firing back
node play.js mine=spear,open theirs=broom,dense   # choose each seedling
```

Any number in the game's `S` table can be overridden on the `play.js` command line (for example `fadeHalf=5000`).

To play locally, just open `index.html` in a browser. It needs no server.
