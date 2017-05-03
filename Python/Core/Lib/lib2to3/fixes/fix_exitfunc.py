# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: fix_exitfunc.py
"""
Convert use of sys.exitfunc to use the atexit module.
"""
from lib2to3 import pytree, fixer_base
from lib2to3.fixer_util import Name, Attr, Call, Comma, Newline, syms

class FixExitfunc(fixer_base.BaseFix):
    keep_line_order = True
    BM_compatible = True
    PATTERN = "\n              (\n                  sys_import=import_name<'import'\n                      ('sys'\n                      |\n                      dotted_as_names< (any ',')* 'sys' (',' any)* >\n                      )\n                  >\n              |\n                  expr_stmt<\n                      power< 'sys' trailer< '.' 'exitfunc' > >\n                  '=' func=any >\n              )\n              "

    def __init__(self, *args):
        super(FixExitfunc, self).__init__(*args)

    def start_tree(self, tree, filename):
        super(FixExitfunc, self).start_tree(tree, filename)
        self.sys_import = None
        return

    def transform(self, node, results):
        if 'sys_import' in results:
            if self.sys_import is None:
                self.sys_import = results['sys_import']
            return
        else:
            func = results['func'].clone()
            func.prefix = u''
            register = pytree.Node(syms.power, Attr(Name(u'atexit'), Name(u'register')))
            call = Call(register, [func], node.prefix)
            node.replace(call)
            if self.sys_import is None:
                self.warning(node, "Can't find sys import; Please add an atexit import at the top of your file.")
                return
            names = self.sys_import.children[1]
            if names.type == syms.dotted_as_names:
                names.append_child(Comma())
                names.append_child(Name(u'atexit', u' '))
            else:
                containing_stmt = self.sys_import.parent
                position = containing_stmt.children.index(self.sys_import)
                stmt_container = containing_stmt.parent
                new_import = pytree.Node(syms.import_name, [
                 Name(u'import'), Name(u'atexit', u' ')])
                new = pytree.Node(syms.simple_stmt, [new_import])
                containing_stmt.insert_child(position + 1, Newline())
                containing_stmt.insert_child(position + 2, new)
            return