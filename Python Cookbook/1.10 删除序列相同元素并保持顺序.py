>>> def dedupe(items):  #只适合不可哈希类型的去重
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			seen.add(item)

			
>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
>>> list(dedupe(a))
[1, 5, 2, 9, 10]
>>> 
>>> 
>>> 
>>> def dedupe_hashable(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)

			
>>> a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
>>> list(dedupe_hashable(a, key=lambda d: (d['x'], d['y'])))     #x, y都相同
[{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
>>> list(dedupe_hashable(a, key=lambda d: (d['x'])))             #x相同
[{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
 
##################################################################
>>> a = [1, 5, 2, 1, 9, 1, 5, 10]
>>> set(a)
{1, 2, 5, 9, 10}   #这种方法并不能保证顺序


##################################################################

>>> with open (somefile, 'r') as f: #去除重复的行
	for line in dedupe(f):
		print(line)
