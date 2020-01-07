import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# <_sre.SRE_Match object at 0x1007d9ed0>
# Arabic digits
print(num.match('\u0661\u0662\u0663'))
# <_sre.SRE_Match object at 0x101234030>

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s)) # Matches
# <_sre.SRE_Match object at 0x10069d370>
print(pat.match(s.upper())) # Doesn't match
# None

print(s.upper()) # Case folds
# 'STRASSE'
 