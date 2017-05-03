# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_intern.py
"""Fixer for intern().

intern(s) -> sys.intern(s)"""
from .. import pytree
from .. import fixer_base
from ..fixer_util import Name, Attr, touch_import

class FixIntern(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'intern'\n           trailer< lpar='('\n                    ( not(arglist | argument<any '=' any>) obj=any\n                      | obj=arglist<(not argument<any '=' any>) any ','> )\n                    rpar=')' >\n           after=any*\n    >\n    "

    def transform(self, node, results):
        syms = self.syms
        obj = results['obj'].clone()
        if obj.type == syms.arglist:
            newarglist = obj.clone()
        else:
            newarglist = pytree.Node(syms.arglist, [obj.clone()])
        after = results['after']
        if after:
            after = [ n.clone() for n in after ]
        new = pytree.Node(syms.power, Attr(Name(u'sys'), Name(u'intern')) + [pytree.Node(syms.trailer, [results['lpar'].clone(), newarglist, results['rpar'].clone()])] + after)
        new.prefix = node.prefix
        touch_import(None, u'sys', node)
        return new