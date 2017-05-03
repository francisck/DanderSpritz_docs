# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: tasking_ur.py
import mcl.framework
import mcl.tasking

class ur:
    LP_MODULE_ID = 34825
    TARGET_MODULE_ID = 34824
    LP_RPC_INFO_LIST_DRIVERS = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 1}
    LP_RPC_INFO_LIST_DATASOURCES = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 2}
    LP_RPC_INFO_CONNECT = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 3}
    LP_RPC_INFO_LIST_SERVERS = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 4}
    LP_RPC_INFO_LIST_DATABASES = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 5}
    LP_RPC_INFO_LIST_TABLES = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 6}
    LP_RPC_INFO_LIST_COLUMNS = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 7}
    LP_RPC_INFO_EXEC = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 8}
    LP_RPC_INFO_LIST_HANDLES = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 9}
    LP_RPC_INFO_DISCONNECT = {'buildType': 'Lp','moduleId': LP_MODULE_ID,'ppcId': 10}
    TARGET_RPC_INFO_LIST_DRIVERS = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 1}
    TARGET_RPC_INFO_LIST_DATASOURCES = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 2}
    TARGET_RPC_INFO_CONNECT = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 3}
    TARGET_RPC_INFO_LIST_SERVERS = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 4}
    TARGET_RPC_INFO_LIST_DATABASES = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 5}
    TARGET_RPC_INFO_LIST_TABLES = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 6}
    TARGET_RPC_INFO_LIST_COLUMNS = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 7}
    TARGET_RPC_INFO_EXEC = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 8}
    TARGET_RPC_INFO_LIST_HANDLES = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 9}
    TARGET_RPC_INFO_DISCONNECT = {'buildType': 'Target','moduleId': TARGET_MODULE_ID,'ppcId': 10}
    RPC_INFO_DISCONNECT = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_DISCONNECT, LP_RPC_INFO_DISCONNECT])
    RPC_INFO_EXEC = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_EXEC, LP_RPC_INFO_EXEC])
    RPC_INFO_LIST_COLUMNS = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_COLUMNS, LP_RPC_INFO_LIST_COLUMNS])
    RPC_INFO_LIST_DATASOURCES = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_DATASOURCES, LP_RPC_INFO_LIST_DATASOURCES])
    RPC_INFO_LIST_SERVERS = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_SERVERS, LP_RPC_INFO_LIST_SERVERS])
    RPC_INFO_LIST_DRIVERS = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_DRIVERS, LP_RPC_INFO_LIST_DRIVERS])
    RPC_INFO_LIST_DATABASES = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_DATABASES, LP_RPC_INFO_LIST_DATABASES])
    RPC_INFO_LIST_TABLES = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_TABLES, LP_RPC_INFO_LIST_TABLES])
    RPC_INFO_LIST_HANDLES = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_LIST_HANDLES, LP_RPC_INFO_LIST_HANDLES])
    RPC_INFO_CONNECT = mcl.tasking.RpcInfo(mcl.framework.UR, [TARGET_RPC_INFO_CONNECT, LP_RPC_INFO_CONNECT])