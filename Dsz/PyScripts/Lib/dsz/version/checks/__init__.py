# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import string

def _getenvvalue(name, addr):
    if dsz.env.Check(name, 0, addr):
        return dsz.env.Get(name, 0, addr)
    else:
        return 'UNKNOWN'


def IsOs64Bit(addr=dsz.script.Env['target_address']):
    answer = string.lower(_getenvvalue('_OS_64BIT', addr))
    if answer == 'yes' or answer == 'true':
        return True
    else:
        return False


def IsUnix(addr=dsz.script.Env['target_address']):
    return not dsz.version.checks.IsWindows(addr)


def IsWindows(addr=dsz.script.Env['target_address']):
    ver = dsz.version.Info(addr)
    if ver.os == 'winnt' or ver.os == 'win9x':
        return True
    else:
        return False