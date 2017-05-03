# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz

def Echo(str):
    dsz.ui.Echo(str, checkForStop=False)


def EchoError(str):
    dsz.ui.Echo(str, dsz.ERROR, checkForStop=False)


def EchoGood(str):
    dsz.ui.Echo(str, dsz.GOOD, checkForStop=False)


def EchoWarning(str):
    dsz.ui.Echo(str, dsz.WARNING, checkForStop=False)


def GetContext():
    import array
    import dsz.env
    import dsz.script
    from mcl.object.CpAddress import CpAddress
    import mcl.object.TaskId
    context = {}
    context['taskid'] = array.array('B', mcl.object.TaskId.TaskId.StrToIntArray(dsz.script.Env['script_task_id']))
    context['srcAddr'] = CpAddress(CpAddress.DottedToInt(dsz.script.Env['local_address']))
    context['dstAddr'] = CpAddress(CpAddress.DottedToInt(dsz.script.Env['target_address']))
    context['user'] = dsz.script.Env['script_user']
    context['fastExfil'] = True
    if dsz.env.Check('_DisableWow64', int(dsz.script.Env['script_command_id'])):
        value = dsz.env.Get('_DisableWow64', int(dsz.script.Env['script_command_id'])).lower()
    else:
        value = 'false'
    if value == 'true' or value == '1' or value == 'yes' or value == 'on':
        context['disableWow64'] = True
    else:
        context['disableWow64'] = False
    return context


def GetFramework():
    import dsz.env
    import dsz.script
    if dsz.env.Check('rpcFramework', int(dsz.script.Env['script_command_id'])):
        return dsz.env.Get('rpcFramework', int(dsz.script.Env['script_command_id']))
    else:
        return 'dsz'


def GetParameters():
    _TASKING_TYPE_STRING = 1
    _TASKING_TYPE_UINT_8 = 2
    _TASKING_TYPE_UINT_16 = 3
    _TASKING_TYPE_UINT_32 = 4
    _TASKING_TYPE_INT_8 = 5
    _TASKING_TYPE_INT_16 = 6
    _TASKING_TYPE_INT_32 = 7
    _TASKING_TYPE_BOOL = 8
    _TASKING_TYPE_UINT_64 = 9
    _TASKING_TYPE_INT_64 = 10
    _TASKING_TYPE_BYTE_ARRAY = 12
    _TASKING_TYPE_DATE_TIME = 13
    _TASKING_TYPE_IPV4ADDR = 14
    _TASKING_TYPE_TIME = 15
    _TASKING_TYPE_IPV6ADDR = 16
    _TASKING_TYPE_IPADDR = 17
    _TASKING_TYPE_CPADDR = 18
    _TASKING_TYPE_CPCIDR = 19
    import _dsz
    import array
    import mcl.object.Demarshaler
    import mcl.object.CpAddress
    import mcl.object.IpAddr
    import mcl.object.Utl_Time
    import socket
    data, dataTypes = _dsz.dszObj.dsz_task_get_data()
    aData = array.array('B')
    for item in data:
        aData.append(item)

    demarsh = mcl.object.Demarshaler.Demarshaler(aData)
    params = dict()
    i = 0
    while i < len(dataTypes):
        name, typeValue = dataTypes[i]
        if typeValue == _TASKING_TYPE_STRING:
            offset = _GetU32(demarsh)
            if offset == 0:
                params[name] = None
            else:
                j = offset + 2
                cList = list()
                while aData[j] != 0:
                    cList.append(chr(aData[j]))
                    j = j + 1

                params[name] = ''.join(cList)
        elif typeValue == _TASKING_TYPE_UINT_8:
            params[name] = demarsh.GetU8()
        elif typeValue == _TASKING_TYPE_UINT_16:
            params[name] = _GetU16(demarsh)
        elif typeValue == _TASKING_TYPE_UINT_32:
            params[name] = _GetU32(demarsh)
        elif typeValue == _TASKING_TYPE_UINT_64:
            params[name] = _GetU64(demarsh)
        elif typeValue == _TASKING_TYPE_INT_8:
            params[name] = demarsh.GetS8()
        elif typeValue == _TASKING_TYPE_INT_16:
            params[name] = _GetS16(demarsh)
        elif typeValue == _TASKING_TYPE_INT_32:
            params[name] = _GetS32(demarsh)
        elif typeValue == _TASKING_TYPE_INT_64:
            params[name] = _GetS64(demarsh)
        elif typeValue == _TASKING_TYPE_BOOL:
            params[name] = demarsh.GetBool()
        elif typeValue == _TASKING_TYPE_TIME or typeValue == _TASKING_TYPE_DATE_TIME:
            seconds = _GetS64(demarsh)
            nanoseconds = _GetU64(demarsh)
            type = demarsh.GetU8()
            demarsh.GetData(7, 0)
            params[name] = mcl.object.MclTime.MclTime(seconds, nanoseconds, type)
        elif typeValue == _TASKING_TYPE_IPADDR:
            type = _GetU32(demarsh)
            if type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4:
                addr = demarsh.GetU32()
                demarsh.GetData(16, 0)
            elif type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
                addr = demarsh.GetData(16, 0)
                scope_id = _GetU32(demarsh)
            else:
                raise RuntimeError('Demarshal of IpAddr type returned unexpected value (%u)' % type)
            ipaddr = mcl.object.IpAddr.IpAddr()
            ipaddr.SetAddr(type, addr)
            if type == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6:
                ipaddr.SetScopeId(scope_id)
            params[name] = ipaddr
        elif typeValue == _TASKING_TYPE_IPV4ADDR:
            addr = demarsh.GetU32()
            ipaddr = mcl.object.IpAddr.IpAddr()
            ipaddr.SetAddr(mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4, addr)
            params[name] = ipaddr
        elif typeValue == _TASKING_TYPE_IPV6ADDR:
            addr = demarsh.GetData(16, 0)
            scope_id = _GetU32(demarsh)
            ipaddr = mcl.object.IpAddr.IpAddr()
            ipaddr.SetAddr(mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV6, addr)
            ipaddr.SetScopeId(scope_id)
            params[name] = ipaddr
        elif typeValue == _TASKING_TYPE_CPADDR:
            params[name] = mcl.object.CpAddress.CpAddress(_GetU32(demarsh))
        elif typeValue == _TASKING_TYPE_CPCIDR:
            addr = _GetU32(demarsh)
            mask = _GetU32(demarsh)
            params[name] = mcl.object.CpAddress.CpCidrAddress(addr, mask)
        elif typeValue == _TASKING_TYPE_BYTE_ARRAY:
            offset = _GetU32(demarsh)
            if offset == 0:
                params[name] = None
            else:
                bArray = array.array('B')
                arrayLen = socket.ntohl(aData[offset] << 24 | aData[offset + 1] << 16 | aData[offset + 2] << 8 | aData[offset + 3])
                j = offset + 4
                while j < offset + 4 + arrayLen:
                    bArray.append(aData[j])
                    j = j + 1

                params[name] = bArray
        else:
            raise RuntimeError('Unhandled parameter type (%d) for %s' % (typeValue, name))
        i = i + 1

    return params


