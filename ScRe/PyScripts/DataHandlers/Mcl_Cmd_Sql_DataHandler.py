# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: Mcl_Cmd_Sql_DataHandler.py
import array
driverWarnings = {'microsoft odbc for oracle': 'Causes pop-up on target'
   }

def DataHandlerMain(namespace, InputFilename, OutputFilename):
    import mcl.imports
    import mcl.data.Input
    import mcl.data.Output
    import mcl.msgtype
    import mcl.status
    import mcl.target
    import mcl.object.Message
    mcl.imports.ImportNamesWithNamespace(namespace, 'mca.scre.cmd.sql', globals())
    input = mcl.data.Input.GetInput(InputFilename)
    output = mcl.data.Output.StartOutput(OutputFilename, input)
    output.Start('Sql', 'sql', [])
    msg = mcl.object.Message.DemarshalMessage(input.GetData())
    if input.GetStatus() != mcl.status.MCL_SUCCESS:
        errorMsg = msg.FindMessage(mcl.object.Message.MSG_KEY_RESULT_ERROR)
        moduleError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_MODULE)
        osError = errorMsg.FindU32(mcl.object.Message.MSG_KEY_RESULT_ERROR_OS)
        if moduleError == ERR_ODBC_ERROR:
            _handleSqlError(output, moduleError, osError)
        else:
            output.RecordModuleError(moduleError, osError, errorStrings)
        output.EndWithStatus(input.GetStatus())
        return True
    else:
        if input.GetMessageType() == mcl.msgtype.SQL_LIST:
            return _handleSqlList(msg, output)
        if input.GetMessageType() == mcl.msgtype.SQL_ERROR:
            return _handleSqlError(msg, output)
        output.RecordError('Unhandled message type (%u)' % input.GetMessageType())
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False


def _handleSqlError(msg, output):
    if msg.GetCount() == 0:
        output.RecordError('No data returned')
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return False
    results = ResultError()
    results.Demarshal(msg)
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Sql')
    sub = xml.AddSubElement('Error')
    sub.AddSubElementWithText('ErrorCode', '%d' % results.errorCode)
    sub.AddSubElementWithText('SqlState', results.sqlState)
    sub.AddSubElementWithText('Message', results.msg)
    output.RecordXml(xml)
    output.EndWithStatus(mcl.target.CALL_FAILED)
    return True


