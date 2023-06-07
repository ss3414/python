# ****************************************************************分割线****************************************************************
# todo 获取目录中的文件列表

# import os
#
# # 当前目录下的所有文件和目录
# # ①[]列表推导（取出所有文件/目录）
# # ②os.path.join()加上文件路径
# # ③根据前后缀过滤（可升级为正则）
# dir = "C:/Users/Administrator/Desktop"
# files = [
#     i for i in os.listdir(dir)
#     if os.path.isfile(os.path.join(dir, i)) and i.endswith(".lnk")
# ]
# print(files)
#
# dirs = [
#     i for i in os.listdir(dir)
#     if os.path.isdir(os.path.join(dir, i))
# ]
# print(dirs)

# ************************************************************半分割线******************************
# todo 获取文件/目录尺寸

# import os
#
# dir = "C:/Users/Administrator/Desktop"
# print(str(int(os.path.getsize(dir) / 1024)) + "KB")

# ************************************************************半分割线******************************
# todo 文件名匹配

# ①fnmatch/glob专门用来文件名匹配
# ②glob相当于os.listdir()+fnmatch

# import glob
#
# files = glob.glob("C:/Users/Administrator/Desktop/*.json")
# print(files)

# ************************************************************半分割线******************************
# todo 文件操作

# import os

# os.rename("C:/Users/Administrator/Desktop/test.txt", "C:/Users/Administrator/Desktop/test1.txt")  # 重命名
# os.remove("C:/Users/Administrator/Desktop/test.txt")  # 删除文件

# path = "/home/fantasy/Desktop/目录"
# print(os.path.exists(path))  # 文件/目录是否存在
# os.mkdir(path)  # 创建目录
# os.rmdir(path)  # 删除目录
# os.removedirs(path)  # 删除目录

# ****************************************************************分割线****************************************************************
# todo 路径

# import os
#
# print(os.path.abspath(__file__))  # 定位到文件
# print(os.path.dirname(__file__))  # 定位到文件所在目录

# ****************************************************************分割线****************************************************************
# todo 运行外部命令

# import os
#
# print(os.popen("ping www.bing.com").read())
