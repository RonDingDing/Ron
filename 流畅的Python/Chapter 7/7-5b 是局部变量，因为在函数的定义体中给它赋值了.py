b = 6
def f2(a):
    print(a)
    print(b)
    b = 9


c = 6
def f3(a):
    global c
    print(a)
    print(c)
    c = 9
f3(3)
print(c)