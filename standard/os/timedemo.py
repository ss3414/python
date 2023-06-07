# ****************************************************************分割线****************************************************************
# todo time

import datetime
import time

# print(datetime.date.today())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 时间转字符串
# print(time.strftime("%y %Y %m %d %H %I %M %S %a %A %b %B %c %j %p %U %w %W %x %X %Z", time.localtime()))  # 格式化符号
print(datetime.datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S"))  # 字符串转时间
# print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])  # 毫秒

# print((datetime.datetime.now() - datetime.datetime.strptime("2021-01-01 00:00:00", "%Y-%m-%d %H:%M:%S")).days)  # 时间差

# print(int(time.time()))  # 当前时间时间戳（10位数）
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(time.time()))))  # 时间戳转时间
# print(time.mktime(time.localtime()))  # 时间转时间戳
