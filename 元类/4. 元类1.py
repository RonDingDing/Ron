#知道type可以创造类之后，我们要知道另一个事实，type也是一种元类
Myclass = METAClass() #将元类实例化成类
myObject = Myclass    #将类实例化为对象




>>> age = 35
>>> age.__class__
<class 'int'>
>>> name = "bob"
>>> name.__class__
<class 'str'>
>>> def foo: pass
SyntaxError: invalid syntax
>>> def foo(): pass

>>> foo.__class__
<class 'function'>
>>> class Bar:pass

>>> b = Bar()
>>> b.__class__
<class '__main__.Bar'>
>>> ###__class__的__class__
>>> 
>>> age.__class__.__class__
<class 'type'>
>>> name.__class__.__class__
<class 'type'>
>>> foo.__class__.__class__
<class 'type'>
>>> b.__class__.__class__
<class 'type'>
 
#Python在创建类的时候，先调用__metaclass__，然后是__new__，然后__new__中调用__init__
#如果是旧式类，找不到__metaclass__会去模块中找模块中的__metaclass__
#现在试试用一个函数加上type来创建元类，把元类中类的所有属性变成大写

 
 	
>>> def upper_attr(future_class_name, future_class_parent, future_class_attr):
	"""
	返回一个类的对象，类中所有属性都变成大写
	"""
	#找到不以"__"开头的属性并将它们变成大写
	uppercase_attr = {}
	for name, val in future_class_attr.items():
		if not name.startswith("__"):
			uppercase_attr[name.upper()] = val
		else:
			uppercase_attr[name] = val
	#最后一步，使用type把类创建出来并作为函数upper_attr的结果返回
	return type(future_class_name, future_class_parent, uppercase_attr)

>>> __metaclass__ = upper_attr
>>> 
>>> class Foo():
	bar = "bip"

	
>>> print(hasattr(Foo, 'bar'))
False
>>> print(hasattr(Foo, 'BAR'))
True


#使用类来表示
>>> class UpperAttrMetaclass(type): 
    # __new__ is the method called before __init__
    # it's the method that creates the object and returns it
    # while __init__ just initializes the object passed as parameter
    # you rarely use __new__, except when you want to control how the object
    # is created.
    # here the created object is the class, and we want to customize it
    # so we override __new__
    # you can do some stuff in __init__ too if you wish
    # some advanced use involves overriding __call__ as well, but we won't
    # see this
        def __new__(upperattr_metaclass, future_class_name,\
                    future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type(future_class_name, future_class_parents, uppercase_attr)


#改进一下
>>> class UpperAttrMetaclass(type): 

    def __new__(upperattr_metaclass, future_class_name, 
                future_class_parents, future_class_attr):

        uppercase_attr = {}
        for name, val in future_class_attr.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        # reuse the type.__new__ method
        # this is basic OOP, nothing magic in there
        return type.__new__(upperattr_metaclass, future_class_name, 
                            future_class_parents, uppercase_attr)



#其实，我有默认版本
>>> class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return type.__new__(cls, clsname, bases, uppercase_attr)


#最后再用super方法调用new，减低继承时无法找到父类相应函数的压力
>>> class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

>>> 
