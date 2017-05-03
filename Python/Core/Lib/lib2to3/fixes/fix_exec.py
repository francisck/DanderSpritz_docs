# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_exec.py
"""Fixer for exec.

This converts usages of the exec statement into calls to a built-in
exec() function.

exec code in ns1, ns2 -> exec(code, ns1, ns2)
"""
from .. import pytree
from .. import fixer_base
from ..fixer_util import Comma, Name, Call

class FixExec(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    exec_stmt< 'exec' a=any 'in' b=any [',' c=any] >\n    |\n    exec_stmt< 'exec' (not atom<'(' [any] ')'>) a=any >\n    "

    def transform(self, node, results):
        syms = self.syms
        a = results['a']
        b = results.get('b')
        c = results.get('c')
        args = [a.clone()]
        args[0].prefix = ''
        if b is not None:
            args.extend([Comma(), b.clone()])
        if c is not None:
            args.extend([Comma(), c.clone()])
        return Call(Name(u'exec'), args, prefix=node.prefix)