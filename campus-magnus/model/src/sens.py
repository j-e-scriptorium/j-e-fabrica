# One-at-a-time sensitivity analysis of the demographic model.
import sys,os,math,json,runpy,statistics as stt,io,contextlib
S=sys.argv[2]; base_argv=['build3.py',sys.argv[1],S]
YEARS=[1750,1780,1805,1830,1850,1880]
def run(env):
    old={k:os.environ.get(k) for k in env}
    os.environ.update({k:str(v) for k,v in env.items()}); os.environ['SENS']='1'
    sys.argv=base_argv
    with contextlib.redirect_stdout(io.StringIO()):
        G=runpy.run_path('build3.py',run_name='__main__')
    for k,v in old.items():
        if v is None: os.environ.pop(k,None)
        else: os.environ[k]=v
    return G
def totals(G):
    FIT=G['FIT_RAW']; out={}
    for y in YEARS:
        k=y-1700; vals=[FIT[g][0][k] for g in FIT if G['G'][g][4]<=y<=G['G'][g][5]]; out[y]=round(sum(math.exp(v) for v in vals if not math.isnan(v)))
    out['unidentified']=sum(1 for g in FIT if math.isnan(FIT[g][0][100]))
    return out
def loo(G):
    fit,PA,np,T,Y0,sig_obs,FIT=G['fit'],G['PA'],G['np'],G['T'],G['Y0'],G['sig_obs'],G['FIT_RAW']
    extra={g:[] for g in PA}
    for o in G['aggs']:
        k=int(round(o['y']-Y0)); members=[x for x in o['g'] if G['G'][x][4]<=o['y']<=G['G'][x][5]]
        if not members: continue
        members=[x for x in members if not math.isnan(FIT[x][0][k])]
        if not members: continue
        tot=sum(math.exp(FIT[x][0][k]) for x in members); ratio=o['pop']/tot
        for x in members: extra[x].append((o['y'],math.exp(FIT[x][0][k])*ratio,sig_obs(o)*1.6,'a'))
    errs=[];zs=[]
    for gid,L in PA.items():
        for j,(y,p,sg,src) in enumerate(L):
            if src!='o': continue
            saved=PA[gid]; PA[gid]=L[:j]+L[j+1:]
            lp,sd=fit(gid,extra[gid]); PA[gid]=saved
            if math.isnan(lp[0]): continue
            pred=float(np.interp(y,T,lp)); st=math.sqrt(float(np.interp(y,T,sd))**2+sg**2)
            errs.append(abs(math.log(p)-pred)); zs.append(abs(math.log(p)-pred)/st)
    return round(math.exp(stt.median(errs)),3),round(sum(z<=2 for z in zs)/len(zs),3)
CASES=[('baseline',{}),
 ('smoothing ×½ (SS 0.01)',{'SS':0.01}),('smoothing ×2 (SS 0.04)',{'SS':0.04}),
 ('growth-rate prior ×½ (SR 0.03)',{'SR':0.03}),('growth-rate prior ×2 (SR 0.12)',{'SR':0.12}),
 ('background growth 0%/yr',{'R0':0.0}),('background growth 1%/yr',{'R0':0.01}),
 ('our anchors tighter (±20%)',{'SG':0.2}),('our anchors looser (±50%)',{'SG':0.5}),('our anchors removed',{'NOGUESS':1}),
 ('Clark ±25%',{'SC':0.25}),('Clark ±50%',{'SC':0.5}),
 ('reconstructions ±30%',{'SSEC':0.3}),('reconstructions ±70%',{'SSEC':0.7}),
 ('epidemic mortality ×0.75',{'EPS':0.75}),('epidemic mortality ×1.25',{'EPS':1.25}),
 ('one fewer person per lodge',{'LD':-1}),('one more person per lodge',{'LD':1}),
 ('no source-family correction',{'BIAS':0}),('source-family prior tighter (±15%)',{'BT':0.15}),('source-family prior looser (±40%)',{'BT':0.4}),
]
res=[]
for name,env in CASES:
    G=run(env); tt=totals(G); f,c2=loo(G)
    res.append(dict(case=name,env=env,totals=tt,loo_factor=f,loo_cover2=c2))
    print(name,tt,f,c2,flush=True)
json.dump(res,open(f'{S}/build/sensitivity.json','w'),ensure_ascii=False,indent=0)
