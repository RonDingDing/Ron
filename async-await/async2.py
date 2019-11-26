import time, asyncio


def four():
    start = time.time()

    async def corowork(name, t):
        print('[corowork] Start coroutine', name)
        await asyncio.sleep(t)  # 1 await 关键字等同于 Python 3.4 中的 yield from 语句，后面接协程对象。asyncio.sleep 方法的返回值为协程对象，这一步为阻塞运行。asyncio.sleep 与 time.sleep 是不同的，前者阻塞当前协程，即 corowork 函数的运行，而 time.sleep 会阻塞整个线程，所以这里必须用前者，阻塞当前协程，CPU 可以在线程内的其它协程中执行
        print('[corowork] Stop coroutine', name)
        return 'Coroutine {} OK'.format(name)  # 2 协程函数的 return 值可以在协程运行结束后保存到对应的 task 对象的 result 方法中

    loop = asyncio.get_event_loop()
    coroutine1 = corowork('ONE', 3)  # 3 创建两个协程对象，在协程内部分别阻塞 3 秒和 1 秒
    coroutine2 = corowork('TWO', 1)  # 3
    task1 = loop.create_task(coroutine1)  # 4 创建两个任务对象
    task2 = loop.create_task(coroutine2)  # 4
    gather = asyncio.gather(task1, task2)  # 5 将任务对象作为参数，asyncio.gather 方法创建任务收集器。注意，asyncio.gather 方法中参数的顺序决定了协程的启动顺序
    loop.run_until_complete(gather)  # 6 将任务收集器作为参数传入事件循环的 run_until_complete 方法，阻塞运行，直到全部任务完成
    print('[task1] ', task1.result())  # 7 任务结束后，事件循环停止，打印任务的 result 方法返回值，即协程函数的 return 值
    print('[task2] ', task2.result())  # 7
    end = time.time()
    print('运行耗时：{:.4f}'.format(end - start))

    result = loop.run_until_complete(gather)
    print(result)


four()
# [corowork] Start coroutine ONE
# [corowork] Start coroutine TWO
# [corowork] Stop coroutine TWO
# [corowork] Stop coroutine ONE
# [task1]  Coroutine ONE OK
# [task2]  Coroutine TWO OK
# ['Coroutine ONE OK', 'Coroutine TWO OK']  # 变量 result 的值
# 运行耗时：3.0070

#
# 简单叙述一下程序协程部分的运行过程：
# -> 首先运行 task1
# -> 打印 [corowork] Start coroutine ONE
# -> 遇到 asyncio.sleep 阻塞
# -> 释放 CPU 转到 task2 中执行
# -> 打印 [corowork] Start coroutine TWO
# -> 再次遇到 asyncio.sleep 阻塞
# -> 这次没有其它协程可以运行了，只能等阻塞结束
# -> task2 的阻塞时间较短，阻塞 1 秒后先结束，打印 [corowork] Stop coroutine TWO
# -> 又过了 2 秒，阻塞 3 秒的 task1 也结束了阻塞，打印 [corowork] Stop coroutine ONE
# -> 至此两个任务全部完成，事件循环停止
# -> 打印两个任务的 result
# -> 打印程序运行时间
# -> 程序全部结束


# 1、多数情况下无需调用 task 的 add_done_callback 方法，可以直接把回调函数中的代码写入 await 语句后面，协程是可以暂停和恢复的
# 2、多数情况下同样无需调用 task 的 result 方法获取协程函数的 return 值，因为事件循环的 run_until_complete 方法的返回值就是协程函数的 return 值。修改上文 # 6 、7 的代码如下：
# 3、事件循环有一个 stop 方法用来停止循环和一个 close 方法用来关闭循环。以上示例中都没有调用 loop.close 方法，似乎并没有什么问题。所以到底要不要调用 loop.close 呢？简单来说，loop 只要不关闭，就还可以再次运行 run_until_complete 方法，关闭后则不可运行。有人会建议调用 loop.close，彻底清理 loop 对象防止误用，其实多数情况下根本没有这个必要。
# 4、asyncio 模块提供了 asyncio.gather 和 asyncio.wait 两个任务收集方法，它们的作用相同，都是将协程任务按顺序排定，再将返回值作为参数加入到事件循环中。前者在上文已经用到，后者与前者的区别是它可以获取任务的执行状态（PENING & FINISHED），当有一些特别的需求例如在某些情况下取消任务，可以使用 asyncio.wait 方法。