# ****************************************************************分割线****************************************************************
# todo setuptools

# 打包流程
# ①在setup.py路径下运行（python setup.py sdist）生成/dist/demo1-1.0.tar.gz文件
# ②解压后在/demo1-1.0目录下运行（python setup.py install）将demo1-1.0-py3.7.egg文件安装到解释器目录下（/Lib/site-packages）
# （egg是Python早期二进制包格式，安装到PyCharm virtualenv环境下会提示找不到模块，但可以运行）
#
# ③在setup.py路径下运行（python setup.py bdist_wheel）生成/dist/demo1-1.0-py3-none-any.whl文件
# ④在whl文件路径下运行（pip install）将whl文件安装到解释器目录下
# （此时可以在/Lib/site-packages目录下找到demo1和demo1-1.0.dist-info两个文件夹）

from setuptools import setup

setup(
    name="demo1",
    version="1.0",
    packages=["demo1"],  # 打包Python package（包内含有__init__.py文件）
    install_requires=[
    ],
    entry_points={
        "console_scripts": ["test1=demo1.test1:test"]  # 安装demo1包后，直接在命令行输入test()相当于运行demo1包test1文件的test方法
    }
)
