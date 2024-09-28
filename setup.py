from distutils.core import setup, Extension
import numpy as np

rlsa_fast_ext = Extension("rlsa_fast", sources = ["rlsa_fast/rlsa_extension.c"], include_dirs = [np.get_include()])

setup(
    name="rlsa_fast",
    version="0.0.1",
    ext_modules = [rlsa_fast_ext],
)
