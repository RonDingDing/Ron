import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)

from threading import Thread
t = Thread(target=countdown, args=(10,))
# t.start()

if t.is_alive():
    print('Still running')
else:
    print('Completed')

# 后台线程
t = Thread(target=countdown, args=(10,), daemon=True)
# t.start()


class CountdownTask:
    def __init__(self ):
        self._running = True
         

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start() 
c.terminate() # Signal termination
t.join()      # Wa


import socket
class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        # sock is a socket
        sock.settimeout(5)        # Set timeout period
        while self._running:
            # Perform a blocking I/O operation w/ timeout
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
            # Continued processing
            ...
        # Terminated
        return

from threading import Thread

class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        
    def run(self):
        while self.n > 0:

            print('T-minus', self.n)
            self.n -= 1
            time.sleep(1)

c = CountdownThread(5)
c.start()


import multiprocessing
c = CountdownTask()
p = multiprocessing.Process(target=c.run, args=(5,))
p.start()