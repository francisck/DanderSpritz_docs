# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_LogEdit_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.logedit', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.logedit.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['file'] == None or len(lpParams['file']) == 0:
        mcl.tasking.EchoError('A file must be specified')
        return False
    else:
        if lpParams['phrase'] == None or len(lpParams['phrase']) == 0:
            mcl.tasking.EchoError('A phrase to replace must be specified')
            return False
        tgtParams = mca.file.cmd.logedit.Params()
        try:
            tgtParams.file = mcl.tasking.virtualdir.GetFullPath(lpParams['file'])
        except:
            mcl.tasking.EchoError('Failed to apply virtual directory to path')
            return False

        tgtParams.phrase = lpParams['phrase']
        tgtParams.flags |= mca.file.cmd.logedit.PARAMS_FLAG_SHARE_READ
        tgtParams.flags |= mca.file.cmd.logedit.PARAMS_FLAG_SHARE_WRITE
        tgtParams.flags |= mca.file.cmd.logedit.PARAMS_FLAG_SHARE_DELETE
        if not lpParams['ascii']:
            tgtParams.flags |= mca.file.cmd.logedit.PARAMS_FLAG_UNICODE
        if lpParams['dosreturn']:
            tgtParams.flags |= mca.file.cmd.logedit.PARAMS_FLAG_DOSRETURN
        rpc = mca.file.cmd.logedit.tasking.RPC_INFO_EDIT
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.logedit.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)