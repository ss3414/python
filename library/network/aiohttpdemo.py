# ****************************************************************分割线****************************************************************
# todo get请求

# import aiohttp
# import asyncio
# import time
# from customutil.common import constant
#
# async def test(url):
#     begin = time.time()
#     session = aiohttp.ClientSession()
#     async with session.get(url, headers=constant.HEADERS) as response:
#         await response.text()  # 等待直到返回response.text()
#         await session.close()
#     end = time.time()
#     print(f"耗时:{round(end - begin)}秒")
#
# begin = time.time()
#
# urls = [
#     "https://github.com",
#     "https://github.com"
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([test(i) for i in urls]))
#
# end = time.time()
# print(f"耗时:{round(end - begin)}秒")

# ****************************************************************分割线****************************************************************
# todo 下载二进制数据

# import asyncio
#
# import aiohttp
#
# async def test(url):
#     session = aiohttp.ClientSession()
#     async with session.get(url, timeout=5) as response:
#         with open("favicon.ico", "wb") as f:
#             f.write(await response.read())
#         await session.close()
#
# urls = [
#     "https://github.com/favicon.ico",
# ]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait([test(i) for i in urls]))

# ****************************************************************分割线****************************************************************
# todo 作为服务器

# import asyncio
#
# from aiohttp import web
#
# # 服务端
# async def server(request):
#     body = "<p>server</p>"
#     response = web.Response(body=body.encode("UTF-8"))
#     response.content_type = "text/html;charset=utf-8"
#     return response
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_get("/", server)  # 路由
#     return await loop.create_server(app.make_handler(), "127.0.0.1", 80)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()
