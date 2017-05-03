# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_input.py
"""Fixer that changes input(...) into eval(input(...))."""
from .. import fixer_base
from ..fixer_util import Call, Name
from .. import patcomp
context = patcomp.compile_pattern("power< 'eval' trailer< '(' any ')' > >")

class FixInput(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              power< 'input' args=trailer< '(' [any] ')' > >\n              "

    def transform(self, node, results):
        if context.match(node.parent.parent):
            return
        new = node.clone()
        new.prefix = u''
        return Call(Name(u'eval'), [new], prefix=node.prefix)