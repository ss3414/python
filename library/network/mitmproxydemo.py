# ****************************************************************分割线****************************************************************
# todo mitmproxy

import mitmproxy.http
from mitmproxy import ctx

class Counter(object):
    def __init__(self):
        self.count = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.count = self.count + 1
        ctx.log.info("count:%d" % self.count)

# 以mitmweb插件的方式启动：mitmdump -s mitmproxydemo.py
addons = [Counter()]
