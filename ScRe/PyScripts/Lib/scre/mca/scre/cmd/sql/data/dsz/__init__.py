# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import _dsz
import dsz
import dsz.data
import dsz.lp
import mcl.tasking
import sys
import Queue
import re
import xml
import xml.sax
import xml.sax.handler

class Sql(dsz.data.TaskReader):

    def __init__(self, cmd=None, id=None):
        dsz.data.TaskReader.__init__(self, cmd, id)
        self.ColumnInfoItem = None
        self.CommandInfo = None
        self.Connection = None
        self.DriversItem = None
        self.HandlesItem = None
        self.Query = None
        self.Row = dsz.data.IteratorBean(self, TableRow)
        self.ServersItem = None
        self.SourcesItem = None
        self.SqlErrorItem = []
        self.UncompressedDataItem = None
        self.__currentCell = None
        self.__currentCellNum = 0
        self.__currentColumn = None
        self.__currentDriver = None
        self.__currentError = None
        self.__currentHandle = None
        self.__currentRow = None
        self.__currentServer = None
        self.__currentSource = None
        self.__currentText = None
        for i in self:
            if self.ColumnInfoItem or self.Connection or self.DriversItem or self.HandlesItem or self.Query or self.ServersItem or self.SourcesItem or self.UncompressedDataItem:
                break

        return

    def startElement(self, name, attrs):
        dsz.data.TaskReader.startElement(self, name, attrs)
        try:
            self.__currentText = ''
            if name == 'Sql':
                self.__timestamp = attrs['lptimestamp']
            if not self.HandlesItem and name == 'Connection':
                self.Connection = ConnectionItem()
            elif self.Connection and name == 'MaxIdleDuration':
                self.Connection.MaxIdleDuration = MaxIdleDurationItem(self._GetValue(attrs, 'type'))
            elif not self.Query and name == 'Query':
                self.Query = QueryItem()
            elif self.Query and name == 'ColumnInfo':
                self.ColumnInfoItem = ColumnInfoItem()
            elif self.ColumnInfoItem and name == 'Column':
                self.__currentColumn = ColumnItem()
                self.ColumnInfoItem.ColumnItem.append(self.__currentColumn)
            elif self.Query and name == 'UncompressedData':
                self.UncompressedDataItem = UncompressedDataItem(self)
            elif name == 'TableRow':
                self.__currentRow = TableRow()
                self.currentItems.put(self.__currentRow)
                self.__currentCellNum = 0
            elif self.__currentRow and name == 'TableData':
                self.__currentCell = TableData(attrs)
                if self.ColumnInfoItem:
                    self.__currentRow.addCell(self.__currentCell, self.__currentCellNum, self.ColumnInfoItem.GetName(self.__currentCellNum))
                self.__currentCellNum += 1
            elif name == 'Servers':
                self.ServersItem = ServersItem()
            elif self.ServersItem and name == 'Server':
                self.__currentServer = Server()
                self.ServersItem.ServerItem.append(self.__currentServer)
            elif name == 'Error':
                self.__currentError = SqlErrorItem()
                self.SqlErrorItem.append(self.__currentError)
            elif name == 'Sources':
                self.SourcesItem = SourcesItem()
            elif self.SourcesItem and name == 'DataSource':
                self.__currentSource = Source()
                self.SourcesItem.SourceItem.append(self.__currentSource)
            elif name == 'Drivers':
                self.DriversItem = DriversItem()
            elif self.DriversItem and name == 'Driver':
                self.__currentDriver = Driver()
                self.DriversItem.DriverItem.append(self.__currentDriver)
            elif not self.Query and name == 'Tables':
                self.Query = QueryItem()
            elif name == 'Handles':
                self.HandlesItem = HandlesItem()
            elif self.HandlesItem and name == 'Connection':
                self.__currentHandle = Handle()
                self.HandlesItem.HandleItem.append(self.__currentHandle)
            elif self.__currentHandle and name == 'MaxIdleDuration':
                self.__currentHandle.MaxIdleDuration = MaxIdleDurationItem(self._GetValue(attrs, 'type'))
            elif not self.Query and name == 'Databases':
                self.Query = QueryItem()
            elif not self.Query and name == 'Columns':
                self.Query = QueryItem()
        except Exception as Err:
            dsz.ui.Echo('%s' % Err)

    def endElement(self, name):
        dsz.data.TaskReader.endElement(self, name)
        try:
            if self.Connection and name == 'ConnectString':
                self.Connection.ConnectionString = self.__currentText
            elif self.Connection and name == 'HandleId':
                self.Connection.HandleId = int(self.__currentText)
            elif self.Connection and name == 'ConnectType':
                self.Connection.ConnectionType = self.__currentText
            elif self.Connection and name == 'AutoCommit':
                self.Connection.AutoCommit = bool(self.__currentText)
            elif self.Connection and name == 'CreateTime':
                self.Connection.CreateTime = self.__currentText
            elif self.Connection and name == 'LastUseTime':
                self.Connection.LastUseTime = self.__currentText
            elif self.Connection and name == 'AccessType':
                self.Connection.AccessType = self.__currentText
            elif self.Connection and name == 'Status':
                self.Connection.Status = self.__currentText
            elif self.Connection and self.Connection.MaxIdleDuration and name == 'MaxIdleDuration':
                self.Connection.MaxIdleDuration.SetTime(self.__currentText)
            elif self.Query and name == 'Command':
                self.Query.Command = self.__currentText
            elif self.Query and name == 'TotalColumns':
                self.Query.TotalColumns = int(self.__currentText)
            elif self.Query and name == 'ConnectString':
                self.Query.ConnectString = self.__currentText
            elif self.__currentColumn and name == 'Name':
                self.__currentColumn.Name = self.__currentText
            elif self.__currentColumn and name == 'ColumnWidth':
                self.__currentColumn.ColumnWidth = int(self.__currentText)
            elif self.__currentColumn and name == 'DataType':
                self.__currentColumn.DataType = self.__currentText
            elif self.__currentColumn and name == 'IsBinary':
                self.__currentColumn.IsBinary = bool(self.__currentText)
            elif self.__currentColumn and name == 'DataType':
                self.__currentColumn.IsNunnable = bool(self.__currentText)
            elif self.__currentCell and name == 'TableData':
                self.__currentCell.Data = self.__currentText
            elif self.__currentServer and name == 'Server':
                self.__currentServer.Name = self.__currentText
            elif self.__currentError and name == 'ErrorCode':
                self.__currentError.ErrorCode = int(self.__currentText)
            elif self.__currentError and name == 'SqlState':
                self.__currentError.SqlState = self.__currentText
            elif self.__currentError and name == 'Message':
                self.__currentError.Message = self.__currentText
            elif self.__currentSource and name == 'Name':
                self.__currentSource.Name = self.__currentText
            elif self.__currentSource and name == 'Description':
                self.__currentSource.Description = self.__currentText
            elif self.__currentDriver and name == 'Name':
                self.__currentDriver.Name = self.__currentText
            elif self.__currentDriver and name == 'Attributes':
                self.__currentDriver.Attributes = self.__currentText
            elif self.__currentHandle and name == 'ConnectString':
                self.__currentHandle.ConnectionString = self.__currentText
            elif self.__currentHandle and name == 'HandleId':
                self.__currentHandle.HandleId = int(self.__currentText)
            elif self.__currentHandle and name == 'ConnectType':
                self.__currentHandle.ConnectionType = self.__currentText
            elif self.__currentHandle and name == 'AutoCommit':
                self.__currentHandle.AutoCommit = bool(self.__currentText)
            elif self.__currentHandle and name == 'CreateTime':
                self.__currentHandle.CreateTime = self.__currentText
            elif self.__currentHandle and name == 'LastUseTime':
                self.__currentHandle.LastUseTime = self.__currentText
            elif self.__currentHandle and name == 'AccessType':
                self.__currentHandle.AccessType = self.__currentText
            elif self.__currentHandle and name == 'Status':
                self.__currentHandle.Status = self.__currentText
            elif self.__currentHandle and self.__currentHandle.MaxIdleDuration and name == 'MaxIdleDuration':
                self.__currentHandle.MaxIdleDuration.SetTime(self.__currentText)
        except Exception as Err:
            dsz.ui.Echo('%s' % Err)

        self.__currentText = ''

    def characters(self, content):
        dsz.data.TaskReader.characters(self, content)
        content = ''.join(content.encode('utf-8'))
        if self.__currentText == None:
            self.__currentText = content
        else:
            self.__currentText += content
        return


