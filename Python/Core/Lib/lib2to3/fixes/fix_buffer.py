# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_buffer.py
"""Fixer that changes buffer(...) into memoryview(...)."""
from .. import fixer_base
from ..fixer_util import Name

class FixBuffer(fixer_base.BaseFix):
    BM_compatible = True
    explicit = True
    PATTERN = "\n              power< name='buffer' trailer< '(' [any] ')' > any* >\n              "

    def transform(self, node, results):
        name = results['name']
        name.replace(Name(u'memoryview', prefix=name.prefix))