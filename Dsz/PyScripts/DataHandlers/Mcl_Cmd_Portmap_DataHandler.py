# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Portmap_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.portmap', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Portmap', 'portmap', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_JUMPUP_FAILED:
            output.RecordModuleError(moduleError, osError, errorStrings, False)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Ports')
        hitMax = False
        lastId = 0
        sub = None
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            result = Result()
            result.Demarshal(msg)
            if result.hitMax:
                hitMax = True
            if result.processId != lastId:
                sub = xml.AddSubElement('Process')
                sub.AddAttribute('id', '%u' % result.processId)
                sub.AddAttribute('name', result.procName)
                lastId = result.processId
            sub2 = sub.AddSubElement('Port')
            state = '??????'
            if result.state == RESULT_PORT_STATE_OPEN:
                state = 'Open'
            elif result.state == RESULT_PORT_STATE_BOUND:
                state = 'Bound'
            elif result.state == RESULT_PORT_STATE_LISTENING:
                state = 'Listening'
            elif result.state == RESULT_PORT_STATE_CONNECTED:
                state = 'Connected'
            elif result.state == RESULT_PORT_STATE_CLEANUP:
                state = 'Cleanup'
            elif result.state == RESULT_PORT_STATE_CLOSING:
                state = 'Closing'
            elif result.state == RESULT_PORT_STATE_TRANSMIT_CLOSING:
                state = 'Closing'
            elif result.state == RESULT_PORT_STATE_INVALID:
                state = 'Invalid'
            elif result.state == RESULT_PORT_STATE_UNKNOWN:
                state = 'Unknown'
            type = 'UNK'
            if result.type == RESULT_PORT_TYPE_UDP:
                type = 'UDP'
            elif result.type == RESULT_PORT_TYPE_TCP:
                type = 'TCP'
            elif result.type == RESULT_PORT_TYPE_RAW:
                type = 'RAW'
            elif result.type == RESULT_PORT_TYPE_UNKNOWN:
                type = 'UNK'
            sub2.AddAttribute('state', state)
            sub2.AddAttribute('type', type)
            sub2.AddAttribute('sourcePort', '%u' % result.srcPort)
            sub2.AddAttribute('sourceAddr', result.srcAddr)

        output.RecordXml(xml)
        if hitMax:
            output.RecordError('Query of ports terminated (maximum reached)')
            output.EndWithStatus(mcl.target.CALL_FAILED)
        else:
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