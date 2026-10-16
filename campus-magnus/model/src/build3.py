import json,sys,math
sys.path.insert(0,sys.argv[1]); S=sys.argv[2]
import data_src as D
import bands_src as B
import pandas as pd
ALLOBS=[dict(o) for o in D.OBS]+[dict(o) for o in B.BOBS]
PINS=json.load(open(f'{sys.argv[2]}/build/pins.json',encoding='utf-8'))
for o in ALLOBS:
    if o['raw'] in PINS and ' p. ' not in o['src'] and ' pp. ' not in o['src']: o['src']=o['src']+', '+PINS[o['raw']]
for o in ALLOBS:
    if o.get('band'): continue
    for pre,dv,key in B.TAG:
        if key and o['g']==dv and o['raw'].startswith(pre): o['band']=key; break
Y0,Y1=1700,1905
gids=[g[0] for g in D.GROUPS]; G={g[0]:g for g in D.GROUPS}
groups=[dict(id=a,tribe=b,name=c,fam=d,start=e,end=f,life=h) for a,b,c,d,e,f,h in D.GROUPS]
groups+=[dict(id=a,tribe=b,name=c,fam='unident',start=1805,end=1805,life='') for a,b,c in D.UNIDENT]
obs=[]
for i,o in enumerate(ALLOBS):
    gg=o['g'] if isinstance(o['g'],list) else [o['g']]
    for x in gg: assert x in G or x.startswith('u_'),x
    obs.append(dict(i=i,g=gg,agg=len(gg)>1,y=o['y'],pop=o['pop'],raw=o['raw'],basis=o['basis'],loc=o['loc'],lat=o['at'][0],lon=o['at'][1],
                    r=o['r'],src=o['src'],kind=o['kind'],part=o.get('part',False) or bool(o.get('band')),whole=o.get('whole',True),band=(gg[0]+'.'+o['band']) if o.get('band') else None,seasonal=o.get('seasonal',False)))
EPIY={1778,1780,1781,1782,1816,1817,1837,1837.5,1838,1849.5,1870,1885}
def smooth(x): return 0.5-0.5*math.cos(math.pi*min(1,max(0,x)))
def surv(gid,t):
    v=1.0
    for s,e,lab,M,src,basis in D.EPI:
        f=M.get(gid)
        if f: v*=1-min(.97,f*float(__import__('os').environ.get('EPS','1')))*smooth((t-s)/(e-s))
    for y,g,f,lab,src in getattr(D,'SHIFTS',[]):
        if g==gid: v*=1-f*smooth((t-y+.5)/.5)
    return v
import seasonal as _SE
tracks={}; diag=[]; DOCP={}; DOCSK={}; GSP={}; FAMS={}; PA={}; POS={}; NOTES={}; SP={}; NY={}
SIG_GUESS=float(__import__('os').environ.get('SG','0.3'))
NOGUESS=__import__('os').environ.get('NOGUESS')
SD_INFL=1.25  # leave-one-out calibration (validate.py): widened, the 2-sd range holds 96% of withheld counts, the 1-sd range 80%
import re as _re
def lodge_adj(basis):
    d=float(__import__('os').environ.get('LD','0'))
    m=_re.search(r'(lodges|tipis|tents|families) × ([\d.]+)',basis or '')
    if not d or not m: return 1.0
    k=float(m.group(2)); return (k+d)/k
