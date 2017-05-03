# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Grep(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Grep.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.File = Grep.File(dsz.cmd.data.Get('File', dsz.TYPE_OBJECT)[0])
        except:
            self.File = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.TaskType = Grep.TaskingInfo.TaskType(dsz.cmd.data.ObjectGet(obj, 'TaskType', dsz.TYPE_OBJECT)[0])
            except:
                self.TaskType = None

            self.SearchParam = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'SearchParam', dsz.TYPE_OBJECT):
                    self.SearchParam.append(Grep.TaskingInfo.SearchParam(x))

            except:
                pass

            try:
                self.SearchMaxMatches = Grep.TaskingInfo.SearchMaxMatches(dsz.cmd.data.ObjectGet(obj, 'SearchMaxMatches', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchMaxMatches = None

            try:
                self.SearchPath = Grep.TaskingInfo.SearchPath(dsz.cmd.data.ObjectGet(obj, 'SearchPath', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchPath = None

            try:
                self.SearchMask = Grep.TaskingInfo.SearchMask(dsz.cmd.data.ObjectGet(obj, 'SearchMask', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchMask = None

            return

        class TaskType(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class SearchParam(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class SearchMaxMatches(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_INT)[0]
                except:
                    self.value = None

                return

        class SearchPath(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

        class SearchMask(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class File(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.numlines = dsz.cmd.data.ObjectGet(obj, 'numlines', dsz.TYPE_INT)[0]
            except:
                self.numlines = None

            try:
                self.location = dsz.cmd.data.ObjectGet(obj, 'location', dsz.TYPE_STRING)[0]
            except:
                self.location = None

            self.line = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'line', dsz.TYPE_OBJECT):
                    self.line.append(Grep.File.line(x))

            except:
                pass

            return

        class line(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.position = dsz.cmd.data.ObjectGet(obj, 'position', dsz.TYPE_INT)[0]
                except:
                    self.position = None

                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return


dsz.data.RegisterCommand('Grep', Grep)
GREP = Grep
grep = Grep