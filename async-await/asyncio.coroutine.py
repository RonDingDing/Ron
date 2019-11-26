# coding=utf-8
import time

import asyncio

def one():
    start = time.time()
    @asyncio.coroutine   # 1 使用协程装饰器创建协程函数
    def do_some_work():  # 2 协程函数
        print('Start coroutine')
        time.sleep(0.1)  # 3 模拟 IO 操作
        print('This is a coroutine')
    loop = asyncio.get_event_loop()     # 4 创建事件循环。每个线程中只能有一个事件循环，get_event_loop 方法会获取当前已经存在的事件循环，如果当前线程中没有，新建一个
    coroutine = do_some_work()          # 5 调用协程函数获取协程对象
    loop.run_until_complete(coroutine)  # 6 将协程对象注入到事件循环，协程的运行由事件循环控制。事件循环的 run_until_complete 方法会阻塞运行，直到任务全部完成。协程对象作为 run_until_complete 方法的参数，loop 会自动将协程对象包装成任务来运行。后面我们会讲到多个任务注入事件循环的情况
    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))  # 7 打印程序运行耗时

one()
# Start coroutine
# This is a coroutine
# 运行耗时：0.1062