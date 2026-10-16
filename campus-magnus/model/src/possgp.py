# Position of a nomadic division: a quasi-periodic Gaussian process (METHODS.md §3).
# position(t) = long-term track T(t) + seasonal component S(t) + literature pattern, each record a noisy sighting of it.
#   T: the sum of a smooth component (scale sT km, length lT years) and a short one (sL, lL) that follows records a year or two
#      apart when they agree; both squared-exponential in time.
#   S: first two annual harmonics whose amplitudes drift (scale sS km, length lS years); learned from the records.
#   literature pattern: half the step to the summer ground named in seasonal.SEASPRI, as a prior mean the records can override.
# Records: places dated to a season carry their phase; camps with no month carry the season-of-record distribution of the
# dated places; range and agency statements and our keyframes observe the annual mean only.
import math,re,json,os,statistics as st
import numpy as np
import possmooth as PS, seasonal as SE

H=(1,2)
LITW=0.5    # weight on the literature pattern (chosen by hold-out: half the literature's distance did better than all of it)
DEFAULT=dict(sT=100,lT=20,sS=20,lS=8,w=(1,0.5),k=0.25,s0=30,sg=150)
ANNUAL=re.compile(r'range|roam|rove|between|hunting grounds|country|territor|live[sd]? |reside|dwell|head(s)? of|heads|lodges;|warriors;|agency|reservation|reserve|occup|inhabit|frequent|usually|generally|centre ours|center ours|\(a range',re.I)

# Year each division settled on a reservation or reserve; roaming then shrinks to a quarter over three years (the page uses the same).
RES={'bru':1878,'ogl':1878,'min':1877,'hnk':1881,'sih':1877,'sna':1877,'twk':1868,'ynk':1859,'yku':1873,'ykl':1863,'mde':1853,'wpk':1853,'wpt':1853,'sis':1867,'ass':1871,'asn':1877,
 'cre':1876,'crw':1876,'crs':1883,'ojb':1882,'sik':1880,'kai':1880,'pik':1880,'gv':1878,'chn':1877,'chs':1875,'arn':1878,'ars':1870,'cwm':1882,'cwr':1884,'kio':1875,'kap':1875,'jic':1887,'lip':1880,
 'cyy':1875,'cyk':1875,'cyp':1855,'cyn':1875,'cyq':1875,'sho':1868,'apc':1732,'cyj':1795,'chy':1832,'ara':1835,
 'sar':1881,'sto':1879,'tkw':1868,'tet':1785,'sao':1806}
def roamf(gid,t):
    r=RES.get(gid); return 1.0 if r is None or t<r else max(0.25,1-0.75*(t-r)/3)

def status(o):
    """'dated' (season known), 'annual' (a range, an agency, a year-round statement) or 'camp' (a camp with no month)"""
    if SE.season_known(o['y'],o['raw'],o['r']): return 'dated'
    if (o['r'] or 25)>150 or abs(o['y']%1)<1e-6 or ANNUAL.search(o['raw'] or ''): return 'annual'
    return 'camp'

def prepare(gid,recs,guesses):
    """recs: whole, stated places of the division (build3 obs dicts); guesses: (year, lat, lon) keyframes"""
    pts=[dict(t=o['y'],lat=o['lat'],lon=o['lon'],r=o['r'] or 25,s=status(o)) for o in recs]
    pts+=[dict(t=y,lat=la,lon=lo,r=None,s='guess') for (y,la,lo) in guesses]
    if not pts: return None
    lat0=st.mean(p['lat'] for p in pts); lon0=st.mean(p['lon'] for p in pts)
    for p in pts: p['x'],p['y']=PS.local(lat0,lon0,p['lat'],p['lon'])
    return dict(gid=gid,pts=sorted(pts,key=lambda p:p['t']),lat0=lat0,lon0=lon0)

def moments(pts):
    ph=[p['t']%1 for p in pts if p['s']=='dated']
    return {h:complex(np.mean([np.exp(2j*math.pi*h*u) for u in ph])) for h in H}

def lit(gid,t,lat0,lon0):
    a,has=SE.prior_A(gid,t,lat0,lon0)
    return np.array(a)*SE.phi(t)*LITW if has else np.zeros(2)

