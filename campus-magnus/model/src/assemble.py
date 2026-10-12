"""Write the page's data files from the build.
usage: python3 assemble.py <model dir>   (reads build/data.json and build/geo.json; writes ../data.js and ../geo.js beside index.html)"""
import sys, os
S = sys.argv[1]; X = os.path.dirname(os.path.abspath(S.rstrip('/')))
for src, name, var in [('data.json', 'data.js', 'CM_DATA'), ('geo.json', 'geo.js', 'CM_GEO')]:
    t = open(f'{S}/build/{src}', encoding='utf8').read()
    open(f'{X}/{name}', 'w', encoding='utf8').write(f'window.{var}={t};\n')
