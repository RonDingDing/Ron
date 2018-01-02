import random


def beforeFunc(arg):
    print ('before %s' % (arg))
     
def afterFunc(arg):
    print ('after %s' % (arg))
 
 
def deco(beforeFunc,afterFunc):
    def outer(mainFunc2):
        def wrapper(*args):
            rand1 = random.randint(0, len(args)-1)
            rand2 = random.randint(0, len(args)-1)

            
            beforeFunc(args[rand1])    
            mainFunc2(*args)           
            afterFunc(args[rand2])    
             
             
        return wrapper
    return outer
     
@deco(beforeFunc,afterFunc)
def mainFunc2(*args):
    print ( args)

"""
如果传入"a", "b", "m"三个参数
>>> mainFunc2("a", "b", "m")
before a
('a', 'b', 'm')
after b
>>> mainFunc2("a", "b", "m")
before b
('a', 'b', 'm')
after m
>>> mainFunc2("a", "b", "m")
before b
('a', 'b', 'm')
after a
"""
