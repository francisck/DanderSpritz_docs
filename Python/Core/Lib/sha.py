# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: sha.py
import warnings
warnings.warn('the sha module is deprecated; use the hashlib module instead', DeprecationWarning, 2)
from hashlib import sha1 as sha
new = sha
blocksize = 1
digest_size = 20
digestsize = 20