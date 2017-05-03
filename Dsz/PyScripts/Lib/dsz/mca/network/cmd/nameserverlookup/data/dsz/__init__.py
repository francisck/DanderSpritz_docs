# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class NameServerLookup(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = NameServerLookup.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.HostInfo = NameServerLookup.HostInfo(dsz.cmd.data.Get('HostInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.HostInfo = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.SearchParam = NameServerLookup.TaskingInfo.SearchParam(dsz.cmd.data.ObjectGet(obj, 'SearchParam', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchParam = None

            return

        class SearchParam(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                return

    class HostInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.info = dsz.cmd.data.ObjectGet(obj, 'info', dsz.TYPE_STRING)[0]
            except:
                self.info = None

            return


dsz.data.RegisterCommand('NameServerLookup', NameServerLookup)
NAMESERVERLOOKUP = NameServerLookup
nameserverlookup = NameServerLookup