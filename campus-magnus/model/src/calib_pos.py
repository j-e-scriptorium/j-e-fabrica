# Hold-out calibration of the position smoother: drop each documented place, smooth the rest, score the prediction.
import sys,runpy,io,contextlib,os,math,itertools,json,statistics as st
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import possmooth as PS
G,DOCP,GSP=B['G'],B['DOCP'],B['GSP']
def life(g): return 'village' if G[g][6]=='village' else 'nomadic'
def prep(g):
    pts=DOCP[g]+[(y,la,lo,None) for (y,la,lo) in GSP[g]]
    lat0=st.mean(p[1] for p in pts); lon0=st.mean(p[2] for p in pts)
    D=[(y,)+PS.local(lat0,lon0,la,lo)+(r,) for (y,la,lo,r) in DOCP[g]]
    Gs=[(y,)+PS.local(lat0,lon0,la,lo) for (y,la,lo) in GSP[g]]
    return D,Gs
PRE={g:prep(g) for g in DOCP}
def score(gs,q,s0,k,sg,use_guess=True):
    nll=0;d=[];cov=0;N=0
    for g in gs:
        D,Gs=PRE[g]; y0,y1=G[g][4],G[g][5]
        if len(D)<2: continue
        for i,(t,x,y,r) in enumerate(D):
            obs=[(tt,xx,yy,(k*rr)**2+s0**2) for j,(tt,xx,yy,rr) in enumerate(D) if j!=i]
            if use_guess: obs+=[(tt,xx,yy,sg**2) for (tt,xx,yy) in Gs if not any(abs(tt-dd[0])<1 for dd in D)]
            T,ms,Ps=PS.smooth(y0,y1,obs,q); m,P=PS.predict_at(T,ms,Ps,t)
            v=P+(k*r)**2+s0**2; dd=(x-m[0])**2+(y-m[1])**2
            nll+=math.log(2*math.pi*v)+dd/(2*v); d.append(math.sqrt(dd)); N+=1
            cov+= math.sqrt(dd)<=1.515*math.sqrt(v)
    return nll/N, st.median(d), cov/N, N
if __name__=='__main__':
    out={}
    for L in ('nomadic','village'):
        gs=[g for g in DOCP if life(g)==L]
        best=None
        q,s0,k,sg=(2000,60,0.5,150) if L=='nomadic' else (200,20,0.5,60)
        grids=dict(q=[100,250,500,1000,2000,4000,8000,16000],s0=[5,10,20,40,60,90,130],k=[0.25,0.5,0.75,1.0],sg=[40,80,150,250,400])
        cur=dict(q=q,s0=s0,k=k,sg=sg)
        for rnd in range(3):
            for par in ['q','s0','k','sg']:
                res=[]
                for v in grids[par]:
                    c=dict(cur);c[par]=v;res.append((score(gs,**c)[0],v))
                cur[par]=min(res)[1]
            print(L,rnd,cur,score(gs,**cur),flush=True)
        out[L]=dict(params=cur,score=score(gs,**cur),noguess=score(gs,use_guess=False,**cur))
        print(L,'without our keyframes',out[L]['noguess'],flush=True)
    json.dump(out,open('../build/poscal.json','w'),indent=1)
