# An alternative seasonal model, tested against the one the map uses (METHODS.md, "Seasonal round: an alternative tested").
# A quasi-periodic Gaussian process for each nomadic division: a smooth long-term track plus a seasonal component whose shape
# and strength are learned and drift slowly (first two annual harmonics). Places dated to a month carry their phase; camps with
# no month carry the season-of-record distribution of the dated places (which peaks in late July); range and agency statements
# and our keyframes observe only the annual mean. Scored on the places dated to a season, each withheld with every place within
# half a year, in a nested split: settings tuned on half the divisions and scored on the other half, then the reverse.
#   python3 seas_gp.py . ..      (about 2 minutes)
import sys,os,runpy,io,contextlib,re,math,itertools,statistics as st
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import possmooth as PS, seasonal as SE, numpy as np
G,obs,GSP=B['G'],B['obs'],B['GSP']
ANNUAL=re.compile(r'range|roam|rove|between|hunting grounds|country|territor|live[sd]? |reside|dwell|head(s)? of|heads|lodges;|warriors;|agency|reservation|reserve|occup|inhabit|frequent|usually|generally|centre ours|center ours|\(a range',re.I)
def status(o):
    if SE.season_known(o['y'],o['raw'],o['r']): return 'dated'
    if (o['r'] or 25)>150 or abs(o['y']%1)<1e-6 or ANNUAL.search(o['raw'] or ''): return 'annual'
    return 'camp'
DIV={}
for g in G:
    if 'nomadic' not in G[g][6]: continue
    pts=[dict(t=o['y'],lat=o['lat'],lon=o['lon'],r=o['r'] or 25,s=status(o)) for o in obs
         if not o['agg'] and o['g'][0]==g and o['loc']=='stated' and o['whole'] and not o['seasonal']]
    if len(pts)<3: continue
    pts+=[dict(t=y,lat=la,lon=lo,r=None,s='guess') for (y,la,lo) in GSP[g]]
    lat0=st.mean(p['lat'] for p in pts); lon0=st.mean(p['lon'] for p in pts)
    for p in pts: p['x'],p['y']=PS.local(lat0,lon0,p['lat'],p['lon'])
    DIV[g]=sorted(pts,key=lambda p:p['t'])
H=(1,2)
PH=[p['t']%1 for P in DIV.values() for p in P if p['s']=='dated']
M={h:complex(np.mean([np.exp(2j*math.pi*h*u) for u in PH])) for h in H}   # circular moments of the season-of-record distribution
def feats(p):
    if p['s']=='dated': return np.array([np.exp(2j*math.pi*h*p['t']) for h in H]),1.0
    if p['s']=='camp': return np.array([np.exp(2j*math.pi*h*math.floor(p['t']))*M[h] for h in H]),1.0
    return np.zeros(len(H),complex),0.0
def predict(P,tq,th):
    t=np.array([p['t'] for p in P]); FS=[feats(p) for p in P]; F=np.array([f for f,_ in FS]); sv=np.array([s for _,s in FS])
    dt=t[:,None]-t[None,:]; w=np.array(th['w'])
    K=th['sT']**2*np.exp(-dt**2/(2*th['lT']**2))
    if th['sS']>0:
        KS=th['sS']**2*np.exp(-dt**2/(2*th['lS']**2))*sum(w[h]*np.real(F[:,h][:,None]*np.conj(F[:,h])[None,:]) for h in range(len(H)))
        np.fill_diagonal(KS,th['sS']**2*w.sum()*sv); K=K+KS
    K[np.diag_indices_from(K)]+=np.array([th['sg']**2 if p['s']=='guess' else (th['k']*p['r'])**2+th['s0']**2 for p in P])
    X=np.array([[p['x'],p['y']] for p in P]); mu=X.mean(0)
    L=np.linalg.cholesky(K); a=np.linalg.solve(L.T,np.linalg.solve(L,X-mu))
    d=tq-t; k=th['sT']**2*np.exp(-d**2/(2*th['lT']**2))
    if th['sS']>0:
        fq=np.array([np.exp(2j*math.pi*h*tq) for h in H])
        k=k+th['sS']**2*np.exp(-d**2/(2*th['lS']**2))*sum(w[h]*np.real(fq[h]*np.conj(F[:,h])) for h in range(len(H)))
    return mu+k@a
def blockcv(th,groups,BW=0.5):
    E=[]
    for g in groups:
        P=DIV[g]
        for p in P:
            if p['s']!='dated': continue
            train=[q for q in P if abs(q['t']-p['t'])>BW]
            if len(train)<2: continue
            m=predict(train,p['t'],th); E.append((g,math.hypot(p['x']-m[0],p['y']-m[1]),max(0,math.hypot(p['x']-m[0],p['y']-m[1])-p['r'])))
    return E
def tune(groups,seasonal):
    best=None
    for sT,lT,s0,k in itertools.product((100,150),(8,12,20),(30,60,90),(0.25,0.5)):
        for sS,lS in (((0,8),) if not seasonal else itertools.product((10,20,30,45),(4,8,15))):
            th=dict(sT=sT,lT=lT,sS=sS,lS=lS,w=(1,0.5),k=k,s0=s0,sg=150); e=st.mean(x[1] for x in blockcv(th,groups))
            if best is None or e<best[0]: best=(e,th)
    return best[1]
if __name__=='__main__':
    gs=sorted(DIV,key=lambda g:-sum(p['s']=='dated' for p in DIV[g])); A,Bf=gs[0::2],gs[1::2]
    print('records by status:',{s:sum(p['s']==s for P in DIV.values() for p in P) for s in ('dated','camp','annual','guess')})
    for seas in (False,True):
        E=blockcv(tune(A,seas),Bf)+blockcv(tune(Bf,seas),A)
        print('trend + seasonal' if seas else 'trend only      ','places',len(E),'| miss: median %.0f km, mean %.0f'%(st.median(x[1] for x in E),st.mean(x[1] for x in E)),
              '| beyond the stated radius: median %.0f, mean %.0f'%(st.median(x[2] for x in E),st.mean(x[2] for x in E)))
    # how far a people's grounds moved between seasons, against how far they moved from year to year
    for g in ('kio',):
        W={};Su={}
        for p in DIV[g]:
            if p['s']!='dated': continue
            f=p['t']%1; yr=math.floor(p['t'])
            if 0.4<=f<=0.7: Su[yr]=p
            elif f>=0.85: W[yr]=p
            elif f<=0.2: W[yr-1]=p
        d=lambda a,b: math.hypot(a['x']-b['x'],a['y']-b['y'])
        print(g,'summer to the next winter: median %.0f km; winter to winter %.0f; summer to summer %.0f'%(
            st.median([d(Su[y],W[y]) for y in Su if y in W]),st.median([d(W[y],W[y+1]) for y in W if y+1 in W]),st.median([d(Su[y],Su[y+1]) for y in Su if y+1 in Su])))
