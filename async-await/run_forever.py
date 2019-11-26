import asyncio

async def work(loop, t):
    print('start')
    await asyncio.sleep(t)  # 模拟 IO 操作
    print('after {}s stop'.format(t))
    loop.stop()             # 停止事件循环，stop 后仍可重新运行

loop = asyncio.get_event_loop()             # 创建事件循环
task = asyncio.ensure_future(work(loop, 1)) # 创建任务，该任务会自动加入事件循环
loop.run_forever()  # 无限运行事件循环，直至 loop.stop 停止
loop.close()        # 关闭事件循环，只有 loop 处于停止状态才会执行


# start
# after 1s stop