import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import math,statistics as st
sys.argv=['x']
import calib_pos as C
PS=C.PS
NP=dict(q=2000,s0=90,k=0.25,sg=150)
E=[];S=[];OLD=[]
for g in C.DOCP:
    if C.life(g)!='nomadic': continue
    D,Gs=C.PRE[g]; y0,y1=C.G[g][4],C.G[g][5]
    if len(D)<2: continue
    for i,(t,x,y,r) in enumerate(D):
        rest=[dd for j,dd in enumerate(D) if j!=i]
        gk=[(tt,xx,yy) for (tt,xx,yy) in Gs if not any(abs(tt-dd[0])<1 for dd in D)]
        obs=[(tt,xx,yy,(NP['k']*rr)**2+NP['s0']**2) for (tt,xx,yy,rr) in rest]+[(tt,xx,yy,NP['sg']**2) for (tt,xx,yy) in gk]
        T,ms,Ps=PS.smooth(y0,y1,obs,NP['q']); m,P=PS.predict_at(T,ms,Ps,t)
        pts=sorted([(a,b,c) for (a,b,c,_) in rest]+gk)
        lo=[p for p in pts if p[0]<=t]; hi=[p for p in pts if p[0]>t]
        if lo and hi: a,b=lo[-1],hi[0]; f=(t-a[0])/(b[0]-a[0]); p=(a[1]+f*(b[1]-a[1]),a[2]+f*(b[2]-a[2]))
        else: a=(lo or hi)[-1 if lo else 0]; p=(a[1],a[2])
        E.append(math.hypot(x-p[0],y-p[1])); S.append(math.sqrt(P+NP['s0']**2))
        dyr=min(abs(t-dd[0]) for dd in rest); OLD.append(min(400,30+180*(1-math.exp(-dyr/0.35))+6*dyr))
n=len(E)
rat=sorted(e/s for e,s in zip(E,S)); c=rat[int(.68*n)]
print('n',n,'scale c',round(c,3))
print('new halo: coverage',round(sum(e<=c*s for e,s in zip(E,S))/n,3),'median radius',round(st.median([c*s for s in S])))
print('old halo: coverage',round(sum(e<=o for e,o in zip(E,OLD))/n,3),'median radius',round(st.median(OLD)))
# coverage by data density terciles
idx=sorted(range(n),key=lambda i:S[i]); th=n//3
for name,sel in (('densest third',idx[:th]),('middle',idx[th:2*th]),('sparsest third',idx[2*th:])):
    print(name,'new cover',round(sum(E[i]<=c*S[i] for i in sel)/len(sel),2),'old cover',round(sum(E[i]<=OLD[i] for i in sel)/len(sel),2))
