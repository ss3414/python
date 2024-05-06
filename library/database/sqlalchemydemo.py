# ****************************************************************分割线****************************************************************
# todo sqlalchemy

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class User(declarative_base()):  # 实体类
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    # password = Column(String(255))
    # file = Column(BLOB())

# 连接MySQL需要pymysql
url = "mysql+pymysql://{user}:{pwd}@{host}:{port}/untitled".format(host="127.0.0.1", port="3306", user="root", pwd="2468")
engine = create_engine(url, echo=True)  # echo调试
DBSession = sessionmaker(bind=engine)
session = DBSession()

# # 插入
# user = User(
#     name="name1",
#     password=""
# )
# with open("/home/fantasy/Downloads/test.pdf", "rb") as f:
#     user.file = f.read()
# session.add(user)

# # 批量插入
# users = [User(name="name1"), User(name="name2")]
# session.add_all(users)

# # 修改
# user = session.query(User).filter(User.id == 1).update({User.name: "name2"})
# print(user)  # 操作的记录数

# # 删除
# user = session.query(User).filter(User.id == 1).delete()
# print(user)

# # 查询
# user = session.query(User).filter(User.id == 1).first()  # where id=0 limit 0,1
# print(user.id)

# # like
# users = session.query(User).filter(User.name.like("%user%")).all()
# print(len(users))

# # 部分字段
# users = session.query(User.id).all()
# ids = [
#     user.id for user in users
# ]
# print(ids)

# 分页
page = 1
size = 2
users = session.query(User).slice((page - 1) * size, page * size)
for user in users:
    print(user.id)
    # count = session.query(User).filter(User.id == user.id).update({User.name: "name"})  # 边查边改
# print(session.query(User).count())

# 多条件/排序
# users = session.query(User).filter(User.id == 1).filter(User.name == "name1").order_by(User.id.desc())
# users = session.query(User).filter(text("id=:id AND site=:site")).params(id=1, site="无忧启动论坛")
# users = session.query(User).filter(User.id.in_([1, 2]))
# for i in users:
#     print(i)

# session.commit()
# session.close()
