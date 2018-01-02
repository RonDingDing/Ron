class ListMetaclass(type):
    def __new__(cls, clsname, bases, attrs):
    #(自己本身，要元类下新建的类名，继承的父类，属性及方法构成的字典)
        attrs['add'] = lambda self, value: self.append(value)
        return super(ListMetaclass, cls).__new__(cls, clsname, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

"""
>>> a = MyList()
>>> a.add(3)
>>> a
[3]
>>> a.append(4)
>>> a
[3, 4]
>>> 

"""

