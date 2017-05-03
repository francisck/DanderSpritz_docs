# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_NetBios_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.network.cmd.netbios', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('NetBios', 'netbios', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    gotAny = False
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('NetBios')
        submsg = msg.FindMessage(MSG_KEY_RESULT_NETBIOS_ADAPTER)
        statusResults = ResultStatus()
        statusResults.Demarshal(submsg)
        if statusResults.status == 0:
            gotAny = True
            _handleNCB(xml, output, submsg)
            _handleAdapter(xml, output, submsg)
            output.RecordXml(xml)
        else:
            output.RecordModuleError(statusResults.errType, 0, errorStrings)
            output.RecordError('Netbios Error (0x%x): %s' % (statusResults.rtnCode, _getNetbiosError(statusResults.rtnCode)))

    if gotAny:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    else:
        output.EndWithStatus(mcl.target.CALL_FAILED)
    return True


def _handleNCB(xml, output, msg):
    results = ResultNCB()
    results.Demarshal(msg)
    sub = xml.AddSubElement('NCB')
    sub.AddAttribute('ncb_command', '%i' % results.ncb_command)
    sub.AddAttribute('ncb_retcode', '%i' % results.ncb_retcode)
    sub.AddAttribute('ncb_lsn', '%i' % results.ncb_lsn)
    sub.AddAttribute('ncb_num', '%i' % results.ncb_num)
    sub.AddAttribute('ncb_rto', '%i' % results.ncb_rto)
    sub.AddAttribute('ncb_sto', '%i' % results.ncb_sto)
    sub.AddAttribute('ncb_lana_num', '%i' % results.ncb_lana_num)
    sub.AddAttribute('ncb_cmd_cplt', '%i' % results.ncb_cmd_cplt)
    subsub = sub.AddSubElement('CallName')
    subsub.SetText(results.ncb_callname)
    subsub = sub.AddSubElement('NCBName')
    subsub.SetText(results.ncb_name)


def _handleAdapter(xml, output, msg):
    results = ResultAdapter()
    results.Demarshal(msg)
    sub = xml.AddSubElement('Adapter')
    sub.AddAttribute('adapter_addr', '%02x.%02x.%02x.%02x.%02x.%02x' % (results.adapter_address[0],
     results.adapter_address[1],
     results.adapter_address[2],
     results.adapter_address[3],
     results.adapter_address[4],
     results.adapter_address[5]))
    sub.AddAttribute('adapter_type', '0x%x' % results.adapter_type)
    sub.AddAttribute('release', '%d.%d' % (results.rev_major, results.rev_minor))
    sub.AddAttribute('duration', '%u' % results.duration)
    sub.AddAttribute('name_count', '%u' % results.name_count)
    sub.AddAttribute('frame_recv', '%u' % results.frmr_recv)
    sub.AddAttribute('frame_xmit', '%u' % results.frmr_xmit)
    sub.AddAttribute('iframe_recv_err', '%u' % results.iframe_recv_err)
    sub.AddAttribute('xmit_aborts', '%u' % results.xmit_aborts)
    sub.AddAttribute('xmit_success', '%u' % results.xmit_success)
    sub.AddAttribute('recv_success', '%u' % results.recv_success)
    sub.AddAttribute('iframe_xmit_err', '%u' % results.iframe_xmit_err)
    sub.AddAttribute('recv_buff_unavail', '%u' % results.recv_buff_unavail)
    sub.AddAttribute('t1_timeouts', '%u' % results.t1_timeouts)
    sub.AddAttribute('ti_timeouts', '%u' % results.ti_timeouts)
    sub.AddAttribute('free_ncbs', '%u' % results.free_ncbs)
    sub.AddAttribute('max_dgram_size', '%u' % results.max_dgram_size)
    sub.AddAttribute('max_sess_pkt_size', '%u' % results.max_sess_pkt_size)
    sub.AddAttribute('pending_sess', '%u' % results.pending_sess)
    sub.AddAttribute('max_cfg_sess', '%u' % results.max_cfg_sess)
    sub.AddAttribute('max_cfg_ncbs', '%u' % results.max_cfg_ncbs)
    sub.AddAttribute('max_ncbs', '%u' % results.max_ncbs)
    sub.AddAttribute('xmit_buf_unavail', '%u' % results.xmit_buf_unavail)
    sub.AddAttribute('max_sess', '%u' % results.max_sess)
    i = 0
    while i < results.name_count:
        nameResults = ResultName()
        nameResults.Demarshal(msg)
        sub2 = sub.AddSubElement('Names')
        sub3 = sub2.AddSubElement('Type')
        sub3.SetText(_getNetbiosNameType(nameResults.type, nameResults.nameFlags, nameResults.networkName))
        sub3 = sub2.AddSubElement('NetName')
        sub3.SetText(_getNetName(nameResults.nameFlags))
        sub3 = sub2.AddSubElement('Name')
        sub3.SetText(nameResults.networkName)
        i = i + 1


