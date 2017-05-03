# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_LogonAsUser_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.data.env
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.security.cmd.logonasuser', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('LogonAsUser', 'logonasuser', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    if msg.GetCount() == 0:
        mcl.data.env.SetValue(LP_ENV_PUT_COMPLETE, 'true')
        return True
    results = Result()
    results.Demarshal(msg)
    try:
        mcl.data.env.SetValue('_USER_%s' % results.user, '0x%08x' % results.hUser, globalValue=True)
    except:
        output.RecordError('Failed to set alias for user')

    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Logon')
    xml.AddAttribute('handle', '0x%08x' % results.hUser)
    if len(results.user) > 0:
        xml.AddAttribute('alias', results.user)
    if len(results.domain) > 0:
        xml.AddAttribute('domain', results.domain)
    output.RecordXml(xml)
    output.GoToBackground()
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