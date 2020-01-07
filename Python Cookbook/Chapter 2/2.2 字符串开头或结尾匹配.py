import os
filename = 'spam.txt'
print(filename.endswith('.txt'))
# True
print(filename.startswith('file:'))
# False
url = 'http://www.python.org'
print(url.startswith('http:'))
# True


filenames = os.listdir('.')
print(filenames)
# [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
print([name for name in filenames if name.endswith(('.c', '.h'))])
# ['foo.c', 'spam.c', 'spam.h'
print(any(name.endswith('.py') for name in filenames))
# True


filenames = os.listdir('.')
print(filenames)
# ['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h']
print([name for name in filenames if name.endswith(('.c', '.h'))])
# ['foo.c', 'spam.c', 'spam.h'
print(any(name.endswith('.py') for name in filenames))
# True


choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# url.startswith(choices)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))
# True

filename = 'spam.txt'
print(filename[-4:] == '.txt')
# True
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')
# True
