# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_LISTEN = dsz.RPC_INFO_LISTEN
    RPC_INFO_CONNECT = dsz.RPC_INFO_CONNECT
    RPC_INFO_COMMAND = dsz.RPC_INFO_COMMAND
    RPC_INFO_WAIT = dsz.RPC_INFO_WAIT
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)