# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: syntax.py
"""Check for errs in the AST.

The Python parser does not catch all syntax errors.  Others, like
assignments with invalid targets, are caught in the code generation
phase.

The compiler package catches some errors in the transformer module.
But it seems clearer to write checkers that use the AST to detect
errors.
"""
from compiler import ast, walk

def check(tree, multi=None):
    v = SyntaxErrorChecker(multi)
    walk(tree, v)
    return v.errors


class SyntaxErrorChecker:
    """A visitor to find syntax errors in the AST."""

    def __init__(self, multi=None):
        """Create new visitor object.
        
        If optional argument multi is not None, then print messages
        for each error rather than raising a SyntaxError for the
        first.
        """
        self.multi = multi
        self.errors = 0

    def error(self, node, msg):
        self.errors = self.errors + 1
        if self.multi is not None:
            print '%s:%s: %s' % (node.filename, node.lineno, msg)
        else:
            raise SyntaxError, '%s (%s:%s)' % (msg, node.filename, node.lineno)
        return

    def visitAssign(self, node):
        pass