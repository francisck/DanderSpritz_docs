# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_SystemVersion_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.systemversion', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('SystemVersion', 'systemversion', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    result = Result()
    result.Demarshal(msg)
    xml.Start('SystemVersion')
    if mcl.os.archNames.has_key(result.arch):
        xml.AddAttribute('architecture', mcl.os.archNames[result.arch])
    else:
        xml.AddAttribute('architecture', 'unknown')
    xml.AddAttribute('architectureValue', '%u' % result.arch)
    if mcl.os.osNames.has_key(result.os):
        xml.AddAttribute('platform', mcl.os.osNames[result.os])
    else:
        xml.AddAttribute('platform', 'unknown')
    xml.AddAttribute('platformValue', '%u' % result.os)
    xml.AddAttribute('major', '%u' % result.majorVersion)
    xml.AddAttribute('minor', '%u' % result.minorVersion)
    xml.AddAttribute('revisionMajor', '%u' % result.revisionMajor)
    xml.AddAttribute('revisionMinor', '%u' % result.revisionMinor)
    xml.AddAttribute('build', '%u' % result.build)
    xml.AddSubElementWithText('ExtraInfo', result.extraInfo)
    if result.os == mcl.os.MCL_OS_WINNT or result.os == mcl.os.MCL_OS_WIN9X:
        sub = xml.AddSubElement('Flags')
        _addWindowsFlags(sub, result.flags)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
    return True


def _addWindowsFlags(xml, mask):
    xml.AddAttribute('value', '0x%08x' % mask)
    if mask & RESULT_WIN32_FLAG_DOMAIN_CONTROLLER:
        xml.AddSubElement('DomainController')
    if mask & RESULT_WIN32_FLAG_SERVER:
        xml.AddSubElement('Server')
    if mask & RESULT_WIN32_FLAG_WORKSTATION:
        xml.AddSubElement('Workstation')
    if mask & RESULT_WIN32_FLAG_BACKOFFICE:
        xml.AddSubElement('BackOffice')
    if mask & RESULT_WIN32_FLAG_BLADE:
        xml.AddSubElement('Blade')
    if mask & RESULT_WIN32_FLAG_CASE_DATACENTER:
        xml.AddSubElement('DataCenter')
    if mask & RESULT_WIN32_FLAG_CASE_ENTERPRISE:
        xml.AddSubElement('Enterprise')
    if mask & RESULT_WIN32_FLAG_EMBEDDEDNT:
        xml.AddSubElement('EmbeddedNT')
    if mask & RESULT_WIN32_FLAG_PERSONAL:
        xml.AddSubElement('Personal')
    if mask & RESULT_WIN32_FLAG_SINGLEUSERTS:
        xml.AddSubElement('SingleUserTS')
    if mask & RESULT_WIN32_FLAG_SMALLBUSINESS:
        xml.AddSubElement('SmallBusiness')
    if mask & RESULT_WIN32_FLAG_SMALLBUSINESS_RESTRICTED:
        xml.AddSubElement('SmallBusinessRestricted')
    if mask & RESULT_WIN32_FLAG_TERMINAL:
        xml.AddSubElement('Terminal')


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)