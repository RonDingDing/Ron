Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> p = (4,5)
>>> x, y = p
>>> x
4
>>> y
5

###########################################


>>> data = ['ACME', 50, 91.1, (2012,12,21)]
>>> name, shares, price, date = data
>>> name
'ACME'
>>> shares
50
>>> date
(2012, 12, 21)
>>> name, shares, price, (year, mon, day)=data
>>> year
2012
>>> mon
12
>>> y
5
>>> day
21
>>> s = 'hello'
>>> a, b, c, d, e = s
>>> a
'h'
>>> b
'e'
>>> e
'o'
>>> data = ['ACME', 50, 91.1, (2012,12,21)]
>>> _, shares, price, _ = data
>>> shares
50
>>> price
91.1


