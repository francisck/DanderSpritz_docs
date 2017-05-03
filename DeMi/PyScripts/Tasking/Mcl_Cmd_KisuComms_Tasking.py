# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_KisuComms_Tasking.py
_CMD_INDEX_LIST = 0
_CMD_INDEX_CONNECT = 1
_CMD_INDEX_DISCONNECT = 2
_CMD_INDEX_CONFIG = 3
_CMD_INDEX_ADD_MODULE = 4
_CMD_INDEX_DELETE_MODULE = 5
_CMD_INDEX_READ_MODULE = 6
_CMD_INDEX_LOAD_DRIVER = 7
_CMD_INDEX_FREE_DRIVER = 8
_CMD_INDEX_LOAD_MODULE = 9
_CMD_INDEX_FREE_MODULE = 10
_CMD_INDEX_PROCESS_LOAD = 11

def TaskingMain(namespace):
    import sys
    import re
    for arg in sys.argv:
        matchObj = re.match('procedure=(.*)', arg)
        if matchObj != None:
            procedure = int(matchObj.group(1))

    if procedure == _CMD_INDEX_LIST:
        return _handleList(namespace)
    else:
        if procedure == _CMD_INDEX_CONNECT:
            return _handleConnect(namespace)
        if procedure == _CMD_INDEX_DISCONNECT:
            return _handleDisconnect(namespace)
        if procedure == _CMD_INDEX_CONFIG:
            return _handleConfig(namespace)
        if procedure == _CMD_INDEX_ADD_MODULE:
            return _handleAddModule(namespace)
        if procedure == _CMD_INDEX_DELETE_MODULE:
            return _handleDeleteModule(namespace)
        if procedure == _CMD_INDEX_READ_MODULE:
            return _handleReadModule(namespace)
        if procedure == _CMD_INDEX_LOAD_DRIVER:
            return _handleLoadDriver(namespace)
        if procedure == _CMD_INDEX_FREE_DRIVER:
            return _handleFreeDriver(namespace)
        if procedure == _CMD_INDEX_LOAD_MODULE:
            return _handleLoadModule(namespace)
        if procedure == _CMD_INDEX_FREE_MODULE:
            return _handleFreeModule(namespace)
        if procedure == _CMD_INDEX_PROCESS_LOAD:
            return _handleProcessLoad(namespace)
        import mcl.tasking
        mcl.tasking.EchoError('Unknown procedure (%u)' % procedure)
        return False
        return


def _convertModuleFlags(namespace, flagsStr):
    import mcl.imports
    mcl.imports.ImportNamesWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    _KisuFlags_Translation = {'BOOT_START': KISU_MODULE_FLAG_BOOT_START,
       'SYSTEM_START': KISU_MODULE_FLAG_SYSTEM_START,
       'AUTO_START': KISU_MODULE_FLAG_AUTO_START,
       'KERNEL_DRIVER': KISU_MODULE_FLAG_KERNEL_DRIVER,
       'USER_MODE': KISU_MODULE_FLAG_USER_MODE,
       'SYSTEM_MODE': KISU_MODULE_FLAG_SYSTEM_MODE,
       'SERVICE_KEY': KISU_MODULE_FLAG_SERVICE_KEY,
       'ENCRYPTED': KISU_MODULE_FLAG_ENCRYPTED,
       'COMPRESSED': KISU_MODULE_FLAG_COMPRESSED,
       'DEMAND_LOAD': KISU_MODULE_FLAG_DEMAND_LOAD,
       'DEMANDLOAD': KISU_MODULE_FLAG_DEMAND_LOAD,
       'AUTO_START_ONCE': KISU_MODULE_FLAG_AUTO_START_ONCE
       }
    flagValue = 0
    for flag in flagsStr.split('|'):
        if not _KisuFlags_Translation.has_key(flag.upper()):
            raise RuntimeError('Invalid flag (%s) specified' % flag)
        flagValue = flagValue | _KisuFlags_Translation[flag.upper()]

    return flagValue


def _getKisuId(namespace, providedId, providedType):
    if providedType != None:
        import mcl.imports
        mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
        if mcf.kisu.ids.nameTable.has_key(providedType.upper()):
            kisuId = mcf.kisu.ids.nameTable[providedType.upper()]
        else:
            raise RuntimeError('Unknown KISU type (%s)' % providedType)
    else:
        kisuId = providedId
    if kisuId == 0:
        import mcl.imports
        import mcl.tasking.env
        mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
        if mcl.tasking.env.CheckValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, globalValue=True):
            kisuId = int(mcl.tasking.env.GetValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, globalValue=True), 0)
    if kisuId == 0:
        raise RuntimeError('Invalid KISU id (0)')
    return kisuId


