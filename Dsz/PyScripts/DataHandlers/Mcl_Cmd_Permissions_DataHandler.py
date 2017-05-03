# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Permissions_DataHandler.py
OBJECT_INHERIT_ACE = 1
CONTAINER_INHERIT_ACE = 2
NO_PROPAGATE_INHERIT_ACE = 4
INHERIT_ONLY_ACE = 8
INHERITED_ACE = 16
SUCCESSFUL_ACCESS_ACE_FLAG = 64
FAILED_ACCESS_ACE_FLAG = 128
FILE_READ_DATA = 1
FILE_WRITE_DATA = 2
FILE_APPEND_DATA = 4
FILE_READ_EA = 8
FILE_WRITE_EA = 16
FILE_EXECUTE = 32
FILE_DELETE_CHILD = 64
FILE_READ_ATTRIBUTES = 128
FILE_WRITE_ATTRIBUTES = 256
DELETE = 65536
READ_CONTROL = 131072
WRITE_DAC = 262144
WRITE_OWNER = 524288
SYNCHRONIZE = 1048576
GENERIC_ALL = 268435456
GENERIC_EXECUTE = 536870912
GENERIC_WRITE = 1073741824
GENERIC_READ = 2147483648L
EXECUTE_MASK = 1179808
GENERIC_READ_MASK = 1179785
GENERIC_WRITE_MASK = 1179926
FULL_CONTROL_MASK = 2032127
READ_WRITE_MASK = GENERIC_WRITE_MASK | GENERIC_READ_MASK
ACCESS_ALLOWED_ACE_TYPE = 0
ACCESS_DENIED_ACE_TYPE = 1
SYSTEM_AUDIT_ACE_TYPE = 2
SYSTEM_ALARM_ACE_TYPE = 3
ACCESS_ALLOWED_COMPOUND_ACE_TYPE = 4
ACCESS_ALLOWED_OBJECT_ACE_TYPE = 5
ACCESS_DENIED_OBJECT_ACE_TYPE = 6
SYSTEM_AUDIT_OBJECT_ACE_TYPE = 7
SYSTEM_ALARM_OBJECT_ACE_TYPE = 8
ACCESS_ALLOWED_CALLBACK_ACE_TYPE = 9
ACCESS_DENIED_CALLBACK_ACE_TYPE = 10
ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE = 11
ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE = 12
SYSTEM_AUDIT_CALLBACK_ACE_TYPE = 13
SYSTEM_ALARM_CALLBACK_ACE_TYPE = 14
SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE = 15
SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE = 16
SYSTEM_MANDATORY_LABEL_ACE_TYPE = 17

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.permissions', globals())
    ACE_FLAGS = {FAILED_ACCESS_ACE_FLAG: 'FailedAccessAce',
       SUCCESSFUL_ACCESS_ACE_FLAG: 'SuccessfulAccessAce',
       CONTAINER_INHERIT_ACE: 'ContainerInheritAce',
       INHERIT_ONLY_ACE: 'InheritOnlyAce',
       INHERITED_ACE: 'InheritedAce',
       NO_PROPAGATE_INHERIT_ACE: 'NoPropogateInheritAce',
       OBJECT_INHERIT_ACE: 'ObjectInheritAce'
       }
    ACE_MASKS = [
     (
      FULL_CONTROL_MASK, True, 'FullControlMask'),
     (
      GENERIC_ALL, True, 'FullControlMask'),
     (
      READ_WRITE_MASK, True, 'ReadWriteMask'),
     (
      GENERIC_WRITE_MASK, True, 'GenericWriteMask'),
     (
      GENERIC_WRITE, True, 'GenericWriteMask'),
     (
      GENERIC_READ_MASK, True, 'GenericReadMask'),
     (
      GENERIC_READ, True, 'GenericReadMask'),
     (
      GENERIC_EXECUTE, True, 'GenericExecuteMask'),
     (
      DELETE, False, 'Delete'),
     (
      WRITE_DAC, False, 'WriteDac'),
     (
      WRITE_OWNER, False, 'WriteOwner'),
     (
      EXECUTE_MASK, True, 'ExecuteMask'),
     (
      FILE_EXECUTE, False, 'FileExecute'),
     (
      FILE_READ_DATA, False, 'FileReadData'),
     (
      FILE_WRITE_DATA, False, 'FileWriteData'),
     (
      FILE_WRITE_EA, False, 'FileWriteEA'),
     (
      FILE_APPEND_DATA, False, 'FileAppendData'),
     (
      FILE_DELETE_CHILD, False, 'FileDeleteChild'),
     (
      FILE_READ_ATTRIBUTES, False, 'FileReadAttributes'),
     (
      FILE_WRITE_ATTRIBUTES, False, 'FileWriteAttributes'),
     (
      READ_CONTROL, False, 'ReadControl'),
     (
      SYNCHRONIZE, False, 'Synchronize'),
     (
      FILE_READ_EA, False, 'FileReadEA')]
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Permissions', 'permissions', [])
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
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['key'] == MSG_KEY_RESULT_QUERY:
            return _handleQuery(ACE_FLAGS, ACE_MASKS, msg, output)
        if entry['key'] == MSG_KEY_RESULT_MODIFY:
            return _handleModify(ACE_MASKS, msg, output)
        output.RecordError('Returned data key (%u) is invalid' % entry['key'])
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleModify(ACE_MASKS, msg, output):
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    result = ResultModify()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('AclModified')
    if result.flags & PARAMS_SET_FLAG_PERMANENT:
        xml.AddAttribute('removePending', 'false')
    else:
        xml.AddAttribute('removePending', 'true')
    _addAceAccessMask(ACE_MASKS, xml, result.accessMask)
    output.RecordXml(xml)
    if result.flags & PARAMS_SET_FLAG_PERMANENT == 0:
        output.GoToBackground()
    output.End()
    return True


