# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Performance_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.performance', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.performance.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.status.cmd.performance.Params()
    tgtParams.initBuffer = lpParams['initbuffer']
    tgtParams.bare = lpParams['bare']
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['dataset'] != None:
        tgtParams.dataSet = lpParams['dataset']
    tgtParams.objectNumber = lpParams['objectNumber']
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    taskXml.AddSearchPath(tgtParams.dataSet)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.status.cmd.performance.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.performance.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)