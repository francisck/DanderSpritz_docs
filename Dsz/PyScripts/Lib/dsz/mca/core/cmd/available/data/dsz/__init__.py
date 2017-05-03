# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Available(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.LpModule = Available.LpModule(dsz.cmd.data.Get('LpModule', dsz.TYPE_OBJECT)[0])
        except:
            self.LpModule = None

        try:
            self.LocalDependencies = Available.LocalDependencies(dsz.cmd.data.Get('LocalDependencies', dsz.TYPE_OBJECT)[0])
        except:
            self.LocalDependencies = None

        try:
            self.RemoteDependencies = Available.RemoteDependencies(dsz.cmd.data.Get('RemoteDependencies', dsz.TYPE_OBJECT)[0])
        except:
            self.RemoteDependencies = None

        return

    class LpModule(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            return

    class LocalDependencies(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
            except:
                self.Address = None

            self.ModuleInfo = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'ModuleInfo', dsz.TYPE_OBJECT):
                    self.ModuleInfo.append(Available.LocalDependencies.ModuleInfo(x))

            except:
                pass

            return

        class ModuleInfo(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
                except:
                    self.Id = None

                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                return

    class RemoteDependencies(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
            except:
                self.Address = None

            self.ModuleInfo = list()
            try:
                for x in dsz.cmd.data.ObjectGet(obj, 'ModuleInfo', dsz.TYPE_OBJECT):
                    self.ModuleInfo.append(Available.RemoteDependencies.ModuleInfo(x))

            except:
                pass

            return

        class ModuleInfo(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
                except:
                    self.Id = None

                try:
                    self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
                except:
                    self.Name = None

                return


dsz.data.RegisterCommand('Available', Available)
AVAILABLE = Available
available = Available