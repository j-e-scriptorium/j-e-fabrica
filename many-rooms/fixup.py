#!/usr/bin/env python3
"""Post-extraction fixups for the Many Rooms corpus.
1. Milton & Hopkins: per-poem composition dates (canonical scholarly
   datings), matched by first-line prefix.
2. Donne: split La Corona (first 7) from the Holy Sonnets; comp dates.
3. Shakespeare 99 (15 ll.) & 126 (12 ll.): restored, flagged irregular.
4. Sidney & Spenser: conservative u/v and i/j positional normalization
   (louing->loving, vp->up, ioy->joy). Spelling otherwise untouched.
"""
import json, re
from pathlib import Path
BASE = Path("/home/claude/sonnets")
recs = json.loads((BASE/"out/sonnets.json").read_text())

def key(s):
    return re.sub(r"[^a-z ]","",s.lower()).strip()[:30]

MILTON = {  # comp dates per Carey/Honigmann consensus
 "o nightingale":1629, "how soon hath time":1632, "captain or colonel":1642,
 "lady that in the prime":1644, "daughter to that good earl":1642,
 "a book was writ of late":1646, "i did but prompt the age":1646,
 "harry whose tuneful":1646, "when faith and love":1646,
 "fairfax whose name":1648, "cromwell our chief of men":1652,
 "vane young in years":1652, "when i consider how my light":1652,
 "avenge o lord thy slaughter":1655, "lawrence of virtuous father":1655,
 "cyriack whose grandsire":1655, "cyriack this three years":1655,
 "methought i saw my late":1658, "donna leggiadra":1630,
 "qual in colle aspro":1630, "giovane piano":1630,
 "diodati e te l dir":1630, "per certo i bei vostri occhi":1630,
}
HOPKINS = {
 "the world is charged":1877, "look at the stars":1877,
 "nothing is so beautiful":1877, "sometimes a lantern":1877,
 "on ear and ear":1877, "i caught this morning":1877,
 "summer ends now":1877, "as a daregale skylark":1877,
 "as kingfishers catch fire":1877, "in the valley of the elwy":1877,
 "i remember a house":1877, "towery city":1879, "have fair fallen":1879,
 "some candle clear":1879, "but tell me child":1879,
 "now times andromeda":1879, "felix randal":1880, "earth sweet earth":1882,
 "earnest earthless":1886, "to what serves mortal beauty":1885,
 "yes why do we all":1885, "not ill not carrion comfort":1885,
 "no worst there is none":1885, "to seem the stranger":1885,
 "i wake and feel":1885, "patience hard thing":1885,
 "my own heart":1885, "honour is flashed":1888,
 "thou art indeed just":1889, "the shepherds brow":1889,
 "the fine delight":1889,
}
matched = {"Milton":0, "Hopkins":0}
for r in recs:
    k = key(r["lines"][0])
    if r["author"]=="John Milton":
        for pre,y in MILTON.items():
            if k.startswith(key(pre)[:18]):
                r["year"]=y; r["year_type"]="comp"; matched["Milton"]+=1; break
    if r["author"]=="Gerard Manley Hopkins":
        for pre,y in HOPKINS.items():
            if k.startswith(key(pre)[:18]):
                r["year"]=y; r["year_type"]="comp"; matched["Hopkins"]+=1; break

# --- Donne: La Corona = first 7 of pg 48688 (they are a linked crown) ---
donne = [r for r in recs if r["author"]=="John Donne"]
for i,r in enumerate(donne):
    if i < 7:
        r["sequence"]="La Corona"; r["title"]=f"La Corona {i+1}"
        r["num"]=i+1; r["year"]=1607; r["year_type"]="comp"
    else:
        r["sequence"]="Holy Sonnets"; r["title"]=f"Holy Sonnets {i-6}"
        r["num"]=i-6; r["year"]=1610; r["year_type"]="comp"

# --- Shakespeare 99 & 126, restored with irregular flag ---
import unicodedata
txt=(BASE/"raw/1041.txt").read_text(errors="replace")
def grab(n, expect):
    R={99:"XCIX",126:"CXXVI"}[n]
    m=re.search(rf"^\s*{R}\s*$", txt, re.M)
    lines=[]
    for ln in txt[m.end():].splitlines():
        if not ln.strip():
            if lines: break
            continue
        lines.append(unicodedata.normalize("NFC",ln.strip()))
    assert len(lines)==expect, (n, len(lines))
    return lines
for n, exp in ((99,15),(126,12)):
    recs.append(dict(author="William Shakespeare", title=f"Sonnets {n}",
        sequence="Sonnets", num=n, year=1609, year_type="pub",
        spelling="modern", irregular=True, lines=grab(n,exp), source_pg=1041))

