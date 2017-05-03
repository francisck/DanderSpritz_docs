# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class EventLogQuery(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.taskinginfo = EventLogQuery.taskinginfo(dsz.cmd.data.Get('taskinginfo', dsz.TYPE_OBJECT)[0])
        except:
            self.taskinginfo = None

        self.EventLog = list()
        try:
            for x in dsz.cmd.data.Get('EventLog', dsz.TYPE_OBJECT):
                self.EventLog.append(EventLogQuery.EventLog(x))

        except:
            pass

        self.Record = list()
        try:
            for x in dsz.cmd.data.Get('Record', dsz.TYPE_OBJECT):
                self.Record.append(EventLogQuery.Record(x))

        except:
            pass

        return

    class taskinginfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Searchpath = EventLogQuery.taskinginfo.Searchpath(dsz.cmd.data.ObjectGet(obj, 'Searchpath', dsz.TYPE_OBJECT)[0])
            except:
                self.Searchpath = None

            try:
                self.target = EventLogQuery.taskinginfo.target(dsz.cmd.data.ObjectGet(obj, 'target', dsz.TYPE_OBJECT)[0])
            except:
                self.target = None

            return

        class Searchpath(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class target(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_STRING)[0]
                except:
                    self.local = None

                try:
                    self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
                except:
                    self.location = None

                return

    class EventLog(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.MostRecentRecordNum = dsz.cmd.data.ObjectGet(obj, 'MostRecentRecordNum', dsz.TYPE_INT)[0]
            except:
                self.MostRecentRecordNum = None

            try:
                self.NumRecords = dsz.cmd.data.ObjectGet(obj, 'NumRecords', dsz.TYPE_INT)[0]
            except:
                self.NumRecords = None

            try:
                self.OldestRecordNum = dsz.cmd.data.ObjectGet(obj, 'OldestRecordNum', dsz.TYPE_INT)[0]
            except:
                self.OldestRecordNum = None

            try:
                self.MostRecentRecordNum = dsz.cmd.data.ObjectGet(obj, 'MostRecentRecordNum', dsz.TYPE_INT)[0]
            except:
                self.MostRecentRecordNum = None

            try:
                self.LastModifiedDate = dsz.cmd.data.ObjectGet(obj, 'LastModifiedDate', dsz.TYPE_STRING)[0]
            except:
                self.LastModifiedDate = None

            try:
                self.LastModifiedTime = dsz.cmd.data.ObjectGet(obj, 'LastModifiedTime', dsz.TYPE_STRING)[0]
            except:
                self.LastModifiedTime = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            return

    class Record(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Number = dsz.cmd.data.ObjectGet(obj, 'Number', dsz.TYPE_INT)[0]
            except:
                self.Number = None

            try:
                self.ProcessId = dsz.cmd.data.ObjectGet(obj, 'ProcessId', dsz.TYPE_INT)[0]
            except:
                self.ProcessId = None

            try:
                self.ThreadId = dsz.cmd.data.ObjectGet(obj, 'ThreadId', dsz.TYPE_INT)[0]
            except:
                self.ThreadId = None

            try:
                self.DateWritten = dsz.cmd.data.ObjectGet(obj, 'DateWritten', dsz.TYPE_STRING)[0]
            except:
                self.DateWritten = None

            try:
                self.TimeWritten = dsz.cmd.data.ObjectGet(obj, 'TimeWritten', dsz.TYPE_STRING)[0]
            except:
                self.TimeWritten = None

            try:
                self.User = dsz.cmd.data.ObjectGet(obj, 'User', dsz.TYPE_STRING)[0]
            except:
                self.User = None

            try:
                self.Computer = dsz.cmd.data.ObjectGet(obj, 'Computer', dsz.TYPE_STRING)[0]
            except:
                self.Computer = None

            try:
                self.Source = dsz.cmd.data.ObjectGet(obj, 'Source', dsz.TYPE_STRING)[0]
            except:
                self.Source = None

            try:
                self.EventType = dsz.cmd.data.ObjectGet(obj, 'EventType', dsz.TYPE_STRING)[0]
            except:
                self.EventType = None

            self.String = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'String', dsz.TYPE_OBJECT):
                    self.String.append(EventLogQuery.Record.String(x))

            except:
                pass

            self.Data = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_OBJECT):
                    self.Data.append(EventLogQuery.Record.Data(x))

            except:
                pass

            return

        class String(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                except:
                    self.Value = None

                return

        class Data(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                except:
                    self.Value = None

                return


dsz.data.RegisterCommand('EventLogQuery', EventLogQuery)
EVENTLOGQUERY = EventLogQuery
eventlogquery = EventLogQuery