def _getNetbiosError(error):
    if error == RESULT_NRC_GOODRET:
        return 'The operation succeeded'
    else:
        if error == RESULT_NRC_BUFLEN:
            return 'An illegal buffer length was supplied'
        if error == RESULT_NRC_ILLCMD:
            return 'An illegal command was supplied'
        if error == RESULT_NRC_CMDTMO:
            return 'The command timed out'
        if error == RESULT_NRC_INCOMP:
            return 'The message was incomplete. The application is to issue another command'
        if error == RESULT_NRC_BADDR:
            return 'The buffer address was illegal'
        if error == RESULT_NRC_SNUMOUT:
            return 'The session number was out of range'
        if error == RESULT_NRC_NORES:
            return 'No resource was available'
        if error == RESULT_NRC_SCLOSED:
            return 'The session was closed'
        if error == RESULT_NRC_CMDCAN:
            return 'The command was canceled'
        if error == RESULT_NRC_DUPNAME:
            return 'A duplicate name existed in the local name table'
        if error == RESULT_NRC_NAMTFUL:
            return 'The name table was full'
        if error == RESULT_NRC_ACTSES:
            return 'The command finished; the name has active sessions and is no longer registered'
        if error == RESULT_NRC_LOCTFUL:
            return 'The local session table was full'
        if error == RESULT_NRC_REMTFUL:
            return 'The remote session table was full. The request to open a session was rejected'
        if error == RESULT_NRC_ILLNN:
            return 'An illegal name number was specified'
        if error == RESULT_NRC_NOCALL:
            return 'The system did not find the name that was called'
        if error == RESULT_NRC_NOWILD:
            return 'Wildcards are not permitted in the ncb_name member'
        if error == RESULT_NRC_INUSE:
            return 'The name was already in use on the remote adapter'
        if error == RESULT_NRC_NAMERR:
            return 'The name was deleted'
        if error == RESULT_NRC_SABORT:
            return 'The session ended abnormally'
        if error == RESULT_NRC_NAMCONF:
            return 'A name conflict was detected'
        if error == RESULT_NRC_IFBUSY:
            return 'The interface was busy'
        if error == RESULT_NRC_TOOMANY:
            return 'Too many commands were outstanding; the application can retry the command later'
        if error == RESULT_NRC_BRIDGE:
            return 'The ncb_lana_num member did not specify a valid network number'
        if error == RESULT_NRC_CANOCCR:
            return 'The command finished while a cancel operation was occurring'
        if error == RESULT_NRC_CANCEL:
            return 'The NCBCANCEL command was not valid; the command was not canceled'
        if error == RESULT_NRC_DUPENV:
            return 'The name was defined by another local process'
        if error == RESULT_NRC_ENVNOTDEF:
            return 'The environment was not defined. A reset command must be issued'
        if error == RESULT_NRC_OSRESNOTAV:
            return 'Operating system resources were exhausted. The application can retry the command later'
        if error == RESULT_NRC_MAXAPPS:
            return 'The maximum number of applications was exceeded'
        if error == RESULT_NRC_NOSAPS:
            return 'No service access points (SAPs) were available for NetBIOS'
        if error == RESULT_NRC_NORESOURCES:
            return 'The requested resources were not available'
        if error == RESULT_NRC_INVADDRESS:
            return 'The NCB address was not valid'
        if error == RESULT_NRC_INVDDID:
            return 'The NCB DDID was invalid'
        if error == RESULT_NRC_LOCKFAIL:
            return 'The attempt to lock the user area failed'
        if error == RESULT_NRC_OPENERR:
            return 'An error occurred during an open operation being performed by the device driver. This error code is not part of the NetBIOS 3.0 specification'
        if error == RESULT_NRC_SYSTEM:
            return 'A system error occurred'
        if error == RESULT_NRC_PENDING:
            return 'An asynchronous operation is not yet finished'
        return 'Unknown netbios error'