def _handleSqlList(msg, output):
    from mcl.object.XmlOutput import XmlOutput
    xml = XmlOutput()
    xml.Start('Sql')
    xml.AddAttribute('ConsoleOutput', 'true')
    if msg.GetCount() == 0:
        output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
        return True
    else:
        entry = msg.PeekByKey(mcl.object.Message.MSG_KEY_INVALID)
        if entry['key'] == MSG_KEY_RESULT_DRIVERS:
            sub = xml.AddSubElement('Drivers')
            rtn = _outputDriverXml(sub, msg)
            if rtn == mcl.target.CALL_SUCCEEDED:
                output.RecordXml(xml)
            output.EndWithStatus(rtn)
            return True
        if entry['key'] == MSG_KEY_RESULT_SOURCE:
            sub = xml.AddSubElement('Sources')
            rtn = _outputSourcesXml(sub, msg)
            if rtn == mcl.target.CALL_SUCCEEDED:
                output.RecordXml(xml)
            output.EndWithStatus(rtn)
            return True
        if entry['key'] == MSG_KEY_RESULT_SERVER:
            sub = xml.AddSubElement('Servers')
            rtn = _outputServersXml(sub, msg)
            if rtn == mcl.target.CALL_SUCCEEDED:
                output.RecordXml(xml)
            output.EndWithStatus(rtn)
            return True
        if entry['key'] == MSG_KEY_RESULT_DATABASES:
            sub = xml.AddSubElement('Databases')
            return _outputChunk(output, msg.FindMessage(MSG_KEY_RESULT_DATABASES), sub, xml)
        if entry['key'] == MSG_KEY_RESULT_TABLES:
            sub = xml.AddSubElement('Tables')
            return _outputChunk(output, msg.FindMessage(MSG_KEY_RESULT_TABLES), sub, xml)
        if entry['key'] == MSG_KEY_RESULT_COLUMNS:
            sub = xml.AddSubElement('Columns')
            return _outputChunk(output, msg.FindMessage(MSG_KEY_RESULT_COLUMNS), sub, xml)
        if entry['key'] == MSG_KEY_RESULT_EXECUTE:
            sub = xml.AddSubElement('Query')
            return _outputChunk(output, msg.FindMessage(MSG_KEY_RESULT_EXECUTE), sub, xml)
        if entry['key'] == MSG_KEY_RESULT_CONNECT:
            sub = xml.AddSubElement('Connection')
            rtn = _outputConnectionXml(sub, msg.FindMessage(MSG_KEY_RESULT_CONNECT), 'Opened')
            if rtn == mcl.target.CALL_SUCCEEDED:
                output.RecordXml(xml)
            output.EndWithStatus(rtn)
            return True
        if entry['key'] == MSG_KEY_RESULT_DISCONNECT:
            sub = xml.AddSubElement('Connection')
            rtn = _outputConnectionXml(sub, msg.FindMessage(MSG_KEY_RESULT_DISCONNECT), 'Closed')
            if rtn == mcl.target.CALL_SUCCEEDED:
                output.RecordXml(xml)
            output.EndWithStatus(rtn)
            return True
        if entry['key'] == MSG_KEY_RESULT_CONNECTIONS:
            sub = xml.AddSubElement('Handles')
            conMsg = msg.FindMessage(MSG_KEY_RESULT_CONNECTIONS)
            while conMsg.GetNumRetrieved() < conMsg.GetCount():
                if mcl.CheckForStop():
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                results = ResultConnection()
                results.Demarshal(conMsg)
                sub2 = sub.AddSubElement('Connection')
                sub2.AddSubElementWithText('ConnectString', results.connectionString)
                sub2.AddSubElementWithText('HandleId', '%u' % results.handleId)
                sub2.AddSubElementWithText('ConnectType', _translateConnectType(results.connectionType))
                if results.accessType == SQL_ACCESS_TYPE_READ_WRITE:
                    sub2.AddSubElementWithText('AccessType', 'READ/WRITE')
                else:
                    sub2.AddSubElementWithText('AccessType', 'READ ONLY')
                if results.autoCommit:
                    sub2.AddSubElementWithText('AutoCommit', 'true')
                else:
                    sub2.AddSubElementWithText('AutoCommit', 'false')
                sub2.AddTimeElement('CreateTime', results.createTime)
                sub2.AddTimeElement('LastUseTime', results.lastUseTime)
                sub2.AddTimeElement('MaxIdleDuration', results.maxIdleDuration)
                _recordHandleInformation('Opened', results.handleId, results.connectionString, results.accessType, results.autoCommit, results.maxIdleDuration)

            output.RecordXml(xml)
            output.EndWithStatus(mcl.target.CALL_SUCCEEDED)
            return True
        output.RecordError('Unhandled result key (0x%08x)' % entry['key'])
        output.EndWithStatus(mcl.target.CALL_FAILED)
        return True


def _SQL_TYPE_IS_BINARY(type):
    if type == SQL_DATA_TYPE_BINARY or type == SQL_DATA_TYPE_VARBINARY or type == SQL_DATA_TYPE_LONGVARBINARY:
        return True
    else:
        return False


