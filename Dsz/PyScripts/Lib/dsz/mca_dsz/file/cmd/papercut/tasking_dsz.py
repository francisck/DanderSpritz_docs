# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking_dsz.py
import mcl.framework
import mcl.tasking

class dsz:
    INTERFACE = 16842801
    PFAM = 4202
    PROVIDER_ANY = 4202
    PROVIDER = 16846954
    RPC_INFO_GET = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 0])
    RPC_INFO_LOCK = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 1])
    RPC_INFO_TRIM = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 2])
    RPC_INFO_MAPPED = mcl.tasking.RpcInfo(mcl.framework.DSZ, [INTERFACE, PROVIDER_ANY, 3])