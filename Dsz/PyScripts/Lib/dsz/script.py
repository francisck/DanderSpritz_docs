# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: script.py
import _dsz
import sys
Env = _dsz.dszObj.env

def CheckStop(shouldExit=True):
    if _dsz.dszObj.check_for_stop():
        if shouldExit:
            sys.exit(-1)
        else:
            return True
    return False


def IsLocal():
    if _dsz.dszObj.env['script_running_locally'] == 'true':
        return True
    else:
        return False


class data:

    def Add(name, value, type, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_add(name, value, type)

    def Clear(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_clear()

    def End(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_end()

    def Start(name, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_start(name)

    def Store(checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.script_data_store()

    Add = staticmethod(Add)
    Clear = staticmethod(Clear)
    End = staticmethod(End)
    Start = staticmethod(Start)
    Store = staticmethod(Store)