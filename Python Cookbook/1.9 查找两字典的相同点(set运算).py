Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = {'x': 1, 'y': 2, 'z': 3}
>>> b = {'w': 10, 'x': 11, 'y': 2}
>>> 
>>> a.keys() & b.keys()
{'y', 'x'}
>>> a.keys() - b.keys()
{'z'}
>>> a.items() & b.items()
{('y', 2)}
>>> c = {key: a[key] for key in a.keys() -('z', 'w')}
>>> c
{'y': 2, 'x': 1}
>>> 
