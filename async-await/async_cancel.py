import asyncio

async def work(id, t):
    print('Working...')
    await asyncio.sleep(t)
    print('Work {} done'.format(id))

def main():
    loop = asyncio.get_event_loop()
    coroutines = [work(i, i) for i in range(1, 4)]            # 1 创建一个列表，列表中有 3 个协程对象，协程内部分别阻塞 1 - 3 秒
    try:
        loop.run_until_complete(asyncio.gather(*coroutines))  # 2 程序运行过程中，快捷键 Ctrl + C 会触发 KeyboardInterrupt 异常。捕获这个异常，在程序终止前完成 # 3 和 # 4 代码的执行
    except KeyboardInterrupt:
        loop.stop()    # 3 事件循环的 stop 方法取消所有未完成的任务，停止事件循环
    finally:
        loop.close()   # 4 关闭事件循环

if __name__ == '__main__':
    main()


# $ python3 async_cancel.py
# Working...
# Working...
# Working...
# Work 1 done
# ^C%

# 程序运行过程：
# -> 首先，id 为 1 的协程先启动运行
# -> 打印 Working...
# -> 遇到 IO 阻塞，释放 CPU ，CPU 去到 id 为 2 的协程中运行
# -> 同样首先打印 Working...
# -> 遇到 IO 阻塞，同样释放 CPU ，第三个协程开始运行，打印 Working...
# -> 以上步骤瞬间完成，这时候的 loop 中全部协程处于阻塞状态
# -> 一秒钟后，id 为 1 的协程结束阻塞
# -> 打印 Work 1 done
# -> 然后手动按下快捷键 Ctrl + C ，触发 KeyboardInterrupt 异常
# -> try except 语句捕获异常，执行 # 3 和 # 4
# -> 程序运行完毕