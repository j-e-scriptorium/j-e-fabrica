# Many Rooms — sonnet corpus v1.4

**2,387 playable sonnets by 87 authors, 1535–1928 — US public domain (pub ≤1930)**, plus
49 more sitting in the archive out of play — 35 undated (`year: null`), 14 dated but
still `needs_review` — until someone can finish them — **2,436 records total**, 101
authors. Normalized JSON, from 23 Project Gutenberg volumes
(GITenberg mirrors) plus other public-domain sources. Pipeline: `extract.py`
(add a volume = add a config) then `fixup.py` (dates, splits, hygiene).

## Schema
`{id, author, title, sequence, num, year, year_type(pub|comp|approx|unknown), spelling,
lines[14], source_pg, irregular?, needs_review?, source?, author_dates?, date_note?}`

`year: null` + `year_type: "unknown"` marks a sonnet with no established date — kept in
the archive, held out of the game (the game filters on `typeof year === "number"`).
`needs_review: true` marks a sonnet whose text still has a gap an OCR pass couldn't
close (a missing word or line, not just noise) — also held out of play regardless of
whether it later gets a date. `date_note`, where present, is a short citation for
the reveal screen (e.g. "on Thomas Clere, d. Apr. 1545; pr. Tottel 1557").

## Dating convention

**A sonnet's `year` is its first-publication date, except where first publication
was posthumous, in which case `year` is the composition date instead** — and a
sonnet first published in the same calendar year its poet died counts as
published in the poet's lifetime, not posthumously (so it's dated by
publication, `year_type: "pub"`, not composition). `year_type` records which
rule produced the date: `pub` (published in the poet's lifetime, including the
death-year case above), `comp` (composition, firmly pinned by an occasion,
letter, or datable death), `approx` (composition, estimated to within a few
years — treat the year as approximate, not exact), `unknown` (no date
established at all). This is why, for example, Wyatt and Surrey are dated to
the 1530s–40s (when they wrote) rather than 1557 (when Tottel's Miscellany
first printed them after both were dead) — publication dating would make them
indistinguishable from everyone else Tottel printed decades later.

## What's in it
Elizabethans: Sidney A&S 107 · Daniel Delia 64 · Constable Diana 64 ·
Lodge Phillis 33 · Fletcher Licia 50 · Spenser Amoretti 63 · Griffin
Fidessa 61 · Smith Chloris 48 · Shakespeare 153 (incl. 99 & 126,
`irregular:true` — 15 and 12 lines) · Drayton Idea 64.
17th c.: Donne (La Corona 7, comp 1607; Holy Sonnets 19, comp 1610) ·
Milton 19 (14 individually comp-dated 1629–1658 by first-line match).
19th–20th c.: **Wordsworth 425+ with per-poem composition dates parsed
from Knight's chronological edition** (the "Composed 1802.—Published
1807" datelines; a dateline persists over grouped series, e.g. the
Ecclesiastical Sonnets) · Keats 18 · EBB 44 · D.G. Rossetti 98 · Hopkins
23 (22 comp-dated 1877–89) · Brooke 14 · Yeats: Leda and the Swan (comp
1923; the split line 11 rejoined).

