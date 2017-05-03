# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Ldap_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.ldap', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.ldap.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.ldap.Params()
    tgtParams.port = lpParams['port']
    tgtParams.scope = lpParams['scope']
    tgtParams.chunkSize = lpParams['chunksize']
    if lpParams['hostName'] != None:
        tgtParams.hostName = lpParams['hostName']
    if lpParams['filter'] != None:
        tgtParams.filter = lpParams['filter']
    if lpParams['attrs'] != None:
        attrs = lpParams['attrs']
        numAttrs = 0
        while len(attrs) > 0:
            if numAttrs >= mca.survey.cmd.ldap.PARAMS_MAX_SEARCH_ATTRIBUTES:
                mcl.tasking.OutputError('Exceeded maximum attributes (%u)' % mca.survey.cmd.ldap.PARAMS_MAX_SEARCH_ATTRIBUTES)
                return False
            pos = attrs.find(',')
            if pos == -1:
                tgtParams.attributes[numAttrs] = attrs
                attrs = ''
            else:
                tgtParams.attributes[numAttrs] = attrs[0:pos]
                attrs = attrs[pos + 1:]
            if len(tgtParams.attributes[numAttrs]) > 0:
                numAttrs = numAttrs + 1

    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.hostName) > 0:
        taskXml.SetTargetRemote(tgtParams.hostName)
    if len(tgtParams.filter) > 0:
        taskXml.AddSearchMask(tgtParams.filter)
    if lpParams['attrs'] != None and len(lpParams['attrs']) > 0:
        taskXml.AddSearchParam(lpParams['attrs'])
    else:
        taskXml.AddSearchParam('all attributes')
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.survey.cmd.ldap.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.ldap.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)