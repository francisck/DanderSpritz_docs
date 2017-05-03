# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: idle.py
import os.path
import sys
idlelib_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, idlelib_dir)
import idlelib.PyShell
idlelib.PyShell.main()