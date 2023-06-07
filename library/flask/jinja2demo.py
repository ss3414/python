# ****************************************************************分割线****************************************************************
# todo 字符串

from jinja2 import Template

template = Template('''
{{ str }}
''')
print(template.render(str="str123"))

# ************************************************************半分割线******************************
# todo 模板文件

# from jinja2 import Environment
# from jinja2.loaders import FileSystemLoader
#
# env = Environment(loader=FileSystemLoader("C:/Users/Administrator/PycharmProjects/python/library/flask"))
# template = env.get_template("index.html")
# # html = template.render(str="str123")
# users = [
#     {"id": 1, "name": "name1"},
#     {"id": 2, "name": "name2"}
# ]
# html = template.render(users=users)
# print(html)
