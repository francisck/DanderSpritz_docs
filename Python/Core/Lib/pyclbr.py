# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: pyclbr.py
"""Parse a Python module and describe its classes and methods.

Parse enough of a Python file to recognize imports and class and
method definitions, and to find out the superclasses of a class.

The interface consists of a single function:
        readmodule_ex(module [, path])
where module is the name of a Python module, and path is an optional
list of directories where the module is to be searched.  If present,
path is prepended to the system search path sys.path.  The return
value is a dictionary.  The keys of the dictionary are the names of
the classes defined in the module (including classes that are defined
via the from XXX import YYY construct).  The values are class
instances of the class Class defined here.  One special key/value pair
is present for packages: the key '__path__' has a list as its value
which contains the package search path.

A class is described by the class Class in this module.  Instances
of this class have the following instance variables:
        module -- the module name
        name -- the name of the class
        super -- a list of super classes (Class instances)
        methods -- a dictionary of methods
        file -- the file in which the class was defined
        lineno -- the line in the file on which the class statement occurred
The dictionary of methods uses the method names as keys and the line
numbers on which the method was defined as values.
If the name of a super class is not recognized, the corresponding
entry in the list of super classes is not a class instance but a
string giving the name of the super class.  Since import statements
are recognized and imported modules are scanned as well, this
shouldn't happen often.

A function is described by the class Function in this module.
Instances of this class have the following instance variables:
        module -- the module name
        name -- the name of the class
        file -- the file in which the class was defined
        lineno -- the line in the file on which the class statement occurred
"""
import sys
import imp
import tokenize
from token import NAME, DEDENT, OP
from operator import itemgetter
__all__ = [
 'readmodule', 'readmodule_ex', 'Class', 'Function']
_modules = {}

class Class:
    """Class to represent a Python class."""

    def __init__(self, module, name, super, file, lineno):
        self.module = module
        self.name = name
        if super is None:
            super = []
        self.super = super
        self.methods = {}
        self.file = file
        self.lineno = lineno
        return

    def _addmethod(self, name, lineno):
        self.methods[name] = lineno


class Function:
    """Class to represent a top-level Python function"""

    def __init__(self, module, name, file, lineno):
        self.module = module
        self.name = name
        self.file = file
        self.lineno = lineno


def readmodule(module, path=None):
    """Backwards compatible interface.
    
    Call readmodule_ex() and then only keep Class objects from the
    resulting dictionary."""
    res = {}
    for key, value in _readmodule(module, path or []).items():
        if isinstance(value, Class):
            res[key] = value

    return res


def readmodule_ex(module, path=None):
    """Read a module file and return a dictionary of classes.
    
    Search for MODULE in PATH and sys.path, read and parse the
    module and return a dictionary with one entry for each class
    found in the module.
    """
    return _readmodule(module, path or [])