def family(o):
    s=o['src'];y=o['y']
    if o.get('basis')=='census' or (y>=1868 and any(k in s for k in ('Annual Report','Commissioner','Indian Office','ARCIA'))): return 'census'
    for key,f in (('Clark','clark'),('Morse','morse'),('Aboriginal Population','mooney1928'),('Mooney (1928)','mooney1928'),('Pike','pike'),
                  ('Henry','henry'),('Thompson','thompson'),('Umfreville','umfreville'),('Mackenzie','umfreville'),('Maximilian','maximilian'),
                  ('Catlin','catlin'),('Mézières','demezieres'),('Henday','hbcjournals'),('Cocking','hbcjournals'),('Vérendrye','verendrye'),('Denig','denig'),('Hayden','hayden'),('Stevens','stevens'),('Doty','stevens'),
                  ('Annual Report','agents'),('Commissioner','agents'),('Indian Office','agents'),('ARCIA','agents'),('Calendar History','mooney_kiowa'),
                  ('Swanton','swanton'),('Hodge','hodge'),('Grinnell','grinnell'),('Hämäläinen','reconstruction'),('Brooks','reconstruction')):
        if key in s: return f
    return 'other'
def sig_obs(o):
    if o['kind']=='secondary': return float(__import__('os').environ.get('SSEC','0.45'))
    if o.get('basis')=='census': return 0.15
    if o['y']>=1868: return 0.1 if any(k in o['raw'].lower() for k in ('census','roll','enrollment','numbered','number ')) else 0.15
    if 'Clark' in o['src']: return float(__import__('os').environ.get('SC','0.35'))
    return 0.3
DOCO={}
for gid in gids:
    g=G[gid]
    spec=[o for o in obs if not o['agg'] and o['g'][0]==gid]
    # ---- positions: documented stated places win; guesses within 1 yr of one are dropped
    pos={}
    by={}
    for o in spec:
        if o['loc']=='stated' and o['whole'] and not o['seasonal'] and (not o['part'] or all(x['loc']=='stated' for x in spec if x['y']==o['y'] and x['pop'] and x['whole'])): by.setdefault(o['y'],[]).append(o)
    docy=[]
    for y,L in by.items():
        w=[o for o in L if o['pop']] or L
        tw=sum((o['pop'] or 1) for o in w)
        pos[y]=[y,sum(o['lat']*(o['pop'] or 1) for o in w)/tw,sum(o['lon']*(o['pop'] or 1) for o in w)/tw,'o']; docy.append(y)
    notes=[]
    for (y,pl,pp,note) in D.GUESS.get(gid,[]):
        if note and not (pl is None and y in EPIY): notes.append([y,note])
        if pl and not any(abs(y-d)<1.0 for d in docy): pos[y]=[y,pl[0],pl[1],'g']
    P=sorted(pos.values())
    # ---- population anchors (log-space, weighted); fitted below jointly
    PA[gid]=[]
    byy={}
    for o in spec:
        if o['pop'] and o['whole']: byy.setdefault(o['y'],[]).append(o)
    for y,L in byy.items():
        tot=sum(o['pop']*(lodge_adj(o['basis'])) for o in L)
        PA[gid].append((y,tot,sig_obs(L[0]),'o')); FAMS.setdefault(gid,[]).append(family(L[0]))
    for (y,pl,pp,note) in D.GUESS.get(gid,[]):
        if pp and not NOGUESS and not (pl is None and y in EPIY): PA[gid].append((y,pp,SIG_GUESS,'g'))
    POS[gid]=P; NOTES[gid]=notes
    _dl=[o for o in spec if o['loc']=='stated' and o['whole'] and not o['seasonal'] and (not o['part'] or all(x['loc']=='stated' for x in spec if x['y']==o['y'] and x['pop'] and x['whole']))]
    DOCP[gid]=[(o['y'],o['lat'],o['lon'],o['r'] or 25) for o in _dl]
    DOCO[gid]=_dl
    DOCSK[gid]=[_SE.season_known(o['y'],o['raw'],o['r']) for o in _dl]
    GSP[gid]=[(p[0],p[1],p[2]) for p in P if p[3]=='g']
    places=[o for o in spec if o['loc']=='stated' and not o['seasonal'] and (not o['part'] or all(x['loc']=='stated' for x in spec if x['y']==o['y'] and x['pop'] and x['whole']))]
    NY[gid]=[round(min(99,min([abs(t-o['y']) for o in places]+[99])),2) for t in range(Y0,Y1+1)]