# --- u/v, i/j positional normalization for old-spelling texts ---
VOW="aeiouyAEIOUY"
def uv(word):
    w=list(word)
    for i,c in enumerate(w):
        if c in "uU" and 0<i<len(w)-1 and w[i-1] in VOW and w[i+1] in VOW:
            w[i]="v" if c=="u" else "V"          # loue -> love
        elif c in "vV" and i==0 and len(w)>1 and w[1] not in VOW+"rl":
            w[i]="u" if c=="v" else "U"          # vp -> up, vnto -> unto
        elif c in "iI" and i==0 and len(w)>1 and w[1] in "aeiouAEIOU":
            w[i]="j" if c=="i" else "J"          # ioy -> joy
    return "".join(w)
def norm_line(l):
    return re.sub(r"[A-Za-z]+", lambda m: uv(m.group(0)), l)
for r in recs:
    if r.get("spelling")=="old":
        r["lines"]=[norm_line(l) for l in r["lines"]]
        r["spelling"]="old-uv-normalized"

for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs, indent=1))
print("matched dates:", matched, "| total:", len(recs))

# --- Yeats: prune non-sonnets/chunks; restore Leda (split line 11 rejoined) ---
recs=[r for r in recs if not (r["author"]=="W. B. Yeats")]
_t=(BASE/"raw/72985.txt").read_text(errors="replace")
_m=re.search(r"LEDA AND THE SWAN(.*?)\n1928",_t,re.S)
_ls=[l.strip() for l in _m.group(1).splitlines() if l.strip()]
# rejoin the dropped line: "And Agamemnon dead." + "Being so caught up,"
_j=[]
for l in _ls:
    if l.startswith("Being so caught up"): _j[-1]=_j[-1]+" "+l
    else: _j.append(l)
assert len(_j)==14, len(_j)
recs.append(dict(author="W. B. Yeats", title="Leda and the Swan",
    sequence="The Tower", num=1, year=1923, year_type="comp",
    spelling="modern", lines=[unicodedata.normalize("NFC",l) for l in _j],
    source_pg=72985))

# --- title hygiene: drop footnote-assemblies; retitle numeric/generic titles ---
recs=[r for r in recs if not re.search(r"FOOTNOTE|VARIANT|NOTES ON|CONTENTS",r["title"],re.I)]
for r in recs: r["title"]=re.sub(r"\[\d+\]","",r["title"]).strip()
for r in recs:
    if re.fullmatch(r"\d{1,4}",r["title"]) or re.fullmatch(r"Sonnets \d+",r["title"]) \
       and r["author"]=="William Wordsworth":
        r["title"]='"'+r["lines"][0].rstrip(",;:.! ")[:58]+'"'

for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("after hygiene:",len(recs))

# --- Keats posthumous one-offs, from full quotations in the biographies ---
def grab_at(pg, anchor, n=14):
    t=(BASE/f"raw/{pg}.txt").read_text(errors="replace")
    i=t.find(anchor); assert i>=0, anchor
    ls=[l.strip().strip('"') for l in t[i:].splitlines() if l.strip()][:n]
    assert len(ls)==n
    return [unicodedata.normalize("NFC",l) for l in ls]
recs.append(dict(author="John Keats", title="When I have fears that I may cease to be",
    sequence="Posthumous", num=1, year=1818, year_type="comp", spelling="modern",
    lines=grab_at(36356,"When I have fears that I may cease to be"), source_pg=36356))
recs.append(dict(author="John Keats", title="Bright star, would I were steadfast as thou art",
    sequence="Posthumous", num=2, year=1819, year_type="comp", spelling="modern",
    lines=grab_at(31682,'"Bright star, would I were steadfast'), source_pg=31682))

for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("with keats one-offs:",len(recs))

# --- Later Life has exactly 28; drop strays past the section's true end ---
recs=[r for r in recs if not (r["sequence"]=="Later Life" and r["num"]>28)]
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("final:",len(recs))

# --- Monna Innominata is a sonnet-of-sonnets: exactly 14; cap strays ---
recs=[r for r in recs if not (r["sequence"]=="Monna Innominata" and r["num"]>14)]
# --- global dedupe on text (collected editions reprint earlier volumes) ---
seen={}; keep=[]
for r in recs:
    k=tuple(r["lines"])
    if k in seen:
        prev=keep[seen[k]]
        if prev["year_type"]=="approx" and r["year_type"]!="approx":
            keep[seen[k]]=r
        continue
    seen[k]=len(keep); keep.append(r)
recs=keep
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("deduped final:",len(recs))

# --- publisher's advertisement pages masquerading as sonnets ---
def is_ad(r):
    t=" ".join(r["lines"])+" "+r["title"]
    return bool(re.search(r"=|\$\d|\bvols?\.\s|\b12mo\b|\bIllustrated\b|\bcloth\b|DRAMATIS|PERSONAE|ARGUMENT",t)
                or re.match(r"PREFACE|NOTE",r["title"]))
