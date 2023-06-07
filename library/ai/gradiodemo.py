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
