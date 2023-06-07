# ****************************************************************分割线****************************************************************
# todo 连接Redis

# from redis import StrictRedis
#
# redis = StrictRedis(host="127.0.0.1", port=6379, db=0, password="")
# redis.set("user", "name1")
# print(redis.get("user"))

# ****************************************************************分割线****************************************************************
# todo 键操作

# from redis import StrictRedis
#
# redis = StrictRedis(host="127.0.0.1", port=6379, db=0, password="")
# # CURD
# print(redis.set("user", "name1"))  # 增加/修改
# print(redis.get("user"))  # 获取
# print(redis.keys("u*"))  # 规则查询
# print(redis.delete("user"))  # 删除

# ****************************************************************分割线****************************************************************
# todo 字符串操作

# from redis import StrictRedis
#
# redis = StrictRedis(host="127.0.0.1", port=6379, db=0, password="")
# print(redis.set("user", "name1"))  # 增加/修改
# print(redis.get("user"))  # 获取