class ColumnInfoItem(dsz.data.DataBean):

    def __init__(self):
        self.ColumnItem = []

    def GetName(self, index):
        if index < 0 or index >= len(self.ColumnItem):
            return None
        else:
            return self.ColumnItem[index].Name


class ColumnItem(dsz.data.DataBean):

    def __init__(self):
        self.Name = None
        self.ColumnWidth = None
        self.DataType = None
        self.IsBinary = None
        self.IsNullable = None
        return


class CommandInfoItem(dsz.data.DataBean):

    def __init__(self):
        self.Action = None
        self.ConnectString = None
        self.TableName = None
        self.QueryString = None
        self.File = None
        self.MaxColumnSize = None
        self.ConsoleOutput = None
        return


class ConnectionItem(dsz.data.DataBean):

    def __init__(self):
        self.ConnectionString = None
        self.ConnectionType = None
        self.HandleId = None
        self.AutoCommit = None
        self.CreateTime = None
        self.LastUseTime = None
        self.Status = None
        self.AccessType = None
        self.MaxIdleDuration = None
        return


class DriversItem(dsz.data.DataBean):

    def __init__(self):
        self.DriverItem = []


class Driver(dsz.data.DataBean):

    def __init__(self):
        self.Name = None
        self.Attributes = None
        return


