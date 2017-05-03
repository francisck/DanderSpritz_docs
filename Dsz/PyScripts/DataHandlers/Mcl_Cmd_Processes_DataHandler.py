# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Processes_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.process.cmd.processes', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Processes', 'processes', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        from mcl.object.XmlOutput import XmlOutput
        xml = None
        lastState = None
        sawInitial = False
        sawList = False
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            data = Result()
            data.Demarshal(msg)
            if lastState != data.state:
                if xml != None:
                    output.RecordXml(xml)
                xml = XmlOutput()
                if data.state == RESULT_STATE_INITIAL or data.state == RESULT_STATE_LIST:
                    xml.Start('Initial')
                elif data.state == RESULT_STATE_STARTED:
                    xml.Start('Started')
                elif data.state == RESULT_STATE_STOPPED:
                    xml.Start('Stopped')
                else:
                    output.RecordError('Unhandled process state (%u)' % data.state)
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return True
            _printProcess(data, xml)
            lastState = data.state
            if data.state == RESULT_STATE_INITIAL:
                sawInitial = True
            elif data.state == RESULT_STATE_LIST:
                sawList = True

        output.RecordXml(xml)
        if sawInitial:
            output.GoToBackground()
        if sawList:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True


def _printProcess(data, parent):
    sub = parent.AddSubElement('Process')
    sub.AddSubElementWithText('Name', data.name)
    sub.AddSubElementWithText('ExecutablePath', data.executablePath)
    sub.AddSubElementWithText('Description', data.description)
    if data.flags & RESULT_PROCESS_FLAG_64_BIT:
        sub.AddSubElement('Is64Bit')
    if data.flags & RESULT_PROCESS_FLAG_32_BIT:
        sub.AddSubElement('Is32Bit')
    if data.processId & 2147483648L:
        sub.AddAttribute('id', '0x%08x' % data.processId)
        sub.AddAttribute('parent', '0x%08x' % data.parentProcessId)
    else:
        sub.AddAttribute('id', '%u' % data.processId)
        sub.AddAttribute('parent', '%u' % data.parentProcessId)
    sub.AddAttribute('display', data.displayLocation)
    sub.AddAttribute('user', data.user)
    sub.AddTimeElement('CreateTime', data.createTime)
    sub.AddTimeElement('CpuTime', data.processorTime)
    if data.state == RESULT_STATE_INITIAL or data.state == RESULT_STATE_LIST:
        sub.AddAttribute('state', 'initial')
    elif data.state == RESULT_STATE_STARTED:
        sub.AddAttribute('state', 'started')
    elif data.state == RESULT_STATE_STOPPED:
        sub.AddAttribute('state', 'stopped')
    else:
        sub.AddAttribute('state', 'unknown')


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)