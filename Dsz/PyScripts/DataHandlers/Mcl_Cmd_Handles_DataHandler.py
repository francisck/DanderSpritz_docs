# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Handles_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    import mcl.tasking.env
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.status.cmd.handles', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Handles', 'handles', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        rtn = mcl.target.CALL_SUCCEEDED
        if msg[0]['key'] == MSG_KEY_RESULT_HANDLE:
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('Handles')
            sub = None
            lastId = 0
            for entry in msg:
                if mcl.CheckForStop():
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                results = ResultHandle()
                results.Demarshal(msg)
                if results.processId != lastId:
                    sub = xml.AddSubElement('Process')
                    sub.AddAttribute('id', '%u' % results.processId)
                    lastId = results.processId
                sub2 = sub.AddSubElement('Handle')
                sub2.AddAttribute('handleId', '%u' % results.handle)
                sub2.AddAttribute('type', results.type)
                sub2.AddSubElementWithText('Metadata', results.metadata)

            output.RecordXml(xml)
        elif msg[0]['key'] == MSG_KEY_RESULT_CLOSE:
            results = ResultClose()
            results.Demarshal(msg)
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('ClosedHandle')
            xml.AddAttribute('handleId', '%u' % results.handleValue)
            xml.AddAttribute('processId', '%s' % results.processId)
            output.RecordXml(xml)
        elif msg[0]['key'] == MSG_KEY_RESULT_DUPLICATE:
            results = ResultDuplicate()
            results.Demarshal(msg)
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('DuplicatedHandle')
            xml.AddAttribute('origProcessId', '%s' % results.origProcessId)
            xml.AddAttribute('origHandleId', '%u' % results.origHandle)
            xml.AddAttribute('newProcessId', '%s' % results.newProcessId)
            xml.AddAttribute('newHandleId', '%u' % results.newHandle)
            output.RecordXml(xml)
        else:
            output.RecordError('Unhandled data key (0x%08x)' % entry['key'])
            rtn = mcl.target.CALL_FAILED
        output.EndWithStatus(rtn)
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