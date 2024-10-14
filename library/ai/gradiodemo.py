# ****************************************************************分割线****************************************************************
# todo gradio

import webbrowser

import gradio

# 响应按钮的方法
def test(textbox, dropdown):
    return textbox + dropdown

app = gradio.Blocks()
with app:
    with gradio.Tab("Tab"):
        with gradio.Row():
            with gradio.Column():
                markdown = gradio.Markdown("# Markdown")
                textbox = gradio.Textbox(value="textbox")
                dropdown = gradio.Dropdown(choices=["1", "2", "3"], value="1")

            with gradio.Column():
                textbox2 = gradio.Textbox()

                button = gradio.Button("按钮")
                button.click(test, inputs=[textbox, dropdown], outputs=[textbox2])  # 将textbox、dropdown内容输出至textbox2

webbrowser.open("http://127.0.0.1:7860")
app.launch()

# ************************************************************半分割线******************************
# todo 暴露接口到公网

# import json

# import gradio

# def test(input):
#     data = json.loads(input)
#     return data

# interface = gradio.Interface(
#     fn=test,
#     inputs="text",
#     outputs="text",
#     title="test"
# )

# # 本地暴露到公网需要安装frpc_windows
# interface.launch(share=True)

# ************************************************************半分割线******************************
# todo 按钮响应

# import subprocess
# import webbrowser

# import gradio
# import requests

# def test1():
#     result = subprocess.Popen(["C:/ProgramData/anaconda3/envs/pyutil/python.exe", "C:/Users/Administrator/Desktop/test.py"], shell=True)
#     yield result

# def test2():
#     response = requests.get("http://127.0.0.1:8080")
#     yield response.text

# app = gradio.Blocks()
# with app:
#     with gradio.Tab("Tab"):
#         with gradio.Row():
#             with gradio.Column():
#                 textbox1 = gradio.Textbox()
#                 button1 = gradio.Button("按钮1")
#                 button1.click(test1, inputs=[], outputs=[textbox1])
#             with gradio.Column():
#                 textbox2 = gradio.Textbox()
#                 button2 = gradio.Button("按钮2")
#                 button2.click(test2, inputs=[], outputs=[textbox2])

# webbrowser.open("http://127.0.0.1:7860")
# app.launch()

# ************************************************************半分割线******************************
# todo test.py

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def test():
#     return "test"

# app.run(host="127.0.0.1", port=8080, debug=True)
