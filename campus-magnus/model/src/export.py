import json,csv,sys
sys.path.insert(0,sys.argv[1]); S=sys.argv[2]
import data_src as D, bands_src as B
d=json.load(open(f'{S}/build/data.json',encoding='utf-8')); rows=json.load(open(f'{S}/build/bandrows.json',encoding='utf-8'))
G={g['id']:g for g in d['groups']}; O=f'{S}/out/'
def W(name,head,data):
    with open(O+name,'w',newline='',encoding='utf-8') as f: w=csv.writer(f); w.writerow(head); w.writerows(data)
bname={u['id']:u['name'] for sp in d['bands'].values() for u in sp['units']}
W('plains_documented_records.csv',['year','groups','tribe','division_or_scope','band_or_village','persons','basis','source_text','place_basis','lat','lon','place_radius_km','source','kind','counts_whole_division','source_family','family_factor'],
  [[o['y'],';'.join(o['g']),G[o['g'][0]]['tribe'],'whole tribe / several divisions' if o['agg'] else G[o['g'][0]]['name'],bname.get(o['band'],'') if o['band'] else '',o['pop'] if o['pop'] is not None else '',o['basis'],o['raw'],o['loc'],o['lat'],o['lon'],o['r'],o['src'],o['kind'],'yes' if o['whole'] else 'no',o.get('fam',''),o.get('famf','')] for o in d['obs']])
W('plains_best_guess_keyframes.csv',['group','tribe','division','year','lat','lon','persons_anchor','note'],
  [[gid,G[gid]['tribe'],G[gid]['name'],y,(pl[0] if pl else ''),(pl[1] if pl else ''),pp if pp else '',n] for gid,L in D.GUESS.items() for (y,pl,pp,n) in L])
W('plains_epidemic_model.csv',['start','end','event','group','division','mortality_applied','source','basis'],
  [[s_,e,lab,g,G[g]['name'],f,src,basis] for s_,e,lab,M,src,basis in D.EPI for g,f in M.items()])
gids=[g['id'] for g in d['groups'] if g['fam']!='unident']
W('plains_fitted_population.csv',['year']+[G[g]['tribe']+' – '+G[g]['name'] for g in gids],
  [[1700+k]+[(d['tracks'][g]['pa'][k] if G[g]['start']<=1700+k<=G[g]['end'] else '') for g in gids] for k in range(206)])
W('plains_settlements.csv',['name','kind','lat','lon','from','to','checked_against'],[list(x) for x in D.SETTLE])
v=json.load(open(f'{S}/build/validation.json'))
W('plains_validation.csv',['division_id','division','year','documented_persons','predicted_without_it','standardized_miss_before_widening'],[[p[0],G[p[0]]['name'],p[1],p[2],p[3],p[4]] for p in v['points']])
# bands
lists=B.LISTS
W('plains_bands.csv',['division_id','tribe','division','unit_id','name','gloss','kind','weight','forced_start','forced_end','offshoot_or_merges_into','chief_c1856_Hayden','names_source','list_year','note','has_recalled_places'],
  [[gid,G[gid]['tribe'],G[gid]['name'],u['id'],u['name'],u['gloss'],u['kind'],u['w'],u['start'] or '',u['end'] or '',bname.get(u['into'],'') if u['into'] else '',u['chief'] or '',sp['src'],sp['Ly'],u['note'],'yes' if u['track'] else 'no']
   for gid,sp in d['bands'].items() for u in sp['units']])
W('plains_band_population.csv',['division_id','unit_id','name','kind','year','persons_best_guess'],[r[:2]+[r[2],r[3],r[4],r[5]] for r in rows if r[4]%5==0])
W('plains_band_places_recalled.csv',['division_id','unit_id','name','year','lat','lon','note'],
  [[gid,u['id'],u['name'],t[0],t[1],t[2],t[3]] for gid,sp in d['bands'].items() for u in sp['units'] for t in u['track']])
W('plains_band_events.csv',['division_id','unit_id','name','year','fraction_of_band_lost','note'],
  [[gid,u['id'],u['name'],s_[0],s_[1],s_[3]] for gid,sp in d['bands'].items() for u in sp['units'] for s_ in u['shocks']])
print('ok',len(rows))
# positions: annual centre and seasonal offset
import seasonal as SE, ecology_src as EC
SRCN={'d':'fitted to season-dated places','p':'literature pattern','0':'none'}
rowsP=[]
for g in gids:
    tr=d['tracks'][g]
    for y in range(max(1700,G[g]['start']),min(1905,G[g]['end'])+1):
        la,lo=SE.herm(tr['pos'],y+0.5); sv=tr.get('sv'); a=sv[y-1700] if sv else [0,0]
        rowsP.append([g,G[g]['name'],y,round(la,3),round(lo,3),tr['sp'][y-1700],a[0],a[1],(tr['svd'][y-1700] if 'svd' in tr else ''),SRCN[tr['svs'][y-1700]] if 'svs' in tr else 'none'])
W('plains_positions.csv',['division_id','division','year','centre_lat_midyear','centre_lon_midyear','halo_km','summer_offset_east_km','summer_offset_north_km','offset_sd_km_per_axis','offset_basis'],rowsP)
W('plains_seasonal_patterns.csv',['division_id','division','from','to','pattern','source_recalled'],[[g,G[g]['name'],r[0],r[1],r[2],r[3]] for g,L in d['seaspri'].items() for r in L])
W('plains_village_moves.csv',['division_id','division','year','what','source_recalled'],[[g,G[g]['name'],m,t,s] for g,L in EC.VMOVE.items() for (m,t,s) in L])
W('plains_bison_range.csv',['from_year','outline_wkt','source'],[[y,'MULTIPOLYGON('+','.join('(('+','.join(f'{x} {yy}' for x,yy in poly+[poly[0]])+'))' for poly in P)+')' if P else 'EMPTY',EC.HORNADAY] for (y,P) in EC.BISON])
