import shelve

d = shelve.open('shelve_text') #打开一个文件


t1 =  123
t2 =  {1:2,2:3}
name = ['alex', 'rain', 'test']

d['test'] = name
d['t1'] = t1
d['t2'] = t2
d.close()

"""
>>> a = shelve.open("shelve_text")
>>> a['t1']
123
>>> a['t2']
{1: 2, 2: 3}
>>> a['test']
['alex', 'rain', 'test']
"""
