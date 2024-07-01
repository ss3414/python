# ****************************************************************分割线****************************************************************
# todo gradio

# import webbrowser
#
# import gradio
#
# # 响应按钮的方法
# def test(textbox, dropdown):
#     return textbox + dropdown
#
# app = gradio.Blocks()
# with app:
#     with gradio.Tab("Tab"):
#         with gradio.Row():
#             with gradio.Column():
#                 markdown = gradio.Markdown("# Markdown")
#                 textbox = gradio.Textbox(value="textbox")
#                 dropdown = gradio.Dropdown(choices=["1", "2", "3"], value="1")
#
#             with gradio.Column():
#                 textbox2 = gradio.Textbox()
#
#                 button = gradio.Button("按钮")
#                 button.click(test, inputs=[textbox, dropdown], outputs=[textbox2])  # 将textbox、dropdown内容输出至textbox2
#
# webbrowser.open("http://127.0.0.1:7860")
# app.launch()

# ************************************************************半分割线******************************
# todo 暴露接口到公网

import json

import gradio

def test(input):
    data = json.loads(input)
    return data

interface = gradio.Interface(
    fn=test,
    inputs="text",
    outputs="text",
    title="test"
)

# 本地暴露到公网需要安装frpc_windows
interface.launch(share=True)
