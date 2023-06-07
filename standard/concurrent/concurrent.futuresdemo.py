# ****************************************************************分割线****************************************************************
# todo Executor.submit()

# import threading
# from concurrent import futures
#
# def test(input):
#     print(threading.current_thread().name)
#     return input["id"]
#
# with futures.ThreadPoolExecutor(max_workers=1) as executor:  # with块结束时自动关闭资源
#     list = [1, 2]
#     for i in list:
#         future = executor.submit(test, {"id": 1, "name": "name"})
#         print(future.result())

# ****************************************************************分割线****************************************************************
# todo Executor.map()

# import threading
# import time
# from concurrent import futures
#
# def test(i):
#     time.sleep(1)
#     print(threading.current_thread().name)
#     return i
#
# # 通过max_workers调整并发数（耗时=range()/max_workers）
# with futures.ThreadPoolExecutor(max_workers=100) as executor:
#     begin = time.time()
#     list = [i for i in range(400)]
#     for i in executor.map(test, list):  # 第2个参数传入的是列表
#         pass
#     end = time.time()
#     print("耗时" + str(round(end - begin)) + "秒")

# ****************************************************************分割线****************************************************************
# todo ProcessPoolExecutor

import time
from concurrent import futures

def test(i):
    time.sleep(1)
    return i

# ①用ProcessPoolExecutor代替ThreadPoolExecutor规避GIL问题
# ②使用ThreadPoolExecutor耗时=range()/max_workers，ProcessPoolExecutor却不严格对应，且max_workers过大则报错
if __name__ == "__main__":
    with futures.ProcessPoolExecutor(max_workers=2) as executor:
        begin = time.time()
        list = [i for i in range(6)]
        for i in executor.map(test, list):
            print(i)
        end = time.time()
        print("耗时" + str(round(end - begin)) + "秒")
    pass
