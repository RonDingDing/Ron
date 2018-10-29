text = 'Hello World'
print(text.ljust(20))
# 'Hello World         '
print(text.rjust(20))
# '         Hello World'
print(text.center(20))
# '    Hello World     '

print(text.rjust(20,'='))
# '=========Hello World'
print(text.center(20,'*'))
# '****Hello World*****'


print(format(text, '>20'))
# '         Hello World'
print(format(text, '<20'))
# 'Hello World         '
print(format(text, '^20'))
# '    Hello World     '

print(format(text, '=>20s'))
# '=========Hello World'
print(format(text, '*^20s'))
# '****Hello World*****'


print('{:>10s} {:>10s}'.format('Hello', 'World'))
# '     Hello      World'


x = 1.2345
print(format(x, '>10'))
# '    1.2345'
print(format(x, '^10.2f'))
# '   1.23   '


print('%-20s' % text)
# 'Hello World         '
print('%20s' % text)
# '         Hello World'