class Fit:
    def __init__(self,div,th,M):
        self.d=div; self.th=th; P=div['pts']; self.P=P
        w=np.array(th['w']); self.w=w
        t=np.array([p['t'] for p in P]); self.t=t
        F=[];sv=[]
        for p in P:
            if p['s']=='dated': F.append([np.exp(2j*math.pi*h*p['t']) for h in H]); sv.append(1.0)
            elif p['s']=='camp': F.append([np.exp(2j*math.pi*h*math.floor(p['t']))*M[h] for h in H]); sv.append(1.0)
            else: F.append([0j]*len(H)); sv.append(0.0)
        self.F=np.array(F)
        dt=t[:,None]-t[None,:]
        K=th['sT']**2*np.exp(-dt**2/(2*th['lT']**2))
        if th.get('sL',0)>0: K=K+th['sL']**2*np.exp(-dt**2/(2*th['lL']**2))
        if th['sS']>0:
            KS=th['sS']**2*np.exp(-dt**2/(2*th['lS']**2))*sum(w[h]*np.real(self.F[:,h][:,None]*np.conj(self.F[:,h])[None,:]) for h in range(len(H)))
            np.fill_diagonal(KS,th['sS']**2*w.sum()*np.array(sv)); K=K+KS
        K[np.diag_indices_from(K)]+=np.array([th['sg']**2 if p['s']=='guess' else (th['k']*p['r'])**2+(th['s0']*roamf(div['gid'],p['t']))**2 for p in P])
        X=np.array([[p['x'],p['y']] for p in P],float)
        for i,p in enumerate(P):
            if p['s']=='dated': X[i]-=lit(div['gid'],p['t'],div['lat0'],div['lon0'])
        self.mu=X.mean(0); self.L=np.linalg.cholesky(K)
        self.alpha=np.linalg.solve(self.L.T,np.linalg.solve(self.L,X-self.mu))
    def _kT(self,tq):
        k=self.th['sT']**2*np.exp(-(tq-self.t)**2/(2*self.th['lT']**2))
        if self.th.get('sL',0)>0: k=k+self.th['sL']**2*np.exp(-(tq-self.t)**2/(2*self.th['lL']**2))
        return k
    def _kS(self,tq):
        if self.th['sS']<=0: return np.zeros(len(self.t))
        fq=np.array([np.exp(2j*math.pi*h*tq) for h in H])
        return self.th['sS']**2*np.exp(-(tq-self.t)**2/(2*self.th['lS']**2))*sum(self.w[h]*np.real(fq[h]*np.conj(self.F[:,h])) for h in range(len(H)))
    def trend(self,tq):
        """annual centre (km) and its per-axis posterior variance"""
        k=self._kT(tq); v=np.linalg.solve(self.L,k)
        return self.mu+k@self.alpha, max(1.0,self.th['sT']**2+self.th.get('sL',0)**2-float(v@v))
    def season(self,tq):
        """seasonal displacement from the annual centre at tq (km east, km north)"""
        return self._kS(tq)@self.alpha+lit(self.d['gid'],tq,self.d['lat0'],self.d['lon0'])
    def at(self,tq):
        m,v=self.trend(tq); return m+self.season(tq),v
    def harmonics(self,year):
        """seasonal displacement in a year as coefficients of cos/sin of 2πf and 4πf (f = fraction of the year), km"""
        fs=(np.arange(24)+0.5)/24; S=np.array([self.season(year+f) for f in fs])
        A=np.column_stack([np.cos(2*math.pi*fs),np.sin(2*math.pi*fs),np.cos(4*math.pi*fs),np.sin(4*math.pi*fs)])
        cx=np.linalg.lstsq(A,S[:,0],rcond=None)[0]; cy=np.linalg.lstsq(A,S[:,1],rcond=None)[0]
        return list(cx)+list(cy)

def load_cal(path):
    if os.path.exists(path):
        c=json.load(open(path)); th=dict(c['th']); th['w']=tuple(th['w']); return th,c
    return dict(DEFAULT),{}