# ================= joint demographic fit =================
import numpy as np
T=np.arange(Y0,Y1+1,1.0); n=len(T)
SIG_SMOOTH=float(__import__('os').environ.get('SS','0.02'))#    # allowed change in annual growth rate per year (log units)
SIG_R=float(__import__('os').environ.get('SR','0.06')); R0=float(__import__('os').environ.get('R0','0.005'))  # weak prior: underlying growth near +0.5%/yr between shocks
def shock(gid): return np.array([math.log(surv(gid,t)) for t in T])
D1=np.zeros((n-1,n))
for k in range(n-1): D1[k,k]=-1;D1[k,k+1]=1
D2=np.zeros((n-2,n))
for k in range(n-2): D2[k,k]=1;D2[k,k+1]=-2;D2[k,k+2]=1
def fit(gid,extra):
    lsv=shock(gid); rows=[];rhs=[];w=[]
    for (y,p,sg,src) in PA[gid]+extra:
        # linear interpolation weights on the annual grid
        y=min(max(y,Y0),Y1); k=min(int(y-Y0),n-2); f=y-Y0-k
        r=np.zeros(n); r[k]=1-f; r[k+1]=f
        rows.append(r); rhs.append(math.log(p)-((1-f)*lsv[k]+f*lsv[k+1])); w.append(1/sg)
    if not rows: return np.full(n,np.nan),np.full(n,9.0)
    A=np.array(rows)*np.array(w)[:,None]; b=np.array(rhs)*np.array(w)
    M=A.T@A+(D2.T@D2)/SIG_SMOOTH**2+(D1.T@D1)/SIG_R**2
    x=np.linalg.solve(M+1e-9*np.eye(n),A.T@b+(D1.T@np.full(n-1,R0))/SIG_R**2)
    var=np.diag(np.linalg.inv(M+1e-9*np.eye(n)))
    return x+lsv,np.sqrt(var)
aggs=[o for o in obs if o['agg'] and o['pop'] and all(x in G for x in o['g'])]
for o in aggs: o['fam']=family(o); o['pop0']=o['pop']
def run_fit():
    global FIT,extra
    extra={g:[] for g in gids}
    for it in range(4):
        FIT={g:fit(g,extra[g]) for g in gids}
        extra={g:[] for g in gids}
        for o in aggs:
            k=int(round(o['y']-Y0)); members=[x for x in o['g'] if G[x][4]<=o['y']<=G[x][5]]
            if not members: continue
            members=[x for x in members if not math.isnan(FIT[x][0][k])]
            if not members: continue
            tot=sum(math.exp(FIT[x][0][k]) for x in members); ratio=o['pop']/tot
            for x in members: extra[x].append((o['y'],math.exp(FIT[x][0][k])*ratio,sig_obs(o)*1.6,'a'))
    FIT={g:fit(g,extra[g]) for g in gids}
