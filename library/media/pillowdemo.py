# ****************************************************************分割线****************************************************************
# todo pillow

# PIL的Python3分支

from PIL import Image

# 图片压缩
# ①只有jpg有quality选项（png转换成jpg再压缩）
# ②quality是个绝对值，对压缩过的图片再压缩基本不会改变其体积
img = Image.open("C:/Users/Administrator/Desktop/test.jpg")
img.save("C:/Users/Administrator/Desktop/test.jpg", quality=50)
