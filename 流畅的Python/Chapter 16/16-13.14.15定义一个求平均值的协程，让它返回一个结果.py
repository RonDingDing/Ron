from collections import namedtuple

Result = namedtuple("Result", "count average")

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total /count
    return Result(count, average)


##>>> coro_avg = averager()
##>>> next(coro_avg)
##>>> coro_avg.send(30)
##>>> coro_avg.send(10)
##>>> coro_avg.send(6.5)
##>>> coro_avg.send(None)
##Traceback (most recent call last):
##  File "<pyshell#49>", line 1, in <module>
##    coro_avg.send(None)
##StopIteration: Result(count=3, average=15.5)



##>>> coro_avg = averager()
##>>> next(coro_avg)
##>>> coro_avg.send(10)
##>>> coro_avg.send(30)
##>>> coro_avg.send(6.5)
##>>> try:
##...     coro_avg.send(None) 因为规定了退出条件
##... except StopIteration as exc:
##...     result = exc.value
##...
##>>> result
##Result(count=3, average=15.5)