recs=[r for r in recs if not is_ad(r)]
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("post-ad-filter:",len(recs))

# --- drama-chunk scrub (verse plays chopped between headings) ---
_dr=re.compile(r"^_?[A-Z][a-zA-Z]{1,14}\._|^[A-Z]{2,}[A-Z ]{0,20}:|\[?_?(Exit|Exeunt|Enter|SCENE|Scene [IVX])")
recs=[r for r in recs if not any(_dr.search(l) for l in r["lines"])]

# --- The Windhover (mechanically unrecoverable from PG print; Wikisource text) ---
_wh=[l for l in (BASE/"raw/windhover_wikisource.txt").read_text().splitlines() if l.strip()]
assert len(_wh)==14
recs.append(dict(author="Gerard Manley Hopkins", title="The Windhover",
    sequence="Poems (1918)", num=12, year=1877, year_type="comp", spelling="modern",
    lines=_wh, source_pg=0))

# --- Surprised by joy (lost to local apparatus; grab from vol 5 print) ---
_ls=[]
for _vol in ("47651","52836"):
  if _ls: break
  _t=(BASE/f"raw/{_vol}.txt").read_text(errors="replace")
  for _m in re.finditer(r"Surprised by joy",_t):
    _cand=[]
    for ln in _t[_m.start():].splitlines():
        if not ln.strip():
            if _cand: break
            continue
        _cand.append(re.sub(r"\s{2,}\d{1,3}\.?$","",re.sub(r"\[\w{1,2}\]","",ln)).strip())
    if len(_cand)==14 and not any("ED." in c or c.startswith("[") for c in _cand):
        _ls=_cand; break
assert len(_ls)==14, len(_ls)
recs.append(dict(author="William Wordsworth", title="Surprised by joy",
    sequence="Sonnets", num=0, year=1815, year_type="comp", spelling="modern",
    lines=[unicodedata.normalize("NFC",l) for l in _ls], source_pg=56361))

# --- Shelley famous-poem composition dates ---
SHELLEY={"i met a traveller":1817,"an old mad blind despised":1819,
 "o wild west wind":1819,"lift not the painted veil":1818,
 "poet of nature thou hast wept":1815,"i hated thee fallen tyrant":1815}
for r in recs:
    if r["author"]=="Percy Bysshe Shelley":
        k=re.sub(r"[^a-z ]","",r["lines"][0].lower())[:22]
        for pre,y in SHELLEY.items():
            if k.startswith(pre[:min(20,len(pre))]): r["year"]=y; r["year_type"]="comp"; break

for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.5 final:",len(recs))

# --- v0.6 targeted recoveries ---
def _grab(pg, anchor, n=14, clean=True):
    t=(BASE/f"raw/{pg}.txt").read_text(errors="replace")
    for m in re.finditer(re.escape(anchor),t):
        c=[]
        for ln in t[m.start():].splitlines():
            if not ln.strip():
                if c: break
                continue
            l=re.sub(r"\s+_?\d{1,3}\.?$","",re.sub(r"\[\w{1,2}\]","",ln)).strip() if clean else ln.strip()
            c.append(unicodedata.normalize("NFC",l))
        if len(c)==n and not any(x.startswith("[") or "ED." in x for x in c):
            return c
    return None
def _add(author,title,seq,year,yt,lines,pg,**kw):
    if lines: recs.append(dict(author=author,title=title,sequence=seq,num=0,
        year=year,year_type=yt,spelling=kw.get("spelling","modern"),lines=lines,source_pg=pg))
    else: print("GRAB FAILED:",title)
def _grab_glue(pg,anchor,n=14):
    t=(BASE/f"raw/{pg}.txt").read_text(errors="replace")
    i=t.find(anchor)
    if i<0: return None
    c=[]
    for ln in t[i:].splitlines():
        s=ln.strip()
        if not s: continue
        if s.startswith("_") or "]" in s: continue   # skip textual glosses
        c.append(unicodedata.normalize("NFC",re.sub(r"\s+\d{1,3}$","",s)))
        if len(c)==n: return c
    return None
_add("Henry Howard, Earl of Surrey","Description of Spring","OBEV",1557,"pub",
     _grab_glue(66619,"The soote season, that bud and bloom forth brings"),66619)
_add("Percy Bysshe Shelley","Lift not the painted veil","Poems",1818,"comp",
     _grab(4800,"Lift not the painted veil which those who live"),4800)
_add("John Keats","Great spirits now on earth","Posthumous",1816,"comp",
     _grab(36356,"Great spirits now on earth are sojourning"),36356)
