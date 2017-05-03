# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Shares_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.shares', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Shares', 'shares', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.SHARES_QUERY:
            return _handleQueryData(msg, output)
        if input.GetMessageType() == mcl.msgtype.SHARES_MAP:
            return _handleMapData(msg, output)
        if input.GetMessageType() == mcl.msgtype.SHARES_LIST:
            return _handleListData(msg, output)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleListData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Shares')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        data = ResultList()
        data.Demarshal(msg)
        sub = xml.AddSubElement('Share')
        sub.AddSubElementWithText('LocalName', data.local)
        sub.AddSubElementWithText('RemoteName', data.remote)
        sub.AddSubElementWithText('UserName', data.username)
        sub.AddSubElementWithText('DomainName', data.domainName)
        sub.AddSubElementWithText('Password', data.password)
        sub.AddAttribute('referenceCount', '%u' % data.referenceCount)
        sub.AddAttribute('useCount', '%u' % data.useCount)
        if data.status == RESULT_LIST_STATUS_OK:
            sub.AddSubElementWithText('Status', 'Ok')
        elif data.status == RESULT_LIST_STATUS_PAUSED:
            sub.AddSubElementWithText('Status', 'Paused')
        elif data.status == RESULT_LIST_STATUS_DISCONNECTED:
            sub.AddSubElementWithText('Status', 'Disconnected')
        elif data.status == RESULT_LIST_STATUS_NETWORK_ERROR:
            sub.AddSubElementWithText('Status', 'NetworkError')
        elif data.status == RESULT_LIST_STATUS_CONNECTING:
            sub.AddSubElementWithText('Status', 'Connecting')
        elif data.status == RESULT_LIST_STATUS_RECONNECTING:
            sub.AddSubElementWithText('Status', 'Reconnecting')
        else:
            sub.AddSubElementWithText('Status', 'Unknown')
        if data.type == RESULT_LIST_TYPE_WILDCARD:
            sub.AddSubElementWithText('Type', 'Wildcard')
        elif data.type == RESULT_LIST_TYPE_DISK_DEVICE:
            sub.AddSubElementWithText('Type', 'Disk Device')
        elif data.type == RESULT_LIST_TYPE_SPOOL_DEVICE:
            sub.AddSubElementWithText('Type', 'Spool Device')
        elif data.type == RESULT_LIST_TYPE_IPC:
            sub.AddSubElementWithText('Type', 'Interprocess Communication')
        else:
            sub.AddSubElementWithText('Type', 'Unknown')

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleMapData(msg, output):
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    results = ResultMap()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('MapResponse')
    if len(results.resourceName) > 0:
        xml.AddSubElementWithText('ResourceName', results.resourceName)
    xml.AddSubElementWithText('ResourcePath', results.resourcePath)
    output.RecordXml(xml)
    output.GoToBackground()
    output.End()
    return True


def _handleQueryData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('QueryResponse')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        data = ResultQuery()
        data.Demarshal(msg)
        sub = xml.AddSubElement('Resource')
        sub.AddSubElementWithText('Name', data.name)
        if data.hasPath:
            sub.AddSubElementWithText('Path', data.path)
        type = sub.AddSubElement('Type')
        if data.admin:
            type.AddAttribute('admin', 'true')
        else:
            type.AddAttribute('admin', 'false')
        if data.type == RESULT_QUERY_TYPE_DISK:
            type.SetText('Disk')
        elif data.type == RESULT_QUERY_TYPE_DEVICE:
            type.SetText('Device')
        elif data.type == RESULT_QUERY_TYPE_PRINT:
            type.SetText('Print')
        elif data.type == RESULT_QUERY_TYPE_IPC:
            type.SetText('IPC')
        else:
            type.SetText('Unknown')
        sub.AddSubElementWithText('Caption', data.caption)
        sub.AddSubElementWithText('Description', data.description)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
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