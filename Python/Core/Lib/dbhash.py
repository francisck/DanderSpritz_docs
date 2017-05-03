# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: dbhash.py
"""Provide a (g)dbm-compatible interface to bsddb.hashopen."""
import sys
import warnings
warnings.warnpy3k('in 3.x, the dbhash module has been removed', stacklevel=2)
try:
    import bsddb
except ImportError:
    del sys.modules[__name__]
    raise

__all__ = ['error', 'open']
error = bsddb.error

def open(file, flag='r', mode=438):
    return bsddb.hashopen(file, flag, mode)