# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Route_Tasking.py
ROUTE_LP_PARAMS_TYPE_QUERY = 0
ROUTE_LP_PARAMS_TYPE_ADD = 1
ROUTE_LP_PARAMS_TYPE_DELETE = 2

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.route', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.route.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    marshalData = False
    if lpParams['type'] == ROUTE_LP_PARAMS_TYPE_QUERY:
        rpc = mca.network.cmd.route.tasking.RPC_INFO_QUERY
    elif lpParams['type'] == ROUTE_LP_PARAMS_TYPE_ADD:
        marshalData = True
        rpc = mca.network.cmd.route.tasking.RPC_INFO_ADD
    elif lpParams['type'] == ROUTE_LP_PARAMS_TYPE_DELETE:
        marshalData = True
        rpc = mca.network.cmd.route.tasking.RPC_INFO_DELETE
    else:
        mcl.tasking.EchoError('Invalid type (%u)' % lpParams['type'])
        return False
    if marshalData:
        from mcl.object.Message import MarshalMessage
        tgtParams = mca.network.cmd.route.Params()
        tgtParams.dest = lpParams['dest']
        tgtParams.netmask = lpParams['netmask']
        tgtParams.gateway = lpParams['gateway']
        tgtParams.iface = lpParams['interface']
        tgtParams.metric = lpParams['metric']
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.route.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)