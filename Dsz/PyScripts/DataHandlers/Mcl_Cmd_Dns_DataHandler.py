# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Dns_DataHandler.py
QUERY_CLASS_IN = 1
QUERY_CLASS_CHAOS = 3
QUERY_CLASS_HS = 4
QUERY_CLASS_ANY = 255
DNS_TYPE_A = 1
DNS_TYPE_NS = 2
DNS_TYPE_MD = 3
DNS_TYPE_MF = 4
DNS_TYPE_CNAME = 5
DNS_TYPE_SOA = 6
DNS_TYPE_MB = 7
DNS_TYPE_MG = 8
DNS_TYPE_MR = 9
DNS_TYPE_NULL = 10
DNS_TYPE_WKS = 11
DNS_TYPE_PTR = 12
DNS_TYPE_HINFO = 13
DNS_TYPE_MINFO = 14
DNS_TYPE_MX = 15
DNS_TYPE_TEXT = 16
DNS_TYPE_RP = 17
DNS_TYPE_AFSDB = 18
DNS_TYPE_X25 = 19
DNS_TYPE_ISDN = 20
DNS_TYPE_RT = 21
DNS_TYPE_NSAP = 22
DNS_TYPE_NSAPPTR = 23
DNS_TYPE_SIG = 24
DNS_TYPE_KEY = 25
DNS_TYPE_PX = 26
DNS_TYPE_GPOS = 27
DNS_TYPE_AAAA = 28
DNS_TYPE_LOC = 29
DNS_TYPE_NXT = 30
DNS_TYPE_SRV = 33
DNS_TYPE_ATMA = 34
DNS_TYPE_TKEY = 249
DNS_TYPE_TSIG = 250
DNS_TYPE_IXFR = 251
DNS_TYPE_AXFR = 252
DNS_TYPE_MAILB = 253
DNS_TYPE_MAILA = 254
DNS_TYPE_ALL = 255
DNS_TYPE_ANY = 255
DNS_TYPE_WINS = 65281
DNS_TYPE_WINSR = 65282
DNS_TYPE_NBSTAT = DNS_TYPE_WINSR

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.dns', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Dns', 'dns', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.DNS:
            return _handleDnsData(msg, output)
        if input.GetMessageType() == mcl.msgtype.DNS_CACHE:
            return _handleDnsCacheData(msg, output)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleDnsData(msg, output):
    result = ResultDns()
    result.Demarshal(msg)
    output.EndWithStatus(_parseResponse(output, result.rawData))
    return True


