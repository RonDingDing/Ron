import asyncio


async def work(t, name):  # 协程函数
    print('[work{}]  start'.format(name))
    await asyncio.sleep(t)
    print('[work{}]  stop'.format(name))


def hello(name):  # 普通函数
    print('[hello]  Hello, {}'.format(name))


def main():
    loop = asyncio.get_event_loop()
    start = loop.time()  # 事件循环内部时刻
    asyncio.ensure_future(work(1, 'A'))  # 任务 1
    # loop.call_later(1.2, hello, 'Tom')
    # 上面注释这行等同于下面这行
    loop.call_at(start + 1.2, hello, 'Tom')  # 任务 2
    loop.call_soon(hello, 'Kitty')  # 任务 3
    task4 = loop.create_task(work(2, 'B'))  # 任务 4
    # loop.call_later(1, hello, 'Jerry')
    # 上面注释这行等同于下面这行
    loop.call_at(start + 1, hello, 'Jerry')  # 任务 5

    loop.run_until_complete(task4)


if __name__ == '__main__':
    main()
    
# [workA]  start
# [hello]  Hello, Kitty
# [workB]  start
# [hello]  Hello, Jerry
# [workA]  stop
# [hello]  Hello, Tom
# [workB]  stop
