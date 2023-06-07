# ****************************************************************分割线****************************************************************
# todo base64

import base64

# 图片转base64
with open("C:/Users/Administrator/Desktop/test.jpg", "rb") as f:
    data = base64.b64encode(f.read())
    # print(data)  # u开头Unicode，r开头转义符，b开头byte
    print(data.decode())  # 字符串

# ①img标签使用<img src="data:image/jpg;base64,data">
# ②在网页中保存需要手动重命名文件名
