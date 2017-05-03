# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_RegistryHive_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.survey.cmd.registryhive', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.registryhive.types', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('RegistryHive', 'registryhive', [])
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
    xml.Start('CommandAction')
    hive = ResultHive()
    hive.Demarshal(msg)
    action = 'Unknown'
    if hive.action == mca.survey.cmd.registryhive.types.ACTION_LOAD:
        action = 'Load'
    elif hive.action == mca.survey.cmd.registryhive.types.ACTION_UNLOAD:
        action = 'Unload'
    elif hive.action == mca.survey.cmd.registryhive.types.ACTION_SAVE:
        action = 'Save'
    xml.AddAttribute('action', action)
    sub = xml.AddSubElement('Hive')
    sub.AddAttribute('key', hive.key)
    sub.AddAttribute('hive', _getHiveString(hive.hive))
    sub.AddAttribute('file', hive.file)
    if hive.permanent:
        sub.AddAttribute('permanent', 'true')
    else:
        sub.AddAttribute('permanent', 'false')
    output.RecordXml(xml)
    if action == 'Load' and hive.permanent == False:
        output.GoToBackground()
    output.End()
    return True


def _getHiveString(hive):
    if hive == mca.survey.cmd.registryhive.types.HIVE_LOCAL_MACHINE:
        return 'HKEY_LOCAL_MACHINE'
    else:
        if hive == mca.survey.cmd.registryhive.types.HIVE_CLASSES_ROOT:
            return 'HKEY_CLASSES_ROOT'
        if hive == mca.survey.cmd.registryhive.types.HIVE_CURRENT_USER:
            return 'HKEY_CURRENT_USER'
        if hive == mca.survey.cmd.registryhive.types.HIVE_CURRENT_CONFIG:
            return 'HKEY_CURRENT_CONFIG'
        if hive == mca.survey.cmd.registryhive.types.HIVE_USERS:
            return 'HKEY_USERS'
        return 'HKEY_UNKNOWN'


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)