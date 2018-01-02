import threading, time,sys

def t1():
    t = threading.Timer(1, a)
    t.start()

def t2():
    t = threading.Timer(3, b)
    t.start()


def a():
    print(1)
    t1()

def b():
    print(2)
    t2()


a()
b()
 