## Added in v1.4 (dating pass on the v1.3 batch, user-supplied)
Dates applied to 137 of the 172 Main's Treasury sonnets added in v1.3, moving
them from `year: null` into play — the corpus's convention (see "Dating
convention" above) supplied by the same source, plus five more first-line
repairs (opening lines the Index of First Lines in v1.3 couldn't reach) and
one text-driven `date_note`. Also: two James Weldon Johnson sonnets ("Mother
Night" and a Plácido translation, both *Fifty Years & Other Poems*, 1917)
added with `needs_review: true` — each is missing its final line in the
source text supplied, so both keep a known, correct date but stay out of
play until the missing line turns up; and the two Rupert Brooke additions
from v1.2 were redated 1913→1915 (`approx`/`comp`→`pub`) to apply the
death-year rule correctly: *1914 and Other Poems* was published in 1915,
the year Brooke died, which counts as published-in-lifetime, not
posthumous — matching the dating already used for its 15 siblings already
in the corpus.

The remaining 35 of the 172 stay undated: Main's anthology gives only
poets' life-dates, and this pass didn't reach every poem (nine C. T. Turner
sonnets need matching against three later Turner volumes on Archive.org;
six Hartley Coleridge sonnets split between an 1833 and a posthumous 1851
volume; a handful of others have no clean lead at all). All still sit in
the corpus, undated, out of play.

## Added in v1.3 (Main's *Treasury of English Sonnets*, 1880 — user-supplied)
172 sonnets recovered from an OCR scan of Main's 1880 anthology (IA
`treasuryofenglis00mainuoft`), supplied pre-extracted with per-poem
`needs_review`/repair metadata. Two entirely new poets enter the corpus:
Charles Tennyson Turner (21) and William Drummond of Hawthornden (14),
plus additions to Wyatt, Surrey, Spenser, Sidney, Constable, Chapman,
Florio, Barnes, Browne, Edwards, Mason, Warton, W. Roscoe, Wordsworth,
Charlotte Smith, Thurlow, Elliott, W. S. Roscoe, Kirke White, Wilson,
De Vere, R. Roscoe, Procter, Shelley (2 sections of *Ode to the West
Wind*), Keats, Talfourd, Hartley Coleridge, Blanchard, Sterling, EBB,
Alford, W. C. Roscoe, Julian Fane, Clare, Hemans, Hood, Hallam, Faber,
and Gray. 255 candidates were dedupe-checked against the existing
corpus first (exact + fuzzy, same-author word-overlap) — 83 were
already present and were skipped rather than duplicated; one further
poem (Spenser, Amoretti 75, "One day I wrote her name...") was dropped
from this batch because its opening line was missing entirely from the
extraction, not just garbled.

Every included poem got a hand pass against its OCR: drop-cap corruption
(the scan's illuminated first letters routinely OCR as noise — running
headers glued onto opening words, page numbers and author life-dates
glued into verse lines, stray symbols standing in for punctuation) was
corrected wherever the intended text was unambiguous from what survived;
19 poems where a genuine word or line was missing (not just garbled) got
`needs_review: true` and stay text-as-found rather than guessed-at. One
mistitled-but-correct-text case from the running-header noise (Turner's
"Letty's Globe" retained its OCR'd alternate subtitle rather than the
better-known title, since the familiar title itself never appears in the
extraction) was left as supplied rather than supplied from memory.

**None of the 172 carry a date** — Main's anthology gives only poets'
life-dates, never per-poem composition or publication years, and
research to date them individually wasn't feasible this round. All 172
are `year: null, year_type: "unknown"`, present in the corpus and
excluded from play until dated.
Rupert Brooke +2: "He Wonders Whether to Praise or to Blame Her" and "A
Memory" (both from *1914 and Other Poems*, comp. c.1913, pre-dating the
war sonnets — dated separately from their blanket-1915 siblings in this
same volume; the two dates now coexist in one sequence, a minor
inconsistency worth revisiting). Also fixed a mistitled entry: s00871,
carried since v0.x as "The Pacific, 1914", is in fact "Sonnet
(Suggested by some of the Proceedings of the Society for Psychical
Research)" — same text, wrong heading; title corrected, text untouched.
Provenance: user-supplied text, cross-verified line-for-line against
Sonnets from the Portuguese I–XLIV and 12 already-present Brooke poems
(all matched exactly) before anything was added.
Not added: two James Weldon Johnson poems ("Mother Night" and "Sonnet,
from the Spanish of Plácido," *Fifty Years & Other Poems*, 1917) were
supplied but each ran only 13 lines after the title was stripped out of
the line array — one line short of a sonnet, ending mid-sentence.
Held pending a complete text.

## Fixes applied since v0.1
Sidney & Spenser: conservative positional u/v–i/j normalization
(louing→loving, vp→up, ioy→joy) — tagged `old-uv-normalized`; other
archaic spellings untouched. Shakespeare 99/126 restored. Donne split.
Milton/Hopkins per-poem dates. Junk-title hygiene (footnote assemblies
dropped; numeric titles replaced with first lines).

## Added in v1.1 (snippet harvest)
Frost, "Acquainted with the Night" (West-Running Brook, 1928 — PG has
no edition of the volume yet, so the corpus's single most-wanted modern
sonnet came in by cross-corroborated snippet, like the founders did) ·
Auden, "The Secret Agent" (comp Jan 1928; pub Poems 1928/1930 → US-PD
— the requested Auden is in) · Keats, "On the Sea" (1817) and "To
Sleep" (1819; l.11 reads "lords" per standard editions, "hoards" is an
attested variant) · Raleigh, "A Vision upon the Fairy Queen" (1590).
Provenance in raw/web_recoveries5.json. cummings could not be
completed: snippets carry only 3 lines and the full-text sites block
fetching — manual.

