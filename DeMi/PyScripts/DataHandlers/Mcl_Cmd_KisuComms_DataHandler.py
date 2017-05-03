# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_KisuComms_DataHandler.py


def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('KisuComms', 'kisucomms', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_KISU_FAILURE:
            if osError & 536870912:
                output.RecordModuleError(moduleError, 0, errorStrings)
                mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.kisu_errors', globals())
                output.RecordModuleError(osError, 0, mcf.kisu.kisu_errors.errorStrings, translateMclStatusError=False)
            else:
                output.RecordModuleError(moduleError, osError, errorStrings, translateMclStatusError=False)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if msg.PeekByKey(MSG_KEY_RESULT_INSTANCE) != None:
            rtn = _handleList(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_CONFIG) != None:
            rtn = _handleConfig(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_CONNECT) != None:
            rtn = _handleConnect(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_MODULE_ADD) != None:
            rtn = _handleModuleAdd(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_MODULE_DELETE) != None:
            rtn = _handleModuleDelete(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_MODULE_READ) != None:
            rtn = _handleModuleRead(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_DRIVER_LOAD) != None:
            rtn = _handleDriverLoad(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_DRIVER_UNLOAD) != None:
            rtn = _handleDriverUnload(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_MODULE_LOAD) != None:
            rtn = _handleModuleLoad(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_MODULE_FREE) != None:
            rtn = _handleModuleFree(namespace, output, msg)
        elif msg.PeekByKey(MSG_KEY_RESULT_PROCESS_LOAD) != None:
            rtn = _handleProcessLoad(namespace, output, msg)
        else:
            output.RecordError('Unhandled key')
            rtn = mcl.target.CALL_FAILED
        output.EndWithStatus(rtn)
        return True


def _getFlagTranslation(namespace):
    mcl.imports.ImportNamesWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    _KisuFlags_Translation = {KISU_MODULE_FLAG_BOOT_START: 'BOOT_START',
       KISU_MODULE_FLAG_SYSTEM_START: 'SYSTEM_START',
       KISU_MODULE_FLAG_AUTO_START: 'AUTO_START',
       KISU_MODULE_FLAG_KERNEL_DRIVER: 'KERNEL_DRIVER',
       KISU_MODULE_FLAG_USER_MODE: 'USER_MODE',
       KISU_MODULE_FLAG_SYSTEM_MODE: 'SYSTEM_MODE',
       KISU_MODULE_FLAG_SERVICE_KEY: 'SERVICE_KEY',
       KISU_MODULE_FLAG_ENCRYPTED: 'ENCRYPTED',
       KISU_MODULE_FLAG_COMPRESSED: 'COMPRESSED',
       KISU_MODULE_FLAG_DEMAND_LOAD: 'DEMAND_LOAD',
       KISU_MODULE_FLAG_AUTO_START_ONCE: 'AUTO_START_ONCE'
       }
    return _KisuFlags_Translation


def _handleConfig(namespace, output, msg):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuConfiguration')
    configMsg = msg.FindMessage(MSG_KEY_RESULT_CONFIG)
    configBase = ResultConfigBase()
    configBase.Demarshal(configMsg)
    xml.AddAttribute('id', '0x%08x' % configBase.instance.id)
    import mcl.imports
    mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
    for name in mcf.kisu.ids.nameTable:
        if mcf.kisu.ids.nameTable[name] == configBase.instance.id:
            xml.AddAttribute('name', name)
            break

    sub = xml.AddSubElement('Version')
    sub.AddAttribute('major', '%u' % configBase.instance.versionMajor)
    sub.AddAttribute('minor', '%u' % configBase.instance.versionMinor)
    sub.AddAttribute('fix', '%u' % configBase.instance.versionFix)
    sub.AddAttribute('build', '%u' % configBase.instance.versionBuild)
    if configMsg.PeekByKey(MSG_KEY_RESULT_CONFIG_KERNEL) != None:
        keyMsg = configMsg.FindMessage(MSG_KEY_RESULT_CONFIG_KERNEL)
        keyInfo = ResultConfigKey()
        keyInfo.Demarshal(keyMsg)
        sub = xml.AddSubElement('KernelModuleLoader')
        sub.AddSubElementWithText('RegKeyPath', keyInfo.path)
        sub.AddSubElementWithText('RegValueName', keyInfo.value)
    if configMsg.PeekByKey(MSG_KEY_RESULT_CONFIG_USER) != None:
        keyMsg = configMsg.FindMessage(MSG_KEY_RESULT_CONFIG_USER)
        keyInfo = ResultConfigKey()
        keyInfo.Demarshal(keyMsg)
        sub = xml.AddSubElement('UserModuleLoader')
        sub.AddSubElementWithText('RegKeyPath', keyInfo.path)
        sub.AddSubElementWithText('RegValueName', keyInfo.value)
    if configMsg.PeekByKey(MSG_KEY_RESULT_CONFIG_MODULE) != None:
        keyMsg = configMsg.FindMessage(MSG_KEY_RESULT_CONFIG_MODULE)
        keyInfo = ResultConfigKey()
        keyInfo.Demarshal(keyMsg)
        sub = xml.AddSubElement('ModuleStoreDirectory')
        sub.AddSubElementWithText('RegKeyPath', keyInfo.path)
        sub.AddSubElementWithText('RegValueName', keyInfo.value)
    if configMsg.PeekByKey(MSG_KEY_RESULT_CONFIG_LAUNCHER) != None:
        keyMsg = configMsg.FindMessage(MSG_KEY_RESULT_CONFIG_LAUNCHER)
        keyInfo = ResultConfigKey()
        keyInfo.Demarshal(keyMsg)
        sub = xml.AddSubElement('Launcher')
        sub.AddSubElementWithText('ServiceName', keyInfo.path)
        sub.AddSubElementWithText('RegValueName', keyInfo.value)
    sub = xml.AddSubElement('Persistence')
    if configBase.persistenceMethod == RESULT_PERSISTENCE_TYPE_LAUNCHER:
        sub.AddAttribute('method', 'DRIVER')
    elif configBase.persistenceMethod == RESULT_PERSISTENCE_TYPE_SOTI:
        sub.AddAttribute('method', 'SOTI')
    elif configBase.persistenceMethod == RESULT_PERSISTENCE_TYPE_JUVI:
        sub.AddAttribute('method', 'JUVI')
    else:
        sub.AddAttribute('method', 'UNKNOWN')
    while configMsg.PeekByKey(MSG_KEY_RESULT_MODULE) != None:
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        module = ResultModule()
        module.Demarshal(configMsg)
        sub = xml.AddSubElement('Module')
        sub.AddAttribute('size', '%u' % module.size)
        sub.AddAttribute('order', '%u' % module.order)
        sub.AddAttribute('flags', '0x%08x' % module.flags)
        sub.AddAttribute('id', '0x%08x' % module.id)
        sub.AddAttribute('moduleName', module.moduleName)
        sub.AddAttribute('processName', module.processName)
        if len(module.hash) > 0:
            hashSub = sub.AddSubElement('Sha1Hash')
            hashSub.SetTextAsData(module.hash)
        trans = _getFlagTranslation(namespace)
        for flag in trans:
            if module.flags & flag:
                sub.AddSubElement(trans[flag])

    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_ACCESSED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Pulled config for 0x%08x' % configBase.instance.id)
    return mcl.target.CALL_SUCCEEDED


def _handleConnect(namespace, output, msg):
    import mcl.imports
    result = ResultConnect()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuCommsInitialized')
    xml.AddAttribute('id', '0x%08x' % result.instance.id)
    xml.AddAttribute('versionMajor', '%u' % result.instance.versionMajor)
    xml.AddAttribute('versionMinor', '%u' % result.instance.versionMinor)
    xml.AddAttribute('versionFix', '%u' % result.instance.versionFix)
    xml.AddAttribute('versionBuild', '%u' % result.instance.versionBuild)
    mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
    for name in mcf.kisu.ids.nameTable:
        if mcf.kisu.ids.nameTable[name] == result.instance.id:
            xml.AddAttribute('name', name)
            break

    output.RecordXml(xml)
    import mcl.data.env
    mcl.data.env.SetValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, '0x%08x' % result.instance.id, globalValue=True)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_CHECKED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Connected to 0x%08x' % result.instance.id)
    return mcl.target.CALL_SUCCEEDED


