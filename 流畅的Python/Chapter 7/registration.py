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


    
