# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_idioms.py
"""Adjust some old Python 2 idioms to their modern counterparts.

* Change some type comparisons to isinstance() calls:
    type(x) == T -> isinstance(x, T)
    type(x) is T -> isinstance(x, T)
    type(x) != T -> not isinstance(x, T)
    type(x) is not T -> not isinstance(x, T)

* Change "while 1:" into "while True:".

* Change both

    v = list(EXPR)
    v.sort()
    foo(v)

and the more general

    v = EXPR
    v.sort()
    foo(v)

into

    v = sorted(EXPR)
    foo(v)
"""
from .. import fixer_base
from ..fixer_util import Call, Comma, Name, Node, BlankLine, syms
CMP = "(n='!=' | '==' | 'is' | n=comp_op< 'is' 'not' >)"
TYPE = "power< 'type' trailer< '(' x=any ')' > >"

class FixIdioms(fixer_base.BaseFix):
    explicit = True
    PATTERN = "\n        isinstance=comparison< %s %s T=any >\n        |\n        isinstance=comparison< T=any %s %s >\n        |\n        while_stmt< 'while' while='1' ':' any+ >\n        |\n        sorted=any<\n            any*\n            simple_stmt<\n              expr_stmt< id1=any '='\n                         power< list='list' trailer< '(' (not arglist<any+>) any ')' > >\n              >\n              '\\n'\n            >\n            sort=\n            simple_stmt<\n              power< id2=any\n                     trailer< '.' 'sort' > trailer< '(' ')' >\n              >\n              '\\n'\n            >\n            next=any*\n        >\n        |\n        sorted=any<\n            any*\n            simple_stmt< expr_stmt< id1=any '=' expr=any > '\\n' >\n            sort=\n            simple_stmt<\n              power< id2=any\n                     trailer< '.' 'sort' > trailer< '(' ')' >\n              >\n              '\\n'\n            >\n            next=any*\n        >\n    " % (TYPE, CMP, CMP, TYPE)

    def match(self, node):
        r = super(FixIdioms, self).match(node)
        if r and 'sorted' in r:
            if r['id1'] == r['id2']:
                return r
            return None
        else:
            return r

    def transform(self, node, results):
        if 'isinstance' in results:
            return self.transform_isinstance(node, results)
        if 'while' in results:
            return self.transform_while(node, results)
        if 'sorted' in results:
            return self.transform_sort(node, results)
        raise RuntimeError('Invalid match')

    def transform_isinstance(self, node, results):
        x = results['x'].clone()
        T = results['T'].clone()
        x.prefix = u''
        T.prefix = u' '
        test = Call(Name(u'isinstance'), [x, Comma(), T])
        if 'n' in results:
            test.prefix = u' '
            test = Node(syms.not_test, [Name(u'not'), test])
        test.prefix = node.prefix
        return test

    def transform_while(self, node, results):
        one = results['while']
        one.replace(Name(u'True', prefix=one.prefix))

    def transform_sort(self, node, results):
        sort_stmt = results['sort']
        next_stmt = results['next']
        list_call = results.get('list')
        simple_expr = results.get('expr')
        if list_call:
            list_call.replace(Name(u'sorted', prefix=list_call.prefix))
        elif simple_expr:
            new = simple_expr.clone()
            new.prefix = u''
            simple_expr.replace(Call(Name(u'sorted'), [new], prefix=simple_expr.prefix))
        else:
            raise RuntimeError('should not have reached here')
        sort_stmt.remove()
        btwn = sort_stmt.prefix
        if u'\n' in btwn:
            if next_stmt:
                prefix_lines = (
                 btwn.rpartition(u'\n')[0], next_stmt[0].prefix)
                next_stmt[0].prefix = u'\n'.join(prefix_lines)
            else:
                end_line = BlankLine()
                list_call.parent.append_child(end_line)
                end_line.prefix = btwn.rpartition(u'\n')[0]