# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Route_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.route', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Route', 'route', [])
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
    if input.GetMessageType() == mcl.msgtype.ROUTE_LIST:
        xml.Start('Routes')
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            result = Result()
            result.Demarshal(msg)
            sub = xml.AddSubElement('Route')
            sub.AddAddressIP('Destination', result.dest)
            if result.dest.GetType() == result.dest.IPADDR_TYPE_IPV4:
                sub.AddSubElementWithText('Netmask', '%u.%u.%u.%u' % (
                 result.netmask >> 24 & 255, result.netmask >> 16 & 255,
                 result.netmask >> 8 & 255, result.netmask & 255))
            else:
                sub.AddSubElementWithText('Netmask', '%u' % result.netmask)
            sub.AddAddressIP('Gateway', result.gateway)
            sub.AddSubElementWithText('Interface', result.iface)
            sub.AddAttribute('metric', '%d' % result.metric)
            sub.AddAttribute('origin', _getOriginStr(result.origin))
            if result.flags & RESULT_FLAG_LOOPBACK:
                sub.AddSubElement('FlagLoopback')
            if result.flags & RESULT_FLAG_AUTOCONFIG:
                sub.AddSubElement('FlagAutoConfigure')
            if result.flags & RESULT_FLAG_PERMANENT:
                sub.AddSubElement('FlagPermanent')
            if result.flags & RESULT_FLAG_PUBLISH:
                sub.AddSubElement('FlagPublish')

    elif input.GetMessageType() == mcl.msgtype.ROUTE_ADD:
        xml.Start('RouteAdded')
    elif input.GetMessageType() == mcl.msgtype.ROUTE_DELETE:
        xml.Start('RouteDeleted')
    else:
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _getOriginStr(origin):
    if origin == RESULT_ORIGIN_MANUAL:
        return 'MANUAL'
    else:
        if origin == RESULT_ORIGIN_WELLKNOWN:
            return 'WELLKNOWN'
        if origin == RESULT_ORIGIN_DHCP:
            return 'DHCP'
        if origin == RESULT_ORIGIN_ROUTER_AD:
            return 'ROUTER_AD'
        if origin == RESULT_ORIGIN_6_TO_4:
            return '6_TO_4'
        return 'UNKNOWN'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)