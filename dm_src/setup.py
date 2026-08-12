from setuptools import setup, Extension
from Cython.Build import cythonize
import os

# 定义要编译的模块
extensions = [
    Extension(
        name="bcorr",  # 生成的模块名称
        sources=["src_tools/bcorr.py"],  # 源文件
        extra_compile_args=["-O3"],  # 编译优化
        language="c"
    )
]

setup(
    name="my_compiled_module",
    version="0.1",
    ext_modules=cythonize(
        extensions
    )
)
