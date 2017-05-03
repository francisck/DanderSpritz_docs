# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_MatchFileTimes_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.matchfiletimes', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.matchfiletimes.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.file.cmd.matchfiletimes.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('MATCHFILETIMES', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    tgtParams.flags = 0
    if lpParams['visibletimes']:
        tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_MODIFIED
        tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_ACCESSED
        tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_CREATED
    else:
        if lpParams['accessed']:
            tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_ACCESSED
        if lpParams['modified']:
            tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_MODIFIED
        if lpParams['created']:
            tgtParams.flags |= mca.file.cmd.matchfiletimes.PARAMS_FLAG_CHANGE_CREATED
    if lpParams['src'] == None or len(lpParams['src']) == 0 or lpParams['dst'] == None or len(lpParams['dst']) == 0:
        mcl.tasking.EchoError('Invalid filename')
        return False
    else:
        try:
            tgtParams.src = mcl.tasking.virtualdir.GetFullPath(lpParams['src'])
            tgtParams.dst = mcl.tasking.virtualdir.GetFullPath(lpParams['dst'])
        except:
            mcl.tasking.EchoError('Unable to apply virtual path to src/dst filenames')
            return False

        taskXml = mcl.tasking.Tasking()
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.file.cmd.matchfiletimes.tasking.RPC_INFO_MATCH
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.matchfiletimes.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)