def _handleDriverLoad(namespace, output, msg):
    result = ResultDriverLoad()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuDriverLoad')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleId', '0x%08x' % result.id)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Loaded driver 0x%08x from 0x%08x' % (result.id, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleDriverUnload(namespace, output, msg):
    result = ResultDriverUnload()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuDriverUnload')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleId', '0x%08x' % result.id)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Unloaded driver 0x%08x from 0x%08x' % (result.id, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleList(namespace, output, msg):
    import mcl.imports
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuEnumeration')
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        result = ResultInstance()
        result.Demarshal(msg)
        if result.id != 0:
            sub = xml.AddSubElement('KiSu')
            sub.AddAttribute('id', '0x%08x' % result.id)
            sub.AddAttribute('versionMajor', '%u' % result.versionMajor)
            sub.AddAttribute('versionMinor', '%u' % result.versionMinor)
            sub.AddAttribute('versionFix', '%u' % result.versionFix)
            sub.AddAttribute('versionBuild', '%u' % result.versionBuild)
            mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
            for name in mcf.kisu.ids.nameTable:
                if mcf.kisu.ids.nameTable[name] == result.id:
                    sub.AddAttribute('name', name)
                    break

    output.RecordXml(xml)
    return mcl.target.CALL_SUCCEEDED


