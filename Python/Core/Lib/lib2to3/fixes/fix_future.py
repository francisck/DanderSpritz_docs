# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_future.py
"""Remove __future__ imports

from __future__ import foo is replaced with an empty line.
"""
from .. import fixer_base
from ..fixer_util import BlankLine

class FixFuture(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = 'import_from< \'from\' module_name="__future__" \'import\' any >'
    run_order = 10

    def transform(self, node, results):
        new = BlankLine()
        new.prefix = node.prefix
        return new