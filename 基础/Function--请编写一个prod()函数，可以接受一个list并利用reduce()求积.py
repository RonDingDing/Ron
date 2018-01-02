from functools import reduce

def prod(li):    
    def times(x, y):
        return x *y
    return reduce(times, li)
    
