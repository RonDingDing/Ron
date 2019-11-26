import time, asyncio, functools


def three():
    start = time.time()

    # @asyncio.coroutine
    async def corowork():  # 1
        print('[corowork] Start coroutine')
        time.sleep(0.1)
        print('[corowork] This is a coroutine')

    def callback(name, task):  # 2
        print('[callback] Hello {}'.format(name))
        print('[callback] coroutine state: {}'.format(task._state))

    loop = asyncio.get_event_loop()
    coroutine = corowork()
    task = loop.create_task(coroutine)
    task.add_done_callback(functools.partial(callback, 'Shiyanlou'))  # 3
    loop.run_until_complete(task)

    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))


three()
# [corowork] Start coroutine
# [corowork] This is a coroutine
# [callback] Hello Shiyanlou
# [callback] coroutine state: FINISHED
# 运行耗时：0.1051
