# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Firewall_DataHandler.py
PROTOCOL_NAMES = {0: 'Any',
   1: 'ICMPv4',
   2: 'IGMP',
   6: 'TCP',
   17: 'UDP',
   41: 'IPv6',
   43: 'IPv6-Route',
   44: 'IPv6-Frag',
   47: 'GRE',
   58: 'ICMPv6',
   59: 'IPv6-NoNxt',
   60: 'IPv6-Opts',
   112: 'VRRP',
   113: 'PGM',
   115: 'P2TP'
   }

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.firewall', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Firewall', 'firewall', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    for entry in msg:
        if entry['key'] == MSG_KEY_RESULT_ENABLE:
            return _handleEnable(msg, output)
        if entry['key'] == MSG_KEY_RESULT_STATUS:
            return _handleStatus(msg, output)
        if entry['key'] == MSG_KEY_RESULT_NOACTION:
            return _handleNoAction(msg, output)
        if entry['key'] == MSG_KEY_RESULT_DELETE:
            return _handleDelete(msg, output)
        output.RecordError('Unhandled key (0x%08x)' % entry['key'])
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleDelete(msg, output):
    results = ResultDelete()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Delete')
    xml.AddAttribute('name', results.name)
    xml.AddAttribute('port', '%u' % results.portNum)
    if results.protocol == FIREWALL_PROTOCOL_TCP:
        xml.AddAttribute('protocol', 'TCP')
    elif results.protocol == FIREWALL_PROTOCOL_UDP:
        xml.AddAttribute('protocol', 'UDP')
    else:
        xml.AddAttribute('protocol', 'unknown')
    output.RecordXml(xml)
    output.End()
    return True


def _handleEnable(msg, output):
    results = ResultEnable()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Enabled')
    if results.cleanup:
        xml.AddAttribute('closePending', 'true')
    else:
        xml.AddAttribute('closePending', 'false')
    xml.AddAttribute('port', '%u' % results.portNum)
    if results.protocol == FIREWALL_PROTOCOL_TCP:
        xml.AddAttribute('protocol', 'TCP')
    elif results.protocol == FIREWALL_PROTOCOL_UDP:
        xml.AddAttribute('protocol', 'UDP')
    else:
        xml.AddAttribute('protocol', 'unknown')
    output.RecordXml(xml)
    if results.cleanup:
        output.GoToBackground()
    output.End()
    return True


def _handleNoAction(msg, output):
    results = ResultNoAction()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('NoAction')
    output.RecordXml(xml)
    if results.cleanup:
        output.GoToBackground()
    output.End()
    return True


def _handleStatus(msg, output):
    submsg = msg.FindMessage(MSG_KEY_RESULT_STATUS)
    status = ResultStatusHeader()
    status.Demarshal(submsg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Status')
    if status.flags & RESULT_STATUS_FLAG_FIREWALL_ENABLED:
        xml.AddAttribute('enabled', 'true')
    else:
        xml.AddAttribute('enabled', 'false')
    if status.flags & RESULT_STATUS_FLAG_VISTA:
        if status.flags & RESULT_STATUS_FLAG_NO_MODIFY:
            xml.AddAttribute('modify', 'false')
        else:
            xml.AddAttribute('modify', 'true')
    while submsg.GetNumRetrieved() < submsg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        _outputProfile(submsg, output, xml)

    output.RecordXml(xml)
    output.End()
    return True


def _outputProfile(msg, output, xmlParent):
    submsg = msg.FindMessage(MSG_KEY_RESULT_PROFILE)
    hdr = ResultProfileHeader()
    hdr.Demarshal(submsg)
    if hdr.type == RESULT_PROFILE_TYPE_STANDARD:
        xml = xmlParent.AddSubElement('Standard')
    elif hdr.type == RESULT_PROFILE_TYPE_DOMAIN:
        xml = xmlParent.AddSubElement('Domain')
    elif hdr.type == RESULT_PROFILE_TYPE_PUBLIC:
        xml = xmlParent.AddSubElement('Public')
    elif hdr.type == RESULT_PROFILE_TYPE_PRIVATE:
        xml = xmlParent.AddSubElement('Private')
    else:
        output.RecordError('Unhandled profile type (%u)' % hdr.type)
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False
    if hdr.flags & RESULT_PROFILE_FLAG_ENABLED:
        xml.AddAttribute('enabled', 'true')
    else:
        xml.AddAttribute('enabled', 'false')
    if hdr.flags & RESULT_PROFILE_FLAG_ALLOW_EXCEPTIONS:
        xml.AddAttribute('exceptions', 'true')
    else:
        xml.AddAttribute('exceptions', 'false')
    if hdr.flags & RESULT_PROFILE_FLAG_ACTIVE:
        xml.AddAttribute('active', 'true')
    else:
        xml.AddAttribute('active', 'false')
    if hdr.flags & RESULT_PROFILE_FLAG_INBOUND_BLOCK:
        xml.AddAttribute('inbound', 'block')
    else:
        xml.AddAttribute('inbound', 'allow')
    if hdr.flags & RESULT_PROFILE_FLAG_OUTBOUND_BLOCK:
        xml.AddAttribute('outbound', 'block')
    else:
        xml.AddAttribute('outbound', 'allow')
    while submsg.GetNumRetrieved() < submsg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        rule = ResultRule()
        rule.Demarshal(submsg)
        if len(rule.applicationName) > 0:
            _outputRule(xml.AddSubElement('Application'), rule)
        else:
            _outputRule(xml.AddSubElement('Port'), rule)


def _outputRule(xml, rule):
    if rule.flags & RESULT_RULE_FLAG_IN and rule.flags & RESULT_RULE_FLAG_OUT:
        dir = 'Both'
    elif rule.flags & RESULT_RULE_FLAG_IN:
        dir = 'In'
    else:
        dir = 'Out'
    xml.AddSubElementWithText('Scope', rule.scope)
    if rule.flags & RESULT_RULE_FLAG_ENABLED:
        xml.AddSubElementWithText('Status', 'Enabled')
    else:
        xml.AddSubElementWithText('Status', 'Disabled')
    xml.AddSubElementWithText('RuleString', rule.ruleString)
    xml.AddSubElementWithText('Direction', dir)
    if rule.flags & RESULT_RULE_FLAG_ALLOW:
        xml.AddSubElementWithText('Action', 'Allow')
    else:
        xml.AddSubElementWithText('Action', 'Block')
    xml.AddSubElementWithText('Group', rule.group)
    if len(rule.applicationName) > 0:
        xml.AddSubElementWithText('Program', rule.applicationName)
        xml.AddSubElementWithText('ProgramName', rule.ruleName)
    else:
        if PROTOCOL_NAMES.has_key(rule.protocol):
            protocol = PROTOCOL_NAMES[rule.protocol]
        else:
            protocol = 'Unknown'
        if len(rule.ports) > 0:
            ports = rule.ports
        else:
            ports = '*'
        xml.AddSubElementWithText('Port', ports)
        xml.AddSubElementWithText('Protocol', protocol)
        xml.AddSubElementWithText('PortName', rule.ruleName)


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)