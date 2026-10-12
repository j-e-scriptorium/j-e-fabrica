# Partial pooling of the seasonal move across divisions of the same people: hold-out test.
import sys,json,math,pickle,os
sys.argv=['x']
exec(open('calib_prof.py').read().rsplit("if __name__=='__main__':",1)[0])
SE.PROF=tuple(json.load(open('../build/profcal.json'))['best'])
RF='../build/seas_Rfull.pkl'
if os.path.exists(RF): RFULL=pickle.load(open(RF,'rb'))
else:
    RFULL={}
    for g in DOCP:
        if 'nomadic' not in G[g][6] or not any(DOCSK[g]) or len(DOCP[g])<2: continue
        pts=DOCP[g]+[(y,la,lo,None) for (y,la,lo) in GSP[g]]
        lat0=st.mean(p[1] for p in pts); lon0=st.mean(p[2] for p in pts)
        docs=[(y,)+PS.local(lat0,lon0,la,lo)+(r,sk) for (y,la,lo,r),sk in zip(DOCP[g],DOCSK[g])]
        gs=[(y,)+PS.local(lat0,lon0,la,lo) for (y,la,lo) in GSP[g]]
        RFULL[g]=SE.residuals(docs,gs,G[g][4],G[g][5],POSP,None,None)
    pickle.dump(RFULL,open(RF,'wb'))
def sib(g): return [h for h in RFULL if h!=g and G[h][1]==G[g][1]]
def run3(lam,tau=5,sigA=60,sigN=60,only=None):
    E=[];per={}
    for g,(docs,gs,lat0,lon0) in CASES.items():
        y0,y1=G[g][4],G[g][5]; years=np.arange(int(y0),int(y1)+1)
        Rs=[r for h in sib(g) for r in RFULL[h]] if (only is None or G[g][1] in only) else []
        for i,d in enumerate(docs):
            if not d[4]: continue
            t,x,y=d[0],d[1],d[2]
            Am,_=SE.estimate(RC[(g,i)],years,tau,sigA,sigN,g,lat0,lon0,Rs,lam)
            Af=SE.Afun_of(years,Am); P1=hermpts(docs,gs,Af,i)
            if len(P1)<2: continue
            nx,ny_=SE.herm(P1,t); a=Af(t); p=SE.phi(t); e=math.hypot(x-nx-p*a[0],y-ny_-p*a[1]); E.append(e); per.setdefault(G[g][1],[]).append(e)
    return round(st.median(E),1),round(st.mean(E),1),{k:(len(v),round(st.median(v))) for k,v in per.items()}
if __name__=='__main__':
    out={}
    for lam in [0,.1,.25,.5,1]:
        r=run3(lam); out[str(lam)]=r; print(lam,r[:2],flush=True)
    print('by people, lam 0',out['0'][2]); print('by people, lam .25',out['0.25'][2]); print('by people, lam 1',out['1'][2])
    for tau,sig in [(3,60),(8,60),(5,30),(5,100)]:
        print('tau',tau,'sig',sig,run3(0,tau,sig,sig)[:2],flush=True)
    json.dump(out,open('../build/poolcal.json','w'),indent=1)
