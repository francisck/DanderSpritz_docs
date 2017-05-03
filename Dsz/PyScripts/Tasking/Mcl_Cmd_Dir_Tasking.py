# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Dir_Tasking.py
LP_TIME_TYPE_ACCESSED = 1
LP_TIME_TYPE_MODIFIED = 2
LP_TIME_TYPE_CREATED = 3
_MIN_SECONDS_FOR_AGE = 25

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.MclTime import MclTime
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.dir', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.dir.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    try:
        path, mask = mcl.tasking.virtualdir.GetMaskAndPath(lpParams['path_and_mask'], lpParams['mask'], lpParams['path'])
    except RuntimeError as err:
        mcl.tasking.EchoError(str(err))
        return False

    try:
        path = mcl.tasking.virtualdir.GetFullPath(path)
    except:
        mcl.tasking.EchoError('Failed to get full path')
        raise
        return False

    if lpParams['age'].GetTimeType() != MclTime.MCL_TIME_TYPE_INVALID:
        if lpParams['afterDate'].GetTimeType() != MclTime.MCL_TIME_TYPE_INVALID or lpParams['beforeDate'].GetTimeType() != MclTime.MCL_TIME_TYPE_INVALID:
            mcl.tasking.EchoError('Age and before/after times are mutually exclusive')
            return False
        if lpParams['age'].GetSeconds() < _MIN_SECONDS_FOR_AGE:
            mcl.tasking.EchoError('An age of %u second(s) is too small' % lpParams['age'].GetSeconds())
            return False
    tgtParams = mca.file.cmd.dir.Params()
    tgtParams.path = path
    tgtParams.mask = mask
    if lpParams['timetype'] == LP_TIME_TYPE_ACCESSED:
        tgtParams.dateType = mca.file.cmd.dir.PARAM_TIME_TYPE_ACCESSED
    elif lpParams['timetype'] == LP_TIME_TYPE_MODIFIED:
        tgtParams.dateType = mca.file.cmd.dir.PARAM_TIME_TYPE_MODIFIED
    elif lpParams['timetype'] == LP_TIME_TYPE_CREATED:
        tgtParams.dateType = mca.file.cmd.dir.PARAM_TIME_TYPE_CREATED
    else:
        mcl.tasking.EchoError('Invalid time type specified')
        return False
    tgtParams.maxEntries = lpParams['max']
    if lpParams['recursive']:
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_RECURSIVE
    if lpParams['dirsonly']:
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_DIRS_ONLY
    tgtParams.age = lpParams['age']
    tgtParams.afterTime = lpParams['afterDate']
    tgtParams.beforeTime = lpParams['beforeDate']
    tgtParams.chunkSize = lpParams['chunksize']
    tgtParams.depth = lpParams['recurseDepth']
    if lpParams['allhashes']:
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_MD5
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA1
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA256
        tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA512
    else:
        if lpParams['md5']:
            tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_MD5
        if lpParams['sha1']:
            tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA1
        if lpParams['sha256']:
            tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA256
        if lpParams['sha512']:
            tgtParams.flags |= mca.file.cmd.dir.PARAM_FLAG_PERFORM_HASH_SHA512
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchMask(tgtParams.mask)
        taskXml.AddSearchPath(tgtParams.path)
        if tgtParams.afterTime.GetTimeType() != MclTime.MCL_TIME_TYPE_INVALID:
            taskXml.SetSearchTimeAfter(tgtParams.afterTime)
        if tgtParams.beforeTime.GetTimeType() != MclTime.MCL_TIME_TYPE_INVALID:
            taskXml.SetSearchTimeBefore(tgtParams.beforeTime)
        if tgtParams.age.GetTimeType() != MclTime.MCL_TIME_TYPE_DELTA:
            taskXml.SetSearchTimeAge(tgtParams.age)
        if tgtParams.flags & mca.file.cmd.dir.PARAM_FLAG_RECURSIVE:
            taskXml.SetRecursive(tgtParams.depth)
        if tgtParams.maxEntries:
            taskXml.SetMaxMatches(tgtParams.maxEntries)
        if tgtParams.flags & mca.file.cmd.dir.PARAM_FLAG_DIRS_ONLY:
            taskXml.SetType('DIRS_ONLY')
        else:
            taskXml.SetType('DIRS_AND_FILES')
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        rpc = mca.file.cmd.dir.tasking.RPC_INFO_LIST
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.dir.errorStrings)
            return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)