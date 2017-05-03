# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: sre.py
"""This file is only retained for backwards compatibility.
It will be removed in the future.  sre was moved to re in version 2.5.
"""
import warnings
warnings.warn('The sre module is deprecated, please import re.', DeprecationWarning, 2)
from re import *
from re import __all__
from re import _compile