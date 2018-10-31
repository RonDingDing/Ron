import math
a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
# inf
print(b)
# -inf
print(c)
# nan



print(math.isinf(a))
# True
print(math.isnan(c))
# True

 

a = float('inf')
print(a + 45)
# inf
print(a * 10)
# inf
print(10 / a)
# 0.0

 
a = float('inf')
print(a/a)
# nan
b = float('-inf')
print(a + b)
# nan

 
c = float('nan')
print(c + 23)
# nan
print(c / 2)
# nan
print(c * 2)
# nan
print(math.sqrt(c))
# nan

 
c = float('nan')
d = float('nan')
print(c == d)
# False
print(c is d)
# False


