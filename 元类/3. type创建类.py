#type的正常使用方式
>>> print(type(1))   
<class 'int'>
>>> print(type("1"))
<class 'str'>

#正常创建类
>>> class ObjectCreator(object):
        pass 
>>> print(type(ObjectCreator))
<class 'type'>
>>> print(type(ObjectCreator()))
<class '__main__.ObjectCreator'>
 



#type(类名, 父类元组(), 包含属性和值的字典{:})，这个函数可以创建一个类
>>> MyShinyClass = type('MyShinyClass', (), {})
>>> print(MyShinyClass)
<class '__main__.MyShinyClass'>
>>> print(MyShinyClass())
<__main__.MyShinyClass object at 0x028C1930>




>>> Foo = type('Foo', (), {'bar':True})
>>> #与下面的是等价的
>>> class Foo(object):
	bar = True

	
>>> Foo = type('Foo', (), {'bar':True})
>>> print(Foo)
<class '__main__.Foo'>
>>> print(Foo.bar)
True
>>> f = Foo()
>>> print(f)
<__main__.Foo object at 0x028DD130>
>>> print(f.bar)
True


#type创建类的父类继承
>>> class FooChild(Foo):
	pass
#相当于
>>> FooChild = type('FooChild', (Foo,), {})
>>> print(FooChild)
<class '__main__.FooChild'>
>>> print(FooChild.bar)
True



#加完属性，应该加方法了 
>>> FooChild = type('FooChild', (Foo,), {'not_bar': lambda self: not self.bar})
#这里相当于
#class FooChild(Foo):
        #def not_bar(self): return not self.bar

$注意lambda的参数是正常类情况下的self
>>> f = FooChild()
>>> f.echo_bar()
False
 
