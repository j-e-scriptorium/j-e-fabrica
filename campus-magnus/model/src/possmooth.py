# Random-walk state-space smoother for a division's position (Kalman filter + Rauch–Tung–Striebel smoother).
# Positions in local km; isotropic, so one variance serves both axes.
import math, numpy as np
H=0.5   # grid step, years
def local(lat0,lon0,lat,lon): return ((lon-lon0)*111*math.cos(math.radians(lat0)),(lat-lat0)*111)
def unlocal(lat0,lon0,x,y): return (lat0+y/111, lon0+x/(111*math.cos(math.radians(lat0))))
def smooth(t0,t1,obs,q):
    """obs: list of (t,x,y,var). Returns grid times, means (n,2), variances (n,)."""
    n=int(round((t1-t0)/H))+1; T=t0+H*np.arange(n)
    byk={}
    for (t,x,y,v) in obs:
        k=min(n-1,max(0,int(round((t-t0)/H)))); byk.setdefault(k,[]).append((x,y,v))
    mf=np.zeros((n,2)); Pf=np.zeros(n); Pp=np.zeros(n)
    m=np.zeros(2); P=1e9; Q=q*H
    for k in range(n):
        if k>0: P=P+Q
        Pp[k]=P
        for (x,y,v) in byk.get(k,()):
            K=P/(P+v); m=m+K*(np.array([x,y])-m); P=(1-K)*P
        mf[k]=m; Pf[k]=P
    ms=mf.copy(); Ps=Pf.copy()
    for k in range(n-2,-1,-1):
        G=Pf[k]/(Pf[k]+Q); ms[k]=mf[k]+G*(ms[k+1]-mf[k]); Ps[k]=Pf[k]+G*G*(Ps[k+1]-(Pf[k]+Q))
    return T,ms,Ps
def predict_at(T,ms,Ps,t):
    k=int(round((t-T[0])/H)); k=min(len(T)-1,max(0,k)); return ms[k],Ps[k]
