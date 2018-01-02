"""
def login(func):
    print("Passed user verification...")
    return func


def home(name):
    print("Welcome [%s] to home page" % name)

def tv(name):
    print("Welcome [%s] to TV page" % name)

def movie(name):
    print("Welcome [%s] to movie page" % name)


tv=login(tv)
tv("ron")
home = login(home)
home("ron")
"""

#这种方法可以用装饰器实现
def login(func):
    def inner(*arg, **kwargs):
        print("Passed user verification...")
        return func(*arg, **kwargs) #不加return，被装饰的函数返回值会失效
    return inner
#这种装饰器应该是通用的

@login
def movie(name):
    print("Welcome [%s] to movie page" % name)

@login
def tv(name, password):
    print("Welcome [%s], [$%s] to tv page" % (name, password))
    return 4 
    
movie("ron")
tv("ron", "111")


