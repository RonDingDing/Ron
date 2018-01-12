class C: pass  
obj = C()  
def func(): pass  
print(sorted(set(dir(func)) - set(dir(obj))))
#['__annotations__', '__call__', '__closure__', '__code__', '__defaults__','__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
