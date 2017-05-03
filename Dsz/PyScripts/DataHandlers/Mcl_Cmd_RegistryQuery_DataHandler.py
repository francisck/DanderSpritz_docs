# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_RegistryQuery_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.registryquery', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('RegistryQuery', 'registryquery', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.GetCount() == 0:
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('Keys')
        sub = None
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            key = msg.FindMessage(MSG_KEY_RESULT_KEY)
            keyinfo = KeyInfo()
            keyinfo.Demarshal(key)
            sub = xml.AddSubElement('Key')
            sub.AddAttribute('name', keyinfo.name)
            sub.AddAttribute('hive', _getHiveString(keyinfo.hive))
            sub.AddTimeElement('LastUpdate', keyinfo.lastUpdate)
            sub.AddAttribute('class', keyinfo.classValue)
            if keyinfo.flags & KEY_FLAG_ACCESS_DENIED:
                sub.AddAttribute('denied', 'true')
            for entry in key:
                if entry['retrieved']:
                    continue
                if entry['key'] == MSG_KEY_RESULT_SUBKEY:
                    subkey = Subkey()
                    subkey.Demarshal(key)
                    sub2 = sub.AddSubElement('Subkey')
                    sub2.AddAttribute('name', subkey.name)
                    sub2.AddTimeElement('LastUpdate', subkey.lastUpdate)
                elif entry['key'] == MSG_KEY_RESULT_VALUE:
                    value = Value()
                    value.Demarshal(key)
                    sub2 = sub.AddSubElement('Value')
                    sub2.AddAttribute('name', value.name)
                    sub2.AddAttribute('type', _getTypeString(value.type))
                    sub2.AddAttribute('typeValue', '0x%x' % value.nativeType)
                    rawSub = sub2.AddSubElement('Raw')
                    rawSub.SetTextAsData(value.data)
                    from mcl.object.Demarshaler import Demarshaler
                    demarsh = Demarshaler(value.data)
                    dataEndian = demarsh.LITTLE_ENDIAN
                    if value.type == VALUE_TYPE_REG_DWORD:
                        try:
                            dword = demarsh.GetU32(dataEndian)
                            sub2.AddSubElementWithText('Translated', '%u' % dword)
                        except:
                            pass

                    elif value.type == VALUE_TYPE_REG_DWORD_BIG_ENDIAN:
                        try:
                            dword = demarsh.GetU32(demarsh.BIG_ENDIAN)
                            sub2.AddSubElementWithText('Translated', '%u' % dword)
                        except:
                            pass

                    elif value.type == VALUE_TYPE_REG_QWORD:
                        try:
                            qword = demarsh.GetU64(dataEndian)
                            sub2.AddSubElementWithText('Translated', '%u' % qword)
                        except:
                            pass

                    elif value.type == VALUE_TYPE_REG_SZ or value.type == VALUE_TYPE_REG_EXPAND_SZ:
                        try:
                            if len(value.data) == 0:
                                str = ''
                            else:
                                if len(value.data) % 2:
                                    value.data.append(0)
                                cList = list()
                                i = 0
                                while i < len(value.data):
                                    if dataEndian == demarsh.BIG_ENDIAN:
                                        cList.append(unichr(value.data[i] << 8 | value.data[i + 1]))
                                    else:
                                        cList.append(unichr(value.data[i] | value.data[i + 1] << 8))
                                    i = i + 2
                                    while len(cList) > 0 and cList[len(cList) - 1] == u'\x00':
                                        del cList[len(cList) - 1]

                                    str = u''.join(cList).encode('utf-8', 'backslashreplace')

                            sub2.AddSubElementWithText('Translated', str)
                        except:
                            pass

                else:
                    output.RecordError('Unhandled item key (0x%08x)' % entry['key'])
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return True

        output.RecordXml(xml)
        output.End()
        return True


def _getHiveString(hive):
    if hive == HIVE_LOCAL_MACHINE:
        return 'HKEY_LOCAL_MACHINE'
    else:
        if hive == HIVE_CLASSES_ROOT:
            return 'HKEY_CLASSES_ROOT'
        if hive == HIVE_CURRENT_USER:
            return 'HKEY_CURRENT_USER'
        if hive == HIVE_CURRENT_CONFIG:
            return 'HKEY_CURRENT_CONFIG'
        if hive == HIVE_USERS:
            return 'HKEY_USERS'
        return 'HKEY_UNKNOWN'


def _getTypeString(type):
    if type == VALUE_TYPE_REG_SZ:
        return 'REG_SZ'
    else:
        if type == VALUE_TYPE_REG_EXPAND_SZ:
            return 'REG_EXPAND_SZ'
        if type == VALUE_TYPE_REG_BINARY:
            return 'REG_BINARY'
        if type == VALUE_TYPE_REG_DWORD:
            return 'REG_DWORD'
        if type == VALUE_TYPE_REG_DWORD_BIG_ENDIAN:
            return 'REG_DWORD_BIG_ENDIAN'
        if type == VALUE_TYPE_REG_LINK:
            return 'REG_LINK'
        if type == VALUE_TYPE_REG_MULTI_SZ:
            return 'REG_MULTI_SZ'
        if type == VALUE_TYPE_REG_RESOURCE_LIST:
            return 'REG_RESOURCE_LIST'
        if type == VALUE_TYPE_REG_FULL_RESOURCE_DESCRIPTOR:
            return 'REG_FULL_RESOURCE_DESCRIPTOR'
        if type == VALUE_TYPE_REG_RESOURCE_REQUIREMENTS_LIST:
            return 'REG_RESOURCE_REQUIREMENTS_LIST'
        if type == VALUE_TYPE_REG_QWORD:
            return 'REG_QWORD'
        if type == VALUE_TYPE_REG_NONE:
            return 'REG_NONE'
        return 'REG_NONE'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)