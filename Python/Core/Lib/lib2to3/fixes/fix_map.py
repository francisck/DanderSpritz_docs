# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_map.py
"""Fixer that changes map(F, ...) into list(map(F, ...)) unless there
exists a 'from future_builtins import map' statement in the top-level
namespace.

As a special case, map(None, X) is changed into list(X).  (This is
necessary because the semantics are changed in this case -- the new
map(None, X) is equivalent to [(x,) for x in X].)

We avoid the transformation (except for the special case mentioned
above) if the map() call is directly contained in iter(<>), list(<>),
tuple(<>), sorted(<>), ...join(<>), or for V in <>:.

NOTE: This is still not correct if the original code was depending on
map(F, X, Y, ...) to go on until the longest argument is exhausted,
substituting None for missing values -- like zip(), it now stops as
soon as the shortest argument is exhausted.
"""
from ..pgen2 import token
from .. import fixer_base
from ..fixer_util import Name, Call, ListComp, in_special_context
from ..pygram import python_symbols as syms

class FixMap(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = "\n    map_none=power<\n        'map'\n        trailer< '(' arglist< 'None' ',' arg=any [','] > ')' >\n    >\n    |\n    map_lambda=power<\n        'map'\n        trailer<\n            '('\n            arglist<\n                lambdef< 'lambda'\n                         (fp=NAME | vfpdef< '(' fp=NAME ')'> ) ':' xp=any\n                >\n                ','\n                it=any\n            >\n            ')'\n        >\n    >\n    |\n    power<\n        'map' trailer< '(' [arglist=any] ')' >\n    >\n    "
    skip_on = 'future_builtins.map'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if node.parent.type == syms.simple_stmt:
                self.warning(node, 'You should use a for loop here')
                new = node.clone()
                new.prefix = u''
                new = Call(Name(u'list'), [new])
            elif 'map_lambda' in results:
                new = ListComp(results['xp'].clone(), results['fp'].clone(), results['it'].clone())
            else:
                if 'map_none' in results:
                    new = results['arg'].clone()
                else:
                    if 'arglist' in results:
                        args = results['arglist']
                        if args.type == syms.arglist and args.children[0].type == token.NAME and args.children[0].value == 'None':
                            self.warning(node, 'cannot convert map(None, ...) with multiple arguments because map() now truncates to the shortest sequence')
                            return None
                    if in_special_context(node):
                        return None
                    new = node.clone()
                new.prefix = u''
                new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new