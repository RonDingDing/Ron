line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
print(re.split(r'[;,\s]\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']


values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(delimiters)
# [' ', ';', ',', ',', ',', '']
 # Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))
# 'asdf fjdk;afed,fjek,asdf,foo'

print(re.split(r'(?:,|;|\s)\s*', line))
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']