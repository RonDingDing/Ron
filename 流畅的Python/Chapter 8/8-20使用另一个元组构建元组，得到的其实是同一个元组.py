t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)
t3 = t1[:]
print(t3 is t1)

#str、bytes 和 frozenset 实例也有这种行为。