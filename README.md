# the Fabrica

The workshop of St. Isidore University — sister site to [the Press](https://j-e-scriptorium.github.io/), which publishes books. Where the Press binds pages, the Workshop builds things that move: data visualizations and games, mechanized for a screen.

Live at whatever this repo's GitHub Pages URL is; `index.html` is the homepage.

## Layout

```
index.html, about.html, visualizations.html, recreations.html   the site shell (see assets/)
exhibit-*.html, about-*.html  one card page and one About page per exhibit
assets/                     shared header/footer, styles, logo, favicon
voyages/                    exhibit: Twenty Voyages (an atlas)
school/                     exhibit: School (a recreation)
many-rooms/                 exhibit: Many Rooms (a sonnet-dating game), plus the corpus + pipeline behind it
lignum-vitae/               exhibit: Lignum Vitae (a duel of growing trees), plus its manual and headless tests
campus-magnus/              exhibit: Campus Magnus (the Plains peoples, 1700–1900), plus its data tables, model and review docs
```

Each exhibit is self-contained in its own folder (its own `index.html`, plus whatever data/scripts it needs) and gets a small "&larr; the Fabrica" link back to the homepage. Exhibits are otherwise free to have their own look and feel — the shell only wraps the homepage and the catalog/about pages.

## Adding an exhibit

1. Build it in its own folder as `<name>/index.html` (+ any assets it needs, alongside it).
2. Add an entry to `visualizations.html` or `recreations.html` (copy an existing `.exhibit-entry` block). The title and glyph link to the exhibit's card page; mark unfinished work with `<span class="status-tag wip">[WIP]</span>` after the title.
3. Add the card page, `exhibit-<name>.html` (copy an existing one): the same card alone, with an `h1` title.
4. Add `about-<name>.html` (copy an existing one). The byline credits the work's makers and says who wrote the notes (`By …; notes by A. Clanker.`).
5. Optionally add it to the homepage teaser list in `index.html`.

No build step, no server required for local dev — just open the HTML files, though the shared header/footer (`assets/fabrica-components.html`) is loaded via `fetch`, which needs `http://`, not `file://` (e.g. `python3 -m http.server`).
