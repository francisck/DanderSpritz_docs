# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_sys_exc.py
"""Fixer for sys.exc_{type, value, traceback}

sys.exc_type -> sys.exc_info()[0]
sys.exc_value -> sys.exc_info()[1]
sys.exc_traceback -> sys.exc_info()[2]
"""
from .. import fixer_base
from ..fixer_util import Attr, Call, Name, Number, Subscript, Node, syms

class FixSysExc(fixer_base.BaseFix):
    exc_info = [
     u'exc_type', u'exc_value', u'exc_traceback']
    BM_compatible = True
    PATTERN = "\n              power< 'sys' trailer< dot='.' attribute=(%s) > >\n              " % '|'.join(("'%s'" % e for e in exc_info))

    def transform(self, node, results):
        sys_attr = results['attribute'][0]
        index = Number(self.exc_info.index(sys_attr.value))
        call = Call(Name(u'exc_info'), prefix=sys_attr.prefix)
        attr = Attr(Name(u'sys'), call)
        attr[1].children[0].prefix = results['dot'].prefix
        attr.append(Subscript(index))
        return Node(syms.power, attr, prefix=node.prefix)