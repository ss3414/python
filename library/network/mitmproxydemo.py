# ****************************************************************分割线****************************************************************
# todo mitmproxy

import mitmproxy.http
from mitmproxy import ctx

class Interceptor(object):
    def __init__(self):
        self.count = 0

    def response(self, flow: mitmproxy.http.HTTPFlow):
        request = flow.request
        url = request.url
        ctx.log.info(f"url:{url}")

        response = flow.response
        headers = response.headers
        content_type = headers.get("content-type")
        if content_type is not None:
            ctx.log.info(f"content-type:{content_type}")
            if "text/html" in content_type:
                ctx.log.info(f"content:\n{response.get_content()}")
            else:
                ctx.log.info(f"state:\n{response.get_state()}")

# 以mitmweb插件的方式启动：mitmdump -s mitmproxydemo.py
addons = [Interceptor()]
