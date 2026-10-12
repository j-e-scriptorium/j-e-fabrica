import json,sys
from collections import defaultdict
d=json.load(open(sys.argv[1]));G={g['id']:g for g in d['groups']}
def pop(gid,y):
    g=G[gid];pa=d['tracks'][gid]['pa']
    if not(g['start']<=y<g['end'] or (y==g['end']==1905)):return 0
    return pa[min(len(pa)-1,int(y-1700))]
Y=[1700,1750,1775,1785,1800,1820,1836,1840,1850,1860,1870,1880,1890,1905]
T=defaultdict(dict)
for gid,g in G.items():
    if g['fam']=='unident':continue
    for y in Y:T[g['tribe']][y]=T[g['tribe']].get(y,0)+pop(gid,y)
print('tribe'.ljust(14),' '.join(str(y).rjust(6) for y in Y))
for t in sorted(T):print(t.ljust(14),' '.join(str(round(T[t][y])).rjust(6) for y in Y))
print('TOTAL'.ljust(14),' '.join(str(round(sum(T[t][y] for t in T))).rjust(6) for y in Y))
