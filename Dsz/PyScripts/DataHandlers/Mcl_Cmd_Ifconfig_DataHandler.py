# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Ifconfig_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.ifconfig', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Ifconfig', 'ifconfig', [])
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
    xml.Start('Ifconfig')
    fixedMsg = msg.FindMessage(MSG_KEY_RESULT_FIXED)
    fixed = FixedResult()
    fixed.Demarshal(fixedMsg)
    sub = xml.AddSubElement('FixedData')
    sub.AddSubElementWithText('Type', _fixedTypeToString(fixed.type))
    sub.AddSubElementWithText('HostName', fixed.hostName)
    sub.AddSubElementWithText('DomainName', fixed.domainName)
    sub.AddSubElementWithText('ScopeId', fixed.scopeId)
    if fixed.enableDns:
        sub.AddSubElementWithText('EnableDns', 'true')
    else:
        sub.AddSubElementWithText('EnableDns', 'false')
    if fixed.enableProxy:
        sub.AddSubElementWithText('EnableProxy', 'true')
    else:
        sub.AddSubElementWithText('EnableProxy', 'false')
    if fixed.enableRouting:
        sub.AddSubElementWithText('EnableRouting', 'true')
    else:
        sub.AddSubElementWithText('EnableRouting', 'false')
    sub2 = sub.AddSubElement('DnsServerList')
    _handleIpAddrs(fixedMsg, sub2)
    for entry in msg:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['retrieved'] or entry['key'] != MSG_KEY_RESULT_ADAPTER:
            continue
        adapterMsg = msg.FindMessage(entry['key'])
        adapter = AdapterResult()
        adapter.Demarshal(adapterMsg)
        sub = xml.AddSubElement('Interface')
        sub.AddAttribute('index', '%u' % adapter.index)
        sub.AddSubElementWithText('Status', _statusToString(adapter.status))
        if adapter.enabled:
            sub.AddSubElementWithText('Enabled', 'true')
        else:
            sub.AddSubElementWithText('Enabled', 'false')
        sub.AddSubElementWithText('Name', adapter.name)
        sub.AddSubElementWithText('Description', adapter.description)
        sub.AddSubElementWithText('DnsSuffix', adapter.dnsSuffix)
        sub2 = sub.AddSubElement('Wins')
        if adapter.primaryWins.IsValid():
            sub2.AddAddressIP('Primary', adapter.primaryWins)
        if adapter.secondaryWins.IsValid():
            sub2.AddAddressIP('Secondary', adapter.secondaryWins)
        if adapter.dhcp.IsValid():
            sub.AddAddressIP('DHCP', adapter.dhcp)
        if adapter.gateway.IsValid():
            sub.AddAddressIP('Gateway', adapter.gateway)
        sub.AddSubElementWithText('Type', _adapterTypeToString(adapter.type))
        if adapter.dhcpEnabled:
            sub.AddSubElementWithText('DhcpEnabled', 'true')
        else:
            sub.AddSubElementWithText('DhcpEnabled', 'false')
        if adapter.haveWins:
            sub.AddSubElementWithText('HaveWins', 'true')
        else:
            sub.AddSubElementWithText('HaveWins', 'false')
        _writeLease(sub, 'Lease', adapter)
        _writeAddress(sub, 'Address', adapter)
        sub.AddSubElementWithText('Mtu', '%u' % adapter.mtu)
        if adapter.arpEnabled:
            sub.AddSubElementWithText('EnabledArp', 'true')
        else:
            sub.AddSubElementWithText('EnabledArp', 'false')
        sub.AddSubElementWithText('SubnetMask', adapter.subnetMask)
        _handleIpAddrs(adapterMsg, sub)

    output.RecordXml(xml)
    output.EndWithStatus(input.GetStatus())
    return True


def _adapterTypeToString(type):
    if type == RESULT_ADAPTER_TYPE_ETHERNET:
        return 'Ethernet'
    else:
        if type == RESULT_ADAPTER_TYPE_TOKENRING:
            return 'TokenRing'
        if type == RESULT_ADAPTER_TYPE_FDDI:
            return 'FDDI'
        if type == RESULT_ADAPTER_TYPE_PPP:
            return 'PPP'
        if type == RESULT_ADAPTER_TYPE_LOCAL:
            return 'Local'
        if type == RESULT_ADAPTER_TYPE_IP6INIP4:
            return 'Ipv6-in-IPv4'
        if type == RESULT_ADAPTER_TYPE_SLIP:
            return 'SLIP'
        if type == RESULT_ADAPTER_TYPE_ATM:
            return 'ATM'
        if type == RESULT_ADAPTER_TYPE_802_11:
            return '802.11 wireless'
        if type == RESULT_ADAPTER_TYPE_TUNNEL:
            return 'Tunnel encapsulation'
        if type == RESULT_ADAPTER_TYPE_1394:
            return '1394 (firewire)'
        if type == RESULT_ADAPTER_TYPE_OTHER:
            return 'Other'
        return 'Other'


def _fixedTypeToString(type):
    if type == RESULT_FIXED_TYPE_BROADCAST:
        return 'Broadcast'
    else:
        if type == RESULT_FIXED_TYPE_PEER_TO_PEER:
            return 'Peer to Peer'
        if type == RESULT_FIXED_TYPE_MIXED:
            return 'Mixed'
        if type == RESULT_FIXED_TYPE_HYBRID:
            return 'Hybrid'
        return 'Other'


def _handleIpAddrs(msg, xml):
    import mcl.object.Message
    for entry in msg:
        if not entry['retrieved'] and entry['type'] == mcl.object.Message.MSG_TYPE_BINARY:
            addr = msg.FindIpAddr(entry['key'])
            if entry['key'] == MSG_KEY_RESULT_IP_DNS:
                sub = xml.AddSubElement('DnsServer')
            else:
                sub = xml.AddSubElement('AdapterIp')
            sub.AddAddressIP('Ip', addr)


def _statusToString(status):
    if status == RESULT_MEDIA_STATE_UP:
        return 'Up'
    else:
        if status == RESULT_MEDIA_STATE_DOWN:
            return 'Down'
        if status == RESULT_MEDIA_STATE_TESTING:
            return 'Testing'
        if status == RESULT_MEDIA_STATE_UNKNOWN:
            return 'Unknown'
        if status == RESULT_MEDIA_STATE_DORMANT:
            return 'Dormant'
        if status == RESULT_MEDIA_STATE_NOT_PRESENT:
            return 'Not Present'
        if status == RESULT_MEDIA_STATE_LOWER_LAYER_DOWN:
            return 'Lower Layer Down'
        return 'Not Known'


def _writeLease(xml, name, set):
    sub = xml.AddSubElement(name)
    sub.AddTimeElement('Obtained', set.leaseObtained)
    sub.AddTimeElement('Expires', set.leaseExpires)


def _writeAddress(xml, name, set):
    addressStr = ''
    i = 0
    while i < set.physicalAddressLength:
        addressStr = addressStr + '%.2X' % set.physicalAddress[i]
        if i != set.physicalAddressLength - 1:
            addressStr = addressStr + '-'
        i = i + 1

    xml.AddSubElementWithText(name, addressStr)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)