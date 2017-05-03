# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_numliterals.py
"""Fixer that turns 1L into 1, 0755 into 0o755.
"""
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Number

class FixNumliterals(fixer_base.BaseFix):
    _accept_type = token.NUMBER

    def match(self, node):
        return node.value.startswith(u'0') or node.value[-1] in u'Ll'

    def transform(self, node, results):
        val = node.value
        if val[-1] in u'Ll':
            val = val[:-1]
        elif val.startswith(u'0') and val.isdigit() and len(set(val)) > 1:
            val = u'0o' + val[1:]
        return Number(val, prefix=node.prefix)