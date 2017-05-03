# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Netmap_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.netmap', globals())
    NETMAP_SOFTWARE = {RESULT_SOFTWARE_WORKSTATION: ('NETMAP_DATA_SOFTWARE_WORKSTATION', 'LAN Manager workstation'),
       RESULT_SOFTWARE_SERVER: ('NETMAP_DATA_SOFTWARE_SERVER', 'LAN Manager server'),
       RESULT_SOFTWARE_SQL_SERVER: ('NETMAP_DATA_SOFTWARE_SQL_SERVER', 'Server running Microsoft SQL Server'),
       RESULT_SOFTWARE_DOMAIN_CTRL: ('NETMAP_DATA_SOFTWARE_DOMAIN_CTRL', 'Primary domain controller'),
       RESULT_SOFTWARE_DOMAIN_BAKCTRL: ('NETMAP_DATA_SOFTWARE_DOMAIN_BAKCTRL', 'Backup domain controller'),
       RESULT_SOFTWARE_TIME_SOURCE: ('NETMAP_DATA_SOFTWARE_TIME_SOURCE', 'Server running the Timesource service'),
       RESULT_SOFTWARE_AFP: ('NETMAP_DATA_SOFTWARE_AFP', 'Apple File Protocol server'),
       RESULT_SOFTWARE_NOVELL: ('NETMAP_DATA_SOFTWARE_NOVELL', 'Novell server'),
       RESULT_SOFTWARE_DOMAIN_MEMBER: ('NETMAP_DATA_SOFTWARE_DOMAIN_MEMBER', 'LAN Manager 2.x domain member'),
       RESULT_SOFTWARE_LOCAL_LIST_ONLY: ('NETMAP_DATA_SOFTWARE_LOCAL_LIST_ONLY', 'Servers maintained by the browser'),
       RESULT_SOFTWARE_PRINTQ_SERVER: ('NETMAP_DATA_SOFTWARE_PRINTQ_SERVER', 'Server sharing print queue'),
       RESULT_SOFTWARE_DIALIN_SERVER: ('NETMAP_DATA_SOFTWARE_DIALIN_SERVER', 'Server running dial-in service'),
       RESULT_SOFTWARE_XENIX_SERVER: ('NETMAP_DATA_SOFTWARE_XENIX_SERVER', 'Xenix server'),
       RESULT_SOFTWARE_SERVER_MFPN: ('NETMAP_DATA_SOFTWARE_SERVER_MFPN', 'Microsoft File and Print for NetWare'),
       RESULT_SOFTWARE_NT: ('NETMAP_DATA_SOFTWARE_NT', 'Windows NT Family'),
       RESULT_SOFTWARE_WFW: ('NETMAP_DATA_SOFTWARE_WFW', 'Server running Windows for Workgroups'),
       RESULT_SOFTWARE_SERVER_NT: ('NETMAP_DATA_SOFTWARE_SERVER_NT', 'Windows NT server that is not a domain controller'),
       RESULT_SOFTWARE_POTENTIAL_BROWSER: ('NETMAP_DATA_SOFTWARE_POTENTIAL_BROWSER', 'Server that can run the browser service'),
       RESULT_SOFTWARE_BACKUP_BROWSER: ('NETMAP_DATA_SOFTWARE_BACKUP_BROWSER', 'Server running a browser service as backup'),
       RESULT_SOFTWARE_MASTER_BROWSER: ('NETMAP_DATA_SOFTWARE_MASTER_BROWSER', 'Server running the master browser service'),
       RESULT_SOFTWARE_DOMAIN_MASTER: ('NETMAP_DATA_SOFTWARE_DOMAIN_MASTER', 'Server running the domain master browser'),
       RESULT_SOFTWARE_DOMAIN_ENUM: ('NETMAP_DATA_SOFTWARE_DOMAIN_ENUM', 'Primary domain'),
       RESULT_SOFTWARE_WINDOWS: ('NETMAP_DATA_SOFTWARE_WINDOWS', 'Windows 9x Family'),
       RESULT_SOFTWARE_TERMINALSERVER: ('NETMAP_DATA_SOFTWARE_TERMINALSERVER', 'Terminal Server'),
       RESULT_SOFTWARE_CLUSTER_NT: ('NETMAP_DATA_SOFTWARE_CLUSTER_NT', 'Server clusters available in the domain'),
       RESULT_SOFTWARE_CLUSTER_VS_NT: ('NETMAP_DATA_SOFTWARE_CLUSTER_VS_NT', 'Cluster virtual servers available in the domain')
       }
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Netmap', 'netmap', [])
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
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Entries')
    for entry in msg:
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['key'] == MSG_KEY_RESULT_ERROR:
            error = ResultError()
            try:
                error.Demarshal(msg)
                output.RecordModuleError(error.pluginError, error.osError, errorStrings)
            except:
                output.RecordXml(xml)
                raise

        elif entry['key'] == MSG_KEY_RESULT_MACHINE:
            data = ResultData()
            try:
                submsg = msg.FindMessage(MSG_KEY_RESULT_MACHINE)
                data.Demarshal(submsg)
            except:
                output.RecordXml(xml)
                raise

            sub = xml.AddSubElement('Entry')
            sub.AddSubElementWithText('LocalName', data.localName)
            sub.AddSubElementWithText('RemoteName', data.remoteName)
            sub.AddSubElementWithText('ParentName', data.parentName)
            sub.AddSubElementWithText('Comment', data.comment)
            sub.AddSubElementWithText('Provider', data.provider)
            typeStr = ''
            if data.type == RESULT_RESOURCETYPE_DISK:
                typeStr = 'DISK'
            elif data.type == RESULT_RESOURCETYPE_PRINT:
                typeStr = 'PRINT'
            elif data.displayType == RESULT_RESOURCEDISPLAYTYPE_DOMAIN:
                typeStr = 'DOMAIN'
            elif data.displayType == RESULT_RESOURCEDISPLAYTYPE_SERVER:
                typeStr = 'SERVER'
            elif data.displayType == RESULT_RESOURCEDISPLAYTYPE_SHARE:
                typeStr = 'SHARE'
            else:
                typeStr = 'GENERIC'
            sub.AddSubElementWithText('Type', typeStr)
            sub.AddAttribute('level', '%u' % data.level)
            i = 0
            while i < RESULT_MAX_ADDRS:
                if len(data.addrs[i]) > 0:
                    sub.AddSubElementWithText('Addr', data.addrs[i])
                i = i + 1

            if data.flags & RESULT_FLAG_HAVE_OS_INFO:
                osData = ResultOsInfo()
                try:
                    osData.Demarshal(submsg)
                except:
                    output.RecordXml(xml)
                    raise

                sub2 = sub.AddSubElement('OsInfo')
                sub2.AddAttribute('osVersionMajor', '%u' % osData.osMajor)
                sub2.AddAttribute('osVersionMinor', '%u' % osData.osMinor)
                if osData.platformType == RESULT_PLATFORM_DOS:
                    sub2.AddAttribute('platformType', 'DOS')
                elif osData.platformType == RESULT_PLATFORM_OS2:
                    sub2.AddAttribute('platformType', 'OS2')
                elif osData.platformType == RESULT_PLATFORM_NT:
                    sub2.AddAttribute('platformType', 'NT')
                elif osData.platformType == RESULT_PLATFORM_OSF:
                    sub2.AddAttribute('platformType', 'OSF')
                elif osData.platformType == RESULT_PLATFORM_VMS:
                    sub2.AddAttribute('platformType', 'VMS')
                elif osData.platformType == RESULT_PLATFORM_UNKNOWN:
                    sub2.AddAttribute('platformType', 'UNKNOWN')
                else:
                    sub2.AddAttribute('platformType', 'UNKNOWN')
                for softwareFlag in NETMAP_SOFTWARE.keys():
                    if osData.software & softwareFlag:
                        sub3 = sub2.AddSubElement('Software')
                        sub3.AddAttribute('name', NETMAP_SOFTWARE[softwareFlag][0])
                        sub3.SetText(NETMAP_SOFTWARE[softwareFlag][1])

            if data.flags & RESULT_FLAG_HAVE_TIME:
                timeData = ResultTime()
                try:
                    timeData.Demarshal(submsg)
                except:
                    output.RecordXml(xml)
                    raise

                sub.AddTimeElement('TimeOfDay', timeData.timeOfDay)
                sub.AddTimeElement('TimeZoneOffset', timeData.tzOffset)
        else:
            output.RecordXml(xml)
            output.RecordError('Invalid return key (0x%08x)' % entry['key'])
            output.EndWithStatus(mcl.target.DSZ_CALL_FAILED)
            return True

    output.RecordXml(xml)
    output.End()
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