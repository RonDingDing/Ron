import socket

obj = socket.socket()
obj.connect(('127.0.0.1', 8002))

content = str(obj.recv(1024), encoding='utf-8')
print('client2 received: ', content)

obj.close()
