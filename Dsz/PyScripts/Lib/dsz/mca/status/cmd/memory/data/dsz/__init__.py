# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Memory(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.MemoryItem = Memory.MemoryItem(dsz.cmd.data.Get('MemoryItem', dsz.TYPE_OBJECT)[0])
        except:
            self.MemoryItem = None

        return

    class MemoryItem(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.virtualAvail = dsz.cmd.data.ObjectGet(obj, 'virtualAvail', dsz.TYPE_INT)[0]
            except:
                self.virtualAvail = None

            try:
                self.physicalAvail = dsz.cmd.data.ObjectGet(obj, 'physicalAvail', dsz.TYPE_INT)[0]
            except:
                self.physicalAvail = None

            try:
                self.pageAvail = dsz.cmd.data.ObjectGet(obj, 'pageAvail', dsz.TYPE_INT)[0]
            except:
                self.pageAvail = None

            try:
                self.physicalLoad = dsz.cmd.data.ObjectGet(obj, 'physicalLoad', dsz.TYPE_INT)[0]
            except:
                self.physicalLoad = None

            try:
                self.pageTotal = dsz.cmd.data.ObjectGet(obj, 'pageTotal', dsz.TYPE_INT)[0]
            except:
                self.pageTotal = None

            try:
                self.virtualTotal = dsz.cmd.data.ObjectGet(obj, 'virtualTotal', dsz.TYPE_INT)[0]
            except:
                self.virtualTotal = None

            try:
                self.physicalTotal = dsz.cmd.data.ObjectGet(obj, 'physicalTotal', dsz.TYPE_INT)[0]
            except:
                self.physicalTotal = None

            return


dsz.data.RegisterCommand('Memory', Memory)
MEMORY = Memory
memory = Memory