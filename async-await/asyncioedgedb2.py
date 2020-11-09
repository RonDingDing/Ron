import asyncio
loop = asyncio.get_event_loop()
# loop.run_forever()
print('*' * 50)

loop.run_until_complete(asyncio.sleep(5))
print('*' * 50)

import datetime
def print_now():
	print(datetime.datetime.now())

loop.call_soon(print_now)
loop.call_soon(print_now)
loop.run_until_complete(asyncio.sleep(5))
print('*' * 50)

def trampoline(name:str = "") -> None:
	print(name, end= " ")
	print_now()
	loop.call_later(0.5, trampoline, name)

loop.call_soon(trampoline)
loop.call_later(8, loop.stop)
loop.run_forever()
print('*' * 50)

loop.call_soon(trampoline, "First")
loop.call_soon(trampoline, "Second")
loop.call_soon(trampoline, "Third")
loop.call_later(8, loop.stop)
loop.run_forever()
print('*' * 50)


def hog():
	num = 0
	for i in range(10000):
		for j in range(10000):
			num += j
	return num
loop.call_later(15, hog)
loop.call_later(20, loop.stop)
loop.run_forever()
print('*' * 50)

loop.set_debug(True)
loop.call_later(15, hog)
loop.call_later(20, loop.stop)
loop.run_forever()
print('*' * 50)
# asyncio 每次迭代EventLoop，EventLoop.run_once 会做的事情（）
# 1. 调用已经准备好的回调函数
# 2. 使用当前的selector或proactor轮询I/O  event_list = self._selector.select(timeout) !!!!
# 3. 为EventLoop的下一次迭代注册回调函数
# 4. 寻找已准备好的call_later的回调函数并执行