def _handleAddModule(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.resource
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['chunkSize'] == 0:
        mcl.tasking.OutputError('Invalid chunkSize given')
        return False
    else:
        if lpParams['localFile'] == None or len(lpParams['localFile']) == 0:
            mcl.tasking.OutputError('No local file given')
            return False
        resFlags = mcl.tasking.resource.OPEN_RES_FLAG_USE_ARCH | mcl.tasking.resource.OPEN_RES_FLAG_USE_OS | mcl.tasking.resource.OPEN_RES_FLAG_USE_LIBC | mcl.tasking.resource.OPEN_RES_FLAG_USE_COMPILED
        hFile, openedFile, dir = mcl.tasking.resource.Open(lpParams['localFile'], resFlags, 'Uploads', lpParams['project'])
        if hFile == None:
            mcl.tasking.OutputError('Failed to open local file %s' % lpParams['localFile'])
            return False
        try:
            import os.path
            import array
            fileSize = os.path.getsize(openedFile)
            if fileSize == 0 or fileSize > 4294967295L:
                mcl.tasking.OutputError("Invalid file size (%u) for '%s'" % (fileSize, openedFile))
                return False
            fileBytes = array.array('B', hFile.read())
            if len(fileBytes) != fileSize:
                mcl.tasking.OutputError('Failed to read file (read=%u | expected=%u)' % (len(fileBytes), fileSize))
                return False
        finally:
            hFile.close()

        onIndex = 0
        bytesLeft = fileSize
        while bytesLeft > 0:
            if mcl.CheckForStop():
                return False
            if bytesLeft > lpParams['chunkSize']:
                bytesToSend = lpParams['chunkSize']
            else:
                bytesToSend = bytesLeft
            endIndex = onIndex + bytesToSend
            tgtParams = mcf.cmd.kisucomms.ParamsModuleAdd()
            tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
            tgtParams.chunkOffset = onIndex
            tgtParams.totalSize = fileSize
            tgtParams.chunk = fileBytes[onIndex:endIndex]
            tgtParams.moduleFlags = _convertModuleFlags(namespace, lpParams['moduleFlags'])
            tgtParams.moduleId = lpParams['moduleId']
            tgtParams.moduleOrder = lpParams['moduleOrder']
            tgtParams.moduleName = lpParams['moduleName']
            tgtParams.processName = lpParams['processName']
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('KiSuModuleAdd')
            xml.AddAttribute('chunkIndex', '%u' % tgtParams.chunkOffset)
            xml.AddAttribute('chunkSize', '%u' % len(tgtParams.chunk))
            xml.AddAttribute('totalSize', '%u' % tgtParams.totalSize)
            mcl.tasking.OutputXml(xml)
            rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_ADD_MODULE
            msg = MarshalMessage()
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
            res = mcl.tasking.RpcPerformCall(rpc)
            if res != mcl.target.CALL_SUCCEEDED:
                mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
                return False
            bytesLeft = bytesLeft - bytesToSend
            onIndex = onIndex + bytesToSend

        return True


def _handleConfig(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsConfig()
    tgtParams.id = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.hashModules = lpParams['checksum']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_CONFIG
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleConnect(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    import mcl.tasking.env
    if mcl.tasking.env.CheckValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, globalValue=True):
        mcl.tasking.OutputError('Already connected to a KISU instance')
        return False
    tgtParams = mcf.cmd.kisucomms.ParamsConnect()
    tgtParams.id = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_CONNECT
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleDeleteModule(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsModuleDelete()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleId = lpParams['moduleId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_DELETE_MODULE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleDisconnect(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    import mcl.tasking.env
    if not mcl.tasking.env.CheckValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, globalValue=True):
        mcl.tasking.OutputError('Not connected to a KISU instance')
        return False
    mcl.tasking.env.DeleteValue(mcf.cmd.kisucomms.COMMS_ESTABLISHED_ENV, globalValue=True)
    mcl.tasking.Echo('Disconnected')
    return mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)


def _handleFreeDriver(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsDriverUnload()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleId = lpParams['moduleId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_UNLOAD_DRIVER
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleFreeModule(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsModuleFree()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleHandle = lpParams['moduleHandle']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_FREE_MODULE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleList(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_LIST
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleLoadDriver(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsDriverLoad()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleId = lpParams['moduleId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_LOAD_DRIVER
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleLoadModule(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsModuleLoad()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleId = lpParams['moduleId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_LOAD_MODULE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleProcessLoad(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsProcessLoad()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.processId = lpParams['processId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_PROCESS_LOAD
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


def _handleReadModule(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.kisucomms.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.kisucomms.ParamsModuleRead()
    tgtParams.instance = _getKisuId(namespace, lpParams['instance'], lpParams['type'])
    tgtParams.moduleId = lpParams['moduleId']
    rpc = mcf.cmd.kisucomms.tasking.RPC_INFO_READ_MODULE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.kisucomms.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)