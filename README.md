# the Fabrica

The workshop of St. Isidore University — sister site to [the Press](https://j-e-scriptorium.github.io/), which publishes books. Where the Press binds pages, the Workshop builds things that move: data visualizations and games, mechanized for a screen.

Live at whatever this repo's GitHub Pages URL is; `index.html` is the homepage.

## Layout

```
index.html, about.html, visualizations.html, recreations.html   the site shell (see assets/)
assets/                     shared header/footer, styles, logo, favicon
voyages/                    exhibit: Twenty Voyages (an atlas)
school/                     exhibit: School (a recreation)
many-rooms/                 exhibit: Many Rooms (a sonnet-dating game), plus the corpus + pipeline behind it
```

Each exhibit is self-contained in its own folder (its own `index.html`, plus whatever data/scripts it needs) and gets a small "&larr; the Fabrica" link back to the homepage. Exhibits are otherwise free to have their own look and feel — the shell only wraps the homepage and the catalog/about pages.

## Adding an exhibit

1. Build it in its own folder as `<name>/index.html` (+ any assets it needs, alongside it).
2. Add an entry to `visualizations.html` or `recreations.html` (copy an existing `.exhibit-entry` block).
3. Optionally add it to the homepage teaser list in `index.html`.

No build step, no server required for local dev — just open the HTML files, though the shared header/footer (`assets/fabrica-components.html`) is loaded via `fetch`, which needs `http://`, not `file://` (e.g. `python3 -m http.server`).
