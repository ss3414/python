# ****************************************************************分割线****************************************************************
# todo 同目录导入
# ①此处为test2导入同级目录文件test1，相对导入为import test1（PyCharm会报错但不影响运行）
# ②但是，将test1/test2所在的demo1目录打包后再安装，运行test2.test()会报找不到test1的错误
# ③绝对导入为from demo1 import test1（此时直接运行test2报错，打包后再安装可运行）
import test1

# from demo1 import test1

def test():
    print("test2:" + __name__)
    test1.test()

if __name__ == "__main__":
    test()
