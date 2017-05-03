# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking_dsz.py
import mcl.framework
import mcl.tasking

class dsz:
    INTERFACE = 16842801
    PFAM = 4125
    PROVIDER_ANY = 4125
    PROVIDER = 16846877
    RPC_INFO_LIST = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 0])
    RPC_INFO_LOAD = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 1])
    RPC_INFO_UNLOAD = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 2])