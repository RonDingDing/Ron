registry = []


def register(func):
    print("Running register(%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("Running f1()")


print("Running main()")
print("Registry ->", registry)
f1()




