# ****************************************************************分割线****************************************************************

from distutils.core import setup

from Cython.Build import cythonize

# ①打包Cython，命令（python setup.py build_ext --inplace），生成demo.cp37-win_amd64.pyd
# ②运行python，import demo
setup(
    ext_modules=cythonize("demo.pyx")
)
