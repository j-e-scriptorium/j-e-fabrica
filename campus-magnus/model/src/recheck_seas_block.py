# Seasonal round, block hold-out: each season-dated place is withheld together with every other place within half a year
# (as calib_track.py does for the track), so the test asks how well a division is placed in a season with no record nearby.
# Prints the median and mean miss with the seasonal move and without it, under this protocol and plain leave-one-out.
#   python3 recheck_seas_block.py . ..      (several minutes; set NP for the number of processes)
import sys,os,runpy,io,contextlib,math,statistics as st
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import possmooth as PS, seasonal as SE, numpy as np
G,DOCP,DOCSK,GSP,POSP,SEAS=B['G'],B['DOCP'],B['DOCSK'],B['GSP'],B['POSP'],B['SEAS']
BW=0.5
CASES={}
for g in DOCP:
    if 'nomadic' not in G[g][6] or not any(DOCSK[g]) or len(DOCP[g])<3: continue
    pts=DOCP[g]+[(y,la,lo,None) for (y,la,lo) in GSP[g]]
    lat0=st.mean(p[1] for p in pts); lon0=st.mean(p[2] for p in pts)
    docs=[(y,)+PS.local(lat0,lon0,la,lo)+(r,sk) for (y,la,lo,r),sk in zip(DOCP[g],DOCSK[g])]
    CASES[g]=(docs,[(y,)+PS.local(lat0,lon0,la,lo) for (y,la,lo) in GSP[g]],lat0,lon0)
def resid(docs,gs,y0,y1,skip):
    R=[]
    for j,d in enumerate(docs):
        if not d[4] or j in skip: continue
        ob=[(t,x,y,(POSP['k']*r)**2+POSP['s0']**2) for i,(t,x,y,r,s) in enumerate(docs) if i!=j and i not in skip]+[(t,x,y,POSP['sg']**2) for (t,x,y) in gs]
        T,ms,Ps=PS.smooth(y0,y1,ob,POSP['q']); m,v=PS.predict_at(T,ms,Ps,d[0])
        R.append((d[0],SE.phi(d[0]),d[1]-m[0],d[2]-m[1],v+(POSP['k']*d[3])**2+POSP['s0']**2))
    return R
def hermpts(docs,gs,skip,Af=None):
    by={}
    for i,(t,x,y,r,s) in enumerate(docs):
        if i in skip: continue
        if s and Af is not None: a=Af(t);p=SE.phi(t);x,y=x-p*a[0],y-p*a[1]
        by.setdefault(t,[]).append((x,y))
    P=[(t,sum(v[0] for v in L)/len(L),sum(v[1] for v in L)/len(L)) for t,L in by.items()]
    return sorted(P+[(t,x,y) for (t,x,y) in gs if not any(abs(t-d)<1 for d in by)])
def work(g):
    docs,gs,lat0,lon0=CASES[g]; y0,y1=G[g][4],G[g][5]; years=np.arange(int(y0),int(y1)+1); out=[]
    for proto in ('loo','block'):
        for i,d in enumerate(docs):
            if not d[4]: continue
            sk={i} if proto=='loo' else {k for k,e in enumerate(docs) if abs(e[0]-d[0])<=BW}
            P0=hermpts(docs,gs,sk)
            if len(P0)<2: continue
            bx,by=SE.herm(P0,d[0])
            Am,_=SE.estimate(resid(docs,gs,y0,y1,sk),years,SEAS['tau'],SEAS['sigA'],SEAS['sigN'],g,lat0,lon0)
            Af=SE.Afun_of(years,Am); nx,ny=SE.herm(hermpts(docs,gs,sk,Af),d[0]); a=Af(d[0]); p=SE.phi(d[0])
            out.append((proto,math.hypot(d[1]-bx,d[2]-by),math.hypot(d[1]-nx-p*a[0],d[2]-ny-p*a[1])))
    return out
if __name__=='__main__':
    from multiprocessing import Pool
    with Pool(int(os.environ.get('NP','3'))) as pool: E=[e for L in pool.map(work,sorted(CASES,key=lambda g:-len(CASES[g][0]))) for e in L]
    for proto in ('loo','block'):
        b=[x[1] for x in E if x[0]==proto]; s=[x[2] for x in E if x[0]==proto]
        print(proto,'places',len(b),'| no seasonal move: median %.0f km, mean %.0f'%(st.median(b),st.mean(b)),'| seasonal: median %.0f km, mean %.0f'%(st.median(s),st.mean(s)))
