# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def ImportNamesWithNamespace(namespace, module, callerGlobals):
    _temp = __import__(namespace + module, callerGlobals, locals(), [module], -1)
    reload(_temp)
    for name in _temp.__dict__.keys():
        if not name.startswith('_'):
            callerGlobals[name] = _temp.__dict__[name]


def ImportWithNamespace(namespace, module, callerGlobals=None):
    _temp = __import__(namespace + module, callerGlobals, locals(), [module], -1)
    reload(_temp)
    if len(namespace) > 0 and callerGlobals != None:
        import sys
        topName = module.partition('.')[0]
        callerGlobals[topName] = sys.modules[namespace + topName]
    return