class HandlesItem(dsz.data.DataBean):

    def __init__(self):
        self.HandleItem = []


class Handle(dsz.data.DataBean):

    def __init__(self):
        self.AutoCommit = None
        self.HandleId = None
        self.CreateTime = None
        self.ConnectionType = None
        self.ConnectionString = None
        self.AccessType = None
        self.LastUseTime = None
        self.MaxIdleDuration = None
        return


class MaxIdleDurationItem(dsz.data.DataBean):

    def __init__(self, type):
        self.Days = None
        self.Hours = None
        self.Minutes = None
        self.Seconds = None
        self.Type = type
        return

    def SetTime(self, time):
        regex = re.compile('(?P<sign>-?)P(?:(?P<years>\\d+)Y)?(?:(?P<months>\\d+)M)?(?:(?P<days>\\d+)D)?(?:T(?:(?P<hours>\\d+)H)?(?:(?P<minutes>\\d+)M)(?:(?P<seconds>\\d)+.(?P<nanos>\\d+)S)?)?.*')
        duration = regex.match(time).groupdict(0)
        self.Days = int(duration['days']) + int(duration['months']) * 30 + int(duration['years']) * 265
        self.Hours = int(duration['hours'])
        self.Minutes = int(duration['minutes'])
        self.Seconds = int(duration['seconds'])
        self.Nanoseconds = int(duration['nanos'])


class QueryItem(dsz.data.DataBean):

    def __init__(self):
        self.Command = None
        self.TotalColumns = None
        self.ConnectString = None
        return


class ServersItem(dsz.data.DataBean):

    def __init__(self):
        self.ServerItem = []


class Server(dsz.data.DataBean):

    def __init__(self):
        self.Name = None
        return


class SourcesItem(dsz.data.DataBean):

    def __init__(self):
        self.SourceItem = []


class Source(dsz.data.DataBean):

    def __init__(self):
        self.Name = None
        self.Description = None
        return


class SqlErrorItem(dsz.data.DataBean):

    def __init__(self):
        self.ErrorCode = None
        self.SqlState = None
        self.Message = None
        return


class TableData(dsz.data.DataBean):

    def __init__(self, attributes):
        try:
            self.IsNull = bool(''.join(attributes.getValue(unicode('null')).encode('utf-8')))
        except Exception as Err:
            self.IsNull = False

        try:
            self.IsTruncated = bool(''.join(attributes.getValue(unicode('truncated')).encode('utf-8')))
        except Exception as Err:
            self.IsTruncated = False

        try:
            self.Bytes = int(''.join(attributes.getValue(unicode('bytes')).encode('utf-8')))
        except Exception as Err:
            self.Bytes = None

        try:
            self.IsBinary = bool(''.join(attributes.getValue(unicode('valueIsBinary')).encode('utf-8')))
        except Exception as Err:
            self.IsBinary = True

        return


class TableRow(dsz.data.DataBean):

    def __init__(self):
        self.TableData = []
        self.Cells = dsz.data.DataBean()

    def addCell(self, cell, index, name):
        while len(self.TableData) <= index:
            self.TableData.append(None)

        self.TableData[index] = cell
        if name:
            self.Cells.__setattr__(name, cell)
        return


class UncompressedDataItem(dsz.data.DataBean):

    def __init__(self, SqlObject):
        self.TableRow = dsz.data.IteratorBean(SqlObject, TableRow)


dsz.data.RegisterCommand('Sql', Sql, True)
SQL = Sql
sql = Sql