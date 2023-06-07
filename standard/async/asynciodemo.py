# ****************************************************************分割线****************************************************************
# todo 异步生成器

# import asyncio
# import time
#
# @asyncio.coroutine
# def test(sleep_time):
#     begin = time.time()
#     yield from asyncio.sleep(sleep_time)
#     end = time.time()
#     print("耗时:" + str(round(end - begin)) + "秒")
#
# begin = time.time()
#
# loop = asyncio.get_event_loop()
# times = [1, 2, 3]
# loop.run_until_complete(asyncio.wait([test(i) for i in times]))
# loop.close()
#
# end = time.time()
# print("共耗时:" + str(round(end - begin)) + "秒")

# ****************************************************************分割线****************************************************************
# todo 异步函数

# import asyncio
# import time
#
# async def test(sleep_time):
#     begin = time.time()
#     await asyncio.sleep(sleep_time)  # 此处不能是time.sleep()
#     end = time.time()
#     print("耗时:" + str(round(end - begin)) + "秒")
#     return str(round(end - begin))
#
# begin = time.time()
#
# loop = asyncio.get_event_loop()  # 事件驱动
# times = [1, 2, 3]
# loop.run_until_complete(asyncio.wait([test(i) for i in times]))
# loop.close()
#
# end = time.time()
# print("共耗时:" + str(round(end - begin)) + "秒")

# ****************************************************************分割线****************************************************************
# todo 异步类

# import asyncio
# import time
#
# class Parent:
#     async def test(self, sleep_time):
#         begin = time.time()
#         await asyncio.sleep(sleep_time)
#         end = time.time()
#         print("耗时:" + str(round(end - begin)) + "秒")
#         return str(round(end - begin))
#
# begin = time.time()
#
# loop = asyncio.get_event_loop()
# times = [1, 2, 3]
# loop.run_until_complete(asyncio.wait([Parent().test(i) for i in times]))
# loop.close()
#
# end = time.time()
# print("共耗时:" + str(round(end - begin)) + "秒")

# ****************************************************************分割线****************************************************************
# todo 异步递归

# import asyncio
# import time
#
# async def test(i):
#     print("test开始")
#     begin = time.time()
#     await asyncio.sleep(i)
#     end = time.time()
#     print("test耗时:" + str(round(end - begin)) + "秒")
#     if i > 1:
#         await test(i - 1)
#     return str(round(end - begin))
#
# begin = time.time()
# loop = asyncio.get_event_loop()
# todos = [asyncio.ensure_future(test(3))]
# loop.run_until_complete(asyncio.wait(todos))
# loop.close()
# end = time.time()
# print("共耗时:" + str(round(end - begin)) + "秒")

# ****************************************************************分割线****************************************************************
# todo 异步回调

# import asyncio
# import time
#
# async def test1(i):
#     print("test1开始")
#     begin = time.time()
#     await asyncio.sleep(i)
#     end = time.time()
#     print("test1耗时:" + str(round(end - begin)) + "秒")
#     return str(round(end - begin))
#
# async def test2(i):
#     print("test2开始")
#     begin = time.time()
#     await asyncio.sleep(i)
#     end = time.time()
#     print("test2耗时:" + str(round(end - begin)) + "秒")
#     return str(round(end - begin))
#
# # 获取协程返回值
# def result(future):
#     print(future.result())
#
# begin = time.time()
# loop = asyncio.get_event_loop()
# todos = [asyncio.ensure_future(test1(2)), asyncio.ensure_future(test2(1))]  # test1()先加入todos先运行
# todos[1].add_done_callback(result)  # 给test2()添加回调函数
# loop.run_until_complete(asyncio.wait(todos))
# loop.close()
# end = time.time()
# print("共耗时:" + str(round(end - begin)) + "秒")
