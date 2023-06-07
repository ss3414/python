# ****************************************************************分割线****************************************************************
# todo StringIO

# 与open()函数的关系

from io import StringIO

# 读
print(StringIO("test").read())  # 使用字符串初始化StringIO

# 写
print(StringIO().write("test2"))  # 打印字符串长度
