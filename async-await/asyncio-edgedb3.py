import datetime
import asyncio
import inspect
#
#
# def print_now():
# 	print(datetime.datetime.now())
#
#
# async def keep_printing(name: str = "") -> None:
# 	while True:
# 		print(name, end=" ")
# 		print_now()
# 		await asyncio.sleep(0.5)
#
#
# # 一直运行
# asyncio.run(keep_printing())
#
# # 10秒后停止，但是会弹出TimeOut错误
# asyncio.run(asyncio.wait_for(keep_printing(), 10))
#
#
# # 抓取错误
# async def async_main() -> None:
# 	try:
# 		await asyncio.wait_for(keep_printing("Hey"), 10)
# 	except asyncio.TimeoutError:
# 		print("oops, time's up")
#
#
# asyncio.run(async_main())
#
#
# async def async_main() -> None:
# 	try:
# 		kp = keep_printing("Hey")
# 		waiter = asyncio.wait_for(kp, 10)
# 		await waiter
# 	except asyncio.TimeoutError:
# 		print("oops, time's up")
#
#
# asyncio.run(async_main())
#
#
# # 忘记 await
# async def async_main() -> None:
# 	kp = keep_printing("Hey")
# 	waiter = asyncio.wait_for(kp, 10)
# 	try:
# 		waiter
# 	except asyncio.TimeoutError:
# 		print("oops, time's up")
#
#
# asyncio.run(async_main())
#
#
# # type
# async def print3times() -> None:
# 	for _ in range(3):
# 		print_now()
# 		await asyncio.sleep(0.1)
#
#
# coro1 = print3times()
# coro2 = print3times()
# print(type(print3times))
# print(type(coro1))
# print(type(coro2))
# asyncio.run(print3times)
# #
# # 只能await一次
# asyncio.run(coro1)
# asyncio.run(coro2)
# asyncio.run(coro1)
#
#
# # 区分 async function 与 coroutine
# async def async_function() -> None:
# 	await keep_printing()
#
#
# coroutine = async_function()
#
# print(inspect.isawaitable(async_function))
# print(inspect.isawaitable(coroutine))
#
#
# # 注意调用顺序，只有第一个一直运行
#
#
# async def async_main() -> None:
# 	await keep_printing("First")
# 	await keep_printing("Second")
# 	await keep_printing("Third")
#
#
# asyncio.run(async_main())
#
#
# # 这才是并发正确写法
#
#
# async def async_main() -> None:
# 	await asyncio.gather(
# 		keep_printing("First"),
# 		keep_printing("Second"),
# 		keep_printing("Third")
# 	)
#
#
# asyncio.run(async_main())
#
#
# # 优雅处理TimeoutError，但没有处理keep_printing中的CancelledError，
#
# async def async_main() -> None:
# 	try:
# 		await asyncio.wait_for(asyncio.gather(
# 			keep_printing("First"),
# 			keep_printing("Second"),
# 			keep_printing("Third")
# 		), 5)
# 	except asyncio.TimeoutError:
# 		print("oops, time's up")
#
#
# asyncio.run(async_main())
#
#
# # CancelledError处理
#
# async def keep_printing(name: str = "") -> None:
# 	while True:
# 		print(name, end=" ")
# 		print_now()
# 		try:
# 			await asyncio.sleep(0.5)
# 		except asyncio.CancelledError:
# 			print(name, "was cancelled")
# 			break
#
#
# asyncio.run(async_main())

# 爬虫小例子
import httpx

# 多重await 连用约等于同步
# async def crawl0(prefix: str, url: str = "") -> None:
# 	url = url or prefix
# 	print(f"Crawling {url}")
# 	client = httpx.AsyncClient()
# 	try:
# 		res = await client.get(url)
# 	finally:
# 		await client.aclose()
# 	for line in res.text.splitlines():
# 		if line.startswith(prefix):
# 			await crawl0(prefix, line)
#
# asyncio.run(crawl0("https://langa.pl/crawl/"))
from typing import Callable, Coroutine
import time

addr = "https://langa.pl/crawl"
todo = set()


# async def progress(url: str, algo: Callable[..., Coroutine]) -> None:
# 	asyncio.create_task(algo(url), name=url)
# 	todo.add(url)
# 	start = time.time()
# 	while len(todo):
# 		print(f"{len(todo)}:" + ", ".join(sorted(todo)))
# 		await asyncio.sleep(0.5)
# 	end = time.time()
# 	print(f"Took {int(end - start)} seconds")


#  速度约等于同步
# async def crawl1(prefix: str, url: str = "") -> None:
# 	url = url or prefix
# 	client = httpx.AsyncClient()
# 	try:
# 		res = await client.get(url)
# 	finally:
# 		await client.aclose()
# 	for line in res.text.splitlines():
# 		if line.startswith(prefix):
# 			todo.add(line)
# 			await crawl1(prefix, line)
# 	todo.discard(url)
#
#
# asyncio.run(progress(addr, crawl1))

# 真正的并发
# async def crawl2(prefix: str, url: str = "") -> None:
# 	url = url or prefix
# 	client = httpx.AsyncClient()
# 	try:
# 		res = await client.get(url)
# 	finally:
# 		await client.aclose()
# 	for line in res.text.splitlines():
# 		if line.startswith(prefix):
# 			todo.add(line)
# 			asyncio.create_task(crawl2(prefix, line), name=line)
# 	todo.discard(url)
#
# asyncio.run(progress(addr, crawl2))

# todo里面加task
async def crawl2(prefix: str, url: str = "") -> None:
	url = url or prefix
	client = httpx.AsyncClient()
	try:
		res = await client.get(url)
	finally:
		await client.aclose()
	for line in res.text.splitlines():
		if line.startswith(prefix):
			task = asyncio.create_task(crawl2(prefix, line), name=line)
			todo.add(task)


#
#
# asyncio.run(progress(addr, crawl2))


async def progress(url: str, algo: Callable[..., Coroutine]) -> None:
	asyncio.create_task(algo(url), name=url)
	todo.add(url)
	start = time.time()
	while len(todo):
		done, _pending = await asyncio.wait(todo, timeout=0.5)
		todo.difference_update(done)
		urls = (t.get_name() for t in todo)
		print(f"{len(todo)}: " + ", ".join(sorted(urls)))
	end = time.time()
	print(f"Took {int(end - start)} seconds")


# asyncio.run(progress(addr, crawl2))
async def async_main() -> None:
	try:
		await progress(addr, crawl2)
	except asyncio.CancelledError:
		for task in todo:
			task.cancel()
		done, pending = await asyncio.wait(todo, timeout=1.0)
		todo.difference_update(done)
		todo.difference_update(pending)
		if todo:
			print("warning: new tasks added while we were cancelling.")


loop = asyncio.get_event_loop()
task = loop.create_task(async_main())
loop.call_later(10, task.cancel)
loop.run_until_complete(task)
