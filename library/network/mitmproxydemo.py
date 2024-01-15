# ****************************************************************分割线****************************************************************
# todo mitmproxy

import sqlite3

import mitmproxy.http
from mitmproxy import ctx

sqlite_file = "D:/同步/编程/数据/untitled.db"
connect = sqlite3.connect(sqlite_file)
cursor = connect.cursor()

def insert(table, data):
    keys = ",".join(data.keys())
    values = ",".join(["?"] * len(data))
    sql = f"INSERT INTO {table} ({keys}) VALUES ({values})"
    rows = cursor.execute(sql, tuple(data.values()))
    connect.commit()

class Interceptor(object):
    def __init__(self):
        self.count = 0

    def response(self, flow: mitmproxy.http.HTTPFlow):
        request = flow.request
        url = request.url
        request_headers = request.headers
        referer = request_headers.get("referer")
        data = {
            "url": url,
            "referer": referer
        }

        response = flow.response
        response_headers = response.headers
        content_type = response_headers.get("content-type")
        if content_type is not None:
            data["content_type"] = content_type
            # fixme GBK编码网页
            if "html" in content_type or "xml" in content_type:
                data["html"] = response.get_content()
            elif "json" in content_type:
                data["json"] = response.get_content()
            elif "image" in content_type:
                data["img"] = response.get_content()
            else:
                ctx.log.info(f"content_type:{content_type} state:\n{response.get_state()}")
        else:
            ctx.log.info(f"url:{url} referer:{referer}")
        insert("http_archive", data)

# 以mitmweb插件的方式启动：mitmdump -s mitmproxydemo.py
addons = [Interceptor()]
