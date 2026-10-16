# Hold-out calibration of the village halo: drop each documented village place, rebuild the hold-and-move track and its halo from
# the rest, and fit the halo's terms so that 68% of withheld places fall inside it, with coverage as even as possible across strata.
import sys,runpy,io,contextlib,os,statistics as st, itertools as it
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import seasonal as SE, ecology_src as EC
G,DOCP,GSP=B['G'],B['DOCP'],B['GSP']; km=B['_km']
def track(pts,gid):
    dense=[]; mvs=[]
    for i,p in enumerate(pts):
        dense.append(p)
        if i+1<len(pts):
            q=pts[i+1]; mv=[m for (m,_,_) in EC.VMOVE.get(gid,[]) if p[0]<m<q[0]+0.3]
            if mv and km(p[1:3],q[1:3])>3:
                m=mv[0]; b=min(q[0],m+0.2); a=min(m-0.2,b-0.2); mvs.append(m)
                if a>p[0]: dense.append((a,p[1],p[2]))
                if b<q[0]: dense.append((b,q[1],q[2]))
            elif q[0]-p[0]>2.2 and km(p[1:3],q[1:3])>3:
                mid=(p[0]+q[0])/2; dense.append((mid-1,p[1],p[2])); dense.append((mid+1,q[1],q[2]))
    return dense,mvs
def terms(pts,mvs,t):
    # (distance term, time term) of the halo at year t, as in build3: distance to the next place times the share of the gap, time to the nearer place
    lo=[p for p in pts if p[0]<=t]; hi=[p for p in pts if p[0]>t]
    if lo and hi:
        a,b=lo[-1],hi[0]; dm=[m for m in mvs if a[0]<m<b[0]+0.3]
        u=0.5*max(0.0,1-abs(t-dm[0])) if dm else min(t-a[0],b[0]-t)/(b[0]-a[0])
        return km(a[1:3],b[1:3])*u, min(t-a[0],b[0]-t), 1
    a=(lo or hi)[-1 if lo else 0]; return 0.0, abs(t-a[0]), 0
R=[]
for g in DOCP:
    if G[g][6]!='village': continue
    byy={}
    for (y,la,lo,r) in DOCP[g]: byy.setdefault(y,[]).append((la,lo))
    docs=sorted((y,sum(p[0] for p in L)/len(L),sum(p[1] for p in L)/len(L)) for y,L in byy.items())
    if len(docs)<2: continue
    for i,d in enumerate(docs):
        pts=sorted([x for j,x in enumerate(docs) if j!=i]+[(y,la,lo) for (y,la,lo) in GSP[g] if abs(y-d[0])>=1])
        if not pts: continue
        dense,mvs=track(pts,g); p=SE.herm([x[:3] for x in dense],d[0]); e=km(p,d[1:3])
        D,T,inside=terms(pts,mvs,d[0]); R.append((g,d[0],e,D,T,inside))
def halo(a,b,c,D,T): return min(300,a+b*D+c*T)
def cov(a,b,c,rows=R): return sum(e<=halo(a,b,c,D,T) for (_,_,e,D,T,_) in rows)/len(rows)
def width(a,b,c): return st.mean(halo(a,b,c,D,T) for (_,_,e,D,T,_) in R)
print('withheld village places',len(R),'median miss',round(st.median(r[2] for r in R)),'km')
# strata of time and distance from the nearest place; the chosen halo holds 68% overall with coverage most even across them
STRATA=(('within 3 yr of a place',lambda r:r[4]<3),('3-10 yr from a place',lambda r:3<=r[4]<10),('10 yr or more from a place',lambda r:r[4]>=10),
        ('next place under 30 km on',lambda r:r[3]<30),('next place 30 km or more on',lambda r:r[3]>=30))
best=None
for a,b,c in it.product(range(10,81,2),(0,0.25,0.5,0.75,1.0,1.25,1.5),(0,0.5,1,2,3,4,6)):
    if cov(a,b,c)<0.68: continue
    dev=sum((cov(a,b,c,[r for r in R if f(r)])-0.68)**2 for _,f in STRATA)
    score=dev+width(a,b,c)/1000
    if best is None or score<best[0]: best=(score,a,b,c)
_,a,b,c=best
print(f'chosen halo: {a} km + {b} x distance term + {c} km a year; coverage',round(cov(a,b,c),3),'mean halo',round(width(a,b,c)),'km')
for nm,f in STRATA:
    rows=[r for r in R if f(r)]
    if rows: print(' ',nm,len(rows),round(cov(a,b,c,rows),3))
