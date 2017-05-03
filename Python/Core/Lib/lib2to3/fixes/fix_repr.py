# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_repr.py
"""Fixer that transforms `xyzzy` into repr(xyzzy)."""
from .. import fixer_base
from ..fixer_util import Call, Name, parenthesize

class FixRepr(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              atom < '`' expr=any '`' >\n              "

    def transform(self, node, results):
        expr = results['expr'].clone()
        if expr.type == self.syms.testlist1:
            expr = parenthesize(expr)
        return Call(Name(u'repr'), [expr], prefix=node.prefix)