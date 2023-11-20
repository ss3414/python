# ****************************************************************分割线****************************************************************
# todo 连接MongoDB

# import pymongo
#
# # untitled数据库，user表（集合）
# client = pymongo.MongoClient(host="127.0.0.1", port=27017, username="root", password="2468")
# db = client["untitled"]
# collection = db["user"]
# print(type(collection))

# ****************************************************************分割线****************************************************************
# todo 插入

# import pymongo
#
# client = pymongo.MongoClient(host="127.0.0.1", port=27017, username="root", password="2468")
# db = client["untitled"]
# collection = db["user"]
#
# user1 = {
#     "_id": 1,  # Python3的int即为Python2的long，可是插入MongoDB中的却为int
#     "name": "name1",
#     "password": "pwd1",
# }
# user2 = {
#     "_id": 2,
#     "name": "name2",
#     "password": "pwd2",
# }
# user3 = {
#     "_id": 3,
#     "name": "name1",
#     "password": "pwd1",
# }
# user4 = {
#     "_id": 4,
#     "name": "name1",
#     "password": "pwd1",
# }
# result = collection.insert_many([user1, user2, user3, user4])
# print(result)

# ****************************************************************分割线****************************************************************
# todo 查询

# import pymongo
#
# client = pymongo.MongoClient(host="127.0.0.1", port=27017, username="root", password="2468")
# db = client["untitled"]
# collection = db["user"]
#
# # find_one（返回查询到的第一条记录）
# result = collection.find_one({"name": "name1"})
# print(type(result))
# print(result)
#
# # find（返回生成器，再遍历生成器）
# results = collection.find({"name": "name1"}, {"name": 1})
# for result in results:
#     print(result)
#
# # 条件查询
# results = collection.find({"_id": {"$gte": 2}})
# for result in results:
#     print(result)
#
# # 计数
# count = collection.find({"_id": {"$gte": 2}}).count()
# print(count)
#
# # 排序
# results = collection.find({"_id": {"$gte": 2}}).sort("_id", pymongo.DESCENDING)
# print(results)
# for result in results:
#     print(result)
#
# # 偏移
# results = collection.find({"_id": {"$gte": 2}}).skip(1).limit(2)
# print(results)
# for result in results:
#     print(result)

# ****************************************************************分割线****************************************************************
# todo 更新

# import pymongo
#
# client = pymongo.MongoClient(host="127.0.0.1", port=27017, username="root", password="2468")
# db = client["untitled"]
# collection = db["user"]
#
# # 整体更新（不推荐）
# condition = {"name": "name1"}
# user = collection.find_one(condition)
# user["password"] = "pwd2"
# result = collection.update(condition, user)
# print(result)
#
# # 更新指定字段
# condition = {"name": "name1"}
# result = collection.update_one(condition, {"$set": {"password": "pwd3"}})
# print(result)
# print(result.matched_count, result.modified_count)  # 符合条件1个，更新1个
#
# # 批量更新
# condition = {"name": "name1"}
# result = collection.update_many(condition, {"$set": {"password": "pwd3"}})
# print(result)
# print(result.matched_count, result.modified_count)

# ****************************************************************分割线****************************************************************
# todo 删除

# import pymongo
# from bson import ObjectId  # 必须用pymongo自带的bson
#
# client = pymongo.MongoClient(host="127.0.0.1", port=27017, username="root", password="2468")
# db = client["untitled"]
# collection = db["user"]
#
# # 根据自生成id删除
# # result = collection.delete_one({"_id": ObjectId("5ea793545eaf338c9c4e90dc")})
# # print(result.deleted_count)
#
# # 条件删除
# # result = collection.delete_many({"name": "name1"})
# # print(result.deleted_count)
#
# # 边查边删
# results = collection.find({"_id": {"$exists": True}})
# ids = []
# for result in results:
#     ids.append(result["_id"])
# for id in ids:
#     collection.delete_one({"_id": ObjectId(id)})
