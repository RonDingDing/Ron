 
>>> record = '....................100 .......513.25 ..........'
>>> cost = int(record[20:23]) * float(record[31:37])
>>> cost
51325.0
>>> 
>>> 
>>> SHARES = slice(20, 23)
>>> PRICE = slice(31, 37)
>>> cost = int(record[SHARES]) * float(record[PRICE])
>>> 
>>> items = [0, 1, 2, 3, 4, 5, 6]
>>> a = slice(2, 4)
>>> items[2: 4]
[2, 3]
>>> items[a]
[2, 3]
>>> items[a] = [10, 11]
>>> items
[0, 1, 10, 11, 4, 5, 6]
>>> del items[a]
>>> items
[0, 1, 4, 5, 6]
>>> 
>>> 
>>> s = slice(5, 50, 2)
>>> s.start
5
>>> s.stop
50
>>> s.step
2
>>> b = "HelloWorld"
>>> a.indices(len(b))
 
>>> for i in range(*a.indices(len(b))):
	print(b[i])

	
l
l
>>> s = "HelloWorld"
>>> a.indices(len(s))
(2, 4, 1)
>>> for i range(*a.indices(len(s))):
	
SyntaxError: invalid syntax
>>> for i in range(*a.indices(len(s))):
	print(s[i])

	
l
l
>>> 
=============================== RESTART: Shell ===============================
>>> a = slice(1, 10)
>>> a
slice(1, 10, None)
>>> a.indices(10)
(1, 10, 1)
>>> a.indices(9)
(1, 9, 1)
>>> a.indices(8)
(1, 8, 1)
>>> a = slice(3, 5)
>>> a.indices(4)
(3, 4, 1)
>>> a.indices(3)
(3, 3, 1)
>>> 
