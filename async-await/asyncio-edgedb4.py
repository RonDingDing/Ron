import asyncio
from typing import Awaitable


# fut = asyncio.Future()
# print(fut.done())
# print(fut.cancelled())
# # print(fut.result())
#
# fut.set_result("result is set!")
# print(fut.done())
# print(fut.cancelled())
# print(fut.result())
#
#
async def get_result(awaitable: Awaitable) -> str:
	try:
		result = await awaitable
	except Exception as e:
		print("oops!", e)
		return "no result :("
	else:
		return result


#
# f = asyncio.Future()
loop = asyncio.get_event_loop()


# loop.call_later(10, f.set_result, "this is my result")
# print(loop.run_until_complete(get_result(f)))

# f = asyncio.Future()
# loop.call_later(10, f.set_result, "another result")
# print(loop.run_until_complete(get_result(get_result(get_result(f)))))

# f = asyncio.Future()
# loop.call_later(10, f.set_exception, ValueError("problem encountered"))
# print(loop.run_until_complete(get_result(f)))

# f = asyncio.Future()
# loop.call_later(10, f.cancel)
# print(loop.run_until_complete(get_result(f)))

# f = asyncio.Future()
# loop.call_later(10, f.set_result, "final result")
# print(loop.run_until_complete(asyncio.gather(get_result(f), get_result(f), get_result(f), )))


# def callback(fut: asyncio.Future) -> None:
# 	print("called by", fut)
#
#
# f = asyncio.Future()
# f.add_done_callback(callback)
# f.add_done_callback(lambda f: loop.stop())
# # 直接 set_result不会触发callback
# f.set_result("yup")
# loop.run_forever()
def indent(num: int):
	return "    " * (num + 1)


async def example(count: int) -> str:
	print(indent(count), "Before the first await")
	await asyncio.sleep(0)
	print(indent(count), "After the first await")
	if count == 0:
		print(indent(count), "Returning result")
		return "result"
	for i in range(count):
		print(indent(count), "Before await inside loop iteration", i)
		await asyncio.sleep(i)
		print(indent(count), "After await inside loop iteration", i)
	print(indent(count), f"Before await on example({count - 1})")
	return await example(count - 1)


class TraceStep(asyncio.tasks._PyTask):
	def _Task__step(self, exc=None):
		print(f"<step name={self.get_name()} done={self.done()}>")
		result = super()._Task__step(exc=exc)
		print(f"</step name={self.get_name()} done={self.done()}>")


loop.set_task_factory(lambda loop, coro: TraceStep(coro, loop=loop))

loop.run_until_complete(example(1))
