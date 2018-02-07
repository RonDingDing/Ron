import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(", ".join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(", ".join(pairs))
        arg_str = ", ".join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result

    return clocked


@functools.lru_cache()
@clock
def fibonacci1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci1(n - 2) + fibonacci1(n - 1)

#尾递归
@clock
def fibonacci2(n, r1, r2):
    if n == 0:
        return r1
    else:
        return fibonacci2(n - 1, r2, r1 + r2)


@clock
def fibonacci3(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci3(n - 2) + fibonacci3(n - 1)


if __name__ == "__main__":
    #print(fibonacci3(99))
    print("\n")
    print(fibonacci2(90, 1, 1))
    print("\n")
    print(fibonacci1(90))