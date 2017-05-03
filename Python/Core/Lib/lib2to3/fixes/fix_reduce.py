# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_reduce.py
"""Fixer for reduce().

Makes sure reduce() is imported from the functools module if reduce is
used in that module.
"""
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import

class FixReduce(fixer_base.BaseFix):
    BM_compatible = True
    order = 'pre'
    PATTERN = "\n    power< 'reduce'\n        trailer< '('\n            arglist< (\n                (not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any) |\n                (not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any ','\n                 not(argument<any '=' any>) any)\n            ) >\n        ')' >\n    >\n    "

    def transform(self, node, results):
        touch_import(u'functools', u'reduce', node)