run_fit()
# ---- source-family bias: each family of sources (Clark, Morse, Mooney's 1928 reconstructions…) may run high or low as a whole.
# Estimated against the fit with a shrinkage prior (tau, log units); the reservation censuses are the fixed reference.
BIAS={}; BIAS_N={}; BIAS_ND={}; RC={}
TAU=float(__import__('os').environ.get('BT','0.25'))
BIAS_G=__import__('os').environ.get('BIASG','0')=='1'   # compare against documented counts only, never our own anchors
PA0={g:list(v) for g,v in PA.items()}
if __import__('os').environ.get('BIAS','1')!='0':
    # leave-one-family-out: refit without family f, then compare f's counts with that fit where it is well supported
    fams=sorted({f for v in FAMS.values() for f in v}|{o['fam'] for o in aggs})
    aggs_all=list(aggs)
    for f in fams:
        if f=='census': continue
        for gid in gids:
            fs=FAMS.get(gid,[]); it_=iter(fs)
            PA[gid]=[a for a in PA0[gid] if (a[3]=='o' and next(it_)!=f) or (a[3]!='o' and BIAS_G)]
        aggs[:]=[o for o in aggs_all if o['fam']!=f]
        run_fit()
        num=den=0.0; c=0
        for gid in gids:
            lp,sd=FIT[gid]
            if math.isnan(lp[0]): continue
            for (y,p,sg,src),ff in zip([a for a in PA0[gid] if a[3]=='o'],FAMS.get(gid,[])):
                if ff!=f: continue
                s_=float(np.interp(y,T,sd))
                if s_>0.35: continue
                w=1/(sg**2+s_**2); rr=math.log(p)-float(np.interp(y,T,lp)); num+=w*rr; den+=w; c+=1; RC[(gid,y)]=(w,rr)
        for o in aggs_all:
            if o['fam']!=f: continue
            k=int(round(o['y']-Y0)); mem=[x for x in o['g'] if G[x][4]<=o['y']<=G[x][5] and not math.isnan(FIT[x][0][k])]
            if not mem or max(FIT[x][1][k] for x in mem)>0.35: continue
            w=1/((sig_obs(o)*1.6)**2+0.1**2); num+=w*(math.log(o['pop0'])-math.log(sum(math.exp(FIT[x][0][k]) for x in mem))); den+=w; c+=1
        BIAS[f]=num/(den+1/TAU**2); BIAS_N[f]=c; BIAS_ND[f]=(num,den)
    BIAS['census']=0.0
    aggs[:]=aggs_all
    for gid in gids:
        it_=iter(FAMS.get(gid,[]))
        PA[gid]=[(y,p*math.exp(-BIAS.get(next(it_),0)),sg,src) if src=='o' else (y,p,sg,src) for (y,p,sg,src) in PA0[gid]]
    for o in aggs: o['pop']=o['pop0']*math.exp(-BIAS.get(o['fam'],0))
    run_fit()
FIT_RAW=dict(FIT)
FIT={g:((v[0],v[1]) if not math.isnan(v[0][0]) else (np.zeros(n),np.full(n,.9))) for g,v in FIT.items()}
# ================= positions: estimated tracks =================
# Nomadic divisions: a Gaussian-process centre (possgp.py) whose settings and halo scale are fitted by hold-out (calib_gp.py).
# Village divisions: hold at each place and move over two years at the midpoint to the next (villages move by relocation, not drift);
# the halo is 24 km plus 1.25 times the distance to the next place times the share of the gap elapsed (calib_vhalo.py).
import possmooth as _PS
import ecology_src as _EC
DENSE={}; SVS={}; MOVES={}
_PC=f'{S}/build/profcal.json'
_SE.PROF=tuple(json.load(open(_PC))['best']) if __import__('os').path.exists(_PC) else None   # seasonal calendar, used for the bands' scatter and the village hunts
import possgp as _GP
GPTH,GPCAL=_GP.load_cal(f'{S}/build/gpcal.json')   # settings fitted by hold-out (calib_gp.py)
SH={}
GPM=_GP.moments([p for g_ in gids if G[g_][6]!='village' for p in (_GP.prepare(g_,DOCO[g_],GSP[g_]) or {'pts':[]})['pts']])   # season-of-record distribution
def _km(a,b):
    la=math.radians((a[0]+b[0])/2); return math.hypot((a[0]-b[0])*111,(a[1]-b[1])*111*math.cos(la))
