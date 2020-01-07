s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))
# 'Guido has 37 messages.'


name = 'Guido'
n = 37
print(s.format_map(vars()))
# 'Guido has 37 messages.'


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n
 
a = Info('Guido',37)
print(s.format_map(vars(a)))
# 'Guido has 37 messages.'


class safesub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

del n 
print(s.format_map(safesub(vars())))


import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = 'Guido'
n = 37
print(sub('Hello {name}'))
# Hello Guido
print(sub('You have {n} messages.'))
# You have 37 messages.
print(sub('Your favorite color is {color}'))
# Your favorite color is {color}


name = 'Guido'
n = 37
# print('%(name) has %(n) messages.' % vars())
# 'Guido has 37 messages.'


import string
s = string.Template('$name has $n messages.')
print(s.substitute(vars()))
'Guido has 37 messages.'
