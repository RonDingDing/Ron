from typing import Mapping
import time
import threading

class Mayhem(threading.Thread):
	def __init__(self, map: Mapping[str, int]) -> None:
		super().__init__()
		self.map = map

	def run(self):
		for key, value in self.map.items():
			time.sleep(value)

d = {"k1": 1, "k2": 2, "k3": 3}
m = Mayhem(d)
m.start()
d["k4"] = 4

# 多线程运行时无法在中间插入线程

# Proactor 模式：
# 当事件到达后，系统分出线程处理数据，如线程已满则让事件继续等待。数据处理完成后，系统告诉用户处理完的数据放在哪里

# Reactor 模式：
# 当事件到达后，系统通知用户准备好读的文件描述符有哪些，准备好写的文件描述符有哪些，然后用户代码自行进行处理