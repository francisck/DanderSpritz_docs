# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def IsLinux(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'linux' or ver.os == 'linux_se':
        return True
    else:
        return False


def IsSeLinux(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'linux_se':
        return True
    else:
        return False


def IsSolaris(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'solaris':
        return True
    else:
        return False