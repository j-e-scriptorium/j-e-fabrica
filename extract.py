#!/usr/bin/env python3
"""PG volumes -> sonnets.json.
Rule: a poem = all verse blocks between headings; it's a sonnet iff it
totals exactly 14 lines. Headings = numerals, SONNET N, short title lines,
or section-name blocks (which also switch author/sequence state)."""
import json, re, unicodedata
from pathlib import Path
RAW=Path("/home/claude/sonnets/raw"); OUT=Path("/home/claude/sonnets/out")
ROMAN=re.compile(r"^[IVXLCivxlc]+\.?$"); ARABIC=re.compile(r"^[0-9]{1,4}\.?$")
SONN=re.compile(r"^(?:SONNET|Sonnet)\s+([IVXLCivxlc]+|[0-9]+)\.?")
def r2i(r):
    v=dict(I=1,V=5,X=10,L=50,C=100); r=r.strip(". ").upper()
    if not r or any(c not in v for c in r): return None
    t=0
    for i,c in enumerate(r): t+= -v[c] if i+1<len(r) and v[r[i+1]]>v[c] else v[c]
    return t
def strip_pg(t):
    s=re.search(r"\*\*\* ?START OF.*?\*\*\*",t); e=re.search(r"\*\*\* ?END OF",t)
    return t[s.end() if s else 0: e.start() if e else len(t)]
def blocks(t):
    out,cur=[],[]
    for ln in t.splitlines():
        if ln.strip(): cur.append(ln.rstrip("\r\n "))
        elif cur: out.append(cur); cur=[]
    if cur: out.append(cur)
    return out
def verseish(b):
    ls=[l.strip() for l in b]
    if any(l.startswith(("[","_[","*")) for l in ls): return False
    if len(b)==1:
        l=ls[0]
        if l.isupper(): return False
        if re.search(r"--Ed\.?$|--I\. ?F\.|--W\. ?W\.|^One of|Journal\)|^\(",l): return False
    return all(2<len(l)<=85 for l in ls)
def dedent(ls):
    p=min((len(l)-len(l.lstrip()) for l in ls if l.strip()),default=0)
    return [l[p:] for l in ls]

def extract(path,cfg):
    txt=strip_pg(path.read_text(errors="replace"))
    if cfg.get("unwrap"):
        _n=cfg["unwrap"] if isinstance(cfg["unwrap"],int) else 5
        out=[]
        for ln in txt.splitlines():
            if re.match(r"^ {%d,}\S"%_n,ln) and out and out[-1].strip():
                out[-1]=out[-1].rstrip()+" "+ln.strip()
            else: out.append(ln)
        txt="\n".join(out)
    if "start" in cfg:
        i=txt.find(cfg["start"]); txt=txt[i:] if i>=0 else txt
    if "end" in cfg:
        i=txt.find(cfg["end"],1); txt=txt[:i] if i>0 else txt
    secs={}
    for s in cfg["sections"]:
        for nm in s.get("names",[s["name"]]):
            secs[nm.upper().rstrip(". :")]=s
    cur=cfg["sections"][0]; capture=len(cfg["sections"])==1
    recs=[]; num=None; ttl=None; poem=[]; cyear=None   # poem = list of blocks
    def emit(lines,n_hint,t_hint,cy=None):
        n=n_hint or (len([r for r in recs if r["sequence"]==cur["seq"]])+1)
        t=t_hint if (t_hint and cur.get("use_titles")) else f'{cur["seq"]} {n}'
        if cur.get("need_comp") and cy is None: return   # skip dateless poems
        recs.append(dict(author=cur["author"],title=t,sequence=cur["seq"],num=n,
            year=cy if cy else cur["year"],
            year_type="comp" if cy else cur.get("yt","pub"),
            spelling=cur.get("spelling","modern"),
            lines=[unicodedata.normalize("NFC",
                re.sub(r"\s+_?\d{1,3}\.?$","",re.sub(r"\[\w{1,2}\]","",l)).strip())
                for l in dedent(lines)],
            source_pg=cfg["pg"]))
    def close():
        nonlocal poem,num,ttl,cyear
        if capture and poem:
            trimmed=list(poem); oy=None
            def viable(bs): return sum(map(len,bs))==14 or (bs and all(len(b)==14 for b in bs))
            while len(trimmed)>1 and not viable(trimmed):
                if len(trimmed[0])<=3: trimmed.pop(0)      # leading epigraphs/mottoes
                elif len(trimmed[-1])<=3:
                    _m=re.match(r"^\(?(1[5-9]\d\d)\)?\.?$",trimmed[-1][-1].strip())
                    if _m: oy=int(_m.group(1))              # Hardy-style trailing date
                    trimmed.pop()
                else: break
            total=sum(len(b) for b in trimmed)
            if total==14:
                emit([l for b in trimmed for l in b],num,ttl,oy or cyear)
            elif trimmed and all(len(b)==14 for b in trimmed):
                for j,b in enumerate(trimmed): emit(b,(num+j) if num else None,ttl if j==0 else None,oy or cyear)
        hadpoem=bool(poem)
        poem=[]; num=None
        if hadpoem: ttl=None   # cyear persists: chronological edition
    for b in blocks(txt):
        first=b[0].strip()
        fkey=first.upper().rstrip(". :")
        if fkey in secs and len(b)<=5:
            close(); cur=secs[fkey]; capture=True; continue
        if len(b)==2 and re.match(r"^_?\d{1,3}$",first):
            close(); num=int(first.strip("_")); ttl=b[1].strip("_ "); continue
        if len(b)==1:
            m=SONN.match(first)
            if m:
                close(); g=m.group(1); num=int(g) if g.isdigit() else r2i(g); continue
            if ARABIC.match(first):
                _n=int(first.rstrip("."))
                _pre=len(recs); close()
                if 1500<=_n<=1930:
                    if len(recs)>_pre:  # a sonnet was just emitted: this is its dateline
                        recs[-1]["year"]=_n; recs[-1]["year_type"]="comp"
                    continue
                num=_n; continue
            if ROMAN.match(first): close(); num=r2i(first); continue
            cand=first.strip('_" ')
            if len(cand)<60 and cand and not cand.startswith(("[","*")) \
               and not re.search(r"--ED|FOOTNOTES|VARIANTS|Published|^One of",cand):
                had=ttl; close()
                ttl=cand if (had is None or poem) else had
                if had is not None and not poem: ttl=had if len(cand)>45 else cand
                continue
        mc=re.search(r"Composed[^\n]*?(1[678]\d\d)"," ".join(b))
        if mc and len(b)<=4:
            cyear=int(mc.group(1)); continue
        if verseish(b): poem.append(b)
        else: close()
    close(); return recs

