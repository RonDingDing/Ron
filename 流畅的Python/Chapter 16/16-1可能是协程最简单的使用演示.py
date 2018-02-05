def simple_coroutine():
    print("-> coroutine stated")
    x = yield
    print("-> coroutine received: %s" % x)


# >>> my = simple_coroutine()
# >>> next(my)
# -> coroutine stated
# >>> my.send(42)
# -> coroutine received: 42
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     my.send(42)
# StopIteration


# 用inspect来检测申城期的状态
# >>> my = simple_coroutine()
# >>> inspect.getgeneratorstate(my)
# 'GEN_CREATED'
# >>> next(my)
# -> coroutine stated
# >>> inspect.getgeneratorstate(my)
# 'GEN_SUSPENDED'
# >>> my.send(42)
# -> coroutine received: 42
# Traceback (most recent call last):
#   File "<pyshell#44>", line 1, in <module>
#     my.send(42)
# StopIteration
# >>> inspect.getgeneratorstate(my)
# 'GEN_CLOSED'
