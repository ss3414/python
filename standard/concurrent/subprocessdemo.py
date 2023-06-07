# ****************************************************************分割线****************************************************************
# todo 运行外部命令

# import subprocess
#
# # check_output只能运行CMD命令
# out_bytes = subprocess.check_output(["tasklist"])
# out_text = out_bytes.decode("gbk")  # 解码CMD输出编码
# print(out_text)
#
# # Popen运行PowerShell命令（无法获取输出）
# out_bytes = subprocess.Popen(["powershell", "ps"])
# print(out_bytes)

# ************************************************************半分割线******************************
# todo 根据程序名获取PID（进程号）并杀死程序

# import os
# import re
# import signal
# import subprocess
#
# out_bytes = subprocess.check_output(["tasklist"])
# out_text = out_bytes.decode("gbk")  # CMD的输出GBK编码
# # print(out_bytes)
#
# result = re.findall("firefox.exe(\\s*)(.*?)(\\s*)Console", out_text)
#
# if result.__len__() > 0:
#     for i in result:
#         try:
#             os.kill(int(i[1]), signal.SIGTERM)  # Windows下无法使用SIGKILL
#             print("杀死" + i[1])
#         except OSError:
#             print(i[1] + "不存在")
