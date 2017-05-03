# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Strings(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Strings.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.Strings = Strings.Strings(dsz.cmd.data.Get('Strings', dsz.TYPE_OBJECT)[0])
        except:
            self.Strings = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.SearchPath = Strings.TaskingInfo.SearchPath(dsz.cmd.data.ObjectGet(obj, 'SearchPath', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchPath = None

            return

        class SearchPath(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class Strings(dsz.data.DataBean):

        def __init__(self, obj):
            self.String = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'String', dsz.TYPE_OBJECT):
                    self.String.append(Strings.Strings.String(x))

            except:
                pass

        class String(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.offset = dsz.cmd.data.ObjectGet(obj, 'offset', dsz.TYPE_INT)[0]
                except:
                    self.offset = None

                try:
                    self.string = dsz.cmd.data.ObjectGet(obj, 'string', dsz.TYPE_STRING)[0]
                except:
                    self.string = None

                return


dsz.data.RegisterCommand('Strings', Strings)
STRINGS = Strings
strings = Strings