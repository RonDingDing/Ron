#创建一个类
>>> class ObjectCreator(object):
	pass

>>> my_object = ObjectCreator()

>>> print(my_object)
<__main__.ObjectCreator object at 0x0024FB50>



>>> print(hasattr(ObjectCreator, 'new_attribute'))
False
>>> ObjectCreator.new_attribute = "foo"
>>> print(hasattr(ObjectCreator, 'new_attribute'))
True
>>> print(ObjectCreator, 'new_attribute')
<class '__main__.ObjectCreator'> new_attribute
>>> print(ObjectCreator.new_attribute)
foo
>>> ObjectCreatorMirror = ObjectCreator
>>> print(ObjectCreatorMirror.new_attribute)
foo
>>> print(ObjectCreatorMirror())
<__main__.ObjectCreator object at 0x02868A30>
 
