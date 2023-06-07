# ****************************************************************分割线****************************************************************
# todo 连接/创建数据库

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="2468")
# cursor = connect.cursor()  # 游标（运行SQL/获取结果集）
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print("Database version:", data)
# cursor.execute("CREATE DATABASE python DEFAULT CHARACTER SET utf8")
# connect.close()  # 手动关闭数据库连接

# ****************************************************************分割线****************************************************************
# todo 创建表

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
# cursor = connect.cursor()
# sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))"
# cursor.execute(sql)
# connect.close()

# ****************************************************************分割线****************************************************************
# todo 插入记录

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
# table = "students"
# cursor = connect.cursor()
#
# # 通用插入方法（数据表字典）
# data = {
#     "id": "20120001",
#     "name": "Bob",
#     "age": 20
# }
# keys = ", ".join(data.keys())
# values = ", ".join(["%s"] * len(data))
#
# sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table=table, keys=keys, values=values)
#
# try:
#     if cursor.execute(sql, tuple(data.values())):  # 把数据表字典绑定到%s上
#         print("Successful")
#         connect.commit()  # 对记录的增删改都需要commit()才能生效
# except Exception as e:
#     print(e)
#     connect.rollback()  # 整个try except commit() rollback()构成一个数据库事务（操作失败回滚）
# connect.close()  # 注意批量插入时不要把connect.close()写入循环中

# ************************************************************半分割线******************************
# todo 批量插入

# import time
#
# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
#
# def batch(table, begin, end):
#     cursor = connect.cursor()
#     begin = time.time()
#     for i in range(begin, end + 1):
#         data = {
#             "id": i,
#         }
#         keys = ", ".join(data.keys())
#         values = ", ".join(["%s"] * len(data))
#         sql = "INSERT INTO {table}({keys}) VALUES ({values})".format(table=table, keys=keys, values=values)
#
#         try:
#             if cursor.execute(sql, tuple(data.values())):
#                 connect.commit()
#                 print(i)
#         except Exception as e:
#             print(e)
#     connect.close()
#     end = time.time()
#     print("共耗时:" + str(round(end - begin)) + "秒")
#
# batch("", 1, 100000)  # 10000条约15秒

# ****************************************************************分割线****************************************************************
# todo 更新记录

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
# table = "students"
# cursor = connect.cursor()
#
# # 通用更新方法（没有则插入，有则更新（ON DUPLICATE KEY UPDATE））
# data = {
#     "id": "20120001",
#     "name": "Bob",
#     "age": 21
# }
#
# keys = ", ".join(data.keys())
# values = ", ".join(["%s"] * len(data))
#
# sql = "INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(table=table, keys=keys, values=values)
# update = ",".join([" {key} = %s".format(key=key) for key in data])
# sql += update
# # ①此处拼接的SQL为（INSERT INTO video(id, URL) VALUES (%s, %s) ON DUPLICATE KEY UPDATE id = %s, URL = %s）
# # ②注意数据表字段除了主键其他不能为NOT NULL
#
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print("Successful")
#         connect.commit()
# except Exception as e:
#     print(e)
#     connect.rollback()
# connect.close()

# ****************************************************************分割线****************************************************************
# todo 删除记录

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
# table = "students"
# cursor = connect.cursor()
#
# # 通用删除方法
# condition = "age > 20"
# sql = "DELETE FROM  {table} WHERE {condition}".format(table=table, condition=condition)
#
# try:
#     print(cursor.execute(sql))  # 成功execute()输出1，失败输出0
#     connect.commit()
# except Exception as e:
#     print(e)
#     connect.rollback()
# connect.close()

# ****************************************************************分割线****************************************************************
# todo 查询记录

# import pymysql
#
# connect = pymysql.connect(host="127.0.0.1", port=3306, db="python", user="root", password="2468")
# table = "students"
# cursor = connect.cursor()
#
# sql = "SELECT * FROM " + table + " WHERE age >= 20"
#
# try:
#     cursor.execute(sql)
#     print("Count:", cursor.rowcount)
#     # fetchone()获取结果集第一条结果（返回结果是tuple，元组（不能修改的列表））
#     # 如果结果集共有3条记录，fetchone()获取第一条，fetchall()只能获取剩下两条（cursor游标类似指针）
#     row = cursor.fetchone()
#     while row:
#         print("Row:", row)
#         row = cursor.fetchone()  # 如果结果集数据量大，fetchall()占用开销会非常高，推荐循环+fetchone()
# except Exception as e:
#     print(e)
