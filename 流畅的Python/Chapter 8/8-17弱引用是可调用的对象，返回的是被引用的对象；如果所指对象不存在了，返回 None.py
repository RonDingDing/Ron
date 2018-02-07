import weakref
a_set = {0,1}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2,3,4}
print(wref())
print(wref() is None)
print(wref() is None)


# >>> import weakref
# >>> a_set = {0,1}
# >>> wref = weakref.ref(a_set)
# >>> wref
# <weakref at 0x02C27960; to 'set' at 0x02C0D300>
# >>> wref()
# {0, 1}
# >>> a_set = {2,3,4}
# >>> wref()
# {0, 1}
# >>> wref() is None
# False
# >>> wref() is None
# True