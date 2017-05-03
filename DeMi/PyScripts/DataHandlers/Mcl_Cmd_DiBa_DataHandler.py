# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DiBa_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mcf.cmd.diba', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('DIBA', 'diba', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_DIBA_FAILURE:
            output.RecordModuleError(moduleError, 0, errorStrings)
            mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.diba_errors', globals())
            output.RecordModuleError(osError, 0, mcf.kisu.diba_errors.errorStrings, translateMclStatusError=False)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.PeekByKey(MSG_KEY_RESULT_INSTALL) != None:
            rtn = _handleInstall(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_UNINSTALL) != None:
            rtn = _handleUninstall(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_PERSISTENCE) != None:
            rtn = _handlePersistence(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_UPGRADE) != None:
            rtn = _handleUpgrade(namespace, output, msg)
        else:
            output.RecordError('Unhandled key')
            rtn = mcl.target.CALL_FAILED
        output.EndWithStatus(rtn)
        return True


def _handleInstall(namespace, output, msg):
    result = ResultInstall()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuInstall')
    xml.AddAttribute('id', '0x%08x' % result.instance)
    import mcl.imports
    mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
    for name in mcf.kisu.ids.nameTable:
        if mcf.kisu.ids.nameTable[name] == result.instance:
            xml.AddAttribute('name', name)
            break

    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_DEPLOYED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Installed 0x%08x' % result.instance)
    return mcl.target.CALL_SUCCEEDED


def _handlePersistence(namespace, output, msg):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuSurveyPersistence')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            output.EndWithStatus(mcl.target.CALL_FAILED)
            return False
        result = ResultPersistence()
        result.Demarshal(msg)
        sub = xml.AddSubElement('Method')
        if result.type == RESULT_PERSISTENCE_TYPE_LAUNCHER:
            sub.AddSubElementWithText('Type', 'DRIVER')
        elif result.type == RESULT_PERSISTENCE_TYPE_SOTI:
            sub.AddSubElementWithText('Type', 'SOTI')
        elif result.type == RESULT_PERSISTENCE_TYPE_JUVI:
            sub.AddSubElementWithText('Type', 'JUVI')
        else:
            sub.AddSubElementWithText('Type', 'UNKNOWN')
        if result.compatible:
            sub.AddSubElementWithText('Compatible', 'true')
        else:
            sub.AddSubElementWithText('Compatible', 'false')
        if result.reason != 0:
            mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.diba_errors', globals())
            if mcf.kisu.diba_errors.errorStrings.has_key(result.reason):
                reasonStr = mcf.kisu.diba_errors.errorStrings[result.reason]
            else:
                reasonStr = 'Unknown (0x%08x)' % result.reason
            sub.AddSubElementWithText('Reason', reasonStr)

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleUninstall(namespace, output, msg):
    result = ResultUninstall()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuUninstall')
    xml.AddAttribute('id', '0x%08x' % result.instance)
    import mcl.imports
    mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
    for name in mcf.kisu.ids.nameTable:
        if mcf.kisu.ids.nameTable[name] == result.instance:
            xml.AddAttribute('name', name)
            break

    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_DELETED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Uninstalled 0x%08x' % result.instance)
    return mcl.target.CALL_SUCCEEDED


def _handleUpgrade(namespace, output, msg):
    result = ResultUpgrade()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuUpgrade')
    xml.AddAttribute('id', '0x%08x' % result.instance)
    import mcl.imports
    mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
    for name in mcf.kisu.ids.nameTable:
        if mcf.kisu.ids.nameTable[name] == result.instance:
            xml.AddAttribute('name', name)
            break

    while msg.PeekByKey(MSG_KEY_RESULT_MODULE) != None:
        module = ResultModule()
        module.Demarshal(msg)
        sub = xml.AddSubElement('Module')
        sub.AddAttribute('size', '%u' % module.size)
        sub.AddAttribute('order', '%u' % module.order)
        sub.AddAttribute('flags', '0x%08x' % module.flags)
        sub.AddAttribute('id', '0x%08x' % module.id)
        sub.AddAttribute('moduleName', module.moduleName)
        sub.AddAttribute('processName', module.processName)
        sub.AddAttribute('actionStatus', '0x%08x' % module.actionStatus)
        if len(module.hash) > 0:
            hashSub = sub.AddSubElement('Sha1Hash')
            hashSub.SetTextAsData(module.hash)

    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_DEPLOYED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Upgraded 0x%08x' % result.instance)
    return mcl.target.CALL_SUCCEEDED


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)