from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
# True
print(fnmatch('foo.txt', '?oo.txt'))
# True
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
# True
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])
# ['Dat1.csv', 'Dat2.csv']


print(fnmatch('foo.txt', '*.TXT'))
# False
# On Windows
print(fnmatch('foo.txt', '*.TXT'))
# True

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

from fnmatch import fnmatchcase
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
# ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])
# ['5412 N CLARK ST']
