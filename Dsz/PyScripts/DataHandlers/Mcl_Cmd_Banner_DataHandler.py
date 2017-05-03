# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Banner_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.banner', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Banner', 'banner', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        if moduleError == ERR_RECV_TIMEOUT:
            output.SetTaskStatus(mcl.target.CALL_SUCCEEDED)
        else:
            output.SetTaskStatus(input.GetStatus())
        output.End()
        return True
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    result = Result()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    if result.socketType == SOCKET_TYPE_TCP:
        xml.Start('Connected')
        output.RecordXml(xml)
    xml.Start('Transfer')
    xml.AddAttribute('address', '%s' % result.rspAddr)
    xml.AddAttribute('port', '%u' % result.port)
    sub = xml.AddSubElement('Data')
    sub.AddAttribute('size', '%u' % len(result.response))
    if len(result.response) > 0:
        sub.SetTextAsData(result.response)
    textStr = ''
    for char in result.response:
        if char == ord('\r') or char == ord('\n') or char == ord('\t') or char >= ord(' ') and char <= ord('~'):
            textStr = textStr + chr(char)
        else:
            textStr = textStr + '?'

    sub = xml.AddSubElementWithText('Text', textStr)
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