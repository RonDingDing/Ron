Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def choose_class(name):
	if name == "foo":
		class Foo(Object):
			pass
		return Foo
	eles:
		
SyntaxError: invalid syntax
>>> def choose_class(name):
	if name == "foo":
		class Foo(object):
			pass
		return Foo
	else:
		class Bar(object):
			pass
		return Bar

	
>>> MyClass = choose_class('foo')
>>> print(MyClass)
<class '__main__.choose_class.<locals>.Foo'>
>>> print(MyClass())
<__main__.choose_class.<locals>.Foo object at 0x0028FB50>
>>> 
