# Leave-one-out check of the demographic fit: drop each documented division count, refit, predict it.
import sys,math,json,runpy,statistics as stt
S=sys.argv[2]
sys.argv=['build3.py',sys.argv[1],S]
G=runpy.run_path('build3.py',run_name='__main__')
fit,PA,np,T,Y0,sig_obs=G['fit'],G['PA'],G['np'],G['T'],G['Y0'],G['sig_obs']
FIT=G['FIT']
extra={g:[] for g in PA}
# rebuild the aggregate allocation from the final fit (held fixed during LOO; a small leak noted in the report)
for o in G['aggs']:
    k=int(round(o['y']-Y0)); members=[x for x in o['g'] if G['G'][x][4]<=o['y']<=G['G'][x][5]]
    if not members: continue
    tot=sum(math.exp(FIT[x][0][k]) for x in members); ratio=o['pop']/tot
    for x in members: extra[x].append((o['y'],math.exp(FIT[x][0][k])*ratio,sig_obs(o)*1.6,'a'))
rows=[]
TAU=G['TAU']
def target(gid,j,y,p):
    # the held-out count corrected with its family's bias estimated WITHOUT this count (no leakage)
    fams=G['FAMS'].get(gid,[]); f=fams[j] if j<len(fams) else None
    if f is None or f=='census' or f not in G['BIAS_ND']: return p
    num,den=G['BIAS_ND'][f]; wr=G['RC'].get((gid,y))
    if wr: num-=wr[0]*wr[1]; den-=wr[0]
    return G['PA0'][gid][j][1]*math.exp(-num/(den+1/TAU**2))
for gid,L in PA.items():
    for j,(y,p,sg,src) in enumerate(L):
        if src!='o': continue
        p=target(gid,j,y,p)
        keep=PA[gid][:j]+PA[gid][j+1:]
        saved=PA[gid]; PA[gid]=keep
        lp,sd=fit(gid,extra[gid]); PA[gid]=saved
        pred=float(np.interp(y,T,lp)); s_fit=float(np.interp(y,T,sd))
        s_tot=math.sqrt(s_fit**2+sg**2)
        # naive comparison: log-linear interpolation between the nearest other documented counts (or the nearest one)
        others=sorted([(yy,pp) for (yy,pp,ss,sr) in keep if sr=='o'])
        lo=[o for o in others if o[0]<y]; hi=[o for o in others if o[0]>y]
        if lo and hi:
            a,b=lo[-1],hi[0]; naive=math.log(a[1])+(math.log(b[1])-math.log(a[1]))*(y-a[0])/(b[0]-a[0])
        elif lo or hi: naive=math.log((lo or hi)[-1 if lo else 0][1])
        else: naive=None
        rows.append(dict(g=gid,y=y,obs=p,pred=round(math.exp(pred)),err=math.log(p)-pred,z=(math.log(p)-pred)/s_tot,s=s_tot,sg=sg,
                         naive_err=(math.log(p)-naive) if naive is not None else None))
n=len(rows)
ae=[abs(r['err']) for r in rows]; z=[abs(r['z']) for r in rows]
nv=[abs(r['naive_err']) for r in rows if r['naive_err'] is not None]; mv=[abs(r['err']) for r in rows if r['naive_err'] is not None]
rep=dict(n=n,median_abs_log_err=round(stt.median(ae),3),median_factor=round(math.exp(stt.median(ae)),2),
 cover1=round(sum(x<=1 for x in z)/n,3),cover2=round(sum(x<=2 for x in z)/n,3),
 naive_n=len(nv),naive_median_factor=round(math.exp(stt.median(nv)),2),model_median_factor_same=round(math.exp(stt.median(mv)),2),
 by_period={})
for a,b in [(1700,1800),(1800,1840),(1840,1870),(1870,1906)]:
    sub=[r for r in rows if a<=r['y']<b]
    if sub: rep['by_period'][f'{a}–{b-1 if b<1906 else 1905}']=dict(n=len(sub),median_factor=round(math.exp(stt.median([abs(r['err']) for r in sub])),2),cover2=round(sum(abs(r['z'])<=2 for r in sub)/len(sub),2))
print(json.dumps(rep,indent=1))
json.dump(dict(report=rep,points=[[r['g'],round(r['y'],2),r['obs'],r['pred'],round(r['z'],2)] for r in rows]),open(f'{S}/build/validation.json','w'),ensure_ascii=False)
