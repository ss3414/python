# ****************************************************************分割线****************************************************************
# todo 查询记录

import sqlite3

connect = sqlite3.connect("D:/同步/编程/数据/untitled.db")
cursor = connect.cursor()
rows = cursor.execute("SELECT * FROM user")
# rows = cursor.execute("PRAGMA table_info(user)")  # 查询表结构
for row in rows:
    print(row)
