# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: env.py
import _dsz
import sys

def Check(name, id=0, addr=_dsz.dszObj.env['target_address'], checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.env_check(name, id, addr)


def Delete(name, id=0, addr=_dsz.dszObj.env['target_address'], checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.env_delete(name, id, addr)


def Get(name, id=0, addr=_dsz.dszObj.env['target_address'], checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.env_get(name, id, addr)


def Set(name, value, id=0, addr=_dsz.dszObj.env['target_address'], checkForStop=True):
    if checkForStop and _dsz.dszObj.check_for_stop():
        sys.exit(-1)
    return _dsz.dszObj.env_set(name, value, id, addr)