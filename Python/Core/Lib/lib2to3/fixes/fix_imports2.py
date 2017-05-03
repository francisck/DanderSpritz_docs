# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_imports2.py
"""Fix incompatible imports and module references that must be fixed after
fix_imports."""
from . import fix_imports
MAPPING = {'whichdb': 'dbm',
   'anydbm': 'dbm'
   }

class FixImports2(fix_imports.FixImports):
    run_order = 7
    mapping = MAPPING