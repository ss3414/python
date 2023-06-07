# ****************************************************************分割线****************************************************************
# todo 多个子线程

# import threading
# import time
#
# def test(i):
#     print("thread %s is running" % threading.current_thread().name)
#     j = 0
#     while j < i:
#         print("thread %s >>> %s" % (threading.current_thread().name, j))
#         time.sleep(1)
#         j += 1
#     print("thread %s ended" % threading.current_thread().name)
#
# print("thread %s is running" % threading.current_thread().name)
#
# threads = []
# for i in range(3):
#     t = threading.Thread(target=test, name="LoopThread", args=(5,))
#     t.start()
#     threads.append(t)
# # Thread.join()必须统一运行，否则子线程无法同时运行
# for i in threads:
#     i.join()
#
# print("thread %s ended" % threading.current_thread().name)

# ****************************************************************分割线****************************************************************
# todo 继承Thread类实现线程

# import time
# import threading
#
# class ThreadClass(threading.Thread):
#     def __init__(self, i):
#         super().__init__()
#         self.i = i
#
#     def run(self):
#         while self.i > 0:
#             print(self.i)
#             self.i -= 1
#             time.sleep(1)
#
# c = ThreadClass(3)
# c.start()  # 倒计时结束后程序正常结束
