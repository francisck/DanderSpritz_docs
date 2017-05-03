# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_FlavControl_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'flav.cmd.flavcontrol', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('FlavControl', 'flavcontrol', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    for entry in msg:
        if entry['key'] == MSG_KEY_RESULT_AVAILABLE:
            rtn = _handleAvailable(output, msg)
        elif entry['key'] == MSG_KEY_RESULT_STRING:
            rtn = _handleString(output, msg)
        elif entry['key'] == MSG_KEY_RESULT_STATUS:
            rtn = _handleStatus(output, msg)
        else:
            output.RecordError('Unhandled key (0x%08x)' % entry['key'])
            rtn = mcl.target.CALL_FAILED

    output.EndWithStatus(rtn)
    return True


def _handleAvailable(output, msg):
    results = AvailableResult()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Available')
    if results.available:
        xml.SetText('true')
    else:
        xml.SetText('false')
    output.RecordXml(xml)
    if results.available:
        return mcl.target.CALL_SUCCEEDED
    else:
        return mcl.target.CALL_FAILED


def _handleStatus(output, msg):
    results = StatusResult()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Status')
    xml.AddSubElementWithText('Major', '%u' % results.major)
    xml.AddSubElementWithText('Minor', '%u' % results.minor)
    xml.AddSubElementWithText('Fix', '%u' % results.fix)
    xml.AddSubElementWithText('Build', '%u' % results.build)
    if results.available:
        xml.AddSubElementWithText('Available', 'true')
    else:
        xml.AddSubElementWithText('Available', 'false')
    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleString(output, msg):
    results = StringResult()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('String')
    xml.SetText(results.str)
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