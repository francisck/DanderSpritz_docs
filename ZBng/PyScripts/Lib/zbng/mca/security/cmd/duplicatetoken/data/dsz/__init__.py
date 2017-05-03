# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class DuplicateToken(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.Token = DuplicateToken.Token(dsz.cmd.data.Get('Token', dsz.TYPE_OBJECT)[0])
        except:
            self.Token = None

        self.Process = list()
        try:
            for x in dsz.cmd.data.Get('Process', dsz.TYPE_OBJECT):
                self.Process.append(DuplicateToken.Process(x))

        except:
            pass

        return

    class Token(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
            except:
                self.value = None

            try:
                self.value = dsz.cmd.data.ObjectGet(obj, 'value', dsz.TYPE_STRING)[0]
            except:
                self.value = None

            return

    class Process(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.id = dsz.cmd.data.ObjectGet(obj, 'id', dsz.TYPE_INT)[0]
            except:
                self.id = None

            try:
                self.name = dsz.cmd.data.ObjectGet(obj, 'name', dsz.TYPE_STRING)[0]
            except:
                self.name = None

            try:
                self.user = dsz.cmd.data.ObjectGet(obj, 'user', dsz.TYPE_STRING)[0]
            except:
                self.user = None

            return


dsz.data.RegisterCommand('DuplicateToken', DuplicateToken)
DUPLICATETOKEN = DuplicateToken
duplicatetoken = DuplicateToken