# ****************************************************************分割线****************************************************************
# todo 协程

# # ①协程和生成器类似，都包含yield关键字，协程中yield关键字位于=右边
# # ②激活协程时在yield处暂停，等待调用方发送数据
# def test(x):
#     print("start:" + x)
#     while True:
#         y = yield x  # 调用next（输出yield右边的值后暂停），调用send（赋值给y）
#
# coroutine = test("str123")
# # print(next(coroutine))  # next，返回迭代器的下一个元素，yield x相当于return x
# try:
#     print("send:" + coroutine.send(None))
# except StopIteration as e:
#     print(e.value)

# ************************************************************半分割线******************************
# todo yield from

# def test():
#     for i in range(3):
#         yield i
#
# def test2():
#     yield from range(3)  # yield from自动捕获StopIteration异常
#
# print(list(test()))
# print(list(test2()))

# ****************************************************************分割线****************************************************************
# todo async/await

async def test():
    return 1

# ①Python 3.7中，@asyncio.coroutine->async，yield from->await
# ②概念：事件循环/事件驱动，Future（尚未完成的计算）
async def test2():
    result = await test()  # await只能出现在async修饰的函数中，且await后面的对象需要Awaitable（可等待的）
    return result

try:
    test2().send(None)
except StopIteration as e:
    print(e.value)
