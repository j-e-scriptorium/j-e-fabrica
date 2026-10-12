# Fit the shape of the seasonal profile by hold-out, and check the seasonal halo's coverage.
import sys,math,itertools,json,pickle,os,statistics as st
sys.argv=['x']
exec(open('calib_seas.py').read().split("if __name__=='__main__':")[0])
# each held-out place's own prediction variance from the smoother run without it
PV='../build/seas_PV.pkl'
if os.path.exists(PV): PVc=pickle.load(open(PV,'rb'))
else:
    PVc={}
    for g,(docs,gs,lat0,lon0) in CASES.items():
        y0,y1=G[g][4],G[g][5]
        for i,d in enumerate(docs):
            if not d[4]: continue
            ob=[(t,x,y,(POSP['k']*r)**2+POSP['s0']**2) for j,(t,x,y,r,s) in enumerate(docs) if j!=i]+[(t,x,y,POSP['sg']**2) for (t,x,y) in gs]
            T,ms,Ps=PS.smooth(y0,y1,ob,POSP['q']); m,v=PS.predict_at(T,ms,Ps,d[0]); PVc[(g,i)]=float(v)
    pickle.dump(PVc,open(PV,'wb'))
def run2(prof,tau=5,sigA=60,sigN=60):
    SE.PROF=prof; E=[];cov0=cov1=0;N=0
    for g,(docs,gs,lat0,lon0) in CASES.items():
        y0,y1=G[g][4],G[g][5]; years=np.arange(int(y0),int(y1)+1)
        for i,d in enumerate(docs):
            if not d[4]: continue
            t,x,y=d[0],d[1],d[2]
            Am,_=SE.estimate(RC[(g,i)],years,tau,sigA,sigN,g,lat0,lon0); V=SE.estimate.var
            Af=SE.Afun_of(years,Am); P1=hermpts(docs,gs,Af,i)
            if len(P1)<2: continue
            nx,ny_=SE.herm(P1,t); a=Af(t); p=SE.phi(t); e=math.hypot(x-nx-p*a[0],y-ny_-p*a[1]); E.append(e)
            k=min(len(years)-1,max(0,int(round(t-years[0])))); base=PVc[(g,i)]+POSP['s0']**2
            cov0+= e<=1.433*math.sqrt(base); cov1+= e<=1.433*math.sqrt(base+p*p*V[k]); N+=1
    return round(st.median(E),1),round(st.mean(E),1),round(cov0/N,3),round(cov1/N,3),N
if __name__=='__main__':
    print('cosine',run2(None),flush=True)
    res=[]
    for a,b,c,d in itertools.product([.1,.15,.2,.25,.3],[.35,.42,.5],[.6,.65,.7,.78],[.8,.85,.9,.95]):
        if not a<b<c<d: continue
        r=run2((a,b,c,d)); res.append((r[1],r[0],(a,b,c,d),r)); 
    res.sort(); 
    for x in res[:8]: print(x,flush=True)
    print('bands phase table (.22,.5,.64,.92)',run2((.22,.5,.64,.92)))
    json.dump(dict(cos=run2(None),best=res[0][2],bestres=res[0][3],top=[[x[2],x[3]] for x in res[:8]]),open('../build/profcal.json','w'),indent=1)
