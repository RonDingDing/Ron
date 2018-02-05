from functools import wraps
def coroutine(func):
    """装饰器：向前执行到第一个`yield`表达式，预激`func`"""
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer

@coroutine
def averager():
    """被装饰的函数"""
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

##>>> coro_avg = averager()
##>>> from inspect import getgeneratorstate
##>>> getgeneratorstate(coro_avg)
##'GEN_SUSPENDED'
##>>> coro_avg.send(10)
##10.0
##>>> coro_avg.send(30)
##20.0
##>>> coro_avg.send(5)
##15.0

##>>> coro_avg.send('spam')
##Traceback (most recent call last):
##  File "<pyshell#4>", line 1, in <module>
##    coro_avg.send('spam')
##  File "E:\Python\流畅的Python\Chapter 16\16-5.6预激协程的装饰器.py", line 19, in averager
##    total += term
##TypeError: unsupported operand type(s) for +=: 'float' and 'str'
