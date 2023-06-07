# ****************************************************************分割线****************************************************************
# todo beautifulsoup4

from bs4 import BeautifulSoup

# 基本用法
html = '''
<html>
<body>
<div class="test">test1</div>
<div class="test">test2</div>
'''
soup = BeautifulSoup(html, "lxml")  # 自动修正HTML格式
print(soup.prettify())  # 格式化缩进输出
# print(type(soup.div))
# print(soup.div.string)  # 输出第一个
# print(soup.get_text())  # 清除所有标签
