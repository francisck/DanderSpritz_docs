# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_has_key.py
"""Fixer for has_key().

Calls to .has_key() methods are expressed in terms of the 'in'
operator:

    d.has_key(k) -> k in d

CAVEATS:
1) While the primary target of this fixer is dict.has_key(), the
   fixer will change any has_key() method call, regardless of its
   class.

2) Cases like this will not be converted:

    m = d.has_key
    if m(k):
        ...

   Only *calls* to has_key() are converted. While it is possible to
   convert the above to something like

    m = d.__contains__
    if m(k):
        ...

   this is currently not done.
"""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, parenthesize

class FixHasKey(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    anchor=power<\n        before=any+\n        trailer< '.' 'has_key' >\n        trailer<\n            '('\n            ( not(arglist | argument<any '=' any>) arg=any\n            | arglist<(not argument<any '=' any>) arg=any ','>\n            )\n            ')'\n        >\n        after=any*\n    >\n    |\n    negation=not_test<\n        'not'\n        anchor=power<\n            before=any+\n            trailer< '.' 'has_key' >\n            trailer<\n                '('\n                ( not(arglist | argument<any '=' any>) arg=any\n                | arglist<(not argument<any '=' any>) arg=any ','>\n                )\n                ')'\n            >\n        >\n    >\n    "

    def transform(self, node, results):
        syms = self.syms
        if node.parent.type == syms.not_test and self.pattern.match(node.parent):
            return None
        else:
            negation = results.get('negation')
            anchor = results['anchor']
            prefix = node.prefix
            before = [ n.clone() for n in results['before'] ]
            arg = results['arg'].clone()
            after = results.get('after')
            if after:
                after = [ n.clone() for n in after ]
            if arg.type in (syms.comparison, syms.not_test, syms.and_test,
             syms.or_test, syms.test, syms.lambdef, syms.argument):
                arg = parenthesize(arg)
            if len(before) == 1:
                before = before[0]
            else:
                before = pytree.Node(syms.power, before)
            before.prefix = u' '
            n_op = Name(u'in', prefix=u' ')
            if negation:
                n_not = Name(u'not', prefix=u' ')
                n_op = pytree.Node(syms.comp_op, (n_not, n_op))
            new = pytree.Node(syms.comparison, (arg, n_op, before))
            if after:
                new = parenthesize(new)
                new = pytree.Node(syms.power, (new,) + tuple(after))
            if node.parent.type in (syms.comparison, syms.expr, syms.xor_expr,
             syms.and_expr, syms.shift_expr,
             syms.arith_expr, syms.term,
             syms.factor, syms.power):
                new = parenthesize(new)
            new.prefix = prefix
            return new