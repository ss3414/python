# ****************************************************************分割线****************************************************************
# todo Python官方教程目录

# 第4章 流程控制
# 第5章 数据结构
# 第6章 模块
# 第7章 输入输出
# 第8章 错误和异常
# 第9章 类

# ****************************************************************分割线****************************************************************
# todo 4_7 函数定义的更多形式

# # lambda关键字创建匿名函数（将函数作为参数传递）
# k = lambda i: i + 1
# print(k(0))

# ****************************************************************分割线****************************************************************
# todo 5_1 列表的更多特性

# # 列表推导式
# list = [i for i in range(10)]
# print(list)

# ************************************************************半分割线******************************
# 列表排序

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list.sort(reverse=True)  # 降序
# print(list)
# list.sort(reverse=False)  # 升序
# print(list)
# for i in list:
#     print(i)

# ************************************************************半分割线******************************
# 列表N等分

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = len(list) // 3
# splits = [list[i:i + n] for i in range(0, len(list), n)]
# for i in splits:
#     print(i)

# ************************************************************半分割线******************************
# 两个列表求交/并/差集

# list1 = [1, 2, 3]
# list2 = [3, 4, 5]
#
# # 列表推导式交/差集
# list3 = [
#     i for i in list1
#     if i in list2
# ]
# list4 = [
#     i for i in list1
#     if i not in list2
# ]
# print(list3)
# print(list4)
#
# # list转set处理
# list5 = list(set(list1).intersection(set(list2)))
# list6 = list(set(list1).union(set(list2)))
# list7 = list(set(list1).difference(set(list2)))
# print(list5)
# print(list6)
# print(list7)

# ****************************************************************分割线****************************************************************
# todo 5_4 集合

# set1 = {1, 2, 3}
# set2 = set()  # 空集合只能用set()创建，{}是个空字典
# print(set1)
# print(set2)

# 集合推导式
# set3 = {
#     i for i in range(10)
# }
# print(set3)

# ****************************************************************分割线****************************************************************
# todo 6_4 包

# ①包目录下必须包含__init__.py文件（哪怕为空）才被认为是一个包
# ②__init__.py相当于class中的（def __init__(self):）函数
# ③在from import 子包/from import *（所有模块）时用到

# 从concurrent包中导入futures模块
# from concurrent import futures
#
# def test(i):
#     return i
#
# with futures.ThreadPoolExecutor(max_workers=1) as executor:
#     future = executor.submit(test, 1)
#     print(future.result())

# ****************************************************************分割线****************************************************************
# todo 8_3 处理异常

# try:
#     f = open("C:/Users/Administrator/Desktop/test.txt", "r", encoding="UTF-8")
# except Exception as e:
#     # ①Exception捕获除SystemExit/KeyboardInterrupt/GeneratorExit之外的所有异常
#     # ②BaseException捕获所有异常
#     print(e)

# ****************************************************************分割线****************************************************************
# todo 9_2 作用域和命名空间

# Python作用域
# ①命名空间：表示变量的可见范围，同一个命名空间不能有两个相同变量名
# ②LEGB：Local（局部）>Enclosing（闭包外）>Global（全局）>Builtin（内建）

# 内建
# ①内建中包含str类型，如果在Global/Local中定义str，则先调用Global/Local中的str
# print(dir(__builtins__))

# 全局
# str = "str123"
# print(globals())

# 局部
# ①for循环不是局部的，列表推导是
# str = "str123"
# print(locals())

# ************************************************************半分割线******************************
# 函数修改全局变量（dict可以直接修改）

# str = "str123"
#
# def test():
#     str = 123  # 因为局部变量遮蔽，此处的str是test()函数内的变量
#     globals()["str"] = 123  # 通过globals()修改/或者用global定义变量
#     print(locals())
#
# print(globals())
# test()
# print(type(str))

# ****************************************************************分割线****************************************************************
# todo 9_3 类

# class User:  # 旧式类
#     def __init__(self, id, name, pwd):  # 构造方法
#         self.id = id
#         self.__name = name  # __私有属性
#         self.pwd = pwd
#
#     def test(self):
#         print("id:%s" % self.id)
#         print("name:%s" % self.__name)
#         print("pwd:%s" % self.pwd)
#
# user = User(1, "name1", "pwd1")
# user.test()
# print(user._User__name)  # 访问私有属性

# ************************************************************半分割线******************************
# 继承

# class Parent(object):  # 新式类
#     def test(self):
#         print("Parent")
#
# class Son1(Parent):
#     def test(self):  # 重写父类方法
#         print("Son1")
#
# class Son2(Parent):
#     def test(self):
#         print("Son2 test")
#
#     def test2(self):
#         print("Son2 test2")
#
# class GrandSon(Son1, Son2):  # Python支持多继承
#     def test(self):
#         Son1.test(self)
#
# # print(issubclass(Son, Parent))
#
# parent = Parent()
# parent.test()
# son1 = Son1()
# son1.test()
# grandson = GrandSon()
# grandson.test()
# grandson.test2()

# ****************************************************************分割线****************************************************************
# todo 9_8 迭代器

# for i in [1, 2, 3]:  # 循环/遍历/迭代
#     print(i)

# ****************************************************************分割线****************************************************************
# todo 9_9 生成器

# ①生成器函数包含迭代器
# ②生成器核心功能：多次返回？
# ③yield：直译为让步（让当前控制流在yield位置停下来等待外界重启，如果重启则返回外界传入的参数）
# def test(i):
#     if i % 2 == 1:
#         yield "奇数"
#     if i % 2 == 0:
#         yield "偶数"  # return不能在yield后面用，返回值/结束函数各写一遍
#     if i % 2 == 0:
#         return
#     print(i)
#
# def main():
#     i = 1
#     while i <= 10:
#         for j in test(i):  # 生成器函数一律用循环调用
#             yield j
#         i += 1
#
# for i in main():
#     print(i)

# ****************************************************************分割线****************************************************************
# todo 9_10 生成器表达式

# list = [i * i for i in range(10)]
# print(list)