def _SQLTypeToStr(type):
    sqlTypes = {SQL_DATA_TYPE_CHAR: 'SQL_CHAR',
       SQL_DATA_TYPE_NUMERIC: 'SQL_NUMERIC',
       SQL_DATA_TYPE_DECIMAL: 'SQL_DECIMAL',
       SQL_DATA_TYPE_INTEGER: 'SQL_INTEGER',
       SQL_DATA_TYPE_SMALLINT: 'SQL_SMALLINT',
       SQL_DATA_TYPE_FLOAT: 'SQL_FLOAT',
       SQL_DATA_TYPE_REAL: 'SQL_REAL',
       SQL_DATA_TYPE_DOUBLE: 'SQL_DOUBLE',
       SQL_DATA_TYPE_DATETIME: 'SQL_DATETIME',
       SQL_DATA_TYPE_TIME: 'SQL_TIME',
       SQL_DATA_TYPE_TIMESTAMP: 'SQL_TIMESTAMP',
       SQL_DATA_TYPE_VARCHAR: 'SQL_VARCHAR',
       SQL_DATA_TYPE_LONGVARCHAR: 'SQL_LONGVARCHAR',
       SQL_DATA_TYPE_BINARY: 'SQL_BINARY',
       SQL_DATA_TYPE_VARBINARY: 'SQL_VARBINARY',
       SQL_DATA_TYPE_LONGVARBINARY: 'SQL_LONGVARBINARY',
       SQL_DATA_TYPE_BIGINT: 'SQL_BIGINT',
       SQL_DATA_TYPE_TINYINT: 'SQL_TINYINT',
       SQL_DATA_TYPE_BIT: 'SQL_BIT',
       SQL_DATA_TYPE_WCHAR: 'SQL_WCHAR',
       SQL_DATA_TYPE_WVARCHAR: 'SQL_WVARCHAR',
       SQL_DATA_TYPE_WLONGVARCHAR: 'SQL_WLONGVARCHAR',
       SQL_DATA_TYPE_GUID: 'SQL_GUID',
       SQL_DATA_TYPE_UNKNOWN: 'SQL_UNKNOWN_TYPE'
       }
    if sqlTypes.has_key(type):
        return sqlTypes[type]
    else:
        return sqlTypes[SQL_DATA_TYPE_UNKNOWN]


def _translateConnectType(connectType):
    if connectType == SQL_CONNECT_TYPE_DATA_SOURCE:
        return 'DataSource'
    else:
        if connectType == SQL_CONNECT_TYPE_DRIVER:
            return 'Driver'
        if connectType == SQL_CONNECT_TYPE_SQLITE:
            return 'Sqlite'
        return 'Unknown'


