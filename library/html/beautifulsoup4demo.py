# ****************************************************************分割线****************************************************************
# todo beautifulsoup4

# from bs4 import BeautifulSoup

# # 基本用法
# html = '''
# <html>
# <body>
# <div class="test">test1</div>
# <div class="test">test2</div>
# '''
# soup = BeautifulSoup(html, "lxml")  # 自动修正HTML格式
# print(soup.prettify())  # 格式化缩进输出
# print(type(soup.div))
# print(soup.div.string)  # 输出第一个
# print(soup.get_text())  # 清除所有标签

# ************************************************************半分割线******************************
# fixme 遍历所有标签并获取内容

import re

from bs4 import BeautifulSoup

# 文本与标签混合，文本无法提取
def html_recursive(tag, html_list):
    if tag.find_all():
        for child in tag.children:
            if child.name:
                html_recursive(child, html_list)
    elif tag.string:
        html_list.append(tag.string.strip())

def html_bs_input(html_file):
    dialogs, contents = [], []
    soup = BeautifulSoup(open(html_file, "r", encoding="UTF-8"), "html.parser")
    for tag in soup.find_all(True):
        html_recursive(tag, contents)
    for content in contents:
        match = re.search("", content)
        if match:
            dialogs.append(content)

html_bs_input("")
