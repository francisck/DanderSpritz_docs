# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def DisableCommand(command, addr=dsz.script.Env['target_address']):
    return _processCommand('disable', command, addr)


def PromptCommand(command, addr=dsz.script.Env['target_address']):
    return _processCommand('prompt', command, addr)


def _processCommand(action, command, addr):
    if addr == dsz.script.Env['local_address']:
        location = 'local'
    elif addr == dsz.script.Env['target_address']:
        location = 'current'
    else:
        location = 'any'
    x = dsz.control.Method()
    dsz.control.echo.Off()
    return dsz.cmd.Run('%s %s %s' % (action, command, location))