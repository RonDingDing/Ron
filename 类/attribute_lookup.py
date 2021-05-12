from typing import Any


# coding=utf-8
class DataDescriptor(object):
    def __init__(self, init_value):
        self.value = init_value

    def __get__(self, instance, typ):
        return "DataDescriptor __get__"

    def __set__(self, instance, value):
        print("DataDescriptor __set__")
        self.value = value


class NonDataDescriptor(object):
    def __init__(self, init_value):
        self.value = init_value

    def __get__(self, instance, typ):
        return "NonDataDescriptor __get__"


class Base(object):
    dd_base = DataDescriptor(0)
    ndd_base = NonDataDescriptor(0)


class Derive(Base):
    dd_derive = DataDescriptor(0)
    ndd_derive = NonDataDescriptor(0)
    same_name_attr = "attr in class"

    def __init__(self):
        self.not_des_attr = "I am not descriptor attr"
        self.same_name_attr = "attr in object"

    def __getattr__(self, key):
        return "__getattr__ with key %s" % key

    def change_attr(self):
        self.__dict__["dd_base"] = "dd_base now in object dict "
        self.__dict__["ndd_derive"] = "ndd_derive now in object dict "


def main():
    b = Base()
    d = Derive()
    print("Derive object dict", d.__dict__)
    assert d.dd_base == "DataDescriptor __get__"
    assert d.ndd_derive == "NonDataDescriptor __get__"
    assert d.not_des_attr == "I am not descriptor attr"
    assert d.no_exists_key == "__getattr__ with key no_exists_key"
    assert d.same_name_attr == "attr in object"
    d.change_attr()
    print("Derive object dict", d.__dict__)
    assert d.dd_base != "dd_base now in object dict "
    assert d.ndd_derive == "ndd_derive now in object dict "

    try:
        b.no_exists_key
    except Exception as e:
        assert isinstance(e, AttributeError)


if __name__ == "__main__":
    main()


# 按照python doc，如果obj是某个类的实例，那么obj.name（以及等价的getattr(obj,'name')）首先调用__getattribute__。如果类定义了__getattr__方法，那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，而对于描述符(__get__)的调用，则是发生在__getattribute__内部的。官网文档是这么描述的

#     The implementation works through a precedence chain that gives data descriptors priority over instance variables, instance variables priority over non-data descriptors, and assigns lowest priority to __getattr__() if provided.

#     obj = Clz(), 那么obj.attr 顺序如下：
#     （1）如果“attr”是出现在Clz或其基类的__dict__中， 且attr是data descriptor， 那么调用其__get__方法, 否则

#     （2）如果“attr”出现在obj的__dict__中， 那么直接返回 obj.__dict__['attr']， 否则

#     （3）如果“attr”出现在Clz或其基类的__dict__中

#         （3.1）如果attr是non-data descriptor，那么调用其__get__方法， 否则

#         （3.2）返回 __dict__['attr']

#     （4）如果Clz有__getattr__方法，调用__getattr__方法，否则

#     （5）抛出AttributeError
