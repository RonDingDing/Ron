data = b'Hello World'
print(data[0:5])
# b'Hello'
print(data.startswith(b'Hello'))
# True
print(data.split())
# [b'Hello', b'World']
print(data.replace(b'Hello', b'Hello Cruel'))
# b'Hello Cruel World'



data = bytearray(b'Hello World')
print(data[0:5])
bytearray(b'Hello')
print(data.startswith(b'Hello'))
# True
print(data.split())
# [bytearray(b'Hello'), bytearray(b'World')]
print(data.replace(b'Hello', b'Hello Cruel'))
# bytearray(b'Hello Cruel World')


a = 'Hello World' # Text string
print(a[0])
# 'H'
print(a[1])
# 'e'
b = b'Hello World' # Byte string
print(b[0])
# 72
print(b[1])
# 101


s = b'Hello World'
print(s)
# b'Hello World' # Observe b'...'
print(s.decode('ascii'))
# Hello World

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

import os
print(os.listdir('.')) # Text string (names are decoded)
# ['jalapeño.txt']

print(os.listdir(b'.')) # Byte string (names left as bytes)
# [b'jalapen\xcc\x83o.txt']