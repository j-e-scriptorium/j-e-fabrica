# Hold-out test of dated village moves: drop each documented village place, rebuild the hold-and-move track, score the miss.
import sys,runpy,io,contextlib,os,math,statistics as st
sys.argv=['build3.py','.','..']; os.environ['SENS']='1'
with contextlib.redirect_stdout(io.StringIO()): B=runpy.run_path('build3.py',run_name='__main__')
import seasonal as SE, ecology_src as EC
G,DOCP,GSP=B['G'],B['DOCP'],B['GSP']; km=B['_km']
def track(pts,gid,use):
    dense=[]
    for i,p in enumerate(pts):
        dense.append(p)
        if i+1<len(pts):
            q=pts[i+1]; mv=[m for (m,_,_) in EC.VMOVE.get(gid,[]) if p[0]<m<q[0]+0.3] if use else []
            if mv and km(p[1:3],q[1:3])>3:
                m=mv[0]; b=min(q[0],m+0.2); a=min(m-0.2,b-0.2)
                if a>p[0]: dense.append((a,p[1],p[2]))
                if b<q[0]: dense.append((b,q[1],q[2]))
            elif q[0]-p[0]>2.2 and km(p[1:3],q[1:3])>3:
                mid=(p[0]+q[0])/2; dense.append((mid-1,p[1],p[2])); dense.append((mid+1,q[1],q[2]))
    return dense
res={0:[],1:[]}; near={0:[],1:[]}
for g in DOCP:
    if G[g][6]!='village' or g not in EC.VMOVE: continue
    byy={}
    for (y,la,lo,r) in DOCP[g]: byy.setdefault(y,[]).append((la,lo))
    docs=sorted((y,sum(p[0] for p in L)/len(L),sum(p[1] for p in L)/len(L)) for y,L in byy.items())
    for i,d in enumerate(docs):
        pts=sorted([x for j,x in enumerate(docs) if j!=i]+[(y,la,lo) for (y,la,lo) in GSP[g] if abs(y-d[0])>=1])
        for use in (0,1):
            p=SE.herm([x[:3] for x in track(pts,g,use)],d[0]); e=km(p,d[1:3]); res[use].append(e)
            if any(abs(m-d[0])<6 for (m,_,_) in EC.VMOVE[g]): near[use].append(e)
for u in (0,1): print('dated moves' if u else 'midpoint','all',len(res[u]),round(st.median(res[u])),round(st.mean(res[u])),'within 6 yr of a move',len(near[u]),round(st.median(near[u])),round(st.mean(near[u])))
