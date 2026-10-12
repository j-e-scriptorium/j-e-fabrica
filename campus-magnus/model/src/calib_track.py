# Hold-out test of the drawn track (monotone Hermite curve through anchors), as opposed to the smoother that sets the halo:
# drop each documented place (and any other within half a year of it), redraw the track from the rest, and measure the miss in km.
import sys,runpy,io,contextlib,os,math,statistics as st,json
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import data_src as D
G,DOCP=B['G'],B['DOCP']
def herm(arr,y):
    n=len(arr)
    if y<=arr[0][0]: return arr[0][1:3]
    if y>=arr[-1][0]: return arr[-1][1:3]
    i=1
    while arr[i][0]<y: i+=1
    a,b=arr[i-1],arr[i]; h=b[0]-a[0]; t=(y-a[0])/h
    def tan(k,c):
        s1=(arr[k][c]-arr[k-1][c])/(arr[k][0]-arr[k-1][0]) if k>0 else None
        s2=(arr[k+1][c]-arr[k][c])/(arr[k+1][0]-arr[k][0]) if k<n-1 else None
        if s1 is None: return s2
        if s2 is None: return s1
        if s1*s2<=0: return 0
        m=(s1+s2)/2; return math.copysign(min(abs(m),3*min(abs(s1),abs(s2))),m)
    t2,t3=t*t,t*t*t; h00,h10,h01,h11=2*t3-3*t2+1,t3-2*t2+t,-2*t3+3*t2,t3-t2
    return [h00*a[c]+h10*h*tan(i-1,c)+h01*b[c]+h11*h*tan(i,c) for c in (1,2)]
def km(a,b): return math.hypot((a[1]-b[1])*111*math.cos(math.radians(a[0])),(a[0]-b[0])*111)
def run(use_guess):
    out={'nomadic':[],'village':[]}
    for g,docs in DOCP.items():
        L='village' if G[g][6]=='village' else 'nomadic'
        if L=='village' or len(docs)<2: continue
        for i,(t,la,lo,r) in enumerate(docs):
            rest=[d for d in docs if abs(d[0]-t)>=0.5]  # withhold every place within half a year, so a same-season duplicate cannot answer for it
            by={}
            for (y,a,b,_) in rest: by.setdefault(y,[]).append((a,b))
            anc={y:[y,st.mean(p[0] for p in v),st.mean(p[1] for p in v)] for y,v in by.items()}
            if use_guess:
                for (y,pl,pp,note) in D.GUESS.get(g,[]):
                    if pl and not any(abs(y-d[0])<1.0 for d in docs): anc[y]=[y,pl[0],pl[1]]  # as in the build: a keyframe near any documented place, the withheld one included, never enters
            arr=sorted(anc.values())
            if not arr: continue
            out[L].append(km((la,lo),herm(arr,t)))
    return out
r1,r0=run(True),run(False)
res={'nomadic_track_median_km':round(st.median(r1['nomadic']),1),'nomadic_track_median_km_without_keyframes':round(st.median(r0['nomadic']),1),'n':len(r1['nomadic'])}
print(res); json.dump(res,open('../build/trackcal.json','w'),indent=1)
