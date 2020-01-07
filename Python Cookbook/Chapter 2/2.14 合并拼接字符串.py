parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
# 'Is Chicago Not Chicago?'
print(','.join(parts))
# 'Is,Chicago,Not,Chicago?'
print(''.join(parts))
# 'IsChicagoNotChicago?'


a = 'Is Chicago'
b = 'Not Chicago?'
print(a + ' ' + b)
# 'Is Chicago Not Chicago?'


print('{} {}'.format(a, b))
# 'Is Chicago Not Chicago?'
print(a + ' ' + b)
# 'Is Chicago Not Chicago?'


a = 'Hello' 'World'
print(a)
'HelloWorld'


data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))
# 'ACME,50,91.1'

c =  's'
print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))  # Still ugly
print(a, b, c, sep=':')  # Better

# Version 1 (string concatenation)
f = open('2.txt', 'w')
chunk1 = "1"
chunk2 = "2"
f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
f.write(chunk1)  # 如果两个字符串很小，那么第一个版本性能会更好些，因为I/O系统调用天生就慢。
f.write(chunk2)  # 如果两个字符串很大，那么第二个版本可能会更加高效， 因为它避免了创建一个很大的临时结果并且要复制大量的内存块数据。


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


text = ''.join(sample())


for part in sample():
    f.write(part)


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


# 结合文件操作
with open('filename', 'w') as f:
    for part in combine(sample(), 32768):
        f.write(part)
