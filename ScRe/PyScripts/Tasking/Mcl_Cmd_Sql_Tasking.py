# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Sql_Tasking.py
_CMD_ACTION_LIST_DRIVERS = 1
_CMD_ACTION_LIST_SOURCES = 2
_CMD_ACTION_CONNECT = 3
_CMD_ACTION_LIST_SERVERS = 4
_CMD_ACTION_LIST_DATABASES = 5
_CMD_ACTION_LIST_TABLES = 6
_CMD_ACTION_LIST_COLUMNS = 7
_CMD_ACTION_EXEC_QUERY = 8
_CMD_ACTION_LIST_HANDLES = 9
_CMD_ACTION_DISCONNECT = 10
actionMap = {_CMD_ACTION_LIST_DRIVERS: 'Drivers',_CMD_ACTION_LIST_SOURCES: 'Sources',
   _CMD_ACTION_CONNECT: 'Connect',
   _CMD_ACTION_LIST_SERVERS: 'Servers',
   _CMD_ACTION_LIST_DATABASES: 'Databases',
   _CMD_ACTION_LIST_TABLES: 'Tables',
   _CMD_ACTION_LIST_COLUMNS: 'Columns',
   _CMD_ACTION_EXEC_QUERY: 'Query',
   _CMD_ACTION_LIST_HANDLES: 'Handles',
   _CMD_ACTION_DISCONNECT: 'Disconnect'
   }
_CMD_ACCESS_TYPE_READ = 0
_CMD_ACCESS_TYPE_READWRITE = 1

