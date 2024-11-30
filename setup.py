from distutils.core import setup, Extension
import numpy as np

rlsa_fast_ext = Extension("rlsafast", sources = ["rlsa_fast/rlsa_extension.c"], include_dirs = [np.get_include()])

setup(
    name="rlsafast",
    version="0.0.3",
    ext_modules = [rlsa_fast_ext],
)