for gid in gids:
    g=G[gid]; y0,y1=g[4],g[5]; docs=DOCP[gid]; gs=GSP[gid]
    if g[6]=='village':
        byy={}
        for (y,la,lo,r) in docs: byy.setdefault(y,[]).append((la,lo))
        pts=sorted([(y,sum(p[0] for p in L)/len(L),sum(p[1] for p in L)/len(L),'o') for y,L in byy.items()]+[(y,la,lo,'g') for (y,la,lo) in gs])
        dense=[]
        for i,p in enumerate(pts):
            dense.append(p)
            if i+1<len(pts):
                q_=pts[i+1]; gap=q_[0]-p[0]
                mv=[m for (m,_,_) in _EC.VMOVE.get(gid,[]) if p[0]<m<q_[0]+0.3]
                if mv and _km(p[1:3],q_[1:3])>3:      # a dated relocation: hold, then move over about five months
                    m=mv[0]; b_=min(q_[0],m+0.2); a_=min(m-0.2,b_-0.2)
                    if a_>p[0]: dense.append((a_,p[1],p[2],'h'))
                    if b_<q_[0]: dense.append((b_,q_[1],q_[2],'h'))
                    MOVES.setdefault(gid,[]).append(m)
                elif gap>2.2 and _km(p[1:3],q_[1:3])>3:
                    mid=(p[0]+q_[0])/2; dense.append((mid-1,p[1],p[2],'h')); dense.append((mid+1,q_[1],q_[2],'h'))
        DENSE[gid]=[[round(p[0],3),round(p[1],4),round(p[2],4),p[3]] for p in dense]
        sp=[]
        for t in range(Y0,Y1+1):
            lo=[p for p in pts if p[0]<=t]; hi=[p for p in pts if p[0]>t]
            if lo and hi:
                a_,b_=lo[-1],hi[0]; dm=[m for m in MOVES.get(gid,[]) if a_[0]<m<b_[0]+0.3]
                if dm: u=0.5*max(0.0,1-abs(t-dm[0]))      # dated move: the place is known on either side of it
                else: u=min(t-a_[0],b_[0]-t)/(b_[0]-a_[0])
                v=24+1.25*_km(a_[1:3],b_[1:3])*u      # fitted by hold-out (calib_vhalo.py): holds 68% of withheld village places
            else: v=24
            sp.append(round(min(300,v)))
        SP[gid]=sp
    else:
        # nomadic: the Gaussian-process position (possgp.py), a smooth annual centre plus a learned seasonal component
        div=_GP.prepare(gid,DOCO[gid],gs)
        f=_GP.Fit(div,GPTH,GPM); lat0,lon0=div['lat0'],div['lon0']
        yrs=list(range(int(math.floor(y0)),int(math.ceil(y1))+1))
        dp=[]
        for t in yrs:
            m,v=f.trend(t); la,lo=_PS.unlocal(lat0,lon0,float(m[0]),float(m[1])); dp.append([t,round(la,4),round(lo,4),'f'])
        DENSE[gid]=dp
        dt_=[p['t'] for p in div['pts'] if p['s']=='dated']
        SH[gid]=[[int(round(c)) for c in f.harmonics(t)] for t in range(Y0,Y1+1)]
        SVS[gid]=''.join(('d' if any(abs(t-u)<=GPTH['lS'] for u in dt_) else ('p' if _SE.prior_A(gid,t,lat0,lon0)[1] else '0')) for t in range(Y0,Y1+1))
        SP[gid]=[round(min(450,1.51*math.sqrt(f.trend(min(max(t,y0),y1))[1]))) for t in range(Y0,Y1+1)]
ZS=[]
for gid in gids:
    lp,sd=FIT[gid]
    res=[(y,p,src,round((math.log(p)-np.interp(y,T,lp))/sg,1)) for (y,p,sg,src) in PA[gid]]
    bad=[r for r in res if abs(r[3])>2]
    ZS.extend([abs(r[3]) for r in res if r[2]=='o'])
    if bad and __import__('os').environ.get('V'): print('misfit',gid,bad)
    tracks[gid]=dict(pos=DENSE[gid],nk=len(POS[gid]),
        pa=[max(5,int(round(math.exp(v)))) for v in lp],sd=[round(min(.9,v*SD_INFL)*100) for v in sd],
        anc=[[y,p,src] for (y,p,sg,src) in PA[gid]],notes=NOTES[gid],sp=SP[gid],ny=NY[gid],**({'sh':SH[gid],'svs':SVS[gid]} if gid in SH and any(any(c) for c in SH[gid]) else {}))
