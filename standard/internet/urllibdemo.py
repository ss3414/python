# ****************************************************************分割线****************************************************************
# todo 分析robots.txt

# 根据位于网站根目录下的robots.txt判断网页是否允许爬取

# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser()
# rp.set_url("https://github.com/robots.txt")
# rp.read()
# print(rp.can_fetch("Googlebot", "https://github.com"))  # 此处伪装成Google的爬虫

# ****************************************************************分割线****************************************************************
# todo 设置代理

# import socket
# from urllib import request
#
# import socks
#
# url = "http://httpbin.org/get"
#
# socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1080)  # 需要pysocks依赖
# socket.socket = socks.socksocket
#
# response = request.urlopen(url)
# print(response.read().decode("UTF-8"))

# ****************************************************************分割线****************************************************************
# todo URL解析

from urllib import parse

urldecode = "http://www.test.com?para1=1&para2=test&para3=test=2&para4=中文"
# 编码后
urlencode = "http%3a%2f%2fwww.test.com%3fpara1%3d1%26para2%3dtest%26para3%3dtest%3d2%26para4%3d%e4%b8%ad%e6%96%87"

print(parse.quote(urldecode))  # 编码
print(parse.parse_qsl(parse.urlparse(urldecode).query))
print(parse.parse_qsl(parse.urlparse(parse.unquote(urlencode)).query))  # 解码后再解析
