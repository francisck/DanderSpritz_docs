# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_apply.py
"""Fixer for apply().

This converts apply(func, v, k) into (func)(*v, **k)."""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Call, Comma, parenthesize

class FixApply(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< 'apply'\n        trailer<\n            '('\n            arglist<\n                (not argument<NAME '=' any>) func=any ','\n                (not argument<NAME '=' any>) args=any [','\n                (not argument<NAME '=' any>) kwds=any] [',']\n            >\n            ')'\n        >\n    >\n    "

    def transform(self, node, results):
        syms = self.syms
        func = results['func']
        args = results['args']
        kwds = results.get('kwds')
        prefix = node.prefix
        func = func.clone()
        if func.type not in (token.NAME, syms.atom) and (func.type != syms.power or func.children[-2].type == token.DOUBLESTAR):
            func = parenthesize(func)
        func.prefix = ''
        args = args.clone()
        args.prefix = ''
        if kwds is not None:
            kwds = kwds.clone()
            kwds.prefix = ''
        l_newargs = [
         pytree.Leaf(token.STAR, u'*'), args]
        if kwds is not None:
            l_newargs.extend([Comma(),
             pytree.Leaf(token.DOUBLESTAR, u'**'),
             kwds])
            l_newargs[-2].prefix = u' '
        return Call(func, l_newargs, prefix=prefix)