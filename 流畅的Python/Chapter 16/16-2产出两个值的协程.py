def simple_coro2(a):
    print('-> Started: a = %s' % a)
    b = yield a
    print('-> Received: b = %s' % b)
    c = yield a + b
    print('-> Received: c = %s' % c)


##>>> my_coro2 = simple_coro2(14)
##>>> from inspect import getgeneratorstate
##>>> getgeneratorstate(my_coro2)
##'GEN_CREATED'
##>>> next(my_coro2)
##-> Started: a = 14
##14
##>>> getgeneratorstate(my_coro2)
##'GEN_SUSPENDED'
##>>> my_coro2.send(28)
##-> Received: b = 28
##42
##>>> my_coro2.send(99)
##-> Received: c = 99
##Traceback (most recent call last):
##  File "<pyshell#6>", line 1, in <module>
##    my_coro2.send(99)
##StopIteration
##>>> getgeneratorstate(my_coro2)
##'GEN_CLOSED'
