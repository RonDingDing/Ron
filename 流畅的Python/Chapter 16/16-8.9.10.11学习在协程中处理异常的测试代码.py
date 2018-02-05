class DemoException(Exception):
    """为这次演示定义的异常类型。"""

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')

        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.') 


##>>> exc_coro = demo_exc_handling()
##>>> next(exc_coro)
##-> coroutine started
##>>> exc_coro.send(11)
##-> coroutine received: 11
##>>> exc_coro.send(22)
##-> coroutine received: 22
##>>> exc_coro.close()
##>>> from inspect import getgeneratorstate
##>>> getgeneratorstate(exc_coro)
##'GEN_CLOSED'


##>>> exc_coro = demo_exc_handling()
##>>> next(exc_coro)
##-> coroutine started
##>>> exc_coro.send(11)
##-> coroutine received: 11
##>>> exc_coro.throw(DemoException)
##*** DemoException handled. Continuing...
##>>> getgeneratorstate(exc_coro)
##'GEN_SUSPENDED'

## 这个错误被抓住了，不会影响运行



##>>> exc_coro.throw(ZeroDivisionError)
##Traceback (most recent call last):
##  File "<pyshell#21>", line 1, in <module>
##    exc_coro.throw(ZeroDivisionError)
##  File "E:\Python\流畅的Python\Chapter 16\16-8.9学习在协程中处理异常的测试代码.py", line 8, in demo_exc_handling
##    x = yield
##ZeroDivisionError
##>>> getgeneratorstate(exc_coro)
##'GEN_CLOSED'

## 这个错误没被抓住，生成器变成closed
