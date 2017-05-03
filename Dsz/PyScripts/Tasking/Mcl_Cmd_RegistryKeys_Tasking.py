# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_RegistryKeys_Tasking.py
CMD_FLAG_USE_WOW_64 = 1
CMD_FLAG_USE_WOW_32 = 2

def TaskingMain(namespace):
    import sys
    import re
    for arg in sys.argv:
        matchObj = re.match('procedure=(.*)', arg)
        if matchObj != None:
            procedure = int(matchObj.group(1))

    if procedure == 0:
        return _handleRegistryAdd(namespace)
    else:
        if procedure == 1:
            return _handleRegistryDelete(namespace)
        import mcl.tasking
        mcl.tasking.EchoError('Unknown procedure (%u)' % procedure)
        return False
        return


def _handleRegistryAdd(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.registrykeys', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.registrykeys.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.install.cmd.registrykeys.ParamsAdd()
    tgtParams.provider = mcl.tasking.technique.Lookup('REGISTRYADD', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    tgtParams.hive = lpParams['hive']
    if lpParams['key'] != None:
        tgtParams.key = lpParams['key']
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['wowtype'] == CMD_FLAG_USE_WOW_64:
        tgtParams.flags |= mca.install.cmd.registrykeys.PARAMS_ADD_FLAG_USE_WOW64_64
    elif lpParams['wowtype'] == CMD_FLAG_USE_WOW_32:
        tgtParams.flags |= mca.install.cmd.registrykeys.PARAMS_ADD_FLAG_USE_WOW64_32
    if lpParams['volatile']:
        tgtParams.flags |= mca.install.cmd.registrykeys.PARAMS_ADD_FLAG_VOLATILE
    if lpParams['value'] != None:
        tgtParams.value = lpParams['value']
        try:
            tgtParams.type = _getType(mca, lpParams['type'])
        except:
            mcl.tasking.OutputError('Invalid type (%s) specified' % lpParams['type'])
            return False

        try:
            tgtParams.data = _getData(mca, tgtParams.type, lpParams['data'])
        except:
            mcl.tasking.OutputError('Invalid data (%s) specified' % lpParams['data'])
            return False

    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.install.cmd.registrykeys.tasking.RPC_INFO_ADD
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.install.cmd.registrykeys.errorStrings)
        return False
    else:
        return True


def _handleRegistryDelete(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.registrykeys', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.registrykeys.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.install.cmd.registrykeys.ParamsDelete()
    tgtParams.provider = mcl.tasking.technique.Lookup('REGISTRYDELETE', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    tgtParams.hive = lpParams['hive']
    tgtParams.recursive = lpParams['recursive']
    if lpParams['key'] != None:
        tgtParams.key = lpParams['key']
    if lpParams['remote'] != None:
        tgtParams.target = lpParams['remote']
    if lpParams['wowtype'] == CMD_FLAG_USE_WOW_64:
        tgtParams.flags |= PARAMS_DELETE_FLAG_USE_WOW64_64
    elif lpParams['wowtype'] == CMD_FLAG_USE_WOW_32:
        tgtParams.flags |= PARAMS_DELETE_FLAG_USE_WOW64_32
    if lpParams['value'] != None:
        tgtParams.deleteValue = True
        tgtParams.value = lpParams['value']
    else:
        tgtParams.deleteValue = False
    taskXml = mcl.tasking.Tasking()
    if len(tgtParams.target) > 0:
        taskXml.SetTargetRemote(tgtParams.target)
    else:
        taskXml.SetTargetLocal()
    taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    rpc = mca.install.cmd.registrykeys.tasking.RPC_INFO_DELETE
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.install.cmd.registrykeys.errorStrings)
        return False
    else:
        return True


def _getData(mca, type, origData):
    from mcl.object.Marshaler import Marshaler
    bytesBuffer = Marshaler()
    data = origData
    if type == mca.install.cmd.registrykeys.PARAMS_TYPE_REG_SZ or type == mca.install.cmd.registrykeys.PARAMS_TYPE_REG_EXPAND_SZ:
        bytesBuffer.AddString(data)
    elif type == mca.install.cmd.registrykeys.PARAMS_TYPE_REG_DWORD:
        bytesBuffer.AddU32(int(data, 0))
    elif type == mca.install.cmd.registrykeys.PARAMS_TYPE_REG_MULTI_SZ:
        for str in data.split('|'):
            bytesBuffer.AddString(str)

    else:
        dataStr = data
        while len(data) > 0:
            spaceLoc = dataStr.find(' ')
            if spaceLoc != -1:
                first = dataStr[0:spaceLoc]
                second = dataStr[spaceLoc + 1:]
                dataStr = second
            else:
                first = dataStr
                data = ''
            value = int(first, 16)
            bytesBuffer.AddU8(value)

    return bytesBuffer.GetData()


def _getType(mca, typeStr):
    REG_TYPES = {'REG_NONE': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_NONE,
       'REG_SZ': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_SZ,
       'REG_EXPAND_SZ': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_EXPAND_SZ,
       'REG_BINARY': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_BINARY,
       'REG_DWORD': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_DWORD,
       'REG_DWORD_LITTLE_ENDIAN': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_DWORD_LITTLE_ENDIAN,
       'REG_DWORD_BIG_ENDIAN': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_DWORD_BIG_ENDIAN,
       'REG_LINK': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_LINK,
       'REG_MULTI_SZ': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_MULTI_SZ,
       'REG_RESOURCE_LIST': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_RESOURCE_LIST,
       'REG_FULL_RESOURCE_DESCRIPTOR': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_FULL_RESOURCE_DESCRIPTOR,
       'REG_RESOURCE_REQUIREMENTS_LIST': mca.install.cmd.registrykeys.PARAMS_TYPE_REG_RESOURCE_REQUIREMENTS_LIST
       }
    return REG_TYPES[typeStr.upper()]


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)