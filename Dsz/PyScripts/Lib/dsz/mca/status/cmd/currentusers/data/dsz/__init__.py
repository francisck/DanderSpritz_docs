# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class CurrentUsers(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.User = CurrentUsers.User(dsz.cmd.data.Get('User', dsz.TYPE_OBJECT)[0])
        except:
            self.User = None

        return

    class User(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.SessionId = dsz.cmd.data.ObjectGet(obj, 'SessionId', dsz.TYPE_INT)[0]
            except:
                self.SessionId = None

            try:
                self.LoginPid = dsz.cmd.data.ObjectGet(obj, 'LoginPid', dsz.TYPE_INT)[0]
            except:
                self.LoginPid = None

            try:
                self.Host = dsz.cmd.data.ObjectGet(obj, 'Host', dsz.TYPE_STRING)[0]
            except:
                self.Host = None

            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Device = dsz.cmd.data.ObjectGet(obj, 'Device', dsz.TYPE_STRING)[0]
            except:
                self.Device = None

            return


dsz.data.RegisterCommand('CurrentUsers', CurrentUsers)
CURRENTUSERS = CurrentUsers
currentusers = CurrentUsers