def S(author,seq,year,**kw): d=dict(author=author,seq=seq,year=year,name=seq.upper()); d.update(kw); return d
CONFIGS=[
 dict(pg=1041,start="THE SONNETS",end="THE END",sections=[S("William Shakespeare","Sonnets",1609)]),
 dict(pg=56375,sections=[S("Sir Philip Sidney","Astrophel and Stella",1591,spelling="old")]),
 dict(pg=2002,sections=[S("Elizabeth Barrett Browning","Sonnets from the Portuguese",1850)]),
 dict(pg=18842,sections=[S("Samuel Daniel","Delia",1592),S("Henry Constable","Diana",1592)]),
 dict(pg=18841,sections=[S("Thomas Lodge","Phillis",1593),S("Giles Fletcher the Elder","Licia",1593)]),
 dict(pg=15448,sections=[S("Michael Drayton","Idea",1619),S("Bartholomew Griffin","Fidessa",1596),S("William Smith","Chloris",1596)]),
 dict(pg=48688,start="HOLY SONNETS.",end="_The Crosse._",sections=[S("John Donne","Holy Sonnets",1633)]),
 dict(pg=31706,start="SONNETS.",end="SONNETS.",sections=[S("John Milton","Sonnets",1645,use_titles=True)]),
 dict(pg=3692,sections=[S("Dante Gabriel Rossetti","The House of Life",1881,use_titles=True)]),
 dict(pg=22403,unwrap=True,sections=[S("Gerard Manley Hopkins","Poems (1918)",1918,use_titles=True)]),
 dict(pg=33902,sections=[S("Rupert Brooke","1914 and Other Poems",1915,use_titles=True)]),
 dict(pg=8209,sections=[S("John Keats","Poems (1817)",1817,use_titles=True)]),
 dict(pg=10602,start="AMORETTI.[*]",end="EPIGRAMS AND SONNETS.",
      sections=[S("Edmund Spenser","Amoretti",1595,spelling="old")]),
 dict(pg=10219,sections=[S("William Wordsworth","Sonnets",1800,use_titles=True,need_comp=True)]),
 dict(pg=12145,sections=[S("William Wordsworth","Sonnets",1807,use_titles=True,need_comp=True)]),
 dict(pg=12383,sections=[S("William Wordsworth","Sonnets",1815,use_titles=True,need_comp=True)]),
 dict(pg=32459,sections=[S("William Wordsworth","Sonnets",1820,use_titles=True,need_comp=True)]),
 dict(pg=56361,sections=[S("William Wordsworth","Sonnets",1825,use_titles=True,need_comp=True)]),
 dict(pg=52836,sections=[S("William Wordsworth","Sonnets",1845,use_titles=True,need_comp=True)]),
 dict(pg=47651,sections=[S("William Wordsworth","Sonnets",1820,use_titles=True,need_comp=True)]),
 dict(pg=47143,sections=[S("William Wordsworth","Sonnets",1835,use_titles=True,need_comp=True)]),
 dict(pg=18915,start="SONNETS, ETC.",end="MONODY",
      sections=[S("William Lisle Bowles","Sonnets",1789,use_titles=True)]),
 dict(pg=27663,sections=[S("Anna Seward","Original Sonnets",1799)]),
 dict(pg=29090,sections=[S("Samuel Taylor Coleridge","Sonnets",1796,yt="approx",use_titles=True)]),
 dict(pg=1365,sections=[S("Henry Wadsworth Longfellow","Sonnets",1873,yt="approx",use_titles=True)]),
 dict(pg=19188,start="MONNA INNOMINATA.",sections=[S("Christina Rossetti","Monna Innominata",1881),S("Christina Rossetti","Later Life",1881,name="LATER LIFE: A DOUBLE SONNET OF SONNETS."),S("Christina Rossetti","A Pageant volume",1881,use_titles=True,names=['A FISHER-WIFE', "A LIFE'S PARALLELS", 'A PROCESSIONAL OF CREATION', 'A PRODIGAL SON', 'AN OCTOBER GARDEN', 'AN OLD-WORLD THICKET', 'AT LAST', 'BOY JOHNNY', 'BRANDONS BOTH', 'BUDS AND BABIES', 'DE PROFUNDIS', 'DEATH-WATCHES', 'FLUTTERED WINGS', 'FOUNDED ON AN ANECDOTE OF THE FIRST FRENCH REVOLUTION', 'FREAKS OF FASHION', 'GOLDEN GLORIES', 'GOLDEN SILENCES', 'IN THE WILLOW SHADE', 'JOHNNY', 'MAIDEN MAY', 'MARIANA', 'MEMENTO MORI', 'PASSING AND GLASSING', 'SOEUR LOUISE DE LA MISERICORDE', 'TEMPUS FUGIT', 'THE THREAD OF LIFE', 'TILL TO-MORROW', "WHAT'S IN A NAME?"])]),
 dict(pg=16950,sections=[S("Christina Rossetti","Goblin Market volume",1862,use_titles=True)]),
 dict(pg=1034,sections=[S("Wilfred Owen","Poems (1920)",1917,yt="comp",use_titles=True)]),
 dict(pg=67791,sections=[S("Charles Hamilton Sorley","Marlborough",1915,yt="comp",use_titles=True)]),
 dict(pg=54985,sections=[S("Matthew Arnold","Sonnets",1855,yt="approx",use_titles=True)]),
 dict(pg=62251,sections=[S("Alice Meynell","Poems",1893,yt="approx",use_titles=True)]),
 dict(pg=4800,sections=[S("Percy Bysshe Shelley","Poems",1818,yt="approx",use_titles=True)]),
 dict(pg=109,sections=[S("Edna St. Vincent Millay","Renascence",1917,use_titles=True)]),
 dict(pg=1247,sections=[S("Edna St. Vincent Millay","Second April",1921,use_titles=True)]),
 dict(pg=59474,unwrap=3,sections=[S("Edna St. Vincent Millay","The Harp-Weaver",1923,use_titles=True)]),
 dict(pg=4399,sections=[S("Edna St. Vincent Millay","A Few Figs from Thistles",1920,use_titles=True)]),
 dict(pg=64989,sections=[S("Claude McKay","Harlem Shadows",1922,use_titles=True)]),
 dict(pg=6682,sections=[S("Elinor Wylie","Nets to Catch the Wind",1921,use_titles=True)]),
 dict(pg=313,sections=[S("Edwin Arlington Robinson","The Children of the Night",1897,use_titles=True)]),
 dict(pg=1035,sections=[S("Edwin Arlington Robinson","The Man Against the Sky",1916,use_titles=True)]),
 dict(pg=29345,sections=[S("Robert Frost","Mountain Interval",1916,use_titles=True)]),
 dict(pg=3021,sections=[S("Robert Frost","A Boy's Will",1913,use_titles=True)]),
 dict(pg=3167,sections=[S("Thomas Hardy","Wessex Poems",1898,use_titles=True)]),
 dict(pg=3295,sections=[S("Emma Lazarus","Poems I",1880,yt="approx",use_titles=True)]),
 dict(pg=3473,sections=[S("Emma Lazarus","Poems II",1880,yt="approx",use_titles=True)]),
 dict(pg=52601,sections=[S("John Clare","Poems (Symons selection)",1835,yt="approx",use_titles=True)]),
 dict(pg=70543,sections=[S("Countee Cullen","Color",1925,use_titles=True)]),
 dict(pg=39783,sections=[S("Ezra Pound","Canzoni & Ripostes",1912,use_titles=True)]),
 dict(pg=18338,sections=[S("Paul Laurence Dunbar","Complete Poems",1899,yt="approx",use_titles=True)]),
 dict(pg=1057,sections=[S("Oscar Wilde","Poems (1881)",1881,use_titles=True)]),
 dict(pg=32491,sections=[S("W. B. Yeats","The Wild Swans at Coole",1919,use_titles=True)]),
 dict(pg=72985,sections=[S("W. B. Yeats","The Tower",1928,use_titles=True)]),
]
def main():
    allr=[]
    for cfg in CONFIGS:
        p=RAW/f'{cfg["pg"]}.txt'
        rs=extract(p,cfg) if p.exists() else []
        by={}
        for r in rs: by[r["sequence"]]=by.get(r["sequence"],0)+1
        print(cfg["pg"], by)
        allr+=rs
    for i,r in enumerate(allr): r["id"]=f"s{i:05d}"
    OUT.joinpath("sonnets.json").write_text(json.dumps(allr,indent=1))
    print("TOTAL",len(allr))
if __name__=="__main__": main()
