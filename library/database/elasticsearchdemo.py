# ****************************************************************分割线****************************************************************
# todo ElasticSearch

# from elasticsearch import Elasticsearch
#
# client = Elasticsearch(hosts="http://127.0.0.1:9200")
# index = "untitled"
#
# # result = client.indices.create(index=index)  # 创建索引
# result = client.indices.delete(index=index)  # 删除索引
#
# # 插入数据
# # data = {
# #     "name": "name1",
# #     "pwd": "pwd1"
# # }
# # result = client.create(index=index, id="1", document=data)
# # # result = client.index(index=index, document=data)  # 自动生成id
#
# # # 更新数据
# # data = {
# #     "name": "name2",
# #     "pwd": "pwd2"
# # }
# # result = client.update(index=index, id="1", doc=data)
#
# # # 删除数据
# # result = client.delete(index=index, id="1")
# print(result)

# ****************************************************************分割线****************************************************************
# todo 查询数据

# from elasticsearch import Elasticsearch
#
# client = Elasticsearch(hosts="http://127.0.0.1:9200")
# index = "untitled"
#
# # # title字段ik分词
# # index_settings = {
# #     "settings": {
# #         "analysis": {
# #             "analyzer": {
# #                 "ik_analyzer": {
# #                     "tokenizer": "ik_smart"
# #                 }
# #             }
# #         }
# #     },
# #     "mappings": {
# #         "properties": {
# #             "title": {
# #                 "type": "text",
# #                 "analyzer": "ik_analyzer",
# #                 "search_analyzer": "ik_analyzer"
# #             }
# #         }
# #     }
# # }
# # client.indices.create(index=index, body=index_settings)
# # client.create(index=index, id="1", document={"title": "战地是第一人称射击游戏"})
#
# # # 查询
# # result = client.search(index=index)
# # print(result)
#
# # 全文检索
# dsl = {
#     "query": {
#         "match": {
#             "title": "射击"
#         }
#     }
# }
# result = client.search(index=index, body=dsl)
# print(result)
