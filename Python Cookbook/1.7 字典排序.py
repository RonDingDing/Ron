Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import OrderedDict
>>> d = OrderedDict()
>>> d['foo'] = 1
>>> d['bar'] = 2
>>> d['spam'] = 3
>>> d['grok'] = 4
>>> d
OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])
 
>>> for key in d:
	print(key, d[key])

	
foo 1
bar 2
spam 3
grok 4
>>> 
>>> import json
>>> json.dumps(d)
'{"foo": 1, "bar": 2, "spam": 3, "grok": 4}'
>>> 
