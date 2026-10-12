# Hold-out test of the seasonal model: drop each place dated to a season, predict it from everything else.
import sys,runpy,io,contextlib,os,math,json,statistics as st,itertools,pickle
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import possmooth as PS, seasonal as SE, numpy as np
G,DOCP,DOCSK,GSP,POSP=B['G'],B['DOCP'],B['DOCSK'],B['GSP'],B['POSP']
def fnv(s):
    h=2166136261
    for ch in s: h^=ord(ch); h=(h*16777619)&0xffffffff
    return h/4294967295
CASES={}
for g in DOCP:
    if 'nomadic' not in G[g][6] or not any(DOCSK[g]) or len(DOCP[g])<3: continue
    pts=DOCP[g]+[(y,la,lo,None) for (y,la,lo) in GSP[g]]
    lat0=st.mean(p[1] for p in pts); lon0=st.mean(p[2] for p in pts)
    docs=[(y,)+PS.local(lat0,lon0,la,lo)+(r,sk) for (y,la,lo,r),sk in zip(DOCP[g],DOCSK[g])]
    gs=[(y,)+PS.local(lat0,lon0,la,lo) for (y,la,lo) in GSP[g]]
    CASES[g]=(docs,gs,lat0,lon0)
def hermpts(docs,gs,Af=None,skip=None):
    by={}
    for i,(t,x,y,r,s) in enumerate(docs):
        if i==skip: continue
        if s and Af is not None: a=Af(t);p=SE.phi(t);x,y=x-p*a[0],y-p*a[1]
        by.setdefault(t,[]).append((x,y))
    P=[(t,sum(v[0] for v in L)/len(L),sum(v[1] for v in L)/len(L)) for t,L in by.items()]
    P+=[(t,x,y) for (t,x,y) in gs if not any(abs(t-d)<1 for d in by)]
    return sorted(P)
CACHE='../build/seas_R.pkl'
if os.path.exists(CACHE): RC=pickle.load(open(CACHE,'rb'))
else:
    RC={}
    for g,(docs,gs,lat0,lon0) in CASES.items():
        y0,y1=G[g][4],G[g][5]
        for i,d in enumerate(docs):
            if d[4]: RC[(g,i)]=SE.residuals(docs,gs,y0,y1,POSP,None,i)
        print('R',g,flush=True)
    pickle.dump(RC,open(CACHE,'wb'))
def run(tau,sigA,sigN,use_prior=True,detail=False):
    E={'base':[],'old':[],'new':[]}; per={}
    for g,(docs,gs,lat0,lon0) in CASES.items():
        y0,y1=G[g][4],G[g][5]; years=np.arange(int(y0),int(y1)+1)
        for i,d in enumerate(docs):
            if not d[4]: continue
            t,x,y=d[0],d[1],d[2]
            P0=hermpts(docs,gs,None,i)
            if len(P0)<2: continue
            bx,by=SE.herm(P0,t); E['base'].append(math.hypot(x-bx,y-by))
            ny=min([abs(t-o[0]) for j,o in enumerate(docs) if j!=i]+[99]); damp=min(1,max(0,(ny-1)/4.3))
            th=fnv(g)*6.283; A=100*damp*SE.phi(t); E['old'].append(math.hypot(x-bx-A*math.cos(th),y-by-A*math.sin(th)))
            if use_prior: Am,_=SE.estimate(RC[(g,i)],years,tau,sigA,sigN,g,lat0,lon0)
            else: Am,_=SE.estimate(RC[(g,i)],years,tau,1e6,sigN,g,lat0,lon0) if False else SE.estimate(RC[(g,i)],years,tau,sigN,sigN,'none',lat0,lon0)
            Af=SE.Afun_of(years,Am); P1=hermpts(docs,gs,Af,i); nx,nyy=SE.herm(P1,t); a=Af(t); p=SE.phi(t)
            e=math.hypot(x-nx-p*a[0],y-nyy-p*a[1]); E['new'].append(e)
            per.setdefault(g,[]).append((E['base'][-1],E['old'][-1],e))
    out={k:(round(st.median(v)),round(st.mean(v)),len(v)) for k,v in E.items()}
    if detail: return out,per
    return out
if __name__=='__main__':
    print('cases',sum(len([d for d in c[0] if d[4]]) for c in CASES.values()))
    res=[]
    for tau,sigA,sigN in itertools.product([5,10,20,40],[30,60,100],[15,30,60]):
        r=run(tau,sigA,sigN); res.append((r['new'][1],r['new'][0],tau,sigA,sigN)); print(tau,sigA,sigN,r,flush=True)
    best=min(res); print('best',best)
    tau,sigA,sigN=best[2:]
    r,per=run(tau,sigA,sigN,detail=True); rn=run(tau,sigA,sigN,use_prior=False)
    print('final',r,'no literature prior',rn)
    for g,L in per.items(): print(g,len(L),[round(st.median([x[k] for x in L])) for k in range(3)])
    json.dump(dict(tau=tau,sigA=sigA,sigN=sigN,res=r,noprior=rn,per={g:[len(L)]+[round(st.median([x[k] for x in L])) for k in range(3)] for g,L in per.items()}),open('../build/seascal.json','w'),indent=1)
