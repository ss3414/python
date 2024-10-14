# ****************************************************************分割线****************************************************************
# todo filecmp

import filecmp

file1 = "C:/Users/Administrator/Desktop/test_0.txt"
file2 = "C:/Users/Administrator/Desktop/test_2.txt"
print(filecmp.cmp(file1, file2, shallow=False))
