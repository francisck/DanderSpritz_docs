# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Ping_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.ping', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Ping', 'ping', [])
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
    xml.Start('PingResponse')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        results = Result()
        results.Demarshal(msg)
        sub = xml.AddSubElement('Response')
        sub.AddTimeElement('Elapsed', results.time)
        sub.AddAttribute('length', '%u' % len(results.rawData))
        if results.ttl != 0:
            sub.AddAttribute('ttl', '%u' % results.ttl)
        dataSub = sub.AddSubElement('Data')
        dataSub.SetTextAsData(results.rawData)
        sub.AddAddressIP('FromAddr', results.fromAddr)
        sub.AddAddressIP('ToAddr', results.toAddr)
        if results.type == REPLY_TYPE_REPLY:
            sub.AddAttribute('type', 'REPLY')
        elif results.type == REPLY_TYPE_DEST_UNREACH:
            sub.AddAttribute('type', 'DESTINATION_UNREACHABLE')
        else:
            sub.AddAttribute('type', 'UNKNOWN')

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