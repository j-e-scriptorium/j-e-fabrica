# Local planar coordinates for a division's positions: km east and north of a reference point.
import math
def local(lat0,lon0,lat,lon): return ((lon-lon0)*111*math.cos(math.radians(lat0)),(lat-lat0)*111)
def unlocal(lat0,lon0,x,y): return (lat0+y/111, lon0+x/(111*math.cos(math.radians(lat0))))
