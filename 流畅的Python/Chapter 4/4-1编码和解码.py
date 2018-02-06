##>>> s = 'café'
##>>> len(s)
##4
##>>> b = s.encode('utf-8')
##>>> b
##b'caf\xc3\xa9'
##>>> len(b)
##5
##>>> b.decode('utf-8')
##'café'
