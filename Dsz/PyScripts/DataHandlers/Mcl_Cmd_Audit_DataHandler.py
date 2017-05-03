# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Audit_DataHandler.py
import array
AUDIT_CATEGORIES = [
 (
  array.array('B', (105, 151, 152, 72, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System'),
 (
  array.array('B', (105, 151, 152, 73, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon'),
 (
  array.array('B', (105, 151, 152, 74, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess'),
 (
  array.array('B', (105, 151, 152, 75, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PrivilegeUse'),
 (
  array.array('B', (105, 151, 152, 76, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DetailedTracking'),
 (
  array.array('B', (105, 151, 152, 77, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange'),
 (
  array.array('B', (105, 151, 152, 78, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement'),
 (
  array.array('B', (105, 151, 152, 79, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DirectoryServiceAccess'),
 (
  array.array('B', (105, 151, 152, 80, 121, 122, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountLogon'),
 (
  array.array('B', (12, 206, 146, 16, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System_SecurityStateChange'),
 (
  array.array('B', (12, 206, 146, 17, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System_SecuritySubsystemExtension'),
 (
  array.array('B', (12, 206, 146, 18, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System_Integrity'),
 (
  array.array('B', (12, 206, 146, 19, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System_IPSecDriverEvents'),
 (
  array.array('B', (12, 206, 146, 20, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'System_Others'),
 (
  array.array('B', (12, 206, 146, 21, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_Logon'),
 (
  array.array('B', (12, 206, 146, 22, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_Logoff'),
 (
  array.array('B', (12, 206, 146, 23, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_AccountLockout'),
 (
  array.array('B', (12, 206, 146, 24, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_IPSecMainMode'),
 (
  array.array('B', (12, 206, 146, 25, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_IPSecQuickMode'),
 (
  array.array('B', (12, 206, 146, 26, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_IPSecUserMode'),
 (
  array.array('B', (12, 206, 146, 27, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_SpecialLogon'),
 (
  array.array('B', (12, 206, 146, 28, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_Others'),
 (
  array.array('B', (12, 206, 146, 29, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_FileSystem'),
 (
  array.array('B', (12, 206, 146, 30, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Registry'),
 (
  array.array('B', (12, 206, 146, 31, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Kernel'),
 (
  array.array('B', (12, 206, 146, 32, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Sam'),
 (
  array.array('B', (12, 206, 146, 33, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_CertificationServices'),
 (
  array.array('B', (12, 206, 146, 34, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_ApplicationGenerated'),
 (
  array.array('B', (12, 206, 146, 35, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Handle'),
 (
  array.array('B', (12, 206, 146, 36, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Share'),
 (
  array.array('B', (12, 206, 146, 37, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_FirewallPacketDrops'),
 (
  array.array('B', (12, 206, 146, 38, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_FirewallConnection'),
 (
  array.array('B', (12, 206, 146, 39, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_Other'),
 (
  array.array('B', (12, 206, 146, 40, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PrivilegeUse_Sensitive'),
 (
  array.array('B', (12, 206, 146, 41, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PrivilegeUse_NonSensitive'),
 (
  array.array('B', (12, 206, 146, 42, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PrivilegeUse_Others'),
 (
  array.array('B', (12, 206, 146, 43, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DetailedTracking_ProcessCreation'),
 (
  array.array('B', (12, 206, 146, 44, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DetailedTracking_ProcessTermination'),
 (
  array.array('B', (12, 206, 146, 45, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DetailedTracking_DpapiActivity'),
 (
  array.array('B', (12, 206, 146, 46, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DetailedTracking_RpcCall'),
 (
  array.array('B', (12, 206, 146, 47, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_AuditPolicy'),
 (
  array.array('B', (12, 206, 146, 48, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_AuthenticationPolicy'),
 (
  array.array('B', (12, 206, 146, 49, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_AuthorizationPolicy'),
 (
  array.array('B', (12, 206, 146, 50, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_MpsscvRulePolicy'),
 (
  array.array('B', (12, 206, 146, 51, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_WfpIPSecPolicy'),
 (
  array.array('B', (12, 206, 146, 52, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'PolicyChange_Others'),
 (
  array.array('B', (12, 206, 146, 53, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_UserAccount'),
 (
  array.array('B', (12, 206, 146, 54, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_ComputerAccount'),
 (
  array.array('B', (12, 206, 146, 55, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_SecurityGroup'),
 (
  array.array('B', (12, 206, 146, 56, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_DistributionGroup'),
 (
  array.array('B', (12, 206, 146, 57, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_ApplicationGroup'),
 (
  array.array('B', (12, 206, 146, 58, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountManagement_Others'),
 (
  array.array('B', (12, 206, 146, 59, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DSAccess_DSAccess'),
 (
  array.array('B', (12, 206, 146, 60, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'DsAccess_AdAuditChanges'),
 (
  array.array('B', (12, 206, 146, 61, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Ds_Replication'),
 (
  array.array('B', (12, 206, 146, 62, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Ds_DetailedReplication'),
 (
  array.array('B', (12, 206, 146, 63, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountLogon_CredentialValidation'),
 (
  array.array('B', (12, 206, 146, 64, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountLogon_Kerberos'),
 (
  array.array('B', (12, 206, 146, 65, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountLogon_Others'),
 (
  array.array('B', (12, 206, 146, 66, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'AccountLogon_KerbCredentialValidation'),
 (
  array.array('B', (12, 206, 146, 67, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'Logon_NPS'),
 (
  array.array('B', (12, 206, 146, 68, 105, 174, 17, 217, 190, 211, 80, 80, 84, 80, 48,
                  48)), 'ObjectAccess_DetailedFileShare')]

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.audit', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Audit', 'audit', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_PATCH_FAILED:
            import mcl.hiding.errors.audit
            output.RecordModuleError(moduleError, 0, errorStrings)
            output.RecordModuleError(osError, 0, mcl.hiding.errors.audit.errorStrings)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.AUDIT_MODIFY:
            return _handleAuditModifyData(msg, output)
        if input.GetMessageType() == mcl.msgtype.AUDIT_QUERY:
            return _handleAuditQueryData(msg, output)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleAuditModifyData(msg, output):
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('TurnedOff')
    output.RecordXml(xml)
    output.GoToBackground()
    output.End()
    return True


def _handleAuditQueryData(msg, output):
    results = ResultAuditStatus()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Status')
    if results.auditingEnabled:
        xml.AddAttribute('current', 'ON')
    else:
        xml.AddAttribute('current', 'OFF')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        eventResults = ResultCategory()
        eventResults.Demarshal(msg)
        sub = xml.AddSubElement('Event')
        if eventResults.flags & RESULT_FLAG_AUDIT_ONSUCCESS:
            sub.AddSubElement('OnSuccess')
        if eventResults.flags & RESULT_FLAG_AUDIT_ONFAILURE:
            sub.AddSubElement('OnFailure')
        category = _lookupName(eventResults.categoryGuid)
        subcategory = _lookupName(eventResults.subcategoryGuid)
        sub.AddAttribute('categoryGUID', '%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x%02x%02x' % (
         eventResults.categoryGuid[0], eventResults.categoryGuid[1], eventResults.categoryGuid[2], eventResults.categoryGuid[3],
         eventResults.categoryGuid[4], eventResults.categoryGuid[5], eventResults.categoryGuid[6], eventResults.categoryGuid[7],
         eventResults.categoryGuid[8], eventResults.categoryGuid[9], eventResults.categoryGuid[10], eventResults.categoryGuid[11],
         eventResults.categoryGuid[12], eventResults.categoryGuid[13], eventResults.categoryGuid[14], eventResults.categoryGuid[15]))
        sub.AddAttribute('subcategoryGUID', '%02x%02x%02x%02x-%02x%02x-%02x%02x-%02x%02x%02x%02x%02x%02x%02x%02x' % (
         eventResults.subcategoryGuid[0], eventResults.subcategoryGuid[1], eventResults.subcategoryGuid[2], eventResults.subcategoryGuid[3],
         eventResults.subcategoryGuid[4], eventResults.subcategoryGuid[5], eventResults.subcategoryGuid[6], eventResults.subcategoryGuid[7],
         eventResults.subcategoryGuid[8], eventResults.subcategoryGuid[9], eventResults.subcategoryGuid[10], eventResults.subcategoryGuid[11],
         eventResults.subcategoryGuid[12], eventResults.subcategoryGuid[13], eventResults.subcategoryGuid[14], eventResults.subcategoryGuid[15]))
        sub.AddAttribute('category', category)
        sub.AddAttribute('categoryNative', eventResults.category)
        if len(eventResults.subcategory) > 0:
            sub.AddAttribute('subcategory', subcategory)
            sub.AddAttribute('subcategoryNative', eventResults.subcategory)

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _lookupName(categoryGuid):
    for category in AUDIT_CATEGORIES:
        if category[0] == categoryGuid:
            return category[1]

    return ''


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)