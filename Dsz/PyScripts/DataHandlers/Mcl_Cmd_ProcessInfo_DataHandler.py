# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_ProcessInfo_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.process.cmd.processinfo', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('ProcessInfo', 'processinfo', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        results = ProcessResult()
        results.Demarshal(msg)
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('ProcessInfo')
        xml.AddAttribute('id', '%i' % results.id)
        rtn = mcl.target.CALL_SUCCEEDED
        sub = None
        for entry in msg:
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            if entry['retrieved']:
                continue
            if entry['key'] == MSG_KEY_RESULT_PROCESS_BASIC_INFO:
                info = ProcessBasicInfoResult()
                try:
                    info.Demarshal(msg)
                except:
                    output.RecordXml(xml)
                    output.RecordError('Returned data is invalid')
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return True

                _handleBasicInfo(xml.AddSubElement('BasicInfo'), info)
            elif entry['key'] == MSG_KEY_RESULT_TOKENS:
                sub = xml.AddSubElement('Groups')
                submsg = msg.FindMessage(MSG_KEY_RESULT_TOKENS)
                while submsg.GetNumRetrieved() < submsg.GetCount():
                    info = TokenResult()
                    try:
                        info.Demarshal(submsg)
                    except:
                        output.RecordXml(xml)
                        output.RecordError('Returned data is invalid')
                        output.EndWithStatus(mcl.target.CALL_FAILED)
                        return True

                    _handleTokenInfo(sub.AddSubElement('Group'), info)

            elif entry['key'] == MSG_KEY_RESULT_PRIVILEGES:
                sub = xml.AddSubElement('Privileges')
                submsg = msg.FindMessage(MSG_KEY_RESULT_PRIVILEGES)
                while submsg.GetNumRetrieved() < submsg.GetCount():
                    info = PrivilegeResult()
                    try:
                        info.Demarshal(submsg)
                    except:
                        output.RecordXml(xml)
                        output.RecordError('Returned data is invalid')
                        output.EndWithStatus(mcl.target.CALL_FAILED)
                        return True

                    _handlePrivilege(sub.AddSubElement('Privilege'), info)

            elif entry['key'] == MSG_KEY_RESULT_MODULES:
                sub = xml.AddSubElement('Modules')
                submsg = msg.FindMessage(MSG_KEY_RESULT_MODULES)
                while submsg.GetNumRetrieved() < submsg.GetCount():
                    moduleMsg = submsg.FindMessage(MSG_KEY_RESULT_MODULE)
                    info = ModuleResult()
                    try:
                        info.Demarshal(moduleMsg)
                    except:
                        output.RecordXml(xml)
                        output.RecordError('Returned data is invalid')
                        output.EndWithStatus(mcl.target.CALL_FAILED)
                        return True

                    sub2 = sub.AddSubElement('Module')
                    _handleModule(sub2, info)
                    while moduleMsg.GetNumRetrieved() < moduleMsg.GetCount():
                        hash = HashResult()
                        try:
                            hash.Demarshal(moduleMsg)
                        except:
                            output.RecordXml(xml)
                            output.RecordError('Returned data is invalid')
                            output.EndWithStatus(mcl.target.CALL_FAILED)
                            return True

                        sub3 = sub2.AddSubElement('Checksum')
                        if hash.hashType == RESULT_HASH_TYPE_MD5:
                            sub3.AddAttribute('type', 'MD5')
                        elif hash.hashType == RESULT_HASH_TYPE_SHA1:
                            sub3.AddAttribute('type', 'SHA1')
                        elif hash.hashType == RESULT_HASH_TYPE_SHA256:
                            sub3.AddAttribute('type', 'SHA256')
                        elif hash.hashType == RESULT_HASH_TYPE_SHA512:
                            sub3.AddAttribute('type', 'SHA512')
                        else:
                            sub3.AddAttribute('type', 'unknown')
                        sub3.SetTextAsData(hash.hash)

            elif entry['key'] == mcl.object.Message.MSG_KEY_RESULT_ERROR:
                try:
                    errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
                    moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
                    osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
                except:
                    output.RecordXml(xml)
                    output.RecordError('Returned data is invalid')
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return True

                if errorStrings.has_key(moduleError):
                    moduleStr = errorStrings[moduleError]
                else:
                    moduleStr = 'Unknown module error (0x%08x)' % moduleError
                osStr = output.TranslateOsError(osError)
                sub = xml.AddSubElement('Errors')
                sub2 = sub.AddSubElement('ModuleError')
                sub2.AddAttribute('value', '%u' % moduleError)
                sub2.SetText(moduleStr)
                sub = sub.AddSubElement('OsError')
                sub2.AddAttribute('value', '%u' % osError)
                sub2.SetText(osStr)
                rtn = mcl.target.CALL_FAILED
            else:
                output.RecordXml(xml)
                output.RecordError('Returned key (0x%08x) is invalid' % entry['key'])
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return True

        output.RecordXml(xml)
        output.EndWithStatus(rtn)
        return True


