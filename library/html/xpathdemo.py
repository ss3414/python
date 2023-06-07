# ****************************************************************分割线****************************************************************
# todo xpath

from lxml import etree

# 读取HTML文件进行解析
# element = etree.parse("test.html", etree.HTMLParser())
# elements = etree.tostring(element)
# print(type(elements))

html = '''
<div>
    <ul>
        <li><a>link1</a></li>
        <li class="test"><a href="../../untitled/test.html" target="_blank" class="c1 c2">link2</a></li>
    </ul>
</div>
'''

# 所有节点
# element = etree.HTML(html, etree.HTMLParser())
# elements = element.xpath("//*")
# print(elements)
# for i in elements:
#     print(etree.tostring(i).decode("UTF-8"))

# 子节点
# element = etree.HTML(html, etree.HTMLParser())
# # elements = element.xpath("//li/a")  # /：获取li下直接子节点
# elements = element.xpath("//ul//a")  # //：获取ul下所有子节点
# print(elements)
# for i in elements:
#     print(etree.tostring(i).decode("UTF-8"))

# 父节点
# element = etree.HTML(html, etree.HTMLParser())
# # elements = element.xpath("//a[@href='test.html']/../@class")  # 通过..获取父节点（/../两个斜杠是必须的？）
# elements = element.xpath("//a[@href='test.html']/parent::*/@class")  # 通过parent::获取父节点（*？）
# print(elements)

# 属性匹配+逻辑运算符
# element = etree.HTML(html, etree.HTMLParser())
# # elements = element.xpath("//a[@href='test.html']")  # 相等
# # elements = element.xpath("//a[contains(@href,'test')]")  # 包含
# # elements = element.xpath("//a[@*='test.html']")  # 任意属性
# # elements = element.xpath("//a[contains(@href,'test') and @target='_blank']")  # and
# # elements = element.xpath("//a[@href='test.html' or @target='_blank']")  # or
# elements = element.xpath("//a[contains(@class,'c1') and contains(@class,'c2')]")  # 属性多值匹配（class）
# for i in elements:
#     print(etree.tostring(i).decode("UTF-8"))

# 获取文本
# element = etree.HTML(html, etree.HTMLParser())
# elements = element.xpath("//li/a/text()")
# print(elements)

# 获取属性
# element = etree.HTML(html, etree.HTMLParser())
# elements = element.xpath("//a[@href='test.html']/@target")
# print(elements)

# 按序选择
# element = etree.HTML(html, etree.HTMLParser())
# # elements = element.xpath("//li[1]/a")
# # elements = element.xpath("//li[last()]/a")
# elements = element.xpath("//li[position()<2]/a")
# for i in elements:
#     print(etree.tostring(i).decode("UTF-8"))

# 节点轴选择
element = etree.HTML(html, etree.HTMLParser())
# elements = element.xpath("//li[2]/ancestor::*")  # 祖先
# elements = element.xpath("//li[2]/child::*")  # 直接子节点
# elements = element.xpath("//li[2]/descendant::*")  # 所有子节点
# elements = element.xpath("//li[2]/attribute::*")  # 属性
# elements = element.xpath("//li[1]/following::*")  # 当前节点后的同级节点及其子节点
elements = element.xpath("//li[1]/following-sibling::*")  # 当前节点后的同级节点
for i in elements:
    print(etree.tostring(i).decode("UTF-8"))
