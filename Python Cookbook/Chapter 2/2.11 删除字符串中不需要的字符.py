# Whitespace stripping
s = ' hello world \n'
print(s.strip())
# 'hello world'
print(s.lstrip())
# 'hello world \n'
print(s.rstrip())
# ' hello world'
  
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
# 'hello====='
print(t.strip('-='))
# 'hello'
 

s = ' hello     world \n'
s = s.strip()
print(s)
'hello     world'

print(s.replace(' ', ''))
# 'helloworld'
import re
print(re.sub('\s+', ' ', s))
# 'hello world'

filename = "somefile.txt"
with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)