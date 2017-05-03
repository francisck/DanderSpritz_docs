# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DiskSpace(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.drive = list()
        try:
            for x in dsz.cmd.data.Get('drive', dsz.TYPE_OBJECT):
                self.drive.append(DiskSpace.drive(x))

        except:
            pass

    class drive(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.low_diskspace = dsz.cmd.data.ObjectGet(obj, 'low_diskspace', dsz.TYPE_BOOL)[0]
            except:
                self.low_diskspace = None

            try:
                self.free = dsz.cmd.data.ObjectGet(obj, 'free', dsz.TYPE_INT)[0]
            except:
                self.free = None

            try:
                self.total = dsz.cmd.data.ObjectGet(obj, 'total', dsz.TYPE_INT)[0]
            except:
                self.total = None

            try:
                self.available = dsz.cmd.data.ObjectGet(obj, 'available', dsz.TYPE_INT)[0]
            except:
                self.available = None

            try:
                self.path = dsz.cmd.data.ObjectGet(obj, 'path', dsz.TYPE_STRING)[0]
            except:
                self.path = None

            return


dsz.data.RegisterCommand('DiskSpace', DiskSpace)
DISKSPACE = DiskSpace
diskspace = DiskSpace