def _handleDnsCacheData(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('DnsCacheEntries')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        result = ResultCache()
        result.Demarshal(msg)
        sub = xml.AddSubElement('CacheEntry')
        sub.AddTimeElement('Ttl', result.ttl)
        sub.AddSubElementWithText('Name', result.name)
        sub.AddSubElementWithText('EntryName', result.entryName)
        data = sub.AddSubElement('Data')
        data.AddAttribute('type', '%u' % result.dataType)
        data.AddAttribute('typeStr', _getTypeStr(result.dataType))
        data.SetText(result.data)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _getTypeStr(type):
    if type == DNS_TYPE_A:
        return 'A'
    else:
        if type == DNS_TYPE_NS:
            return 'NS'
        if type == DNS_TYPE_MD:
            return 'MD'
        if type == DNS_TYPE_MF:
            return 'MX'
        if type == DNS_TYPE_CNAME:
            return 'CNAME'
        if type == DNS_TYPE_SOA:
            return 'SOA'
        if type == DNS_TYPE_MB:
            return 'MB'
        if type == DNS_TYPE_MG:
            return 'MG'
        if type == DNS_TYPE_MR:
            return 'MR'
        if type == DNS_TYPE_NULL:
            return 'NULL'
        if type == DNS_TYPE_WKS:
            return 'WKS'
        if type == DNS_TYPE_PTR:
            return 'PTR'
        if type == DNS_TYPE_HINFO:
            return 'HINFO'
        if type == DNS_TYPE_MINFO:
            return 'MINFO'
        if type == DNS_TYPE_MX:
            return 'MX'
        if type == DNS_TYPE_TEXT:
            return 'TEXT'
        if type == DNS_TYPE_RP:
            return 'RP'
        if type == DNS_TYPE_AFSDB:
            return 'AFSDB'
        if type == DNS_TYPE_X25:
            return 'X25'
        if type == DNS_TYPE_ISDN:
            return 'ISDN'
        if type == DNS_TYPE_RT:
            return 'RT'
        if type == DNS_TYPE_NSAP:
            return 'NSAP'
        if type == DNS_TYPE_NSAPPTR:
            return 'NSAPPTR'
        if type == DNS_TYPE_SIG:
            return 'SIG'
        if type == DNS_TYPE_KEY:
            return 'KEY'
        if type == DNS_TYPE_PX:
            return 'PX'
        if type == DNS_TYPE_GPOS:
            return 'GPOS'
        if type == DNS_TYPE_AAAA:
            return 'AAAA'
        if type == DNS_TYPE_LOC:
            return 'LOC'
        if type == DNS_TYPE_NXT:
            return 'NXT'
        if type == DNS_TYPE_SRV:
            return 'SRV'
        if type == DNS_TYPE_ATMA:
            return 'ATMA'
        return 'UNKNOWN'


def _parseDnsHeader(demarsh):
    hdr = {}
    hdr['id'] = demarsh.GetU16()
    byteThree = demarsh.GetU8()
    hdr['qr'] = byteThree >> 7 & 1
    hdr['opcode'] = byteThree >> 3 & 15
    hdr['aa'] = byteThree >> 2 & 1
    hdr['tc'] = byteThree >> 1 & 1
    hdr['rd'] = byteThree & 1
    byteFour = demarsh.GetU8()
    hdr['ra'] = byteFour >> 7 & 1
    hdr['zero'] = byteFour >> 4 & 7
    hdr['rcode'] = byteFour & 15
    hdr['qdcount'] = demarsh.GetU16()
    hdr['ancount'] = demarsh.GetU16()
    hdr['nscount'] = demarsh.GetU16()
    hdr['arcount'] = demarsh.GetU16()
    return hdr


def _parseQuestion(demarsh, xml):
    _printString(demarsh, xml)
    qType = demarsh.GetU16()
    qClass = demarsh.GetU16()
    xml.AddSubElementWithText('Type', '0x%04x' % qType)
    xml.AddSubElementWithText('Class', '0x%04x' % qClass)


def _parseResource(demarsh, xml):
    _printString(demarsh, xml)
    aType = demarsh.GetU16()
    aClass = demarsh.GetU16()
    typeStr = None
    if aClass == QUERY_CLASS_IN:
        if aType == DNS_TYPE_A:
            typeStr = 'Host Address (INET)'
        elif aType == DNS_TYPE_NS:
            typeStr = 'Authoritative Server (INET)'
        elif aType == DNS_TYPE_CNAME:
            typeStr = 'Canonical name (INET)'
        elif aType == DNS_TYPE_SOA:
            typeStr = 'Start of Authority Zone (INET)'
        elif aType == DNS_TYPE_PTR:
            typeStr = 'Domain Name Pointer (INET)'
        elif aType == DNS_TYPE_HINFO:
            typeStr = 'Host Information (INET)'
        elif aType == DNS_TYPE_MX:
            typeStr = 'Mail Routing Information (INET)'
        elif aType == DNS_TYPE_SRV:
            typeStr = 'Service Location (INET)'
        elif aType == DNS_TYPE_AAAA:
            typeStr = 'IPv6 Address'
    if typeStr != None:
        xml.AddSubElementWithText('TypeStr', typeStr)
    else:
        xml.AddSubElementWithText('Type', '0x%04x' % aType)
        xml.AddSubElementWithText('Class', '0x%04x' % aClass)
    ttl = demarsh.GetU32()
    xml.AddAttribute('ttl', '%u' % ttl)
    sub = xml.AddSubElement('DnsData')
    _printData(demarsh, sub, aType, aClass)
    return


def _parseResponse(output, rsp):
    from mcl.object.Demarshaler import Demarshaler
    demarsh = Demarshaler(rsp)
    try:
        dnsHdr = _parseDnsHeader(demarsh)
    except:
        output.RecordError('Response not long enough (%d) to contain valid DNS response' % len(rsp))
        return mcl.target.CALL_FAILED

    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Dns')
    xml.AddAttribute('id', '0x%04x' % dnsHdr['id'])
    if dnsHdr['qr'] != 0:
        xml.AddSubElement('Response')
    xml.AddAttribute('opCode', '0x%02x' % dnsHdr['opcode'])
    if dnsHdr['aa'] != 0:
        xml.AddSubElement('Authority')
    if dnsHdr['tc'] != 0:
        xml.AddSubElement('Truncated')
    if dnsHdr['ra'] != 0:
        xml.AddSubElement('RecursionAvailable')
    rspStr = None
    if dnsHdr['rcode'] == 0:
        rspStr = 'No Error'
    elif dnsHdr['rcode'] == 1:
        rspStr = 'Format Error'
    elif dnsHdr['rcode'] == 2:
        rspStr = 'Server Failure'
    elif dnsHdr['rcode'] == 3:
        rspStr = 'Name Error (domain does not exist)'
    elif dnsHdr['rcode'] == 4:
        rspStr = 'Not Implemented'
    elif dnsHdr['rcode'] == 5:
        rspStr = 'Operation Refused'
    elif dnsHdr['rcode'] == 6:
        rspStr = 'The name exists'
    elif dnsHdr['rcode'] == 7:
        rspStr = 'The RRset (name,type) exists'
    elif dnsHdr['rcode'] == 8:
        rspStr = 'The RRset (name,type) does not exist'
    elif dnsHdr['rcode'] == 9:
        rspStr = 'The requestor is not authorized to perform this operation'
    elif dnsHdr['rcode'] == 10:
        rspStr = 'The zone specified is not a zone'
    elif dnsHdr['rcode'] == 16:
        rspStr = 'Bad Signature'
    elif dnsHdr['rcode'] == 17:
        rspStr = 'Bad Key'
    elif dnsHdr['rcode'] == 18:
        rspStr = 'Bad Time'
    else:
        rspStr = 'Unkown error'
    sub = xml.AddSubElement('ResponseCode')
    if rspStr != None:
        sub.SetText(rspStr)
    sub.AddAttribute('code', '%i' % dnsHdr['rcode'])
    sub = xml.AddSubElement('QuestionData')
    if dnsHdr['qdcount'] > 0:
        i = 0
        while i < dnsHdr['qdcount']:
            subsub = sub.AddSubElement('Question')
            _parseQuestion(demarsh, subsub)
            i = i + 1

    sub = xml.AddSubElement('AnswerData')
    if dnsHdr['ancount'] > 0:
        i = 0
        while i < dnsHdr['ancount']:
            subsub = sub.AddSubElement('Answer')
            _parseResource(demarsh, subsub)
            i = i + 1

    sub = xml.AddSubElement('NameServerData')
    if dnsHdr['nscount'] > 0:
        i = 0
        while i < dnsHdr['nscount']:
            subsub = sub.AddSubElement('NameServer')
            _parseResource(demarsh, subsub)
            i = i + 1

    sub = xml.AddSubElement('AdditionalRecordsData')
    if dnsHdr['arcount'] > 0:
        i = 0
        while i < dnsHdr['arcount']:
            subsub = sub.AddSubElement('AdditionalData')
            _parseResource(demarsh, subsub)
            i = i + 1

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _printData(demarsh, xml, dType, dClass):
    data = demarsh.GetData(lengthBytes=2)
    if dClass == QUERY_CLASS_IN:
        sub = None
        if dType == DNS_TYPE_A:
            if len(data) == 4:
                xml.AddAttribute('type', 'hostAddress')
                xml.SetText('%u.%u.%u.%u' % (data[0], data[1], data[2], data[3]))
                return
        elif dType == DNS_TYPE_AAAA:
            if len(data) == 16:
                xml.AddAttribute('type', 'hostAddress')
                xml.SetText('%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x:%02x%02x' % (
                 data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7],
                 data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15]))
                return
        else:
            if dType == DNS_TYPE_NS:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'nameServer')
                _printString(demarsh, xml)
                return
            if dType == DNS_TYPE_CNAME:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'ownerPrimaryName')
                _printString(demarsh, xml)
                return
            if dType == DNS_TYPE_PTR:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'domain')
                _printString(demarsh, xml)
                return
            if dType == DNS_TYPE_SOA:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'authorityZone')
                sub = xml.AddSubElement('PrimaryNameServer')
                _printString(demarsh, sub)
                sub = xml.AddSubElement('ResponsibleMailbox')
                _printString(demarsh, sub)
                sub = xml.AddSubElement('Version')
                _printDword(demarsh, sub)
                sub = xml.AddSubElement('RefreshInterval')
                _printDword(demarsh, sub)
                sub = xml.AddSubElement('RetryInterval')
                _printDword(demarsh, sub)
                sub = xml.AddSubElement('ExpirationLimit')
                _printDword(demarsh, sub)
                sub = xml.AddSubElement('MinimumTTL')
                _printDword(demarsh, sub)
                return
            if dType == DNS_TYPE_MX:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'mailExchange')
                sub = xml.AddSubElement('Preference')
                _printWord(demarsh, sub)
                sub = xml.AddSubElement('ExchangeMailbox')
                _printString(demarsh, sub)
                return
            if dType == DNS_TYPE_HINFO:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'hostInfo')
                sub = xml.AddSubElement('CPUType')
                _printSubString(demarsh, sub)
                sub = xml.AddSubElement('HostType')
                _printSubString(demarsh, sub)
                return
            if dType == DNS_TYPE_SRV:
                demarsh.SetIndex(demarsh.GetIndex() - len(data))
                xml.AddAttribute('type', 'serviceLocation')
                sub = xml.AddSubElement('Priority')
                _printWord(demarsh, sub, True)
                sub = xml.AddSubElement('Weight')
                _printWord(demarsh, sub, True)
                sub = xml.AddSubElement('Port')
                _printWord(demarsh, sub, True)
                sub = xml.AddSubElement('Target')
                _printString(demarsh, sub)
    xml.AddAttribute('unknownData', 'true')
    sub = xml.AddSubElement('RawData')
    sub.SetTextAsData(data)
    return


def _printDword(demarsh, xml, decimal=False):
    dword = demarsh.GetU32()
    if decimal:
        xml.SetText('%u' % dword)
    else:
        xml.SetText('0x%08x' % dword)


def _printString(demarsh, xml):
    doneName = False
    while not doneName:
        sub = xml.AddSubElement('String')
        doneName = _printSubString(demarsh, sub)


def _printSubString(demarsh, xml):
    len = demarsh.GetU8()
    if len == 0:
        return True
    else:
        if len & 192:
            offset = (len & 63) << 8
            offset |= demarsh.GetU8()
            currentIndex = demarsh.GetIndex()
            demarsh.SetIndex(offset)
            try:
                _printString(demarsh, xml)
            finally:
                demarsh.SetIndex(currentIndex)

            return True
        strBytes = demarsh.GetData(expectedSize=len, lengthBytes=0)
        cList = list()
        for val in strBytes:
            if val == 0:
                break
            cList.append(chr(val))

        xml.SetText(''.join(cList))
        return False


def _printWord(demarsh, xml, decimal=False):
    word = demarsh.GetU16()
    if decimal:
        xml.SetText('%u' % word)
    else:
        xml.SetText('0x%04x' % word)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)