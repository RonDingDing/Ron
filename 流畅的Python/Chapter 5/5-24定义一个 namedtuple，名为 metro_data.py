metro_data = [
 ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
 ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
 ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
 ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
 ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
 ]

from collections import namedtuple
LatLong = namedtuple('LatLong', 'lat long') 
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) 
               for name, cc, pop, (lat, long) in metro_data]
print(metro_areas[0])
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722,
long=139.691667))
print(metro_areas[0].coord.lat)
#35.689722
from operator import attrgetter
import operator
name_lat = attrgetter('name', 'coord.lat') 

for city in sorted(metro_areas, key=attrgetter('coord.lat')): 
    print(name_lat(city)) 

 
##('Sao Paulo', -23.547778)
##('Mexico City', 19.433333)
##('Delhi NCR', 28.613889)
##('Tokyo', 35.689722)
##('New York-Newark', 40.808611)


print([name for name in dir(operator) if not name.startswith('_')])

##['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains',
##'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt',
##'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imod', 'imul',
##'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift',
##'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le',
##'length_hint', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne',
##'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub',
##'truediv', 'truth', 'xor']
