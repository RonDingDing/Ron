class A:  #经典类，3.0开始已经废除，
    n = 'A'
    def f2(self):
        print("f2 from A")
        
class B(A):
    n = 'B'
    def f1(self):
        print("f1 from B")
    #def f2(self):
        #print("f2 from B")
class C(A):
    n = 'C'
    def f2(self):
        print("f2 from C")

class D(B, C):
    pass

"""
未加注释中的两句
>>> d = D()
>>> d.f1()
f1 from B
>>> d.f2()
f2 from C
"""


"""
加了注释中的两句
>>> d = D()
>>> d.f1()
f1 from B
>>> d.f2()
f2 from B
"""

"""
D 的 f2 先去 B 然后 C

        A.f2

B.f2             C.f2
        D


D--B--C--A同一级别顺序找一遍，然后往上
这叫广度优先
D--B--A
深度优先
"""

class Animal2(object): #新式类
    pass
