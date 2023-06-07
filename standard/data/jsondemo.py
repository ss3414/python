# ****************************************************************分割线****************************************************************
# todo Dict（字典）JSON互转

import json

data = {
    "id": 1,
    "name": "name1",
    "pwd": "pwd1"
}
json_str = json.dumps(data)  # 转换
print(type(json_str))
print(json_str)

data = json.loads(json_str)
# data = list(json.loads(json_str))  # 解析JSON数组
print(type(data))
print(data)

# ****************************************************************分割线****************************************************************
# todo 读写JSON文件

# import json
#
# with open("../untitled/test.json", "w", encoding="UTF-8") as f:
#     data = {
#         "id": 1,
#         "name": "name1",
#         "pwd": "pwd1"
#     }
#     json.dump(data, f)
#
# with open("../untitled/test.json", "r", encoding="UTF-8") as f:
#     data = json.load(f)
#     print(type(data))  # dict
#     print(data)

# ************************************************************半分割线******************************
# todo 读写含中文Unicode的JSON字符串

# import json
#
# json_str = '''
# {
#   "unicode": "test\u4e2d\u6587"
# }
# '''
# data = json.loads(json_str)
# print(data)

# ************************************************************半分割线******************************
# todo 向JSON文件中追加内容

# import json
#
# with open("../untitled/test.json", "r", encoding="UTF-8") as read:
#     jsons = json.load(read)
#     with open("../untitled/test.json", "w", encoding="UTF-8") as write:
#         data = {
#             "name": "name1",
#             "pwd": "pwd1"
#         }
#         jsons.append(data)
#         json.dump(jsons, write, ensure_ascii=False)  # 写入中文)
