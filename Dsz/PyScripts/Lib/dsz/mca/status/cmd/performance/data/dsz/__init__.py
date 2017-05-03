# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Performance(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Performance.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.Performance = Performance.Performance(dsz.cmd.data.Get('Performance', dsz.TYPE_OBJECT)[0])
        except:
            self.Performance = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = Performance.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            try:
                self.SearchParam = Performance.TaskingInfo.SearchParam(dsz.cmd.data.ObjectGet(obj, 'SearchParam', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchParam = None

            return

        class Target(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.local = dsz.cmd.data.ObjectGet(obj, 'local', dsz.TYPE_BOOL)[0]
                except:
                    self.local = None

                try:
                    self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
                except:
                    self.location = None

                return

        class SearchParam(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class Performance(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.perfCount = dsz.cmd.data.ObjectGet(obj, 'perfCount', dsz.TYPE_INT)[0]
            except:
                self.perfCount = None

            try:
                self.perfCountsPerSecond = dsz.cmd.data.ObjectGet(obj, 'perfCountsPerSecond', dsz.TYPE_INT)[0]
            except:
                self.perfCountsPerSecond = None

            try:
                self.perfTime100nSec = dsz.cmd.data.ObjectGet(obj, 'perfTime100nSec', dsz.TYPE_INT)[0]
            except:
                self.perfTime100nSec = None

            try:
                self.systemName = dsz.cmd.data.ObjectGet(obj, 'systemName', dsz.TYPE_STRING)[0]
            except:
                self.systemName = None

            self.object = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'object', dsz.TYPE_OBJECT):
                    self.object.append(Performance.Performance.object(x))

            except:
                pass

            return

        class object(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.nameIndex = dsz.cmd.data.ObjectGet(obj, 'nameIndex', dsz.TYPE_INT)[0]
                except:
                    self.nameIndex = None

                try:
                    self.helpIndex = dsz.cmd.data.ObjectGet(obj, 'helpIndex', dsz.TYPE_INT)[0]
                except:
                    self.helpIndex = None

                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                try:
                    self.help = dsz.cmd.data.ObjectGet(obj, 'help', dsz.TYPE_STRING)[0]
                except:
                    self.help = None

                self.Counter = list()
                try:
                    for x in dsz.cmd.data.ObjectGet(obj, 'Counter', dsz.TYPE_OBJECT):
                        self.Counter.append(Performance.Performance.object.Counter(x))

                except:
                    pass

                return

            class Counter(dsz.data.DataBean):

                def __init__(self, obj):
                    try:
                        self.nameIndex = dsz.cmd.data.ObjectGet(obj, 'nameIndex', dsz.TYPE_INT)[0]
                    except:
                        self.nameIndex = None

                    try:
                        self.helpIndex = dsz.cmd.data.ObjectGet(obj, 'helpIndex', dsz.TYPE_INT)[0]
                    except:
                        self.helpIndex = None

                    try:
                        self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_INT)[0]
                    except:
                        self.type = None

                    try:
                        self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                    except:
                        self.name = None

                    try:
                        self.help = dsz.cmd.data.ObjectGet(obj, 'help', dsz.TYPE_STRING)[0]
                    except:
                        self.help = None

                    try:
                        self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                    except:
                        self.value = None

                    try:
                        self.valueType = dsz.cmd.data.ObjectGet(obj, 'valueType', dsz.TYPE_STRING)[0]
                    except:
                        self.valueType = None

                    try:
                        self.valueSuffix = dsz.cmd.data.ObjectGet(obj, 'valueSuffix', dsz.TYPE_STRING)[0]
                    except:
                        self.valueSuffix = None

                    return


dsz.data.RegisterCommand('Performance', Performance)
PERFORMANCE = Performance
performance = Performance