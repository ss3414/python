# ****************************************************************分割线****************************************************************
# todo 创建索引

# from elasticsearch import Elasticsearch
# 
# es = Elasticsearch(["127.0.0.1"], port=9200)
# result = es.indices.create(index="untitled", ignore=400)  # ignore=400（忽略400错误（已创建））
# print(result)

# ****************************************************************分割线****************************************************************
# todo 删除索引

# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(["127.0.0.1"], port=9200)
# result = es.indices.delete(index="untitled", ignore=[400, 404])
# print(result)

# ****************************************************************分割线****************************************************************
# todo 插入数据

# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(["127.0.0.1"], port=9200)
#
# data = {
#     "id": 1,
#     "name": "name1",
#     "pwd": "pwd1"
# }
# # result = es.create(index="untitled", doc_type="user", id=1, body=data)
# result = es.index(index="untitled", doc_type="user", body=data)  # 自动生成id
# print(result)

# ****************************************************************分割线****************************************************************
# todo 更新数据

# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(["127.0.0.1"], port=9200)
#
# data = {
#     "id": 2,
#     "name": "name2",
#     "pwd": "pwd2"
# }
# result = es.index(index="untitled", doc_type="user", body=data, id=1)  # 根据id，没有则插入，有则更新
# print(result)

# ****************************************************************分割线****************************************************************
# todo 删除数据

# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(["127.0.0.1"], port=9200)
#
# result = es.delete(index="untitled", doc_type="user", id=1)
# print(result)

# ****************************************************************分割线****************************************************************
# todo 查询数据

# from elasticsearch import Elasticsearch
#
# es = Elasticsearch(["127.0.0.1"], port=9200)
#
# # # title字段ik分词
# # mapping = {
# #     "properties": {
# #         "title": {
# #             "type": "text",
# #             "analyzer": "ik_max_word",
# #             "search_analyzer": "ik_max_word",
# #         }
# #     }
# # }
# # es.indices.create(index="untitled", ignore=400)
# # result = es.indices.put_mapping(index="untitled", doc_type="user", body=mapping)
# # print(result)
#
# # # 测试数据
# # data = {"title": "中华人民共和国"}
# # result = es.index(index="untitled", doc_type="user", body=data, id=1)
# # print(result)
#
# # 查询
# # result = es.search(index="untitled")
# # print(result)
#
# # fixme 全文检索
# dsl = {
#     "query": {
#         "match": {
#             "title": "中国"
#         }
#     }
# }
# result = es.search(index="untitled", body=dsl)
# print(result)

# ****************************************************************分割线****************************************************************
# fixme ElasticSearch SQL

# import requests
#
# address = "http://127.0.0.1:9200"
# explain = "{address}/_plugin/_explain".format(address=address)  # SQL
# # Payload形式发送数据
# response = requests.post(url=explain, headers={"Content-Type": "application/json;charset=UTF-8"}, data="SELECT * FROM untitled")
# print(response.text)
# # print(json.loads(response.text))