## Added in v1.0 (final hunt)
Dunbar 22 (Complete Poems; "Douglass" 1903, "Robert Gould Shaw" 1900
pinned) · Wilde 42 (Poems 1881 — count is high-ish; spot-check for
14-line chunks of Charmides etc.) · Herbert 2 ("Prayer (I)" and
"Redemption," 1633 Temple text — the two Temple sonnets every anthology
carries; ~13 more remain in the unmirrored volume) · Blake 1 ("To the
Evening Star," 1783 — the unrhymed proto-Romantic sonnet). All web
texts cross-corroborated; provenance in raw/web_recoveries4.json.

## Added in v0.9 (canon-first audit — see poets100.md)
Coverage re-audited from a 100-poet canon checklist (poets100.md) rather
than by sonneteer. Added: Hardy 9 (Wessex Poems; all comp-dated 1866 via
new bare-year dateline capture — "Hap," "Revulsion," the She-to-Him
group) · Emma Lazarus 44 (The New Colossus pinned to 1883) · Cullen 5
(Color 1925, "Yet Do I Marvel") · Pound 11 (Canzoni & Ripostes 1912,
"A Virginal") · Clare 5 (Symons selection only; his ~400 need better
sources) · Poe ("Sonnet—To Science" 1829) · Byron 2 (Chillon + Lake
Leman, 1816) · Cowper ("To Mrs Unwin") and Hood ("Silence") from OBEV.
Checklist verdict: ~42 of the 100 canonical poets wrote no meaningful
sonnets; remaining ranked gaps are in poets100.md.

## Added in v0.8 (the American 20th century — US public domain)
Corpus policy is now explicitly **US public domain (published ≤1930)**;
EU life+70 status is not tracked per user instruction. Frost (d.1963)
is the only currently-included author still in copyright in life+70
jurisdictions. Added: Millay 43 (Renascence 1917, A Few Figs 1920,
Second April 1921 — its Twelve Sonnets complete — The Harp-Weaver 1923
incl. "Euclid alone" and "What lips my lips have kissed") · McKay 34
from Harlem Shadows 1922 ("If We Must Die" dated to its 1919 Liberator
printing) · E. A. Robinson 35 (Children of the Night 1897 — finally
populating the 1890s — and Man Against the Sky) · Elinor Wylie 7 (Nets
to Catch the Wind 1921, incl. Wild Peaches) · Frost 9 (A Boy's Will
1913, Mountain Interval 1916: Mowing, The Oven Bird, Putting in the
Seed, Range-Finding). Not yet gettable via the GitHub mirror (post-2019
PD entrants not synced): Auden Poems 1930 (US-PD since Jan 2026),
Frost's West-Running Brook 1928 ("Acquainted with the Night"), Millay's
Buck in the Snow 1928, cummings' Tulips and Chimneys 1923; all need
Gutenberg-direct fetching. Millay's Fatal Interview (52 sonnets) enters
US PD Jan 1, 2027.

## Added in v0.7 (the founders, properly)
Wyatt now 6: Whoso list to hunt · The long love (Egerton text, the
famous pairing with Surrey's "Love that doth reign" — both translate
Petrarch's Rima 140) · My galley · I find no peace (Rima 134) ·
Farewell Love · Divers doth use. Surrey now 4: adding "Set me whereas
the sun" and "Alas! so all things now do hold their peace." All texts
fetched and cross-corroborated (provenance per poem in
raw/web_recoveries2.json); all dated c.1535/c.1542 approx. This is the
anthology core of both founders — nearly every Wyatt/Surrey sonnet a
survey course assigns. Full Tottel (~30 more Wyatt, ~10 more Surrey,
mostly minor) remains unreachable without a scanned-book pipeline: no
PG/GITenberg volume exists, and sonnets.org blocks fetching.
"Unstable dream" found only in fragment; skipped.

## Added in v0.6 (founders & the 18th century)
Wyatt, "Whoso list to hunt" (comp c.1535 — the corpus now begins at the
form's English origin) · Surrey ×2: "Description of Spring" (from the
Oxford Book of English Verse; textual glosses shed) and "Love that doth
reign" (both c.1542 approx) · Gray, "Sonnet on the Death of Richard
West" (comp 1742 — the poem Wordsworth's Preface made pedagogically
immortal) · Charlotte Smith ×4 from Elegiac Sonnets (1784–89), incl.
the Middleton churchyard sonnet · Keats posthumous +3 ("Great spirits"
1816, "Time's sea" 1818, "Why did I laugh to-night?" 1819, all from
full quotations in Colvin) · Shelley's "Lift not the painted veil"
recovered from the raw file. Web-recovered texts (Wyatt, Surrey's
"Love that doth reign", Gray, Smith) are composed from fetched,
cross-corroborated sources, never from model memory; provenance is in
raw/web_recoveries.json. "On the Sea" remains absent (only excerpted
in Colvin). Wyatt is 1/~30 and Surrey 2/~15: representation, not
coverage — full Tottel needs an off-mirror old-spelling source.

## Added in v0.5 (coverage audit round)
Shelley added (~20 incl. Ozymandias 1817, England in 1819, To the Nile,
To Wordsworth — closing the corpus's single worst gap). The Windhover
restored (its PG printing interleaves Hopkins's lineation with the
printer's wrapping undecidably; text taken from Wikisource). "Surprised
by joy" restored (was present only as an editor's footnote in one
volume). Drama scrub: ~50 fourteen-line chunks of verse plays
(Coleridge's Wallenstein/Remorse, Longfellow's dramas, Shelley's Cenci)
removed via speaker-tag detection. Trailing-apparatus shedding rescued
~35 more sonnets incl. Shakespeare's missing 152nd regular sonnet and
D. G. Rossetti's proem ("A Sonnet is a moment's monument"). Hutchinson
line-numbers (_5, _10) cleaned. Publisher-ad and preface filters
extended.

## Added in v0.4
S. T. Coleridge ~113 (collected ed.; blanket 1796, `year_type:approx`) ·
Longfellow ~103 (blanket 1873 approx; **includes his verse translations
of Italian/Spanish sonnets — filter by title if you want originals
only**) · Christina Rossetti 68: Monna Innominata complete 14 (the
Dante/Petrarch epigraphs are shed, incl. 3-line ones), Later Life 28,
Goblin Market vol. + Pageant vol. poems · Matthew Arnold 30 (1855
approx; the volume's publisher-advertisement pages parsed as 14-line
"sonnets" and are now filtered — watch for this hazard in any
19th-c. trade volume) · Alice Meynell 15 (1893 approx) · war poets:
Sorley 8 (comp 1915), Owen 3 (comp 1917; "Futility" included — 14
lines, standardly read as a sonnet variant). Epigraph-shedding also
recovered ~90 sonnets in previously-processed volumes (dedications and
mottoes had been silently disqualifying them). Reprint dedupe added
(collected editions reprint earlier volumes; non-approx dates win).

## Added in v0.3
Anna Seward, Original Sonnets (71, pub 1799 — composed across the
1770s–90s; per-poem dates unavailable) · W. L. Bowles, Sonnets (41,
dated 1789 = Fourteen Sonnets year; later sonnets in the section carry
this approximate date — refine manually if desired) · Keats posthumous:
"When I have fears" (comp 1818) and "Bright star" (comp 1819), taken
from full quotations in the Colvin and W. M. Rossetti biographies.
Bowles's footnote-marked titles cleaned. Meredith excluded by policy
(16-line form). Orthography policy settled: positional u/v–i/j
normalization only; old spelling otherwise retained.

## Known limitations (ranked)
1. 1660–1780 remains empty by design (the form's true dormancy).
   Optional bridges if wanted: Gray's West sonnet (1742 — the Select
   Poems edition lacks it; beware The Bard's 14-line ode strophes, which
   masquerade as sonnets), Charlotte Smith's Elegiac Sonnets (1784),
   Thomas Warton — all need Gutenberg-direct or Wikisource fetching.
2. Amoretti is 63/89 — the Todd text has dropped lines; the 14-line rule
   correctly rejects corrupt sonnets. Recovering the rest needs a better
   source text.
3. 5 Milton + 1 Hopkins unmatched by first line → still carry pub year.
4. Wordsworth dates trust Knight's chronological arrangement; a persisted
   dateline can be ±a few years for undated poems. Spot-check.
5. Sidney/Spenser remain old-spelled beyond u/v — a gameplay tell.
   Full modernization is editorial work.
6. Not yet in: Christina Rossetti (Monna Innominata), Wyatt/Surrey
   (old spelling), further Keats posthumous sonnets (Colvin's biography
   quotes several more in full — "Time's sea", "To Sleep", "On the
   Sea" — but harvesting quoted verse from a biography risks
   misattribution; verify by hand), Michael Field, Longfellow.
