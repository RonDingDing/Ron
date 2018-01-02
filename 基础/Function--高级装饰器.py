##普通装饰器
def decorator(mainFunc):
    def wrapper(arg):
        print('before')
        mainFunc(arg)
        print('after')
    return wrapper

@decorator
def mainFunc(arg):
    print('main %s' % arg)


"""
上段代码执行的结果
>>> mainFunc(1)
before
main 1
after
"""

####################################################################################################################
def beforeFunc(argb):
    print ('before %s' % (argb))
     
def afterFunc(arga):
    print ('after %s' % (arga))
 
 
def deco(beforeFunc,afterFunc):
    def outer(mainFunc2):
        def wrapper(arga, argb, argm):
             
            beforeFunc(argb)    
            mainFunc2(arga, argb, argm)           
            afterFunc(arga)
             
             
        return wrapper
    return outer
     
@deco(beforeFunc,afterFunc)
def mainFunc2(arga, argb, argm):
    print ('index %s %s %s' % (arga, argb, argm))
    
"""
上段代码执行的效果
>>> mainFunc2("a", "b", "m")
before b
index a b m
after a
"""
    
