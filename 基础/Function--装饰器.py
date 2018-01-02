def log(func):
    def wrapper():
        print("before call")
        func()
           
    return wrapper
    

@log
def f1():
    print("f1")
