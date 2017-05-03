# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Grep_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.file.cmd.grep', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Grep', 'grep', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        filemsg = msg.FindMessage(MSG_KEY_RESULT_FILE)
        result = ResultFileInfo()
        result.Demarshal(filemsg)
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('File')
        xml.AddAttribute('location', result.file)
        if result.openStatus != 0:
            errStr = output.TranslateOsError(result.openStatus)
            xml.AddAttribute('error', errStr)
        else:
            while filemsg.GetNumRetrieved() < filemsg.GetCount():
                if mcl.CheckForStop():
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                line = ResultLine()
                line.Demarshal(filemsg)
                if len(line.line) > 0:
                    sub = xml.AddSubElement('Line')
                    sub.AddAttribute('position', '%u' % line.position)
                    sub.SetText(line.line)

        output.RecordXml(xml)

    output.End()
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