def _outputChunk(output, msg, xml, base):
    results = ResultExecute()
    results.Demarshal(msg)
    xml.AddSubElementWithText('Command', results.queryString)
    xml.AddSubElementWithText('TotalColumns', '%u' % results.totalColumns)
    xml.AddSubElementWithText('StartRow', '%u' % results.startRow)
    xml.AddSubElementWithText('EndRow', '%u' % results.endRow)
    xml.AddSubElementWithText('CountRows', '%u' % results.rowsModified)
    xml.AddSubElementWithText('ConnectString', results.connectionString)
    if msg.PeekByKey(MSG_KEY_RESULT_COLUMNS) != None:
        colInfoSub = xml.AddSubElement('ColumnInfo')
        colMsg = msg.FindMessage(MSG_KEY_RESULT_COLUMNS)
        while colMsg.GetNumRetrieved() < colMsg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            colInfo = ResultColumnInfo()
            colInfo.Demarshal(colMsg)
            sub = colInfoSub.AddSubElement('Column')
            sub.AddSubElementWithText('Name', colInfo.name)
            sub.AddSubElementWithText('ColumnWidth', '%u' % colInfo.width)
            sub.AddSubElementWithText('DataType', _SQLTypeToStr(colInfo.dataType))
            if _SQL_TYPE_IS_BINARY(colInfo.dataType):
                sub.AddSubElementWithText('IsBinary', 'true')
            else:
                sub.AddSubElementWithText('IsBinary', 'false')
            if colInfo.isNullable:
                sub.AddSubElementWithText('IsNullable', 'true')
            else:
                sub.AddSubElementWithText('IsNullable', 'false')

    if msg.PeekByKey(MSG_KEY_RESULT_ROW) != None:
        dataSub = xml.AddSubElement('UncompressedData')
        while msg.GetNumRetrieved() < msg.GetCount():
            if mcl.CheckForStop():
                output.EndWithStatus(mcl.target.CALL_FAILED)
                return False
            rowMsg = msg.FindMessage(MSG_KEY_RESULT_ROW)
            sub = dataSub.AddSubElement('TableRow')
            while rowMsg.GetNumRetrieved() < rowMsg.GetCount():
                if mcl.CheckForStop():
                    output.EndWithStatus(mcl.target.CALL_FAILED)
                    return False
                cellMsg = rowMsg.FindMessage(MSG_KEY_RESULT_CELL)
                cellInfo = ResultCellInfo()
                cellInfo.Demarshal(cellMsg)
                sub2 = sub.AddSubElement('TableData')
                sub2.AddAttribute('valueIsBinary', 'false')
                if cellInfo.flags & RESULT_CELL_INFO_FLAG_IS_TRUNCATED:
                    sub2.AddAttribute('truncated', 'true')
                else:
                    sub2.AddAttribute('truncated', 'false')
                if cellInfo.flags & RESULT_CELL_INFO_FLAG_IS_NULL:
                    sub2.AddAttribute('null', 'true')
                else:
                    sub2.AddAttribute('null', 'false')
                    if cellInfo.dataType == SQL_DATA_TYPE_CHAR or cellInfo.dataType == SQL_DATA_TYPE_WCHAR:
                        outputText = cellMsg.FindString(MSG_KEY_RESULT_CELL_DATA)
                        try:
                            sub2.SetText(outputText)
                        except:
                            a = array.array('B')
                            a.fromstring(outputText)
                            sub2.SetTextAsData(a)
                            sub2.AddAttribute('bytes', '%u' % len(outputText))
                            sub2.AddAttribute('valueIsBinary', 'true')

                    elif cellInfo.dataType == SQL_DATA_TYPE_INTEGER:
                        longVal = cellMsg.FindS64(MSG_KEY_RESULT_CELL_DATA)
                        sub2.SetText('%d' % longVal)
                    elif cellInfo.dataType == SQL_DATA_TYPE_SMALLINT:
                        shortVal = cellMsg.FindS16(MSG_KEY_RESULT_CELL_DATA)
                        sub2.SetText('%d' % shortVal)
                    else:
                        hexData = cellMsg.FindData(MSG_KEY_RESULT_CELL_DATA)
                        sub2.SetTextAsData(hexData)
                        sub2.AddAttribute('bytes', '%u' % len(hexData))

    output.RecordXml(base)
    output.End()
    return True


def _outputDriverXml(parent, msg):
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        results = ResultDrivers()
        results.Demarshal(msg)
        sub = parent.AddSubElement('Driver')
        sub.AddSubElementWithText('Name', results.driver)
        sub.AddSubElementWithText('Attributes', results.attribute)
        if driverWarnings.has_key(results.driver.lower()):
            sub.AddSubElementWithText('Warning', driverWarnings[results.driver.lower()])

    return mcl.target.CALL_SUCCEEDED


def _outputSourcesXml(parent, msg):
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        results = ResultSource()
        results.Demarshal(msg)
        sub = parent.AddSubElement('DataSource')
        sub.AddSubElementWithText('Name', results.datasource)
        sub.AddSubElementWithText('Description', results.description)
        if driverWarnings.has_key(results.datasource.lower()):
            sub.AddSubElementWithText('Warning', driverWarnings[results.datasource.lower()])

    return mcl.target.CALL_SUCCEEDED


def _outputServersXml(parent, msg):
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        results = ResultServer()
        results.Demarshal(msg)
        parent.AddSubElementWithText('Server', results.server)

    return mcl.target.CALL_SUCCEEDED


