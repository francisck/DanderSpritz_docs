# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_zip.py
"""
Fixer that changes zip(seq0, seq1, ...) into list(zip(seq0, seq1, ...)
unless there exists a 'from future_builtins import zip' statement in the
top-level namespace.

We avoid the transformation if the zip() call is directly contained in
iter(<>), list(<>), tuple(<>), sorted(<>), ...join(<>), or for V in <>:.
"""
from .. import fixer_base
from ..fixer_util import Name, Call, in_special_context

class FixZip(fixer_base.ConditionalFix):
    BM_compatible = True
    PATTERN = "\n    power< 'zip' args=trailer< '(' [any] ')' >\n    >\n    "
    skip_on = 'future_builtins.zip'

    def transform(self, node, results):
        if self.should_skip(node):
            return None
        else:
            if in_special_context(node):
                return None
            new = node.clone()
            new.prefix = u''
            new = Call(Name(u'list'), [new])
            new.prefix = node.prefix
            return new