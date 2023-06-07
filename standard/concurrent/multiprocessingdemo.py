# ****************************************************************分割线****************************************************************
# todo multiprocessing（单个子进程）

# import os
# import time
# from multiprocessing import Process
#
# def test(i):
#     print("Child process %s is running" % os.getpid())
#     j = 0
#     while j < i:
#         print("Child process %s >>> %s" % (os.getpid(), j))
#         time.sleep(1)
#         j += 1
#     print("Child process %s ended" % os.getpid())
#
# # ①if __name__ == "__main__"（只有直接运行当前文件才会运行main方法中内容）
# # ②multiprocessing多进程，if __name__是必需的
# if __name__ == "__main__":
#     print("Parent process %s is running" % os.getpid())
#     # 程序运行到这里时进入子进程，如果没有在子进程内打断点程序是不会暂停的
#     p = Process(target=test, args=(3,))
#     p.start()
#     p.join()
#     print("Parent process ended")

# ****************************************************************分割线****************************************************************
# todo Pool（多个子进程）

# import multiprocessing
# import os
# import time
# from multiprocessing import Pool
#
# def test(i):
#     print("Child process %s is running" % os.getpid())
#     j = 0
#     while j < i:
#         print("Child process %s >>> %s" % (os.getpid(), j))
#         time.sleep(1)
#         j += 1
#     print("Child process %s ended" % os.getpid())
#
# if __name__ == "__main__":
#     print("Parent process %s is running" % os.getpid())
#     core = multiprocessing.cpu_count()  # 同时最多进程数（取决于CPU核心数？）
#     p = Pool(core)
#     for i in range(core + 1):  # 运行的子进程数>同时最多进程数
#         p.apply_async(test, args=(3,))
#     p.close()
#     p.join()
#     print("Parent process ended")

# ************************************************************半分割线******************************
# todo 多进程写入TXT（回调写入）

# import multiprocessing
# from multiprocessing import Pool
#
# def test(i):
#     return i
#
# def log(i):
#     f = open("C:/Users/Administrator/Desktop/test.txt", "a", encoding="UTF-8")
#     f.write(str(i))
#     f.close()
#
# if __name__ == "__main__":
#     core = multiprocessing.cpu_count()
#     p = Pool(core)
#     for i in range(core):
#         p.apply_async(test, args=(i,), callback=log)  # 回调函数只能接受一个参数
#     p.close()
#     p.join()
