# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Environment_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.environment', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.environment.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.process.cmd.environment.Params()
    tgtParams.action = lpParams['action']
    if lpParams['envVar'] != None:
        tgtParams.variable = lpParams['envVar']
    if lpParams['setValue'] != None:
        tgtParams.value = lpParams['setValue']
    if tgtParams.action != mca.process.cmd.environment.ACTION_GET and len(tgtParams.variable) == 0:
        mcl.tasking.OutputError('No environment variable specified for set or delete')
        return False
    else:
        rpc = mca.process.cmd.environment.tasking.RPC_INFO_ACTION
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchMask(tgtParams.variable)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.environment.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)