# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Services_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.services', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Services', 'services', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Services')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        results = Result()
        results.Demarshal(msg)
        sub = xml.AddSubElement('Service')
        sub.AddAttribute('serviceName', results.name)
        sub.AddAttribute('displayName', results.displayName)
        subsub = sub.AddSubElement('State')
        subsub.AddAttribute('value', '%u' % results.serviceState)
        subsub.SetText(_getServiceState(results.serviceState))
        subsub = sub.AddSubElement('ServiceType')
        subsub.AddAttribute('value', '0x%08x' % results.serviceType)
        if results.serviceType & RESULT_SERVICE_TYPE_OWN_PROCESS:
            subsub.AddSubElement('SERVICE_WIN32_OWN_PROCESS')
        if results.serviceType & RESULT_SERVICE_TYPE_SHARE_PROCESS:
            subsub.AddSubElement('SERVICE_WIN32_SHARE_PROCESS')
        if results.serviceType & RESULT_SERVICE_TYPE_KERNEL_DRIVER:
            subsub.AddSubElement('SERVICE_KERNEL_DRIVER')
        if results.serviceType & RESULT_SERVICE_TYPE_FILE_SYSTEM_DRIVER:
            subsub.AddSubElement('SERVICE_FILE_SYSTEM_DRIVER')
        if results.serviceType & RESULT_SERVICE_TYPE_INTERACTIVE_PROCESS:
            subsub.AddSubElement('SERVICE_INTERACTIVE_PROCESS')
        subsub = sub.AddSubElement('AcceptedCodes')
        subsub.AddAttribute('value', '0x%08x' % results.serviceControls)
        if results.serviceControls & RESULT_CONTROL_ACCEPT_STOP:
            subsub.AddSubElement('SERVICE_ACCEPT_STOP')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_PAUSE_CONTINUE:
            subsub.AddSubElement('SERVICE_ACCEPT_PAUSE_CONTINUE')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_SHUTDOWN:
            subsub.AddSubElement('SERVICE_ACCEPT_SHUTDOWN')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_PARAMCHANGE:
            subsub.AddSubElement('SERVICE_ACCEPT_PARAMCHANGE')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_NETBINDCHANGE:
            subsub.AddSubElement('SERVICE_ACCEPT_NETBINDCHANGE')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_HARDWAREPROFILECHANGE:
            subsub.AddSubElement('SERVICE_ACCEPT_HARDWAREPROFILECHANGE')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_POWEREVENT:
            subsub.AddSubElement('SERVICE_ACCEPT_POWEREVENT')
        if results.serviceControls & RESULT_CONTROL_ACCEPT_SESSIONCHANGE:
            subsub.AddSubElement('SERVICE_ACCEPT_SESSIONCHANGE')

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _getServiceState(state):
    if state == RESULT_SERVICE_STATE_STOPPED:
        return 'STOPPED'
    else:
        if state == RESULT_SERVICE_STATE_START_PENDING:
            return 'START PENDING'
        if state == RESULT_SERVICE_STATE_STOP_PENDING:
            return 'STOP PENDING'
        if state == RESULT_SERVICE_STATE_RUNNING:
            return 'RUNNING'
        if state == RESULT_SERVICE_STATE_CONTINUE_PENDING:
            return 'CONTINUE PENDING'
        if state == RESULT_SERVICE_STATE_PAUSE_PENDING:
            return 'PAUSE PENDING'
        if state == RESULT_SERVICE_STATE_PAUSED:
            return 'PAUSED'
        return 'UNKNOWN'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)