def _getNetbiosNameType(type, flags, name):
    if len(name) == 0:
        return ''
    flags = flags & 128
    if type == 0:
        if name.startswith('IS~'):
            return 'Internet Information Server'
        else:
            if flags != 0:
                return 'Domain Name'
            return 'Workstation Service'

    elif type == 1:
        if flags != 0:
            return 'Master Browser'
        else:
            return 'Messenger Service'

    else:
        if type == 3:
            return 'Messenger Service'
        if type == 6:
            return 'RAS Server Service'
        if type == 27:
            return 'Domain Master Browser'
        if type == 28:
            if name.startswith('INet~'):
                return 'Internet Information Server'
            else:
                return 'Domain Controller'

        else:
            if type == 29:
                return 'Master Browser'
            if type == 30:
                return 'Browser Service Elections'
            if type == 31:
                return 'NetDDE Service'
            if type == 32:
                if name.startswith('Forte'):
                    return 'DCA IrmaLan Gateway Server Service'
                else:
                    return 'File Server Service'

            else:
                if type == 33:
                    return 'RAS Client Service'
                if type == 34:
                    return 'Microsoft Exchange Interchange'
                if type == 35:
                    return 'Microsoft Exchange Store'
                if type == 36:
                    return 'Microsoft Exchange Directory'
                if type == 43:
                    return 'Lotus Notes Server Service'
                if type == 47:
                    return 'Lotus Notes'
                if type == 48:
                    return 'Modem Sharing Server Service'
                if type == 49:
                    return 'Modem Sharing Client Service'
                if type == 51:
                    return 'Lotus Notes'
                if type == 67:
                    return 'SMS Administrators Remote Control Tool'
                if type == 68:
                    return 'SMS Clients Remote Control'
                if type == 69:
                    return 'SMS Clients Remote Chat'
                if type == 70:
                    return 'SMS Clients Remote Transfer'
                if type == 76:
                    return 'DEC Pathworks TCPIP Service'
                if type == 82:
                    return 'DEC Pathworks TCPIP Service'
                if type == 106:
                    return 'Microsoft Exchange IMC'
                if type == 135:
                    return 'Microsoft Exchange MTA'
                if type == 190:
                    return 'Network Monitor Agent'
                if type == 191:
                    return 'Network Monitor Application'
                return 'Unknown Type'


def _getNetName(flags):
    if flags == RESULT_UNIQUE_NAME:
        return 'UNIQUE'
    else:
        if flags == RESULT_REGISTERED:
            return 'UNIQUE REGISTERED'
        if flags == RESULT_DEREGISTERED:
            return 'UNIQUE DEREGISTRED'
        if flags == RESULT_DUPLICATE:
            return 'DUPLICATE'
        if flags == RESULT_DUPLICATE_DEREG:
            return 'DUPLICATE DEREGISTERED'
        if flags == RESULT_GROUP_NAME:
            return 'GROUP'
        if flags == RESULT_GROUP_NAME | RESULT_REGISTERED:
            return 'GROUP REGISTERED'
        if flags == RESULT_GROUP_NAME | RESULT_DEREGISTERED:
            return 'GROUP DEREGISTERED'
        if flags == RESULT_GROUP_NAME | RESULT_DUPLICATE:
            return 'GROUP DUPLICATE'
        if flags == RESULT_GROUP_NAME | RESULT_DUPLICATE_DEREG:
            return 'GRP DUP DEREG'
        return 'DK'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)