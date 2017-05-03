# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class CpRpc(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Rpc = CpRpc.Rpc(dsz.cmd.data.Get('Rpc', dsz.TYPE_OBJECT)[0])
        except:
            self.Rpc = None

        try:
            self.Result = CpRpc.Result(dsz.cmd.data.Get('Result', dsz.TYPE_OBJECT)[0])
        except:
            self.Result = None

        return

    class Rpc(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            return

    class Result(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Id = dsz.cmd.data.ObjectGet(obj, 'Id', dsz.TYPE_INT)[0]
            except:
                self.Id = None

            try:
                self.GroupTag = dsz.cmd.data.ObjectGet(obj, 'GroupTag', dsz.TYPE_INT)[0]
            except:
                self.GroupTag = None

            try:
                self.Status = dsz.cmd.data.ObjectGet(obj, 'Status', dsz.TYPE_INT)[0]
            except:
                self.Status = None

            try:
                self.StatusString = dsz.cmd.data.ObjectGet(obj, 'StatusString', dsz.TYPE_STRING)[0]
            except:
                self.StatusString = None

            try:
                self.Address = dsz.cmd.data.ObjectGet(obj, 'Address', dsz.TYPE_STRING)[0]
            except:
                self.Address = None

            try:
                self.Output = CpRpc.Result.Output(dsz.cmd.data.ObjectGet(obj, 'Output', dsz.TYPE_OBJECT)[0])
            except:
                self.Output = None

            return

        class Output(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Length = dsz.cmd.data.ObjectGet(obj, 'Length', dsz.TYPE_INT)[0]
                except:
                    self.Length = None

                try:
                    self.Data = dsz.cmd.data.ObjectGet(obj, 'Data', dsz.TYPE_STRING)[0]
                except:
                    self.Data = None

                return


dsz.data.RegisterCommand('CpRpc', CpRpc)
CPRPC = CpRpc
cprpc = CpRpc