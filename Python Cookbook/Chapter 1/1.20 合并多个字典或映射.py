a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

from collections import ChainMap
c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
# 1
print(c['y']) # Outputs 2 (from b)
# 2
print(c['z']) # Outputs 3 (from a)
# 3

print(len(c))
# 3
print(list(c.keys()))
# ['x', 'y', 'z']
print(list(c.values()))
# [1, 2, 3]
 
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# {'w': 40, 'z': 10}
# del c['y']

# Traceback (most recent call last):
# ...
# KeyError: "Key not found in the first mapping: 'y'"

values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
# ChainMap({'x': 3}, {'x': 2}, {'x': 1})
print(values['x'])
# 3
# Discard last mapping
values = values.parents
print(values['x'])
2
#  Discard last mapping
values = values.parents
print(values['x'])
# 1
print(values)
# ChainMap({'x': 1})


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = dict(b)
merged.update(a)
print(merged['x'])
# 1
print(merged['y'])
# 2
print(merged['z'])
# 3

a['x'] = 13
print( merged['x'])
# 1


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
merged = ChainMap(a, b)
print(merged['x'])
# 1
a['x'] = 42
print( merged['x']) # Notice change to merged dicts
# 42