def _handleModuleAdd(namespace, output, msg):
    result = ResultModuleAdd()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuAddedModule')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleId', '0x%08x' % result.id)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Added module 0x%08x to 0x%08x' % (result.id, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleModuleDelete(namespace, output, msg):
    result = ResultModuleDelete()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuDeletedModule')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleId', '0x%08x' % result.id)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Deleted module 0x%08x to 0x%08x' % (result.id, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleModuleFree(namespace, output, msg):
    result = ResultModuleFree()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuModuleFree')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleHandle', '0x%08x' % result.moduleHandle)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Freed module at 0x%08x from 0x%08x' % (result.moduleHandle, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleModuleLoad(namespace, output, msg):
    result = ResultModuleLoad()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuModuleLoad')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('moduleId', '0x%08x' % result.id)
    xml.AddAttribute('moduleHandle', '0x%08x' % result.moduleHandle)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Loaded module 0x%08x at 0x%08x from 0x%08x' % (result.id, result.moduleHandle, result.instance))
    return mcl.target.CALL_SUCCEEDED


def _handleModuleRead(namespace, output, msg):
    import os.path
    result = ResultModuleRead()
    result.Demarshal(msg)
    f, path, logName = output.CreateLogFile(prefix='demi', suffix='get', subDir='DemiOutput', utf8=False)
    if f == None:
        output.RecordError('Failed to create log file for 0x%08x' % results.id)
        return mcl.target.CALL_FAILED
    else:
        try:
            f.write(result.data)
            f.flush()
        finally:
            f.close()

        from mcl.object.XmlOutput import XmlOutput
        xml = XmlOutput()
        xml.Start('KiSuReadModuleSuccess')
        xml.AddAttribute('id', '0x%08x' % result.id)
        xml.AddAttribute('instance', '0x%08x' % result.instance)
        xml.AddAttribute('bytes', '%u' % len(result.data))
        xml.SetText(os.path.normpath('%s/%s' % (path, logName)))
        output.RecordXml(xml)
        import mcl.tools
        verInfo = mcl.tools.GetVersion('DeMi')
        if verInfo != None:
            mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Read module 0x%08x to 0x%08x' % (result.id, result.instance))
        return mcl.target.CALL_SUCCEEDED


def _handleProcessLoad(namespace, output, msg):
    result = ResultProcessLoad()
    result.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('KiSuProcessLoad')
    xml.AddAttribute('instance', '0x%08x' % result.instance)
    xml.AddAttribute('processId', '%u' % result.processId)
    output.RecordXml(xml)
    import mcl.tools
    verInfo = mcl.tools.GetVersion('DeMi')
    if verInfo != None:
        mcl.tools.RecordUsage('DeMi', verInfo['full'], mcl.tools.USAGE_FLAG_EXERCISED, mcl.tools.USAGE_STATUS_SUCCESSFUL, comments='Modules loaded into process %u from 0x%08x' % (result.processId, result.instance))
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