def _readmodule(module, path, inpackage=None):
    """Do the hard work for readmodule[_ex].
    
    If INPACKAGE is given, it must be the dotted name of the package in
    which we are searching for a submodule, and then PATH must be the
    package search path; otherwise, we are searching for a top-level
    module, and PATH is combined with sys.path.
    """
    if inpackage is not None:
        fullmodule = '%s.%s' % (inpackage, module)
    else:
        fullmodule = module
    if fullmodule in _modules:
        return _modules[fullmodule]
    else:
        dict = {}
        if module in sys.builtin_module_names and inpackage is None:
            _modules[module] = dict
            return dict
        i = module.rfind('.')
        if i >= 0:
            package = module[:i]
            submodule = module[i + 1:]
            parent = _readmodule(package, path, inpackage)
            if inpackage is not None:
                package = '%s.%s' % (inpackage, package)
            return _readmodule(submodule, parent['__path__'], package)
        f = None
        if inpackage is not None:
            f, fname, (_s, _m, ty) = imp.find_module(module, path)
        else:
            f, fname, (_s, _m, ty) = imp.find_module(module, path + sys.path)
        if ty == imp.PKG_DIRECTORY:
            dict['__path__'] = [
             fname]
            path = [fname] + path
            f, fname, (_s, _m, ty) = imp.find_module('__init__', [fname])
        _modules[fullmodule] = dict
        if ty != imp.PY_SOURCE:
            f.close()
            return dict
        stack = []
        g = tokenize.generate_tokens(f.readline)
        try:
            for tokentype, token, start, _end, _line in g:
                if tokentype == DEDENT:
                    lineno, thisindent = start
                    while stack and stack[-1][1] >= thisindent:
                        del stack[-1]

                elif token == 'def':
                    lineno, thisindent = start
                    while stack and stack[-1][1] >= thisindent:
                        del stack[-1]

                    tokentype, meth_name, start = g.next()[0:3]
                    if tokentype != NAME:
                        continue
                    if stack:
                        cur_class = stack[-1][0]
                        if isinstance(cur_class, Class):
                            cur_class._addmethod(meth_name, lineno)
                    else:
                        dict[meth_name] = Function(fullmodule, meth_name, fname, lineno)
                    stack.append((None, thisindent))
                elif token == 'class':
                    lineno, thisindent = start
                    while stack and stack[-1][1] >= thisindent:
                        del stack[-1]

                    tokentype, class_name, start = g.next()[0:3]
                    if tokentype != NAME:
                        continue
                    tokentype, token, start = g.next()[0:3]
                    inherit = None
                    if token == '(':
                        names = []
                        level = 1
                        super = []
                        while True:
                            tokentype, token, start = g.next()[0:3]
                            if token in (')', ',') and level == 1:
                                n = ''.join(super)
                                if n in dict:
                                    n = dict[n]
                                else:
                                    c = n.split('.')
                                    if len(c) > 1:
                                        m = c[-2]
                                        c = c[-1]
                                        if m in _modules:
                                            d = _modules[m]
                                            if c in d:
                                                n = d[c]
                                names.append(n)
                                super = []
                            if token == '(':
                                level += 1
                            elif token == ')':
                                level -= 1
                                if level == 0:
                                    break
                            elif token == ',' and level == 1:
                                pass
                            elif tokentype in (NAME, OP) and level == 1:
                                super.append(token)

                        inherit = names
                    cur_class = Class(fullmodule, class_name, inherit, fname, lineno)
                    if not stack:
                        dict[class_name] = cur_class
                    stack.append((cur_class, thisindent))
                elif token == 'import' and start[1] == 0:
                    modules = _getnamelist(g)
                    for mod, _mod2 in modules:
                        try:
                            if inpackage is None:
                                _readmodule(mod, path)
                            else:
                                try:
                                    _readmodule(mod, path, inpackage)
                                except ImportError:
                                    _readmodule(mod, [])

                        except:
                            pass

                elif token == 'from' and start[1] == 0:
                    mod, token = _getname(g)
                    if not mod or token != 'import':
                        continue
                    names = _getnamelist(g)
                    try:
                        d = _readmodule(mod, path, inpackage)
                    except:
                        continue

                    for n, n2 in names:
                        if n in d:
                            dict[n2 or n] = d[n]
                        elif n == '*':
                            for n in d:
                                if n[0] != '_':
                                    dict[n] = d[n]

        except StopIteration:
            pass

        f.close()
        return dict


def _getnamelist(g):
    names = []
    while True:
        name, token = _getname(g)
        if not name:
            break
        if token == 'as':
            name2, token = _getname(g)
        else:
            name2 = None
        names.append((name, name2))
        while token != ',' and '\n' not in token:
            token = g.next()[1]

        if token != ',':
            break

    return names


def _getname(g):
    parts = []
    tokentype, token = g.next()[0:2]
    if tokentype != NAME and token != '*':
        return (None, token)
    else:
        parts.append(token)
        while True:
            tokentype, token = g.next()[0:2]
            if token != '.':
                break
            tokentype, token = g.next()[0:2]
            if tokentype != NAME:
                break
            parts.append(token)

        return ('.'.join(parts), token)


def _main():
    import os
    mod = sys.argv[1]
    if os.path.exists(mod):
        path = [
         os.path.dirname(mod)]
        mod = os.path.basename(mod)
        if mod.lower().endswith('.py'):
            mod = mod[:-3]
    else:
        path = []
    dict = readmodule_ex(mod, path)
    objs = dict.values()
    objs.sort(lambda a, b: cmp(getattr(a, 'lineno', 0), getattr(b, 'lineno', 0)))
    for obj in objs:
        if isinstance(obj, Class):
            print 'class', obj.name, obj.super, obj.lineno
            methods = sorted(obj.methods.iteritems(), key=itemgetter(1))
            for name, lineno in methods:
                if name != '__path__':
                    print '  def', name, lineno

        elif isinstance(obj, Function):
            print 'def', obj.name, obj.lineno


if __name__ == '__main__':
    _main()