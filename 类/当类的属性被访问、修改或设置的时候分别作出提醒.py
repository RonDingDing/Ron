class MyDes:
    def __init__(self, value=None, name=None): #这里的self是自带参数，value和name与下面的10和“x”对应
        self.value = value
        self.name = name
    
    def __get__ (self, instance, owner):
        print ("正在获取变量：",self.name)
        return self.value

    def __set__ (self, instance, value):
        print ("正在修改变量：",self.name)
        self.value = value
        
        
    def __delete__ (self, instance):  #尝试删除时，因为修改了魔法方法，所以这里并没有真正删除
        print ("正在修改变量：", self.name)
        print ("噢~这个变量没法删除~")

class Test:
    x = MyDes(10, "x")
