# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_EventLogQuery_DataHandler.py
EVENTLOG_SUCCESS = 0
EVENTLOG_ERROR_TYPE = 1
EVENTLOG_WARNING_TYPE = 2
EVENTLOG_INFORMATION_TYPE = 4
EVENTLOG_AUDIT_SUCCESS = 8
EVENTLOG_AUDIT_FAILURE = 16
FACILITY_NULL = 0
FACILITY_RPC = 1
FACILITY_DISPATCH = 2
FACILITY_STORAGE = 3
FACILITY_ITF = 4
FACILITY_WIN32 = 7
FACILITY_WINDOWS = 8
FACILITY_SECURITY = 9
FACILITY_CONTROL = 10
FACILITY_CERT = 11
FACILITY_INTERNET = 12
FACILITY_MEDIASERVER = 13
FACILITY_MSMQ = 14
FACILITY_SETUPAPI = 15
FACILITY_SCARD = 16
FACILITY_COMPLUS = 17
FACILITY_AAF = 18
FACILITY_URT = 19
FACILITY_ACS = 20

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.eventlogquery', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('EventLogQuery', 'eventlogquery', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    atLeastOneOpened = False
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        logmsg = msg.FindMessage(MSG_KEY_RESULT_LOG)
        opened = ResultLogStatus()
        opened.Demarshal(logmsg)
        if opened.opened:
            atLeastOneOpened = True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        if opened.opened == False:
            errStr = output.TranslateOsError(opened.error)
            xml.Start('ErrLog')
            xml.AddAttribute('osError', errStr)
            xml.AddAttribute('name', opened.logName)
        elif logmsg.PeekByKey(MSG_KEY_RESULT_LOG_INFO):
            eventInfo = ResultLogInfo()
            eventInfo.Demarshal(logmsg)
            xml.Start('EventLog')
            xml.AddAttribute('name', opened.logName)
            xml.AddAttribute('mostRecentRecordNum', '%u' % eventInfo.mostRecentRecNum)
            xml.AddAttribute('numRecords', '%u' % eventInfo.numRecords)
            xml.AddAttribute('oldestRecordNum', '%u' % eventInfo.oldestRecNum)
            xml.AddTimeElement('Time', eventInfo.mostRecentRecTime)
        else:
            xml.Start('Records')
            xml.AddAttribute('name', opened.logName)
            while logmsg.GetNumRetrieved() < logmsg.GetCount():
                if mcl.CheckForStop():
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                recordmsg = logmsg.FindMessage(MSG_KEY_RESULT_RECORD)
                record = ResultRecord()
                record.Demarshal(recordmsg)
                _handleEventRecord(xml, recordmsg, record)

        output.RecordXml(xml)

    if atLeastOneOpened:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    else:
        output.EndWithStatus(mcl.target.CALL_FAILED)
    return True


def _handleEventRecord(xml, msg, record):
    sub = xml.AddSubElement('Record')
    sub.AddAttribute('number', '%u' % record.RecordNumber)
    sub.AddAttribute('eventType', _getEventType(record.EventType))
    _parseEventId(sub, record.EventID)
    sub.AddAttribute('source', record.SourceName)
    sub.AddAttribute('computer', record.ComputerName)
    sub.AddAttribute('processId', '%u' % record.ProcessId)
    sub.AddAttribute('threadId', '%u' % record.ThreadId)
    sub.AddAttribute('sid', record.UserSid)
    sub.AddTimeElement('TimeGenerated', record.TimeGenerated)
    sub.AddTimeElement('TimeWritten', record.TimeWritten)
    while msg.PeekByKey(MSG_KEY_RESULT_STRING):
        str = msg.FindString(MSG_KEY_RESULT_STRING)
        sub.AddSubElementWithText('String', str)

    while msg.PeekByKey(MSG_KEY_RESULT_DATA):
        buffer = msg.FindData(MSG_KEY_RESULT_DATA)
        subsub = sub.AddSubElement('Data')
        subsub.SetTextAsData(buffer)


def _getEventType(type):
    if type == EVENTLOG_SUCCESS:
        return 'None'
    else:
        if type == EVENTLOG_ERROR_TYPE:
            return 'Error'
        if type == EVENTLOG_WARNING_TYPE:
            return 'Warning'
        if type == EVENTLOG_INFORMATION_TYPE:
            return 'Information'
        if type == EVENTLOG_AUDIT_SUCCESS:
            return 'Success Audit'
        if type == EVENTLOG_AUDIT_FAILURE:
            return 'Failure Audit'
        return 'N/A'


def _parseEventId(xml, eventId):
    xml.AddAttribute('eventId', '0x%08x' % eventId)
    xml.AddAttribute('code', '%u' % (eventId & 65535))
    severity = eventId & 3221225472L
    severityStr = 'Unknown'
    if severity == 0:
        severityStr = 'Success'
    elif severity == 1073741824:
        severityStr = 'Informational'
    elif severity == 2147483648L:
        severityStr = 'Warning'
    elif severity == 3221225472L:
        severityStr = 'Error'
    xml.AddAttribute('severity', severityStr)
    if eventId & 536870912:
        xml.AddAttribute('type', 'customer')
    else:
        xml.AddAttribute('type', 'system')
    facility = eventId >> 16 & 4095
    facilityStr = 'FACILITY_NULL'
    if facility == FACILITY_ACS:
        facilityStr = 'FACILITY_ACS'
    elif facility == FACILITY_AAF:
        facilityStr = 'FACILITY_AAF'
    elif facility == FACILITY_CERT:
        facilityStr = 'FACILITY_CERT'
    elif facility == FACILITY_COMPLUS:
        facilityStr = 'FACILITY_COMPLUS'
    elif facility == FACILITY_CONTROL:
        facilityStr = 'FACILITY_CONTROL'
    elif facility == FACILITY_DISPATCH:
        facilityStr = 'FACILITY_DISPATCH'
    elif facility == FACILITY_INTERNET:
        facilityStr = 'FACILITY_INTERNET'
    elif facility == FACILITY_ITF:
        facilityStr = 'FACILITY_ITF'
    elif facility == FACILITY_MEDIASERVER:
        facilityStr = 'FACILITY_MEDIASERVER'
    elif facility == FACILITY_MSMQ:
        facilityStr = 'FACILITY_MSMQ'
    elif facility == FACILITY_RPC:
        facilityStr = 'FACILITY_RPC'
    elif facility == FACILITY_SCARD:
        facilityStr = 'FACILITY_SCARD'
    elif facility == FACILITY_SECURITY:
        facilityStr = 'FACILITY_SECURITY'
    elif facility == FACILITY_SETUPAPI:
        facilityStr = 'FACILITY_SETUPAPI'
    elif facility == FACILITY_STORAGE:
        facilityStr = 'FACILITY_STORAGE'
    elif facility == FACILITY_URT:
        facilityStr = 'FACILITY_URT'
    elif facility == FACILITY_WIN32:
        facilityStr = 'FACILITY_WIN32'
    elif facility == FACILITY_WINDOWS:
        facilityStr = 'FACILITY_WINDOWS'
    xml.AddAttribute('facility', facilityStr)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)