# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def CheckValue(name, globalValue=False):
    import dsz
    if globalValue:
        return dsz.env.Check(name, checkForStop=False)
    else:
        return dsz.env.Check(name, int(dsz.script.Env['script_command_id']), checkForStop=False)


def DeleteValue(name, globalValue=False):
    import dsz
    if globalValue:
        rtn = dsz.env.Delete(name, checkForStop=False)
    else:
        rtn = dsz.env.Delete(name, int(dsz.script.Env['script_command_id']), checkForStop=False)
    if not rtn:
        raise RuntimeError('Delete of %s env value failed' % name)


def GetValue(name, globalValue=False):
    import dsz
    if globalValue:
        return dsz.env.Get(name, checkForStop=False)
    else:
        return dsz.env.Get(name, int(dsz.script.Env['script_command_id']), checkForStop=False)


def SetValue(name, value, globalValue=False):
    import dsz
    if globalValue:
        rtn = dsz.env.Set(name, value, checkForStop=False)
    else:
        rtn = dsz.env.Set(name, value, int(dsz.script.Env['script_command_id']), checkForStop=False)
    if not rtn:
        raise RuntimeError('Set of %s env value failed' % name)