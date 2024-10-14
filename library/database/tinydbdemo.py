# ****************************************************************分割线****************************************************************
# todo tinydb

from tinydb import TinyDB

db_file = "C:/Users/Administrator/Desktop/index.db"
db = TinyDB(db_file)

for data in db.all():
    print(data)
