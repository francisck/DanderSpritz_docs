# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Environment(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Environment.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.Environment = Environment.Environment(dsz.cmd.data.Get('Environment', dsz.TYPE_OBJECT)[0])
        except:
            self.Environment = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            self.SearchMask = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'SearchMask', dsz.TYPE_OBJECT):
                    self.SearchMask.append(Environment.TaskingInfo.SearchMask(x))

            except:
                pass

            try:
                self.Recursive = dsz.cmd.data.ObjectGet(obj, 'Recursive', dsz.TYPE_BOOL)[0]
            except:
                self.Recursive = None

            return

        class SearchMask(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class Environment(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Action = dsz.cmd.data.ObjectGet(obj, 'Action', dsz.TYPE_STRING)[0]
            except:
                self.Action = None

            self.Value = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_OBJECT):
                    self.Value.append(Environment.Environment.Value(x))

            except:
                pass

            return

        class Value(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                except:
                    self.Value = None

                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                return


dsz.data.RegisterCommand('Environment', Environment)
ENVIRONMENT = Environment
environment = Environment