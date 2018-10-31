from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
# Decimal('6.3')
print(a + b)
# 6.3
print((a + b) == Decimal('6.3'))
# True


from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
# 0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)
 
# 0.765
with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)
 
# 0.76470588235294117647058823529411764705882352941176


nums = [1.23e+18, 1, -1.23e+18]
import math
print(math.fsum(nums))