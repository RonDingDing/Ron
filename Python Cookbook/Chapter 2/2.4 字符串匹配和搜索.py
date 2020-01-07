text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')
# False
# Match at start or end
print(text.startswith('yeah'))
# True
print(text.endswith('no'))
# False
# Search for the location of the first occurrence
print(text.find('no'))
# 10


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
 
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# yes

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')
 
# no



datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

# yes

if datepat.match(text2):
    print('yes')
else:
    print('no')

# no


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# ['11/27/2012', '3/13/2013']



datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m)
# <_sre.SRE_Match object at 0x1005d2750>
  
# Extract the contents of each group
print(m.group(0))
# '11/27/2012'
print(m.group(1))
# '11'
print(m.group(2))
# '27'
print(m.group(3))
# '2012'
print(m.groups())
# ('11', '27', '2012')
month, day, year = m.groups()


# Find all matches (notice splitting into tuples)
print(text)
# 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
# [('11', '27', '2012'), ('3', '13', '2013')]
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))
 
# 2012-11-27
# 2013-3-13
 

for m in datepat.finditer(text):
    print(m.groups())
# ('11', '27', '2012')
# ('3', '13', '2013')


m = datepat.match('11/27/2012abcdef')
print(m)
# <_sre.SRE_Match object at 0x1005d27e8>
print(m.group())
# '11/27/2012'


datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
# None
print(datepat.match('11/27/2012'))
# <_sre.SRE_Match object at 0x1005d2750>
 

print(re.findall(r'(\d+)/(\d+)/(\d+)', text))
# [('11', '27', '2012'), ('3', '13', '2013')]