print(round(1.23, 1))
# 1.2
print(round(1.27, 1))
# 1.3
print(round(-1.27, 1))
# -1.3
print(round(1.25361,3))
# 1.254

# round 函数返回离它最近的偶数。 

a = 1627731
print(round(a, -1))
# 1627730
print(round(a, -2))
# 1627700
print(round(a, -3))
# 1628000


x = 1.23456
print(format(x, '0.2f'))
# '1.23'
print(format(x, '0.3f'))
# '1.235'
print('value is {:0.3f}'.format(x))
# 'value is 1.235'


a = 2.1
b = 4.2
c = a + b
print(c)
# 6.300000000000001
c = round(c, 2) # "Fix" result (???)
print(c)
# 6.3