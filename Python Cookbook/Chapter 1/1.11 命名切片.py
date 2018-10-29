
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 51325.0


SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2: 4])
# [2, 3]
print(items[a])
# [2, 3]
items[a] = [10, 11]
print(items)
# [0, 1, 10, 11, 4, 5, 6]
del items[a]
print(items)
# [0, 1, 4, 5, 6]


s = slice(5, 50, 2)
print(s.start)
# 5
print(s.stop)
# 50
print(s.step)
# 2
b = "HelloWorld"
print(a.indices(len(b)))
# (2, 4, 1)
for i in range(*a.indices(len(b))):
    print(b[i])


# l
# l
s = "HelloWorld"
print(a.indices(len(s)))
# (2, 4, 1)
for i in range(*a.indices(len(s))):
    print(s[i])


# l
# l

a = slice(1, 10)
print(a)
# slice(1, 10, None)
print(a.indices(10))
# (1, 10, 1)
print(a.indices(9))
# (1, 9, 1)
print(a.indices(8))
# (1, 8, 1)
a = slice(3, 5)
print(a.indices(4))
# (3, 4, 1)
print(a.indices(3))
# (3, 3, 1)
