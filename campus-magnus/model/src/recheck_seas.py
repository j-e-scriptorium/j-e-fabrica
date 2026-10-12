import sys,json,math,statistics as st
sys.argv=['x']
exec(open('calib_prof.py').read().rsplit("if __name__=='__main__':",1)[0])
pc=json.load(open('../build/profcal.json'))
r=run2(tuple(pc['best'])); rc=run2(None)
SE.PROF=tuple(pc['best'])
r0=run(5,60,60)   # base (no offset) from calib_seas
print('chosen',r,'cosine',rc,'base',r0['base'])
