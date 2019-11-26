import time, asyncio


def two():
    start = time.time()

    @asyncio.coroutine
    def do_some_work():
        print('Start coroutine')
        time.sleep(0.1)
        print('This is a coroutine')

    loop = asyncio.get_event_loop()
    coroutine = do_some_work()
    task = loop.create_task(coroutine)  # 1
    print('task 是不是 asyncio.Task 的实例？', isinstance(task, asyncio.Task))  # 2
    print('Task state:', task._state)  # 3
    loop.run_until_complete(task)  # 4
    print('Task state:', task._state)
    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


two()
# task 是不是 asyncio.Task 的实例？ True
# Task state: PENDING
# Start coroutine
# This is a coroutine
# Task state: FINISHED
# 运行耗时：0.1052
