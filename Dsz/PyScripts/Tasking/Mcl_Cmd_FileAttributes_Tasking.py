# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_FileAttributes_Tasking.py
FILEATTRIBS_ACTION_GET = 1
FILEATTRIBS_ACTION_SET = 2
FILEATTRIBS_ACTION_REPLACE = 3
FILEATTRIBS_ACTION_REMOVE = 4
FILEATTRIBS_ACTION_ADD = 5

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.virtualdir
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.fileattributes', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.file.cmd.fileattributes.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    if lpParams['file'] == None or len(lpParams['file']) == 0:
        mcl.tasking.EchoError('A filename must be specified')
        return False
    else:
        try:
            file = mcl.tasking.virtualdir.GetFullPath(lpParams['file'])
        except:
            mcl.tasking.EchoError('Unable to apply virtual path to filename')
            return False

        if lpParams['action'] == FILEATTRIBS_ACTION_GET:
            params = mca.file.cmd.fileattributes.GetParams()
            params.file = file
            rpc = mca.file.cmd.fileattributes.tasking.RPC_INFO_GET
            msg = MarshalMessage()
            params.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
        elif lpParams['action'] == FILEATTRIBS_ACTION_SET or lpParams['action'] == FILEATTRIBS_ACTION_REPLACE or lpParams['action'] == FILEATTRIBS_ACTION_REMOVE or lpParams['action'] == FILEATTRIBS_ACTION_ADD:
            params = mca.file.cmd.fileattributes.SetParams()
            params.file = file
            params.ftAccessed = lpParams['ftAccessed']
            params.ftCreated = lpParams['ftCreated']
            params.ftModified = lpParams['ftModified']
            if lpParams['owner'] != None:
                params.owner = lpParams['owner']
            if lpParams['group'] != None:
                params.group = lpParams['group']
            if lpParams['action'] == FILEATTRIBS_ACTION_SET:
                params.setType = mca.file.cmd.fileattributes.PARAMS_SET_TYPE_SET
            elif lpParams['action'] == FILEATTRIBS_ACTION_REPLACE:
                params.setType = mca.file.cmd.fileattributes.PARAMS_SET_TYPE_REPLACE
            elif lpParams['action'] == FILEATTRIBS_ACTION_REMOVE:
                params.setType = mca.file.cmd.fileattributes.PARAMS_SET_TYPE_REMOVE
            elif lpParams['action'] == FILEATTRIBS_ACTION_ADD:
                params.setType = mca.file.cmd.fileattributes.PARAMS_SET_TYPE_ADD
            try:
                params.attributes = _getAttributes(mca, lpParams['attributes'])
            except RuntimeError as err:
                mcl.tasking.EchoError(str(err))
                return False

            rpc = mca.file.cmd.fileattributes.tasking.RPC_INFO_SET
            msg = MarshalMessage()
            params.Marshal(msg)
            rpc.SetData(msg.Serialize())
            rpc.SetMessagingType('message')
        else:
            mcl.tasking.EchoError('Unhandled action type (%u)' % lpParams['action'])
            return False
        res = mcl.tasking.RpcPerformCall(rpc)
        if res != mcl.target.CALL_SUCCEEDED:
            mcl.tasking.RecordModuleError(res, 0, mca.file.cmd.fileattributes.errorStrings)
            return False
        return True


def _getAttributes(mca, attribStr):
    USERINPUT_TO_ATTRIB = {'ARCHIVE': mca.file.cmd.fileattributes.ATTRIB_ARCHIVE,
       'HIDDEN': mca.file.cmd.fileattributes.ATTRIB_HIDDEN,
       'NORMAL': mca.file.cmd.fileattributes.ATTRIB_NORMAL,
       'NOTINDEXED': mca.file.cmd.fileattributes.ATTRIB_NOT_INDEXED,
       'OFFLINE': mca.file.cmd.fileattributes.ATTRIB_OFFLINE,
       'READONLY': mca.file.cmd.fileattributes.ATTRIB_READONLY,
       'SYSTEM': mca.file.cmd.fileattributes.ATTRIB_SYSTEM,
       'TEMPORARY': mca.file.cmd.fileattributes.ATTRIB_TEMPORARY,
       'COMPRESSED': mca.file.cmd.fileattributes.ATTRIB_COMPRESSED,
       'ENCRYPTED': mca.file.cmd.fileattributes.ATTRIB_ENCRYPTED,
       'OWNERREAD': mca.file.cmd.fileattributes.ATTRIB_OWNER_READ,
       'OWNERWRITE': mca.file.cmd.fileattributes.ATTRIB_OWNER_WRITE,
       'OWNEREXEC': mca.file.cmd.fileattributes.ATTRIB_OWNER_EXEC,
       'GROUPREAD': mca.file.cmd.fileattributes.ATTRIB_GROUP_READ,
       'GROUPWRITE': mca.file.cmd.fileattributes.ATTRIB_GROUP_WRITE,
       'GROUPEXEC': mca.file.cmd.fileattributes.ATTRIB_GROUP_EXEC,
       'WORLDREAD': mca.file.cmd.fileattributes.ATTRIB_WORLD_READ,
       'WORLDWRITE': mca.file.cmd.fileattributes.ATTRIB_WORLD_WRITE,
       'WORLDEXEC': mca.file.cmd.fileattributes.ATTRIB_WORLD_EXEC,
       'SETUID': mca.file.cmd.fileattributes.ATTRIB_SET_UID,
       'SETGID': mca.file.cmd.fileattributes.ATTRIB_SET_GID,
       'STICKYBIT': mca.file.cmd.fileattributes.ATTRIB_STICKY_BIT
       }
    if attribStr == None:
        return 0
    else:
        attribValue = 0
        while len(attribStr) > 0:
            pos = attribStr.find('|')
            if pos == -1:
                value = attribStr
                attribStr = ''
            else:
                value = attribStr[0:pos]
                attribStr = attribStr[pos + 1:]
            if len(value) > 0:
                if USERINPUT_TO_ATTRIB.has_key(value.upper()):
                    attribValue |= USERINPUT_TO_ATTRIB[value.upper()]
                else:
                    raise RuntimeError('Invalid attribute (%s)' % value)

        return attribValue


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)