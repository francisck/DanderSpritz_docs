# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Users_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.users', globals())
    _AUTH_FLAGS = {RESULT_AUTH_FLAG_PRINT: 'AfOpPrint',
       RESULT_AUTH_FLAG_COMM: 'AfOpComm',
       RESULT_AUTH_FLAG_SERVER: 'AfOpServer',
       RESULT_AUTH_FLAG_ACCOUNTS: 'AfOpAccounts'
       }
    _USER_FLAGS = {RESULT_USER_FLAG_SCRIPT: 'UfScript',
       RESULT_USER_FLAG_ACCOUNTDISABLE: 'UfAccountDisable',
       RESULT_USER_FLAG_HOMEDIR_REQUIRED: 'UfHomedirRequired',
       RESULT_USER_FLAG_LOCKOUT: 'UfLockout',
       RESULT_USER_FLAG_PASSWD_NOTREQD: 'UfPasswdNotReqd',
       RESULT_USER_FLAG_PASSWD_CANT_CHANGE: 'UfPasswdCantChange',
       RESULT_USER_FLAG_ENCRYPTED_TEXT_PASSWORD_ALLOWED: 'UfEncryptedTextPasswordAllowed',
       RESULT_USER_FLAG_TEMP_DUPLICATE_ACCOUNT: 'UfTempDuplicateAccount',
       RESULT_USER_FLAG_NORMAL_ACCOUNT: 'UfNormalAccount',
       RESULT_USER_FLAG_INTERDOMAIN_TRUST_ACCOUNT: 'UfInterdomainTrustAccount',
       RESULT_USER_FLAG_WORKSTATION_TRUST_ACCOUNT: 'UfWorkstationTrustAccount',
       RESULT_USER_FLAG_SERVER_TRUST_ACCOUNT: 'UfServerTrustAccount',
       RESULT_USER_FLAG_DONT_EXPIRE_PASSWD: 'UfDontExpirePasswd',
       RESULT_USER_FLAG_SMARTCARD_REQUIRED: 'UfSmartCardRequired',
       RESULT_USER_FLAG_TRUSTED_FOR_DELEGATION: 'UfTrustedForDelegation',
       RESULT_USER_FLAG_NOT_DELEGATED: 'UfNotDelegated',
       RESULT_USER_FLAG_USE_DES_KEY_ONLY: 'UfUseDesKeyOnly',
       RESULT_USER_FLAG_DONT_REQUIRE_PREAUTH: 'UfDontRequirePreauth',
       RESULT_USER_FLAG_PASSWORD_EXPIRED: 'UfPasswordExpired',
       RESULT_USER_FLAG_TRUSTED_TO_AUTHENTICATE_FOR_DELEGATION: 'UfTrustedToAuthenticateForDelegation',
       RESULT_USER_FLAG_MNS_LOGON_ACCOUNT: 'UfMnsLogonAccount',
       RESULT_USER_FLAG_NO_AUTH_DATA_REQUIRED: 'UfNoAuthDataRequired',
       RESULT_USER_FLAG_PARTIAL_SECRETS_ACCOUNT: 'UfPartialSecretsAccount',
       RESULT_USER_FLAG_USE_AES_KEYS: 'UfUseAesKeys'
       }
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Users', 'users', [])
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
    xml.Start('Users')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        results = Result()
        try:
            results.Demarshal(msg)
        except:
            output.RecordXml(xml)
            output.RecordError('Returned data is invalid')
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False

        _handleUser(_USER_FLAGS, _AUTH_FLAGS, xml, results)

    output.RecordXml(xml)
    output.End()
    return True


def _getPrivText(privs):
    if privs == RESULT_PRIV_GUEST:
        return 'Guest'
    else:
        if privs == RESULT_PRIV_USER:
            return 'User'
        if privs == RESULT_PRIV_ADMIN:
            return 'Administrator'
        return 'Unknown'


def _handleUser(_USER_FLAGS, _AUTH_FLAGS, xml, info):
    sub = xml.AddSubElement('User')
    sub.AddAttribute('userId', '%u' % info.userId)
    sub.AddAttribute('primaryGroupId', '%u' % info.primaryGroupId)
    sub.AddSubElementWithText('Name', info.name)
    sub.AddSubElementWithText('Comment', info.comment)
    sub.AddSubElementWithText('FullName', info.fullName)
    sub.AddSubElementWithText('HomeDir', info.homeDir)
    sub.AddSubElementWithText('UserShell', info.userShell)
    if len(info.userShell) == 0:
        import mcl.object.MclTime
        if info.lastLogon.GetTimeType() == mcl.object.MclTime.MclTime.MCL_TIME_TYPE_NOT_A_TIME:
            sub.AddSubElement('NeverLoggedOn')
        else:
            sub.AddTimeElement('LastLogon', info.lastLogon)
        sub.AddAttribute('numLogons', '%i' % info.numLogons)
        if info.acctExpires.GetTimeType() == mcl.object.MclTime.MclTime.MCL_TIME_TYPE_NOT_A_TIME:
            sub.AddSubElement('AcctNeverExpires')
        else:
            sub.AddTimeElement('AcctExpires', info.acctExpires)
        sub.AddTimeElement('PasswdLastChanged', info.passwordLastChanged)
        if info.flags & RESULT_USER_FLAG_PASSWORD_EXPIRED:
            sub.AddAttribute('passwdExpired', 'true')
        else:
            sub.AddAttribute('passwdExpired', 'false')
        sub.AddSubElementWithText('Privilege', _getPrivText(info.privs))
        sub2 = sub.AddSubElement('Flags')
        sub3 = sub2.AddSubElement('AuthFlags')
        sub3.AddAttribute('mask', '0x%x' % info.authFlags)
        for AUTH_FLAG_VALUE in _AUTH_FLAGS.keys():
            if info.authFlags & AUTH_FLAG_VALUE:
                sub3.AddSubElement(_AUTH_FLAGS[AUTH_FLAG_VALUE])

        sub3 = sub2.AddSubElement('AccountFlags')
        sub3.AddAttribute('mask', '0x%x' % info.flags)
        for USER_FLAG_VALUE in _USER_FLAGS.keys():
            if info.flags & USER_FLAG_VALUE:
                sub3.AddSubElement(_USER_FLAGS[USER_FLAG_VALUE])


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)