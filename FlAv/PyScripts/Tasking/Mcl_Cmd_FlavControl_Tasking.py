# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_FlavControl_Tasking.py
FLAV_CMD_STATUS = 1
FLAV_CMD_AVAILABLE = 2
FLAV_CMD_NETSTAT = 3
FLAV_CMD_IPCONFIG = 4

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'flav.cmd.flavcontrol', globals())
    mcl.imports.ImportWithNamespace(namespace, 'flav.cmd.flavcontrol.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['cmd'] == FLAV_CMD_STATUS:
        rpc = flav.cmd.flavcontrol.tasking.RPC_INFO_STATUS
    elif lpParams['cmd'] == FLAV_CMD_AVAILABLE:
        rpc = flav.cmd.flavcontrol.tasking.RPC_INFO_AVAILABLE
    elif lpParams['cmd'] == FLAV_CMD_NETSTAT:
        tgtParams = flav.cmd.flavcontrol.Params()
        tgtParams.bufferSize = lpParams['bufferSize']
        rpc = flav.cmd.flavcontrol.tasking.RPC_INFO_NETSTAT
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['cmd'] == FLAV_CMD_IPCONFIG:
        tgtParams = flav.cmd.flavcontrol.Params()
        tgtParams.bufferSize = lpParams['bufferSize']
        rpc = flav.cmd.flavcontrol.tasking.RPC_INFO_IPCONFIG
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.OutputError('Unhandled command type (%u)' % lpParams['cmd'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, flav.cmd.flavcontrol.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)