# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DomainController_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.domaincontroller', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('DomainController', 'domaincontroller', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    rtn = mcl.target.CALL_SUCCEEDED
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        statusResults = ResultStatus()
        statusResults.Demarshal(msg)
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('DomainController')
        xml.AddSubElementWithText('DCName', statusResults.dc)
        properties = xml.AddSubElement('Properties')
        if statusResults.typeServ & RESULT_FLAG_TYPE_DOMAIN_CTRL:
            properties.AddSubElement('Primary')
        if statusResults.typeServ & RESULT_FLAG_TYPE_DOMAIN_BAKCTRL:
            properties.AddSubElement('Backup')
        if statusResults.extraInfoRtn != 0:
            sub = xml.AddSubElement('ExtendedErrorInfo')
            errorStr = output.TranslateOsError(statusResults.extraInfoRtn)
            sub.AddSubElementWithText('QueryError', errorStr)
        else:
            results = ResultDomainController()
            results.Demarshal(msg)
            xml.AddSubElementWithText('DCFullName', results.dcName)
            sub = xml.AddSubElement('DCAddress')
            sub.SetText(results.dcAddress)
            if results.addressType == RESULT_ADDRTYPE_INET:
                sub.AddAttribute('addrType', 'IPAddress')
            elif results.addressType == RESULT_ADDRTYPE_NETBIOS:
                sub.AddAttribute('addrType', 'NetBIOS')
            else:
                sub.AddAttribute('addrType', 'Unknown')
            xml.AddSubElementWithText('DomainGuid', results.domainGuid)
            xml.AddSubElementWithText('DomainName', results.domainName)
            xml.AddSubElementWithText('DnsForestName', results.dnsForestName)
            xml.AddSubElementWithText('DCSiteName', results.dcSiteName)
            xml.AddSubElementWithText('ClientSiteName', results.clientSiteName)
            if results.flags & RESULT_FLAG_DC_KDC:
                properties.AddSubElement('KerberosKeyDistCenter')
            if results.flags & RESULT_FLAG_DC_GC:
                properties.AddSubElement('GlobalCatalog')
            if results.flags & RESULT_FLAG_DC_DS:
                properties.AddSubElement('DirectoryService')
            if results.flags & RESULT_FLAG_DC_TIMESERV:
                properties.AddSubElement('TimeService')
            if results.flags & RESULT_FLAG_DC_WRITABLE:
                properties.AddSubElement('SAM')
        if statusResults.dcEnumStatus == 1:
            sub = xml.AddSubElement('AddlInformation')
            sub.AddSubElementWithText('EnumQueryError', 'Although all domain controllers (dcs) were requested, only primary dc obtained as enumeration of dcs failed')
            rtn = mcl.target.CALL_FAILED
        output.RecordXml(xml)

    output.EndWithStatus(rtn)
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