from collections import namedtuple
import re
text = 'foo = 23 + 42 * 10'

tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

scanner = master_pat.scanner(text)
print(scanner.match())
result = scanner.match()
print(result.lastgroup, result.group())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


# Example use
for tok in generate_tokens(master_pat, text):
    print(tok)

# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')


tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
print('\n')
for tok in tokens:
    print(tok)

# Token(type='NAME', value='foo')
# Token(type='EQ', value='=')
# Token(type='NUM', value='23')
# Token(type='PLUS', value='+')
# Token(type='NUM', value='42')
# Token(type='TIMES', value='*')
# Token(type='NUM', value='10')

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))


PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))
print('\n')
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)
# Token(type='PRINT', value='print')
# Token(type='NAME', value='er')