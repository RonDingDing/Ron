class Animal(object):
    def __init__(self, name): #实例属性，在实例化类对象时创建
        self.name = name  #双下划线是私有属性，只允许类对象对自己访问，不允许子类对象及其他访问，_Animal__name可以访问
                          #单下划线是保护属性，只有类对象和子类对象能访问到这些变量
        
    
    hobbie = 'meat' #类属性
   
    """
    >>> cat = Animal("cat")
    >>> cat.hobbie
    'meat'
    >>> cat.hobbie = "running"
    >>> dog = Animal("dog")
    >>> dog.hobbie
    'meat'
    >>> Animal.hobbie = "eating"
    >>> dog.hobbie
    'eating'
    >>> cat.hobbie
    'running'
    >>> elephant = Animal("elephant")
    >>> elephant.hobbie
    'eating'
    观察一下修改类属性，实例属性之后类属性的变化
    """
    
    @classmethod #类方法，不能访问实例变量
    def talk(self):
        print("%s is taliking ..." % self.hobbie)

    """
    >>> Animal.talk()
    meat is taliking ...
    >>> a = Animal("cat")
    >>> a.talk()
    meat is taliking ...
    >>> a.talk() = lambda x: print(2*x)
    SyntaxError: can't assign to function call
    >>> a.talk = lambda x: print(2*x)
    >>> a.talk(22)
    44
    >>> Animal.talk()
    meat is taliking ...

    """



    @staticmethod #静态方法，与实例变量、类变量没有半毛钱关系
                  #自治的，是一个工具箱
    def walk(self):
        print("%s is walking..." % self.name)


    """
    >>> a = Animal("cat")
    >>> a.walk()
    Traceback (most recent call last):
      File "<pyshell#28>", line 1, in <module>
        a.walk()
    TypeError: walk() missing 1 required positional argument: 'self'
    >>> a.walk("s")
    Traceback (most recent call last):
      File "<pyshell#29>", line 1, in <module>
        a.walk("s")
      File "D:/Dpan/学习资料/Learning Outside Classes/IT/Python实例/类/@classmethod, @property, @staticmethod.py", line 48, in walk
        print("%s is walking..." % self.name)
    AttributeError: 'str' object has no attribute 'name'

    观察错误，这时的self已经不是类中指代自身的self了，而是字符串“s”，
    该方法只是一个挂名在该类下的僵尸方法，它的心属于外面的世界
    """




    
    @property    #把方法变成属性
    def feet(self):
        if self.num:
            return self.num
        else:
            return 4
    """
    >>> a = Animal("cat")
    >>> a.feet()
    Traceback (most recent call last):
      File "<pyshell#31>", line 1, in <module>
        a.feet()
    TypeError: 'int' object is not callable
    >>> a.feet
    4
    """

    @feet.setter    #改值，名称要和上面的一样
    def feet(self, num):
        self.num = num
        print("feet:", self.num)

    """
    >>> a = Animal("cat")
    >>> a.feet
    4
    >>> a.feet = 33
    feet: 33
    >>> a.feet
    33
    """
    @feet.deleter    #改值，名称要和上面的一样
    def feet(self):
        del self.num
        print("feet got deleted.")


    """
    >>> a = Animal("cat")
    >>> a.feet
    4
    >>> a.feet = 2
    feet: 2
    >>> a.feet
    2
    >>> a.num
    2
    >>> del a.feet
    feet got deleted.
    >>> a.feet
    Traceback (most recent call last):
      File "<pyshell#45>", line 1, in <module>
        a.feet
      File "D:\Dpan\学习资料\Learning Outside Classes\IT\Python实例\类\@classmethod, @property, @staticmethod.py", line 79, in feet
        return self.num
    AttributeError: 'Animal' object has no attribute 'num'
    """
