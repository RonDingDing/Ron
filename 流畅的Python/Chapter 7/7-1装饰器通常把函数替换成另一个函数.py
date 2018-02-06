def deco(func):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print('running target()')

    
##>>> target()
##running inner()
##>>> target
##<function deco.<locals>.inner at 0x02C6C738>
##>>> 