_add("John Keats","Why did I laugh to-night?","Posthumous",1819,"comp",
     _grab(36356,"Why did I laugh to-night?"),36356)
_add("John Keats","Time's sea hath been","Posthumous",1818,"comp",
     _grab(36356,"Time's sea hath been five years"),36356)
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("post-recoveries:",len(recs))

# --- v0.6 web-recovered founders & 18th c. (texts from fetched sources) ---
_web=json.loads((BASE/"raw/web_recoveries.json").read_text())["poems"]
for p in _web:
    assert len(p["lines"])==14, p["title"]
    recs.append(dict(author=p["author"],title=p["title"],sequence=p["sequence"],num=0,
        year=p["year"],year_type=p["year_type"],spelling=p["spelling"],
        lines=[unicodedata.normalize("NFC",l) for l in p["lines"]],source_pg=0))
# Surrey's soote season: re-date to composition era (he died 1547)
for r in recs:
    if r["title"]=="Description of Spring": r["year"]=1542; r["year_type"]="approx"
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.6:",len(recs))

# --- v0.7: Wyatt & Surrey expansion (fetched, cross-corroborated texts) ---
_web2=json.loads((BASE/"raw/web_recoveries2.json").read_text())["poems"]
for p in _web2:
    assert len(p["lines"])==14, p["title"]
    recs.append(dict(author=p["author"],title=p["title"],sequence=p["sequence"],num=0,
        year=p["year"],year_type=p["year_type"],spelling=p["spelling"],
        lines=[unicodedata.normalize("NFC",l) for l in p["lines"]],source_pg=0))
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.7:",len(recs))

# --- v0.8 date refinements ---
for r in recs:
    if r["author"]=="Claude McKay" and r["lines"][0].startswith("If we must die"):
        r["year"]=1919; r["year_type"]="comp"   # pub. The Liberator, July 1919
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.8:",len(recs))

# --- v0.9 date pins + OBEV one-offs ---
for r in recs:
    if r["author"]=="Emma Lazarus" and r["lines"][0].startswith("Not like the brazen giant"):
        r["year"]=1883; r["year_type"]="comp"; r["title"]="The New Colossus"
_add("William Cowper","To Mrs Unwin","OBEV",1793,"comp",
     _grab_glue(66619,"Mary! I want a lyre with other strings"),66619)
_add("Thomas Hood","Silence","OBEV",1823,"pub",
     _grab_glue(66619,"There is a silence where hath been no sound"),66619)
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.9:",len(recs))

# --- v0.9 web recoveries: Poe, Byron ---
_web3=json.loads((BASE/"raw/web_recoveries3.json").read_text())["poems"]
for p in _web3:
    assert len(p["lines"])==14, p["title"]
    recs.append(dict(author=p["author"],title=p["title"],sequence=p["sequence"],num=0,
        year=p["year"],year_type=p["year_type"],spelling="modern",
        lines=[unicodedata.normalize("NFC",l) for l in p["lines"]],source_pg=0))
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v0.9 final:",len(recs))

# --- Dunbar date pins ---
for r in recs:
    if r["author"]=="Paul Laurence Dunbar":
        l0=r["lines"][0].lower()
        if l0.startswith("ah, douglass"): r["year"]=1903; r["year_type"]="pub"
        if "thunder voice of fate" in " ".join(r["lines"][:2]).lower(): r["year"]=1900; r["year_type"]="pub"
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("with dunbar/wilde:",len(recs))

# --- v1.0 web recoveries: Herbert, Blake ---
_web4=json.loads((BASE/"raw/web_recoveries4.json").read_text())["poems"]
for p in _web4:
    assert len(p["lines"])==14, p["title"]
    recs.append(dict(author=p["author"],title=p["title"],sequence=p["sequence"],num=0,
        year=p["year"],year_type=p["year_type"],spelling=p["spelling"],
        lines=[unicodedata.normalize("NFC",l) for l in p["lines"]],source_pg=0))
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v1.0:",len(recs))

recs=[r for r in recs if "Edition" not in r["title"]]
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v1.0 final:",len(recs))

# --- v1.1 web recoveries: Frost 1928, Keats x2, Auden, Raleigh ---
_web5=json.loads((BASE/"raw/web_recoveries5.json").read_text())["poems"]
for p in _web5:
    assert len(p["lines"])==14, p["title"]
    recs.append(dict(author=p["author"],title=p["title"],sequence=p["sequence"],num=0,
        year=p["year"],year_type=p["year_type"],spelling="modern",
        lines=[unicodedata.normalize("NFC",l) for l in p["lines"]],source_pg=0))
for i,r in enumerate(recs): r["id"]=f"s{i:05d}"
(BASE/"out/sonnets.json").write_text(json.dumps(recs,indent=1))
print("v1.1:",len(recs))