def GetProcedureNumber():
    import sys
    import re
    procedure = 0
    for arg in sys.argv:
        matchObj = re.match('procedure=(.*)', arg)
        if matchObj != None:
            procedure = int(matchObj.group(1))

    return procedure


def OutputError(str):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('ErrorString')
    xml.SetText(str)
    OutputXml(xml)


def OutputXml(xml):
    import _dsz
    import mcl_platform
    mcl_platform.TransferXmlToCore(xml)
    _dsz.dszObj.xml_store()


def RecordModuleError(moduleError, osError, errorStrings={}, translateOsError=True, osErrorStrings=None, translateMclStatusError=True):
    import mcl.data.Output
    output = mcl.data.Output.DszDataHandlerOutput(None)
    output.RecordModuleError(moduleError, osError, errorStrings, translateOsError=translateOsError, osErrorStrings=osErrorStrings, translateMclStatusError=translateMclStatusError)
    return


def RpcPerformCall(rpcInfo, wait=False):
    import _dsz
    if _dsz.dszObj.check_for_stop():
        import sys
        sys.exit(-1)
    if wait:
        waitInfo = 1
    else:
        waitInfo = 0
    if rpcInfo.taskInfo_disable:
        taskInfoDisable = 1
    else:
        taskInfoDisable = 0
    if rpcInfo.messagingType.lower() == 'message':
        mclMessaging = 1
    else:
        mclMessaging = 0
    if rpcInfo.data == None:
        data = None
    else:
        data = bytearray(rpcInfo.data)
    if rpcInfo.dest == None:
        dest = 0
    else:
        dest = rpcInfo.dest
    return _dsz.dszObj.dsz_task_perform_rpc(rpcInfo.framework, dest, rpcInfo.apiValues, data, waitInfo, taskInfoDisable, mclMessaging)


def TaskGoToBackground():
    import _dsz
    _dsz.dszObj.go_to_background()


def TaskSetStatus(status):
    import _dsz
    rtn = _dsz.dszObj.dsz_dh_set_status(status)
    if rtn != 0:
        raise RuntimeError('Failed to set command status')


def _GetU16(demarsh):
    import socket
    return socket.ntohs(demarsh.GetU16())


def _GetU32(demarsh):
    import socket
    return socket.ntohl(demarsh.GetU32())


def _GetU64(demarsh):
    import socket
    val1 = socket.ntohl(demarsh.GetU32())
    val2 = socket.ntohl(demarsh.GetU32())
    return val2 << 32 | val1


def _GetS16(demarsh):
    val = _GetU16(demarsh)
    if val & 32768:
        val = (val & 32767) - 32768
    return val


def _GetS32(demarsh):
    import socket
    val = socket.ntohl(demarsh.GetU32())
    if val & 2147483648L:
        val = (val & 2147483647) - 2147483648L
    return val


def _GetS64(demarsh):
    import socket
    val1 = socket.ntohl(demarsh.GetU32())
    val2 = socket.ntohl(demarsh.GetU32())
    fullVal = val2 << 32 | val1
    if fullVal & 9223372036854775808L:
        fullVal = (fullVal & 9223372036854775807L) - 9223372036854775808L
    return fullVal