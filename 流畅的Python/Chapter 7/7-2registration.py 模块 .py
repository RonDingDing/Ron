registry = []

def register(func):
    print("Running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("Running f1()")

@register
def f2():
    print("Running f2()")

def f3():
    print("Running f3()")

def main():
    print("Running main()")
    print("Registry ->", registry)
    f1()
    f2()
    f3()

if __name__ == "__main__":
    main()
    print('\n')
    import registration
    ##Running register(<function f1 at 0x02BBC930>)
    ##Running register(<function f2 at 0x02BBC8E8>)
    ##import时装饰函数已经运行，而被装饰函数没有运行
    ## registration.registry 
    #[<function f1 at 0x02BBC930>, <function f2 at 0x02BBC8E8>]


    
