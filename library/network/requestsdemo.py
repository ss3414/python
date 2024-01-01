# ****************************************************************分割线****************************************************************
# todo get请求

# import requests
#
# url = "http://httpbin.org/get"  # http://httpbin.org/get会返回get请求的相应信息
# params = {
#     "name": "name1",
#     "pwd": "pwd1"
# }
#
# response = requests.get(url, params=params)
# print(response)
# print(response.text)
# print(response.status_code)

# ****************************************************************分割线****************************************************************
# todo post请求

# import requests
# from customutil.common import constant
#
# url = "http://httpbin.org/post"
# params = {
#     "name": "name1",
#     "pwd": "pwd1"
# }
#
# response = requests.post(url, params=params, headers=constant.HEADERS)
# print(response)
# print(response.text)
# print(response.status_code)

# ************************************************************半分割线******************************
# todo 发送JSON（application/json）

# import requests
#
# url = "http://127.0.0.1/requestJSON"
# json = {"list": [{"name": "姓名1", "pwd": "pwd1"}, {"name": "姓名2", "pwd": "pwd2"}], "status": 2000}
#
# response = requests.post(url, json=json, headers={"Content-Type": "application/json;charset=UTF-8"})
# print(response.text)

# ****************************************************************分割线****************************************************************
# todo response响应

# import requests
# from customutil.common import constant
# 
# url = "http://www.jianshu.com"
# response = requests.get(url, headers=constant.HEADERS)
# 
# print(type(response), response)
# print(type(response.status_code), response.status_code)
# print(type(response.headers), response.headers)
# print(type(response.cookies), response.cookies)
# print(type(response.url), response.url)
# print(type(response.history), response.history)

# ****************************************************************分割线****************************************************************
# todo 下载二进制数据

# import requests
# from requests.exceptions import ConnectTimeout
#
# try:
#     url = "http://bbs.wuyou.net/static/image/common/logo.png"
#     response = requests.get(url, timeout=5)
#     print(response.content)
#     # with open("logo.png", "wb") as f:
#     #     f.write(response.content)
# except ConnectTimeout as e:
#     print(e)

# ****************************************************************分割线****************************************************************
# todo 模拟登录并获取Cookie

# import re
# 
# import requests
# from customutil.common import constant
# 
# loginURL = "http://bbs.wuyou.net/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1"
# params = {
#     "fastloginfield": "username",
#     "username": "ss2468776986",
#     "password": "Wy12345678",
#     "quickforward": "yes",
#     "handlekey": "ls"
# }
# 
# response = requests.post(loginURL, params=params, headers=constant.HEADERS)
# cookieURL = "http://bbs.wuyou.net/forum.php?mod=guide&view=my"
# response2 = requests.post(cookieURL, cookies=response.cookies, headers=constant.HEADERS)
# if "ss2468776986" in response2.text:
#     cookies = []
#     for i in response.cookies:
#         temp = str(i)
#         name = re.findall("<Cookie (.*?)=", temp)
#         value = re.findall("=(.*?) for", temp)
#         cookie = {"name": name[0], "value": value[0]}
#         cookies.append(cookie)
#     for i in cookies:
#         print(i)

# ************************************************************半分割线******************************
# todo 带Cookie访问

# import requests
# from customutil.common import constant
# 
# url = "https://www.tsdm.love/home.php?mod=spacecp"
# constant.HEADERS["Cookie"] = ""
# response = requests.post(url, headers=constant.HEADERS)
# print(response.text)
# if "ss177" in response.text:
#     print("ss177登录成功")

# ****************************************************************分割线****************************************************************
# todo 设置代理

# from socket import error as socket_error
#
# import requests
# from customutil.common import constant
#
# try:
#     url = "http://httpbin.org/get"
#     address = "127.0.0.1:10808"  # 需要pysocks依赖
#     proxies = {
#         "http": "socks5://" + address,
#         "https": "socks5://" + address
#     }
#     response = requests.get(url, constant.HEADERS, proxies=proxies, verify=False)  # 忽略HTTPS证书
#     print(response.status_code)
#     print(response.text)
# except Exception as e:
#     print(e)

# ****************************************************************分割线****************************************************************
# todo 上传文件

# 上传中文文件名
# ①修改\venv\Lib\site-packages\urllib3\fields.py
# ②注释第45行（value = email.utils.encode_rfc2231(value, "UTF-8")）
# ③将第46行由（value = '%s*=%s' % (name, value)）修改为（value = '%s="%s"' % (name, value)）

# import requests
#
# url = "http://127.0.0.1/singleUpload"
# files = {
#     "uploadFile": open("C:/Users/Administrator/Desktop/test.pdf", "rb")
#     # rb以二进制格式（文件）只读打开一个文件
#     # 相当于<input type="file" name="uploadFile"/>
# }
#
# response = requests.post(url, files=files)
# print("status:" + str(response.status_code))
# print("responseEntity:" + response.text)

# ****************************************************************分割线****************************************************************
# todo 多线程发送请求

import datetime
import threading
from concurrent import futures

import requests

def test(url):
    begin = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    response = requests.get(url)
    end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(threading.current_thread().name + " " + begin + "~" + end + "：" + str(response.status_code))

with futures.ThreadPoolExecutor(max_workers=2) as executor:
    for i in range(2):
        future = executor.submit(test, "https://github.com")

# ****************************************************************分割线****************************************************************
# todo 身份认证

# 以Tomcat Manager为例

# import requests
# from requests.auth import HTTPBasicAuth
#
# url = "http://127.0.0.1"
# response = requests.get(url=url, auth=HTTPBasicAuth("admin", "123456"))
# print(response.text)
