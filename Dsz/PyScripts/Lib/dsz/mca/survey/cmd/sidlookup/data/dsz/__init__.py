# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class SidLookup(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Sid = SidLookup.Sid(dsz.cmd.data.Get('Sid', dsz.TYPE_OBJECT)[0])
        except:
            self.Sid = None

        return

    class Sid(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_STRING)[0]
            except:
                self.id = None

            return


dsz.data.RegisterCommand('SidLookup', SidLookup)
SIDLOOKUP = SidLookup
sidlookup = SidLookup