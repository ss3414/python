# ****************************************************************分割线****************************************************************
# todo 内置类型

# 数字类型int/float/complex（复数）
# 迭代器/生成器类型
# 序列类型list/tuple（元组）/range
# 文本序列（字符串）类型str
# 二进制序列类型bytes/bytearray/memoryview
# 集合类型set/frozenset
# 映射类型dict
# 上下文管理器类型
# 其他内置类型：模块/类与对象/函数/方法/代码对象/类型对象/空对象/省略符对象/未实现对象/布尔值/内部对象

# ************************************************************半分割线******************************
# 函数是Python中的"一等公民"

# import re
#
# def test():
#     print()
#
# class test2:
#     print()
#
# # ①整型/浮点型/字符串/None/list/set/dict/方法/类/对象/模块
# # ②Python中所有数据类型都是某个类的实例，1是int类的对象，int类本身又是type类的对象
# # ③Python中函数也是对象，所以函数是Python中的"一等公民"，可以作为参数/返回值
# list = [1, 1.0, "test", None, [1], {1}, {"key": "value"}, test, test2, test2(), re]
# for i in list:
#     print(str(i) + " " + str(type(i)) + " " + str(type(type(i))))

# ****************************************************************分割线****************************************************************
# todo 内置常量

# True/False/None
# NotImplemented
# Ellipsis（与省略号"..."字面值相同）
# __debug__

# 由site模块添加的常量（一般用于命令行）：quit()/exit()/copyright/credits/license

# ****************************************************************分割线****************************************************************
# todo 内置函数

# abs()：绝对值
# all()：判断迭代器是否含空元素/是否全为空
# any()：判断迭代器是否含非空元素
# ascii()：返回对象的可打印字符串
# bin()：将整数转换为"0b"开头的二进制字符串
# bool()：判断布尔值
# breakpoint()：断点
# bytearray()：返回bytes数组
# bytes()：返回bytes对象
# callable()：判断参数是否可调用
# chr()：返回Unicode码对应的字符
# classmethod()：把一个方法封装成类方法
# compile()：将source编译成代码/AST对象
# complex()：复数
# delattr()：删除属性
# dict()：新建dict类型变量
# dir()：返回属性列表
# divmod()：除法和取余
# enumerate()：返回枚举对象
# eval()：执行表达式
# exec()：动态执行Python代码
# filter()：过滤迭代器中为真的元素并生成一个新的迭代器
# float()：浮点数
# format()：格式化
# frozenset()：返回frozenset对象
# getattr()：获取对象属性的值
# globals()：
# hasattr()：判断是否包含属性
# hash()：返回哈希值
# help()：命令行帮助
# hex()：将整数转换为"0x"开头的十六进制字符串
# id()：返回对象的标识值
# input()：输入
# int()：转换为整型
# isinstance()：判断类型
# issubclass()：判断子类
# iter()：返回iterator对象
# len()：返回长度
# list()：新建list类型变量
# locals()：
# map()：
# max()：最大值
# memoryview()：返回memoryview对象
# min()：最小值
# next()：返回迭代器的下一个元素
# object()：返回一个对象
# oct()：将整数转换为"0o"开头的八进制字符串
# open()：打开文件
# ord()：返回字符对应的Unicode码
# pow()：指数
# print()：打印
# property()：返回属性
# range()：生成随机数
# repr()：返回对象的可打印字符串
# reversed()：迭代器逆序
# round()：取整
# set()：新建set类型变量
# setattr()：设置对象属性的值
# slice()：切片
# sorted()：排序
# staticmethod()：将方法转换为静态方法
# str()：转换为字符串型
# sum()：求和
# super()：
# tuple()：新建tuple类型变量
# type()：返回类型
# vars()：
# zip()：
# __import__()：

# ************************************************************半分割线******************************
# todo open（读写文本/二进制）

# 逐行读取TXT
# ①读取时会带上换行符\n
# ②最后一行没有换行符，请务必保证TXT文件最后空一行（空行不读取）
# f = open("C:/Users/Administrator/Desktop/test.txt", "r", encoding="UTF-8")
# line = f.readline()
# while line:
#     print(line[0:len(line) - 1])
#     line = f.readline()

# 写入TXT
# ①with块：with块结束时，文件会自动关闭
# ②r读/w写/a追加，t（Windows特有模式）
# with open("C:/Users/Administrator/Desktop/test.txt", "w", encoding="UTF-8") as f:
#     f.write("test")

# 边读边写
# with open("C:/Users/Administrator/Desktop/test.txt", "r", encoding="UTF-8") as read:
#     str = ""
#     line = read.readline()
#     while line:
#         line = line.replace("\n", "")
#         str += (line + "+\n")
#         line = read.readline()
#     with open("C:/Users/Administrator/Desktop/test.txt", "w", encoding="UTF-8") as write:
#         write.write(str)

# 读取二进制文件
# with open("C:/Users/Administrator/Desktop/test.bin", "rb") as f:
#     data = f.read()
#     text = data.decode("UTF-8")
#     print(text)

# 写入二进制文件
# with open("C:/Users/Administrator/Desktop/test.bin", "wb") as f:
#     f.write(b"test")  # 写入二进制"test"，而非文本（记事本打开test.bin可以看到"test"）
#     f.write("test".encode("UTF-8"))

# 判断是否为二进制文件
# try:
#     with open("", "r", encoding="UTF-8") as f:
#         line = f.readline()
# except UnicodeDecodeError:
#     print("UnicodeDecodeError")

# ****************************************************************分割线****************************************************************
# todo magic方法

# 以双下划线开头结尾的方法
