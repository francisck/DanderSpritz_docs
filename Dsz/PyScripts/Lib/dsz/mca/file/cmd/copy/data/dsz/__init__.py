# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Copy(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.CopyResults = Copy.CopyResults(dsz.cmd.data.Get('CopyResults', dsz.TYPE_OBJECT)[0])
        except:
            self.CopyResults = None

        return

    class CopyResults(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Destination = dsz.cmd.data.ObjectGet(obj, 'Destination', dsz.TYPE_STRING)[0]
            except:
                self.Destination = None

            try:
                self.Source = dsz.cmd.data.ObjectGet(obj, 'Source', dsz.TYPE_STRING)[0]
            except:
                self.Source = None

            return


dsz.data.RegisterCommand('Copy', Copy)
COPY = Copy
copy = Copy