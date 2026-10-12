# Coverage of the seasonal halo on withheld season-dated places, with the chosen profile.
import sys,json,math
sys.argv=['x']
exec(open('calib_prof.py').read().rsplit("if __name__=='__main__':",1)[0])
pc=json.load(open('../build/profcal.json')); SE.PROF=tuple(pc['best']); ratios=[]; r0=[]
for g,(docs,gs,lat0,lon0) in CASES.items():
    y0,y1=G[g][4],G[g][5]; years=np.arange(int(y0),int(y1)+1)
    for i,d in enumerate(docs):
        if not d[4]: continue
        t,x,y=d[0],d[1],d[2]; Am,_=SE.estimate(RC[(g,i)],years,5,60,60,g,lat0,lon0); V=SE.estimate.var
        Af=SE.Afun_of(years,Am); P1=hermpts(docs,gs,Af,i)
        if len(P1)<2: continue
        nx,ny_=SE.herm(P1,t); a=Af(t); p=SE.phi(t); e=math.hypot(x-nx-p*a[0],y-ny_-p*a[1])
        k=min(len(years)-1,max(0,int(round(t-years[0])))); b=PVc[(g,i)]+POSP['s0']**2
        ratios.append(e/math.sqrt(b+p*p*V[k])); r0.append(e/math.sqrt(b))
ratios.sort(); c68=ratios[int(.68*len(ratios))]
out=dict(cov_annual_halo=round(sum(r<=1.433 for r in r0)/len(r0),3),cov_with_offset_sd=round(sum(r<=1.433 for r in ratios)/len(ratios),3),c68=round(c68,3),factor=round(c68/1.433,3))
print(out); pc.update(halo=out); pc['halo_factor_season']=out['factor']; pc.pop('c68_season',None); pc.pop('cov_at_1433',None)
json.dump(pc,open('../build/profcal.json','w'),indent=1)
