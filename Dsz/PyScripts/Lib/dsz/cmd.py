# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cmd.py
import _dsz
import sys

def LastId():
    return _dsz.dszObj.cmd_get_last_id()


def Prompt(c, flags=0, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    if _dsz.dszObj.prompt("Do you want to run command '%s'?" % c, True):
        return _dsz.dszObj.run(c, flags)
    else:
        return False


def Run(c, flags=0, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    rtn = _dsz.dszObj.run(c, flags)
    return rtn[0]


def RunEx(c, flags=0, checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.run(c, flags)


class data:

    def Clear(cmdId):
        return _dsz.dszObj.cmd_data_clear(cmdId)

    def Get(name, type, cmdId=0, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.cmd_data_get(name, type, cmdId)

    def ObjectGet(obj, name, type, cmdId=0, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.cmd_data_obj_get(obj, name, type, cmdId)

    def Size(name, cmdId=0, checkForStop=True):
        if checkForStop and _dsz.dszObj.check_for_stop():
            sys.exit(-1)
        return _dsz.dszObj.cmd_data_get_size(name, cmdId)

    Clear = staticmethod(Clear)
    Get = staticmethod(Get)
    ObjectGet = staticmethod(ObjectGet)
    Size = staticmethod(Size)