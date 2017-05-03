# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_ne.py
"""Fixer that turns <> into !=."""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base

class FixNe(fixer_base.BaseFix):
    _accept_type = token.NOTEQUAL

    def match(self, node):
        return node.value == u'<>'

    def transform(self, node, results):
        new = pytree.Leaf(token.NOTEQUAL, u'!=', prefix=node.prefix)
        return new