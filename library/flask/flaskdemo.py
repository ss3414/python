# ****************************************************************分割线****************************************************************
# todo flask

import json
import time
from urllib.parse import quote

from flask import Flask
from flask import make_response
from flask import render_template
from flask import request
from flask import send_from_directory
from flask_sockets import Sockets
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

app = Flask(
    __name__,
    template_folder="./templates"  # 相对路径
)
sockets = Sockets(app)

@app.route("/")  # 路由
def index():
    html = render_template("index.html", str="str123")  # 相对路径（test.html直接放在flask目录下）
    return html

# 表单
@app.route("/form", methods=["post"])
def form():
    name = request.form.get("name")
    data = {
        "status": 1000,
        "name": name
    }
    json_str = json.dumps(data)
    return json_str

# 下载
@app.route("/download")
def download():
    filename = "idea使用教程2017-06-01.pdf"
    response = make_response(send_from_directory("D:/同步/文档/Idea/", filename, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment;filename={0}".format(quote(filename))
    response.headers["Content-Type"] = "application/octet-stream"
    return response

# WebSocket连接
@sockets.route("/connect")
def connect(ws):
    count = int(ws.receive())
    while count > 0 and not ws.closed:
        ws.send(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        time.sleep(1)
        count -= 1
    ws.close()

if __name__ == "__main__":
    # app.run(host="127.0.0.1", port=8080, debug=True)

    server = pywsgi.WSGIServer(("127.0.0.1", 8080), app, handler_class=WebSocketHandler)
    server.serve_forever()