def _outputConnectionXml(parent, msg, connStatus):
    import mcl
    import mcl.target
    while msg.GetNumRetrieved() < msg.GetCount():
        if mcl.CheckForStop():
            return mcl.target.CALL_FAILED
        results = ResultConnection()
        results.Demarshal(msg)
        parent.AddSubElementWithText('ConnectString', results.connectionString)
        parent.AddSubElementWithText('HandleId', '%u' % results.handleId)
        parent.AddSubElementWithText('Status', connStatus)
        parent.AddSubElementWithText('ConnectType', _translateConnectType(results.connectionType))
        if results.accessType == SQL_ACCESS_TYPE_READ_WRITE:
            parent.AddSubElementWithText('AccessType', 'READ/WRITE')
        elif results.accessType == SQL_ACCESS_TYPE_READ_ONLY:
            parent.AddSubElementWithText('AccessType', 'READ ONLY')
        else:
            parent.AddSubElementWithText('AccessType', 'UNKNOWN')
        if results.autoCommit:
            parent.AddSubElementWithText('AutoCommit', 'true')
        else:
            parent.AddSubElementWithText('AutoCommit', 'false')
        parent.AddTimeElement('CreateTime', results.createTime)
        parent.AddTimeElement('LastUseTime', results.lastUseTime)
        parent.AddTimeElement('MaxIdleDuration', results.maxIdleDuration)
        _recordHandleInformation(connStatus, results.handleId, results.connectionString, results.accessType, results.autoCommit, results.maxIdleDuration)

    return mcl.target.CALL_SUCCEEDED


def _recordHandleInformation(connStatus, handleId, connectionString, accessType, autoCommit, maxIdleDuration):
    try:
        import mcl.data.env
        if connStatus == 'Opened':
            mcl.data.env.SetValue('_SCRE_HANDLE_CONNECT_STR_%u' % handleId, connectionString, globalValue=True)
            if accessType == SQL_ACCESS_TYPE_READ_WRITE:
                mcl.data.env.SetValue('_SCRE_HANDLE_ACCESS_TYPE_%u' % handleId, 'READ/WRITE', globalValue=True)
            else:
                mcl.data.env.SetValue('_SCRE_HANDLE_ACCESS_TYPE_%u' % handleId, 'READ ONLY', globalValue=True)
            if autoCommit:
                mcl.data.env.SetValue('_SCRE_HANDLE_AUTO_COMMIT_%u' % handleId, 'true', globalValue=True)
            else:
                mcl.data.env.SetValue('_SCRE_HANDLE_AUTO_COMMIT_%u' % handleId, 'false', globalValue=True)
            mcl.data.env.SetValue('_SCRE_TIMEOUT_SECONDS_%u' % handleId, '%u' % maxIdleDuration.GetSeconds(), globalValue=True)
        else:
            try:
                mcl.data.env.DeleteValue('_SCRE_HANDLE_CONNECT_STR_%u' % handleId, globalValue=True)
            except:
                pass

            try:
                mcl.data.env.DeleteValue('_SCRE_HANDLE_ACCESS_TYPE_%u' % handleId, globalValue=True)
            except:
                pass

            try:
                mcl.data.env.DeleteValue('_SCRE_HANDLE_AUTO_COMMIT_%u' % handleId, globalValue=True)
            except:
                pass

            try:
                mcl.data.env.DeleteValue('_SCRE_TIMEOUT_SECONDS_%u' % handleId, globalValue=True)
            except:
                pass

    except:
        pass


if __name__ == '__main__':
    import sys
    try:
        namespace, InputFilename, OutputFilename = sys.argv[1:]
    except:
        print '%s <namespace> <input filename> <output filename>' % sys.argv[0]
        sys.exit(1)

    if DataHandlerMain(namespace, InputFilename, OutputFilename) != True:
        sys.exit(-1)