import statistics as _st
print('SS',SIG_SMOOTH,'SR',SIG_R,'median|z|',round(_st.median(ZS),2),'>2:',sum(z>2 for z in ZS),'of',len(ZS))
d=pd.read_csv(f'{S}/geo/cities.csv',encoding='latin-1')
d=d[(d.LON>-117)&(d.LON<-87.5)&(d.LAT>26)&(d.LAT<50)]
cols=[str(y) for y in range(1790,1910,10)]
d=d[(d[cols]>0).any(axis=1)]
cities=[[r.City+', '+r.ST,round(r.LAT,3),round(r.LON,3),[int(r[c]) for c in cols]] for _,r in d.iterrows()]
# ================= bands: internal structure of each division =================
def clamp(v,a=0.0,b=1.0): return a if v<a else b if v>b else v
def rng(t,s,e,r):
    a=1.0
    if s is not None: a=min(a,clamp((t-s)/r))
    if e is not None: a=min(a,clamp((e-t)/r))
    return a
def popd(gid,t):
    lp=FIT[gid][0]; return math.exp(np.interp(t,T,lp))
BSPEC={}
for gid in gids:
    g=G[gid]; L=B.LISTS.get(gid); named=[x for x in B.BANDS if x['div']==gid]
    if not L and not named: continue
    L=L or {}
    village=('village' in g[6] and '→' not in g[6]) or ('gap' in L)
    Ly=min(max(L.get('y',1850),g[4]),g[5])
    units=[]
    for x in named:
        u=dict(id=gid+'.'+x['key'],key=x['key'],name=x['name'],gloss=x.get('gloss',''),w=x.get('w',1.0),start=x.get('start'),end=x.get('end'),
               into=(gid+'.'+x['into']) if x.get('into') else None,kind=x.get('kind','village' if village else 'band'),chief=x.get('chief1856'),note=x.get('note',''),
               track=[[t[0],t[1][0],t[1][1],t[2]] for t in x.get('track',[])],tdoc=x.get('tdoc',False),tchk=x.get('tchk',''),shocks=[])
        units.append(u)
    ids={u['id'] for u in units}
    for u in units: assert u['into'] is None or u['into'] in ids,(u['id'],u['into'])
    gen=L.get('gen') or ('unnamed village' if village else 'unnamed band')
    genonly=not any(u['kind']!='following' for u in units)
    wLy=sum(u['w'] for u in units if u['kind']!='following' and rng(Ly,u['start'],u['end'],1.5)>0.5)
    Sx=L.get('S') or (popd(gid,Ly)/wLy if wLy else (600 if village else 250))
    maxgen=B.MAXGEN.get(gid,25)
    BSPEC[gid]=dict(S=round(Sx,1),Ly=Ly,gen=gen,maxgen=maxgen,village=village,gap=L.get('gap',5),genonly=genonly,
                    src=L.get('src',''),note=L.get('note',''),units=units)
for (y,dv,key,lo,hi,camp,lab) in B.BSHOCK:
    u=[u for u in BSPEC[dv]['units'] if u['key']==key][0]; u['shocks'].append([y,round(min(.9,(lo+hi)/2/camp),3),0.05,lab+f': {lo}–{hi} killed in a camp of about {camp} (recalled; camp size ours)'])
for (y,dv,M,src) in B.BEPI:
    fdiv=[e for e in D.EPI if abs(e[0]-y)<.01][0][3].get(dv,0)
    for key,f in M.items():
        u=[u for u in BSPEC[dv]['units'] if u['key']==key][0]; u['shocks'].append([y+0.2,round(1-(1-f)/(1-fdiv),3),0.4,src])
