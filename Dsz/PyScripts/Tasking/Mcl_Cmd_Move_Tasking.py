# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Move_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.move', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.move.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['src'] == None or len(lpParams['src']) == 0 or lpParams['dst'] == None or len(lpParams['dst']) == 0:
        mcl.tasking.EchoError('A source and destination must be specified')
        return False
    else:
        tgtParams = mca.file.cmd.move.Params()
        tgtParams.afterReboot = lpParams['afterReboot']
        try:
            tgtParams.src = mcl.tasking.virtualdir.GetFullPath(lpParams['src'])
            tgtParams.dst = mcl.tasking.virtualdir.GetFullPath(lpParams['dst'])
        except:
            mcl.tasking.EchoError('Failed to get full paths for file move')
            return False

        rpc = mca.file.cmd.move.tasking.RPC_INFO_MOVE
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.move.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)