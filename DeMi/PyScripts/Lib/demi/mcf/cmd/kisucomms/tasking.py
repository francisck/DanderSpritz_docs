# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking.py
import mcl_platform.tasking
from tasking_dsz import *
_fw = mcl_platform.tasking.GetFramework()
if _fw == 'dsz':
    RPC_INFO_LIST = dsz.RPC_INFO_LIST
    RPC_INFO_CONNECT = dsz.RPC_INFO_CONNECT
    RPC_INFO_CONFIG = dsz.RPC_INFO_CONFIG
    RPC_INFO_ADD_MODULE = dsz.RPC_INFO_ADD_MODULE
    RPC_INFO_DELETE_MODULE = dsz.RPC_INFO_DELETE_MODULE
    RPC_INFO_READ_MODULE = dsz.RPC_INFO_READ_MODULE
    RPC_INFO_LOAD_DRIVER = dsz.RPC_INFO_LOAD_DRIVER
    RPC_INFO_UNLOAD_DRIVER = dsz.RPC_INFO_UNLOAD_DRIVER
    RPC_INFO_LOAD_MODULE = dsz.RPC_INFO_LOAD_MODULE
    RPC_INFO_FREE_MODULE = dsz.RPC_INFO_FREE_MODULE
    RPC_INFO_PROCESS_LOAD = dsz.RPC_INFO_PROCESS_LOAD
else:
    raise RuntimeError('Unsupported framework (%s)' % _fw)