# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py


def CheckValue(name, globalValue=False):
    import mcl_platform.data.env
    return mcl_platform.data.env.CheckValue(name, globalValue)


def DeleteValue(name, globalValue=False):
    import mcl_platform.data.env
    mcl_platform.data.env.DeleteValue(name, globalValue)


def GetValue(name, globalValue=False):
    import mcl_platform.data.env
    return mcl_platform.data.env.GetValue(name, globalValue)


def IsTrue(name, globalValue=False):
    import mcl_platform.data.env
    if mcl_platform.data.env.CheckValue(name, globalValue):
        value = mcl_platform.data.env.GetValue(name, globalValue).lower()
        if value == 'true' or value == 'on' or value == 'yes' or value == '1':
            return True
    return False


def SetValue(name, value, globalValue=False):
    import mcl_platform.data.env
    mcl_platform.data.env.SetValue(name, value, globalValue)