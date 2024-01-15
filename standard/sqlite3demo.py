# ****************************************************************分割线****************************************************************
# todo 插入

import sqlite3

connect = sqlite3.connect("D:/同步/编程/数据/untitled.db")
cursor = connect.cursor()
table = "user"

data = {
    "id": 1,
    "name": "name1",
    "password": open("C:/Users/Administrator/Desktop/test.jpg", "rb").read()
}
keys = ",".join(data.keys())
values = ",".join(["?"] * len(data))
sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
rows = cursor.execute(sql, tuple(data.values()))
connect.commit()
print(rows)

# ************************************************************半分割线******************************
# todo 查询

# import sqlite3
#
# connect = sqlite3.connect("D:/同步/编程/数据/untitled.db")
# cursor = connect.cursor()
# rows = cursor.execute("SELECT * FROM user")
# # rows = cursor.execute("PRAGMA table_info(user)")  # 查询表结构
# for row in rows:
#     open("C:/Users/Administrator/Desktop/test2.jpg", "wb").write(row[2])
#     print(row)