def TaskingMain(namespace):
    import mcl.imports
    import mcl.target
    import mcl.tasking
    import mcl.tasking.env
    import mcl.tasking.technique
    from mcl.object.Message import MarshalMessage
    mcl.imports.ImportWithNamespace(namespace, 'mca.scre.cmd.sql', globals())
    mcl.imports.ImportWithNamespace(namespace, 'mca.scre.cmd.sql.tasking', globals())
    lpParams = mcl.tasking.GetParameters()
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('CommandInfo')
    xml.AddSubElementWithText('Action', actionMap[lpParams['actionCmd']])
    if lpParams['actionCmd'] == _CMD_ACTION_LIST_DRIVERS:
        rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_DRIVERS
    elif lpParams['actionCmd'] == _CMD_ACTION_LIST_SOURCES:
        rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_DATASOURCES
    elif lpParams['actionCmd'] == _CMD_ACTION_LIST_HANDLES:
        rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_HANDLES
    else:
        connectParams = mca.scre.cmd.sql.ParamsConnect()
        connectParams.connectionString = lpParams['connectString']
        if connectParams.connectionString == None:
            if not mcl.tasking.env.CheckValue('_SCRE_HANDLE_CONNECT_STR_%u' % lpParams['handleId'], globalValue=True) or not mcl.tasking.env.CheckValue('_SCRE_HANDLE_ACCESS_TYPE_%u' % lpParams['handleId'], globalValue=True) or not mcl.tasking.env.CheckValue('_SCRE_HANDLE_AUTO_COMMIT_%u' % lpParams['handleId'], globalValue=True):
                mcl.tasking.OutputError('The given handle id was not found')
                return False
            connectParams.connectionString = mcl.tasking.env.GetValue('_SCRE_HANDLE_CONNECT_STR_%u' % lpParams['handleId'], globalValue=True)
            accessType = mcl.tasking.env.GetValue('_SCRE_HANDLE_ACCESS_TYPE_%u' % lpParams['handleId'], globalValue=True)
            if accessType == 'READ ONLY':
                connectParams.accessType = mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_ONLY
            elif accessType == 'READ/WRITE':
                connectParams.accessType = mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_WRITE
            else:
                mcl.tasking.OutputError('Unknown access type for handle %u' % lpParams['handleId'])
                return False
            if not mcl.tasking.env.IsTrue('_SCRE_HANDLE_AUTO_COMMIT_%u' % lpParams['handleId'], globalValue=True):
                connectParams.flags &= ~mca.scre.cmd.sql.PARAMS_CONNECT_FLAG_AUTOCOMMIT
        else:
            if lpParams['accessType'] == _CMD_ACCESS_TYPE_READ:
                connectParams.accessType = mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_ONLY
            elif lpParams['accessType'] == _CMD_ACCESS_TYPE_READWRITE:
                connectParams.accessType = mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_WRITE
            else:
                mcl.tasking.OutputError('Unknown access type')
                return False
            if not lpParams['autoCommit']:
                connectParams.flags &= ~mca.scre.cmd.sql.PARAMS_CONNECT_FLAG_AUTOCOMMIT
            if connectParams.connectionString == None or len(connectParams.connectionString) == 0:
                mcl.tasking.OutputError('A connection string must be specified')
                return False
            xml.AddSubElementWithText('ConnectionString', connectParams.connectionString)
            if not lpParams['allowConnect']:
                connectParams.flags |= mca.scre.cmd.sql.PARAMS_CONNECT_FLAG_USE_EXISTING
            if connectParams.accessType == mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_ONLY:
                xml.AddSubElementWithText('AccessType', 'READ ONLY')
            elif connectParams.accessType == mca.scre.cmd.sql.SQL_ACCESS_TYPE_READ_WRITE:
                xml.AddSubElementWithText('AccessType', 'READ/WRITE')
            else:
                mcl.tasking.OutputError('Unknown access type')
                return False
            if connectParams.flags & mca.scre.cmd.sql.PARAMS_CONNECT_FLAG_AUTOCOMMIT:
                xml.AddSubElementWithText('AutoCommit', 'true')
            else:
                xml.AddSubElementWithText('AutoCommit', 'false')
            if mcl.tasking.env.CheckValue('_SCRE_TIMEOUT_SECONDS_%u' % lpParams['handleId'], globalValue=True):
                connectParams.timeoutSeconds = int(mcl.tasking.env.GetValue('_SCRE_TIMEOUT_SECONDS_%u' % lpParams['handleId'], globalValue=True))
            else:
                connectParams.timeoutSeconds = lpParams['timeout'].GetSeconds()
            msg = MarshalMessage()
            if lpParams['actionCmd'] == _CMD_ACTION_CONNECT:
                rpc = mca.scre.cmd.sql.tasking.RPC_INFO_CONNECT
                connectParams.Marshal(msg)
            elif lpParams['actionCmd'] == _CMD_ACTION_LIST_SERVERS:
                rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_SERVERS
                connectParams.Marshal(msg)
            else:
                if lpParams['actionCmd'] == _CMD_ACTION_DISCONNECT:
                    rpc = mca.scre.cmd.sql.tasking.RPC_INFO_DISCONNECT
                    connectParams.Marshal(msg)
                else:
                    queryParams = mca.scre.cmd.sql.ParamsQueryBase()
                    queryParams.connectInfo = connectParams
                    queryParams.maxColumnSize = lpParams['maxColumnSize']
                    queryParams.chunkSize = lpParams['chunkSize']
                    if queryParams.maxColumnSize < 1:
                        mcl.tasking.OutputError('maxColumnSize must be a positive number')
                        return False
                xml.AddSubElementWithText('MaxColumnSize', '%u' % queryParams.maxColumnSize)
                if lpParams['actionCmd'] == _CMD_ACTION_LIST_DATABASES:
                    rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_DATABASES
                    queryParams.Marshal(msg)
                elif lpParams['actionCmd'] == _CMD_ACTION_LIST_TABLES:
                    rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_TABLES
                    queryParams.Marshal(msg)
                elif lpParams['actionCmd'] == _CMD_ACTION_LIST_COLUMNS:
                    if lpParams['tableName'] == None or len(lpParams['tableName']) == 0:
                        mcl.tasking.OutputError('A table name must be specified')
                        return False
                    tgtParams = mca.scre.cmd.sql.ParamsQueryColumns()
                    tgtParams.baseInfo = queryParams
                    tgtParams.tableName = lpParams['tableName']
                    rpc = mca.scre.cmd.sql.tasking.RPC_INFO_LIST_COLUMNS
                    xml.AddSubElementWithText('TableName', tgtParams.tableName)
                    tgtParams.Marshal(msg)
                elif lpParams['actionCmd'] == _CMD_ACTION_EXEC_QUERY:
                    if lpParams['queryString'] == None and lpParams['queryFile'] == None:
                        mcl.tasking.OutputError('A query string or file must be specified')
                        return False
                    tgtParams = mca.scre.cmd.sql.ParamsQueryStatement()
                    tgtParams.baseInfo = queryParams
                    if lpParams['queryString'] != None:
                        if len(lpParams['queryString']) == 0:
                            mcl.tasking.OutputError('Query string must have a value specified')
                            return False
                        tgtParams.queryString = lpParams['queryString']
                        xml.AddSubElementWithText('QueryString', tgtParams.queryString)
                    else:
                        import mcl.tasking.resource
                        if len(lpParams['queryFile']) == 0:
                            mcl.tasking.OutputError('File must have a value specified')
                            return False
                        resFlags = 0
                        f, openedName, usedProject = mcl.tasking.resource.Open(lpParams['queryFile'], resFlags, None, None)
                        if f == None:
                            mcl.tasking.OutputError("Failed to open local file '%s'" % lpParams['queryFile'])
                            return False
                        try:
                            import os.path
                            import array
                            fileSize = os.path.getsize(openedName)
                            if fileSize == 0 or fileSize > 4294967295L:
                                mcl.tasking.OutputError("Invalid file size (%u) for put of '%s'" % (fileSize, openedName))
                                return False
                            fileQueryString = f.read()
                            try:
                                unicode(fileQueryString, 'utf-8')
                            except:
                                mcl.tasking.OutputError('Input file could not be parsed as utf-8')
                                return False

                        finally:
                            f.close()
                            f = None

                        tgtParams.queryString = fileQueryString.strip()
                        xml.AddSubElementWithText('File', lpParams['queryFile'])
                        xml.AddSubElementWithText('QueryString', tgtParams.queryString)
                    rpc = mca.scre.cmd.sql.tasking.RPC_INFO_EXEC
                    tgtParams.Marshal(msg)
                else:
                    mcl.tasking.OutputError('Unhandled action type (%u)' % lpParams['actionCmd'])
                    return False
        rpc.SetData(msg.Serialize())
    xml.AddSubElementWithText('ConsoleOutput', 'true')
    mcl.tasking.OutputXml(xml)
    rpc.SetMessagingType('message')
    res = mcl.tasking.RpcPerformCall(rpc)
    if res != mcl.target.CALL_SUCCEEDED:
        mcl.tasking.RecordModuleError(res, 0, mca.scre.cmd.sql.errorStrings)
        return False
    else:
        return True


if __name__ == '__main__':
    import sys
    if TaskingMain(sys.argv[1]) != True:
        sys.exit(-1)