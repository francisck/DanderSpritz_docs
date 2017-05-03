# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class RegistryHive(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = RegistryHive.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.target = RegistryHive.TaskingInfo.target(dsz.cmd.data.ObjectGet(obj, 'target', dsz.TYPE_OBJECT)[0])
            except:
                self.target = None

            try:
                self.hive = RegistryHive.TaskingInfo.hive(dsz.cmd.data.ObjectGet(obj, 'hive', dsz.TYPE_OBJECT)[0])
            except:
                self.hive = None

            return

        class target(dsz.data.DataBean):

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

        class hive(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.hive = dsz.cmd.data.ObjectGet(obj, 'hive', dsz.TYPE_STRING)[0]
                except:
                    self.hive = None

                try:
                    self.srcfile = dsz.cmd.data.ObjectGet(obj, 'srcfile', dsz.TYPE_STRING)[0]
                except:
                    self.srcfile = None

                try:
                    self.key = dsz.cmd.data.ObjectGet(obj, 'key', dsz.TYPE_STRING)[0]
                except:
                    self.key = None

                return


dsz.data.RegisterCommand('RegistryHive', RegistryHive)
REGISTRYHIVE = RegistryHive
registryhive = RegistryHive