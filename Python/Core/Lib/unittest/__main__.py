# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __main__.py
"""Main entry point"""
import sys
if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = 'python -m unittest'
__unittest = True
from .main import main, TestProgram, USAGE_AS_MAIN
TestProgram.USAGE = USAGE_AS_MAIN
main(module=None)