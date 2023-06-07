# ****************************************************************分割线****************************************************************
# todo pyquery

from pyquery import PyQuery

# # 字符串初始化
# html = '''
# <div class="test"></div>
# '''
# element = PyQuery(html)
# print(type(element))
# print(element)
# print(type(element("div")))
# print(element("div"))

# URL初始化
# element = PyQuery(url="https://github.com")
# print(element)

# 文件初始化
# element = PyQuery(filename="../../untitled/test.html")
# print(element)

# 文件编码问题
with open("../../untitled/test.html", "r", encoding="UTF-8") as f:
    content = f.read()
element = PyQuery(content)
print(element)

# CSS选择器
# html = '''
# <div class="test"></div>
# <div class="test"></div>
# '''
# element = PyQuery(html)
# print(type(element(".test")))  # 类型为PyQuery
# print(type(element(".test").items()))  # 类型为generator，生成器（无法确定长度）
# for i in element(".test").items():
#     print(i("div"))

# 子节点
# html = '''
# <div class="parent">
# <div class="son"></div>
# </div>
# '''
# element = PyQuery(html)
# parent = element(".parent")
# son = parent.find(".son")
# print(son)

# 父节点
# html = '''
# <div class="parent">
# <div class="son">
# <div class="grandson"></div>
# </div>
# </div>
# '''
# element = PyQuery(html)
# grandson = element(".grandson")
# son = grandson.parent()  # 直接父节点
# parent = grandson.parents()  # 所有父节点
# print(son)
# print(parent)  # 输出.parent/.son节点
# print(parent(".parent"))  # 只输出.parent节点

# 兄弟节点
# html = '''
# <div class="parent">
# <div class="son1"></div>
# <div class="son2"></div>
# <div class="son3 active"></div>
# </div>
# '''
# element = PyQuery(html)
# son2 = element(".son2")
# son = son2.siblings()
# print(son)
# print(son(".active"))

# 遍历
# html = '''
# <div class="test"></div>
# <div class="test"></div>
# '''
# element = PyQuery(html)
# print(type(element(".test")))
# print(type(element(".test").items()))
# for i in element(".test").items():
#     print(i("div"))

# 获取属性
# html = '''
# <div class="test 1"></div>
# <div class="test 2"></div>
# '''
# element = PyQuery(html)
# test = element(".test")
# for i in element(".test").items():
#     print(i.attr("class"))

# 获取文本
# html = '''
# <div class="test1">
# <div class="test2">
# 内容
# </div>
# </div>
# '''
# element = PyQuery(html)
# test1 = element(".test1")
# print(test1.text())  # text()返回所有节点
# print(test1.html())  # html()返回第一个节点

# 节点操作
# html = '''
# <div class="test1">
# 内容
# <div class="test2">
# </div>
# </div>
# '''
# element = PyQuery(html)
# test1 = element(".test1")
# test1 = test1.remove(".test2")
# print(test1.html())

# ****************************************************************分割线****************************************************************
# todo 设置代理

# import socket
# 
# import socks
# from pyquery import PyQuery
# 
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
# }
# url = "http://www.google.co.jp"
# 
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)
# socket.socket = socks.socksocket
# 
# element = PyQuery(url=url, headers=headers)
# print(type(element))
