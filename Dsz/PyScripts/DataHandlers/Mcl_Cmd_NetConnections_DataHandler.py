# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_NetConnections_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    from mcl.object.IpAddr import IpAddr
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.netconnections', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Netconnections', 'netconnections', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.GetCount() == 0:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Connections')
        sub = None
        firstLoop = True
        lastType = 0
        infoType = 0
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            submsg = msg.FindMessage(MSG_KEY_RESULT)
            resultType = Result()
            resultType.Demarshal(submsg)
            if firstLoop or resultType.dataType != lastType:
                if resultType.dataType == RESULT_DATA_TYPE_INITIAL:
                    sub = xml.AddSubElement('Initial')
                elif resultType.dataType == RESULT_DATA_TYPE_LIST:
                    sub = xml.AddSubElement('Initial')
                elif resultType.dataType == RESULT_DATA_TYPE_ADDED:
                    sub = xml.AddSubElement('Started')
                elif resultType.dataType == RESULT_DATA_TYPE_REMOVED:
                    sub = xml.AddSubElement('Stopped')
                else:
                    sub = xml.AddSubElement('Unknown')
                lastType = resultType.dataType
                firstLoop = False
            for entry in submsg:
                if entry['retrieved']:
                    continue
                if entry['key'] == MSG_KEY_RESULT_IP:
                    connection = ResultIp()
                    connection.Demarshal(submsg)
                    _handleIpResult(sub, connection)
                elif entry['key'] == MSG_KEY_RESULT_NAMEDPIPE:
                    connection = ResultNamedPipe()
                    connection.Demarshal(submsg)
                    _handleNamedPipeResult(sub, connection)
                elif entry['key'] == MSG_KEY_RESULT_MAILSLOT:
                    connection = ResultMailSlot()
                    connection.Demarshal(submsg)
                    _handleMailSlotResult(sub, connection)
                else:
                    output.RecordError('Returned result key (0x%08x) is invalid' % entry['key'])
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False

        output.RecordXml(xml)
        if resultType.dataType == RESULT_DATA_TYPE_INITIAL:
            output.GoToBackground()
        output.End()
        return True


def _handleIpResult(xml, connection):
    sub = xml.AddSubElement('Connection')
    if connection.protocol == RESULT_IP_PROTOCOL_TCP:
        sub.AddAttribute('type', 'TCP')
    elif connection.protocol == RESULT_IP_PROTOCOL_UDP:
        sub.AddAttribute('type', 'UDP')
    elif connection.protocol == RESULT_IP_PROTOCOL_RAW:
        sub.AddAttribute('type', 'RAW')
    if connection.valid:
        sub.AddAttribute('valid', 'true')
    else:
        sub.AddAttribute('valid', 'false')
    sub.AddAddressIP('LocalAddress', connection.localIp)
    sub.AddSubElementWithText('LocalPort', '%u' % connection.localPort)
    if connection.protocol == RESULT_IP_PROTOCOL_TCP:
        if connection.hasRemoteIp:
            sub.AddAddressIP('RemoteAddress', connection.remoteIp)
            sub.AddSubElementWithText('RemotePort', '%u' % connection.remotePort)
        if connection.state == RESULT_IP_STATE_ESTABLISHED:
            sub.AddAttribute('state', 'ESTABLISHED')
        elif connection.state == RESULT_IP_STATE_SYN_SENT:
            sub.AddAttribute('state', 'SYN_SENT')
        elif connection.state == RESULT_IP_STATE_SYN_RECV:
            sub.AddAttribute('state', 'SYN_RECEIVED')
        elif connection.state == RESULT_IP_STATE_FIN_WAIT_1:
            sub.AddAttribute('state', 'FIN_WAIT')
        elif connection.state == RESULT_IP_STATE_FIN_WAIT_2:
            sub.AddAttribute('state', 'FIN_WAIT2')
        elif connection.state == RESULT_IP_STATE_TIME_WAIT:
            sub.AddAttribute('state', 'TIME_WAIT')
        elif connection.state == RESULT_IP_STATE_CLOSED:
            sub.AddAttribute('state', 'CLOSED')
        elif connection.state == RESULT_IP_STATE_CLOSE_WAIT:
            sub.AddAttribute('state', 'CLOSE_WAIT')
        elif connection.state == RESULT_IP_STATE_LAST_ACK:
            sub.AddAttribute('state', 'LAST_ACK')
        elif connection.state == RESULT_IP_STATE_LISTEN:
            sub.AddAttribute('state', 'LISTENING')
        elif connection.state == RESULT_IP_STATE_CLOSING:
            sub.AddAttribute('state', 'CLOSING')
        elif connection.state == RESULT_IP_STATE_UNKNOWN:
            sub.AddAttribute('state', 'UNKNOWN')
    sub.AddSubElementWithText('Pid', '%u' % connection.pid)


def _handleMailSlotResult(xml, connection):
    sub = xml.AddSubElement('MailSlot')
    sub.AddSubElementWithText('Name', connection.name)


def _handleNamedPipeResult(xml, connection):
    sub = xml.AddSubElement('NamedPipe')
    sub.AddSubElementWithText('Name', connection.name)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)