def _handleQuery(ACE_FLAGS, ACE_MASKS, msg, output):
    qmsg = msg.FindMessage(MSG_KEY_RESULT_QUERY)
    owner = ResultQueryInfo()
    owner.Demarshal(qmsg)
    queryType = 'Unknown'
    if owner.type == TYPE_FILE:
        queryType = 'File'
    else:
        if owner.type == TYPE_REG_KEY:
            queryType = 'RegKey'
        elif owner.type == TYPE_GENERIC:
            if owner.objectType == 0:
                queryType = 'SE_UNKNOWN_OBJECT_TYPE'
            elif owner.objectType == 1:
                queryType = 'SE_FILE_OBJECT'
            elif owner.objectType == 2:
                queryType = 'SE_SERVICE'
            elif owner.objectType == 3:
                queryType = 'SE_PRINTER'
            elif owner.objectType == 4:
                queryType = 'SE_REGISTRY_KEY'
            elif owner.objectType == 5:
                queryType = 'SE_LMSHARE'
            elif owner.objectType == 6:
                queryType = 'SE_KERNEL_OBJECT'
            elif owner.objectType == 7:
                queryType = 'SE_WINDOW_OBJECT'
            elif owner.objectType == 8:
                queryType = 'SE_DS_OBJECT'
            elif owner.objectType == 9:
                queryType = 'SE_DS_OBJECT_ALL'
            elif owner.objectType == 10:
                queryType = 'SE_PROVIDER_DEFINED_OBJECT'
            elif owner.objectType == 11:
                queryType = 'SE_WMIGUID_OBJECT'
            elif owner.objectType == 12:
                queryType = 'SE_REGISTRY_WOW64_32KEY'
            else:
                queryType = 'UNKNOWN'
        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('ObjectPerms')
        xml.AddAttribute('type', queryType)
        xml.AddAttribute('name', owner.object)
        xml.AddAttribute('accountName', owner.account)
        xml.AddAttribute('accountDomainName', owner.acctDomain)
        xml.AddAttribute('groupName', owner.group)
        xml.AddAttribute('groupDomainName', owner.groupDomain)
        xml.AddSubElementWithText('PermissionString', owner.permString)
        sub = xml.AddSubElement('Flags')
        if owner.flags != 0:
            if owner.flags & RESULT_SD_FLAG_DACL_AUTO_INHERIT_REQ:
                sub.AddSubElement('SE_DACL_AUTO_INHERIT_REQ')
            if owner.flags & RESULT_SD_FLAG_DACL_AUTO_INHERITED:
                sub.AddSubElement('SE_DACL_AUTO_INHERITED')
            if owner.flags & RESULT_SD_FLAG_DACL_DEFAULTED:
                sub.AddSubElement('SE_DACL_DEFAULTED')
            if owner.flags & RESULT_SD_FLAG_DACL_PRESENT:
                sub.AddSubElement('SE_DACL_PRESENT')
            if owner.flags & RESULT_SD_FLAG_DACL_PROTECTED:
                sub.AddSubElement('SE_DACL_PROTECTED')
            if owner.flags & RESULT_SD_FLAG_GROUP_DEFAULTED:
                sub.AddSubElement('SE_GROUP_DEFAULTED')
            if owner.flags & RESULT_SD_FLAG_OWNER_DEFAULTED:
                sub.AddSubElement('SE_OWNER_DEFAULTED')
            if owner.flags & RESULT_SD_FLAG_RM_CONTROL_VALID:
                sub.AddSubElement('SE_RM_CONTROL_VALID')
            if owner.flags & RESULT_SD_FLAG_SACL_AUTO_INHERIT_REQ:
                sub.AddSubElement('SE_SACL_AUTO_INHERIT_REQ')
            if owner.flags & RESULT_SD_FLAG_SACL_AUTO_INHERITED:
                sub.AddSubElement('SE_SACL_AUTO_INHERITED')
            if owner.flags & RESULT_SD_FLAG_SACL_DEFAULTED:
                sub.AddSubElement('SE_SACL_DEFAULTED')
            if owner.flags & RESULT_SD_FLAG_SACL_PRESENT:
                sub.AddSubElement('SE_SACL_PRESENT')
            if owner.flags & RESULT_SD_FLAG_SACL_PROTECTED:
                sub.AddSubElement('SE_SACL_PROTECTED')
            if owner.flags & RESULT_SD_FLAG_SELF_RELATIVE:
                sub.AddSubElement('SE_SELF_RELATIVE')
        while qmsg.GetNumRetrieved() < qmsg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            ace = ResultAce()
            ace.Demarshal(qmsg)
            sub = xml.AddSubElement('Acl')
            if ace.aceType == RESULT_DACL_ACE:
                sub.AddAttribute('type', 'DACL')
            else:
                sub.AddAttribute('type', 'SACL')
            sub2 = sub.AddSubElement('Ace')
            sub2.AddAttribute('typeValue', '%u' % ace.type)
            sub2.AddAttribute('type', _getAceType(ace.type))
            sub2.AddAttribute('user', ace.user)
            sub2.AddAttribute('domain', ace.domain)
            _addAceFlags(ACE_FLAGS, sub2, ace.flags)
            _addAceAccessMask(ACE_MASKS, sub2, ace.accessMask)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _addAceFlags(ACE_FLAGS, xml, flags):
    sub = xml.AddSubElement('Flags')
    sub.AddAttribute('value', '0x%08x' % flags)
    for aceFlag in ACE_FLAGS.keys():
        if flags & aceFlag:
            sub.AddSubElement(ACE_FLAGS[aceFlag])
            flags &= ~aceFlag

    if flags:
        sub.AddAttribute('unknown', '0x%08x' % flags)


