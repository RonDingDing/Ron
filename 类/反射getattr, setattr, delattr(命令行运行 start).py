#反射，就是根据字符串找到内存地址

import sys
class WebServer(object):
    
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        print("Server is starting...")

    def stop(self):
        print("Server is stopping...")

    def restart(self):
        self.stop()
        self.start()


def test_run(ins, name):
    print("running...", name, ins.host)


if __name__ == "__main__":
    
    server = WebServer('localhost', 333)
    server2 = WebServer('localhost', 333)
    #print(sys.argv[1])
    if hasattr(server, sys.argv[1]): #如果server存在sys.argv[1]属性 
        func = getattr(server, sys.argv[1]) #获取server.start内存地址
        func()  #server.start()

    setattr(server, 'run', test_run) #把test_run作为实例方法绑定到sever中
    server.run(server, 'alex')
    #delattr(server, 'start')
    
