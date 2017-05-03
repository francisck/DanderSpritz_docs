# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class RegistryQuery(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.TaskingInfo = RegistryQuery.TaskingInfo(dsz.cmd.data.Get('TaskingInfo', dsz.TYPE_OBJECT)[0])
        except:
            self.TaskingInfo = None

        self.Key = list()
        try:
            for x in dsz.cmd.data.Get('Key', dsz.TYPE_OBJECT):
                self.Key.append(RegistryQuery.Key(x))

        except:
            pass

        return

    class TaskingInfo(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.recursive = dsz.cmd.data.ObjectGet(obj, 'recursive', dsz.TYPE_BOOL)[0]
            except:
                self.recursive = None

            try:
                self.Target = RegistryQuery.TaskingInfo.Target(dsz.cmd.data.ObjectGet(obj, 'Target', dsz.TYPE_OBJECT)[0])
            except:
                self.Target = None

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

    class Key(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.updateDate = dsz.cmd.data.ObjectGet(obj, 'updateDate', dsz.TYPE_STRING)[0]
            except:
                self.updateDate = None

            try:
                self.updateTime = dsz.cmd.data.ObjectGet(obj, 'updateTime', dsz.TYPE_STRING)[0]
            except:
                self.updateTime = None

            try:
                self.hive = dsz.cmd.data.ObjectGet(obj, 'hive', dsz.TYPE_STRING)[0]
            except:
                self.hive = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.keyClass = dsz.cmd.data.ObjectGet(obj, 'keyClass', dsz.TYPE_STRING)[0]
            except:
                self.keyClass = None

            self.Subkey = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Subkey', dsz.TYPE_OBJECT):
                    self.Subkey.append(RegistryQuery.Key.Subkey(x))

            except:
                pass

            self.Value = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_OBJECT):
                    self.Value.append(RegistryQuery.Key.Value(x))

            except:
                pass

            return

        class Subkey(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                try:
                    self.updateDate = dsz.cmd.data.ObjectGet(obj, 'updateDate', dsz.TYPE_STRING)[0]
                except:
                    self.updateDate = None

                try:
                    self.updateTime = dsz.cmd.data.ObjectGet(obj, 'updateTime', dsz.TYPE_STRING)[0]
                except:
                    self.updateTime = None

                return

        class Value(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.typeValue = dsz.cmd.data.ObjectGet(obj, 'typeValue', dsz.TYPE_INT)[0]
                except:
                    self.typeValue = None

                try:
                    self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
                except:
                    self.value = None

                try:
                    self.type = dsz.cmd.data.ObjectGet(obj, 'type', dsz.TYPE_STRING)[0]
                except:
                    self.type = None

                try:
                    self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
                except:
                    self.name = None

                return


dsz.data.RegisterCommand('RegistryQuery', RegistryQuery)
REGISTRYQUERY = RegistryQuery
registryquery = RegistryQuery