def shock_factor(u,t):
    v=1.0
    for y,f,r,_ in u['shocks']: v*=1-f*clamp((t-y)/r)
    return v
def acts(sp,t,pop):
    K=pop/sp['S']; pre=sp['genonly'] or t<sp['Ly']; used=0.0; anyon=False; out=[]
    for u in sp['units']:
        if u['kind']=='following':
            r=min(0.15,(u['end']-u['start'])/4); out.append(rng(t,u['start'],u['end'],r)); continue
        a=rng(t,u['start'],u['end'],1.5)
        if a>0 and pre:
            cap=1.0 if not anyon else clamp((K-used)/u['w']+0.5)
            a=min(a,cap); used+=u['w']*a
        if a>0: anyon=True
        out.append(a)
    gens=[]
    if pre:
        rem=K-used
        for k in range(sp['maxgen']):
            a=clamp(rem-k)
            if k==0 and not anyon: a=1.0
            if a<=0: break
            gens.append(a)
    return out,gens
def mult(u,t):
    m=u.get('_m')
    if m is None: return 1.0
    return float(np.interp(t,T,m))
def shares(gid,t,withm=True):
    sp=BSPEC[gid]; pop=popd(gid,t); a,gs=acts(sp,t,pop)
    raw=[u['w']*ai*(mult(u,t) if withm else 1)*shock_factor(u,t) for u,ai in zip(sp['units'],a)]+list(gs)
    tot=sum(raw) or 1
    return [r/tot for r in raw],a,gs,pop
# documented band counts -> share multipliers decaying with a 20-year scale
BTAU=20.0
brec={}
for o in obs:
    if o['band'] and o['pop'] and o['g'][0] in BSPEC: brec.setdefault(o['band'],[]).append(o)
for it in range(4):
    for bid,recs in brec.items():
        gid=bid.split('.')[0]; sp=BSPEC[gid]; k=[u['id'] for u in sp['units']].index(bid); u=sp['units'][k]
        if '_r' not in u: u['_r']={}
        for o in recs:
            sh=shares(gid,o['y'])[0][k]; model=popd(gid,o['y'])*sh
            # records of the same band and year are summed (parts of one band)
            tgt=sum(x['pop'] for x in recs if x['y']==o['y'])
            prev=u['_r'].get(o['y'],1.0)
            u['_r'][o['y']]=clamp(prev*(tgt/max(model,1))**0.8,0.2,5.0)
        ys=sorted(u['_r']); lr=[math.log(u['_r'][y]) for y in ys]
        m=[]
        for t in T:
            kk=[math.exp(-abs(t-y)/BTAU) for y in ys]
            m.append(math.exp(sum(a*b for a,b in zip(kk,lr))/sum(kk)*max(kk)))
        u['_m']=np.array(m)
if __import__('os').environ.get('V'):
    for bid,recs in brec.items():
        gid=bid.split('.')[0]; sp=BSPEC[gid]; k=[u['id'] for u in sp['units']].index(bid)
        for o in recs: print(' bandfit',bid,o['y'],o['pop'],round(popd(gid,o['y'])*shares(gid,o['y'])[0][k]))
BANDROWS=[]
for gid,sp in BSPEC.items():
    g=G[gid]
    for u in sp['units']:
        if '_m' in u: u['mult']=[round(float(v),3) for v in u['_m']]
        u['shocks']=[s[:3]+[s[3]] for s in u['shocks']]
    # stacked shares for the panel chart and CSV: annual
    for t in range(max(Y0,g[4]),min(Y1,g[5])+1):
        sh,a,gs,pop=shares(gid,t)
        for k,u in enumerate(sp['units']):
            if a[k]>0: BANDROWS.append((gid,u['id'],u['name'],u['kind'],t,round(pop*sh[k])))
        for j in range(len(gs)): BANDROWS.append((gid,f'{gid}#{j+1}',sp['gen'],'unnamed',t,round(pop*sh[len(sp['units'])+j])))
    for u in sp['units']:
        u.pop('_m',None); u.pop('_r',None)
