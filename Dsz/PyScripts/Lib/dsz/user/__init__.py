# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.user.unix
import dsz.user.windows

def GetCurrent():
    x = dsz.control.Method()
    dsz.control.echo.Off()
    if not dsz.cmd.Run('whoami', dsz.RUN_FLAG_RECORD):
        raise RuntimeError, 'Command failed'
    users = dsz.cmd.data.Get('User::Name', dsz.TYPE_STRING)
    return users[0]