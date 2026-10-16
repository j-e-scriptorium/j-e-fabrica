# Calibrate and test the Gaussian-process positions of the nomadic divisions (possgp.py; METHODS.md §3).
#   python3 calib_gp.py . ..      (about 15 minutes)  →  ../build/gpcal.json
# 1. Settings tuned by block hold-out on all places (each withheld with every place within half a year): season-dated places
#    against the predicted position at their date, range and agency statements and undated camps against the annual centre.
#    The same tuning run on half the divisions and scored on the other half, both ways, gives the out-of-sample figures.
# 2. All places, held out the same way, against the annual centre (with and without our keyframes).
# 3. The roaming radius by season: the spread of withheld season-dated places around the predicted centre beyond the model's
#    own uncertainty and the record's stated radius, set so that the halo holds 68% of them in winter, summer and between.
import sys,os,runpy,io,contextlib,math,json,itertools,statistics as st
S=sys.argv[2] if len(sys.argv)>2 else '..'
sys.argv=['build3.py','.',S]; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import possgp as GP, seasonal as SE
G=B['G']
DIV={g:GP.prepare(g,B['DOCO'][g],B['GSP'][g]) for g in B['DOCO'] if 'nomadic' in G[g][6] and len(B['DOCO'][g])>=3}
M=GP.moments([p for d in DIV.values() for p in d['pts']])
def holdout(th,groups,kinds=('dated',),guesses=True,BW=0.5):
    out=[]
    for g in groups:
        d=DIV[g]
        for p in d['pts']:
            if p['s'] not in kinds: continue
            tr=[q for q in d['pts'] if abs(q['t']-p['t'])>BW and (guesses or q['s']!='guess')]
            if len(tr)<2: continue
            f=GP.Fit(dict(d,pts=tr),th,M)
            m,v=f.at(p['t']) if p['s']=='dated' else f.trend(p['t'])
            out.append(dict(g=g,t=p['t'],s=p['s'],d=math.hypot(p['x']-m[0],p['y']-m[1]),v=v,r=p['r'],ph=SE.phi(p['t'])))
    return out
ALLK=('dated','annual','camp')
def score(E): return st.mean(e['d'] for e in E)
def tune(groups):
    """best settings with a seasonal component, and best with none"""
    best={True:None,False:None}
    for lT,sL,lL,s0,k,sS in itertools.product((30,45),(75,150),(2,4),(60,90),(0.25,0.5),(0,20,45,70)):
        th=dict(sT=200,lT=lT,sL=sL,lL=lL,sS=sS,lS=8,w=(1,0.5),k=k,s0=s0,sg=150); e=score(holdout(th,groups,kinds=ALLK)); key=sS>0
        if best[key] is None or e<best[key][0]: best[key]=(e,th)
    return best[True][1],best[False][1]
def summ(E): d=[e['d'] for e in E]; return dict(n=len(d),median=round(st.median(d)),mean=round(st.mean(d)),beyond_radius_median=round(st.median(max(0,e['d']-e['r']) for e in E)))
def bin_(ph): return 'winter' if ph<=-0.9 else ('summer' if ph>=0.9 else 'between')
def roam_for(E,cover=0.68):
    lo,hi=0.0,500.0
    for _ in range(40):
        R=(lo+hi)/2; c=sum(e['d']<=1.51*math.sqrt(e['v']+R*R+(e['r']/1.51)**2) for e in E)/len(E)
        lo,hi=(lo,R) if c>=cover else (R,hi)
    return round(hi)
if __name__=='__main__':
    gs=sorted(DIV,key=lambda g:-sum(p['s']=='dated' for p in DIV[g]['pts']))
    A,Bh=gs[0::2],gs[1::2]
    Es,Et=[],[]
    for tr_,te in ((A,Bh),(Bh,A)):
        ts,tt=tune(tr_); Es+=holdout(ts,te,kinds=ALLK); Et+=holdout(tt,te,kinds=ALLK)
    pick=lambda E,k: [e for e in E if e['s']==k]
    nested={'track only':dict(all=summ(Et),dated=summ(pick(Et,'dated')),annual=summ(pick(Et,'annual'))),
            'track and seasonal component':dict(all=summ(Es),dated=summ(pick(Es,'dated')),annual=summ(pick(Es,'annual')))}; print('out of sample',nested,flush=True)
    th=tune(gs)[0]; print('settings',th,flush=True)
    Ed=holdout(th,gs); Ea=holdout(th,gs,kinds=('dated','annual','camp')); Eng=holdout(th,gs,kinds=('dated','annual','camp'),guesses=False)
    roam={b:roam_for([e for e in Ed if bin_(e['ph'])==b]) for b in ('winter','between','summer')}
    roam['annual']=roam_for([e for e in Ea if e['s']!='dated'])
    cov={b:round(sum(e['d']<=1.51*math.sqrt(e['v']+roam[b]**2+(e['r']/1.51)**2) for e in Ed if bin_(e['ph'])==b)/max(1,sum(bin_(e['ph'])==b for e in Ed)),2) for b in ('winter','between','summer')}
    # the Kiowa calendar: how far the grounds moved between seasons, and from year to year
    W={};Su={}
    for p in DIV['kio']['pts']:
        if p['s']!='dated': continue
        f=p['t']%1; yr=math.floor(p['t'])
        if 0.4<=f<=0.7: Su[yr]=p
        elif f>=0.85: W[yr]=p
        elif f<=0.2: W[yr-1]=p
    dd=lambda a,b: math.hypot(a['x']-b['x'],a['y']-b['y'])
    kio=dict(summer_to_winter=round(st.median([dd(Su[y],W[y]) for y in Su if y in W])),winter_to_winter=round(st.median([dd(W[y],W[y+1]) for y in W if y+1 in W])),summer_to_summer=round(st.median([dd(Su[y],Su[y+1]) for y in Su if y+1 in Su])))
    out=dict(th=th,litw=GP.LITW,out_of_sample=nested,season_dated=summ(Ed),
             places=dict(all=summ(Ea),without_keyframes=summ(Eng)),roam=roam,roam_coverage=cov,
             by_season={b:summ([e for e in Ed if bin_(e['ph'])==b]) for b in ('winter','between','summer')},kiowa=kio)
    json.dump(out,open(f'{S}/build/gpcal.json','w'),indent=1); print(json.dumps(out,indent=1))
