# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class Cd(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.CurrentDirectory = Cd.CurrentDirectory(dsz.cmd.data.Get('CurrentDirectory', dsz.TYPE_OBJECT)[0])
        except:
            self.CurrentDirectory = None

        return

    class CurrentDirectory(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.path = dsz.cmd.data.ObjectGet(obj, 'path', dsz.TYPE_STRING)[0]
            except:
                self.path = None

            try:
                self.Virtual = dsz.cmd.data.ObjectGet(obj, 'Virtual', dsz.TYPE_BOOL)[0]
            except:
                self.Virtual = None

            return


dsz.data.RegisterCommand('Cd', Cd)
CD = Cd
cd = Cd

class Pwd(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        try:
            self.CurrentDirectory = Pwd.CurrentDirectory(dsz.cmd.data.Get('CurrentDirectory', dsz.TYPE_OBJECT)[0])
        except:
            self.CurrentDirectory = None

        return

    class CurrentDirectory(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.path = dsz.cmd.data.ObjectGet(obj, 'path', dsz.TYPE_STRING)[0]
            except:
                self.path = None

            try:
                self.Virtual = dsz.cmd.data.ObjectGet(obj, 'Virtual', dsz.TYPE_BOOL)[0]
            except:
                self.Virtual = None

            return


dsz.data.RegisterCommand('Pwd', Pwd)
PWD = Pwd
pwd = Pwd