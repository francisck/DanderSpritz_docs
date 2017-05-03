# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Cd_Tasking.py
LP_CD_TYPE_REAL = 0
LP_CD_TYPE_VIRTUAL = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.env
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.cd', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.cd.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['type'] == LP_CD_TYPE_REAL:
        isVirtual = False
    elif lpParams['type'] == LP_CD_TYPE_VIRTUAL:
        isVirtual = True
    else:
        mcl.tasking.EchoError('Unhandled dir type (%u)' % lpParams['type'])
        return False
    try:
        if isVirtual:
            mcl.tasking.env.SetValue('IsVirtual', 'true')
        else:
            mcl.tasking.env.SetValue('IsVirtual', 'false')
    except:
        mcl.tasking.EchoError("Failed to set 'IsVirtual' environment variable")
        return False

    if lpParams['dir'] == None:
        dir = ''
    else:
        dir = lpParams['dir']
    if isVirtual:
        if len(dir) > 0 and lpParams['force']:
            try:
                mcl.tasking.virtualdir.Set(dir)
            except:
                mcl.tasking.EchoError('Failed to set virtual working directory')
                return False

        try:
            currentDir = mcl.tasking.virtualdir.GetFullPath(dir)
        except:
            mcl.tasking.EchoError('Failed to get virtual working directory')
            return False

        if len(currentDir) > 0:
            if len(dir) == 0 or lpParams['force']:
                if currentDir.startswith('\\\\?\\UNC\\'):
                    userDir = '\\\\%s' % currentDir[8:]
                elif currentDir.startswith('\\\\?\\'):
                    userDir = currentDir[4:]
                else:
                    userDir = currentDir
                from mcl.object.XmlOutput import XmlOutput
                xml = XmlOutput()
                xml.Start('DirectoryInfo')
                xml.AddSubElementWithText('CurrentDirectory', userDir)
                xml.AddAttribute('virtual', 'true')
                mcl.tasking.OutputXml(xml)
                mcl.tasking.TaskSetStatus(mcl.target.CALL_SUCCEEDED)
                return True
            dir = currentDir
    tgtParams = mca.file.cmd.cd.Params()
    tgtParams.dir = dir
    if isVirtual or len(tgtParams.dir) == 0:
        rpc = mca.file.cmd.cd.tasking.RPC_INFO_QUERY
    else:
        rpc = mca.file.cmd.cd.tasking.RPC_INFO_SET
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.cd.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)