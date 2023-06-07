# ****************************************************************分割线****************************************************************
# todo winreg

import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer")

# 遍历
try:
    i = 0
    while 1:
        name, value, type = winreg.EnumValue(key, i)
        str = "type:{type} name:{name} value:{value}".format(type=repr(type), name=repr(value), value=repr(name))
        print(str)
        i += 1
except WindowsError:
    pass

# # 获取
# value, type = winreg.QueryValueEx(key, "")
# print(value)
