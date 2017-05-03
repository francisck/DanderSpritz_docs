# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_except.py
"""Fixer for except statements with named exceptions.

The following cases will be converted:

- "except E, T:" where T is a name:

    except E as T:

- "except E, T:" where T is not a name, tuple or list:

        except E as t:
            T = t

    This is done because the target of an "except" clause must be a
    name.

- "except E, T:" where T is a tuple or list literal:

        except E as t:
            T = t.args
"""
from .. import pytree
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Assign, Attr, Name, is_tuple, is_list, syms

def find_excepts(nodes):
    for i, n in enumerate(nodes):
        if n.type == syms.except_clause:
            if n.children[0].value == u'except':
                yield (
                 n, nodes[i + 2])


class FixExcept(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "\n    try_stmt< 'try' ':' (simple_stmt | suite)\n                  cleanup=(except_clause ':' (simple_stmt | suite))+\n                  tail=(['except' ':' (simple_stmt | suite)]\n                        ['else' ':' (simple_stmt | suite)]\n                        ['finally' ':' (simple_stmt | suite)]) >\n    "

    def transform(self, node, results):
        syms = self.syms
        tail = [ n.clone() for n in results['tail'] ]
        try_cleanup = [ ch.clone() for ch in results['cleanup'] ]
        for except_clause, e_suite in find_excepts(try_cleanup):
            if len(except_clause.children) == 4:
                E, comma, N = except_clause.children[1:4]
                comma.replace(Name(u'as', prefix=u' '))
                if N.type != token.NAME:
                    new_N = Name(self.new_name(), prefix=u' ')
                    target = N.clone()
                    target.prefix = u''
                    N.replace(new_N)
                    new_N = new_N.clone()
                    suite_stmts = e_suite.children
                    for i, stmt in enumerate(suite_stmts):
                        if isinstance(stmt, pytree.Node):
                            break

                    if is_tuple(N) or is_list(N):
                        assign = Assign(target, Attr(new_N, Name(u'args')))
                    else:
                        assign = Assign(target, new_N)
                    for child in reversed(suite_stmts[:i]):
                        e_suite.insert_child(0, child)

                    e_suite.insert_child(i, assign)
                elif N.prefix == u'':
                    N.prefix = u' '

        children = [ c.clone() for c in node.children[:3] ] + try_cleanup + tail
        return pytree.Node(node.type, children)