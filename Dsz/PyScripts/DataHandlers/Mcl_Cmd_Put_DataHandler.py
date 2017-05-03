# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Put_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.data.env
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.file.cmd.put', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Put', 'put', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        mcl.data.env.SetValue(LP_ENV_PUT_COMPLETE, 'true')
        return True
    results = Result()
    try:
        results.Demarshal(msg)
    except:
        output.RecordError('Failed to get callback parameters')
        mcl.data.env.SetValue(LP_ENV_ERROR_ENCOUNTERED, 'true')
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True

    if len(results.filePath) > 0:
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Results')
        xml.AddSubElementWithText('File', results.filePath)
        output.RecordXml(xml)
        mcl.data.env.SetValue(LP_ENV_FILE_OPENED, 'true')
    bytesLeft = int(mcl.data.env.GetValue(LP_ENV_BYTES_LEFT))
    totalBytes = int(mcl.data.env.GetValue(LP_ENV_FILE_SIZE))
    if results.bytesWritten > bytesLeft:
        output.RecordError('Target reported more data written than is left?!')
        mcl.data.env.SetValue(LP_ENV_ERROR_ENCOUNTERED, 'true')
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True
    if results.bytesWritten > 0:
        bytesLeft -= results.bytesWritten
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Results')
        xml.AddAttribute('bytesWritten', '%u' % results.bytesWritten)
        xml.AddAttribute('bytesLeft', '%u' % bytesLeft)
        xml.AddAttribute('totalBytes', '%u' % totalBytes)
        output.RecordXml(xml)
        mcl.data.env.SetValue(LP_ENV_BYTES_LEFT, '%u' % bytesLeft)
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