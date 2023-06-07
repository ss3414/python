# ****************************************************************分割线****************************************************************
# todo chardet

import chardet

file = "C:/Users/Administrator/Desktop/test.txt"
print(chardet.detect(open(file, "rb").read()))
