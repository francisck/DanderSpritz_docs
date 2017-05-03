# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DllLoad(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.DllLoad = DllLoad.DllLoad(dsz.cmd.data.Get('DllLoad', dsz.TYPE_OBJECT)[0])
        except:
            self.DllLoad = None

        try:
            self.DllUnload = DllLoad.DllUnload(dsz.cmd.data.Get('DllUnload', dsz.TYPE_OBJECT)[0])
        except:
            self.DllUnload = None

        return

    class DllLoad(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.LoadAddress = dsz.cmd.data.ObjectGet(obj, 'LoadAddress', dsz.TYPE_INT)[0]
            except:
                self.LoadAddress = None

            return

    class DllUnload(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Unloaded = dsz.cmd.data.ObjectGet(obj, 'Unloaded', dsz.TYPE_BOOL)[0]
            except:
                self.Unloaded = None

            return


dsz.data.RegisterCommand('DllLoad', DllLoad)
DLLLOAD = DllLoad
dllload = DllLoad