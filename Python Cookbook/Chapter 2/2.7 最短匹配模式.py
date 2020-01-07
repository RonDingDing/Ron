import re

str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
# ['no.']
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
# ['no." Phone says "yes.']
 

str_pat = re.compile(r'"(.*?)"')
print(str_pat.findall(text2))
# ['no.', 'yes.']
