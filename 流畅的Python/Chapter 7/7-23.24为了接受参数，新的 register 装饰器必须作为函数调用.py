# registry = set()
#
#
# def register(active=True):
#     def decorate(func):
#         print("Running register(active=%s)->decorate(%s)" % (active, func))
#         if active:
#             registry.add(func)
#         else:
#             registry.discard(func)
#         return func
#
#     return decorate
#
#
# @register(active=False)
# def f1():
#     print("Running f1()")
#
#
# @register()
# def f2():
#     print("Running f2()")
#
#
# def f3():
#     print("Running f3()")
#

if __name__ == "__main__":
    # import registration_param
    # print(registration_param.registry)

    from registration_param import *
    print(registry)
    register()(f3)
    print(registry)
    register(active=False)(f2)
    print(registry)