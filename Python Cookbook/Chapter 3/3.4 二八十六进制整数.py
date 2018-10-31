x = 1234
print(bin(x))
# '0b10011010010'
print(oct(x))
# '0o2322'
print(hex(x))
# '0x4d2'

x = -1234
print(format(x, 'b'))
# '-10011010010'
print(format(x, 'x'))
# '-4d2'


x = -1234
print(format(2**32 + x, 'b'))
# '11111111111111111111101100101110'
print(format(2**32 + x, 'x'))
# 'fffffb2e'

print(int('4d2', 16))
# 1234
print(int('10011010010', 2))
# 1234