def _getUseType(type):
    if type == RESULT_TOKEN_TYPE_INVALID:
        return 'Invalid'
    else:
        if type == RESULT_TOKEN_TYPE_USER:
            return 'User'
        if type == RESULT_TOKEN_TYPE_GROUP:
            return 'Group'
        if type == RESULT_TOKEN_TYPE_DOMAIN:
            return 'Domain'
        if type == RESULT_TOKEN_TYPE_ALIAS:
            return 'Alias'
        if type == RESULT_TOKEN_TYPE_WELLKNOWN_GROUP:
            return 'Well Known Group'
        if type == RESULT_TOKEN_TYPE_DELETED_ACCOUNT:
            return 'Deleted Account'
        if type == RESULT_TOKEN_TYPE_UNKNOWN:
            return 'Unknown'
        if type == RESULT_TOKEN_TYPE_COMPUTER:
            return 'Computer'
        return 'Non-matching Type'


def _handleBasicInfo(sub, info):
    _handleTokenInfo(sub.AddSubElement('User'), info.user)
    _handleTokenInfo(sub.AddSubElement('Owner'), info.owner)
    _handleTokenInfo(sub.AddSubElement('Group'), info.group)


def _handleModule(sub, info):
    sub.AddAttribute('name', info.name)
    sub.AddAttribute('baseAddress', '0x%08x' % info.baseAddress)
    sub.AddAttribute('entryPoint', '0x%08x' % info.entryPoint)
    sub.AddAttribute('imageSize', '0x%08x' % info.imageSize)


def _handlePrivilege(sub, info):
    sub.AddAttribute('name', info.name)
    sub.AddAttribute('attributes', '0x%08x' % info.attributes)
    if info.attributes & RESULT_PRIV_ATTRIBUTE_ENABLED_BY_DEFAULT:
        sub.AddSubElement('SE_PRIVILEGE_ENABLED_BY_DEFAULT')
    if info.attributes & RESULT_PRIV_ATTRIBUTE_ENABLED:
        sub.AddSubElement('SE_PRIVILEGE_ENABLED')
    if info.attributes & RESULT_PRIV_ATTRIBUTE_REMOVED:
        sub.AddSubElement('SE_PRIVILEGE_REMOVED')
    if info.attributes & RESULT_PRIV_ATTRIBUTE_USED_FOR_ACCESS:
        sub.AddSubElement('SE_PRIVILEGE_USED_FOR_ACCESS')


def _handleTokenInfo(sub, info):
    sub.AddAttribute('name', info.name)
    sub.AddAttribute('attributes', '0x%08x' % info.attributes)
    sub.AddAttribute('type', _getUseType(info.type))
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_MANDATORY:
        sub.AddSubElement('SE_GROUP_MANDATORY')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_ENABLED_BY_DEFAULT:
        sub.AddSubElement('SE_GROUP_ENABLED_BY_DEFAULT')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_ENABLED:
        sub.AddSubElement('SE_GROUP_ENABLED')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_OWNER:
        sub.AddSubElement('SE_GROUP_OWNER')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_USE_FOR_DENY_ONLY:
        sub.AddSubElement('SE_GROUP_USE_FOR_DENY_ONLY')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_LOGON_ID:
        sub.AddSubElement('SE_GROUP_LOGON_ID')
    if info.attributes & RESULT_TOKEN_ATTRIBUTE_RESOURCE:
        sub.AddSubElement('SE_GROUP_RESOURCE')


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)