nb=sum(len(sp['units']) for sp in BSPEC.values())
print('bands: divisions',len(BSPEC),'named units',nb,'band records',len(brec))

epi=[dict(s=s,e=e,label=lab,m=M,src=src,basis=basis) for s,e,lab,M,src,basis in D.EPI]
FAMLAB={'clark':'Clark, 1804–06','henry':'Henry the younger, 1809','thompson':'Thompson, 1798','pike':'Pike, 1806','morse':'Morse, 1820','umfreville':'Umfreville & Mackenzie, 1789–1801','maximilian':'Maximilian, 1833','catlin':'Catlin, 1832–34','denig':'Denig, 1833–56','hayden':'Hayden, 1862','stevens':'Stevens & Doty, 1853–55','agents':'Indian Office before 1868','mooney1928':'Mooney’s 1928 reconstructions','mooney_kiowa':'Mooney, Kiowa calendar','swanton':'Swanton’s series','hodge':'Hodge’s Handbook','grinnell':'Grinnell','reconstruction':'modern reconstructions','other':'other sources','census':'Indian Office, 1868 on (reference)','demezieres':'De Mézières, 1770–79','hbcjournals':'Henday and Cocking, 1754–73','verendrye':'La Vérendrye, 1733–43'}
for o in aggs: o['pop']=o['pop0']   # documented value, not the corrected one used in fitting
for o in obs: o['fam']=family(o); o['famf']=round(math.exp(BIAS.get(o['fam'],0)),2)
BIASOUT=[[FAMLAB.get(f,f),BIAS_N.get(f,0),round(math.exp(b),2)] for f,b in sorted(BIAS.items(),key=lambda x:x[1]) if f!='census' and BIAS_N.get(f,0)>0]
SEASOUT={g:[[a,b_,('' if spec[0]=='vec' else 'winter ground %.2f°N %.2f°W, summer ground %.2f°N %.2f°W'%(spec[1][0],-spec[1][1],spec[2][0],-spec[2][1])),src] for (a,b_,spec,src) in L] for g,L in _SE.SEASPRI.items()}
for g,L in SEASOUT.items():
    for r_,(a,b_,spec,src) in zip(L,_SE.SEASPRI[g]):
        if spec[0]=='vec': r_[2]=f'summer ground about {2*spec[2]} km {["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"][int((spec[1]+11.25)%360//22.5)]} of the winter ground'
VMOUT={g:[[m,t_,s_] for (m,t_,s_) in L] for g,L in _EC.VMOVE.items()}
out=dict(roam=GPCAL.get('roam',{'winter':85,'between':65,'summer':71}),res=_GP.RES,prof=list(_SE.PROF) if _SE.PROF else None,bias=BIASOUT,seaspri=SEASOUT,vmove=VMOUT,fam=D.FAM,famname=D.FAMNAME,groups=groups,obs=obs,tracks=tracks,cities=cities,settle=[list(s) for s in D.SETTLE],epi=epi,Y0=Y0,bands=BSPEC,struct=B.STRUCT,sensitivity=(json.load(open(f'{S}/build/sensitivity.json')) if __import__('os').path.exists(f'{S}/build/sensitivity.json') else None),validation=(json.load(open(f'{S}/build/validation.json')) if __import__('os').path.exists(f'{S}/build/validation.json') else None))
if not __import__('os').environ.get('SENS'): json.dump(out,open(f'{S}/build/data.json','w'),ensure_ascii=False,separators=(',',':'))
if not __import__('os').environ.get('SENS'): json.dump(BANDROWS,open(f'{S}/build/bandrows.json','w'),ensure_ascii=False)
print('obs',len(obs),'primary',sum(o['kind']=='primary' for o in obs),'placeonly',sum(o['pop'] is None for o in obs),'bytes',len(json.dumps(out,ensure_ascii=False,separators=(',',':'))))
