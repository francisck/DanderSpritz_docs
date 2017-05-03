# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DmGz_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'dmgz.cmd.dmgz', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('DmGz', 'dmgz', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    for entry in msg:
        if entry['key'] == MSG_KEY_RESULT_ADAPTERS:
            rtn = _handleAdapters(output, msg)
        elif entry['key'] == MSG_KEY_RESULT_STATUS:
            rtn = _handleStatus(output, msg)
        elif entry['key'] == MSG_KEY_RESULT_VERSION:
            rtn = _handleVersion(output, msg)
        else:
            output.RecordError('Unhandled key (0x%08x)' % entry['key'])
            rtn = mcl.target.CALL_FAILED

    output.EndWithStatus(rtn)
    return True


def _handleAdapters(output, msg):
    if msg.GetCount() == 0:
        output.RecordError('No status values returned')
        return mcl.target.CALL_FAILED
    submsg = msg.FindMessage(MSG_KEY_RESULT_ADAPTERS)
    results = ResultFilterInfo()
    results.Demarshal(submsg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('AdaptersInfo')
    if results.threadRunning:
        xml.AddAttribute('threadRunning', 'true')
    else:
        xml.AddAttribute('threadRunning', 'false')
    if results.filterActive:
        xml.AddAttribute('filterActive', 'true')
    else:
        xml.AddAttribute('filterActive', 'false')
    xml.AddAttribute('numAdapters', '%u' % submsg.GetCount(MSG_KEY_RESULT_ADAPTER_NAME))
    while submsg.GetNumRetrieved() < submsg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        name = submsg.FindString(MSG_KEY_RESULT_ADAPTER_NAME)
        xml.AddSubElementWithText('Adapter', name)

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleStatus(output, msg):
    if msg.GetCount() == 0:
        output.RecordError('No status values returned')
        return mcl.target.CALL_FAILED
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('StatusInfo')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        status = ResultStatus()
        status.Demarshal(msg)
        sub = xml.AddSubElement('Status')
        sub.AddAttribute('index', '%u' % status.index)
        sub.AddSubElementWithText('BoundProcess', '%u' % status.boundProcess)
        sub.AddTimeElement('LastTriggerTime', status.lastTriggerTime)
        sub.AddSubElementWithText('Mailslot', status.commsPath)
        sub2 = sub.AddSubElement('LastTriggerStatus')
        sub2.AddAttribute('value', '%u' % status.lastTriggerStatus)
        statusStr = 'UNKNOWN'
        if status.lastTriggerStatus == RESULT_STATUS_TRIGGER_NONE:
            statusStr = 'NONE'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_ACCEPTED:
            statusStr = 'ACCEPTED'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_DECRYPT_FAILED:
            statusStr = 'DECRYPT_FAILED'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_BAD_SIZE:
            statusStr = 'BAD_SIZE'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_BAD_ID:
            statusStr = 'BAD_ID'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_BAD_TIMESTAMP:
            statusStr = 'BAD_TIMESTAMP'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_BAD_DST_ADDRESS:
            statusStr = 'BAD_DST_ADDRESS'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_DELIVERY_FAILED:
            statusStr = 'DELIVERY_FAILED'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_UNSUPPORTED_TYPE:
            statusStr = 'UNSUPPORTED_TYPE'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_INVALID_AUTH:
            statusStr = 'INVALID_AUTH'
        elif status.lastTriggerStatus == RESULT_STATUS_TRIGGER_OTHER_FAILURE:
            statusStr = 'OTHER_FAILURE'
        else:
            statusStr = 'OTHER_FAILURE'
        sub2.SetText(statusStr)

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleVersion(output, msg):
    version = ResultVersion()
    version.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Version')
    xml.AddSubElementWithText('Major', '%u' % version.major)
    xml.AddSubElementWithText('Minor', '%u' % version.minor)
    xml.AddSubElementWithText('Fix', '%u' % version.fix)
    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)