# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking_dsz.py
import mcl.framework
import mcl.tasking

class dsz:
    INTERFACE = 16842801
    PFAM = 4196
    PROVIDER_ANY = 4196
    PROVIDER = 16846948
    RPC_INFO_LIST_DRIVERS = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 0])
    RPC_INFO_LIST_DATASOURCES = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 1])
    RPC_INFO_CONNECT = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 2])
    RPC_INFO_LIST_SERVERS = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 3])
    RPC_INFO_LIST_DATABASES = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 4])
    RPC_INFO_LIST_TABLES = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 5])
    RPC_INFO_LIST_COLUMNS = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 6])
    RPC_INFO_EXEC = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 7])
    RPC_INFO_LIST_HANDLES = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 8])
    RPC_INFO_DISCONNECT = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 9])