def _addAceAccessMask(ACE_MASKS, xml, accessMask):
    sub = xml.AddSubElement('Mask')
    sub.AddAttribute('value', '0x%08x' % accessMask)
    for aceMask in ACE_MASKS:
        match = False
        if aceMask[1]:
            if accessMask & aceMask[0] == aceMask[0]:
                match = True
        elif accessMask & aceMask[0]:
            match = True
        if match:
            sub.AddSubElement(aceMask[2])
            accessMask &= ~aceMask[0]

    if accessMask:
        sub.AddAttribute('unknown', '0x%08x' % accessMask)


def _getAceType(aceType):
    if aceType == ACCESS_ALLOWED_ACE_TYPE:
        return 'ACCESS_ALLOWED_ACE_TYPE'
    else:
        if aceType == ACCESS_DENIED_ACE_TYPE:
            return 'ACCESS_DENIED_ACE_TYPE'
        if aceType == SYSTEM_AUDIT_ACE_TYPE:
            return 'SYSTEM_AUDIT_ACE_TYPE'
        if aceType == SYSTEM_ALARM_ACE_TYPE:
            return 'SYSTEM_ALARM_ACE_TYPE'
        if aceType == ACCESS_ALLOWED_COMPOUND_ACE_TYPE:
            return 'ACCESS_ALLOWED_COMPOUND_ACE_TYPE'
        if aceType == ACCESS_ALLOWED_OBJECT_ACE_TYPE:
            return 'ACCESS_ALLOWED_OBJECT_ACE_TYPE'
        if aceType == ACCESS_DENIED_OBJECT_ACE_TYPE:
            return 'ACCESS_DENIED_OBJECT_ACE_TYPE'
        if aceType == SYSTEM_AUDIT_OBJECT_ACE_TYPE:
            return 'SYSTEM_AUDIT_OBJECT_ACE_TYPE'
        if aceType == SYSTEM_ALARM_OBJECT_ACE_TYPE:
            return 'SYSTEM_ALARM_OBJECT_ACE_TYPE'
        if aceType == ACCESS_ALLOWED_CALLBACK_ACE_TYPE:
            return 'ACCESS_ALLOWED_CALLBACK_ACE_TYPE'
        if aceType == ACCESS_DENIED_CALLBACK_ACE_TYPE:
            return 'ACCESS_DENIED_CALLBACK_ACE_TYPE'
        if aceType == ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE:
            return 'ACCESS_ALLOWED_CALLBACK_OBJECT_ACE_TYPE'
        if aceType == ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE:
            return 'ACCESS_DENIED_CALLBACK_OBJECT_ACE_TYPE'
        if aceType == SYSTEM_AUDIT_CALLBACK_ACE_TYPE:
            return 'SYSTEM_AUDIT_CALLBACK_ACE_TYPE'
        if aceType == SYSTEM_ALARM_CALLBACK_ACE_TYPE:
            return 'SYSTEM_ALARM_CALLBACK_ACE_TYPE'
        if aceType == SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE:
            return 'SYSTEM_AUDIT_CALLBACK_OBJECT_ACE_TYPE'
        if aceType == SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE:
            return 'SYSTEM_ALARM_CALLBACK_OBJECT_ACE_TYPE'
        if aceType == SYSTEM_MANDATORY_LABEL_ACE_TYPE:
            return 'SYSTEM_MANDATORY_LABEL_ACE_TYPE'
        return 'UNKNOWN_ACE_TYPE'


if __name__ == '__main__':
    import sys
    try:
        InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(InputFilename, OutputFilename) != True:
        sys.exit(-1)