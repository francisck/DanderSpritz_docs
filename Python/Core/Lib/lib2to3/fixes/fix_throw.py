# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_throw.py
"""Fixer for generator.throw(E, V, T).

g.throw(E)       -> g.throw(E)
g.throw(E, V)    -> g.throw(E(V))
g.throw(E, V, T) -> g.throw(E(V).with_traceback(T))

g.throw("foo"[, V[, T]]) will warn about string exceptions."""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ArgList, Attr, is_tuple

class FixThrow(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    power< any trailer< '.' 'throw' >\n           trailer< '(' args=arglist< exc=any ',' val=any [',' tb=any] > ')' >\n    >\n    |\n    power< any trailer< '.' 'throw' > trailer< '(' exc=any ')' > >\n    "

    def transform(self, node, results):
        syms = self.syms
        exc = results['exc'].clone()
        if exc.type is token.STRING:
            self.cannot_convert(node, 'Python 3 does not support string exceptions')
            return
        else:
            val = results.get(u'val')
            if val is None:
                return
            val = val.clone()
            if is_tuple(val):
                args = [ c.clone() for c in val.children[1:-1] ]
            else:
                val.prefix = u''
                args = [val]
            throw_args = results['args']
            if 'tb' in results:
                tb = results['tb'].clone()
                tb.prefix = u''
                e = Call(exc, args)
                with_tb = Attr(e, Name(u'with_traceback')) + [ArgList([tb])]
                throw_args.replace(pytree.Node(syms.power, with_tb))
            else:
                throw_args.replace(Call(exc, args))
            return