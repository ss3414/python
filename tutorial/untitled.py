# ****************************************************************分割线****************************************************************
# todo 装饰器

# ①装饰器提供Python AOP功能
# ②AOP：Python采用装饰器模式（又叫包装器模式），Java采用代理模式

# def log(func):
#     print("log")
#     func()
#
# def test():
#     print("test")
#
# log(test)  # 需要将函数作为参数传递给log()，且破坏了原有代码逻辑结构

# ************************************************************半分割线******************************
# 简单装饰器

# def log(func):
#     def wrapper(*args, **kwargs):  # *args, **kwargs（可变参数）
#         print("log")
#         return func(*args, **kwargs)
#
#     return wrapper
#
# def test():
#     print("test")
#
# test = log(test)  # 被装饰器装饰后只会运行装饰器内代码，不会运行test()
# test()

# ************************************************************半分割线******************************
# 装饰器语法糖

# import re
#
# def log(func):
#     def wrapper(*args, **kwargs):
#         name = re.search("<function\s(.*?)\s", str(func))[1]
#         print(name)
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @log
# def test():
#     print("test")
#
# test()

# ****************************************************************分割线****************************************************************
# todo 类型检查

# # ①函数注解：对函数的参数/返回值做类型注解，提供给第三方工具检查（mypy）
# # ②变量注解：参数默认值
# def test(str1: str = "str123") -> None:  # 参数str型，返回值None型
#     print("" + str1)
#
# test()  # 打印默认值str123
# test(123)  # 运行报TypeError（类型错误）

# ************************************************************半分割线******************************
# typing

# from typing import List
#
# def test(list: List[str]) -> None:
#     for i in list:
#         print("" + i)
#
# test(["str123"])

# ****************************************************************分割线****************************************************************
# todo 函数式编程

# Python中的函数式编程
# ①Python语法：lambda/列表解析/字典解析/生成器
# ②Python内置函数：map
# ③Python标准库
# ④Python第三方库

# ****************************************************************分割线****************************************************************
# todo Unicode

# 查看字符的Unicode十六进制编码
for i in "０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ":
    unicode = hex(ord(i)).replace("0x", "\\u")
    convert = unicode.encode("UTF-8").decode("unicode_escape")
    print(f"{i}:{unicode}:{convert}")
