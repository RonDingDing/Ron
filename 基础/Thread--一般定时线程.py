import threading, time,sys

def a():
    while True:
        time.sleep(3)
        print(1)


def b():
    while True:
        time.sleep(1)
        print(2)
    
t = threading.Thread(target=a)
t2 = threading.Thread(target=b)
t.start()    
t2.start()


