# ****************************************************************分割线****************************************************************
# todo 加入系统路径

import sys

sys.path.append("..")  # 将当前文件的上层目录加入系统路径

from demo1 import test1

def test():
    print("test3:" + __name__)
    test1.test()

if __name__ == "__main__":
    test()
