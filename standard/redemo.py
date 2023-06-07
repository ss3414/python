# ****************************************************************分割线****************************************************************
# todo re

# ①Linux文本处理三剑客：grep/sed/awk
# ②文本处理语言：Perl

# ****************************************************************分割线****************************************************************
# todo match

# match从字符串开头开始匹配，一旦开头不匹配，整个匹配失败

# import re
#
# content = "https://cuiqingcai.com/5530.html"
# match = re.match("https(.*)com(.*)html", content)
# print(match)
# print(match.group())
# print(match.group(0))  # group(0)等同于group()
# print(match.group(1))  # group(1)第一个圆括号内匹配的内容
# print(match.span())  # group()长度

# ****************************************************************分割线****************************************************************
# todo search

# search只返回匹配的第一个结果

# import re
#
# content = "http://cuiqingcai.com" + "https://cuiqingcai.com/5530.html"
# match = re.search("https(.*)com(.*)html", content)
# print(match)
# print(match.group())

# ************************************************************半分割线******************************
# todo 正则处理Unicode

# import re
#
# # 直接写\u4e2d\u6587就是"中文"的Unicode
# str = '''
# \\u4e2d\\u6587
# '''
# print(str)  # \u4e2d\u6587
# print(str.encode("UTF-8").decode("unicode_escape"))  # 中文（字符串格式Unicode转中文）
#
# match = re.search(r"\\u.{4}", str)
# print(match[0])

# ************************************************************半分割线******************************
# todo re.sub()全部替换

# import re
#
# str = "str\"str\"str\""
# print(re.sub("\"", "\\\"", str))
#
# # 压缩到一行
# str = '''
#     <span>
#     *
#     </span>
# '''
# str = re.sub("(^\s*)|(\n^)", "", str, flags=re.MULTILINE)  # 多行模式
# print(str)

# ****************************************************************分割线****************************************************************
# todo findall

# findall默认输出圆括号内匹配中的内容

# import re
# #
# # content = "https://cuiqingcai.com\n" + "https://cuiqingcai.com/5530.html"
# # match = re.findall("https(.*)com", content)
# # print(match)

# ****************************************************************分割线****************************************************************
# todo 零宽断言

# import re
#
# content = "123abc456"
# # match = re.findall("\d*", content)  # 123/456
# # match = re.findall("\d*(?=a)", content)  # 123（正向，匹配以a结尾的数字但不包括a本身）
# match = re.findall("\d*(?!a)", content)  # 12/456（反向，匹配不以a结尾的数字）
# print(match)
