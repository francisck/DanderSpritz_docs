# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_print.py
"""Fixer for print.

Change:
    'print'          into 'print()'
    'print ...'      into 'print(...)'
    'print ... ,'    into 'print(..., end=" ")'
    'print >>x, ...' into 'print(..., file=x)'

No changes are applied if print_function is imported from __future__

"""
from .. import patcomp
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, Comma, String, is_tuple
parend_expr = patcomp.compile_pattern("atom< '(' [atom|STRING|NAME] ')' >")

class FixPrint(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n              simple_stmt< any* bare='print' any* > | print_stmt\n              "

    def transform(self, node, results):
        bare_print = results.get('bare')
        if bare_print:
            bare_print.replace(Call(Name(u'print'), [], prefix=bare_print.prefix))
            return
        else:
            args = node.children[1:]
            if len(args) == 1 and parend_expr.match(args[0]):
                return
            sep = end = file = None
            if args and args[-1] == Comma():
                args = args[:-1]
                end = ' '
            if args and args[0] == pytree.Leaf(token.RIGHTSHIFT, u'>>'):
                file = args[1].clone()
                args = args[3:]
            l_args = [ arg.clone() for arg in args ]
            if l_args:
                l_args[0].prefix = u''
            if sep is not None or end is not None or file is not None:
                if sep is not None:
                    self.add_kwarg(l_args, u'sep', String(repr(sep)))
                if end is not None:
                    self.add_kwarg(l_args, u'end', String(repr(end)))
                if file is not None:
                    self.add_kwarg(l_args, u'file', file)
            n_stmt = Call(Name(u'print'), l_args)
            n_stmt.prefix = node.prefix
            return n_stmt

    def add_kwarg(self, l_nodes, s_kwd, n_expr):
        n_expr.prefix = u''
        n_argument = pytree.Node(self.syms.argument, (
         Name(s_kwd),
         pytree.Leaf(token.EQUAL, u'='),
         n_expr))
        if l_nodes:
            l_nodes.append(Comma())
            n_argument.prefix = u' '
        l_nodes.append(n_argument)