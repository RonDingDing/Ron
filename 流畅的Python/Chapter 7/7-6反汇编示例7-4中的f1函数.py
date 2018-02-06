b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

from dis import dis
print(dis(f2))