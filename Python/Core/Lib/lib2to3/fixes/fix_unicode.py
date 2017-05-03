# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_unicode.py
"""Fixer that changes unicode to str, unichr to chr, and u"..." into "...".

"""
import re
from ..pgen2 import token
from .. import fixer_base
_mapping = {u'unichr': u'chr',u'unicode': u'str'}
_literal_re = re.compile(u'[uU][rR]?[\\\'\\"]')

class FixUnicode(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = "STRING | 'unicode' | 'unichr'"

    def transform(self, node, results):
        if node.type == token.NAME:
            new = node.clone()
            new.value = _mapping[node.value]
            return new
        if node.type == token.STRING:
            if _literal_re.match(node.value):
                new = node.clone()
                new.value = new.value[1:]
                return new