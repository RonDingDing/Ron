import weakref
s1 = {1,2,3}
s2 = s1
def bye1():
    print("s1 Gone")
ender = weakref.finalize(s1, bye1)
print(ender.alive)
del s1
print(ender.alive)
s2 = "spam"
print(ender.alive)
