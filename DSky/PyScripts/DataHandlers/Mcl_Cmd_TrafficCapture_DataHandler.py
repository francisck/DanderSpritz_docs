# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_TrafficCapture_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.dsky.cmd.trafficcapture', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('TrafficCapture', 'trafficcapture', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        entry = msg.PeekByKey(mcl.object.Message.MSG_TYPE_INVALID)
        if entry['key'] == MSG_KEY_RESULT_GET_FILTER:
            return _handleGetFilter(output, msg)
        if entry['key'] == MSG_KEY_RESULT_GET_STATUS:
            return _handleGetStatus(output, msg)
        if entry['key'] == MSG_KEY_RESULT_SEND_CONTROL:
            return _handleSendControl(output, msg)
        if entry['key'] == MSG_KEY_RESULT_VALIDATE_FILTER:
            return _handleValidateFilter(output, msg)
        output.RecordError('Returned key (0x%08x) is invalid' % entry['key'])
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True


def _handleGetFilter(output, msg):
    results = ResultGetFilter()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Filter')
    _printFilter(results.adapterFilter, results.filter, xml)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleGetStatus(output, msg):
    results = ResultGetStatus()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Status')
    if results.filterActive:
        xml.AddAttribute('filterActive', 'true')
    else:
        xml.AddAttribute('filterActive', 'false')
    if results.packetThreadRunning:
        xml.AddAttribute('threadRunning', 'true')
    else:
        xml.AddAttribute('threadRunning', 'false')
    xml.AddAttribute('maxCaptureSize', '%u' % results.maxCaptureFileSize)
    xml.AddAttribute('captureFile', results.captureFile)
    xml.AddAttribute('captureFileSize', '%u' % results.captureFileSize)
    xml.AddAttribute('maxPacketSize', '%u' % results.maxPacketSize)
    if len(results.key) > 0:
        sub = xml.AddSubElement('EncryptionKey')
        sub.SetTextAsData(results.key)
    sub = xml.AddSubElement('Version')
    sub.AddAttribute('major', '%u' % results.majorVersion)
    sub.AddAttribute('minor', '%u' % results.minorVersion)
    sub.AddAttribute('revision', '%u' % results.revision)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleSendControl(output, msg):
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _handleValidateFilter(output, msg):
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _printFilter(adapterFilter, filter, xml):
    BPF_LD = 0
    BPF_LDX = 1
    BPF_ST = 2
    BPF_STX = 3
    BPF_ALU = 4
    BPF_JMP = 5
    BPF_RET = 6
    BPF_MISC = 7
    BPF_W = 0
    BPF_H = 8
    BPF_B = 16
    BPF_IMM = 0
    BPF_ABS = 32
    BPF_IND = 64
    BPF_MEM = 96
    BPF_LEN = 128
    BPF_MSH = 160
    BPF_ADD = 0
    BPF_SUB = 16
    BPF_MUL = 32
    BPF_DIV = 48
    BPF_OR = 64
    BPF_AND = 80
    BPF_LSH = 96
    BPF_RSH = 112
    BPF_NEG = 128
    BPF_JA = 0
    BPF_JEQ = 16
    BPF_JGT = 32
    BPF_JGE = 48
    BPF_JSET = 64
    BPF_K = 0
    BPF_X = 8
    BPF_A = 16
    BPF_TAX = 0
    BPF_TXA = 128
    sub = xml.AddSubElement('AdapterFilter')
    sub.AddAttribute('value', '0x%x' % adapterFilter)
    if adapterFilter & ADAPTER_FILTER_TYPE_DIRECTED:
        sub.AddSubElement('NdisPacketTypeDirected')
    if adapterFilter & ADAPTER_FILTER_TYPE_MULTICAST:
        sub.AddSubElement('NdisPacketTypeMulticast')
    if adapterFilter & ADAPTER_FILTER_TYPE_ALL_MULTICAST:
        sub.AddSubElement('NdisPacketTypeAllMulticast')
    if adapterFilter & ADAPTER_FILTER_TYPE_BROADCAST:
        sub.AddSubElement('NdisPacketTypeBroadcast')
    if adapterFilter & ADAPTER_FILTER_TYPE_SOURCE_ROUTING:
        sub.AddSubElement('NdisPacketTypeSourceRouting')
    if adapterFilter & ADAPTER_FILTER_TYPE_PROMISCUOUS:
        sub.AddSubElement('NdisPacketTypePromiscuous')
    if adapterFilter & ADAPTER_FILTER_TYPE_SMT:
        sub.AddSubElement('NdisPacketTypeSmt')
    if adapterFilter & ADAPTER_FILTER_TYPE_ALL_LOCAL:
        sub.AddSubElement('NdisPacketTypeAllLocal')
    if adapterFilter & ADAPTER_FILTER_TYPE_MAC_FRAME:
        sub.AddSubElement('NdisPacketTypeMacFrame')
    if adapterFilter & ADAPTER_FILTER_TYPE_FUNCTIONAL:
        sub.AddSubElement('NdisPacketTypeFunctional')
    if adapterFilter & ADAPTER_FILTER_TYPE_ALL_FUNCTIONAL:
        sub.AddSubElement('NdisPacketTypeAllFunctional')
    if adapterFilter & ADAPTER_FILTER_TYPE_GROUP:
        sub.AddSubElement('NdisPacketTypeGroup')
    sub = xml.AddSubElement('BpfFilter')
    sub.AddAttribute('length', '%u' % len(filter))
    sub.SetTextAsData(filter)
    line = 1
    import mcl.object.Demarshaler
    demarsh = mcl.object.Demarshaler.Demarshaler(filter)
    sub = xml.AddSubElement('BpfFilterInstructions')
    while demarsh.BytesLeft() > 0:
        code = demarsh.GetU16(demarsh.LITTLE_ENDIAN)
        jt = demarsh.GetU8()
        jf = demarsh.GetU8()
        k = demarsh.GetS32(demarsh.LITTLE_ENDIAN)
        if k & 32768:
            kShort = (k & 32767) - 32768
        else:
            kShort = k
        lineSub = sub.AddSubElement('Instruction')
        lineSub.SetText('FOO')
        if code == BPF_LD | BPF_W | BPF_LEN:
            lineSub.SetText('LDW A,wirelen')
        elif code == BPF_LD | BPF_W | BPF_ABS:
            lineSub.SetText('LDW A,p[%d]' % kShort)
        elif code == BPF_LD | BPF_H | BPF_ABS:
            lineSub.SetText('LDH A,p[%d]' % kShort)
        elif code == BPF_LD | BPF_B | BPF_ABS:
            lineSub.SetText('LDB A,p[%d]' % kShort)
        elif code == BPF_LD | BPF_W | BPF_IND:
            lineSub.SetText('LDW A,p[X+%d]' % kShort)
        elif code == BPF_LD | BPF_H | BPF_IND:
            lineSub.SetText('LDH A,p[X+%d]' % kShort)
        elif code == BPF_LD | BPF_B | BPF_IND:
            lineSub.SetText('LDB A,p[X+%d]' % kShort)
        elif code == BPF_LD | BPF_IMM:
            lineSub.SetText('LD A,%d' % kShort)
        elif code == BPF_LD | BPF_MEM:
            lineSub.SetText('LD A,M[%d]' % kShort)
        elif code == BPF_LDX | BPF_W | BPF_LEN:
            lineSub.SetText('LDW X,wirelen')
        elif code == BPF_LDX | BPF_MSH | BPF_B:
            lineSub.SetText('LDH X,p[%d]' % kShort)
        elif code == BPF_LDX | BPF_IMM:
            lineSub.SetText('LD X,%d' % kShort)
        elif code == BPF_LDX | BPF_MEM:
            lineSub.SetText('LD X,M[%d]' % kShort)
        elif code == BPF_JMP | BPF_JA:
            lineSub.SetText('JMP %d' % (line + 1 + k))
        elif code == BPF_JMP | BPF_JGT | BPF_K:
            lineSub.SetText('IF(A > %d) JMP %d ELSE JMP %d' % (k, line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JGE | BPF_K:
            lineSub.SetText('IF(A >= %d) JMP %d ELSE JMP %d' % (k, line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JEQ | BPF_K:
            lineSub.SetText('IF(A == %d) JMP %d ELSE JMP %d' % (k, line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JSET | BPF_K:
            lineSub.SetText('IF(A & 0x%x) JMP %d ELSE JMP %d' % (k, line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JGT | BPF_X:
            lineSub.SetText('IF(A > X) JMP %d ELSE JMP %d' % (line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JGE | BPF_X:
            lineSub.SetText('IF(A >= X) JMP %d ELSE JMP %d' % (line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JEQ | BPF_X:
            lineSub.SetText('IF(A == X) JMP %d ELSE JMP %d' % (line + 1 + jt, line + 1 + jf))
        elif code == BPF_JMP | BPF_JSET | BPF_X:
            lineSub.SetText('IF(A & X) JMP %d ELSE JMP %d' % (line + 1 + jt, line + 1 + jf))
        elif code == BPF_RET | BPF_K:
            lineSub.SetText('RET %d' % kShort)
        elif code == BPF_RET | BPF_A:
            lineSub.SetText('RET A')
        elif code == BPF_MISC | BPF_TAX:
            lineSub.SetText('MOV X,A')
        elif code == BPF_MISC | BPF_TXA:
            lineSub.SetText('MOV A,X')
        elif code == BPF_ST:
            lineSub.SetText('ST M[%d],A' % k)
        elif code == BPF_STX:
            lineSub.SetText('ST M[%d],X' % k)
        elif code == BPF_ALU | BPF_ADD | BPF_X:
            lineSub.SetText('ADD A,X')
        elif code == BPF_ALU | BPF_SUB | BPF_X:
            lineSub.SetText('SUB A,X')
        elif code == BPF_ALU | BPF_MUL | BPF_X:
            lineSub.SetText('MUL A,X')
        elif code == BPF_ALU | BPF_DIV | BPF_X:
            lineSub.SetText('DIV A,X')
        elif code == BPF_ALU | BPF_AND | BPF_X:
            lineSub.SetText('AND A,X')
        elif code == BPF_ALU | BPF_OR | BPF_X:
            lineSub.SetText('OR A,X')
        elif code == BPF_ALU | BPF_LSH | BPF_X:
            lineSub.SetText('LSH A,X')
        elif code == BPF_ALU | BPF_RSH | BPF_X:
            lineSub.SetText('RSH A,X')
        elif code == BPF_ALU | BPF_ADD | BPF_K:
            lineSub.SetText('ADD A,%d' % k)
        elif code == BPF_ALU | BPF_SUB | BPF_K:
            lineSub.SetText('SUB A,%d' % k)
        elif code == BPF_ALU | BPF_MUL | BPF_K:
            lineSub.SetText('MUL A,%d' % k)
        elif code == BPF_ALU | BPF_DIV | BPF_K:
            lineSub.SetText('DIV A,%d' % k)
        elif code == BPF_ALU | BPF_AND | BPF_K:
            lineSub.SetText('AND A,0x%x' % k)
        elif code == BPF_ALU | BPF_OR | BPF_K:
            lineSub.SetText('OR A,0x%x' % k)
        elif code == BPF_ALU | BPF_LSH | BPF_K:
            lineSub.SetText('LSH A,%d' % k)
        elif code == BPF_ALU | BPF_RSH | BPF_K:
            lineSub.SetText('RSH A,%d' % k)
        elif code == BPF_ALU | BPF_NEG:
            lineSub.SetText('NEG A')
        else:
            lineSub.SetText('UNKNOWN (%02x)' % code)
        line = line + 1


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)